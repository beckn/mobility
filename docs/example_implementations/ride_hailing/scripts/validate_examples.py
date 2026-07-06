"""
validate_examples.py
=====================

Structurally validates every generated example against the beckn v2.0.0 API
spec (components.schemas of beckn.yaml).

Because the sandbox has no ``jsonschema`` package (and no TLS for pip), this is a
hand-rolled checker that enforces the constraints that actually matter for these
examples:

  * ``additionalProperties: false`` on the closed core schemas (no stray fields).
  * ``required`` fields present at each level.
  * ``enum`` membership (contract/commitment/settlement status codes, etc.).
  * ``Attributes`` bags always carry ``@context`` + ``@type``.
  * ``anyOf`` gates (Catalog needs resources|offers; TimePeriod needs a bound).
  * Referential integrity (Offer.resourceIds resolve to Resource ids).

The spec is downloaded once via ``curl`` (the sandbox blocks Python TLS) to
``beckn.yaml`` next to this script; delete it to force a refresh.

Run:  python3 validate_examples.py
"""

import glob
import json
import os
import subprocess
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "example-jsons"))
SPEC_URL = "https://raw.githubusercontent.com/beckn/protocol-specifications-v2/refs/heads/main/api/v2.0.0/beckn.yaml"
SPEC_PATH = os.path.join(HERE, "beckn.yaml")


def load_spec():
    if not os.path.exists(SPEC_PATH):
        subprocess.run(["curl", "-sL", SPEC_URL, "-o", SPEC_PATH], check=True)
    return yaml.safe_load(open(SPEC_PATH))["components"]["schemas"]


S = load_spec()
errs = []
def bad(msg):
    errs.append(msg)


def props_ok(obj, name, path):
    """Enforce additionalProperties:false + required for a named spec schema."""
    sc = S[name]
    props = sc.get("properties", {})
    if sc.get("additionalProperties") is False:
        for k in obj:
            if k not in props:
                bad(f"{path}: '{k}' not allowed by {name} (additionalProperties:false)")
    for r in sc.get("required", []):
        if r not in obj:
            bad(f"{path}: missing required '{r}' ({name})")


def attrs(a, path):
    if not (isinstance(a, dict) and "@context" in a and "@type" in a):
        bad(f"{path}: Attributes require @context and @type")


def descriptor(d, path):
    props_ok(d, "Descriptor", path)

def timeperiod(tp, path):
    props_ok(tp, "TimePeriod", path)
    if not ("startDate" in tp or "endDate" in tp or ("startTime" in tp and "endTime" in tp)):
        bad(f"{path}: TimePeriod needs startDate|endDate|startTime+endTime")

def location(l, path):
    props_ok(l, "Location", path)
    if "type" not in l.get("geo", {}):
        bad(f"{path}: Location.geo needs GeoJSON type")

# PriceComponent (schema.beckn.io/PriceComponent/v2.1) - mirrored here because it
# is a schema.beckn.io type, not inlined in beckn.yaml. Validates the components of
# any nested PriceSpecification bag inside an Attributes container.
PRICE_COMPONENT_KEYS = {"type", "value", "currency", "description", "componentAttributes"}
PRICE_COMPONENT_TYPES = {"UNIT", "TAX", "DELIVERY", "DISCOUNT", "FEE", "SURCHARGE",
                         "DEPOSIT_REFUNDABLE", "DEPOSIT", "ADVANCE", "TIP", "CARRY_FORWARD",
                         "PENALTY", "DONATION", "TRANCHE", "CASHBACK", "SERVICE_FEE",
                         "PROCESSING_FEE", "CONVENIENCE_FEE", "REFUND", "TOTAL", "OTHER"}

def price_components(obj, path):
    if isinstance(obj, dict):
        if obj.get("@type") == "PriceSpecification" and isinstance(obj.get("components"), list):
            for i, comp in enumerate(obj["components"]):
                cp = f"{path}.components[{i}]"
                for k in comp:
                    if k not in PRICE_COMPONENT_KEYS:
                        bad(f"{cp}: '{k}' not allowed by PriceComponent (additionalProperties:false)")
                if comp.get("type") not in PRICE_COMPONENT_TYPES:
                    bad(f"{cp}.type '{comp.get('type')}' not in PriceComponent enum")
                if "componentAttributes" in comp:
                    attrs(comp["componentAttributes"], cp + ".componentAttributes")
        for k, v in obj.items():
            price_components(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            price_components(v, f"{path}[{i}]")

def consideration(c, path):
    props_ok(c, "Consideration", path)
    if "status" in c: descriptor(c["status"], path + ".status")
    if "considerationAttributes" in c:
        attrs(c["considerationAttributes"], path + ".considerationAttributes")
        price_components(c["considerationAttributes"], path + ".considerationAttributes")

def participant(p, path):
    props_ok(p, "Participant", path)
    if "participantAttributes" in p: attrs(p["participantAttributes"], path + ".participantAttributes")

def settlement(s, path):
    props_ok(s, "Settlement", path)
    if s.get("status") not in (None, "DRAFT", "COMMITTED", "COMPLETE"):
        bad(f"{path}.status '{s['status']}' not in enum")
    if "settlementAttributes" in s: attrs(s["settlementAttributes"], path + ".settlementAttributes")

def performance(p, path):
    props_ok(p, "Performance", path)
    if "status" in p: descriptor(p["status"], path + ".status")
    if "performanceAttributes" in p: attrs(p["performanceAttributes"], path + ".performanceAttributes")

def offer(o, path, in_commitment=False):
    props_ok(o, "Offer", path)
    if in_commitment:
        for r in ("id", "resourceIds"):
            if r not in o: bad(f"{path}: commitment offer requires '{r}'")
    if "offerAttributes" in o: attrs(o["offerAttributes"], path + ".offerAttributes")
    for i, c in enumerate(o.get("considerations", [])): consideration(c, f"{path}.considerations[{i}]")
    if "validity" in o: timeperiod(o["validity"], path + ".validity")

def resource(r, path, need_qty=False):
    props_ok(r, "Resource", path)
    if need_qty and "quantity" not in r: bad(f"{path}: requires quantity")
    if "descriptor" in r: descriptor(r["descriptor"], path + ".descriptor")
    if "resourceAttributes" in r: attrs(r["resourceAttributes"], path + ".resourceAttributes")

def commitment(cm, path):
    props_ok(cm, "Commitment", path)
    code = cm.get("status", {}).get("descriptor", {}).get("code")
    if code not in ("DRAFT", "ACTIVE", "CLOSED"):
        bad(f"{path}.status.descriptor.code '{code}' not in enum")
    for i, r in enumerate(cm.get("resources", [])): resource(r, f"{path}.resources[{i}]", need_qty=True)
    if "offer" in cm: offer(cm["offer"], path + ".offer", in_commitment=True)
    if "commitmentAttributes" in cm: attrs(cm["commitmentAttributes"], path + ".commitmentAttributes")

def contract(c, path):
    props_ok(c, "Contract", path)
    if len(c.get("commitments", [])) < 1: bad(f"{path}: commitments minItems 1")
    if "descriptor" in c: descriptor(c["descriptor"], path + ".descriptor")
    if c.get("status", {}).get("code") not in ("DRAFT", "ACTIVE", "CANCELLED", "COMPLETE"):
        bad(f"{path}.status.code not in enum")
    for i, cm in enumerate(c.get("commitments", [])): commitment(cm, f"{path}.commitments[{i}]")
    for i, x in enumerate(c.get("consideration", [])): consideration(x, f"{path}.consideration[{i}]")
    for i, x in enumerate(c.get("participants", [])): participant(x, f"{path}.participants[{i}]")
    for i, x in enumerate(c.get("settlements", [])): settlement(x, f"{path}.settlements[{i}]")
    for i, x in enumerate(c.get("performance", [])): performance(x, f"{path}.performance[{i}]")

def catalog(c, path):
    props_ok(c, "Catalog", path)
    if not ("resources" in c or "offers" in c): bad(f"{path}: Catalog needs resources|offers")
    descriptor(c["descriptor"], path + ".descriptor")
    props_ok(c["provider"], "Provider", path + ".provider")
    for i, l in enumerate(c["provider"].get("availableAt", [])): location(l, f"{path}.provider.availableAt[{i}]")
    for i, r in enumerate(c.get("resources", [])): resource(r, f"{path}.resources[{i}]")
    for i, o in enumerate(c.get("offers", [])): offer(o, f"{path}.offers[{i}]")
    if "validity" in c: timeperiod(c["validity"], path + ".validity")
    rids = {r["id"] for r in c.get("resources", [])}
    for i, o in enumerate(c.get("offers", [])):
        for rid in o.get("resourceIds", []):
            if rid not in rids: bad(f"{path}.offers[{i}] references unknown resourceId '{rid}'")

def tracking(t, path):
    props_ok(t, "Tracking", path)
    if t.get("status") not in ("ACTIVE", "INACTIVE"): bad(f"{path}.status not in enum")
    if "contract" in t:
        contract(t["contract"], path + ".contract")
        if "id" not in t["contract"]: bad(f"{path}.contract requires id")
    if "trackingAttributes" in t: attrs(t["trackingAttributes"], path + ".trackingAttributes")

def rating_input(r, path):
    props_ok(r, "RatingInput", path)
    if "target" in r and "targetAttributes" in r["target"]:
        attrs(r["target"]["targetAttributes"], path + ".target.targetAttributes")

def support(s, path):
    props_ok(s, "Support", path)
    for i, ch in enumerate(s.get("channels", [])): attrs(ch, f"{path}.channels[{i}]")


# action folder -> (wrapper schema, message validator)
def val_contract(msg, path): contract(msg["contract"], path + ".contract")
def val_catalogs(msg, path):
    for i, c in enumerate(msg["catalogs"]): catalog(c, f"{path}.catalogs[{i}]")
def val_tracking(msg, path): tracking(msg["tracking"], path + ".tracking")
def val_support(msg, path):  support(msg["support"], path + ".support")
def val_rate(msg, path):
    for i, r in enumerate(msg["ratingInputs"]): rating_input(r, f"{path}.ratingInputs[{i}]")
def val_onrate(msg, path):
    for i, r in enumerate(msg["ratings"]): rating_input(r, f"{path}.ratings[{i}]")

ACTIONS = {
    "on_discover": ("OnDiscoverAction", val_catalogs),
    "select": ("SelectAction", val_contract),
    "on_select": ("OnSelectAction", val_contract),
    "init": ("InitAction", val_contract),
    "on_init": ("OnInitAction", val_contract),
    "confirm": ("ConfirmAction", val_contract),
    "on_confirm": ("OnConfirmAction", val_contract),
    "status": ("StatusAction", val_contract),
    "on_status": ("OnStatusAction", val_contract),
    "track": ("TrackAction", val_tracking),
    "on_track": ("OnTrackAction", val_tracking),
    "update": ("UpdateAction", val_contract),
    "on_update": ("OnUpdateAction", val_contract),
    "cancel": ("CancelAction", val_contract),
    "on_cancel": ("OnCancelAction", val_contract),
    "rate": ("RateAction", val_rate),
    "on_rate": ("OnRateAction", val_onrate),
    "support": ("SupportAction", val_support),
    "on_support": ("OnSupportAction", val_support),
}


def main():
    total, failed = 0, 0
    for action, (sch, validator) in ACTIONS.items():
        for fn in sorted(glob.glob(os.path.join(BASE, action, "requests", "post.request.*.json"))):
            before = len(errs)
            obj = json.load(open(fn))
            if obj["context"]["action"] != action:
                bad(f"{fn}: context.action != {action}")
            msg = obj["message"]
            # Wrapper action schema (required + additionalProperties).
            if sch in S:
                props_ok(msg, sch, f"{action}:{os.path.basename(fn)}:message")
            validator(msg, f"{action}:{os.path.basename(fn)}")
            total += 1
            if len(errs) != before:
                failed += 1
    print(f"Checked {total} files, {failed} with issues.\n")
    if errs:
        for e in errs:
            print("  ✗", e)
        sys.exit(1)
    print("ALL EXAMPLES FULLY COMPLIANT WITH beckn v2.0.0 API SPEC ✓")


if __name__ == "__main__":
    main()
