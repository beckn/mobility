"""
generate_examples.py
=====================

Generates every ride-hailing example JSON from ``on_discover`` through
``on_support`` for all transport-mode use cases defined in ``mobility_lib``.

Output layout (one file per use case, grouped by use case via the filename):

    example-jsons/<action>/requests/post.request.<use_case>.json

The single ``Contract`` object is threaded through the whole contracting +
performance + post-performance lifecycle, mutating exactly as the beckn spec
prescribes:

    on_discover -> catalog of offers linked to TripRequest resources
    select      -> DRAFT contract, commitments only (NO id, NO PII, NO price)
    on_select   -> PN assigns Contract id + priced Consideration (correct fare object)
    init        -> + billing Participant + DRAFT Settlement (payment intent)
    on_init     -> finalised fare + provider Participant
    confirm     -> Settlement COMMITTED (payment reference)
    on_confirm  -> Contract ACTIVE, Commitment ACTIVE, Settlement COMPLETE, Performance
    status/on_status -> performance progress
    track/on_track   -> Tracking handle (ACTIVE for on-road modes, INACTIVE otherwise)
    update/on_update -> contract mutation (extra stop) with recomputed fare
    cancel/on_cancel -> Contract CANCELLED + refund Settlement
    rate/on_rate     -> RatingInputs for provider / ride
    support/on_support -> Support request + resolved channels & ticket

Run:  python3 generate_examples.py
"""

import json
import os

import mobility_lib as m
from mobility_lib import ctx, descriptor, resource_ids, schema_context_for

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "example-jsons"))

# Catalog / offer validity windows.
VALID = {"startDate": "2026-07-06T00:00:00Z", "endDate": "2026-07-06T23:59:59Z"}
OFFER_VALID = {"startDate": "2026-07-06T09:00:00Z", "endDate": "2026-07-06T10:00:00Z"}


# --------------------------------------------------------------------------- #
# Shared party / settlement builders                                          #
# --------------------------------------------------------------------------- #
def consumer():
    """
    Rider Participant, typed as a beckn Passenger (not schema.org Person).
    Optimal ignorance: at init the rider shares only a contact name + phone (needed
    so the driver can reach them) - NOT a home postal address (a ride is not a
    delivery, so it is never required).
    """
    return {"id": "consumer-001", "descriptor": descriptor("Rider"),
            "participantAttributes": {"@context": ctx.PASSENGER, "@type": "Passenger",
                "passengerId": "psg-001", "passengerType": "ADULT",
                "person": {"@context": ctx.PERSON, "@type": "Person", "id": "person-001",
                           "name": "Alex Rider", "telephone": "+31 6 1234 5678"}}}

def provider_participant(uc):
    pid, name = uc["provider"]
    # Typed as a beckn Provider (not schema.org Organization).
    return {"id": pid, "descriptor": descriptor(name),
            "participantAttributes": {"@context": ctx.PROVIDER, "@type": "Provider"}}

def settlement(uc, status, value=None, note=None):
    # settlementAttributes is a beckn SettlementTerm (amount, where money is remitted,
    # accepted methods). Settlement.status (DRAFT/COMMITTED/COMPLETE) is the lifecycle;
    # SettlementTerm.settlementStatus (PENDING/COMPLETE) mirrors it at term level.
    amount = uc["total"] if value is None else value
    a = {"@context": ctx.SETTLE, "@type": "SettlementTerm",
         "amount": {"currency": "EUR", "value": amount},
         "settlementStatus": "COMPLETE" if status == "COMPLETE" else "PENDING",
         "payTo": {"paymentUrl": "https://pay.example.com/" + uc["con_id"]},
         "acceptedPaymentMethods": ["BANK_TRANSFER"]}
    if note: a["descriptor"] = descriptor(note)
    return {"id": "set-" + uc["con_id"], "considerationId": uc["con_id"],
            "status": status, "settlementAttributes": a}


# --------------------------------------------------------------------------- #
# Contract building blocks                                                     #
# --------------------------------------------------------------------------- #
def offer_stub(uc):
    """Offer as embedded in a Commitment: requires id + resourceIds."""
    o = {"id": uc["offer_id"], "resourceIds": resource_ids(uc),
         "offerAttributes": uc["offer_attrs"]}
    return o

def commitment(uc, code):
    """A Commitment: status + resources (id+quantity) + offer (id+resourceIds)."""
    names = {"DRAFT": "Draft commitment", "ACTIVE": "Active commitment", "CLOSED": "Closed commitment"}
    # From select onward a booking exists, so precise pickup/drop are disclosed.
    c = {"id": "cmt-" + uc["con_id"],
         "status": {"descriptor": descriptor(names[code], code=code)},
         "resources": m.build_resources(uc["legs"], coarse=False),
         "offer": offer_stub(uc)}
    if uc["commit_attrs"]:
        c["commitmentAttributes"] = uc["commit_attrs"]
    return c

def consideration(uc, status_code, status_name, fare=None):
    """A priced Consideration extended by the mode's correct fare object."""
    return {"id": uc["con_id"],
            "status": descriptor(status_name, code=status_code),
            "considerationAttributes": fare if fare is not None else uc["fare"]()}

def contract(uc, *, cid=None, status, commit_code, consideration_list=None,
             participants=None, settlements=None, performance=None):
    names = {"DRAFT": "Draft contract", "ACTIVE": "Active contract",
             "CANCELLED": "Cancelled contract", "COMPLETE": "Completed contract"}
    c = {}
    if cid: c["id"] = cid
    c["descriptor"] = uc["cdesc"]
    c["status"] = descriptor(names[status], code=status)
    c["commitments"] = [commitment(uc, commit_code)]
    if consideration_list is not None: c["consideration"] = consideration_list
    if participants is not None:        c["participants"] = participants
    if settlements is not None:         c["settlements"] = settlements
    if performance is not None:         c["performance"] = performance
    return c


# --------------------------------------------------------------------------- #
# on_discover (catalog)                                                        #
# --------------------------------------------------------------------------- #
def provider_block(uc):
    pid, name = uc["provider"]
    return {"id": pid, "descriptor": descriptor(name, name + " mobility services"),
            "availableAt": [m.location(m.CENTRAAL, "Stationsplein", "1012 AB")]}

def build_on_discover(uc):
    # Discovery: coarse-area resources (optimal ignorance) + a headline TARIFF /
    # estimate only. The itemised breakup is NOT shown here - it appears once a
    # selection exists (on_select) and is recalculated at completion.
    offer = {"id": uc["offer_id"], "descriptor": descriptor(uc["cdesc"]["name"], "Offer"),
             "resourceIds": resource_ids(uc), "offerAttributes": uc["offer_attrs"],
             "considerations": [consideration(uc, "PRICE_ESTIMATE", "Fare estimate", fare=uc["tariff"]())],
             "validity": OFFER_VALID}
    catalog = {"id": "cat-" + uc["name"], "descriptor": uc["cdesc"],
               "provider": provider_block(uc), "isActive": True,
               "resources": m.build_resources(uc["legs"], coarse=True), "offers": [offer], "validity": VALID}
    return m.envelope("on_discover", {"catalogs": [catalog]},
                      schema_context_for(uc, [ctx.PRICE]))


# --------------------------------------------------------------------------- #
# Contracting: select .. on_confirm                                           #
# --------------------------------------------------------------------------- #
def build_contracting(uc):
    parts = [consumer(), provider_participant(uc)]
    quote  = [consideration(uc, "PRICE_QUOTED", "Quoted fare")]
    final  = [consideration(uc, "PRICE_CONFIRMED", "Confirmed fare")]
    out = {}

    # select (CN -> PN): draft, no id/PII/price.
    out["select"] = m.envelope("select",
        {"contract": contract(uc, status="DRAFT", commit_code="DRAFT")},
        schema_context_for(uc))

    # on_select (PN -> CN): id assigned + priced quote.
    out["on_select"] = m.envelope("on_select",
        {"contract": contract(uc, cid=uc["cid"], status="DRAFT", commit_code="DRAFT",
                              consideration_list=quote)},
        schema_context_for(uc, [ctx.PRICE, ctx.PRICECOMP]))

    # init (CN -> PN): billing participant + draft settlement.
    out["init"] = m.envelope("init",
        {"contract": contract(uc, cid=uc["cid"], status="DRAFT", commit_code="DRAFT",
                              consideration_list=quote, participants=[consumer()],
                              settlements=[settlement(uc, "DRAFT")])},
        schema_context_for(uc, [ctx.PRICE, ctx.PRICECOMP, ctx.PASSENGER, ctx.PERSON, ctx.PROVIDER, ctx.SETTLE]))

    # on_init (PN -> CN): finalised terms + provider participant.
    out["on_init"] = m.envelope("on_init",
        {"contract": contract(uc, cid=uc["cid"], status="DRAFT", commit_code="DRAFT",
                              consideration_list=final, participants=parts,
                              settlements=[settlement(uc, "DRAFT")])},
        schema_context_for(uc, [ctx.PRICE, ctx.PRICECOMP, ctx.PASSENGER, ctx.PERSON, ctx.PROVIDER, ctx.SETTLE]))

    # confirm (CN -> PN): payment committed.
    out["confirm"] = m.envelope("confirm",
        {"contract": contract(uc, cid=uc["cid"], status="DRAFT", commit_code="DRAFT",
                              consideration_list=final, participants=parts,
                              settlements=[settlement(uc, "COMMITTED")])},
        schema_context_for(uc, [ctx.PRICE, ctx.PRICECOMP, ctx.PASSENGER, ctx.PERSON, ctx.PROVIDER, ctx.SETTLE]))

    # on_confirm (PN -> CN): ACTIVE + performance (issued fulfillment artifact).
    perf = [{"id": "perf-" + uc["con_id"], "status": descriptor("Fulfillment scheduled", code="CONFIRMED"),
             "commitmentIds": ["cmt-" + uc["con_id"]], "performanceAttributes": uc["perf"]()}]
    out["on_confirm"] = m.envelope("on_confirm",
        {"contract": contract(uc, cid=uc["cid"], status="ACTIVE", commit_code="ACTIVE",
                              consideration_list=final, participants=parts,
                              settlements=[settlement(uc, "COMPLETE")],
                              performance=perf)},
        schema_context_for(uc, [ctx.PRICE, ctx.PRICECOMP, ctx.PASSENGER, ctx.PERSON, ctx.PROVIDER, ctx.SETTLE]))
    return out


# --------------------------------------------------------------------------- #
# Performance: status / track                                                 #
# --------------------------------------------------------------------------- #
def build_performance(uc):
    final = [consideration(uc, "PRICE_CONFIRMED", "Confirmed fare")]
    parts = [consumer(), provider_participant(uc)]
    out = {}

    # status (CN -> PN): query by contract id (Contract still needs commitments).
    out["status"] = m.envelope("status",
        {"contract": contract(uc, cid=uc["cid"], status="ACTIVE", commit_code="ACTIVE")},
        schema_context_for(uc))

    # on_status (PN -> CN): current performance progress.
    perf = [{"id": "perf-" + uc["con_id"],
             "status": descriptor("In progress", code="IN_PROGRESS"),
             "commitmentIds": ["cmt-" + uc["con_id"]], "performanceAttributes": uc["perf"]()}]
    out["on_status"] = m.envelope("on_status",
        {"contract": contract(uc, cid=uc["cid"], status="ACTIVE", commit_code="ACTIVE",
                              consideration_list=final, participants=parts, performance=perf)},
        schema_context_for(uc, [ctx.PRICE, ctx.PRICECOMP, ctx.PASSENGER, ctx.PERSON, ctx.PROVIDER, ctx.SETTLE]))

    # track (CN -> PN): Tracking wraps the contract (id required) + a status/url.
    light = contract(uc, cid=uc["cid"], status="ACTIVE", commit_code="ACTIVE")
    out["track"] = m.envelope("track",
        {"tracking": {"contract": light, "status": uc["track"],
                      "url": "https://track.example.com/<transactionId>"}},
        schema_context_for(uc))

    # on_track (PN -> CN): live tracking handle (ACTIVE only for on-road modes).
    # Live position expressed as a beckn GeoJSONGeometry Point (not schema.org).
    trk = {"contract": light, "status": uc["track"],
           "url": "https://track.example.com/live/" + uc["cid"],
           "trackingAttributes": {"@context": ctx.GEO, "@type": "GeoJSONGeometry",
                                  "type": "Point", "coordinates": m.CENTRAAL}}
    if uc["track"] == "INACTIVE":
        trk["trackingAttributes"]["description"] = "Live tracking not applicable to this service"
    out["on_track"] = m.envelope("on_track", {"tracking": trk}, schema_context_for(uc, [ctx.GEO]))
    return out


# --------------------------------------------------------------------------- #
# update / cancel / rate / support                                            #
# --------------------------------------------------------------------------- #
def build_update(uc):
    parts = [consumer(), provider_participant(uc)]
    # A representative mutation: rider adds an extra stop -> +3.00 to the fare.
    new_total = round(uc["total"] + 3.00, 2)
    fare = m.price_spec(new_total, [
        {"type": "UNIT", "value": uc["total"], "currency": "EUR", "description": "Original fare"},
        {"type": "SURCHARGE", "value": 3.00, "currency": "EUR", "description": "Added intermediate stop"}])
    revised = [consideration(uc, "PRICE_QUOTED", "Revised fare", fare=fare)]
    out = {}
    # update (CN -> PN): desired post-mutation state; context.try previews terms.
    env = m.envelope("update",
        {"contract": contract(uc, cid=uc["cid"], status="ACTIVE", commit_code="ACTIVE",
                              consideration_list=revised, participants=parts)},
        schema_context_for(uc, [ctx.PRICE, ctx.PRICECOMP, ctx.PASSENGER, ctx.PERSON, ctx.PROVIDER, ctx.SETTLE]))
    env["context"]["try"] = True   # preview the recalculated terms first
    out["update"] = env
    # on_update (PN -> CN): committed revised contract.
    out["on_update"] = m.envelope("on_update",
        {"contract": contract(uc, cid=uc["cid"], status="ACTIVE", commit_code="ACTIVE",
                              consideration_list=[consideration(uc, "PRICE_CONFIRMED", "Revised fare", fare=fare)],
                              participants=parts,
                              settlements=[settlement(uc, "COMMITTED", value=new_total)])},
        schema_context_for(uc, [ctx.PRICE, ctx.PRICECOMP, ctx.PASSENGER, ctx.PERSON, ctx.PROVIDER, ctx.SETTLE]))
    return out


def build_cancel(uc):
    parts = [consumer(), provider_participant(uc)]
    # cancel (CN -> PN): identify active contract to cancel (id required).
    out = {}
    env = m.envelope("cancel",
        {"contract": contract(uc, cid=uc["cid"], status="ACTIVE", commit_code="ACTIVE")},
        schema_context_for(uc))
    env["context"]["try"] = True   # preview cancellation terms first
    out["cancel"] = env
    # on_cancel (PN -> CN): terminal CANCELLED state + refund settlement (minus fee).
    fee = 2.00
    refund = round(uc["total"] - fee, 2)
    cancel_fare = m.price_spec(uc["total"], [
        {"type": "PENALTY", "value": fee, "currency": "EUR", "description": "Cancellation fee"},
        {"type": "REFUND", "value": refund, "currency": "EUR", "description": "Refund to rider"}])
    settlements = [
        settlement(uc, "COMPLETE"),
        settlement(uc, "COMPLETE", value=refund, note="Refund less cancellation fee"),
    ]
    out["on_cancel"] = m.envelope("on_cancel",
        {"contract": contract(uc, cid=uc["cid"], status="CANCELLED", commit_code="CLOSED",
                              consideration_list=[consideration(uc, "PRICE_ADJUSTED", "Cancellation charge", fare=cancel_fare)],
                              participants=parts, settlements=settlements)},
        schema_context_for(uc, [ctx.PRICE, ctx.PRICECOMP, ctx.PASSENGER, ctx.PERSON, ctx.PROVIDER, ctx.SETTLE]))
    return out


def rating_input(target_id, target_name, value):
    # Score carried as a beckn Rating (not schema.org Rating).
    return {"target": {"id": target_id, "descriptor": descriptor(target_name),
                       "targetAttributes": {"@context": ctx.RATING, "@type": "beckn:Rating",
                                            "beckn:ratingValue": value}},
            "range": {"min": 1, "max": 5, "value": value}}

def build_rate(uc):
    out = {}
    inputs = [rating_input(tid, tname, 5) for tid, tname in uc["rate_targets"]]
    # rate (CN -> PN): submit ratings.
    out["rate"] = m.envelope("rate", {"ratingInputs": inputs}, schema_context_for(uc, [ctx.RATING]))
    # on_rate (PN -> CN): confirm recorded ratings.
    out["on_rate"] = m.envelope("on_rate", {"ratings": inputs}, schema_context_for(uc, [ctx.RATING]))
    return out


def support_info(**fields):
    """A support contact as a beckn SupportInfo (replaces schema.org ContactPoint)."""
    a = {"@context": ctx.SUPPORT, "@type": "SupportInfo"}
    a.update(fields)
    return a

def build_support(uc):
    pid, name = uc["provider"]
    out = {}
    # support (CN -> PN): describe the help needed against the order + preferred channel.
    out["support"] = m.envelope("support",
        {"support": {"orderId": uc["cid"],
                     "descriptor": descriptor("Help with my booking", "Rider needs assistance",
                                              long="Rider left an item in the vehicle / needs booking help"),
                     "channels": [support_info(name="Rider", channels=["CHAT", "IN_APP"],
                                               chat="https://support.example.com/chat")]}},
        schema_context_for(uc, [ctx.SUPPORT]))
    # on_support (PN -> CN): resolved support contact + created ticket (in descriptor).
    out["on_support"] = m.envelope("on_support",
        {"support": {"orderId": uc["cid"],
                     "descriptor": descriptor("Support ticket SUP-" + uc["con_id"] + " created",
                                              code="TICKET_OPEN"),
                     "channels": [support_info(
                         name=name + " Support", channels=["PHONE", "EMAIL", "WEB"],
                         telephone="+31 20 555 0000", email="support@" + pid + ".example.com",
                         url="https://support.example.com/ticket/SUP-" + uc["con_id"],
                         hoursAvailable="24/7")]}},
        schema_context_for(uc, [ctx.SUPPORT]))
    return out


# --------------------------------------------------------------------------- #
# Driver                                                                       #
# --------------------------------------------------------------------------- #
def write(action, use_case_name, obj):
    d = os.path.join(BASE, action, "requests")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"post.request.{use_case_name}.json"), "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main():
    total = 0
    for uc in m.USE_CASES:
        files = {"on_discover": build_on_discover(uc)}
        for group in (build_contracting, build_performance, build_update, build_cancel,
                      build_rate, build_support):
            files.update(group(uc))
        for action, obj in files.items():
            write(action, uc["name"], obj)
            total += 1
    print(f"wrote {total} files across {len(m.USE_CASES)} use cases")


if __name__ == "__main__":
    main()
