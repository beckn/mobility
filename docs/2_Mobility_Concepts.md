# Mobility Domain Concepts

This document catalogues the core business concepts (nouns) defined by each mobility domain standard, mapped to the use cases in which they apply.

**Column Definitions**

| Column | Description |
|--------|-------------|
| **Domain Standard** | Name of the industry domain standard that defines this concept |
| **Domain Concept** | The core business entity or idea being modeled (e.g., Pickup Location, Ticket, Fare Product) |
| **Use Cases** | Comma-separated list of use cases that this concept applies to |

---

## Concepts Table


| Domain Standard | Domain Concept | Use Cases |
|---|---|---|
| **GTFS Static** | Agency | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **GTFS Static** | Route | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **GTFS Static** | Trip | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **GTFS Static** | Stop | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **GTFS Static** | Stop Time | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **GTFS Static** | Calendar | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **GTFS Static** | Calendar Date | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **GTFS Static** | Shape | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **GTFS Static** | Frequency | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Tram) |
| **GTFS Static** | Transfer | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Multi-modal Trip Planning |
| **GTFS Static** | Feed Info | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **GTFS Realtime** | Trip Update | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **GTFS Realtime** | Vehicle Position | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **GTFS Realtime** | Stop Time Update | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **GTFS Realtime** | Trip Descriptor | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **GTFS Realtime** | Vehicle Descriptor | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **GTFS Flex** | Location Group | Demand-Responsive Transit, Paratransit, Rural Transit |
| **GTFS Flex** | Location Group Stop | Demand-Responsive Transit, Paratransit, Rural Transit |
| **GTFS Flex** | Booking Rule | Demand-Responsive Transit, Paratransit, Rural Transit |
| **GTFS Flex** | Stop Area | Demand-Responsive Transit, Paratransit, Rural Transit |
| **GTFS Fares v2** | Fare Product | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Multi-modal Ticketing |
| **GTFS Fares v2** | Fare Leg Rule | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Multi-modal Ticketing |
| **GTFS Fares v2** | Fare Transfer Rule | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **GTFS Fares v2** | Rider Category | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **GTFS Fares v2** | Fare Medium | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **GTFS Fares v2** | Network | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry) |
| **GTFS Fares v2** | Area | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Multi-modal Ticketing |
| **GTFS Pathways** | Pathway | Public Transit (Metro), Public Transit (Rail), Accessibility / Station Navigation |
| **GTFS Pathways** | Level | Public Transit (Metro), Public Transit (Rail), Accessibility / Station Navigation |
| **GTFS Pathways** | Stop (Entrance / Exit / Generic Node / Boarding Area) | Public Transit (Metro), Public Transit (Rail), Accessibility / Station Navigation |
| **GTFS Levels** | Level | Public Transit (Metro), Public Transit (Rail), Multi-level Station Navigation |
| **GTFS Translations** | Translation | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-lingual Transit Information |
| **GTFS Alerts** | Alert | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry) |
| **GTFS Alerts** | Entity Selector | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry) |
| **GTFS Alerts** | Time Range | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry) |
| **GTFS Alerts** | Translated String | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry) |
| **GTFS Bikes** | Bike Allowed (Route) | Public Transit (Bus), Bike Sharing, Multi-modal Trip Planning |
| **GTFS Bikes** | Bike Allowed (Trip) | Public Transit (Bus), Bike Sharing, Multi-modal Trip Planning |
| **GTFS Occupancy** | Occupancy Status | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GTFS Occupancy** | Passenger Count | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GTFS Occupancy** | Vehicle Position (with Occupancy) | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GBFS** | System Information | Bike Sharing, E-Scooter Sharing, Moped Sharing, Cargo Bike Sharing |
| **GBFS** | Station Information | Bike Sharing, E-Scooter Sharing, Moped Sharing, Cargo Bike Sharing |
| **GBFS** | Station Status | Bike Sharing, E-Scooter Sharing, Moped Sharing, Cargo Bike Sharing |
| **GBFS** | Vehicle Type | Bike Sharing, E-Scooter Sharing, Moped Sharing, Cargo Bike Sharing |
| **GBFS** | Vehicle Status | Bike Sharing, E-Scooter Sharing, Moped Sharing, Cargo Bike Sharing |
| **GBFS** | System Pricing Plan | Bike Sharing, E-Scooter Sharing, Moped Sharing, Cargo Bike Sharing |
| **GBFS** | Geofencing Zone | Bike Sharing, E-Scooter Sharing, Moped Sharing |
| **GBFS** | System Alert | Bike Sharing, E-Scooter Sharing, Moped Sharing, Cargo Bike Sharing |
| **MDS** | Vehicle | E-Scooter Sharing, Bike Sharing, Moped Sharing, Ride Hailing, Carsharing |
| **MDS** | Trip | E-Scooter Sharing, Bike Sharing, Moped Sharing, Ride Hailing, Carsharing |
| **MDS** | Event | E-Scooter Sharing, Bike Sharing, Moped Sharing, Ride Hailing, Carsharing |
| **MDS** | Telemetry | E-Scooter Sharing, Bike Sharing, Moped Sharing, Ride Hailing |
| **MDS** | Stop / Station | Bike Sharing, E-Scooter Sharing, Moped Sharing |
| **MDS** | Policy | E-Scooter Sharing, Bike Sharing, Moped Sharing, Ride Hailing, Carsharing |
| **MDS** | Geography | E-Scooter Sharing, Bike Sharing, Moped Sharing, Ride Hailing, Carsharing |
| **SIRI** | Service Delivery | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **SIRI** | Monitored Vehicle Journey | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **SIRI** | Monitored Call | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **SIRI** | Stop Monitoring Delivery | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **SIRI** | Estimated Timetable Delivery | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **SIRI** | Vehicle Monitoring Delivery | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **SIRI** | General Message Delivery | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **SIRI** | Affected Line | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **NeTEx** | Stop Place | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Multi-modal Trip Planning |
| **NeTEx** | Quay | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **NeTEx** | Scheduled Stop Point | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **NeTEx** | Line | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **NeTEx** | Route | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **NeTEx** | Service Journey | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **NeTEx** | Operator | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **NeTEx** | Authority | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **NeTEx** | Network | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **NeTEx** | Tariff Zone | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **NeTEx** | Fare Zone | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **NeTEx** | Fare Product | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Multi-modal Ticketing |
| **NeTEx** | Sales Offer Package | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Multi-modal Ticketing |
| **NeTEx** | Distribution Channel | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **NeTEx** | Service Calendar | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **NeTEx** | Day Type | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **NeTEx** | Vehicle Type | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **NeTEx** | Notice | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **Transmodel** | Stop Point | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **Transmodel** | Line | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **Transmodel** | Route | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **Transmodel** | Vehicle Journey | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **Transmodel** | Vehicle Type | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **Transmodel** | Operator | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **Transmodel** | Authority | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **Transmodel** | Network | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) |
| **Transmodel** | Fare Product | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry) |
| **Transmodel** | Tariff Zone | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **Transmodel** | Timetable | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit |
| **OJP** | Trip Request | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning, Demand-Responsive Transit |
| **OJP** | Trip Result | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning, Demand-Responsive Transit |
| **OJP** | Trip Leg | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning, Demand-Responsive Transit |
| **OJP** | Location Information Request | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **OJP** | Stop Event Request | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **OJP** | Stop Event Result | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **OJP** | Exchange Points | Multi-modal Trip Planning, Demand-Responsive Transit |
| **TRIAS** | Trip Request | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **TRIAS** | Trip Result | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **TRIAS** | Trip Leg | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **TRIAS** | Stop Event | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **TRIAS** | Location Information | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **TRIAS** | Fare Result | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **TRIAS** | Interchange | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning |
| **VDV 736 / VDV 454** | Stop Monitoring | Public Transit (Bus), Public Transit (Tram) |
| **VDV 736 / VDV 454** | Departure Message | Public Transit (Bus), Public Transit (Tram) |
| **VDV 736 / VDV 454** | Vehicle Journey | Public Transit (Bus), Public Transit (Tram) |
| **VDV 736 / VDV 454** | Line | Public Transit (Bus), Public Transit (Tram) |
| **VDV 736 / VDV 454** | Direction | Public Transit (Bus), Public Transit (Tram) |
| **VDV 736 / VDV 454** | Prognosis | Public Transit (Bus), Public Transit (Tram) |
| **IATA NDC** | Offer | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Offer Item | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Order | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Order Item | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Passenger | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Flight Segment | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Seat | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Fare Component | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Baggage Allowance | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Ancillary Service | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA NDC** | Price | Commercial Aviation, Airline Ticketing & Distribution |
| **IATA ONE Order** | Order | Commercial Aviation, Airline Order Management |
| **IATA ONE Order** | Order Item | Commercial Aviation, Airline Order Management |
| **IATA ONE Order** | Passenger | Commercial Aviation, Airline Order Management |
| **IATA ONE Order** | Flight Segment | Commercial Aviation, Airline Order Management |
| **IATA ONE Order** | Seat | Commercial Aviation, Airline Order Management |
| **IATA ONE Order** | Service | Commercial Aviation, Airline Order Management |
| **IATA ONE Order** | Payment Method | Commercial Aviation, Airline Order Management |
| **IATA ONE Order** | Payment Transaction | Commercial Aviation, Airline Order Management |
| **IATA ONE Order** | Itinerary Element | Commercial Aviation, Airline Order Management |
| **BOB** | Booking | Railways (Interoperable Rail), Rail Ticketing |
| **BOB** | Offer | Railways (Interoperable Rail), Rail Ticketing |
| **BOB** | Offer Part | Railways (Interoperable Rail), Rail Ticketing |
| **BOB** | Passenger | Railways (Interoperable Rail), Rail Ticketing |
| **BOB** | Travel Document | Railways (Interoperable Rail), Rail Ticketing |
| **BOB** | Reservation | Railways (Interoperable Rail), Rail Ticketing |
| **BOB** | Distribution Channel | Railways (Interoperable Rail), Rail Ticketing |
| **BOB** | Trip Specification | Railways (Interoperable Rail), Rail Ticketing |
| **TAP TSI** | Ticket | Railways (Interoperable Rail), Rail Ticketing |
| **TAP TSI** | Travel Document | Railways (Interoperable Rail), Rail Ticketing |
| **TAP TSI** | Reservation | Railways (Interoperable Rail), Rail Ticketing |
| **TAP TSI** | Journey | Railways (Interoperable Rail), Rail Ticketing |
| **TAP TSI** | Segment | Railways (Interoperable Rail), Rail Ticketing |
| **TAP TSI** | Passenger | Railways (Interoperable Rail), Rail Ticketing |
| **TAP TSI** | Carrier | Railways (Interoperable Rail), Rail Ticketing |
| **OSDM** | Offer | Railways (Interoperable Rail), Rail Ticketing |
| **OSDM** | Booking | Railways (Interoperable Rail), Rail Ticketing |
| **OSDM** | Passenger | Railways (Interoperable Rail), Rail Ticketing |
| **OSDM** | Travel Document | Railways (Interoperable Rail), Rail Ticketing |
| **OSDM** | Trip Specification | Railways (Interoperable Rail), Rail Ticketing |
| **OSDM** | Place Request | Railways (Interoperable Rail), Rail Ticketing |
| **OSDM** | Fare | Railways (Interoperable Rail), Rail Ticketing |
| **OSDM** | Ancillary | Railways (Interoperable Rail), Rail Ticketing |
| **ISO 24014-1** | Fare Product | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **ISO 24014-1** | Contract | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **ISO 24014-1** | Application | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **ISO 24014-1** | Purse | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **ISO 24014-1** | Security Module | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **ISO 24014-1** | Terminal | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **ISO 24014-1** | Transaction | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing |
| **ISO 20022** | Payment Instruction | Multi-modal Ticketing, Transit Fare Payments |
| **ISO 20022** | Transaction | Multi-modal Ticketing, Transit Fare Payments |
| **ISO 20022** | Account | Multi-modal Ticketing, Transit Fare Payments |
| **ISO 20022** | Financial Institution | Multi-modal Ticketing, Transit Fare Payments |
| **ISO 20022** | Credit Transfer | Multi-modal Ticketing, Transit Fare Payments |
| **ISO 20022** | Direct Debit | Multi-modal Ticketing, Transit Fare Payments |
| **ISO 20022** | Message | Multi-modal Ticketing, Transit Fare Payments |
| **ETSI DATEX II** | Traffic Status | Road Traffic Management, Multi-modal Travel Information |
| **ETSI DATEX II** | Traffic Flow | Road Traffic Management, Multi-modal Travel Information |
| **ETSI DATEX II** | Travel Time | Road Traffic Management, Multi-modal Travel Information |
| **ETSI DATEX II** | Measurement Site | Road Traffic Management, Multi-modal Travel Information |
| **ETSI DATEX II** | Parking Record | Parking, Multi-modal Travel Information |
| **ETSI DATEX II** | Parking Table | Parking, Multi-modal Travel Information |
| **ETSI DATEX II** | Situation (Alert) | Road Traffic Management, Multi-modal Travel Information |
| **ETSI DATEX II** | Elaborated Data Publication | Road Traffic Management, Multi-modal Travel Information |
| **OCPI** | Location | Electric Vehicle Charging, EV Roaming |
| **OCPI** | EVSE | Electric Vehicle Charging, EV Roaming |
| **OCPI** | Connector | Electric Vehicle Charging, EV Roaming |
| **OCPI** | Session | Electric Vehicle Charging, EV Roaming |
| **OCPI** | Charge Detail Record (CDR) | Electric Vehicle Charging, EV Roaming |
| **OCPI** | Token | Electric Vehicle Charging, EV Roaming |
| **OCPI** | Tariff | Electric Vehicle Charging, EV Roaming |
| **OCPI** | Command | Electric Vehicle Charging, EV Roaming |
| **OCPP** | Charging Station | Electric Vehicle Charging |
| **OCPP** | Connector | Electric Vehicle Charging |
| **OCPP** | Transaction | Electric Vehicle Charging |
| **OCPP** | Meter Value | Electric Vehicle Charging |
| **OCPP** | Status Notification | Electric Vehicle Charging |
| **OCPP** | Reservation | Electric Vehicle Charging |
| **OCPP** | Authorization | Electric Vehicle Charging |
| **SAE J2735 / DSRC** | Basic Safety Message (BSM) | Connected & Autonomous Vehicles, Road Transport |
| **SAE J2735 / DSRC** | Map Data (MAP) | Connected & Autonomous Vehicles, Road Transport |
| **SAE J2735 / DSRC** | Signal Phase and Timing (SPaT) | Connected & Autonomous Vehicles, Road Transport |
| **SAE J2735 / DSRC** | Traveler Information Message (TIM) | Connected & Autonomous Vehicles, Road Transport |
| **SAE J2735 / DSRC** | Probe Vehicle Data | Connected & Autonomous Vehicles, Road Transport |
| **SAE J2735 / DSRC** | Road Side Alert | Connected & Autonomous Vehicles, Road Transport |
| **C-ITS (ETSI ITS)** | Cooperative Awareness Message (CAM) | Connected & Autonomous Vehicles, Road Traffic Management |
| **C-ITS (ETSI ITS)** | Decentralized Environmental Notification Message (DENM) | Connected & Autonomous Vehicles, Road Traffic Management |
| **C-ITS (ETSI ITS)** | Signal Phase And Timing (SPAT) | Connected & Autonomous Vehicles, Road Traffic Management |
| **C-ITS (ETSI ITS)** | Map Data (MAP) | Connected & Autonomous Vehicles, Road Traffic Management |
| **C-ITS (ETSI ITS)** | In-Vehicle Information (IVI) | Connected & Autonomous Vehicles, Road Traffic Management |
| **C-ITS (ETSI ITS)** | Collective Perception Message (CPM) | Connected & Autonomous Vehicles, Road Traffic Management |
| **TOMP-API** | Booking | MaaS (Mobility as a Service), Ride Hailing, Bike Sharing, E-Scooter Sharing, Carsharing, Demand-Responsive Transit |
| **TOMP-API** | Leg | MaaS (Mobility as a Service), Ride Hailing, Bike Sharing, E-Scooter Sharing, Carsharing, Demand-Responsive Transit |
| **TOMP-API** | Asset | MaaS (Mobility as a Service), Bike Sharing, E-Scooter Sharing, Carsharing |
| **TOMP-API** | Asset Type | MaaS (Mobility as a Service), Bike Sharing, E-Scooter Sharing, Carsharing |
| **TOMP-API** | System Information | MaaS (Mobility as a Service), Bike Sharing, E-Scooter Sharing, Carsharing |
| **TOMP-API** | Operator | MaaS (Mobility as a Service), Ride Hailing, Bike Sharing, E-Scooter Sharing, Carsharing |
| **TOMP-API** | Planning Result | MaaS (Mobility as a Service), Ride Hailing, Bike Sharing, E-Scooter Sharing, Carsharing |
| **TOMP-API** | User | MaaS (Mobility as a Service), Ride Hailing, Bike Sharing, E-Scooter Sharing, Carsharing |
| **TOMP-API** | Payment | MaaS (Mobility as a Service), Ride Hailing, Bike Sharing, E-Scooter Sharing, Carsharing |
| **TOMP-API** | Deposit | MaaS (Mobility as a Service), Carsharing, Bike Sharing |
| **OpenMaaS / MaaS Alliance API** | Journey | MaaS (Mobility as a Service), Multi-modal Booking |
| **OpenMaaS / MaaS Alliance API** | Booking | MaaS (Mobility as a Service), Multi-modal Booking |
| **OpenMaaS / MaaS Alliance API** | Leg | MaaS (Mobility as a Service), Multi-modal Booking |
| **OpenMaaS / MaaS Alliance API** | Provider | MaaS (Mobility as a Service), Multi-modal Booking |
| **OpenMaaS / MaaS Alliance API** | Asset | MaaS (Mobility as a Service), Multi-modal Booking |
| **OpenMaaS / MaaS Alliance API** | Fare Product | MaaS (Mobility as a Service), Multi-modal Booking |
| **OpenMaaS / MaaS Alliance API** | Availability | MaaS (Mobility as a Service), Multi-modal Booking |
| **IXSI** | Provider Information | Carsharing, Bike Sharing |
| **IXSI** | Bookee Object (Vehicle / Bike) | Carsharing, Bike Sharing |
| **IXSI** | Booking | Carsharing, Bike Sharing |
| **IXSI** | Availability | Carsharing, Bike Sharing |
| **IXSI** | Place (Stop Point) | Carsharing, Bike Sharing |
| **IXSI** | User | Carsharing, Bike Sharing |
| **IXSI** | Attribute | Carsharing, Bike Sharing |
| **OpenTripPlanner / OTP API** | Plan | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail), Cycling, Walking |
| **OpenTripPlanner / OTP API** | Itinerary | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail), Cycling, Walking |
| **OpenTripPlanner / OTP API** | Leg | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail), Cycling, Walking |
| **OpenTripPlanner / OTP API** | Stop | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail) |
| **OpenTripPlanner / OTP API** | Route | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail) |
| **OpenTripPlanner / OTP API** | Agency | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail) |
| **OpenTripPlanner / OTP API** | Trip | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail) |
| **OpenTripPlanner / OTP API** | Pattern | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail) |
| **OpenTripPlanner / OTP API** | Place | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail), Cycling, Walking |
| **OpenAPI / OAS 3.x** | Path (Endpoint) | Ride Hailing, MaaS (Mobility as a Service), Carsharing, Bike Sharing, E-Scooter Sharing |
| **OpenAPI / OAS 3.x** | Request Body | Ride Hailing, MaaS (Mobility as a Service), Carsharing, Bike Sharing, E-Scooter Sharing |
| **OpenAPI / OAS 3.x** | Response | Ride Hailing, MaaS (Mobility as a Service), Carsharing, Bike Sharing, E-Scooter Sharing |
| **OpenAPI / OAS 3.x** | Schema | Ride Hailing, MaaS (Mobility as a Service), Carsharing, Bike Sharing, E-Scooter Sharing |
| **OpenAPI / OAS 3.x** | Parameter | Ride Hailing, MaaS (Mobility as a Service), Carsharing, Bike Sharing, E-Scooter Sharing |
| **OpenAPI / OAS 3.x** | Security Scheme | Ride Hailing, MaaS (Mobility as a Service), Carsharing, Bike Sharing, E-Scooter Sharing |
| **APDS** | Place | Parking, Multi-modal Trip Planning |
| **APDS** | Rate | Parking, Multi-modal Trip Planning |
| **APDS** | Right Specification | Parking, Multi-modal Trip Planning |
| **APDS** | Session | Parking, Multi-modal Trip Planning |
| **APDS** | Observation | Parking, Multi-modal Trip Planning |
| **APDS** | Issuer | Parking, Multi-modal Trip Planning |
| **APDS** | Assignee | Parking, Multi-modal Trip Planning |
| **Linked GTFS** | Agency | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **Linked GTFS** | Route | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **Linked GTFS** | Trip | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **Linked GTFS** | Stop | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **Linked GTFS** | Stop Time | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **Linked GTFS** | Calendar | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **Linked GTFS** | Shape | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GTFS-LD** | Agency | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GTFS-LD** | Route | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GTFS-LD** | Trip | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GTFS-LD** | Stop | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GTFS-LD** | Stop Time | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GTFS-LD** | Service (Calendar) | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **GTFS-LD** | Feed | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **TransOnto / Transmodel Ontology** | Stop Point | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Demand-Responsive Transit |
| **TransOnto / Transmodel Ontology** | Line | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Demand-Responsive Transit |
| **TransOnto / Transmodel Ontology** | Route | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Demand-Responsive Transit |
| **TransOnto / Transmodel Ontology** | Vehicle Journey | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Demand-Responsive Transit |
| **TransOnto / Transmodel Ontology** | Vehicle Type | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry) |
| **TransOnto / Transmodel Ontology** | Operator | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Demand-Responsive Transit |
| **TransOnto / Transmodel Ontology** | Network | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry) |
| **TransOnto / Transmodel Ontology** | Tariff Zone | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) |
| **OSLO Mobility** | Transport Object | Public Transit (Bus), Public Transit (Metro), Bike Sharing, MaaS (Mobility as a Service) |
| **OSLO Mobility** | Stop | Public Transit (Bus), Public Transit (Metro), Bike Sharing, MaaS (Mobility as a Service) |
| **OSLO Mobility** | Route | Public Transit (Bus), Public Transit (Metro), MaaS (Mobility as a Service) |
| **OSLO Mobility** | Booking | Bike Sharing, MaaS (Mobility as a Service) |
| **OSLO Mobility** | Vehicle | Public Transit (Bus), Public Transit (Metro), Bike Sharing, MaaS (Mobility as a Service) |
| **OSLO Mobility** | Transport Zone | Public Transit (Bus), Public Transit (Metro), MaaS (Mobility as a Service) |
| **OSLO Mobility** | Operator | Public Transit (Bus), Public Transit (Metro), Bike Sharing, MaaS (Mobility as a Service) |
| **schema.org Transport Types** | BusOrCoach | Public Transit (Bus), Multi-modal Trip Planning |
| **schema.org Transport Types** | TrainTrip | Public Transit (Rail), Multi-modal Trip Planning |
| **schema.org Transport Types** | Flight | Commercial Aviation, Multi-modal Trip Planning |
| **schema.org Transport Types** | TaxiReservation | Ride Hailing |
| **schema.org Transport Types** | TrainStation | Public Transit (Rail), Multi-modal Trip Planning |
| **schema.org Transport Types** | BusStation | Public Transit (Bus), Multi-modal Trip Planning |
| **schema.org Transport Types** | Airport | Commercial Aviation, Multi-modal Trip Planning |
| **schema.org Transport Types** | Reservation | Public Transit (Rail), Public Transit (Bus), Commercial Aviation, Ride Hailing, Multi-modal Trip Planning |
| **GEONAMES / GeoSPARQL** | Spatial Object | All location-aware mobility domains |
| **GEONAMES / GeoSPARQL** | Geometry | All location-aware mobility domains |
| **GEONAMES / GeoSPARQL** | Feature | All location-aware mobility domains |
| **GEONAMES / GeoSPARQL** | Point | All location-aware mobility domains |
| **GEONAMES / GeoSPARQL** | Polygon | All location-aware mobility domains |
| **GEONAMES / GeoSPARQL** | Bounding Box | All location-aware mobility domains |
| **INSPIRE (Annex III — Transport Networks)** | Transport Network | Road Transport, Railways, Aviation, Waterways |
| **INSPIRE (Annex III — Transport Networks)** | Transport Link | Road Transport, Railways, Aviation, Waterways |
| **INSPIRE (Annex III — Transport Networks)** | Transport Node | Road Transport, Railways, Aviation, Waterways |
| **INSPIRE (Annex III — Transport Networks)** | Railway Line | Railways |
| **INSPIRE (Annex III — Transport Networks)** | Road | Road Transport |
| **INSPIRE (Annex III — Transport Networks)** | Waterway | Waterways |
| **INSPIRE (Annex III — Transport Networks)** | Air Route | Aviation |
| **INSPIRE (Annex III — Transport Networks)** | Vehicle Traffic Area | Road Transport, Railways, Aviation |
| **ERA Ontology** | Track | Railways (Interoperable Rail), Infrastructure Management |
| **ERA Ontology** | Operational Point | Railways (Interoperable Rail), Infrastructure Management |
| **ERA Ontology** | Contact Line System | Railways (Interoperable Rail), Infrastructure Management |
| **ERA Ontology** | Load Capability | Railways (Interoperable Rail), Infrastructure Management |
| **ERA Ontology** | Train Detection System | Railways (Interoperable Rail), Infrastructure Management |
| **ERA Ontology** | Section of Line | Railways (Interoperable Rail), Infrastructure Management |
| **ERA Ontology** | Track Parameter | Railways (Interoperable Rail), Infrastructure Management |
| **LDES** | Event Stream | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Real-time mobility data publishing |
| **LDES** | Collection | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Real-time mobility data publishing |
| **LDES** | View | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Real-time mobility data publishing |
| **LDES** | Fragmentation Strategy | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Real-time mobility data publishing |
| **LDES** | Member | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Real-time mobility data publishing |
| **LDES** | Tree Node | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Real-time mobility data publishing |
| **LDES** | Relation | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Real-time mobility data publishing |
| **CityGML / CityJSON (Transportation module)** | Transportation Complex | Urban Mobility, Public Transit Station Modelling, Autonomous Vehicles |
| **CityGML / CityJSON (Transportation module)** | Road | Urban Mobility, Autonomous Vehicles |
| **CityGML / CityJSON (Transportation module)** | Railway | Urban Mobility, Public Transit Station Modelling |
| **CityGML / CityJSON (Transportation module)** | Track | Urban Mobility, Public Transit Station Modelling |
| **CityGML / CityJSON (Transportation module)** | Square | Urban Mobility, Autonomous Vehicles |
| **CityGML / CityJSON (Transportation module)** | Traffic Area | Urban Mobility, Autonomous Vehicles |
| **CityGML / CityJSON (Transportation module)** | Auxiliary Traffic Area | Urban Mobility, Autonomous Vehicles |
