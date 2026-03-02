# Stress Testing Schema Against Mobility Use Cases
This document contains a methodical framework to stress test the current schema against several mobility use cases. This document can also be used by AI Agents to develop robust stress test cases to test mobility use cases. 

## Context

**Beckn** has evolved in its positioning from a simple P2P protocol for commerce, to a more sophisticated ***fabric for value exchange*** with an *all-new protocol architecture*, and for the first time, a *run-time, utility-grade infrastructure* [[1]](https://github.com/beckn/core_schema/blob/core-schema-v2.0-fixes/docs/1_Introduction.md). 

Value is perceived differently by everyone. So it is important to construct it in a way that it can be exchanged effectively on a protocol.  

To understand value, we need to start with an abstract entity called a **Resource** **(IRI - beckn:Resource)**. In canonical terms, a **Resource** can be considered as a subclass of **schema:Thing**. 

While **schema:Thing** represents the most generic type of object, it is of little value to Beckn. So we are going to make it slightly more useful and call it [Resource](https://schema.beckn.io/core/Resource). The *canonical difference* between a Thing and a Resource (in Beckn) is this – 

<p style="text-align:center; font-weight: bold">"A Resource <i>always</i> carries value"</p>

Anything can be perceived as a Resource. This is typically something of value that a consumer wants. Notice the subtle difference in definition. A Resource is something that a **consumer** "wants", _not_ what a consumer wants to "_buy_"... The act of buying is just _one_ way the consumer can get the Resource. 

That is because, **value** is not always monetary value. Even a simple resource like a retail product say, bread, eggs, or butter doesn't carry monetary value. It carries value when the consumer is hungry for breakfast, but when they are not hungry, the same items do not carry any value.  Likewise, a resource can carry many kinds of value depending on the context it is sought in — like economic value, strategic value, sentimental value, survival value, social value etc. For example, an employment has monetary value, economic value, and social value depending on the context it is perceived in. 

A skilled worker does not _buy_ an employment (i.e. resource) by paying money. He "gains" an employment by providing his credentials and showcasing his skills and/or talent. For a patient suffering from an ailment, a "diagnosis" or a "treatment", or a "cure" is the resource.

Every **Consumer** looking to obtain a resource needs someone who can provide them with that resource. In Beckn, that someone is called a **Provider**. In Beckn, a Consumer is onboarded by an business entity called a **Beckn Application Platform (BAP)**; and a Provider is onboarded by a business entity called a **Beckn Provider Platform (BPP)**. The BAP and BPP communicate with each other using Beckn Protocol.

The Consumer and Provider exchange value by going through the following flows. 

1. **Catalog Publishing and Discovery Flows** : The provider publishes a catalog of product offerings. The consumer describes the intent to obtain a resource and discovers some product offerings in that catalog that match the consumer's intent. The outcome of these flow is for the consumer to identify a set of product offerings and the provider(s) they want to obtain it from. 
   
2. **Contracting Flows** : The consumer and provider(s) agree on a specific order value that must be transferred the consumer to obtain that resource. This agreement can sometimes happen unilaterally, sometimes bilaterally through bargaining, negotiation, bidding, auctioning, etc. Furthermore, they both also agree on the terms of the contract, contract serviceability, and liabilities. The outcome of this flow is to establish a dual digitally signed contract between the consumer and the provider.
   
3. **Fulfillment Flows** : The provider fulfills the contract by delivering the resource to the consumer either themselves or via a fulfillment agent. The consumer tracks the delivery of the resource either in real-time or non-real-time. The consumer and provider also sometimes update the contract at this stage by re-agreeing on the order value, the terms of service, payment, and liabilities. The outcome of this flow is to ultimately deliver the resource to the consumer as per the terms agreed in the established contract. 
   
4. **Post-fulfillment Flows** : The customer contacts the provider's customer support if needed. The provider also provides support to the consumer either directly or via a customer support agent. The consumer also rates various aspects of the whole discovery, contracting and fulfillment journey in obtaining that resource. The provider also sometimes requests additional feedback from the consumer against a specific rating provided by the consumer. Furthermore, in some cases, there is also a payment settlement flow that gets invoked based on the terms agreed in the contract. Additionally, any support tickets, grievances, refunds, returns, penalties, etc are calculated and applied at this stage. 

With this knowledge in mind, lets us see how these abstract concepts can help us understand how a mobility ecosystem can exist on Beckn.  

### Mobility on Beckn
In the most abstract sense, the sole purpose of mobility is to transport humans from one point to another. For the more geeky reader, these points are in 4-space where each point is described as three coordinates in space and one of time (x,y,z,t). So a movement of a person from Point A (x1, y1, z1, t1) to Point B (x2, y2, z2, t2) where t2 is > t1 always (*We cannot go back in time... yet*) — is called **Mobility**. 

In a networked, mobility ecosystem operating on the Beckn Fabric, a MaaS BPP:
1. Publishes a catalog of MaaS products offered by itself or more mobility providers it onboards
2. Manages and allocates the mobility supply
3. Calculates serviceability
4. Creates and manages bookings

While a MaaS BAP:
1. Discovers and renders available mobility products to the consumer
2. Relays the consumer's booking, tracking, and support requests to one or more BPPs

This document uses the following artifacts from the repository:
1. `schema` : A directory of classes used in popular mobility use cases
2. `docs` : A directory of documentation for developer implementing mobility use cases on beckn
3. `tests` : A directory of test cases to stress test the schema
4. `GOVERNANCE` : A document explaining how this schema can evolve
   
#### Current Scope of Use Cases
The current mobility schema supports the following use cases:

1. [Ride Hailing](./ride_hailing/README.md)
2. [Advance Cab Reservation](./advance_cab_reservation/README.md)
3. [Cab Rental](./cab_rental/README.md)
4. [Public Transit (Bus)](./public_transit_bus/README.md)
5. [Public Transit (Metro)](./public_transit_metro/README.md)
6. [Intercity Bus Transport](./intercity_bus/README.md)

#### Scope for Future Use Cases
1. Airlines (Domestic)
2. Airlines (International)
3. Railways (Domestic)
4. Railways (International)
5. Public Transit (Ferry)
6. Bike Sharing
7. Shared Cab
8. Personal Car Rental


## Forces
- The classes defined in this schema MUST be mutually exclusive so as to describe unique components of all the flows (positive and negative) across all the use cases covered in the scope in a lossless manner
- The classes defined in this schema MUST be collectively exhaustive so as to cover as many variations of the use case across jurisdictions
- The classes defined in this schema SHOULD inherit as many properties from the Beckn Core schema as possible
- Each keyword in the schema (Class Name, Property, Enumeration), MUST have an associated IRI (Internationalized Resource Identifier) available at `https://schema.beckn.io/mobility/{SchemaName}`
- Classes must align with the Beckn 4-stage order lifecycle: **Discovery → Contracting → Fulfillment → Post-Fulfillment**

---

## Problem Statement

1. How do we ensure that the current mobility schema list is exhaustive and covers all use cases within the scope?
2. How do we verify that the current mobility schema classes cleanly extend from the core primitives of Beckn?
3. How do we confirm that the schema is mutually exclusive — i.e., no two classes describe the same concept at the same lifecycle stage?
4. How do we detect schema gaps — concepts needed by real-world use cases that are not yet covered by any mobility class?

---

## Stress Test Methodology

### What is a Lifecycle Stress Test?

A **lifecycle stress test** is a structured walk-through of a specific mobility use case across all Beckn API actions, checking at each step which schema classes are required and whether those classes exist, are correctly defined, and carry the right properties.

A stress test is **not** a unit test or integration test. It is a **semantic completeness check** — a way to reason about whether the vocabulary is rich enough to express everything needed for a use case without ambiguity or loss of information.

### Test Structure

Each use case stress test follows this structure:

1. **Use Case Narrative** — A plain-language description of the scenario from a consumer's perspective
2. **Actors** — BAP (consumer application), BPP (provider platform), consumer (human), and provider (mobility operator)
3. **Lifecycle Stage Walkthrough** — For each Beckn API action pair (`search/on_search`, `select/on_select`, etc.), the test documents:
   - The **semantic intent** of the action
   - The **schema classes** required to express the request and response
   - A **class coverage check** (does the class exist? does it have the right properties?)
   - Any **identified gaps**
4. **Coverage Summary Table** — A consolidated table of all classes used and their lifecycle stage
5. **Gap Report** — A structured list of any missing or incomplete classes

### Beckn API Action Pairs

| Stage | BAP → BPP | BPP → BAP | Semantic Purpose |
|-------|-----------|-----------|-----------------|
| Discovery | `search` | `on_search` | Consumer expresses intent; provider returns matching catalog |
| Contracting | `select` | `on_select` | Consumer selects an option; provider confirms serviceability |
| Contracting | `init` | `on_init` | Consumer initiates order with participant details; provider returns payment terms |
| Contracting | `confirm` | `on_confirm` | Consumer confirms order with payment; provider creates contract |
| Fulfillment | `status` | `on_status` | Consumer polls for fulfillment state; provider returns current state |
| Fulfillment | `track` | `on_track` | Consumer requests live tracking; provider returns tracking endpoint |
| Fulfillment | `update` | `on_update` | Consumer or provider modifies the contract; both acknowledge changes |
| Fulfillment / Post | `cancel` | `on_cancel` | Consumer requests cancellation; provider applies policy and confirms |
| Post-Fulfillment | `rating` | `on_rating` | Consumer submits rating; provider acknowledges |
| Post-Fulfillment | `support` | `on_support` | Consumer raises support issue; provider returns support info |

### Schema Coverage Check Criteria

For each class used in a test, verify:

| Check | Criterion |
|-------|-----------|
| **Existence** | Does the class have a directory under `schema/`? |
| **Parent alignment** | Is the parent class (`rdfs:subClassOf`) the correct Beckn lifecycle entity? |
| **Own properties** | Does the class carry the properties needed for this use case? |
| **Inherited properties** | Does the parent class provide the generic properties needed? |
| **IRI** | Does the class have a valid canonical IRI at `https://schema.beckn.io/mobility/{ClassName}`? |

### Pass / Fail Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Class exists, parent is correct, properties are sufficient |
| ⚠️ | Class exists but parent or properties may need review |
| ❌ | Class is missing from schema — gap identified |
| 🔁 | Class is reused from another lifecycle stage (by design) |

---

## How to Run a Stress Test

Stress tests in this directory are **document-form** semantic checks designed to be walked through by a human expert or an AI agent. To run a stress test:

1. Open the relevant use case file (e.g., [`tests/ride_hailing/README.md`](./ride_hailing/README.md))
2. Walk through each API action section
3. For each class listed, open `schema/{ClassName}/README.md` and verify the criteria above
4. Record gaps and open GitHub Issues at [`beckn/mobility/issues`](https://github.com/beckn/mobility/issues)
5. If gaps are found, update `schema/generate_readmes.py` to add the missing class, then run `python3 schema/generate_readmes.py`

---

## Cross-Use-Case Schema Reuse Matrix

The table below shows which schema classes are shared across multiple use cases, indicating their cross-cutting importance.

| Class | Ride Hailing | Advance Cab | Cab Rental | Public Transit Bus | Public Transit Metro | Intercity Bus |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| `RideRequest` | ✅ | ✅ | — | — | — | — |
| `TripRequest` | — | — | — | ✅ | ✅ | ✅ |
| `TripSpecification` | — | — | — | — | — | ✅ |
| `PlanningResult` | ✅ | ✅ | ✅ | — | — | — |
| `Timetable` | — | — | — | ✅ | ✅ | ✅ |
| `Route` | — | — | — | ✅ | ✅ | ✅ |
| `VehicleJourney` | — | — | — | ✅ | ✅ | ✅ |
| `Leg` | — | — | — | ✅ | ✅ | ✅ |
| `Stop` | — | — | — | ✅ | ✅ | ✅ |
| `StopTime` | — | — | — | ✅ | ✅ | ✅ |
| `Trip` | ✅ | ✅ | ✅ | — | — | — |
| `Driver` | ✅ | ✅ | ✅ | — | — | — |
| `Vehicle` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `FareEstimate` | ✅ | ✅ | ✅ | — | — | — |
| `FareProduct` | — | — | — | ✅ | ✅ | ✅ |
| `Fare` | — | — | — | ✅ | ✅ | ✅ |
| `FareBreakup` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `Ticket` | — | — | — | ✅ | ✅ | ✅ |
| `TravelDocument` | — | — | — | ✅ | ✅ | ✅ |
| `Receipt` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `VehiclePosition` | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `TripUpdate` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `CancellationPolicy` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `Rating` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `Review` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `Feedback` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `SupportCase` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ContactHandle` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `Alert` | — | — | — | ✅ | ✅ | ✅ |
| `VehicleCategory` | ✅ | ✅ | ✅ | — | — | — |
| `VehicleType` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `Passenger` | — | — | — | ✅ | ✅ | ✅ |
| `Rider` | ✅ | ✅ | ✅ | — | — | — |
| `RiderCategory` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `BaggageAllowance` | — | — | — | — | — | ✅ |
| `Seat` | — | — | — | — | — | ✅ |
| `SurgeMultiplier` | ✅ | — | — | — | — | — |
| `WaitingPolicy` | ✅ | ✅ | ✅ | — | — | — |
| `NoShowPolicy` | ✅ | ✅ | — | — | — | — |
| `PickupPolicy` | ✅ | ✅ | ✅ | — | — | — |
| `DropPolicy` | ✅ | ✅ | ✅ | — | — | — |
| `PricingModel` | ✅ | ✅ | ✅ | — | — | — |
| `SystemPricingPlan` | — | — | ✅ | — | — | — |
| `BookingRule` | — | ✅ | — | ✅ | ✅ | ✅ |
| `Interchange` | — | — | — | — | ✅ | — |
| `StopPlace` | — | — | — | — | ✅ | — |
| `Quay` | — | — | — | — | ✅ | — |
| `Pathway` | — | — | — | — | ✅ | — |
| `LostAndFoundItem` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## Test Files

| Use Case | Test File | Status |
|----------|-----------|--------|
| Ride Hailing | [tests/ride_hailing/README.md](./ride_hailing/README.md) | ✅ Complete |
| Advance Cab Reservation | [tests/advance_cab_reservation/README.md](./advance_cab_reservation/README.md) | ✅ Complete |
| Cab Rental | [tests/cab_rental/README.md](./cab_rental/README.md) | ✅ Complete |
| Public Transit (Bus) | [tests/public_transit_bus/README.md](./public_transit_bus/README.md) | ✅ Complete |
| Public Transit (Metro) | [tests/public_transit_metro/README.md](./public_transit_metro/README.md) | ✅ Complete |
| Intercity Bus Transport | [tests/intercity_bus/README.md](./intercity_bus/README.md) | ✅ Complete |

---

## Consolidated Gap Report

After running stress tests across all 6 use cases, **3 schema gaps** were identified. All gaps are in the ride hailing / rental cluster. Transit use cases (bus, metro, intercity) are fully covered.

| # | Gap Class | Description | Use Cases Affected | Severity | Proposed Resolution |
|---|-----------|-------------|-------------------|----------|---------------------|
| 1 | **`VehicleFeature`** | `VehicleType` has no structured properties for vehicle amenities shown at catalog time: boot space, A/C availability, child seat, WiFi, charging points, reclining seats. Currently only expressible via untyped `tags` inherited from `beckn:Item`. | Ride Hailing, Advance Cab, Cab Rental, Intercity Bus | Medium | Create `VehicleFeature` class extending `beckn:Feature` (following the `BikeAllowed` pattern). Properties: `featureCode` (schema:Text), `featureValue` (schema:Text). Example instances: `BootSpace` (featureValue: "350L"), `AirConditioning` (featureValue: "yes"), `WiFi` (featureValue: "yes"). |
| 2 | **`RoutePreference`** | No mobility class for capturing ride route preferences (toll vs non-toll, highway vs city). The BPP must present a form in `on_init` for ride hailing to collect this preference — it affects the final fare. Beckn protocol's `XInput` mechanism handles the form delivery, but the mobility schema has no semantically-typed class for the preference itself. | Ride Hailing, Advance Cab, Cab Rental | Medium | Create `RoutePreference` class extending `beckn:Form` (or `beckn:Descriptor`) with properties: `tollPreference` (TOLL / NO_TOLL / ANY), `routeType` (HIGHWAY / CITY / ANY), `acPreference` (AC / NON_AC / ANY). This enables type-safe preference handling across BPP implementations. |
| 3 | **`FulfillmentAuthorization`** | The ride-start / rental-start OTP is issued by BPP at driver assignment (via `on_update`). In Beckn core, this is `beckn:Fulfillment.start.authorization` with `type: OTP` and `token`. The `Trip` class does not explicitly surface this relationship — BAP implementations must know to look in `fulfillments[].start.authorization` from core. | Ride Hailing, Advance Cab, Cab Rental | Medium | Add `startAuthorization` property to the `Trip` class, typed as `beckn:Authorization` from core (with `type` OTP/PIN/QR and `token`). Alternatively, create a `FulfillmentAuthorization` mobility class that wraps the core concept with clear documentation. |

### Key Design Decisions Confirmed by Stress Testing

| Decision | Rationale |
|----------|-----------|
| `on_confirm` for ride hailing returns DRIVER ALLOCATION STATUS, not driver details | Driver details arrive only when a driver actually accepts — this is via BPP-pushed `on_update`. Returning placeholder driver info at `on_confirm` would be misleading. |
| `on_update` is the primary channel for driver assignment in ride hailing | The BPP pushes the full order state + driver + vehicle + OTP when a driver accepts. This is the most information-dense message in the ride lifecycle. |
| Bus and Metro `on_update` carry NOTHING in contract changes | Tickets remain valid regardless of route diversions or delays. Only informational `Alert` objects are pushed. No `TripUpdate.contractChanges` needed. |
| Intercity bus `on_update` carries tracking active flag + GPS URL | After departure, BPP activates live tracking and pushes the tracking endpoint. This is different from bus/metro (no tracking) and ride hailing (tracking active from `on_update` at driver assignment). |
| Search intent type varies by use case | Ride hailing: GPS `Place`. City bus: `Stop` (stop-to-stop). Metro: `StopPlace` (station-to-station). Intercity bus: `Place` (city-to-city). These are semantically distinct and must be implemented separately. |
| Tickets are Verifiable Credentials (VCs) for transit | `TravelDocument.documentType: QR_CODE` with a signed token enables VC-based ticketing for bus, metro, and intercity bus. The `Ticket` class carries the record; `TravelDocument` carries the proof. |
