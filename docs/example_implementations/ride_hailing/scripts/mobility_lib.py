"""
mobility_lib.py
===============

Shared building blocks for generating Beckn v2.0.0 ride-hailing example JSONs.

Key modelling principles baked in here:

  * GENERIC INTENT - a TripRequest expresses an origin->destination need without
    pinning a transport mode (`modes` is left empty); many different services may
    satisfy it. The concrete mode is conveyed by the offer (RideOption, FareProduct,
    Vehicle, Driver) and any Route, not by the intent.
  * OPTIMAL IGNORANCE - information is shared just-in-time. During DISCOVERY the
    consumer shares only a coarse area (city + region + country + postal-district,
    rounded coordinates) - never a street address. Precise pickup/drop addresses
    are revealed only from `select` onward, when a booking actually exists.
  * TARIFF vs BREAKUP - `on_discover` shows a headline tariff / fare estimate only
    (like a ride-hailing app). The itemised price breakup (PriceSpecification ->
    PriceComponent[]) appears once a selection exists (`on_select`) and is
    recalculated at completion.
  * BECKN-FIRST TYPES - domain attribute bags use beckn / schema.beckn.io types
    (Passenger, Provider, GeoJSONGeometry, Rating, SurgeMultiplier, FareLegRule ...)
    in preference to schema.org.
  * SELF-DESCRIBING EXTENSION - all domain data lives in `*Attributes` bags (the
    spec's `Attributes` schema: required @context + @type, additionalProperties
    true). Core beckn schemas (additionalProperties:false) are never modified.
"""

# --------------------------------------------------------------------------- #
# 1. Context (JSON-LD) URIs                                                     #
# --------------------------------------------------------------------------- #
class ctx:
    TRIP      = "https://schema.beckn.io/TripRequest/2.0/context.jsonld"
    RIDE      = "https://schema.beckn.io/RideOption/2.0/context.jsonld"
    SVC       = "https://schema.beckn.io/ServiceClass/2.0/context.jsonld"
    FARE      = "https://schema.beckn.io/FareProduct/2.0/context.jsonld"
    VEH       = "https://schema.beckn.io/Vehicle/2.0/context.jsonld"
    DRV       = "https://schema.beckn.io/Driver/2.0/context.jsonld"
    ROUTE     = "https://schema.beckn.io/Route/2.0/context.jsonld"
    PRICE     = "https://schema.beckn.io/PriceSpecification/2.1/context.jsonld"
    PRICECOMP = "https://schema.beckn.io/PriceComponent/2.1/context.jsonld"
    # Fare-structure vocabularies:
    FAREEST   = "https://schema.beckn.io/FareEstimate/2.0/context.jsonld"
    SURGE     = "https://schema.beckn.io/SurgeMultiplier/2.0/context.jsonld"
    TARIFF    = "https://schema.beckn.io/TariffZone/2.0/context.jsonld"
    LEGRULE   = "https://schema.beckn.io/FareLegRule/2.0/context.jsonld"
    RIDERCAT  = "https://schema.beckn.io/RiderCategory/2.0/context.jsonld"
    MEDIUM    = "https://schema.beckn.io/FareMedium/2.0/context.jsonld"
    TICKET    = "https://schema.beckn.io/Ticket/2.0/context.jsonld"
    # Party / identity / geo / rating (beckn-first, replacing schema.org):
    PASSENGER = "https://schema.beckn.io/Passenger/2.0/context.jsonld"
    PERSON    = "https://schema.beckn.io/Person/2.0/context.jsonld"
    PROVIDER  = "https://schema.beckn.io/Provider/2.0/context.jsonld"
    GEO       = "https://schema.beckn.io/GeoJSONGeometry/2.0/context.jsonld"
    RATING    = "https://schema.beckn.io/Rating/2.0/context.jsonld"
    SETTLE    = "https://schema.beckn.io/SettlementTerm/2.0/context.jsonld"
    SUPPORT   = "https://schema.beckn.io/SupportInfo/2.1/context.jsonld"
    ITIN      = "https://schema.beckn.io/Itinerary/2.0/context.jsonld"
    SPP       = "https://schema.beckn.io/SystemPricingPlan/2.0/context.jsonld"
    # (No schema.org: every attribute bag now uses a beckn / schema.beckn.io type.)


# --------------------------------------------------------------------------- #
# 2. Amsterdam geography ([lon, lat], RFC 7946)                                 #
# --------------------------------------------------------------------------- #
CENTRAAL = [4.9003, 52.3791]   # Amsterdam Centraal (origin)
RIJKS    = [4.8852, 52.3600]   # Rijksmuseum (destination)
VIJZEL   = [4.8912, 52.3564]   # Vijzelgracht metro (multimodal interchange)


def location(coords, street, postal, coarse=False):
    """
    A beckn ``Location`` (required GeoJSON ``geo`` + optional address).

    ``coarse=True`` (discovery phase) applies OPTIMAL IGNORANCE: the street line is
    dropped, the postal code is reduced to its 4-digit district prefix, and the
    coordinates are rounded to ~1 km so only a bounded area is disclosed.
    """
    if coarse:
        addr = {"addressLocality": "Amsterdam", "addressRegion": "North Holland",
                "addressCountry": "NL", "postalCode": postal.split()[0]}
        geo = {"type": "Point", "coordinates": [round(coords[0], 2), round(coords[1], 2)]}
    else:
        addr = {"streetAddress": street, "addressLocality": "Amsterdam",
                "addressRegion": "North Holland", "addressCountry": "NL",
                "postalCode": postal}
        geo = {"type": "Point", "coordinates": coords}
    return {"geo": geo, "address": addr}


# --------------------------------------------------------------------------- #
# 3. Primitive builders                                                        #
# --------------------------------------------------------------------------- #
def descriptor(name, short=None, long=None, code=None):
    d = {}
    if code:  d["code"] = code
    d["name"] = name
    if short: d["shortDesc"] = short
    if long:  d["longDesc"] = long
    return d


def trip(origin, destination, extra=None):
    """
    A self-describing TripRequest bag. ``modes`` is intentionally EMPTY: the trip is
    a generic mobility intent (origin -> destination) that any mode may satisfy.
    """
    t = {"@context": ctx.TRIP, "@type": "TripRequest",
         "modes": "", "origin": origin, "destination": destination}
    if extra:
        t.update(extra)
    return t


def money(value, currency="EUR"):
    """Bare PriceSpecification fragment (currency + value, NO breakup)."""
    return {"@context": ctx.PRICE, "@type": "PriceSpecification",
            "currency": currency, "value": value}


def price_spec(value, components=None, currency="EUR"):
    """PriceSpecification with an optional itemised breakup (list of PriceComponent)."""
    p = {"@context": ctx.PRICE, "@type": "PriceSpecification",
         "currency": currency, "value": value}
    if components:
        p["components"] = components
    return p


def pc(ptype, value, description, attrs=None, currency="EUR"):
    """
    A PriceSpecification breakup line = a ``PriceComponent``.

    Optional ``componentAttributes`` (a JSON-LD ``Attributes`` bag) richly describes
    WHY the line applies and HOW it was calculated - e.g. a SurgeMultiplier on a
    surged base line, or a FareLegRule + TariffZones on a zonal transit line. The
    receiving node renders/acts on it; it never computes the fare itself.
    """
    c = {"type": ptype, "value": value, "currency": currency, "description": description}
    if attrs is not None:
        c["componentAttributes"] = attrs
    return c


def _route(route_id, short, route_type):
    return {"@context": ctx.ROUTE, "@type": "Route",
            "routeId": route_id, "shortName": short, "routeType": route_type}

def _tariff_zone(zone_id, name, coords):
    return {"@context": ctx.TARIFF, "@type": "TariffZone",
            "zoneId": zone_id, "zoneName": name,
            "geometry": {"type": "Point", "coordinates": coords}}


# --------------------------------------------------------------------------- #
# 4. Beckn envelope                                                            #
# --------------------------------------------------------------------------- #
def envelope(action, message, schema_context):
    seen, sc = set(), []
    for c in schema_context:
        if c not in seen:
            seen.add(c); sc.append(c)
    return {
        "context": {
            "action": action, "version": "2.0.0",
            "bapId": "<bapId>", "senderId": "<senderId>", "bapUri": "<bapUri:uri>",
            "bppId": "<bppId>", "bppUri": "<bppUri:uri>", "receiverId": "<receiverId>",
            "transactionId": "<transactionId:uuid>", "messageId": "<messageId:uuid>",
            "networkId": "<networkId>", "timestamp": "<timestamp:date-time>",
            "key": "<key>", "try": False, "ttl": "<ttl>",
            "schemaContext": sc,
            "requestDigest": {"digest": "<digest:pattern ^BLAKE-512=[A-Za-z0-9+/]+=*$>"},
        },
        "message": message,
    }


# --------------------------------------------------------------------------- #
# 5. TARIFF builders (on_discover) - headline price only, NO breakup           #
# --------------------------------------------------------------------------- #
def tariff_ride_hailing():
    # A fare ESTIMATE range + the current surge indicator (as a ride-hailing app
    # would show at discovery). No itemised breakup at this stage.
    return {
        "@context": ctx.FAREEST, "@type": "FareEstimate",
        "estimatedAmount": 17.42, "currency": "EUR",
        "minimumAmount": 15.00, "maximumAmount": 21.00,
        "surgeMultiplier": {"@context": ctx.SURGE, "@type": "SurgeMultiplier",
                            "multiplierValue": 1.2, "reason": "HIGH_DEMAND"},
    }

def tariff_transit(value=3.40, rider="ADULT"):
    # The applicable fare-table entry for this rider category (no breakup).
    return {
        "@context": ctx.FARE, "@type": "FareProduct",
        "fareProductId": "gvb-1h", "durationType": "SINGLE_TRIP",
        "riderCategory": {"@context": ctx.RIDERCAT, "@type": "RiderCategory",
                          "riderCategoryId": rider.lower(), "descriptor": descriptor(rider.capitalize())},
        "price": money(value),
    }

def tariff_rate(value, note):
    p = money(value)
    p["description"] = note
    return p


# --------------------------------------------------------------------------- #
# 6. FARE builders (on_select onward) - full breakup via PriceComponent[]       #
# --------------------------------------------------------------------------- #
def fare_ride_hailing():
    # Breakup reuses core PriceSpecification.components; surge is folded into one
    # UNIT line whose componentAttributes carry the SurgeMultiplier (why/how).
    return {
        "@context": ctx.FAREEST, "@type": "FareEstimate",
        "estimatedAmount": 17.42, "currency": "EUR",
        "minimumAmount": 15.00, "maximumAmount": 21.00,
        "price": price_spec(17.42, [
            pc("UNIT", 14.40, "(Base fare + distance) X 1.2x surge pricing", attrs={
                "@context": ctx.SURGE, "@type": "SurgeMultiplier",
                "multiplierValue": 1.2, "reason": "HIGH_DEMAND",
                "validUntil": "2026-07-06T10:00:00Z", "appliedTo": money(12.00)}),
            pc("TAX", 3.02, "VAT 21%"),
        ]),
    }

def fare_transit(value=3.40, rider="ADULT"):
    return {
        "@context": ctx.FARE, "@type": "FareProduct",
        "fareProductId": "gvb-1h", "durationType": "SINGLE_TRIP",
        "price": price_spec(value, [
            pc("UNIT", value, rider.capitalize() + " single journey, Zone Amsterdam Centrum", attrs={
                "@context": ctx.LEGRULE, "@type": "FareLegRule",
                "fareProductId": "gvb-1h", "legGroupId": "urban-single",
                "fromAreaId": _tariff_zone("AMS-CENTRE", "Amsterdam Centrum", CENTRAAL),
                "toAreaId": _tariff_zone("AMS-CENTRE", "Amsterdam Centrum", RIJKS)}),
        ]),
        "riderCategory": {"@context": ctx.RIDERCAT, "@type": "RiderCategory",
                          "riderCategoryId": rider.lower(), "descriptor": descriptor(rider.capitalize()),
                          "proofRequired": "none" if rider == "ADULT" else "student ID"},
        "fareMedium": {"@context": ctx.MEDIUM, "@type": "FareMedium",
                       "mediumType": "MOBILE_APP", "mediumId": "gvb-app-token"},
    }

def fare_price(value, components):
    return price_spec(value, components)


# --------------------------------------------------------------------------- #
# 7. Fulfillment (Performance) artifacts issued at on_confirm                   #
# --------------------------------------------------------------------------- #
def perf_driver():
    return {"@context": ctx.DRV, "@type": "Driver", "yearsOfExperience": 6,
            "person": {"@context": ctx.PERSON, "@type": "Person",
                       "id": "person-drv-01", "name": "Driver assigned at pickup"},
            "vehicleNumber": "12-ABC-3"}

def perf_ticket():
    return {"@context": ctx.TICKET, "@type": "Ticket", "ticketId": "TCK-000123",
            "ticketType": "SINGLE", "validFrom": "2026-07-06T09:00:00Z",
            "validUntil": "2026-07-06T10:00:00Z",
            "fareMedium": {"@context": ctx.MEDIUM, "@type": "FareMedium",
                           "mediumType": "QR_CODE", "mediumId": "QR-TCK-000123"}}

def perf_vehicle(vid, plate):
    return {"@context": ctx.VEH, "@type": "Vehicle", "vehicleId": vid, "licensePlate": plate,
            "pickupLocation": location(CENTRAAL, "De Ruijterkade 34", "1012 AA")}


# --------------------------------------------------------------------------- #
# 8. Resources - built per phase (coarse area in discovery, precise later)      #
# --------------------------------------------------------------------------- #
def build_resources(legs, coarse):
    """Turn a use case's leg specs into Resource objects at the given granularity."""
    out = []
    for lg in legs:
        extra = {"route": lg["route"]} if lg.get("route") else None
        origin = location(*lg["o"], coarse=coarse)
        dest = location(*lg["d"], coarse=coarse)
        out.append({"id": lg["id"], "quantity": {"value": lg["qty"][0], "unit": lg["qty"][1]},
                    "resourceAttributes": trip(origin, dest, extra)})
    return out

def resource_ids(uc):
    return [lg["id"] for lg in uc["legs"]]

def schema_context_for(uc, extra=()):
    return [ctx.TRIP] + list(uc["contexts"]) + list(extra)


# --------------------------------------------------------------------------- #
# 9. USE CASES - one per transport mode                                        #
# --------------------------------------------------------------------------- #
O = (CENTRAAL, "Stationsplein", "1012 AB")     # origin spec (coords, street, postal)
D = (RIJKS, "Museumstraat 1", "1071 XX")       # destination spec

USE_CASES = []

# 1. Cab ride-hailing
USE_CASES.append({
    "name": "cab_hailing",
    "provider": ("pn-amsterdam-cabs", "Amsterdam Cabs"),
    "cid": "b1a7c1e2-1111-4a2b-8c3d-000000000001",
    "cdesc": descriptor("Cab ride: Centraal -> Rijksmuseum", "Ride-hailing"),
    "legs": [{"id": "res-trip-cab-01", "qty": (1, "trip"), "o": O, "d": D}],
    "offer_id": "off-ride-economy",
    "offer_attrs": {"@context": ctx.RIDE, "@type": "RideOption", "vehicleType": "SEDAN",
                    "estimatedDuration": "PT12M", "estimatedDistance": 3.2,
                    "serviceClass": {"@context": ctx.SVC, "@type": "ServiceClass",
                                     "serviceClassCode": "ECONOMY",
                                     "features": ["air-conditioning", "4 seats"]}},
    "con_id": "con-ride-economy",
    "tariff": tariff_ride_hailing,
    "fare": fare_ride_hailing,
    "total": 17.42,
    "perf": perf_driver,
    "commit_attrs": None,
    "contexts": [ctx.RIDE, ctx.SVC, ctx.FAREEST, ctx.SURGE, ctx.DRV],
    "track": "ACTIVE",
    "rate_targets": [("pn-amsterdam-cabs", "Amsterdam Cabs"), ("res-trip-cab-01", "The ride")],
})

# 2. Metro fare product
USE_CASES.append({
    "name": "metro_fare",
    "provider": ("pn-gvb", "GVB Amsterdam"),
    "cid": "b1a7c1e2-2222-4a2b-8c3d-000000000002",
    "cdesc": descriptor("Metro single journey: Centraal -> Rijksmuseum", "Transit fare"),
    "legs": [{"id": "res-trip-metro-01", "qty": (1, "journey"), "o": O, "d": D,
              "route": _route("gvb-metro-52", "52", "RAIL")}],
    "offer_id": "off-fare-single",
    "offer_attrs": {"@context": ctx.FARE, "@type": "FareProduct",
                    "fareProductId": "gvb-1h", "durationType": "SINGLE_TRIP", "mediaDuration": "PT1H"},
    "con_id": "con-fare-single",
    "tariff": lambda: tariff_transit(3.40, "ADULT"),
    "fare": lambda: fare_transit(3.40, "ADULT"),
    "total": 3.40,
    "perf": perf_ticket,
    "commit_attrs": None,
    "contexts": [ctx.FARE, ctx.ROUTE, ctx.TARIFF, ctx.LEGRULE, ctx.RIDERCAT, ctx.MEDIUM, ctx.TICKET],
    "track": "INACTIVE",
    "rate_targets": [("pn-gvb", "GVB Amsterdam")],
})

# 3. Self-drive bike rental
USE_CASES.append({
    "name": "bike_rental",
    "provider": ("pn-ovfiets", "OV-fiets"),
    "cid": "b1a7c1e2-3333-4a2b-8c3d-000000000003",
    "cdesc": descriptor("Shared bike rental (24h)", "Self-drive bike"),
    "legs": [{"id": "res-trip-bike-01", "qty": (1, "day"), "o": O, "d": D}],
    "offer_id": "off-bike-rental",
    "offer_attrs": {"@context": ctx.VEH, "@type": "Vehicle", "vehicleId": "ovf-city",
                    "make": "Batavus", "model": "City Bike", "color": "blue", "vehicleType": "CITY_BICYCLE"},
    "con_id": "con-bike-rental",
    "tariff": lambda: tariff_rate(4.55, "Rental per 24h"),
    "fare": lambda: fare_price(4.55, [pc("UNIT", 4.55, "Rental per 24h")]),
    "total": 4.55,
    "perf": lambda: perf_vehicle("ovf-city", "n/a"),
    "commit_attrs": None,
    "contexts": [ctx.VEH],
    "track": "INACTIVE",
    "rate_targets": [("pn-ovfiets", "OV-fiets"), ("res-trip-bike-01", "The bike")],
})

# 4. Driver-on-demand for the rider's own car
USE_CASES.append({
    "name": "driver_rental",
    "provider": ("pn-safedrivers", "SafeDrivers NL"),
    "cid": "b1a7c1e2-4444-4a2b-8c3d-000000000004",
    "cdesc": descriptor("Driver hire for your own car", "Driver-on-demand"),
    "legs": [{"id": "res-trip-driver-01", "qty": (1, "trip"), "o": O, "d": D}],
    "offer_id": "off-driver-hire",
    "offer_attrs": {"@context": ctx.DRV, "@type": "Driver", "yearsOfExperience": 8,
                    "contact": "+31 20 555 0142",
                    "person": {"@context": ctx.PERSON, "@type": "Person",
                               "id": "person-drv-pool", "name": "Vetted driver"}},
    "con_id": "con-driver-hire",
    "tariff": lambda: tariff_rate(19.00, "Driver fee, up to 30 min (+ VAT)"),
    "fare": lambda: fare_price(19.00, [
        pc("UNIT", 15.00, "Driver fee (up to 30 min)"),
        pc("TAX", 4.00, "VAT 21%")]),
    "total": 19.00,
    "perf": perf_driver,
    "commit_attrs": None,
    "contexts": [ctx.DRV, ctx.PERSON],
    "track": "ACTIVE",
    "rate_targets": [("pn-safedrivers", "SafeDrivers NL")],
})

# 5. Self-drive car rental (selection carries rental duration + distance)
# The rental selection is expressed as a beckn Itinerary: pickup/drop as
# departure/arrival, plus totalDuration and totalDistance (in METRES per schema).
CAR_RENTAL_SELECTION = {
    "@context": ctx.ITIN, "@type": "Itinerary",
    "departureTime": "2026-07-06T09:00:00Z", "arrivalTime": "2026-07-06T13:00:00Z",
    "totalDuration": "PT4H", "totalDistance": 45000,
}
USE_CASES.append({
    "name": "car_rental",
    "provider": ("pn-amsterdam-carrental", "Amsterdam Car Rental"),
    "cid": "b1a7c1e2-5555-4a2b-8c3d-000000000005",
    "cdesc": descriptor("Self-drive car rental (4h, ~45 km)", "Vehicle rental"),
    "legs": [{"id": "res-trip-carrental-01", "qty": (4, "hour"), "o": O, "d": D}],
    "offer_id": "off-car-rental",
    "offer_attrs": {"@context": ctx.VEH, "@type": "Vehicle", "vehicleId": "acr-vw-polo",
                    "make": "Volkswagen", "model": "Polo", "year": 2024, "color": "white",
                    "vehicleType": "COMPACT_CAR", "licensePlate": "12-ABC-3"},
    "con_id": "con-car-rental",
    "tariff": lambda: tariff_rate(6.00, "From EUR 6.00/hour + EUR 0.25/km; refundable EUR 150 deposit"),
    # The time & distance lines carry the applicable SystemPricingPlan rate; the
    # deposit is a plain SURCHARGE line (see note re: Invoice being an ill fit).
    "fare": lambda: fare_price(43.70, [
        pc("UNIT", 24.00, "4 hours @ 6.00/h", attrs={
            "@context": ctx.SPP, "@type": "SystemPricingPlan",
            "planId": "acr-hourly", "currency": "EUR", "isTaxable": True,
            "perMinuteChargingRate": 0.10}),
        pc("UNIT", 11.25, "45 km @ 0.25/km", attrs={
            "@context": ctx.SPP, "@type": "SystemPricingPlan",
            "planId": "acr-hourly", "currency": "EUR", "isTaxable": True,
            "perKmChargingRate": 0.25}),
        pc("FEE", 1.50, "Insurance"),
        pc("TAX", 6.95, "VAT 21%"),
        # A first-class DEPOSIT_REFUNDABLE line; its terms (held now, refunded to the
        # rider after fulfillment) are defined via the componentAttributes extension
        # using a beckn SettlementTerm.
        pc("DEPOSIT_REFUNDABLE", 150.00,
           "Refundable security deposit (hold; refunded after return of the vehicle undamaged)", attrs={
               "@context": ctx.SETTLE, "@type": "SettlementTerm",
               "amount": {"currency": "EUR", "value": 150.00},
               "paymentTrigger": "POST_FULFILLMENT",
               "settlementStatus": "PENDING",
               "payTo": {"vpa": "rider-refund-account@bank"},
               "acceptedPaymentMethods": ["BANK_TRANSFER"]})]),
    "total": 43.70,
    "perf": lambda: perf_vehicle("acr-vw-polo", "12-ABC-3"),
    "commit_attrs": CAR_RENTAL_SELECTION,
    "contexts": [ctx.VEH, ctx.ITIN, ctx.SPP, ctx.SETTLE],
    "track": "INACTIVE",
    "rate_targets": [("pn-amsterdam-carrental", "Amsterdam Car Rental")],
})

# 6. Multimodal point-to-point itinerary (walk + metro + walk)
USE_CASES.append({
    "name": "multimodal_itinerary",
    "provider": ("pn-journeyplanner", "Amsterdam Journey Planner"),
    "cid": "b1a7c1e2-6666-4a2b-8c3d-000000000006",
    "cdesc": descriptor("Walk + Metro itinerary: Centraal -> Rijksmuseum", "Multimodal transit"),
    "legs": [
        {"id": "res-leg-walk-1", "qty": (1, "leg"), "o": O,
         "d": (CENTRAAL, "Centraal Metro Entrance", "1012 AB")},
        {"id": "res-leg-metro-2", "qty": (1, "leg"),
         "o": (CENTRAAL, "Centraal Metro", "1012 AB"), "d": (VIJZEL, "Vijzelgracht Metro", "1017 HH"),
         "route": _route("gvb-metro-52", "52", "RAIL")},
        {"id": "res-leg-walk-3", "qty": (1, "leg"),
         "o": (VIJZEL, "Vijzelgracht Metro", "1017 HH"), "d": D},
    ],
    "offer_id": "off-itinerary-walk-metro",
    "offer_attrs": {"@context": ctx.FARE, "@type": "FareProduct", "fareProductId": "gvb-1h",
                    "durationType": "SINGLE_TRIP", "mediaDuration": "PT1H", "totalDuration": "PT19M",
                    "legOrder": ["res-leg-walk-1", "res-leg-metro-2", "res-leg-walk-3"]},
    "con_id": "con-itinerary",
    "tariff": lambda: tariff_transit(3.40, "ADULT"),
    "fare": lambda: fare_transit(3.40, "ADULT"),
    "total": 3.40,
    "perf": perf_ticket,
    "commit_attrs": None,
    "contexts": [ctx.FARE, ctx.ROUTE, ctx.TARIFF, ctx.LEGRULE, ctx.RIDERCAT, ctx.MEDIUM, ctx.TICKET],
    "track": "INACTIVE",
    "rate_targets": [("pn-journeyplanner", "Amsterdam Journey Planner")],
})
