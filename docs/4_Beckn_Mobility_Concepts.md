# Beckn Mobility Concepts

> This document lists all unique mobility domain concepts derived from major global standards (GTFS, GBFS, MDS, SIRI, NeTEx, Transmodel, IATA, BOB, OSDM, OCPI, OCPP, SAE J2735, C-ITS, TOMP-API, OpenMaaS, IXSI, OTP, APDS, ERA, LDES, CityGML, GeoSPARQL, INSPIRE, and more), consolidated into a single ontology vocabulary for the Beckn mobility domain.

**Prefix Declarations**

| Prefix | URI |
|--------|-----|
| `beckn:` | `https://schema.beckn.io/mobility/` |
| `schema:` | `https://schema.org/` |
| `geo:` | `http://www.opengis.net/ont/geosparql#` |
| `foaf:` | `http://xmlns.com/foaf/0.1/` |
| `gtfs:` | `http://vocab.gtfs.org/terms#` |
| `era:` | `http://data.europa.eu/949/` |
| `owl:` | `http://www.w3.org/2002/07/owl#` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |

---

## Unique Mobility Concepts

| # | Concept | Description | Semantic Equivalences | Beckn IRI |
|---|---------|-------------|----------------------|-----------|
| 1 | Operator | An organization that provides and operates public transport or shared mobility services under a defined service agreement. | `owl:equivalentClass gtfs:Agency` ; `rdfs:subClassOf schema:Organization` ; `rdfs:subClassOf foaf:Organization` | `beckn:Operator` |
| 2 | Authority | A governmental or administrative body responsible for planning, regulating, and overseeing transport services within a jurisdiction. | `rdfs:subClassOf schema:GovernmentOrganization` ; `rdfs:subClassOf foaf:Organization` | `beckn:Authority` |
| 3 | Carrier | A transport service provider identified in a passenger contract, responsible for operating a specific segment of travel. | `rdfs:subClassOf schema:Organization` | `beckn:Carrier` |
| 4 | Passenger | A person who travels using a transport service and is identified in a booking or travel document. | `rdfs:subClassOf schema:Person` ; `rdfs:subClassOf foaf:Person` | `beckn:Passenger` |
| 5 | User | A registered participant in a mobility platform who may search, book, and use transport services. | `rdfs:subClassOf schema:Person` ; `rdfs:subClassOf foaf:Person` | `beckn:User` |
| 6 | Stop | A designated location where vehicles stop to allow passengers to board or alight from a transport service. | `owl:equivalentClass gtfs:Stop` ; `rdfs:subClassOf geo:Feature` ; `rdfs:seeAlso schema:BusStop` | `beckn:Stop` |
| 7 | Stop Place | A physical location serving as a transit stop facility, comprising one or more quays, entrances, and associated infrastructure. | `rdfs:subClassOf geo:Feature` ; `rdfs:seeAlso gtfs:Stop` | `beckn:StopPlace` |
| 8 | Stop Point | An abstract or scheduled point in a public transport network at which passengers can board or alight from a service. | `rdfs:subClassOf geo:Feature` | `beckn:StopPoint` |
| 9 | Quay | A specific platform, bay, or boarding area within a Stop Place at which passengers board or alight from a vehicle. | `rdfs:subClassOf geo:Feature` ; `rdfs:seeAlso gtfs:Stop` | `beckn:Quay` |
| 10 | Station | A major transit facility serving as a hub for one or more transport modes, typically offering waiting areas, ticketing, and interchange facilities. | `rdfs:subClassOf schema:CivicStructure` ; `rdfs:seeAlso schema:TrainStation` ; `rdfs:seeAlso schema:BusStation` | `beckn:Station` |
| 11 | Stop Area | A group of stops that collectively define a zone from which a demand-responsive service may pick up or drop off passengers. | `rdfs:subClassOf geo:Feature` | `beckn:StopArea` |
| 12 | Location Group | A set of geographic locations (stops or areas) that can collectively serve as an origin or destination for flexible transit services. | `rdfs:subClassOf geo:Feature` | `beckn:LocationGroup` |
| 13 | Location Group Stop | An association between a stop and a location group, used in flexible transit service planning. | `rdfs:seeAlso beckn:Stop` | `beckn:LocationGroupStop` |
| 14 | Level | A floor or vertical level within a multi-level transit station or facility, used to define internal navigation paths. | `rdfs:seeAlso schema:Floor` | `beckn:Level` |
| 15 | Pathway | A connection between two points within a transit station (e.g., stairway, elevator, walkway) used for indoor navigation and accessibility routing. | `rdfs:subClassOf geo:Feature` | `beckn:Pathway` |
| 16 | Place | A named or unnamed geographic location relevant to mobility, such as an address, point of interest, stop, or area. | `owl:equivalentClass schema:Place` ; `rdfs:subClassOf geo:Feature` | `beckn:Place` |
| 17 | Area | A geographic boundary defining a zone relevant to fare calculation or transport operations. | `rdfs:subClassOf geo:Feature` ; `rdfs:seeAlso schema:GeoShape` | `beckn:Area` |
| 18 | Tariff Zone | A geographic zone used to define and apply fare structures, within which a single fare or set of rules applies. | `rdfs:subClassOf geo:Feature` ; `rdfs:seeAlso schema:GeoShape` | `beckn:TariffZone` |
| 19 | Geofencing Zone | A virtual geographic boundary used to define operational areas, speed limits, parking rules, or restrictions for shared mobility services. | `rdfs:subClassOf geo:Feature` ; `rdfs:seeAlso schema:GeoShape` | `beckn:GeofencingZone` |
| 20 | Geography | A defined geographic area used to specify operational policies for micromobility services such as e-scooters or bikes. | `rdfs:subClassOf geo:Feature` | `beckn:Geography` |
| 21 | Spatial Object | Any object with a spatial extent or location, serving as the base class for all geographic features. | `owl:equivalentClass geo:SpatialObject` | `beckn:SpatialObject` |
| 22 | Geometry | The geometric representation of a spatial object, such as a point, line, or polygon. | `owl:equivalentClass geo:Geometry` | `beckn:Geometry` |
| 23 | Feature | A spatially bounded real-world object with associated properties and a geometric representation. | `owl:equivalentClass geo:Feature` | `beckn:Feature` |
| 24 | Point | A zero-dimensional geometric primitive representing a single geographic coordinate. | `owl:equivalentClass geo:Point` | `beckn:Point` |
| 25 | Polygon | A two-dimensional closed geometric shape representing an enclosed geographic area. | `rdfs:subClassOf geo:Geometry` ; `rdfs:seeAlso schema:GeoShape` | `beckn:Polygon` |
| 26 | Bounding Box | A rectangular geographic extent defined by minimum and maximum latitude and longitude values. | `rdfs:subClassOf geo:Geometry` ; `rdfs:seeAlso schema:GeoShape` | `beckn:BoundingBox` |
| 27 | Transport Network | A connected set of transport links and nodes forming the infrastructure for a specific transport mode. | `rdfs:subClassOf geo:Feature` | `beckn:TransportNetwork` |
| 28 | Transport Link | A directed connection between two transport nodes representing a navigable segment of a transport network. | `rdfs:subClassOf geo:Feature` | `beckn:TransportLink` |
| 29 | Transport Node | A point in a transport network at which transport links meet, such as a junction, station, or terminal. | `rdfs:subClassOf geo:Feature` | `beckn:TransportNode` |
| 30 | Road | A surface infrastructure element used by road vehicles, including carriageways, lanes, and road segments. | `rdfs:subClassOf geo:Feature` | `beckn:Road` |
| 31 | Railway | A guided-track infrastructure element used by trains or trams, including tracks, switches, and rail corridors. | `rdfs:subClassOf geo:Feature` | `beckn:Railway` |
| 32 | Track | A specific section of railway track with defined physical and operational parameters. | `owl:equivalentClass era:Track` ; `rdfs:subClassOf geo:Feature` | `beckn:Track` |
| 33 | Waterway | A navigable body of water used for ferry or boat transport services. | `rdfs:subClassOf geo:Feature` | `beckn:Waterway` |
| 34 | Air Route | A defined path used by aircraft between two points, typically between airports or air navigation waypoints. | `rdfs:subClassOf geo:Feature` ; `rdfs:seeAlso schema:Flight` | `beckn:AirRoute` |
| 35 | Traffic Area | A surface area within a transport complex designated for vehicle movement, such as carriageways and manoeuvring areas. | `rdfs:subClassOf geo:Feature` | `beckn:TrafficArea` |
| 36 | Auxiliary Traffic Area | A surface area adjacent to traffic areas, such as pedestrian paths, bicycle lanes, or parking areas within a transport complex. | `rdfs:subClassOf geo:Feature` | `beckn:AuxiliaryTrafficArea` |
| 37 | Transportation Complex | A set of transport infrastructure objects (roads, railways, squares) forming a unified urban transport feature. | `rdfs:subClassOf geo:Feature` | `beckn:TransportationComplex` |
| 38 | Operational Point | A location on the rail network with operational significance, such as a station, junction, or signal point. | `owl:equivalentClass era:OperationalPoint` ; `rdfs:subClassOf geo:Feature` | `beckn:OperationalPoint` |
| 39 | Section of Line | A segment of a railway line between two consecutive operational points, with defined track parameters. | `owl:equivalentClass era:SectionOfLine` ; `rdfs:subClassOf geo:Feature` | `beckn:SectionOfLine` |
| 40 | Contact Line System | An overhead electrification system supplying traction power to electric rail vehicles. | `owl:equivalentClass era:ContactLineSystem` | `beckn:ContactLineSystem` |
| 41 | Load Capability | The maximum permitted axle load or train weight for a section of railway track. | `owl:equivalentClass era:LoadCapability` | `beckn:LoadCapability` |
| 42 | Train Detection System | A system used to detect the presence and location of trains on a section of railway track. | `owl:equivalentClass era:TrainDetectionSystem` | `beckn:TrainDetectionSystem` |
| 43 | Track Parameter | A physical or operational parameter describing a railway track, such as gauge, gradient, or curvature. | `rdfs:seeAlso era:Track` | `beckn:TrackParameter` |
| 44 | Line | A named, branded public transport service identified by a number or name, typically operating over one or more routes. | `rdfs:seeAlso gtfs:Route` | `beckn:Line` |
| 45 | Route | The physical or logical path followed by a transport service, defined as an ordered sequence of stops or waypoints. | `owl:equivalentClass gtfs:Route` ; `rdfs:seeAlso schema:Trip` | `beckn:Route` |
| 46 | Network | A grouping of routes and lines operated under a common brand or authority, used for fare and operational management. | `rdfs:seeAlso schema:Organization` | `beckn:Network` |
| 47 | Vehicle Journey | A specific operational instance of a vehicle traveling a defined route at a scheduled time on a given service day. | `rdfs:seeAlso gtfs:Trip` | `beckn:VehicleJourney` |
| 48 | Service Calendar | A schedule defining on which dates a transport service operates, including regular service days and exceptional dates. | `rdfs:seeAlso gtfs:Calendar` ; `rdfs:seeAlso schema:Schedule` | `beckn:ServiceCalendar` |
| 49 | Day Type | A classification of a day (e.g., weekday, weekend, public holiday) used to define when a service pattern is valid. | `rdfs:seeAlso schema:DayOfWeek` | `beckn:DayType` |
| 50 | Timetable | A structured schedule listing planned arrival and departure times for vehicles at each stop along a route. | `rdfs:seeAlso schema:Schedule` | `beckn:Timetable` |
| 51 | Stop Time | The scheduled arrival and departure times for a vehicle at a specific stop within a vehicle journey. | `owl:equivalentClass gtfs:StopTime` | `beckn:StopTime` |
| 52 | Frequency | A headway-based service specification indicating how often a vehicle runs on a route within a given time window. | `owl:equivalentClass gtfs:Frequency` | `beckn:Frequency` |
| 53 | Shape | The geographic path traced by a vehicle along a route, represented as an ordered sequence of geographic coordinates. | `owl:equivalentClass gtfs:Shape` ; `rdfs:subClassOf geo:Geometry` | `beckn:Shape` |
| 54 | Pattern | A unique sequence of stops visited by trips on a route, grouping trips with identical stop sequences and timing structures. | `rdfs:seeAlso gtfs:Trip` | `beckn:Pattern` |
| 55 | Direction | The direction of travel of a transport service along a route, typically expressed as inbound or outbound. | `rdfs:seeAlso schema:Direction` | `beckn:Direction` |
| 56 | Transfer | A defined connection rule between two routes or services at a common stop, specifying minimum transfer time or transfer type. | `owl:equivalentClass gtfs:Transfer` | `beckn:Transfer` |
| 57 | Interchange | A planned transfer connection point where passengers switch between two or more transport services, with defined timing constraints. | `rdfs:subClassOf beckn:Stop` | `beckn:Interchange` |
| 58 | Exchange Points | Locations in a transport network where fixed-route and flexible services connect, enabling passenger interchange. | `rdfs:subClassOf geo:Feature` | `beckn:ExchangePoints` |
| 59 | Vehicle Position | The current real-time geographic position, bearing, and speed of a vehicle operating a transport service. | `rdfs:subClassOf geo:Feature` ; `rdfs:seeAlso schema:Vehicle` | `beckn:VehiclePosition` |
| 60 | Trip Update | A real-time update to the schedule of a vehicle journey, including predicted arrival and departure times at stops. | `rdfs:seeAlso beckn:VehicleJourney` | `beckn:TripUpdate` |
| 61 | Stop Time Update | A real-time update to the predicted arrival or departure time of a vehicle at a specific stop within a journey. | `rdfs:seeAlso beckn:StopTime` | `beckn:StopTimeUpdate` |
| 62 | Trip Descriptor | An identifier that uniquely references a specific vehicle journey in a real-time transit feed. | `rdfs:seeAlso beckn:VehicleJourney` | `beckn:TripDescriptor` |
| 63 | Vehicle Descriptor | An identifier that uniquely references a specific vehicle in a real-time transit feed. | `rdfs:seeAlso beckn:Vehicle` | `beckn:VehicleDescriptor` |
| 64 | Monitored Vehicle Journey | A real-time representation of a vehicle journey being actively tracked, including position and schedule adherence data. | `rdfs:subClassOf beckn:VehicleJourney` | `beckn:MonitoredVehicleJourney` |
| 65 | Monitored Call | A real-time arrival or departure prediction for a specific vehicle at a specific stop within a monitored journey. | `rdfs:seeAlso beckn:StopTime` | `beckn:MonitoredCall` |
| 66 | Stop Monitoring | A real-time data service providing predicted arrivals and departures of vehicles at a specific stop. | `rdfs:seeAlso beckn:Stop` | `beckn:StopMonitoring` |
| 67 | Estimated Timetable Delivery | A real-time data delivery providing predicted departure and arrival times for a set of vehicle journeys. | `rdfs:seeAlso beckn:Timetable` | `beckn:EstimatedTimetableDelivery` |
| 68 | Vehicle Monitoring Delivery | A real-time data delivery providing current positions and operational states of a set of vehicles. | `rdfs:seeAlso beckn:VehiclePosition` | `beckn:VehicleMonitoringDelivery` |
| 69 | General Message Delivery | A real-time delivery of textual messages or alerts related to service disruptions or passenger information. | `rdfs:seeAlso beckn:Alert` | `beckn:GeneralMessageDelivery` |
| 70 | Service Delivery | The top-level response container in SIRI encapsulating one or more real-time data delivery types. | — | `beckn:ServiceDelivery` |
| 71 | Affected Line | A reference to a transport line that is affected by a service disruption or alert. | `rdfs:seeAlso beckn:Line` | `beckn:AffectedLine` |
| 72 | Departure Message | A real-time message containing predicted departure times for vehicles at a stop, as used in VDV real-time standards. | `rdfs:seeAlso beckn:StopTime` | `beckn:DepartureMessage` |
| 73 | Prognosis | A real-time prediction of a vehicle's arrival or departure time at a stop, including an indication of prediction confidence. | `rdfs:seeAlso beckn:StopTime` | `beckn:Prognosis` |
| 74 | Occupancy Status | An indicator of the current passenger load level of a vehicle, such as empty, many seats available, or full. | `rdfs:seeAlso schema:ItemAvailability` | `beckn:OccupancyStatus` |
| 75 | Passenger Count | The measured number of passengers currently aboard a vehicle, used for real-time capacity and load management. | — | `beckn:PassengerCount` |
| 76 | Telemetry | Time-series data streams reporting the real-time location, speed, and operational state of a mobility vehicle or asset. | `rdfs:seeAlso schema:Vehicle` | `beckn:Telemetry` |
| 77 | Event | A discrete state change in the lifecycle of a vehicle or mobility asset, such as a trip starting, vehicle reserved, or battery low. | `rdfs:subClassOf schema:Event` | `beckn:Event` |
| 78 | Alert | A notification of a service disruption, delay, or advisory affecting one or more routes, stops, or vehicle journeys. | `rdfs:seeAlso schema:Event` | `beckn:Alert` |
| 79 | Entity Selector | A selector that identifies which transport entities (routes, trips, stops, or agencies) are affected by a given alert. | `rdfs:seeAlso beckn:Alert` | `beckn:EntitySelector` |
| 80 | Time Range | A period defined by a start and end time during which an alert, service change, or condition is active. | `rdfs:seeAlso schema:Schedule` | `beckn:TimeRange` |
| 81 | Translated String | A text string provided in multiple languages, used for localizing alert messages or timetable information. | `rdfs:seeAlso schema:Language` | `beckn:TranslatedString` |
| 82 | Translation | A record providing a localized version of a specific field or value in a transit dataset. | — | `beckn:Translation` |
| 83 | Notice | A textual notice or remark associated with a transport service element, providing supplementary information to passengers. | `rdfs:seeAlso schema:Note` | `beckn:Notice` |
| 84 | Situation | A road traffic event or condition (e.g., accident, roadworks) that affects normal traffic flow and may require advisory action. | `rdfs:subClassOf schema:Event` | `beckn:Situation` |
| 85 | Fare Product | A purchasable entitlement to travel defining conditions of use, validity, and applicable passenger categories. | `rdfs:seeAlso schema:Offer` ; `rdfs:seeAlso schema:Product` | `beckn:FareProduct` |
| 86 | Fare Leg Rule | A rule defining how a fare is applied to a single leg of a journey based on origin, destination, network, and time. | `rdfs:seeAlso beckn:FareProduct` | `beckn:FareLegRule` |
| 87 | Fare Transfer Rule | A rule defining how fares from different legs are combined when a passenger makes a transfer between services. | `rdfs:seeAlso beckn:FareProduct` | `beckn:FareTransferRule` |
| 88 | Rider Category | A classification of passenger type (e.g., adult, child, senior, student) used to determine applicable fare entitlements. | `rdfs:subClassOf schema:Person` | `beckn:RiderCategory` |
| 89 | Fare Medium | The physical or digital medium used to carry or present a fare product, such as a contactless card, mobile app, or paper ticket. | — | `beckn:FareMedium` |
| 90 | Fare | The monetary cost of travel for a specific journey or service, calculated based on applicable fare rules and passenger categories. | `rdfs:seeAlso schema:PriceSpecification` | `beckn:Fare` |
| 91 | Fare Component | A component of an air travel fare that applies to a specific flight segment or leg, used in aviation pricing. | `rdfs:seeAlso beckn:Fare` | `beckn:FareComponent` |
| 92 | Fare Result | The calculated fare for a requested trip, returned as part of a trip planning or fare enquiry response. | `rdfs:seeAlso schema:PriceSpecification` | `beckn:FareResult` |
| 93 | Sales Offer Package | A combination of one or more fare products bundled for sale through a specific distribution channel. | `rdfs:seeAlso schema:Offer` | `beckn:SalesOfferPackage` |
| 94 | System Pricing Plan | A pricing plan defined by a shared mobility system, describing costs and billing rules for vehicle use. | `rdfs:seeAlso schema:PriceSpecification` | `beckn:SystemPricingPlan` |
| 95 | Tariff | A structured set of pricing rules for a service, defining costs based on time, energy consumed, distance, or other parameters. | `rdfs:seeAlso schema:PriceSpecification` | `beckn:Tariff` |
| 96 | Ticket | A document or digital record granting the holder the right to travel on a specific transport service or within a defined validity scope. | `rdfs:seeAlso schema:Ticket` | `beckn:Ticket` |
| 97 | Travel Document | A document (physical or digital) issued to a passenger proving entitlement to travel, used for validation or inspection. | `rdfs:subClassOf schema:CreativeWork` | `beckn:TravelDocument` |
| 98 | Contract | An agreement between a passenger and a transit authority stored on a smart card, granting access to specific fare products. | `rdfs:seeAlso schema:Agreement` | `beckn:Contract` |
| 99 | Distribution Channel | A channel or platform through which fare products or tickets are sold or distributed to end customers. | `rdfs:seeAlso schema:ItemList` | `beckn:DistributionChannel` |
| 100 | Booking Rule | A set of rules governing how and when a demand-responsive transport service must be booked in advance. | — | `beckn:BookingRule` |
| 101 | Booking | A confirmed reservation of a transport service by a user, establishing the rights and conditions of travel. | `rdfs:seeAlso schema:Reservation` | `beckn:Booking` |
| 102 | Offer | A priced and conditioned travel option presented to a customer prior to purchase, typically including fare and availability. | `owl:equivalentClass schema:Offer` | `beckn:Offer` |
| 103 | Offer Item | A specific priced component within an offer, representing a flight, ancillary service, or seat. | `rdfs:subClassOf schema:Offer` | `beckn:OfferItem` |
| 104 | Offer Part | A component of an interoperable transport offer, representing one service segment or product element. | `rdfs:subClassOf schema:Offer` | `beckn:OfferPart` |
| 105 | Order | A confirmed purchase record encompassing one or more travel products, created after a customer accepts an offer. | `owl:equivalentClass schema:Order` | `beckn:Order` |
| 106 | Order Item | A single item within a confirmed order, corresponding to a specific service or product purchased by the customer. | `owl:equivalentClass schema:OrderItem` | `beckn:OrderItem` |
| 107 | Reservation | A confirmed allocation of a specific resource (e.g., seat, charging point, parking space) to a customer for a defined period. | `owl:equivalentClass schema:Reservation` | `beckn:Reservation` |
| 108 | Trip Specification | A description of the desired journey used as input to search and price transport options. | — | `beckn:TripSpecification` |
| 109 | Place Request | A request for a specific accommodation or seat assignment within a transport service during the booking process. | — | `beckn:PlaceRequest` |
| 110 | Availability | The real-time or scheduled state of a vehicle, dock, or service indicating whether it is currently available for use or booking. | `rdfs:seeAlso schema:ItemAvailability` | `beckn:Availability` |
| 111 | Trip Request | A request submitted to a journey planning system specifying origin, destination, travel time, and preferences. | — | `beckn:TripRequest` |
| 112 | Trip Result | The result of a trip planning request, containing one or more journey options with leg details and timing. | — | `beckn:TripResult` |
| 113 | Leg | A single uninterrupted segment of a journey made using one transport mode or service between two consecutive locations. | `rdfs:seeAlso schema:Trip` | `beckn:Leg` |
| 114 | Journey | A complete travel itinerary from origin to destination, potentially comprising multiple legs using different transport modes. | `rdfs:seeAlso schema:Trip` | `beckn:Journey` |
| 115 | Itinerary | A complete planned trip containing an ordered sequence of legs, including transfer points, durations, and timing. | `rdfs:seeAlso schema:Trip` | `beckn:Itinerary` |
| 116 | Plan | A journey planning response containing one or more itinerary options for a given trip request. | — | `beckn:Plan` |
| 117 | Planning Result | The output of a MaaS platform planning request, listing available transport options for a requested trip. | — | `beckn:PlanningResult` |
| 118 | Location Information Request | A request for details about a specific geographic location, stop, or point of interest in the transport network. | `rdfs:seeAlso beckn:Place` | `beckn:LocationInformationRequest` |
| 119 | Stop Event | A departure or arrival event at a stop, used to retrieve the next or previous vehicle movements at a specific location. | `rdfs:seeAlso beckn:StopTime` | `beckn:StopEvent` |
| 120 | Segment | A portion of a rail journey operated continuously by a single carrier between two consecutive stops or stations. | `rdfs:subClassOf beckn:Leg` | `beckn:Segment` |
| 121 | Flight Segment | A single non-stop flight operated between two airports, forming a unit of an air travel itinerary. | `rdfs:subClassOf beckn:Leg` ; `rdfs:seeAlso schema:Flight` | `beckn:FlightSegment` |
| 122 | Itinerary Element | A component of an aviation itinerary such as a flight segment, ground transport leg, or ancillary service. | `rdfs:subClassOf beckn:Itinerary` | `beckn:ItineraryElement` |
| 123 | Vehicle | A motorized or human-powered mobility asset used to carry passengers or goods between locations. | `rdfs:seeAlso schema:Vehicle` | `beckn:Vehicle` |
| 124 | Vehicle Type | A class or category of vehicle defined by its mode of transport, capacity, propulsion type, and accessibility features. | `rdfs:subClassOf schema:Vehicle` | `beckn:VehicleType` |
| 125 | Asset | A specific mobility resource (vehicle, bike, scooter, or car) managed and made available for use by a mobility provider. | `rdfs:seeAlso schema:Product` | `beckn:Asset` |
| 126 | Vehicle Status | The real-time operational state of a vehicle or mobility asset, such as available, in use, reserved, or disabled. | `rdfs:seeAlso schema:ItemAvailability` | `beckn:VehicleStatus` |
| 127 | Bike Allowed | An indicator specifying whether bicycles are permitted on board a particular route or vehicle journey. | — | `beckn:BikeAllowed` |
| 128 | Station Information | Static descriptive information about a shared mobility docking station, including its location, capacity, and features. | `rdfs:subClassOf schema:CivicStructure` | `beckn:StationInformation` |
| 129 | Station Status | The real-time operational state of a shared mobility station, including the number of available docks and vehicles. | `rdfs:seeAlso schema:ItemAvailability` | `beckn:StationStatus` |
| 130 | System Information | Static metadata about a shared mobility or transport system, including name, operator, timezone, and coverage area. | `rdfs:seeAlso schema:Organization` | `beckn:SystemInformation` |
| 131 | Charging Station | A physical facility containing one or more EV supply equipment units for charging electric vehicles. | `rdfs:subClassOf schema:LocalBusiness` | `beckn:ChargingStation` |
| 132 | EVSE | An Electric Vehicle Supply Equipment unit at a charging location, capable of charging one vehicle at a time. | `rdfs:subClassOf schema:LocalBusiness` | `beckn:EVSE` |
| 133 | Connector | A physical socket or coupling at an EVSE used to connect an electric vehicle for charging. | — | `beckn:Connector` |
| 134 | Session | An active usage or charging session at a resource, tracking energy consumption, duration, and cost. | — | `beckn:Session` |
| 135 | Charge Detail Record | A complete record of a finished EV charging session, including energy consumed, duration, start/stop times, and cost. | `rdfs:subClassOf schema:Invoice` | `beckn:ChargeDetailRecord` |
| 136 | Token | An authorization token (e.g., RFID card or app token) used to authenticate a user at an EV charging station. | — | `beckn:Token` |
| 137 | Command | A remote instruction sent to an EV charging station to perform an action such as starting or stopping a charging session. | — | `beckn:Command` |
| 138 | Meter Value | An energy meter reading from an EV charger, used to measure consumption for billing and monitoring purposes. | — | `beckn:MeterValue` |
| 139 | Authorization | A check or decision confirming whether a user or token is permitted to initiate a session at a charging station or resource. | `rdfs:seeAlso schema:DigitalDocument` | `beckn:Authorization` |
| 140 | Payment | A financial transaction made by a user to settle the cost of a transport, parking, or charging service. | `rdfs:seeAlso schema:PayAction` | `beckn:Payment` |
| 141 | Payment Method | The instrument or mechanism used to make a payment, such as a credit card, bank transfer, or digital wallet. | `owl:equivalentClass schema:PaymentMethod` | `beckn:PaymentMethod` |
| 142 | Payment Transaction | A completed or in-progress financial transaction associated with purchasing a transport or mobility service. | `rdfs:seeAlso schema:PayAction` | `beckn:PaymentTransaction` |
| 143 | Payment Instruction | A formal instruction to transfer funds between financial institutions, as defined in ISO 20022. | — | `beckn:PaymentInstruction` |
| 144 | Transaction | A discrete financial or data exchange event, such as a fare payment, contactless card tap, or charging session settlement. | — | `beckn:Transaction` |
| 145 | Account | A financial account held by a user or institution, used for storing value or settling transport payments. | `rdfs:seeAlso schema:FinancialProduct` | `beckn:Account` |
| 146 | Credit Transfer | A payment instruction initiated by the payer to push funds from their account to a payee's account. | — | `beckn:CreditTransfer` |
| 147 | Direct Debit | A payment instruction initiated by the payee to pull funds from a payer's account on a one-off or recurring basis. | — | `beckn:DirectDebit` |
| 148 | Financial Institution | A bank or payment service provider that processes, clears, or settles financial transactions. | `rdfs:subClassOf schema:Organization` ; `rdfs:subClassOf foaf:Organization` | `beckn:FinancialInstitution` |
| 149 | Deposit | A security deposit collected from a user at the start of a shared mobility service, refundable upon satisfactory return. | `rdfs:seeAlso schema:PayAction` | `beckn:Deposit` |
| 150 | Purse | An electronic stored-value wallet on a smart card used to pre-pay for transit services by deducting value per journey. | `rdfs:seeAlso schema:MonetaryAmount` | `beckn:Purse` |
| 151 | Security Module | A tamper-resistant hardware component on a smart card that manages cryptographic keys and secure data operations. | — | `beckn:SecurityModule` |
| 152 | Application | A software application stored on a smart card that manages a specific transit service or fare product. | — | `beckn:Application` |
| 153 | Terminal | A physical device at which passengers interact with a transit system for ticketing, fare validation, or payment. | `rdfs:subClassOf schema:LocalBusiness` | `beckn:Terminal` |
| 154 | Basic Safety Message | A periodic V2X broadcast message transmitted by vehicles containing speed, heading, and position for collision avoidance. | — | `beckn:BasicSafetyMessage` |
| 155 | Map Data | A V2X message describing the topology of an intersection or road segment for use by connected vehicles. | `rdfs:seeAlso schema:Map` | `beckn:MapData` |
| 156 | Signal Phase and Timing | A V2X message providing real-time traffic signal phase and timing data to vehicles approaching an intersection. | — | `beckn:SignalPhaseAndTiming` |
| 157 | Traveler Information Message | A V2X message delivered to vehicles or devices containing road conditions, speed limits, or safety advisories. | `rdfs:seeAlso schema:Message` | `beckn:TravelerInformationMessage` |
| 158 | Probe Vehicle Data | Position, speed, and heading data collected from a moving vehicle used for traffic monitoring and analytics. | `rdfs:seeAlso schema:Vehicle` | `beckn:ProbeVehicleData` |
| 159 | Road Side Alert | A V2X alert message broadcast by a roadside unit warning vehicles of hazards, incidents, or road conditions. | `rdfs:subClassOf beckn:Alert` | `beckn:RoadSideAlert` |
| 160 | Cooperative Awareness Message | A periodic V2X broadcast by a vehicle or infrastructure unit sharing its identity, position, and status with nearby entities. | — | `beckn:CooperativeAwarenessMessage` |
| 161 | Decentralized Environmental Notification Message | A V2X event-triggered message notifying nearby road users of a detected hazard or unusual environmental condition. | `rdfs:subClassOf beckn:Alert` | `beckn:DecentralizedEnvironmentalNotificationMessage` |
| 162 | In-Vehicle Information | A V2X message delivering road sign or regulatory information directly to an in-vehicle human-machine interface. | `rdfs:seeAlso schema:Message` | `beckn:InVehicleInformation` |
| 163 | Collective Perception Message | A V2X message sharing a vehicle's perception of nearby objects (pedestrians, vehicles) with surrounding road users. | — | `beckn:CollectivePerceptionMessage` |
| 164 | Traffic Status | A classification of current traffic conditions on a road segment, such as free flow, slow, queuing, or stationary. | — | `beckn:TrafficStatus` |
| 165 | Traffic Flow | A measured or estimated count of vehicles passing a specific point on a road within a given time interval. | — | `beckn:TrafficFlow` |
| 166 | Travel Time | The estimated or measured time required to traverse a defined road segment under current traffic conditions. | `rdfs:seeAlso schema:Duration` | `beckn:TravelTime` |
| 167 | Measurement Site | A physical or virtual location where traffic data such as flow, speed, or occupancy is collected or measured. | `rdfs:subClassOf geo:Feature` | `beckn:MeasurementSite` |
| 168 | Parking Record | A description of a parking facility including its location, capacity, access restrictions, and static pricing information. | `rdfs:subClassOf schema:CivicStructure` | `beckn:ParkingRecord` |
| 169 | Parking Table | A collection of parking records describing the parking facilities available in a defined area or operator network. | `rdfs:seeAlso schema:ItemList` | `beckn:ParkingTable` |
| 170 | Elaborated Data Publication | A structured publication of processed or aggregated traffic data, such as journey times or congestion indices. | `rdfs:seeAlso schema:DataFeed` | `beckn:ElaboratedDataPublication` |
| 171 | Rate | A pricing rule for a parking facility, defining costs based on duration, vehicle type, time of day, or other criteria. | `rdfs:seeAlso schema:PriceSpecification` | `beckn:Rate` |
| 172 | Right Specification | A specification defining the conditions under which a parking right or permit is granted, including time, location, and vehicle type. | `rdfs:seeAlso schema:Permit` | `beckn:RightSpecification` |
| 173 | Observation | A recorded event or measurement in a parking context, such as a vehicle entering or leaving a parking space. | — | `beckn:Observation` |
| 174 | Issuer | An organization or authority that issues parking rights, permits, or authorization credentials. | `rdfs:subClassOf schema:Organization` | `beckn:Issuer` |
| 175 | Assignee | A person or entity to whom a parking right, permit, or credential has been assigned. | `rdfs:subClassOf schema:Person` | `beckn:Assignee` |
| 176 | Provider | A mobility service provider registered on a MaaS platform, offering transport options to end users. | `rdfs:subClassOf schema:Organization` ; `rdfs:subClassOf foaf:Organization` | `beckn:Provider` |
| 177 | Attribute | A descriptive property or feature associated with a mobility asset, such as electric propulsion, wheelchair accessibility, or child seat. | `rdfs:seeAlso schema:PropertyValue` | `beckn:Attribute` |
| 178 | Policy | A set of operational rules defined by a mobility authority governing vehicle behavior, permitted areas, speed, or parking. | `rdfs:seeAlso schema:GovernmentService` | `beckn:Policy` |
| 179 | Seat | A specific seat position reserved or assigned to a passenger on a flight, train, or other transport service. | `rdfs:seeAlso schema:Seat` | `beckn:Seat` |
| 180 | Baggage Allowance | The quantity and weight of baggage a passenger is permitted to carry or check in without incurring additional charges. | — | `beckn:BaggageAllowance` |
| 181 | Ancillary Service | An optional or additional service available for purchase alongside base transport, such as extra baggage or lounge access. | `rdfs:subClassOf schema:Service` | `beckn:AncillaryService` |
| 182 | Service | A purchasable service component included in a transport order, such as catering, priority boarding, or seat upgrade. | `rdfs:seeAlso schema:Service` | `beckn:Service` |
| 183 | Price | The monetary amount associated with an offer, fare, or service, including breakdowns for taxes, surcharges, and fees. | `owl:equivalentClass schema:PriceSpecification` | `beckn:Price` |
| 184 | Event Stream | A linked data stream of time-ordered events representing changes to a dataset, following the LDES specification. | `rdfs:seeAlso schema:DataFeed` | `beckn:EventStream` |
| 185 | Collection | A set of linked data resources forming a cohesive dataset or versioned event stream. | `rdfs:seeAlso schema:Collection` | `beckn:Collection` |
| 186 | View | A paginated or filtered access point into a linked data collection or event stream. | — | `beckn:View` |
| 187 | Fragmentation Strategy | A method for dividing a linked data collection into navigable fragments based on time, property, or spatial criteria. | — | `beckn:FragmentationStrategy` |
| 188 | Member | An individual data item or event that is part of a linked data collection or event stream. | — | `beckn:Member` |
| 189 | Tree Node | A node in the TREE hypermedia structure that links to related data fragments within a linked data collection. | — | `beckn:TreeNode` |
| 190 | Relation | A typed link between two tree nodes indicating a navigational or filtering relationship within a linked data collection. | `rdfs:seeAlso schema:PropertyValue` | `beckn:Relation` |
| 191 | Feed | A data publication providing transit or mobility information in a standardized format for consumption by applications or planners. | `rdfs:seeAlso schema:DataFeed` | `beckn:Feed` |
| 192 | Message | A structured data container used to communicate a request, response, or notification between transport or financial systems. | `rdfs:seeAlso schema:Message` | `beckn:Message` |
| 193 | Path (Endpoint) | A specific URL path exposed by an API, representing a resource or operation accessible to API clients. | — | `beckn:Endpoint` |
| 194 | Request Body | The structured data payload sent by a client in the body of an API request. | — | `beckn:RequestBody` |
| 195 | Response | The structured data returned by an API server in reply to a client request. | — | `beckn:Response` |
| 196 | Schema | A formal definition of the structure and data types used in an API request or response payload. | `rdfs:seeAlso schema:DataType` | `beckn:Schema` |
| 197 | Parameter | A named input variable passed to an API endpoint via path, query string, header, or cookie. | — | `beckn:Parameter` |
| 198 | Security Scheme | A definition of the authentication or authorization mechanism required to access a secured API endpoint. | — | `beckn:SecurityScheme` |
| 199 | Transport Object | A generic transport entity in the OSLO mobility ontology representing any object involved in transport operations. | — | `beckn:TransportObject` |
