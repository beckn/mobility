# Mobility Domain Standards

This document catalogues key standards used across the mobility domain, assessed against criteria relevant to semantic interoperability and data integration.

**Column Definitions**

| Column | Description |
|--------|-------------|
| **Domain Standard** | Name of the mobility domain standard |
| **Supported Use Cases** | The transport / mobility contexts in which the standard is primarily applied |
| **Has Validation Schema?** | A machine-readable structural definition (e.g., JSON Schema, Protobuf schema) used to validate the format and constraints of data instances |
| **Has RDF/OWL Ontology?** | A formally defined semantic model expressing the concepts of this domain and their relationships using RDF and optionally OWL |
| **Has Persistent IRIs?** | Globally unique, stable identifiers assigned to concepts for unambiguous reference across systems |
| **Has Standard JSON–RDF Mapping?** | A formally specified transformation that maps the JSON representation of its concepts to an RDF graph (e.g., via JSON-LD context or defined conversion rules) |

---

## Standards Table

| Domain Standard | Supported Use Cases | Has Validation Schema? | Has RDF/OWL Ontology? | Has Persistent IRIs? | Has Standard JSON–RDF Mapping? |
|---|---|:---:|:---:|:---:|:---:|
| **GTFS Static** *(General Transit Feed Specification — Static)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit | No | No | No | No |
| **GTFS Realtime** *(GTFS-RT)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) | [Yes (Protobuf schema)](https://github.com/google/transit/blob/master/gtfs-realtime/proto/gtfs-realtime.proto) | No | No | No |
| **GTFS Flex** | Demand-Responsive Transit, Paratransit, Rural Transit | No | No | No | No |
| **GTFS Fares v2** | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Multi-modal Ticketing | No | No | No | No |
| **GTFS Pathways** | Public Transit (Metro), Public Transit (Rail), Accessibility / Station Navigation | No | No | No | No |
| **GTFS Levels** | Public Transit (Metro), Public Transit (Rail), Multi-level Station Navigation | No | No | No | No |
| **GTFS Translations** | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-lingual Transit Information | No | No | No | No |
| **GTFS Alerts** *(Service Alerts via GTFS-RT)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry) | [Yes (Protobuf schema)](https://github.com/google/transit/blob/master/gtfs-realtime/proto/gtfs-realtime.proto) | No | No | No |
| **GTFS Bikes** | Public Transit (Bus), Bike Sharing, Multi-modal Trip Planning | No | No | No | No |
| **GTFS Occupancy** *(via GTFS-RT VehiclePosition)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) | [Yes (Protobuf schema)](https://github.com/google/transit/blob/master/gtfs-realtime/proto/gtfs-realtime.proto) | No | No | No |
| **GBFS** *(General Bikeshare Feed Specification)* | Bike Sharing, E-Scooter Sharing, Moped Sharing, Cargo Bike Sharing | [Yes (JSON Schema)](https://github.com/MobilityData/gbfs-json-schema) | No | No | No |
| **MDS** *(Mobility Data Specification)* | E-Scooter Sharing, Bike Sharing, Moped Sharing, Ride Hailing, Carsharing | [Yes (JSON Schema)](https://github.com/openmobilityfoundation/mobility-data-specification) | No | No | No |
| **SIRI** *(Service Interface for Real-time Information)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram) | [Yes (XML Schema / XSD)](https://github.com/SIRI-CEN/SIRI) | No | No | No |
| **NeTEx** *(Network Timetable Exchange)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit, Multi-modal Trip Planning | [Yes (XML Schema / XSD)](https://github.com/NeTEx-CEN/NeTEx) | No | [Yes (NeTEx object IDs with codespace)](https://netex-cen.eu/model/) | No |
| **Transmodel** *(CEN EN 12896)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Public Transit (Tram), Demand-Responsive Transit | No | [Yes (partial; Transmodel Ontology / OntoTransmodel)](https://github.com/oeg-upm/transmodel-ontology) | [Yes (conceptual model IDs)](https://w3id.org/transmodel/) | No |
| **OJP** *(Open API for Distributed Journey Planning — CEN TS 17118)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning, Demand-Responsive Transit | [Yes (XML Schema / XSD)](https://github.com/openTdataCH/ojp-schemas) | No | No | No |
| **TOMP-API** *(Transport Operator MaaS Provider API)* | MaaS (Mobility as a Service), Ride Hailing, Bike Sharing, E-Scooter Sharing, Carsharing, Demand-Responsive Transit | [Yes (OpenAPI / JSON Schema)](https://github.com/TOMP-WG/TOMP-API) | No | No | No |
| **IATA NDC** *(New Distribution Capability)* | Commercial Aviation, Airline Ticketing & Distribution | [Yes (XML Schema / XSD)](https://www.iata.org/en/programs/airlines/ndc/) | No | No | No |
| **IATA ONE Order** | Commercial Aviation, Airline Order Management | [Yes (XML Schema / XSD)](https://www.iata.org/en/programs/passenger/one-order/) | No | No | No |
| **BOB** *(Backend Order & Booking — UIC / ERA)* | Railways (Interoperable Rail), Rail Ticketing | [Yes (JSON Schema via OpenAPI)](https://github.com/UnionInternationalCheminsdeFer/BOB) | No | No | No |
| **ISO 24014-1** *(Interoperable Fare Management)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Ticketing | No | No | No | No |
| **ISO 20022** *(Financial Messaging — used in transit fare payments)* | Multi-modal Ticketing, Transit Fare Payments | [Yes (XML Schema / XSD)](https://www.iso20022.org/catalogue-messages/iso-20022-messages-archive) | No | No | No |
| **TRIAS** *(Traveller Information Architecture Standard — VDV 431)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Multi-modal Trip Planning | [Yes (XML Schema / XSD)](https://github.com/VDVde/TRIAS) | No | No | No |
| **VDV 736 / VDV 454** *(ITCS/DFI real-time data — Germany)* | Public Transit (Bus), Public Transit (Tram) | [Yes (XML Schema / XSD)](https://www.vdv.de/schnittstellen.aspx) | No | No | No |
| **TAP TSI** *(Technical Specifications for Interoperability — Telematics Applications for Passengers — EU Rail)* | Railways (Interoperable Rail), Rail Ticketing | [Yes (XML Schema / XSD)](https://www.era.europa.eu/domains/registers/tap-tsi_en) | No | No | No |
| **ETSI DATEX II** | Road Traffic Management, Parking, Multi-modal Travel Information | [Yes (XML Schema / XSD)](https://datex2.eu/) | No | No | No |
| **OCPI** *(Open Charge Point Interface)* | Electric Vehicle Charging, EV Roaming | [Yes (JSON Schema via OpenAPI)](https://github.com/ocpi/ocpi) | No | No | No |
| **OCPP** *(Open Charge Point Protocol)* | Electric Vehicle Charging | [Yes (JSON Schema)](https://github.com/mobilityhouse/ocpp) | No | No | No |
| **OpenTripPlanner / OTP API** | Multi-modal Trip Planning, Public Transit (Bus), Public Transit (Rail), Cycling, Walking | [Yes (OpenAPI / JSON Schema)](https://github.com/opentripplanner/OpenTripPlanner) | No | No | No |
| **OpenAPI / OAS 3.x** *(used as transport envelope by many mobility APIs)* | Ride Hailing, MaaS, Carsharing, Bike Sharing, E-Scooter Sharing | [Yes (JSON Schema)](https://spec.openapis.org/oas/latest.html) | No | No | No |
| **Linked GTFS** | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) | No | [Yes (RDF vocabulary)](http://vocab.gtfs.org/) | [Yes (HTTP IRIs per resource)](http://vocab.gtfs.org/) | [Yes (CSV-to-RDF mapping defined)](https://github.com/OpenTransport/linked-gtfs) |
| **GTFS-LD** *(GTFS as Linked Data)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail) | No | [Yes (RDF/OWL vocabulary)](https://github.com/OpenTransport/gtfs-ld) | [Yes (HTTP IRIs)](http://vocab.gtfs.org/) | [Yes (JSON-LD context defined)](https://github.com/OpenTransport/gtfs-ld) |
| **TransOnto / Transmodel Ontology** | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Public Transit (Ferry), Demand-Responsive Transit | No | [Yes (OWL ontology)](https://github.com/oeg-upm/transmodel-ontology) | [Yes (persistent IRIs)](https://w3id.org/transmodel/ontology#) | No |
| **OSLO Mobility** *(Open Standards for Linked Organisations — Belgium)* | Public Transit (Bus), Public Transit (Metro), Bike Sharing, MaaS | No | [Yes (OWL / SHACL)](https://github.com/Informatievlaanderen/OSLOthema-mobiliteit) | [Yes (persistent IRIs)](https://data.vlaanderen.be/ns/mobiliteit) | [Yes (JSON-LD context defined)](https://data.vlaanderen.be/context/mobiliteit.jsonld) |
| **schema.org Transport Types** | Multi-modal Trip Planning, Ride Hailing, Public Transit | No | [Yes (RDFa / OWL-compatible)](https://schema.org/docs/schema_org_rdfa.html) | [Yes (schema.org IRIs)](https://schema.org/) | [Yes (JSON-LD context)](https://schema.org/docs/jsonldcontext.jsonld) |
| **GEONAMES / GeoSPARQL** | All location-aware mobility domains | No | [Yes (OWL ontology)](https://www.ogc.org/standard/geosparql/) | [Yes (persistent IRIs)](http://www.opengis.net/ont/geosparql) | No |
| **INSPIRE (Annex III — Transport Networks)* | Road Transport, Railways, Aviation, Waterways | [Yes (XML Schema / XSD)](https://inspire.ec.europa.eu/schemas/) | [Yes (GML application schema + INSPIRE ontology)](https://inspire.ec.europa.eu/ontology/) | [Yes (persistent IRIs)](https://inspire.ec.europa.eu/) | No |
| **ERA Ontology** *(European Union Agency for Railways)* | Railways (Interoperable Rail), Infrastructure Management | No | [Yes (OWL ontology)](https://data-interop.era.europa.eu/era-vocabulary/) | [Yes (persistent IRIs)](https://data.europa.eu/949/) | No |
| **LDES** *(Linked Data Event Streams)* | Public Transit (Bus), Public Transit (Metro), Public Transit (Rail), Real-time mobility data publishing | No | [Yes (RDF vocabulary)](https://w3id.org/ldes/specification) | [Yes (persistent IRIs)](https://w3id.org/ldes/) | [Yes (JSON-LD context defined)](https://w3id.org/ldes/specification) |
| **CityGML / CityJSON (Transportation module)** | Urban Mobility, Public Transit Station Modelling, Autonomous Vehicles | [Yes (JSON Schema for CityJSON)](https://www.cityjson.org/specs/) | [Yes (OWL ontology)](https://github.com/w3c-lbd-cg/OntoCityGML) | [Yes (persistent IRIs)](https://www.citygml.org/) | [Partial (CityJSON-LD experimental)](https://github.com/cityjson/cityjson-ld) |
| **SAE J2735 / DSRC** *(Dedicated Short-Range Communications — V2X)* | Connected & Autonomous Vehicles, Road Transport | [Yes (ASN.1 schema)](https://www.sae.org/standards/content/j2735_202309/) | No | No | No |
| **C-ITS (ETSI ITS standards)** | Connected & Autonomous Vehicles, Road Traffic Management | [Yes (ASN.1 / XML Schema)](https://www.etsi.org/technologies/automotive-intelligent-transport) | No | No | No |
| **OpenMaaS / MaaS Alliance API** | MaaS (Mobility as a Service), Multi-modal Booking | [Yes (OpenAPI / JSON Schema)](https://github.com/maas-alliance/OpenMaaS) | No | No | No |
| **APDS** *(Alliance for Parking Data Standards)* | Parking, Multi-modal Trip Planning | [Yes (JSON Schema via OpenAPI)](https://www.allianceforparkingdatastandards.org/) | No | No | No |
| **IXSI** *(Interface for X-Sharing Information — VDV)* | Carsharing, Bike Sharing | [Yes (XML Schema / XSD)](https://github.com/RWTH-i5-IDSG/ixsi) | No | No | No |
| **OSDM** *(Open Sales & Distribution Model — UIC)* | Railways (Interoperable Rail), Rail Ticketing | [Yes (JSON Schema via OpenAPI)](https://github.com/UnionInternationalCheminsdeFer/OSDM) | No | No | No |

---

## Summary Statistics

| Criterion | Count of Standards |
|---|:---:|
| Total standards listed | 44 |
| Has Validation Schema | 31 |
| Has RDF/OWL Ontology | 12 |
| Has Persistent IRIs | 12 |
| Has Standard JSON–RDF Mapping | 6 |

---

## Notes

1. **"Has Validation Schema?"** — Includes any machine-readable structural schema (XML Schema/XSD, JSON Schema, Protobuf `.proto`, ASN.1, OpenAPI with embedded schemas). A `No` indicates the specification is defined only in human-readable prose or spreadsheet/CSV form.

2. **"Has RDF/OWL Ontology?"** — A `Yes` requires a published, formally defined RDF vocabulary or OWL ontology that captures the domain concepts of the standard (not merely a generic upper ontology that happens to mention the domain).

3. **"Has Persistent IRIs?"** — A `Yes` requires that concept identifiers are stable HTTP(S) URIs or URNs explicitly assigned by the standardisation body and intended for long-term reference.

4. **"Has Standard JSON–RDF Mapping?"** — A `Yes` requires an officially published JSON-LD context file, a defined SPARQL/R2RML mapping, or an equivalent formally specified transformation. Unofficial community mappings are not counted.

5. **Popularity ordering** is a best-effort approximation based on global deployment breadth, number of published feeds/APIs, and community activity as of early 2025. GTFS variants are listed first due to their dominant global adoption in public transit data publishing, followed by other widely deployed open standards, then more domain-specific or regionally concentrated standards, and finally semantically enriched / Linked Data variants.
