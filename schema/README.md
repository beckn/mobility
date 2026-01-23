# Global Mobility Standards Landscape

## Introduction

This document provides an objective overview of prominent **mobility standards** used across public transport, shared mobility, ticketing, journey planning, traffic context, parking, rail, and aviation. The list is ordered approximately by **real-world adoption and ecosystem visibility** (most adopted → least adopted), and includes a **JSON-LD support** column to indicate whether there is any published work that provides **JSON-LD** directly, or **RDF/OWL** artifacts that can be serialized as JSON-LD.

**JSON-LD support legend**

* **Yes (JSON-LD)**: a project publishes JSON-LD outputs or an `@context`.
* **Yes (RDF/OWL)**: RDF/OWL exists; JSON-LD is a compatible serialization.
* **Partial**: limited/experimental mappings exist, not widely used.
* **No known**: no notable JSON-LD/RDF/OWL schema publication found/known.

---

## Global Mobility Standards (Ordered by Adoption)

| Rank | Standard                    | Sub-industry                              | Has Schema?               | Has API Specs?           | Global / Regional   | Community Support | JSON-LD support? (where)                                                                                                      |
| ---: | --------------------------- | ----------------------------------------- | ------------------------- | ------------------------ | ------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
|    1 | **GTFS (Static)**           | Public transit schedules & stops          | Partial (CSV contract)    | No                       | **Global de-facto** | **Very High**     | **Yes (RDF/JSON-LD)** via Linked Transit / Linked Connections toolchains (GTFS → RDF/JSON-LD).                                |
|    2 | **GTFS Realtime (GTFS-RT)** | Public transit realtime operations        | Yes (Protobuf)            | Partial (feed interface) | **Global de-facto** | **Very High**     | **Yes (JSON-LD)** via `gtfsrt2lc`-style pipelines (GTFS-RT → Linked Connections JSON-LD fragments).                           |
|    3 | **GBFS**                    | Bike sharing & micromobility availability | Yes (JSON)                | Yes                      | **Global de-facto** | High              | **Yes (JSON-LD-compatible)** via **NGSI-LD / Smart Data Models** mappings (JSON-LD contexts + examples in that ecosystem).    |
|    4 | **IATA NDC**                | Aviation distribution (offers/orders)     | Yes (XML / JSON profiles) | Yes                      | Global              | High              | **No known** widely-used JSON-LD/RDF/OWL publication (mostly XML/JSON message specs).                                         |
|    5 | **IATA ONE Order**          | Aviation order management                 | Partial                   | Yes                      | Global              | Medium–High       | **No known** widely-used JSON-LD/RDF/OWL publication.                                                                         |
|    6 | **MDS**                     | Shared mobility regulation & ops          | Yes (OpenAPI)             | Yes                      | Global-leaning      | High              | **No known** mainstream JSON-LD/RDF/OWL schema project (it’s already JSON/REST; LD mappings are not standard).                |
|    7 | **CDS**                     | Curb & kerbside management                | Yes (OpenAPI)             | Yes                      | Global-leaning      | High              | **Partial**: curb LD efforts exist in the wild, but no clearly dominant CDS→JSON-LD canonical mapping.                        |
|    8 | **Calypso**                 | Closed-loop transit ticketing             | Yes                       | Partial                  | Global              | Medium–High       | **No known** JSON-LD/RDF/OWL publication.                                                                                     |
|    9 | **APDS**                    | Parking data                              | Yes (OpenAPI)             | Yes                      | Global-leaning      | Medium–High       | **Yes (JSON-LD-compatible)** via **Smart Data Models / NGSI-LD** parking and APDS-aligned models (JSON-LD contexts).          |
|   10 | **CIPURSE**                 | Ticketing security standard               | Yes                       | Partial                  | Global-leaning      | Medium            | **No known** JSON-LD/RDF/OWL publication.                                                                                     |
|   11 | **NeTEx (EN 16614)**        | Public transport data exchange            | Yes (XSD)                 | No                       | Regional (EU)       | Medium            | **Partial (RDF-capable)**: NeTEx-to-RDF conversions exist (XSD→RDF pipelines); not a single global canonical JSON-LD context. |
|   12 | **SIRI (EN 15531)**         | Public transport realtime exchange        | Yes (XSD)                 | Yes                      | Regional (EU)       | Medium            | **Partial (RDF-capable)**: seen in some linked-transit work; not a dominant canonical JSON-LD context.                        |
|   13 | **DATEX II**                | Road traffic & travel context             | Yes (XML)                 | Partial                  | Regional (EU)       | Medium–High       | **Partial (RDF-capable)**: semantic/linked-data work exists for traffic, but no single de-facto JSON-LD schema for DATEX II.  |
|   14 | **railML**                  | Rail data exchange                        | Yes (XSD)                 | No                       | Global-leaning      | Medium            | **No known** widely adopted JSON-LD/RDF/OWL publication (mostly XML).                                                         |
|   15 | **OSDM**                    | Rail ticket distribution                  | Yes (API specs)           | Yes                      | Global-leaning      | Medium            | **No known** widely adopted JSON-LD/RDF/OWL publication (API/spec-first).                                                     |
|   16 | **OJP**                     | Multimodal journey planning               | Yes (XSD)                 | Yes                      | Regional (EU)       | Medium            | **No known / Partial**: semantic models can be built, but no obvious canonical JSON-LD publication tied to OJP.               |
|   17 | **TRIAS (VDV 431-2)**       | Journey planning & departures             | Yes (XSD)                 | Yes                      | Regional (DACH)     | Medium            | **No known** widely used JSON-LD/RDF/OWL publication.                                                                         |
|   18 | **ITSO**                    | Smart ticketing (UK)                      | Partial                   | Partial                  | Regional (UK)       | Medium            | **No known** JSON-LD/RDF/OWL publication.                                                                                     |
|   19 | **Transmodel (EN 12896)**   | Public transport reference model          | No (conceptual)           | No                       | Regional (EU)       | Medium            | **Yes (OWL/RDF)** via Transmodel ontology work (OWL → JSON-LD serialization possible).                                        |

---

## MaaS Stack Buckets

### 1) Discovery & Catalog (static supply, assets, places)

* **GTFS (Static)**
* **NeTEx**
* **GBFS**
* **APDS**
* (Often paired reference models: **Transmodel**, IFOPT-like concepts when used)

### 2) Availability & Realtime Operations (what’s happening now)

* **GTFS-RT**
* **SIRI**
* **GBFS** (vehicle/station availability)
* **DATEX II** (incidents/road conditions affecting travel)

### 3) Journey Planning (routing, itineraries, traveler info interfaces)

* **OJP**
* **TRIAS**
* (Frequently relies on GTFS/NeTEx + realtime feeds)

### 4) Booking & Commerce (orders, reservations, distribution)

* **IATA NDC**
* **IATA ONE Order**
* **OSDM**

### 5) Ticketing & Entitlement (proof of right-to-travel; validation ecosystems)

* **Calypso**
* **ITSO**
* **CIPURSE**

### 6) Policy, Regulation & Right-of-Way Operations (city ↔ operator governance)

* **MDS**
* **CDS**

### 7) Reference Models & Semantics (conceptual backbone)

* **Transmodel** (and its OWL/RDF work)
* (NeTEx/SIRI often “inherit” semantic structure from Transmodel in practice)

---

## Heat Map: Standards vs MaaS Layers

**Legend:** ✅ strong fit / primary use · ◐ supports or commonly adjacent · — not typical

| Standard       | Discovery & Catalog    | Availability & Realtime | Journey Planning | Booking & Commerce        | Ticketing & Entitlement | Policy & Regulation | Semantics/Reference |
| -------------- | ---------------------- | ----------------------- | ---------------- | ------------------------- | ----------------------- | ------------------- | ------------------- |
| GTFS (Static)  | ✅                      | ◐                       | ✅                | —                         | —                       | —                   | ◐                   |
| GTFS-RT        | —                      | ✅                       | ◐                | —                         | —                       | —                   | —                   |
| GBFS           | ✅                      | ✅                       | ◐                | —                         | —                       | ◐                   | ◐                   |
| NeTEx          | ✅                      | ◐                       | ◐                | —                         | ◐ (fares)               | —                   | ✅                   |
| SIRI           | —                      | ✅                       | ◐                | —                         | —                       | —                   | ◐                   |
| Transmodel     | ◐                      | ◐                       | ◐                | —                         | ◐                       | —                   | ✅                   |
| OJP            | ◐                      | ◐                       | ✅                | —                         | —                       | —                   | ◐                   |
| TRIAS          | ◐                      | ◐                       | ✅                | —                         | —                       | —                   | ◐                   |
| MDS            | ◐                      | ✅ (ops reporting)       | —                | —                         | —                       | ✅                   | —                   |
| CDS            | ✅ (curb rules)         | ◐                       | ◐                | —                         | —                       | ✅                   | ◐                   |
| APDS           | ✅                      | ◐                       | ◐                | —                         | —                       | ◐                   | ◐                   |
| DATEX II       | ◐                      | ✅                       | ◐                | —                         | —                       | ◐                   | ◐                   |
| Calypso        | —                      | —                       | —                | ◐ (integration-dependent) | ✅                       | —                   | —                   |
| ITSO           | —                      | —                       | —                | ◐                         | ✅                       | —                   | —                   |
| CIPURSE        | —                      | —                       | —                | ◐                         | ✅ (security layer)      | —                   | —                   |
| railML         | ✅ (rail planning data) | ◐                       | ◐                | —                         | —                       | —                   | ◐                   |
| OSDM           | —                      | —                       | —                | ✅                         | ◐                       | —                   | —                   |
| IATA NDC       | —                      | —                       | —                | ✅                         | ◐                       | —                   | —                   |
| IATA ONE Order | —                      | —                       | —                | ✅                         | ◐                       | —                   | —                   |

---

If you want this “heat map” to be **more quantitative**, I can score each cell (e.g., 0–3) and compute a per-standard “coverage index” (how much of the MaaS stack it spans) versus “depth index” (how strongly it owns one layer).
