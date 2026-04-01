#!/usr/bin/env python3
"""Generate README.md files for all mobility schema classes.
Run:  python3 schema/generate_readmes.py
"""
import os

MOB       = "https://schema.beckn.io/mobility"
CORE_DIR  = "https://github.com/beckn/core_schema/tree/draft/schema"
CORE_IRI  = "https://schema.beckn.io/core"
SCHEMA    = "https://schema.org"
TRANSMODEL= "https://w3id.org/transmodel/ontology#"
GEO       = "http://www.opengis.net/ont/geosparql#"
ERA       = "https://data.europa.eu/949/"
OSLO      = "https://data.vlaanderen.be/ns/mobiliteit#"
INSPIRE   = "https://inspire.ec.europa.eu/ontology/"

PREFIX_MAP = {
    "mobility:": MOB + "/",
    "beckn:":    CORE_DIR + "/",
    "schema:":   SCHEMA + "/",
    "transmodel:": TRANSMODEL,
    "geo:":      GEO,
    "era:":      ERA,
    "oslo:":     OSLO,
    "inspire:":  INSPIRE,
    "ldes:":     "https://w3id.org/ldes/",
}

def resolve_prefix(iri):
    for pfx, base in PREFIX_MAP.items():
        if iri.startswith(pfx):
            return base + iri[len(pfx):]
    return "#"

STRENGTH = {
    "owl:equivalentClass": "Exact",
    "rdfs:subClassOf":     "Subclass",
    "owl:sameAs":          "Exact",
    "skos:exactMatch":     "Exact Match",
    "skos:closeMatch":     "Close Match",
    "rdfs:seeAlso":        "Related",
    "skos:broadMatch":     "Broad Match",
}

def mob_type(n): return (n, f"{MOB}/{n}")
def core_type(n): return (n, f"{CORE_DIR}/{n}")
def sch(n): return (f"schema:{n}", f"{SCHEMA}/{n}")

CORE_PROPS = {
    "Constraint": [
        ("id",             *sch("Text"),            "Unique identifier for the constraint"),
        ("constraintType", *sch("Text"),            "Type of constraint (extensible term)"),
        ("operator",       *sch("Text"),            "Comparator operator (e.g. <=, >=, =)"),
        ("value",          *sch("Number"),          "Numeric value of the constraint"),
        ("unitCode",       *sch("Text"),            "Unit of measure code (UN/ECE Rec 20)"),
        ("validity",       *core_type("TimePeriod"),"Validity window for this constraint"),
    ],
    "Policy": [
        ("id",               *sch("Text"),               "Unique identifier for the policy"),
        ("policyType",       *sch("Text"),               "Type of policy (extensible term)"),
        ("descriptor",       *core_type("Descriptor"),   "Human-readable description of the policy"),
        ("validity",         *core_type("TimePeriod"),   "Validity window for this policy version"),
        ("policyAttributes", *core_type("Attributes"),  "Extensible domain-specific policy attributes"),
    ],
    "Alert": [
        ("id",         *sch("Text"),             "Unique identifier for the alert"),
        ("descriptor", *core_type("Descriptor"), "Human-readable description of the alert"),
        ("validity",   *core_type("TimePeriod"), "Time period during which the alert is active"),
        ("status",     *core_type("State"),      "Current status of the alert"),
    ],
    "Tracking": [
        ("id",       *sch("Text"),             "Unique identifier for the tracking record"),
        ("url",      *sch("URL"),              "URL endpoint for real-time tracking information"),
        ("status",   *core_type("State"),      "Current tracking status"),
        ("validity", *core_type("TimePeriod"), "Validity period for this tracking record"),
    ],
    "Offer": [
        ("id",         *sch("Text"),                    "Unique identifier for the offer"),
        ("descriptor", *core_type("Descriptor"),        "Human-readable description of the offer"),
        ("price",      *core_type("PriceSpecification"),"Price specification for this offer"),
        ("validity",   *core_type("TimePeriod"),        "Validity period of the offer"),
        ("tags",       *sch("Text"),                    "Tags or labels associated with the offer"),
    ],
    "Item": [
        ("id",         *sch("Text"),                    "Unique identifier for the item"),
        ("descriptor", *core_type("Descriptor"),        "Human-readable description of the item"),
        ("categoryId", *core_type("CategoryCode"),      "Category code classifying the item"),
        ("price",      *core_type("PriceSpecification"),"Price specification for this item"),
        ("quantity",   *core_type("Quantity"),          "Available quantity of the item"),
        ("tags",       *sch("Text"),                    "Tags associated with the item"),
    ],
    "Fulfillment": [
        ("id",           *sch("Text"),                   "Unique identifier for the fulfillment"),
        ("type",         *sch("Text"),                   "Type of fulfillment (extensible term)"),
        ("agent",        *core_type("FulfillmentAgent"), "The entity responsible for performing the fulfillment"),
        ("mode",         *core_type("FulfillmentMode"),  "Mode of fulfillment"),
        ("state",        *core_type("State"),            "Current state of the fulfillment"),
        ("participants", *core_type("Participant"),      "Participants entitled to receive this fulfillment"),
        ("stages",       *core_type("FulfillmentStage"), "Stages in the fulfillment lifecycle"),
        ("instructions", *core_type("Descriptor"),       "Instructions for fulfillment"),
    ],
    "Location": [
        ("id",         *sch("Text"),                "Unique identifier for the location"),
        ("descriptor", *core_type("Descriptor"),   "Human-readable description of the location"),
        ("gps",        *sch("Text"),               "GPS coordinates as a latitude,longitude string"),
        ("address",    *core_type("Address"),      "Physical address of the location"),
        ("city",       *sch("Text"),               "City name"),
        ("country",    *sch("Text"),               "ISO 3166-1 alpha-2 country code"),
        ("geojson",    *core_type("GeoJSONGeometry"),"GeoJSON geometry object representing this location"),
    ],
    "Catalog": [
        ("id",         *sch("Text"),             "Unique identifier for the catalog"),
        ("descriptor", *core_type("Descriptor"), "Human-readable description of the catalog"),
        ("tags",       *sch("Text"),             "Tags associated with the catalog"),
    ],
    "State": [
        ("id",         *sch("Text"),             "Unique identifier for the state"),
        ("descriptor", *core_type("Descriptor"), "Human-readable description of the state"),
        ("updatedAt",  *sch("DateTime"),         "Timestamp when the state was last updated"),
    ],
    "Entitlement": [
        ("id",          *sch("Text"),               "Unique identifier for the entitlement"),
        ("descriptor",  *core_type("Descriptor"),   "Human-readable information about the entitlement"),
        ("resource",    *core_type("ContractItem"), "The resource being accessed against this entitlement"),
        ("credentials", *core_type("Descriptor"),   "Credential descriptors for the entitlement"),
    ],
    "Participant": [
        ("id",           *sch("Text"),               "Unique identifier for the participant"),
        ("person",       *core_type("Person"),       "Personal details of the participant"),
        ("organization", *core_type("Organization"), "Organisation the participant belongs to"),
        ("entitlements", *core_type("Entitlement"),  "Entitlements held by the participant"),
    ],
    "Rating": [
        ("id",             *sch("Text"),           "Unique identifier for the rating"),
        ("ratingValue",    *sch("Number"),         "Numeric rating value"),
        ("ratingCategory", *sch("Text"),           "Category being rated (e.g. driver, vehicle, service)"),
        ("feedback",       *core_type("Feedback"), "Feedback associated with this rating"),
    ],
    "Invoice": [
        ("id",         *sch("Text"),                    "Unique identifier for the invoice"),
        ("descriptor", *core_type("Descriptor"),        "Human-readable description of the invoice"),
        ("price",      *core_type("PriceSpecification"),"Total price for the invoice"),
        ("breakup",    *core_type("PriceSpecification"),"Itemised price breakup"),
        ("validity",   *core_type("TimePeriod"),        "Validity period of the invoice"),
    ],
    "SupportTicket": [
        ("id",         *sch("Text"),             "Unique identifier for the support ticket"),
        ("descriptor", *core_type("Descriptor"), "Description of the support issue"),
        ("status",     *core_type("State"),      "Current status of the support ticket"),
        ("refId",      *sch("Text"),             "Reference to the associated order or fulfillment"),
    ],
    "Feedback": [
        ("id",         *sch("Text"),           "Unique identifier for the feedback"),
        ("descriptor", *core_type("Descriptor"),"Feedback content and form"),
        ("rating",     *core_type("Rating"),   "Rating associated with this feedback"),
    ],
    "CategoryCode": [
        ("id",               *sch("Text"),             "Unique identifier for the category code"),
        ("descriptor",       *core_type("Descriptor"), "Human-readable label for the category"),
        ("parentCategoryId", *sch("Text"),             "Identifier of the parent category if hierarchical"),
    ],
    "Quantity": [
        ("unitCode", *sch("Text"),   "Unit of measure code (UN/ECE Rec 20)"),
        ("value",    *sch("Number"), "Numeric quantity value"),
        ("maximum",  *sch("Number"), "Maximum allowed quantity"),
        ("minimum",  *sch("Number"), "Minimum required quantity"),
    ],
    "Descriptor": [
        ("name",       *sch("Text"), "Short display name of the entity"),
        ("short_desc", *sch("Text"), "Brief textual description"),
        ("long_desc",  *sch("Text"), "Detailed or long-form description"),
        ("media",      *sch("URL"),  "Media resource URLs (images, audio, video)"),
        ("images",     *sch("URL"),  "Image URLs for visual display"),
    ],
    "TimePeriod": [
        ("startDate", *sch("DateTime"), "Start date and time of the period"),
        ("endDate",   *sch("DateTime"), "End date and time of the period"),
        ("startTime", *sch("Text"),     "Start time of day in HH:MM:SS format"),
        ("endTime",   *sch("Text"),     "End time of day in HH:MM:SS format"),
    ],
    "GeoJSONGeometry": [
        ("type",        *sch("Text"),     "GeoJSON geometry type (Point, Polygon, LineString, etc.)"),
        ("coordinates", *sch("ItemList"), "Coordinate array per RFC 7946"),
    ],
    "Person": [
        ("id",        *sch("Text"),           "Unique identifier for the person"),
        ("name",      *sch("Text"),           "Full name of the person"),
        ("email",     *sch("Text"),           "Email address"),
        ("telephone", *sch("Text"),           "Telephone number"),
        ("address",   *core_type("Address"), "Physical address"),
    ],
    "Organization": [
        ("id",         *sch("Text"),             "Unique identifier for the organisation"),
        ("descriptor", *core_type("Descriptor"), "Human-readable description of the organisation"),
        ("address",    *core_type("Address"),    "Physical address of the organisation"),
    ],
    "PriceSpecification": [
        ("currency",     *sch("Text"),   "ISO 4217 currency code (e.g. INR, USD, EUR)"),
        ("value",        *sch("Number"), "Monetary amount"),
        ("offerPrice",   *sch("Number"), "Discounted or offered price"),
        ("maximumValue", *sch("Number"), "Maximum price value"),
        ("minimumValue", *sch("Number"), "Minimum price value"),
    ],
    "FulfillmentAgent": [
        ("id",           *sch("Text"),               "Unique identifier for the fulfillment agent"),
        ("person",       *core_type("Person"),       "Personal details of the agent"),
        ("organization", *core_type("Organization"), "Organisation the agent belongs to"),
        ("contact",      *sch("Text"),               "Contact information for the agent"),
        ("rating",       *core_type("Rating"),       "Overall rating of the agent"),
    ],
    "ContractItem": [
        ("id",         *sch("Text"),                    "Unique identifier for the contract item"),
        ("descriptor", *core_type("Descriptor"),        "Human-readable description of the item"),
        ("price",      *core_type("PriceSpecification"),"Price for this contract item"),
        ("quantity",   *core_type("Quantity"),          "Quantity of this contract item"),
    ],
    "CancellationPolicy": [
        ("id",                *sch("Text"),             "Unique identifier for the cancellation policy"),
        ("descriptor",        *core_type("Descriptor"), "Human-readable description of the policy"),
        ("cancellationTerms", *sch("Text"),             "Terms and conditions governing cancellation"),
        ("refundPercentage",  *sch("Number"),           "Percentage of the fare refunded on cancellation"),
        ("cancelByTime",      *core_type("TimePeriod"), "Deadline by which cancellation must be made"),
    ],
    "Contract": [
        ("id",           *sch("Text"),               "Unique identifier for the contract"),
        ("descriptor",   *core_type("Descriptor"),   "Human-readable description of the contract"),
        ("items",        *core_type("ContractItem"), "Line items within the contract"),
        ("fulfillments", *core_type("Fulfillment"),  "Fulfillments associated with this contract"),
        ("state",        *core_type("State"),        "Current state of the contract"),
    ],
    "FulfillmentStop": [
        ("id",           *sch("Text"),             "Unique identifier for the fulfillment stop"),
        ("location",     *core_type("Location"),   "Geographic location of the stop"),
        ("type",         *sch("Text"),             "Type of stop (start, end, intermediate)"),
        ("instructions", *core_type("Descriptor"), "Instructions for passengers at this stop"),
        ("time",         *core_type("TimePeriod"), "Expected time window at this stop"),
    ],
    "PriceComponent": [
        ("title", *sch("Text"),                    "Title or label of this price component"),
        ("price", *core_type("PriceSpecification"),"Monetary value of this component"),
        ("tags",  *sch("Text"),                    "Tags associated with this price component"),
    ],
    "DiscoveryIntent": [
        ("id",         *sch("Text"),             "Unique identifier for the discovery intent"),
        ("descriptor", *core_type("Descriptor"), "Human-readable description of what is being sought"),
        ("tags",       *sch("Text"),             "Additional filtering or search criteria"),
    ],
    "SupportInfo": [
        ("phone", *sch("Text"), "Support phone number"),
        ("email", *sch("Text"), "Support email address"),
        ("url",   *sch("URL"),  "URL to support portal or chat interface"),
    ],
    "Feature": [
        ("id",         *sch("Text"),             "Unique identifier for the feature"),
        ("descriptor", *core_type("Descriptor"), "Human-readable label of the feature"),
        ("value",      *sch("Text"),             "Value of the feature (e.g. yes, no, unknown)"),
    ],
}

CORE_PROPS["Provider"] = [
    ("id",          "schema:Text",           "https://schema.org/Text",              "Unique identifier for the provider"),
    ("descriptor",  "Descriptor",             "https://github.com/beckn/core_schema/tree/draft/schema/Descriptor", "Human-readable description of the provider"),
    ("categories",  "CategoryCode",           "https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode", "Service categories offered by the provider"),
    ("locations",   "Location",               "https://github.com/beckn/core_schema/tree/draft/schema/Location",    "Locations where the provider offers services"),
    ("items",       "Item",                   "https://github.com/beckn/core_schema/tree/draft/schema/Item",        "Items available for discovery from this provider"),
    ("fulfillments","Fulfillment",            "https://github.com/beckn/core_schema/tree/draft/schema/Fulfillment", "Fulfillment options offered by this provider"),
    ("ratingsTotal","schema:Number",          "https://schema.org/Number",            "Total number of ratings received"),
    ("rating",      "Rating",                 "https://github.com/beckn/core_schema/tree/draft/schema/Rating",      "Aggregate rating of the provider"),
]
CORE_PROPS["Intent"] = [
    ("textSearch", "schema:Text", "https://schema.org/Text",   "Free-text search query expressing what the traveler is looking for"),
    ("filters",    "schema:Text", "https://schema.org/Text",   "JSONPath filter criteria applied to the search results"),
    ("spatial",    "SpatialConstraint", "https://github.com/beckn/core_schema/tree/draft/schema/SpatialConstraint", "Geographic constraints on the search area"),
    ("provider",   "schema:Text", "https://schema.org/Text",   "Identifier of a specific provider to search within"),
]

CORE_PROPS["RatingInput"] = [
    ("target",      "schema:Text", "https://schema.org/Text",  "The entity being rated, with id and category (Order, Fulfillment, Provider, Agent)"),
    ("range",       "schema:Text", "https://schema.org/Text",  "Rating scale definition (numeric range or descriptor array)"),
    ("ratingValue", "schema:Number","https://schema.org/Number","Numeric rating value selected by the user"),
    ("feedback",    "Descriptor",  "https://github.com/beckn/core_schema/tree/draft/schema/Descriptor", "Textual feedback or written review accompanying the rating"),
]

CORE_PROPS["SupportRequest"] = [
    ("orderId",       "schema:Text", "https://schema.org/Text", "Identifier of the contract/order against which support is required"),
    ("ticketIds",     "SupportTicket","https://github.com/beckn/core_schema/tree/draft/schema/SupportTicket", "Identifiers of any open support tickets"),
    ("callbackPhone", "schema:Text", "https://schema.org/Text", "Telephone number for callback support"),
]


CLASS_DATA = [
    {"name":"AffectedLine","description":"A reference to a transport line that is affected by a service disruption or alert.","related":[("beckn:Alert","rdfs:subClassOf","Subclass"),("mobility:Line","rdfs:seeAlso","Related")],"parent":("Alert","core"),"own_props":[("lineId",*sch("Text"),"Identifier of the affected transport line"),("lineRef",*mob_type("Line"),"Reference to the affected Line entity"),("affectedStops",*mob_type("Stop"),"Stops on this line affected by the disruption"),("cause",*sch("Text"),"Cause of the disruption affecting this line")]},
    {"name":"Alert","description":"A notification of a service disruption, delay, or advisory affecting one or more routes, stops, or vehicle journeys.","related":[("beckn:Alert","rdfs:subClassOf","Subclass"),("schema:Event","rdfs:seeAlso","Related")],"parent":("Alert","core"),"own_props":[("cause",*sch("Text"),"Cause of the alert (e.g. TECHNICAL_PROBLEM, STRIKE, ACCIDENT)"),("effect",*sch("Text"),"Effect on service (e.g. DETOUR, REDUCED_SERVICE, NO_SERVICE)"),("url",*sch("URL"),"URL to a page with more information about the alert"),("headerText",*sch("Text"),"Short header text for the alert"),("descriptionText",*sch("Text"),"Detailed description of the alert"),("activePeriod",*core_type("TimePeriod"),"Time period during which the alert is active"),("informedEntity",*mob_type("EntitySelector"),"Transport entities affected by this alert")]},
    {"name":"AncillaryService","description":"An optional or additional service available for purchase alongside base transport, such as extra baggage or lounge access.","related":[("beckn:Offer","rdfs:subClassOf","Subclass"),("schema:Service","rdfs:seeAlso","Related")],"parent":("Offer","core"),"own_props":[("serviceCode",*sch("Text"),"IATA service code (e.g. BG for extra baggage)"),("serviceCategory",*sch("Text"),"Category of the ancillary service"),("maxQuantity",*sch("Number"),"Maximum quantity of this service that can be purchased")]},
    {"name":"Asset","description":"A specific mobility resource (vehicle, bike, scooter, or car) managed and made available for use by a mobility provider.","related":[("beckn:Item","rdfs:subClassOf","Subclass"),("schema:Product","rdfs:seeAlso","Related")],"parent":("Item","core"),"own_props":[("assetId",*sch("Text"),"Provider-assigned unique identifier for the asset"),("assetType",*mob_type("VehicleType"),"Vehicle type classification of this asset"),("currentStatus",*mob_type("VehicleStatus"),"Real-time operational status of this asset"),("currentLocation",*core_type("Location"),"Current geographic location of the asset")]},
    {"name":"Authority","description":"A governmental or administrative body responsible for planning, regulating, and overseeing transport services within a jurisdiction.","related":[("beckn:Provider","rdfs:subClassOf","Subclass"),("schema:GovernmentOrganization","rdfs:subClassOf","Subclass")],"parent":("Provider","core"),"own_props":[("authorityId",*sch("Text"),"Unique identifier for the authority"),("jurisdiction",*sch("Text"),"Geographic or administrative jurisdiction of this authority"),("regulatoryScope",*sch("Text"),"Scope of regulatory powers (e.g. national, regional, local)")]},
    {"name":"BaggageAllowance","description":"The quantity and weight of baggage a passenger is permitted to carry or check in without incurring additional charges.","related":[("beckn:Constraint","rdfs:subClassOf","Subclass")],"parent":("Constraint","core"),"own_props":[("cabinBaggageCount",*sch("Number"),"Maximum number of cabin (carry-on) bags allowed"),("cabinBaggageWeight",*sch("Number"),"Maximum weight in kilograms for cabin baggage"),("checkedBaggageCount",*sch("Number"),"Maximum number of checked bags allowed"),("checkedBaggageWeight",*sch("Number"),"Maximum weight in kilograms per checked bag")]},
    {"name":"BikeAllowed","description":"An indicator specifying whether bicycles are permitted on board a particular route or vehicle journey.","related":[("beckn:Feature","rdfs:subClassOf","Subclass")],"parent":("Feature","conceptual"),"own_props":[("bikeAllowedValue",*sch("Text"),"Indicates whether bikes are allowed: yes, no, or unknown")]},
    {"name":"BookingRule","description":"A set of rules governing how and when a demand-responsive transport service must be booked in advance.","related":[("beckn:Policy","rdfs:subClassOf","Subclass")],"parent":("Policy","core"),"own_props":[("latestBookingTime",*sch("Text"),"Latest time before departure that a booking can be made"),("earliestBookingTime",*sch("Text"),"Earliest time before departure that a booking can be made"),("priorNoticeDurationMin",*sch("Number"),"Minimum advance notice in minutes required for booking"),("priorNoticeStartDay",*sch("Number"),"Earliest day before service when booking opens"),("priorNoticeStartTime",*sch("Text"),"Time of day on the start day when booking opens"),("message",*sch("Text"),"Customer-facing message about booking requirements"),("phoneNumber",*sch("Text"),"Phone number to call for booking"),("url",*sch("URL"),"URL to booking interface")]},
    {"name":"CancellationPolicy","description":"A policy defining the terms and conditions under which a transport booking can be cancelled, including applicable refund percentages and cancellation deadlines.","related":[("beckn:CancellationPolicy","owl:equivalentClass","Exact")],"parent":("CancellationPolicy","core"),"own_props":[("cancellationFee",*sch("Number"),"Flat cancellation fee charged upon cancellation"),("gracePeriodMinutes",*sch("Number"),"Number of minutes after booking during which cancellation is free"),("fareComponent",*mob_type("FareBreakup"),"Fare components affected by this cancellation policy")]},
    {"name":"ContactHandle","description":"A communication handle (such as a phone number, email address, or chat URL) used to contact a driver or support agent in a mobility service.","related":[("beckn:SupportInfo","rdfs:subClassOf","Subclass")],"parent":("SupportInfo","core"),"own_props":[("handleType",*sch("Text"),"Type of contact handle (PHONE, EMAIL, CHAT, APP)"),("handle",*sch("Text"),"The actual contact handle value (number, address, or URL)"),("label",*sch("Text"),"Human-readable label for this contact handle")]},
    {"name":"DayType","description":"A classification of a day (e.g., weekday, weekend, public holiday) used to define when a service pattern is valid.","related":[("beckn:TimePeriod","rdfs:subClassOf","Subclass"),("schema:DayOfWeek","rdfs:seeAlso","Related")],"parent":("TimePeriod","core"),"own_props":[("dayTypeCode",*sch("Text"),"Code identifying the day type (e.g. WEEKDAY, WEEKEND, HOLIDAY)"),("daysOfWeek",*sch("ItemList"),"List of days of the week applicable to this day type")]},
    {"name":"DepartureMessage","description":"A real-time message containing predicted departure times for vehicles at a stop, as used in VDV real-time standards.","related":[("beckn:Alert","rdfs:subClassOf","Subclass"),("mobility:StopTime","rdfs:seeAlso","Related")],"parent":("Alert","core"),"own_props":[("stopRef",*mob_type("Stop"),"Reference to the stop for which departures are reported"),("lineRef",*mob_type("Line"),"Reference to the line departing from this stop"),("vehicleRef",*mob_type("VehicleDescriptor"),"Reference to the departing vehicle"),("expectedDeparture",*sch("DateTime"),"Predicted departure time"),("delaySeconds",*sch("Number"),"Delay in seconds relative to scheduled departure")]},
    {"name":"Direction","description":"The direction of travel of a transport service along a route, typically expressed as inbound or outbound.","related":[("beckn:Descriptor","rdfs:subClassOf","Subclass"),("schema:Direction","rdfs:seeAlso","Related")],"parent":("Descriptor","core"),"own_props":[("directionId",*sch("Text"),"Binary direction identifier (0 for one direction, 1 for the other)"),("directionCode",*sch("Text"),"Named direction code (e.g. INBOUND, OUTBOUND, CLOCKWISE)")]},
    {"name":"DistributionChannel","description":"A channel or platform through which fare products or tickets are sold or distributed to end customers.","related":[("beckn:Catalog","skos:closeMatch","Close Match"),("schema:ItemList","rdfs:seeAlso","Related")],"parent":("Catalog","core"),"own_props":[("channelType",*sch("Text"),"Type of distribution channel (e.g. ONLINE, TICKET_OFFICE, MOBILE_APP)"),("channelName",*sch("Text"),"Human-readable name of this distribution channel"),("url",*sch("URL"),"URL to access this distribution channel")]},
    {"name":"Driver","description":"A person who operates a transport vehicle and is responsible for the safe delivery of passengers during a mobility service trip.","related":[("beckn:FulfillmentAgent","owl:equivalentClass","Exact"),("schema:Person","rdfs:subClassOf","Subclass")],"parent":("FulfillmentAgent","core"),"own_props":[("licenseNumber",*sch("Text"),"Driver's license number"),("vehicleNumber",*sch("Text"),"Registration number of the vehicle being driven"),("yearsOfExperience",*sch("Number"),"Number of years of professional driving experience")]},
    {"name":"DropPolicy","description":"A set of rules governing the locations and conditions under which passengers may be dropped off at the end of a ride-hailing or on-demand transport service.","related":[("beckn:Policy","rdfs:subClassOf","Subclass")],"parent":("Policy","core"),"own_props":[("allowedDropAreas",*mob_type("Geofence"),"Geographic areas where drop-off is permitted"),("dropConditions",*sch("Text"),"Conditions that must be met for a valid drop-off"),("dropNote",*sch("Text"),"Customer-facing note about drop-off rules")]},
    {"name":"EmergencyEvent","description":"A critical safety or operational event requiring immediate response, such as an accident, vehicle breakdown, or passenger emergency.","related":[("beckn:Alert","rdfs:subClassOf","Subclass"),("schema:Event","rdfs:seeAlso","Related")],"parent":("Alert","core"),"own_props":[("emergencyType",*sch("Text"),"Type of emergency (e.g. ACCIDENT, BREAKDOWN, MEDICAL)"),("severity",*sch("Text"),"Severity level of the emergency (LOW, MEDIUM, HIGH, CRITICAL)"),("reportedAt",*sch("DateTime"),"Timestamp when the emergency was reported"),("location",*core_type("Location"),"Geographic location of the emergency")]},
    {"name":"Entitlement","description":"A specific right or benefit granted to a passenger or rider, such as free travel, priority boarding, or a concessionary pass.","related":[("beckn:Entitlement","owl:equivalentClass","Exact")],"parent":("Entitlement","core"),"own_props":[("entitlementType",*sch("Text"),"Type of entitlement (e.g. FREE_TRAVEL, CONCESSION, PRIORITY)"),("eligibilityRules",*sch("Text"),"Rules defining who is eligible for this entitlement"),("issuingAuthority",*mob_type("Authority"),"The authority or operator that issued this entitlement"),("validity",*core_type("TimePeriod"),"Validity period of the entitlement")]},
    {"name":"EntitySelector","description":"A selector that identifies which transport entities (routes, trips, stops, or agencies) are affected by a given alert.","related":[("beckn:Alert","rdfs:subClassOf","Subclass"),("mobility:Alert","rdfs:seeAlso","Related")],"parent":("Alert","core"),"own_props":[("agencyId",*sch("Text"),"Identifier of the affected agency"),("routeId",*sch("Text"),"Identifier of the affected route"),("routeType",*sch("Text"),"Type of the affected route (e.g. BUS, RAIL)"),("tripDescriptor",*mob_type("TripDescriptor"),"Descriptor identifying the affected trip"),("stopId",*sch("Text"),"Identifier of the affected stop")]},
    {"name":"EstimatedTimetableDelivery","description":"A real-time data delivery providing predicted departure and arrival times for a set of vehicle journeys.","related":[("beckn:Tracking","rdfs:subClassOf","Subclass"),("mobility:Timetable","rdfs:seeAlso","Related")],"parent":("Tracking","core"),"own_props":[("responseTimestamp",*sch("DateTime"),"Timestamp of this delivery response"),("estimatedVehicleJourneys",*mob_type("VehicleJourney"),"Vehicle journeys with estimated timetable data"),("validUntil",*sch("DateTime"),"Time until which this estimated data is valid")]},
    {"name":"Event","description":"A discrete state change in the lifecycle of a vehicle or mobility asset, such as a trip starting, vehicle reserved, or battery low.","related":[("beckn:State","rdfs:subClassOf","Subclass"),("schema:Event","rdfs:subClassOf","Subclass")],"parent":("State","core"),"own_props":[("eventType",*sch("Text"),"Type of lifecycle event (e.g. TRIP_START, VEHICLE_RESERVED, BATTERY_LOW)"),("entityId",*sch("Text"),"Identifier of the entity that generated the event"),("triggeredAt",*sch("DateTime"),"Timestamp when the event was triggered"),("payload",*sch("Text"),"Additional event-specific data payload")]},
    {"name":"ExchangePoints","description":"Locations in a transport network where fixed-route and flexible services connect, enabling passenger interchange.","related":[("beckn:FulfillmentStop","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("FulfillmentStop","conceptual"),"own_props":[("exchangePointType",*sch("Text"),"Type of exchange point (e.g. FIXED_TO_FLEX, FLEX_TO_FLEX)"),("connectingServices",*mob_type("VehicleJourney"),"Services that connect at this exchange point")]},
    {"name":"Fare","description":"The monetary cost of travel for a specific journey or service, calculated based on applicable fare rules and passenger categories.","related":[("beckn:Offer","rdfs:subClassOf","Subclass"),("schema:PriceSpecification","rdfs:seeAlso","Related")],"parent":("Offer","core"),"own_props":[("fareId",*sch("Text"),"Unique identifier for the fare"),("amount",*sch("Number"),"Total fare amount"),("currency",*sch("Text"),"ISO 4217 currency code"),("fareAttributes",*sch("Text"),"Transfer permissions, agency, and transfer limit"),("fareRules",*mob_type("FareLegRule"),"Leg rules that determine when this fare applies")]},
    {"name":"FareBreakup","description":"A detailed breakdown of the total fare into its constituent components, including base fare, taxes, surcharges, and discounts.","related":[("beckn:PriceComponent","rdfs:subClassOf","Subclass")],"parent":("PriceComponent","conceptual"),"own_props":[("componentTitle",*sch("Text"),"Human-readable title for this fare component"),("amount",*sch("Number"),"Monetary amount for this fare component"),("currency",*sch("Text"),"ISO 4217 currency code for this component"),("taxAmount",*sch("Number"),"Tax amount included in this component"),("taxRate",*sch("Number"),"Tax rate percentage applied")]},
    {"name":"FareComponent","description":"A component of an air travel fare that applies to a specific flight segment or leg, used in aviation pricing.","related":[("beckn:PriceComponent","rdfs:subClassOf","Subclass"),("mobility:Fare","rdfs:seeAlso","Related")],"parent":("PriceComponent","conceptual"),"own_props":[("fareBasisCode",*sch("Text"),"IATA fare basis code identifying the fare type"),("cabin",*sch("Text"),"Cabin class (ECONOMY, BUSINESS, FIRST)"),("bookingCode",*sch("Text"),"Booking class code (e.g. Y, M, K)"),("amount",*sch("Number"),"Fare amount for this component"),("currency",*sch("Text"),"ISO 4217 currency code"),("segmentRef",*mob_type("FlightSegment"),"Flight segment this fare component applies to")]},
    {"name":"FareEstimate","description":"An estimated fare for a requested trip, typically returned in response to a search before the booking is confirmed.","related":[("beckn:Offer","rdfs:subClassOf","Subclass")],"parent":("Offer","core"),"own_props":[("estimatedAmount",*sch("Number"),"Estimated total fare amount"),("currency",*sch("Text"),"ISO 4217 currency code"),("minimumAmount",*sch("Number"),"Minimum possible fare"),("maximumAmount",*sch("Number"),"Maximum possible fare"),("fareBreakup",*mob_type("FareBreakup"),"Itemised breakdown of the estimated fare")]},
    {"name":"FareLegRule","description":"A rule defining how a fare is applied to a single leg of a journey based on origin, destination, network, and time.","related":[("beckn:Policy","rdfs:subClassOf","Subclass"),("mobility:FareProduct","rdfs:seeAlso","Related")],"parent":("Policy","core"),"own_props":[("fareProductId",*sch("Text"),"Identifier of the fare product this rule applies to"),("legGroupId",*sch("Text"),"Leg group identifier for grouping related rules"),("networkId",*sch("Text"),"Network to which this rule is restricted"),("fromAreaId",*mob_type("TariffZone"),"Origin tariff zone for this fare leg rule"),("toAreaId",*mob_type("TariffZone"),"Destination tariff zone for this fare leg rule"),("containsServiceId",*mob_type("Route"),"Specific route this rule applies to")]},
    {"name":"FareMedium","description":"The physical or digital medium used to carry or present a fare product, such as a contactless card, mobile app, or paper ticket.","related":[("beckn:Entitlement","rdfs:subClassOf","Subclass")],"parent":("Entitlement","core"),"own_props":[("mediumType",*sch("Text"),"Type of fare medium (e.g. CONTACTLESS_CARD, MOBILE_APP, PAPER_TICKET, QR_CODE)"),("mediumId",*sch("Text"),"Unique identifier or number of the physical or digital medium")]},
    {"name":"FareProduct","description":"A purchasable entitlement to travel defining conditions of use, validity, and applicable passenger categories.","related":[("beckn:Offer","owl:equivalentClass","Exact"),("schema:Offer","rdfs:seeAlso","Related"),("schema:Product","rdfs:seeAlso","Related")],"parent":("Offer","core"),"own_props":[("fareProductId",*sch("Text"),"Unique identifier for the fare product"),("riderCategoryId",*mob_type("RiderCategory"),"Passenger category eligible for this fare product"),("durationType",*sch("Text"),"Duration basis (e.g. SINGLE_TRIP, DAILY, MONTHLY)"),("mediaDuration",*sch("Duration"),"Duration for which the fare product is valid"),("fixedStartDate",*sch("DateTime"),"Fixed start date for calendar-based fare products")]},
    {"name":"FareResult","description":"The calculated fare for a requested trip, returned as part of a trip planning or fare enquiry response.","related":[("beckn:Offer","rdfs:subClassOf","Subclass"),("schema:PriceSpecification","rdfs:seeAlso","Related")],"parent":("Offer","core"),"own_props":[("totalAmount",*sch("Number"),"Total calculated fare amount"),("currency",*sch("Text"),"ISO 4217 currency code"),("fareProducts",*mob_type("FareProduct"),"Fare products applicable to the result"),("fareBreakup",*mob_type("FareBreakup"),"Itemised breakdown of the calculated fare")]},
    {"name":"FareTransferRule","description":"A rule defining how fares from different legs are combined when a passenger makes a transfer between services.","related":[("beckn:Policy","rdfs:subClassOf","Subclass"),("mobility:FareProduct","rdfs:seeAlso","Related")],"parent":("Policy","core"),"own_props":[("fareProductId",*sch("Text"),"Identifier of the fare product this transfer rule applies to"),("transferCount",*sch("Number"),"Number of transfers permitted under this rule"),("durationLimit",*sch("Number"),"Maximum duration in minutes for the transfer window"),("fareTransferType",*sch("Text"),"Type of fare adjustment on transfer (e.g. FREE, DISCOUNT, ADDITIONAL_FARE)")]},
    {"name":"Feed","description":"A data publication providing transit or mobility information in a standardised format for consumption by applications or planners.","related":[("beckn:Catalog","rdfs:subClassOf","Subclass"),("schema:DataFeed","rdfs:seeAlso","Related")],"parent":("Catalog","core"),"own_props":[("feedType",*sch("Text"),"Format of the feed (e.g. GTFS, GTFS_RT, GBFS, NeTEx)"),("feedId",*sch("Text"),"Unique identifier for the feed"),("feedPublisher",*sch("Text"),"Name of the organisation publishing this feed"),("feedLanguage",*sch("Text"),"BCP-47 language code for the feed content"),("feedStartDate",*sch("DateTime"),"Date from which the feed data is valid"),("feedEndDate",*sch("DateTime"),"Date until which the feed data is valid")]},
    {"name":"Feedback","description":"A passenger's qualitative assessment or textual comment about a completed trip, driver, or mobility service.","related":[("beckn:Feedback","owl:equivalentClass","Exact")],"parent":("Feedback","core"),"own_props":[("feedbackText",*sch("Text"),"Textual content of the feedback"),("feedbackType",*sch("Text"),"Category of feedback (e.g. COMPLIMENT, COMPLAINT, SUGGESTION)"),("serviceComponent",*sch("Text"),"Component of the service being reviewed (e.g. DRIVER, VEHICLE, APP)")]},
    {"name":"FlightSegment","description":"A single non-stop flight operated between two airports, forming a unit of an air travel itinerary.","related":[("beckn:Fulfillment","rdfs:subClassOf","Subclass"),("mobility:Leg","rdfs:subClassOf","Subclass"),("schema:Flight","rdfs:seeAlso","Related")],"parent":("Leg","mobility"),"own_props":[("flightNumber",*sch("Text"),"IATA/ICAO flight number (e.g. AI101)"),("departureAirport",*sch("Text"),"IATA airport code of the departure airport"),("arrivalAirport",*sch("Text"),"IATA airport code of the arrival airport"),("departureTime",*sch("DateTime"),"Scheduled local departure date and time"),("arrivalTime",*sch("DateTime"),"Scheduled local arrival date and time"),("airline",*sch("Text"),"IATA airline code of the operating carrier"),("aircraftType",*sch("Text"),"IATA aircraft type code")]},
    {"name":"Frequency","description":"A headway-based service specification indicating how often a vehicle runs on a route within a given time window.","related":[("beckn:Constraint","rdfs:subClassOf","Subclass")],"parent":("Constraint","core"),"own_props":[("headwaySecs",*sch("Number"),"Time in seconds between consecutive vehicle departures"),("exactTimes",*sch("Boolean"),"Whether departures are at exact scheduled times (true) or headway-based (false)"),("startTime",*sch("Text"),"Time at which this frequency period begins (HH:MM:SS)"),("endTime",*sch("Text"),"Time at which this frequency period ends (HH:MM:SS)")]},
    {"name":"FulfillmentStop","description":"A specific location associated with a fulfillment (trip or journey) at which passengers board, alight, or transfer between services.","related":[("beckn:FulfillmentStop","rdfs:subClassOf","Subclass")],"parent":("FulfillmentStop","conceptual"),"own_props":[("stopType",*sch("Text"),"Role of this stop in the fulfillment (START, END, INTERMEDIATE)"),("scheduledTime",*sch("DateTime"),"Scheduled arrival or departure time at this stop"),("actualTime",*sch("DateTime"),"Actual arrival or departure time at this stop"),("stopRef",*mob_type("Stop"),"Reference to the Stop entity for this fulfillment stop"),("passengerCount",*mob_type("PassengerCount"),"Passenger count at this fulfillment stop")]},
    {"name":"GeneralMessageDelivery","description":"A real-time delivery of textual messages or alerts related to service disruptions or passenger information.","related":[("beckn:Alert","rdfs:subClassOf","Subclass"),("mobility:Alert","rdfs:seeAlso","Related")],"parent":("Alert","core"),"own_props":[("responseTimestamp",*sch("DateTime"),"Timestamp of this general message delivery"),("infoMessages",*mob_type("Alert"),"List of informational messages in this delivery"),("channel",*sch("Text"),"Distribution channel for this message (e.g. WEB, SMS, APP)")]},
    {"name":"Geofence","description":"A virtual geographic boundary used to define service areas, restricted zones, or operational boundaries for mobility assets.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("Location","core"),"own_props":[("geofenceType",*sch("Text"),"Type of geofence (e.g. SERVICE_AREA, RESTRICTED, SPEED_LIMIT)"),("geometry",*core_type("GeoJSONGeometry"),"GeoJSON geometry defining the geofence boundary"),("rules",*sch("Text"),"Operational rules applied within this geofence")]},
    {"name":"GeofencingZone","description":"A virtual geographic boundary used to define operational areas, speed limits, parking rules, or restrictions for shared mobility services.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass"),("schema:GeoShape","rdfs:seeAlso","Related")],"parent":("Location","core"),"own_props":[("featureType",*sch("Text"),"Type of geofencing zone feature (e.g. parking, restricted, slow)"),("geometry",*core_type("GeoJSONGeometry"),"GeoJSON geometry defining the zone boundary"),("rideAllowed",*sch("Boolean"),"Whether riding is permitted within this zone"),("rideThroughAllowed",*sch("Boolean"),"Whether riding through without stopping is permitted"),("stationParking",*sch("Boolean"),"Whether docking at a station is required to end a trip here")]},
    {"name":"Incident","description":"A reported event on the transport network that affects normal service operations, such as a disruption, roadblock, or infrastructure failure.","related":[("beckn:Alert","rdfs:subClassOf","Subclass")],"parent":("Alert","core"),"own_props":[("incidentType",*sch("Text"),"Type of incident (e.g. DISRUPTION, ROADBLOCK, MAINTENANCE)"),("severity",*sch("Text"),"Severity level of the incident (LOW, MEDIUM, HIGH)"),("affectedArea",*core_type("Location"),"Geographic area affected by the incident"),("startTime",*sch("DateTime"),"Date and time the incident started"),("endTime",*sch("DateTime"),"Expected or actual end date and time of the incident")]},
    {"name":"Interchange","description":"A planned transfer connection point where passengers switch between two or more transport services, with defined timing constraints.","related":[("beckn:FulfillmentStop","rdfs:subClassOf","Subclass"),("mobility:Stop","rdfs:subClassOf","Subclass")],"parent":("Stop","mobility"),"own_props":[("minTransferTime",*sch("Number"),"Minimum required transfer time in seconds"),("transferType",*sch("Text"),"Type of interchange (e.g. TIMED, GUARANTEED, IN_SEAT)"),("fromStopId",*mob_type("Stop"),"The stop passengers transfer from"),("toStopId",*mob_type("Stop"),"The stop passengers transfer to"),("fromTripId",*mob_type("VehicleJourney"),"The vehicle journey passengers transfer from"),("toTripId",*mob_type("VehicleJourney"),"The vehicle journey passengers transfer to")]},
    {"name":"Itinerary","description":"A complete planned trip containing an ordered sequence of legs, including transfer points, durations, and timing.","related":[("beckn:Contract","rdfs:subClassOf","Subclass"),("schema:Trip","rdfs:seeAlso","Related")],"parent":("Contract","core"),"own_props":[("legs",*mob_type("Leg"),"Ordered list of legs making up this itinerary"),("totalDuration",*sch("Duration"),"Total travel duration for the itinerary"),("totalDistance",*sch("Number"),"Total distance in metres for the itinerary"),("transferCount",*sch("Number"),"Number of transfers in the itinerary"),("departureTime",*sch("DateTime"),"Departure time of the first leg"),("arrivalTime",*sch("DateTime"),"Arrival time of the last leg")]},
    {"name":"ItineraryElement","description":"A component of an aviation itinerary such as a flight segment, ground transport leg, or ancillary service.","related":[("beckn:ContractItem","rdfs:subClassOf","Subclass"),("mobility:Itinerary","rdfs:subClassOf","Subclass")],"parent":("ContractItem","core"),"own_props":[("elementType",*sch("Text"),"Type of itinerary element (FLIGHT, GROUND_TRANSPORT, ANCILLARY)"),("segmentRef",*mob_type("FlightSegment"),"Reference to a flight segment if this is a flight element"),("legRef",*mob_type("Leg"),"Reference to a transport leg if this is a surface element"),("sequence",*sch("Number"),"Sequential order of this element within the itinerary")]},
    {"name":"Journey","description":"A complete travel itinerary from origin to destination, potentially comprising multiple legs using different transport modes.","related":[("beckn:Contract","rdfs:subClassOf","Subclass"),("schema:Trip","rdfs:seeAlso","Related")],"parent":("Contract","core"),"own_props":[("origin",*core_type("Location"),"Origin location of the journey"),("destination",*core_type("Location"),"Destination location of the journey"),("departureTime",*sch("DateTime"),"Planned departure time"),("arrivalTime",*sch("DateTime"),"Planned arrival time"),("legs",*mob_type("Leg"),"Ordered list of legs comprising this journey")]},
    {"name":"Leg","description":"A single uninterrupted segment of a journey made using one transport mode or service between two consecutive locations.","related":[("beckn:Fulfillment","rdfs:subClassOf","Subclass"),("schema:Trip","rdfs:seeAlso","Related")],"parent":("Fulfillment","core"),"own_props":[("mode",*sch("Text"),"Transport mode for this leg (e.g. BUS, RAIL, WALK, BICYCLE)"),("origin",*core_type("Location"),"Start location of the leg"),("destination",*core_type("Location"),"End location of the leg"),("startTime",*sch("DateTime"),"Scheduled or actual start time of the leg"),("endTime",*sch("DateTime"),"Scheduled or actual end time of the leg"),("distance",*sch("Number"),"Distance of this leg in metres"),("headsign",*sch("Text"),"Destination sign text displayed on the vehicle"),("routeRef",*mob_type("Route"),"Reference to the route served on this leg")]},
    {"name":"Level","description":"A floor or vertical level within a multi-level transit station or facility, used to define internal navigation paths.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("schema:Floor","rdfs:seeAlso","Related")],"parent":("Location","core"),"own_props":[("levelId",*sch("Text"),"Unique identifier for this level within the station"),("levelName",*sch("Text"),"Human-readable name of the level (e.g. Ground Floor, Level 1)"),("elevation",*sch("Number"),"Elevation of this level in metres above ground"),("stationRef",*mob_type("Station"),"Reference to the station this level belongs to")]},
    {"name":"Line","description":"A named, branded public transport service identified by a number or name, typically operating over one or more routes.","related":[("beckn:Item","rdfs:subClassOf","Subclass"),("transmodel:Line","owl:equivalentClass","Exact")],"parent":("Item","core"),"own_props":[("lineId",*sch("Text"),"GTFS or NeTEx identifier for the line"),("shortName",*sch("Text"),"Short public-facing name (e.g. 42, M1, Jubilee)"),("longName",*sch("Text"),"Full descriptive name of the line"),("lineType",*sch("Text"),"Mode of transport (e.g. BUS, SUBWAY, RAIL, FERRY)"),("color",*sch("Text"),"Hex colour code for line display on maps"),("textColor",*sch("Text"),"Hex colour code for text displayed on the line colour"),("operatorRef",*mob_type("Operator"),"Reference to the operator running this line"),("networkRef",*mob_type("Network"),"Reference to the network this line belongs to")]},
    {"name":"LocationGroup","description":"A set of geographic locations (stops or areas) that can collectively serve as an origin or destination for flexible transit services.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("Location","core"),"own_props":[("locationGroupId",*sch("Text"),"Unique identifier for the location group"),("locationGroupName",*sch("Text"),"Human-readable name for the location group"),("stops",*mob_type("Stop"),"Stops included in this location group")]},
    {"name":"LocationGroupStop","description":"An association between a stop and a location group, used in flexible transit service planning.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("mobility:Stop","rdfs:seeAlso","Related")],"parent":("Location","core"),"own_props":[("locationGroupId",*sch("Text"),"Identifier of the parent location group"),("stopId",*mob_type("Stop"),"Reference to the stop in this association")]},
    {"name":"LocationInformationRequest","description":"A request for details about a specific geographic location, stop, or point of interest in the transport network.","related":[("beckn:Intent","rdfs:subClassOf","Subclass"),("mobility:Place","rdfs:seeAlso","Related")],"parent":("Intent","core"),"own_props":[("requestType",*sch("Text"),"Type of location information requested (e.g. STOP, ADDRESS, POI)"),("locationName",*sch("Text"),"Name or keyword to search for"),("coordinates",*core_type("GeoJSONGeometry"),"Geographic coordinates to query around"),("radius",*sch("Number"),"Search radius in metres")]},
    {"name":"LostAndFoundItem","description":"An item that has been reported lost or found in connection with a transport service.","related":[("beckn:SupportRequest","rdfs:subClassOf","Subclass")],"parent":("SupportRequest","core"),"own_props":[("itemType",*sch("Text"),"Type of the lost/found item (e.g. BAG, PHONE, WALLET)"),("itemDescription",*sch("Text"),"Detailed description of the item"),("foundAt",*sch("DateTime"),"Date and time the item was found"),("lostAt",*sch("DateTime"),"Date and time the item was lost"),("vehicleRef",*mob_type("Vehicle"),"Vehicle on which the item was found or lost")]},
    {"name":"MonitoredCall","description":"A real-time arrival or departure prediction for a specific vehicle at a specific stop within a monitored journey.","related":[("beckn:Tracking","rdfs:subClassOf","Subclass"),("mobility:StopTime","rdfs:seeAlso","Related")],"parent":("Tracking","core"),"own_props":[("stopPointRef",*mob_type("StopPoint"),"Reference to the stop point for this call"),("visitNumber",*sch("Number"),"Visit sequence number for loop services"),("vehicleAtStop",*sch("Boolean"),"Whether the vehicle is currently at the stop"),("expectedArrivalTime",*sch("DateTime"),"Predicted arrival time at this stop"),("expectedDepartureTime",*sch("DateTime"),"Predicted departure time from this stop"),("aimedArrivalTime",*sch("DateTime"),"Scheduled arrival time from the timetable"),("aimedDepartureTime",*sch("DateTime"),"Scheduled departure time from the timetable"),("arrivalStatus",*sch("Text"),"Arrival status (e.g. onTime, delayed, early)"),("departureStatus",*sch("Text"),"Departure status (e.g. onTime, delayed, early)")]},
    {"name":"MonitoredVehicleJourney","description":"A real-time representation of a vehicle journey being actively tracked, including position and schedule adherence data.","related":[("beckn:Tracking","rdfs:subClassOf","Subclass"),("mobility:VehicleJourney","rdfs:subClassOf","Subclass")],"parent":("VehicleJourney","mobility"),"own_props":[("lineRef",*mob_type("Line"),"Reference to the line being monitored"),("directionRef",*mob_type("Direction"),"Direction of travel being monitored"),("vehicleRef",*mob_type("VehicleDescriptor"),"Reference to the monitored vehicle"),("vehicleLocation",*mob_type("VehiclePosition"),"Current geographic position of the vehicle"),("bearing",*sch("Number"),"Compass bearing of travel in degrees"),("delay",*sch("Number"),"Delay in seconds relative to schedule (negative = early)"),("occupancy",*mob_type("OccupancyStatus"),"Current passenger occupancy of the vehicle")]},
    {"name":"Network","description":"A grouping of routes and lines operated under a common brand or authority, used for fare and operational management.","related":[("beckn:Catalog","rdfs:subClassOf","Subclass"),("schema:Organization","rdfs:seeAlso","Related")],"parent":("Catalog","core"),"own_props":[("networkId",*sch("Text"),"Unique identifier for the network"),("networkName",*sch("Text"),"Human-readable name of the network"),("operatorRef",*mob_type("Operator"),"Operator(s) running services within this network"),("lines",*mob_type("Line"),"Lines that belong to this network")]},
    {"name":"NoShowPolicy","description":"Rules governing the consequences and fees applied when a passenger fails to appear for a confirmed transport service booking.","related":[("beckn:Policy","rdfs:subClassOf","Subclass")],"parent":("Policy","core"),"own_props":[("noShowFee",*sch("Number"),"Flat fee charged for a no-show"),("gracePeriodMinutes",*sch("Number"),"Grace period in minutes before a no-show is recorded"),("currency",*sch("Text"),"ISO 4217 currency code for the no-show fee")]},
    {"name":"OccupancyStatus","description":"An indicator of the current passenger load level of a vehicle, such as empty, many seats available, or full.","related":[("beckn:State","rdfs:subClassOf","Subclass"),("schema:ItemAvailability","rdfs:seeAlso","Related")],"parent":("State","core"),"own_props":[("occupancyLevel",*sch("Text"),"Occupancy level (EMPTY, MANY_SEATS_AVAILABLE, FEW_SEATS_AVAILABLE, STANDING_ROOM_ONLY, FULL, NOT_ACCEPTING_PASSENGERS)"),("availableSeats",*sch("Number"),"Estimated number of seats currently available"),("totalSeats",*sch("Number"),"Total seating capacity of the vehicle")]},
    {"name":"Operator","description":"An organization that provides and operates public transport or shared mobility services under a defined service agreement.","related":[("beckn:Provider","owl:equivalentClass","Exact"),("transmodel:Operator","owl:equivalentClass","Exact"),("schema:Organization","rdfs:subClassOf","Subclass")],"parent":("Provider","core"),"own_props":[("operatorId",*sch("Text"),"Unique identifier for the operator"),("operatingRegions",*sch("Text"),"Geographic regions where the operator provides services"),("licenseNumber",*sch("Text"),"Regulatory license or accreditation number"),("contactInfo",*sch("Text"),"Public contact information for the operator")]},
    {"name":"Passenger","description":"A person who travels using a transport service and is identified in a booking or travel document.","related":[("beckn:Participant","rdfs:subClassOf","Subclass"),("schema:Person","rdfs:subClassOf","Subclass")],"parent":("Participant","core"),"own_props":[("passengerId",*sch("Text"),"Unique identifier for the passenger in this booking"),("passengerType",*sch("Text"),"Classification of passenger (e.g. ADULT, CHILD, SENIOR, STUDENT)"),("specialRequirements",*sch("Text"),"Accessibility or special assistance requirements")]},
    {"name":"PassengerCount","description":"The measured number of passengers currently aboard a vehicle, used for real-time capacity and load management.","related":[("beckn:Quantity","rdfs:subClassOf","Subclass")],"parent":("Quantity","core"),"own_props":[("boardingCount",*sch("Number"),"Number of passengers who boarded at the last stop"),("alightingCount",*sch("Number"),"Number of passengers who alighted at the last stop"),("currentOccupancy",*sch("Number"),"Total number of passengers currently on board")]},
    {"name":"PassengerGroup","description":"A collection of passengers traveling together as a group, with a group size and a designated lead passenger.","related":[("beckn:Quantity","rdfs:subClassOf","Subclass")],"parent":("Quantity","core"),"own_props":[("groupId",*sch("Text"),"Unique identifier for this passenger group"),("groupSize",*sch("Number"),"Total number of passengers in the group"),("leadPassenger",*mob_type("Passenger"),"The lead or primary passenger for the group")]},
    {"name":"Pathway","description":"A connection between two points within a transit station (e.g., stairway, elevator, walkway) used for indoor navigation and accessibility routing.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("Location","core"),"own_props":[("pathwayId",*sch("Text"),"Unique identifier for the pathway"),("fromStopId",*mob_type("Stop"),"Stop at the start of the pathway"),("toStopId",*mob_type("Stop"),"Stop at the end of the pathway"),("pathwayMode",*sch("Text"),"Type of pathway (1=walkway, 2=stairs, 3=moving_sidewalk, 4=escalator, 5=elevator, 6=fare_gate, 7=exit_gate)"),("isBidirectional",*sch("Boolean"),"Whether the pathway can be traversed in both directions"),("length",*sch("Number"),"Length of the pathway in metres"),("traversalTime",*sch("Number"),"Time in seconds to traverse the pathway")]},
    {"name":"Pattern","description":"A unique sequence of stops visited by trips on a route, grouping trips with identical stop sequences and timing structures.","related":[("beckn:Item","rdfs:subClassOf","Subclass"),("transmodel:JourneyPattern","rdfs:seeAlso","Related")],"parent":("Item","core"),"own_props":[("patternId",*sch("Text"),"Unique identifier for the journey pattern"),("routeRef",*mob_type("Route"),"Reference to the route this pattern belongs to"),("directionId",*sch("Text"),"Direction of travel (0 or 1)"),("stops",*mob_type("Stop"),"Ordered list of stops in this pattern"),("shapeRef",*mob_type("Shape"),"Reference to the geographic shape of this pattern")]},
    {"name":"PickupDropoffPoint","description":"A designated location used as a pickup or dropoff point for passengers in a ride-hailing or demand-responsive transport service.","related":[("beckn:FulfillmentStop","rdfs:subClassOf","Subclass")],"parent":("FulfillmentStop","conceptual"),"own_props":[("pdpType",*sch("Text"),"Type of point (PICKUP, DROPOFF, BOTH)"),("landmark",*sch("Text"),"Nearby landmark or reference point"),("accessNotes",*sch("Text"),"Instructions for accessing this pickup/dropoff point")]},
    {"name":"PickupPolicy","description":"A set of rules governing the locations and conditions under which passengers may be picked up for a ride-hailing or on-demand transport service.","related":[("beckn:Policy","rdfs:subClassOf","Subclass")],"parent":("Policy","core"),"own_props":[("allowedPickupAreas",*mob_type("Geofence"),"Geographic areas where pickup is permitted"),("pickupConditions",*sch("Text"),"Conditions that must be met for a valid pickup"),("pickupNote",*sch("Text"),"Customer-facing note about pickup rules")]},
    {"name":"Place","description":"A named or unnamed geographic location relevant to mobility, such as an address, point of interest, stop, or area.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("schema:Place","owl:equivalentClass","Exact"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("Location","core"),"own_props":[("placeType",*sch("Text"),"Type of place (e.g. ADDRESS, STOP, POI, STATION, AREA)"),("placeName",*sch("Text"),"Human-readable name of the place")]},
    {"name":"PlaceRequest","description":"A request for a specific accommodation or seat assignment within a transport service during the booking process.","related":[("beckn:ContractItem","rdfs:subClassOf","Subclass")],"parent":("ContractItem","core"),"own_props":[("accommodationType",*sch("Text"),"Type of accommodation requested (e.g. SEAT, BERTH, COMPARTMENT)"),("preferences",*sch("Text"),"Passenger preferences (e.g. window, aisle, quiet zone)"),("seatRef",*mob_type("Seat"),"Specific seat requested, if applicable")]},
    {"name":"Plan","description":"A journey planning response containing one or more itinerary options for a given trip request.","related":[("beckn:Catalog","rdfs:subClassOf","Subclass")],"parent":("Catalog","core"),"own_props":[("requestedTime",*sch("DateTime"),"The departure or arrival time that was requested"),("itineraries",*mob_type("Itinerary"),"List of itinerary options returned in the plan"),("from",*core_type("Location"),"Origin location for this plan"),("to",*core_type("Location"),"Destination location for this plan")]},
    {"name":"PlanningResult","description":"The output of a MaaS platform planning request, listing available transport options for a requested trip.","related":[("beckn:Catalog","rdfs:subClassOf","Subclass")],"parent":("Catalog","core"),"own_props":[("origin",*core_type("Location"),"Origin location for the planning query"),("destination",*core_type("Location"),"Destination location for the planning query"),("options",*mob_type("RideOption"),"Available transport options returned"),("itineraries",*mob_type("Itinerary"),"Multi-modal itinerary options if applicable")]},
    {"name":"PricingModel","description":"The pricing structure or tariff model used by a mobility service provider to calculate fares.","related":[("beckn:Offer","rdfs:subClassOf","Subclass")],"parent":("Offer","core"),"own_props":[("modelType",*sch("Text"),"Type of pricing model (e.g. FIXED, METERED, SUBSCRIPTION, SURGE)"),("baseRate",*sch("Number"),"Base fare charged at the start of a trip"),("perMinuteRate",*sch("Number"),"Additional charge per minute of travel"),("perKmRate",*sch("Number"),"Additional charge per kilometre of travel"),("currency",*sch("Text"),"ISO 4217 currency code"),("surgeEnabled",*sch("Boolean"),"Whether surge pricing can be applied")]},
    {"name":"Prognosis","description":"A real-time prediction of a vehicle's arrival or departure time at a stop, including an indication of prediction confidence.","related":[("beckn:Tracking","rdfs:subClassOf","Subclass"),("mobility:StopTime","rdfs:seeAlso","Related")],"parent":("Tracking","core"),"own_props":[("scheduledTime",*sch("DateTime"),"Timetabled scheduled time"),("estimatedTime",*sch("DateTime"),"Predicted actual time"),("certainty",*sch("Text"),"Confidence of the prognosis (e.g. real, prognosis, calculated, unknown)"),("delaySeconds",*sch("Number"),"Delay in seconds relative to the scheduled time")]},
    {"name":"Provider","description":"A mobility service provider registered on a MaaS platform, offering transport options to end users.","related":[("beckn:Provider","owl:equivalentClass","Exact"),("schema:Organization","rdfs:subClassOf","Subclass")],"parent":("Provider","core"),"own_props":[("providerId",*sch("Text"),"Unique identifier for the mobility provider"),("providerName",*sch("Text"),"Human-readable name of the provider"),("categories",*sch("Text"),"Categories of mobility services offered (e.g. RIDE_HAILING, BIKE_SHARE)")]},
    {"name":"Quay","description":"A specific platform, bay, or boarding area within a Stop Place at which passengers board or alight from a vehicle.","related":[("beckn:FulfillmentStop","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("FulfillmentStop","conceptual"),"own_props":[("quayId",*sch("Text"),"Unique identifier for the quay"),("publicCode",*sch("Text"),"Publicly displayed platform or bay code"),("quayType",*sch("Text"),"Type of quay (e.g. RAIL_PLATFORM, BUS_BAY, FERRY_BERTH)"),("stopPlaceRef",*mob_type("StopPlace"),"Reference to the parent Stop Place")]},
    {"name":"Rating","description":"A numerical or categorical score assigned by a user to a driver, vehicle, or mobility service experience.","related":[("beckn:RatingInput","rdfs:subClassOf","Subclass")],"parent":("RatingInput","core"),"own_props":[("ratedEntityId",*sch("Text"),"Identifier of the entity being rated (driver, vehicle, service)"),("ratedEntityType",*sch("Text"),"Type of entity being rated (DRIVER, VEHICLE, SERVICE)"),("comment",*sch("Text"),"Optional text comment accompanying the rating")]},
    {"name":"Receipt","description":"A payment receipt issued to a passenger upon completion and settlement of a transport service trip.","related":[("beckn:Invoice","owl:equivalentClass","Exact"),("schema:Invoice","rdfs:seeAlso","Related")],"parent":("Invoice","core"),"own_props":[("receiptId",*sch("Text"),"Unique identifier for the receipt"),("issuedAt",*sch("DateTime"),"Timestamp when the receipt was issued"),("paymentMethod",*sch("Text"),"Method of payment used (e.g. CARD, UPI, CASH, WALLET)"),("tripRef",*mob_type("Trip"),"Reference to the trip for which this receipt is issued")]},
    {"name":"Review","description":"A written review or opinion submitted by a passenger about a completed mobility service, driver, or vehicle.","related":[("beckn:RatingInput","rdfs:subClassOf","Subclass")],"parent":("RatingInput","core"),"own_props":[("reviewText",*sch("Text"),"The written text of the review"),("reviewedAt",*sch("DateTime"),"Date and time the review was submitted"),("reviewer",*mob_type("Rider"),"The passenger who submitted this review")]},
    {"name":"RideOption","description":"A specific ride-hailing vehicle category and pricing option presented to a passenger in response to a ride request.","related":[("beckn:Offer","rdfs:subClassOf","Subclass")],"parent":("Offer","core"),"own_props":[("vehicleType",*mob_type("VehicleCategory"),"Category of vehicle for this ride option"),("estimatedArrival",*sch("DateTime"),"Estimated vehicle arrival time at the pickup point"),("estimatedDuration",*sch("Duration"),"Estimated trip duration"),("estimatedDistance",*sch("Number"),"Estimated trip distance in kilometres"),("pricingModel",*mob_type("PricingModel"),"Pricing model applicable to this ride option")]},
    {"name":"RideRequest","description":"A passenger's request for an on-demand transport service between two points, specifying origin, destination, and travel preferences.","related":[("beckn:Intent","rdfs:subClassOf","Subclass")],"parent":("Intent","core"),"own_props":[("origin",*core_type("Location"),"Pickup location for the ride"),("destination",*core_type("Location"),"Dropoff location for the ride"),("requestedTime",*sch("DateTime"),"Requested pickup time"),("passengerCount",*sch("Number"),"Number of passengers"),("vehiclePreference",*mob_type("VehicleCategory"),"Preferred vehicle category")]},
    {"name":"Rider","description":"A person using a shared mobility service (such as a bike-share, scooter, or car-share) who has a registered account with the provider.","related":[("beckn:Participant","rdfs:subClassOf","Subclass"),("schema:Person","rdfs:subClassOf","Subclass")],"parent":("Participant","core"),"own_props":[("riderId",*sch("Text"),"Unique identifier for the rider account"),("preferredPaymentMethod",*sch("Text"),"Rider preferred payment method"),("membershipPlan",*sch("Text"),"Active membership or subscription plan")]},
    {"name":"RiderCategory","description":"A classification of passenger type (e.g., adult, child, senior, student) used to determine applicable fare entitlements.","related":[("beckn:CategoryCode","rdfs:subClassOf","Subclass"),("schema:Person","rdfs:subClassOf","Subclass")],"parent":("CategoryCode","core"),"own_props":[("riderCategoryId",*sch("Text"),"Unique identifier for the rider category"),("eligibilityRules",*sch("Text"),"Rules defining who qualifies for this rider category"),("proofRequired",*sch("Text"),"Type of proof required to qualify (e.g. student ID, senior card)")]},
    {"name":"Route","description":"The physical or logical path followed by a transport service, defined as an ordered sequence of stops or waypoints.","related":[("beckn:Item","rdfs:subClassOf","Subclass"),("transmodel:Route","rdfs:seeAlso","Related"),("schema:Trip","rdfs:seeAlso","Related")],"parent":("Item","core"),"own_props":[("routeId",*sch("Text"),"Unique identifier for the route"),("shortName",*sch("Text"),"Short public-facing name (e.g. 42A)"),("longName",*sch("Text"),"Full descriptive name of the route"),("routeType",*sch("Text"),"Mode of transport (e.g. BUS, RAIL, TRAM, FERRY)"),("operatorRef",*mob_type("Operator"),"Operator providing this route"),("networkRef",*mob_type("Network"),"Network this route belongs to")]},
    {"name":"SafetyPolicy","description":"A set of rules, protocols, and standards governing safety requirements for drivers, vehicles, and passengers on a mobility platform.","related":[("beckn:Policy","rdfs:subClassOf","Subclass")],"parent":("Policy","core"),"own_props":[("safetyInstructions",*sch("Text"),"Instructions and guidelines for passenger and driver safety"),("emergencyContact",*mob_type("ContactHandle"),"Emergency contact handle for safety incidents"),("insuranceCoverage",*sch("Text"),"Description of insurance coverage under this policy")]},
    {"name":"SalesOfferPackage","description":"A combination of one or more fare products bundled for sale through a specific distribution channel.","related":[("beckn:Offer","rdfs:subClassOf","Subclass"),("schema:Offer","rdfs:seeAlso","Related")],"parent":("Offer","core"),"own_props":[("fareProducts",*mob_type("FareProduct"),"Fare products included in this sales package"),("distributions",*mob_type("DistributionChannel"),"Channels through which this package can be purchased"),("conditionsOfTravel",*sch("Text"),"Conditions applying to the use of this package")]},
    {"name":"Seat","description":"A specific seat position reserved or assigned to a passenger on a flight, train, or other transport service.","related":[("beckn:Entitlement","rdfs:subClassOf","Subclass"),("schema:Seat","rdfs:seeAlso","Related")],"parent":("Entitlement","core"),"own_props":[("seatId",*sch("Text"),"Unique identifier or label for the seat"),("row",*sch("Text"),"Row designation (number or letter)"),("column",*sch("Text"),"Column or seat letter within the row"),("seatType",*sch("Text"),"Type of seat (e.g. WINDOW, AISLE, MIDDLE, UPPER_BERTH)"),("seatCharacteristics",*sch("Text"),"Additional characteristics (e.g. EXTRA_LEGROOM, QUIET_ZONE, ACCESSIBLE)"),("deckLevel",*sch("Text"),"Deck or level (UPPER, LOWER, MAIN)")]},
    {"name":"Segment","description":"A portion of a rail journey operated continuously by a single carrier between two consecutive stops or stations.","related":[("beckn:Fulfillment","rdfs:subClassOf","Subclass"),("mobility:Leg","rdfs:subClassOf","Subclass")],"parent":("Leg","mobility"),"own_props":[("carrierCode",*sch("Text"),"Code of the carrier operating this segment"),("segmentNumber",*sch("Number"),"Sequence number of this segment within the journey"),("trainNumber",*sch("Text"),"Train or service number for this segment"),("coachNumber",*sch("Text"),"Coach or carriage number")]},
    {"name":"ServiceCalendar","description":"A schedule defining on which dates a transport service operates, including regular service days and exceptional dates.","related":[("beckn:TimePeriod","rdfs:subClassOf","Subclass"),("schema:Schedule","rdfs:seeAlso","Related")],"parent":("TimePeriod","core"),"own_props":[("serviceId",*sch("Text"),"Unique identifier for the service calendar"),("monday",*sch("Boolean"),"Whether service operates on Mondays"),("tuesday",*sch("Boolean"),"Whether service operates on Tuesdays"),("wednesday",*sch("Boolean"),"Whether service operates on Wednesdays"),("thursday",*sch("Boolean"),"Whether service operates on Thursdays"),("friday",*sch("Boolean"),"Whether service operates on Fridays"),("saturday",*sch("Boolean"),"Whether service operates on Saturdays"),("sunday",*sch("Boolean"),"Whether service operates on Sundays"),("exceptionDates",*sch("DateTime"),"Dates on which service is added or removed from the regular schedule")]},
    {"name":"ServiceClass","description":"A classification of the level of service offered by a transport service, such as economy, business, or first class.","related":[("beckn:CategoryCode","rdfs:subClassOf","Subclass")],"parent":("CategoryCode","core"),"own_props":[("serviceClassCode",*sch("Text"),"Code identifying the service class (e.g. ECONOMY, BUSINESS, FIRST)"),("features",*sch("ItemList"),"List of features and amenities included in this service class")]},
    {"name":"ServiceDelivery","description":"The top-level response container in SIRI encapsulating one or more real-time data delivery types.","related":[("beckn:Catalog","rdfs:subClassOf","Subclass")],"parent":("Catalog","core"),"own_props":[("responseTimestamp",*sch("DateTime"),"Timestamp when this service delivery was generated"),("producerRef",*sch("Text"),"Identifier of the system producing this delivery"),("requestMessageRef",*sch("Text"),"Reference to the request that triggered this delivery"),("stopMonitoring",*mob_type("StopMonitoring"),"Stop monitoring delivery payloads"),("vehicleMonitoring",*mob_type("VehicleMonitoringDelivery"),"Vehicle monitoring delivery payloads"),("estimatedTimetable",*mob_type("EstimatedTimetableDelivery"),"Estimated timetable delivery payloads")]},
    {"name":"Shape","description":"The geographic path traced by a vehicle along a route, represented as an ordered sequence of geographic coordinates.","related":[("beckn:GeoJSONGeometry","rdfs:subClassOf","Subclass"),("geo:Geometry","rdfs:subClassOf","Subclass")],"parent":("GeoJSONGeometry","core"),"own_props":[("shapeId",*sch("Text"),"Unique identifier for the shape"),("distanceTraveled",*sch("Number"),"Distance along the shape in metres up to this point")]},
    {"name":"Station","description":"A major transit facility serving as a hub for one or more transport modes, typically offering waiting areas, ticketing, and interchange facilities.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("schema:CivicStructure","rdfs:subClassOf","Subclass"),("schema:TrainStation","rdfs:seeAlso","Related"),("schema:BusStation","rdfs:seeAlso","Related")],"parent":("Location","core"),"own_props":[("stationId",*sch("Text"),"Unique identifier for the station"),("stationName",*sch("Text"),"Human-readable name of the station"),("stationType",*sch("Text"),"Primary transport mode served (e.g. RAIL, BUS, METRO, FERRY)"),("platforms",*mob_type("Quay"),"Platforms or quays within this station"),("levels",*mob_type("Level"),"Levels or floors within the station"),("pathways",*mob_type("Pathway"),"Internal navigation pathways within the station")]},
    {"name":"StationInformation","description":"Static descriptive information about a shared mobility docking station, including its location, capacity, and features.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("schema:CivicStructure","rdfs:subClassOf","Subclass")],"parent":("Location","core"),"own_props":[("stationId",*sch("Text"),"Unique identifier for the docking station"),("shortName",*sch("Text"),"Shortened name of the station for display"),("capacity",*sch("Number"),"Total number of docking points at this station"),("hasKiosk",*sch("Boolean"),"Whether this station has a kiosk for key cards or passes"),("rentalMethods",*sch("Text"),"Methods by which bikes can be rented (e.g. KEY, CREDITCARD, APP)"),("regionId",*sch("Text"),"Identifier of the system region this station belongs to")]},
    {"name":"StationStatus","description":"The real-time operational state of a shared mobility station, including the number of available docks and vehicles.","related":[("beckn:State","rdfs:subClassOf","Subclass"),("schema:ItemAvailability","rdfs:seeAlso","Related")],"parent":("State","core"),"own_props":[("stationId",*sch("Text"),"Unique identifier of the station being reported"),("numBikesAvailable",*sch("Number"),"Number of bikes currently available for rental"),("numDocksAvailable",*sch("Number"),"Number of empty docking points currently available"),("isInstalled",*sch("Boolean"),"Whether the station is physically installed and operational"),("isRenting",*sch("Boolean"),"Whether the station is currently renting bikes"),("isReturning",*sch("Boolean"),"Whether the station is currently accepting bike returns"),("lastReported",*sch("DateTime"),"Timestamp of the last status update for this station")]},
    {"name":"Stop","description":"A designated location where vehicles stop to allow passengers to board or alight from a transport service.","related":[("beckn:FulfillmentStop","rdfs:subClassOf","Subclass"),("schema:BusStop","rdfs:seeAlso","Related"),("transmodel:ScheduledStopPoint","rdfs:seeAlso","Related"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("FulfillmentStop","conceptual"),"own_props":[("stopId",*sch("Text"),"Unique identifier for the stop"),("stopCode",*sch("Text"),"Short public-facing code for the stop"),("stopName",*sch("Text"),"Human-readable name of the stop"),("locationType",*sch("Text"),"Classification of location (0=stop, 1=station, 2=entrance, 3=generic_node, 4=boarding_area)"),("parentStation",*mob_type("Station"),"Reference to the parent station if this is a platform"),("wheelchairBoarding",*sch("Text"),"Wheelchair accessibility (0=no info, 1=accessible, 2=not accessible)")]},
    {"name":"StopArea","description":"A group of stops that collectively define a zone from which a demand-responsive service may pick up or drop off passengers.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("Location","core"),"own_props":[("areaId",*sch("Text"),"Unique identifier for the stop area"),("areaName",*sch("Text"),"Human-readable name of the stop area"),("stops",*mob_type("Stop"),"Stops contained within this area"),("geometry",*core_type("GeoJSONGeometry"),"GeoJSON geometry defining the area boundary")]},
    {"name":"StopEvent","description":"A departure or arrival event at a stop, used to retrieve the next or previous vehicle movements at a specific location.","related":[("beckn:FulfillmentStop","rdfs:subClassOf","Subclass"),("beckn:DiscoveryIntent","rdfs:subClassOf","Subclass"),("mobility:StopTime","rdfs:seeAlso","Related")],"parent":("FulfillmentStop","conceptual"),"own_props":[("stopEventType",*sch("Text"),"Type of event (DEPARTURE, ARRIVAL)"),("timetabledTime",*sch("DateTime"),"Scheduled time for the event"),("estimatedTime",*sch("DateTime"),"Estimated actual time for the event"),("serviceJourneyRef",*mob_type("VehicleJourney"),"Reference to the vehicle journey for this event"),("stopPointRef",*mob_type("StopPoint"),"Reference to the stop point where the event occurs")]},
    {"name":"StopMonitoring","description":"A real-time data service providing predicted arrivals and departures of vehicles at a specific stop.","related":[("beckn:Tracking","rdfs:subClassOf","Subclass"),("mobility:Stop","rdfs:seeAlso","Related")],"parent":("Tracking","core"),"own_props":[("stopRef",*mob_type("Stop"),"Reference to the stop being monitored"),("monitoredCalls",*mob_type("MonitoredCall"),"List of real-time arrival/departure calls at this stop"),("responseTimestamp",*sch("DateTime"),"Timestamp of this stop monitoring response")]},
    {"name":"StopPlace","description":"A physical location serving as a transit stop facility, comprising one or more quays, entrances, and associated infrastructure.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("Location","core"),"own_props":[("stopPlaceId",*sch("Text"),"Unique identifier for the stop place"),("stopPlaceType",*sch("Text"),"Type of stop place (e.g. AIRPORT, BUS_STATION, FERRY_STOP, METRO_STATION)"),("quays",*mob_type("Quay"),"Quays or boarding areas within this stop place"),("entrances",*mob_type("Pathway"),"Entrances and pathways into this stop place")]},
    {"name":"StopPoint","description":"An abstract or scheduled point in a public transport network at which passengers can board or alight from a service.","related":[("beckn:FulfillmentStop","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("FulfillmentStop","conceptual"),"own_props":[("stopPointId",*sch("Text"),"Unique identifier for the stop point"),("shortName",*sch("Text"),"Short display name or code"),("publicCode",*sch("Text"),"Publicly visible code displayed at the stop"),("stopAreaRef",*mob_type("StopArea"),"Reference to the stop area this point belongs to")]},
    {"name":"StopTime","description":"The scheduled arrival and departure times for a vehicle at a specific stop within a vehicle journey.","related":[("beckn:TimePeriod","rdfs:subClassOf","Subclass"),("transmodel:PassingTime","rdfs:seeAlso","Related")],"parent":("TimePeriod","core"),"own_props":[("arrivalTime",*sch("Text"),"Scheduled arrival time in HH:MM:SS format"),("departureTime",*sch("Text"),"Scheduled departure time in HH:MM:SS format"),("stopSequence",*sch("Number"),"Order of this stop within the vehicle journey"),("stopRef",*mob_type("Stop"),"Reference to the stop for this stop time"),("pickupType",*sch("Text"),"How passengers board at this stop (0=regular, 1=no_pickup, 2=phone_agency, 3=coordinate_with_driver)"),("dropOffType",*sch("Text"),"How passengers alight at this stop (0=regular, 1=no_drop_off, 2=phone_agency, 3=coordinate_with_driver)"),("distanceTraveled",*sch("Number"),"Distance from the route origin to this stop in metres")]},
    {"name":"StopTimeUpdate","description":"A real-time update to the predicted arrival or departure time of a vehicle at a specific stop within a journey.","related":[("beckn:Tracking","rdfs:subClassOf","Subclass"),("mobility:StopTime","rdfs:seeAlso","Related")],"parent":("Tracking","core"),"own_props":[("stopId",*mob_type("Stop"),"Reference to the stop being updated"),("stopSequence",*sch("Number"),"Sequence of this stop in the trip"),("arrivalDelay",*sch("Number"),"Arrival delay in seconds (negative = early)"),("departureDelay",*sch("Number"),"Departure delay in seconds (negative = early)"),("scheduleRelationship",*sch("Text"),"Relationship to schedule (SCHEDULED, SKIPPED, NO_DATA)")]},
    {"name":"SupportCase","description":"A formal customer service inquiry, complaint, or request raised by a passenger or provider through the mobility platform's support system.","related":[("beckn:SupportRequest","rdfs:subClassOf","Subclass")],"parent":("SupportRequest","core"),"own_props":[("caseType",*sch("Text"),"Type of support case (e.g. COMPLAINT, INQUIRY, TECHNICAL)"),("priority",*sch("Text"),"Priority level of the case (LOW, MEDIUM, HIGH, URGENT)"),("reportedAt",*sch("DateTime"),"Timestamp when the case was reported"),("resolvedAt",*sch("DateTime"),"Timestamp when the case was resolved")]},
    {"name":"SurgeMultiplier","description":"A dynamic pricing factor applied during periods of high demand that increases base fares proportionally to balance supply and demand.","related":[("beckn:PriceComponent","rdfs:subClassOf","Subclass")],"parent":("PriceComponent","conceptual"),"own_props":[("multiplierValue",*sch("Number"),"The surge multiplier value (e.g. 1.5 for 1.5x surge)"),("validUntil",*sch("DateTime"),"Timestamp until which the surge multiplier is active"),("reason",*sch("Text"),"Reason for the surge (e.g. HIGH_DEMAND, SPECIAL_EVENT)"),("geofenceRef",*mob_type("Geofence"),"Geographic area where the surge pricing applies")]},
    {"name":"SystemPricingPlan","description":"A pricing plan defined by a shared mobility system, describing costs and billing rules for vehicle use.","related":[("beckn:Offer","rdfs:subClassOf","Subclass"),("schema:PriceSpecification","rdfs:seeAlso","Related")],"parent":("Offer","core"),"own_props":[("planId",*sch("Text"),"Unique identifier for the pricing plan"),("currency",*sch("Text"),"ISO 4217 currency code"),("isTaxable",*sch("Boolean"),"Whether tax is applied to this pricing plan"),("perMinuteChargingRate",*sch("Number"),"Charge per minute of vehicle use"),("perKmChargingRate",*sch("Number"),"Charge per kilometre of vehicle use"),("perTripStartingFee",*sch("Number"),"Flat fee charged at the start of each trip")]},
    {"name":"TariffZone","description":"A geographic zone used to define and apply fare structures, within which a single fare or set of rules applies.","related":[("beckn:Location","rdfs:subClassOf","Subclass"),("geo:Feature","rdfs:subClassOf","Subclass"),("schema:GeoShape","rdfs:seeAlso","Related")],"parent":("Location","core"),"own_props":[("zoneId",*sch("Text"),"Unique identifier for the tariff zone"),("zoneName",*sch("Text"),"Human-readable name of the tariff zone"),("geometry",*core_type("GeoJSONGeometry"),"GeoJSON geometry defining the zone boundary")]},
    {"name":"Telemetry","description":"Time-series data streams reporting the real-time location, speed, and operational state of a mobility vehicle or asset.","related":[("beckn:Tracking","rdfs:subClassOf","Subclass"),("schema:Vehicle","rdfs:seeAlso","Related")],"parent":("Tracking","core"),"own_props":[("vehicleId",*sch("Text"),"Identifier of the vehicle transmitting telemetry"),("timestamp",*sch("DateTime"),"Timestamp of the telemetry reading"),("latitude",*sch("Number"),"Latitude in WGS-84 decimal degrees"),("longitude",*sch("Number"),"Longitude in WGS-84 decimal degrees"),("speed",*sch("Number"),"Current speed in kilometres per hour"),("bearing",*sch("Number"),"Direction of travel in degrees (0=north, 90=east)"),("batteryLevel",*sch("Number"),"Battery charge percentage (for electric vehicles)"),("odometer",*sch("Number"),"Odometer reading in metres since vehicle start")]},
    {"name":"Ticket","description":"A document or digital record granting the holder the right to travel on a specific transport service or within a defined validity scope.","related":[("beckn:Entitlement","rdfs:subClassOf","Subclass"),("schema:Ticket","rdfs:seeAlso","Related")],"parent":("Entitlement","core"),"own_props":[("ticketId",*sch("Text"),"Unique identifier or serial number of the ticket"),("ticketType",*sch("Text"),"Type of ticket (e.g. SINGLE, RETURN, SEASON, FLEXI)"),("validFrom",*sch("DateTime"),"Date and time from which the ticket is valid"),("validUntil",*sch("DateTime"),"Date and time until which the ticket is valid"),("fareProductRef",*mob_type("FareProduct"),"Reference to the fare product this ticket is issued under"),("passengerRef",*mob_type("Passenger"),"Reference to the passenger this ticket is issued to")]},
    {"name":"Timetable","description":"A structured schedule listing planned arrival and departure times for vehicles at each stop along a route.","related":[("beckn:Catalog","rdfs:subClassOf","Subclass"),("schema:Schedule","rdfs:seeAlso","Related")],"parent":("Catalog","core"),"own_props":[("routeRef",*mob_type("Route"),"Reference to the route this timetable covers"),("trips",*mob_type("VehicleJourney"),"Vehicle journeys (trips) in this timetable"),("validFrom",*sch("DateTime"),"Date from which this timetable is valid"),("validUntil",*sch("DateTime"),"Date until which this timetable is valid")]},
    {"name":"Transfer","description":"A defined connection rule between two routes or services at a common stop, specifying minimum transfer time or transfer type.","related":[("beckn:FulfillmentStop","rdfs:subClassOf","Subclass"),("transmodel:Interchange","rdfs:seeAlso","Related")],"parent":("FulfillmentStop","conceptual"),"own_props":[("fromStopId",*mob_type("Stop"),"Stop passengers transfer from"),("toStopId",*mob_type("Stop"),"Stop passengers transfer to"),("fromRouteId",*mob_type("Route"),"Route passengers transfer from"),("toRouteId",*mob_type("Route"),"Route passengers transfer to"),("transferType",*sch("Text"),"Type of transfer (0=recommended, 1=timed, 2=min_time, 3=not_possible)"),("minTransferTime",*sch("Number"),"Minimum transfer time in seconds")]},
    {"name":"TransportObject","description":"A generic transport entity in the OSLO mobility ontology representing any object involved in transport operations.","related":[("beckn:Item","rdfs:subClassOf","Subclass"),("oslo:TransportObject","owl:equivalentClass","Exact")],"parent":("Item","core"),"own_props":[("objectType",*sch("Text"),"Type of transport object (e.g. VEHICLE, INFRASTRUCTURE, ASSET)"),("attributes",*sch("Text"),"Additional extensible attributes for this transport object")]},
    {"name":"TravelDocument","description":"A document (physical or digital) issued to a passenger proving entitlement to travel, used for validation or inspection.","related":[("beckn:Entitlement","rdfs:subClassOf","Subclass"),("schema:CreativeWork","rdfs:subClassOf","Subclass")],"parent":("Entitlement","core"),"own_props":[("documentType",*sch("Text"),"Type of travel document (e.g. E_TICKET, PDF_TICKET, SMARTCARD, BARCODE)"),("documentNumber",*sch("Text"),"Unique document number or serial"),("issuingAuthority",*mob_type("Operator"),"The operator or authority that issued this document"),("validFrom",*sch("DateTime"),"Start date of the document validity"),("validUntil",*sch("DateTime"),"Expiry date of the document")]},
    {"name":"Trip","description":"A confirmed and booked journey from an origin to a destination, representing a completed mobility service order.","related":[("beckn:Contract","rdfs:subClassOf","Subclass")],"parent":("Contract","core"),"own_props":[("tripId",*sch("Text"),"Unique identifier for the trip"),("origin",*core_type("Location"),"Pickup location"),("destination",*core_type("Location"),"Dropoff location"),("startTime",*sch("DateTime"),"Actual start time of the trip"),("endTime",*sch("DateTime"),"Actual end time of the trip"),("distance",*sch("Number"),"Total distance of the trip in kilometres"),("driverRef",*mob_type("Driver"),"Reference to the driver for this trip"),("vehicleRef",*mob_type("Vehicle"),"Reference to the vehicle for this trip")]},
    {"name":"TripDescriptor","description":"An identifier that uniquely references a specific vehicle journey in a real-time transit feed.","related":[("beckn:Descriptor","rdfs:subClassOf","Subclass"),("mobility:VehicleJourney","rdfs:seeAlso","Related")],"parent":("Descriptor","core"),"own_props":[("tripId",*sch("Text"),"GTFS trip_id of the trip being referenced"),("routeId",*sch("Text"),"GTFS route_id associated with the trip"),("directionId",*sch("Text"),"Direction of travel (0 or 1)"),("startTime",*sch("Text"),"Scheduled start time of the trip in HH:MM:SS"),("startDate",*sch("Text"),"Start date of the trip in YYYYMMDD format"),("scheduleRelationship",*sch("Text"),"Relationship to the GTFS schedule (SCHEDULED, ADDED, UNSCHEDULED, CANCELED)")]},
    {"name":"TripRequest","description":"A request submitted to a journey planning system specifying origin, destination, travel time, and preferences.","related":[("beckn:Intent","rdfs:subClassOf","Subclass")],"parent":("Intent","core"),"own_props":[("origin",*core_type("Location"),"Origin location for the trip"),("destination",*core_type("Location"),"Destination location for the trip"),("departureTime",*sch("DateTime"),"Requested departure time"),("arrivalTime",*sch("DateTime"),"Requested arrival time (alternative to departureTime)"),("modes",*sch("Text"),"Permitted transport modes (e.g. BUS, RAIL, WALK)"),("numItineraries",*sch("Number"),"Number of itinerary alternatives requested")]},
    {"name":"TripResult","description":"The result of a trip planning request, containing one or more journey options with leg details and timing.","related":[("beckn:Catalog","rdfs:subClassOf","Subclass")],"parent":("Catalog","core"),"own_props":[("itineraries",*mob_type("Itinerary"),"List of itinerary options in the result"),("requestRef",*mob_type("TripRequest"),"Reference to the originating trip request")]},
    {"name":"TripSpecification","description":"A description of the desired journey used as input to search and price transport options.","related":[("beckn:Intent","rdfs:subClassOf","Subclass")],"parent":("Intent","core"),"own_props":[("origin",*core_type("Location"),"Desired origin of the trip"),("destination",*core_type("Location"),"Desired destination of the trip"),("time",*sch("DateTime"),"Desired departure or arrival time"),("numTravelers",*sch("Number"),"Number of travelers for whom to price options"),("modes",*sch("Text"),"Preferred transport modes for the trip")]},
    {"name":"TripUpdate","description":"A multi-dimensional update to an in-progress or upcoming mobility trip, covering contract modifications (added/removed services, route changes), status notifications (driver arriving, trip started), and real-time tracking endpoint information.","related":[("beckn:Contract","rdfs:subClassOf","Subclass"),("beckn:State","rdfs:seeAlso","Related"),("beckn:Tracking","rdfs:seeAlso","Related"),("beckn:TrackingRequest","rdfs:seeAlso","Related"),("mobility:VehicleJourney","rdfs:seeAlso","Related")],"parent":("Contract","core"),"own_props":[("contractChanges",*core_type("ContractItem"),"Items added or modified in the trip contract (new stop, route change, add-on service)"),("cancelledItems",*core_type("ContractItem"),"Items removed from the original trip contract"),("stateUpdate",*core_type("State"),"Status notification for the traveler (e.g. driver arriving, trip started, trip ended, driver changed)"),("trackingEndpoint",*core_type("Tracking"),"Real-time tracking endpoint including URL, protocol, and data schema reference"),("driverRef",*mob_type("Driver"),"Reference to the current driver if changed from the originally assigned driver"),("updatedAt",*sch("DateTime"),"Timestamp when this trip update was issued")]},
    {"name":"Vehicle","description":"A motorized or human-powered mobility asset used to carry passengers or goods between locations.","related":[("beckn:Item","rdfs:subClassOf","Subclass"),("schema:Vehicle","rdfs:seeAlso","Related")],"parent":("Item","core"),"own_props":[("vehicleId",*sch("Text"),"Unique identifier for the vehicle"),("licensePlate",*sch("Text"),"Vehicle registration plate number"),("make",*sch("Text"),"Manufacturer of the vehicle"),("model",*sch("Text"),"Model name of the vehicle"),("year",*sch("Number"),"Year of manufacture"),("color",*sch("Text"),"Colour of the vehicle"),("vehicleType",*mob_type("VehicleType"),"Type classification of the vehicle")]},
    {"name":"VehicleCategory","description":"A broad classification of vehicles by their physical type, such as two-wheeler, three-wheeler, four-wheeler, or bus.","related":[("beckn:CategoryCode","rdfs:subClassOf","Subclass")],"parent":("CategoryCode","core"),"own_props":[("vehicleCategoryCode",*sch("Text"),"Code for the vehicle category (e.g. TWO_WHEELER, THREE_WHEELER, FOUR_WHEELER, BUS)"),("maxPassengers",*sch("Number"),"Maximum number of passengers for vehicles in this category")]},
    {"name":"VehicleDescriptor","description":"An identifier that uniquely references a specific vehicle in a real-time transit feed.","related":[("beckn:Descriptor","rdfs:subClassOf","Subclass"),("mobility:Vehicle","rdfs:seeAlso","Related")],"parent":("Descriptor","core"),"own_props":[("vehicleId",*sch("Text"),"Internal system identifier for the vehicle"),("label",*sch("Text"),"User-visible label or number for the vehicle"),("licensePlate",*sch("Text"),"Vehicle license plate number")]},
    {"name":"VehicleJourney","description":"A specific operational instance of a vehicle traveling a defined route at a scheduled time on a given service day.","related":[("beckn:Fulfillment","owl:equivalentClass","Exact"),("transmodel:VehicleJourney","owl:equivalentClass","Exact")],"parent":("Fulfillment","core"),"own_props":[("vehicleJourneyCode",*sch("Text"),"Unique code for this vehicle journey"),("routeRef",*mob_type("Route"),"Reference to the route being served"),("serviceCalendarRef",*mob_type("ServiceCalendar"),"Calendar defining when this journey operates"),("vehicleRef",*mob_type("Vehicle"),"Vehicle assigned to this journey"),("patternRef",*mob_type("Pattern"),"Journey pattern being followed"),("stopTimes",*mob_type("StopTime"),"Scheduled stop times for each stop on this journey")]},
    {"name":"VehicleMonitoringDelivery","description":"A real-time data delivery providing current positions and operational states of a set of vehicles.","related":[("beckn:Tracking","rdfs:subClassOf","Subclass"),("mobility:VehiclePosition","rdfs:seeAlso","Related")],"parent":("Tracking","core"),"own_props":[("responseTimestamp",*sch("DateTime"),"Timestamp of this monitoring delivery"),("vehicleActivities",*mob_type("MonitoredVehicleJourney"),"List of vehicle activity records in this delivery"),("validUntil",*sch("DateTime"),"Time until which this delivery data is valid")]},
    {"name":"VehiclePosition","description":"The current real-time geographic position, bearing, and speed of a vehicle operating a transport service.","related":[("beckn:Tracking","rdfs:subClassOf","Subclass"),("schema:Vehicle","rdfs:seeAlso","Related"),("geo:Feature","rdfs:subClassOf","Subclass")],"parent":("Tracking","core"),"own_props":[("tripDescriptor",*mob_type("TripDescriptor"),"Identifies the trip this vehicle is operating"),("vehicleDescriptor",*mob_type("VehicleDescriptor"),"Identifies the reporting vehicle"),("latitude",*sch("Number"),"Current latitude in WGS-84 decimal degrees"),("longitude",*sch("Number"),"Current longitude in WGS-84 decimal degrees"),("bearing",*sch("Number"),"Current bearing in degrees (0=north, 90=east)"),("speed",*sch("Number"),"Current speed in metres per second"),("currentStopSequence",*sch("Number"),"Stop sequence index of the stop the vehicle is at or approaching"),("currentStatus",*sch("Text"),"Vehicle status relative to the stop (INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO)"),("timestamp",*sch("DateTime"),"Timestamp of this position report")]},
    {"name":"VehicleStatus","description":"The real-time operational state of a vehicle or mobility asset, such as available, in use, reserved, or disabled.","related":[("beckn:State","rdfs:subClassOf","Subclass"),("schema:ItemAvailability","rdfs:seeAlso","Related")],"parent":("State","core"),"own_props":[("statusCode",*sch("Text"),"Operational status code (e.g. AVAILABLE, IN_USE, RESERVED, DISABLED, CHARGING)"),("batteryLevel",*sch("Number"),"Current battery charge percentage"),("rangeMeters",*sch("Number"),"Estimated remaining range in metres"),("lastReportedAt",*sch("DateTime"),"Timestamp of the last status update")]},
    {"name":"VehicleType","description":"A class or category of vehicle defined by its mode of transport, capacity, propulsion type, and accessibility features.","related":[("beckn:CategoryCode","rdfs:subClassOf","Subclass"),("schema:Vehicle","rdfs:subClassOf","Subclass")],"parent":("CategoryCode","core"),"own_props":[("vehicleTypeCode",*sch("Text"),"Code identifying the vehicle type (e.g. BUS, TRAM, METRO, BICYCLE, SCOOTER)"),("maxCapacity",*sch("Number"),"Maximum number of passengers the vehicle type can carry"),("propulsionType",*sch("Text"),"Propulsion type (e.g. ELECTRIC, COMBUSTION, HUMAN, HYBRID)"),("wheelchairAccessible",*sch("Boolean"),"Whether vehicles of this type are wheelchair accessible")]},
    {"name":"WaitingPolicy","description":"Rules governing the maximum time a driver is required to wait for a passenger at the pickup location before being permitted to cancel the booking.","related":[("beckn:Policy","rdfs:subClassOf","Subclass")],"parent":("Policy","core"),"own_props":[("freeWaitingTimeMinutes",*sch("Number"),"Number of minutes the driver waits for free before charging"),("maxWaitingTimeMinutes",*sch("Number"),"Maximum total minutes the driver will wait before auto-cancelling"),("chargePerExtraMinute",*sch("Number"),"Additional charge per minute beyond the free waiting time"),("currency",*sch("Text"),"ISO 4217 currency code for waiting charges")]},
]

MOBILITY_OWN_PROPS = {c["name"]: c["own_props"] for c in CLASS_DATA}

PARENT_URL = {
    "core":       CORE_DIR,
    "conceptual": CORE_IRI,
    "mobility":   MOB,
}

def prop_row(name, type_label, type_url, description, is_inherited=False):
    prop_base = CORE_IRI if is_inherited else MOB
    prop_url  = f"{prop_base}/{name}"
    return f"| [{name}]({prop_url}) | [{type_label}]({type_url}) | {description} |"

def section_header_row(class_name, class_url):
    return f"| **[Properties from {class_name}]({class_url})** | | |"

def generate_readme(c):
    name        = c["name"]
    description = c["description"]
    related     = c.get("related", [])
    parent      = c.get("parent")
    own_props   = c.get("own_props", [])

    class_url = f"{MOB}/{name}"

    # Related classes table
    if related:
        rel_rows = "\n".join(
            f"| [{iri}]({resolve_prefix(iri)}) | {pred} | {STRENGTH.get(pred, pred)} |"
            for iri, pred, _ in related
        )
        related_table = (
            "| Type | Relationship | Strength |\n"
            "|------|--------------|----------|\n"
            + rel_rows
        )
    else:
        related_table = (
            "| Type | Relationship | Strength |\n"
            "|------|--------------|----------|\n"
            "| — | — | — |"
        )

    # Properties table
    prop_lines = ["| Property | Expected Type | Description |", "|---|---|---|"]

    if parent:
        parent_name, parent_vocab = parent
        parent_base_url = PARENT_URL[parent_vocab]
        parent_url = f"{parent_base_url}/{parent_name}"

        prop_lines.append(section_header_row(name, class_url))
        for p in own_props:
            prop_lines.append(prop_row(*p, is_inherited=False))

        prop_lines.append(section_header_row(parent_name, parent_url))
        if parent_vocab in ("core", "conceptual"):
            inherited = CORE_PROPS.get(parent_name, [])
        else:
            inherited = MOBILITY_OWN_PROPS.get(parent_name, [])
        for p in inherited:
            prop_lines.append(prop_row(*p, is_inherited=True))
    else:
        for p in own_props:
            prop_lines.append(prop_row(*p, is_inherited=False))

    props_block = "\n".join(prop_lines)

    return f"""# {name}

A schema.beckn.io Type

{description}

**Canonical IRI :** `mobility:{name}`

**Canonical URL:** {class_url}

**Related Classes:**

{related_table}

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

{props_block}

## Example

[Insert brief description of the example]

```json
[Insert Example JSON-LD]
```

## Example Beckn Protocol Requests Payload using this Schema

> [Brief description of the request with container schema, core schema, and mobility bindings]

```json
[Insert Example JSON-LD]
```
"""

if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    generated = 0
    skipped   = 0
    for c in CLASS_DATA:
        name     = c["name"]
        out_dir  = os.path.join(base, name)
        out_path = os.path.join(out_dir, "README.md")
        if not os.path.isdir(out_dir):
            print(f"  SKIP {name} — directory not found")
            skipped += 1
            continue
        content = generate_readme(c)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  OK   {name}/README.md")
        generated += 1
    print(f"\nDone: {generated} generated, {skipped} skipped.")
