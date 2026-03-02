# Public Transit (Bus) — Lifecycle Stress Test

## Use Case Narrative

Ravi wants to travel from Silk Board to Majestic Bus Stand in Bengaluru via BMTC buses. He opens a transit app, types his origin and destination, and the app shows him two route options — a direct Route 500C and a two-bus option with a transfer at KR Market. He selects the direct route, chooses an Adult single-trip fare, and pays for a digital ticket. The bus departs on time; Ravi tracks it live via the app. At Majestic, the journey ends. He rates the service and later raises a support case because he was overcharged.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Ravi | Consumer — the bus passenger | Represented by BAP |
| Transit App | BAP — renders routes and tickets | `beckn:BAP` |
| BMTC Platform | BPP — manages timetables, ticketing, real-time | `beckn:BPP` |
| Bus | Fulfillment vehicle — serves the route | `mobility:Vehicle` |

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Ravi submits a transit search request — origin stop, destination stop, preferred departure time, and passenger category.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripRequest`](../../schema/TripRequest/README.md) | Top-level search intent for public transit | `beckn:Intent` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Origin bus stop (Silk Board) | `beckn:FulfillmentStop` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Destination bus stop (Majestic) | `beckn:FulfillmentStop` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult passenger (affects fare eligibility) | `beckn:CategoryCode` | ✅ |
| [`PassengerGroup`](../../schema/PassengerGroup/README.md) | Number of passengers (1 adult) | `beckn:Quantity` | ✅ |

**Notes:** `TripRequest` extends `beckn:Intent` and carries `origin`, `destination`, `departureTime`, and `modes` (BUS). The `Stop` class with `stopId` and `stopName` identifies named bus stops. `RiderCategory` at search time enables the BPP to compute concession fares (e.g., student, senior) in the response.

---

#### Action: `on_search`
**Semantic intent:** The BMTC platform returns available bus routes, timetables, and fare options for the Silk Board → Majestic journey.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripResult`](../../schema/TripResult/README.md) | Top-level catalog of journey options | `beckn:Catalog` | ✅ |
| [`Itinerary`](../../schema/Itinerary/README.md) | Each journey option (direct or with transfer) | `beckn:Contract` | ✅ |
| [`Leg`](../../schema/Leg/README.md) | Each uninterrupted bus segment within an itinerary | `beckn:Fulfillment` | ✅ |
| [`Route`](../../schema/Route/README.md) | Route 500C details (stops, mode, operator) | `beckn:Item` | ✅ |
| [`Line`](../../schema/Line/README.md) | BMTC line serving this route | `beckn:Item` | ✅ |
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | The specific bus trip at the requested time | `beckn:Fulfillment` | ✅ |
| [`StopTime`](../../schema/StopTime/README.md) | Scheduled arrival/departure at each stop on the route | `beckn:TimePeriod` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Intermediate and terminal stops on the route | `beckn:FulfillmentStop` | ✅ |
| [`Fare`](../../schema/Fare/README.md) | Applicable fare for the journey | `beckn:Offer` | ✅ |
| [`FareProduct`](../../schema/FareProduct/README.md) | Adult single-trip fare product | `beckn:Offer` | ✅ |
| [`FareLegRule`](../../schema/FareLegRule/README.md) | Rules governing how this fare applies to this leg | `beckn:Policy` | ✅ |
| [`Network`](../../schema/Network/README.md) | BMTC network the route belongs to | `beckn:Catalog` | ✅ |
| [`Operator`](../../schema/Operator/README.md) | BMTC as the transit operator | `beckn:Provider` | ✅ |
| [`Timetable`](../../schema/Timetable/README.md) | Published timetable for the route | `beckn:Catalog` | ✅ |
| [`ServiceCalendar`](../../schema/ServiceCalendar/README.md) | Days on which the service operates | `beckn:TimePeriod` | ✅ |
| [`Frequency`](../../schema/Frequency/README.md) | Headway-based frequency (if no fixed timetable) | `beckn:Constraint` | ✅ |
| [`Transfer`](../../schema/Transfer/README.md) | Transfer rule at KR Market (for the 2-bus option) | `beckn:FulfillmentStop` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Refund terms for a digital bus ticket | `beckn:CancellationPolicy` | ✅ |

**Notes:** The two itinerary options — direct 500C and two-bus via KR Market — each appear as a separate `Itinerary` with one or two `Leg` entries respectively. The transfer itinerary uses `Transfer` with `minTransferTime` to describe the KR Market connection.

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Ravi selects the direct Route 500C journey and confirms the Adult single-trip fare.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | The specific 500C trip Ravi wants to board | `beckn:Fulfillment` | ✅ |
| [`FareProduct`](../../schema/FareProduct/README.md) | Adult single-trip fare product selected | `beckn:Offer` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult (confirming category for fare) | `beckn:CategoryCode` | ✅ |

---

#### Action: `on_select`
**Semantic intent:** The BPP confirms the selected journey is available and returns the confirmed fare and boarding details.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | Confirmed 500C trip with stop times | `beckn:Fulfillment` | ✅ |
| [`Fare`](../../schema/Fare/README.md) | Confirmed fare for the selected journey | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Base fare + any applicable taxes | `beckn:PriceComponent` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Boarding stop (Silk Board) with platform info | `beckn:FulfillmentStop` | ✅ |
| [`StopTime`](../../schema/StopTime/README.md) | Scheduled departure time from Silk Board | `beckn:TimePeriod` | ✅ |
| [`FareMedium`](../../schema/FareMedium/README.md) | Digital ticket medium (QR code or NFC) | `beckn:Entitlement` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Bus ticket cancellation / no-refund policy | `beckn:CancellationPolicy` | ✅ |

---

#### Action: `init`
**Semantic intent:** Ravi submits his passenger details for ticket issuance.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Passenger`](../../schema/Passenger/README.md) | Ravi's identity for ticket attribution | `beckn:Participant` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult category (for fare validation) | `beckn:CategoryCode` | ✅ |
| [`FareMedium`](../../schema/FareMedium/README.md) | Preferred medium (mobile app QR code) | `beckn:Entitlement` | ✅ |

---

#### Action: `on_init`
**Semantic intent:** The BPP returns the final ticket price and payment instructions.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Draft contract — the planned journey | `beckn:Contract` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final fare breakup before payment | `beckn:PriceComponent` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Binding cancellation policy (typically no refund for bus tickets) | `beckn:CancellationPolicy` | ✅ |
| [`Entitlement`](../../schema/Entitlement/README.md) | Seat entitlement or concession entitlement if applicable | `beckn:Entitlement` | ✅ |

---

#### Action: `confirm`
**Semantic intent:** Ravi pays and confirms the ticket purchase.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Order being confirmed | `beckn:Contract` | ✅ |
| [`Passenger`](../../schema/Passenger/README.md) | Confirming passenger identity | `beckn:Participant` | ✅ |

---

#### Action: `on_confirm`
**Semantic intent:** BPP issues the digital bus ticket and returns the confirmed journey contract.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Confirmed journey contract | `beckn:Contract` | ✅ |
| [`Ticket`](../../schema/Ticket/README.md) | Issued digital bus ticket with QR code | `beckn:Entitlement` | ✅ |
| [`TravelDocument`](../../schema/TravelDocument/README.md) | The digital travel document (QR code or PDF ticket) | `beckn:Entitlement` | ✅ |
| [`FareProduct`](../../schema/FareProduct/README.md) | The purchased fare product with validity scope | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final fare breakup (binding) | `beckn:PriceComponent` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Boarding stop and destination stop references | `beckn:FulfillmentStop` | ✅ |
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | The 500C trip reference for boarding | `beckn:Fulfillment` | ✅ |

---

### Stage 3 — Fulfillment

---

#### Action: `status`
**Semantic intent:** Ravi's app checks whether the bus has departed and how far it is from Silk Board.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Journey being queried | `beckn:Contract` | ✅ |

---

#### Action: `on_status`
**Semantic intent:** The BPP returns the real-time status of the bus — live location, current stop, and schedule adherence.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | State update for the journey | `beckn:Contract` | ✅ |
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Current live location of the 500C bus | `beckn:Tracking` | ✅ |
| [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | Predicted arrival delays at upcoming stops | `beckn:Tracking` | ✅ |
| [`OccupancyStatus`](../../schema/OccupancyStatus/README.md) | Current passenger load (seats available) | `beckn:State` | ✅ |
| [`Alert`](../../schema/Alert/README.md) | Any service disruption on the route | `beckn:Alert` | ✅ |

---

#### Action: `track`
**Semantic intent:** Ravi opens the live bus tracker map.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Journey being tracked | `beckn:Contract` | ✅ |

---

#### Action: `on_track`
**Semantic intent:** BPP returns the real-time tracking data for the 500C bus.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Current GPS coordinates, bearing, speed of bus | `beckn:Tracking` | ✅ |
| [`MonitoredVehicleJourney`](../../schema/MonitoredVehicleJourney/README.md) | Real-time vehicle journey with schedule adherence | `beckn:Tracking` | ✅ |
| [`MonitoredCall`](../../schema/MonitoredCall/README.md) | Predicted arrival at Silk Board stop | `beckn:Tracking` | ✅ |
| [`StopMonitoring`](../../schema/StopMonitoring/README.md) | All predicted arrivals at Silk Board stop | `beckn:Tracking` | ✅ |
| [`Prognosis`](../../schema/Prognosis/README.md) | Arrival time prediction with confidence | `beckn:Tracking` | ✅ |

---

#### Action: `update`
**Semantic intent:** An alert is issued — the 500C is diverted due to roadwork; passengers must change at KR Market.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Contract modification — route change/diversion | `beckn:Contract` | ✅ |
| [`Alert`](../../schema/Alert/README.md) | Service disruption alert (diversion) | `beckn:Alert` | ✅ |
| [`AffectedLine`](../../schema/AffectedLine/README.md) | The 500C line identified as affected | `beckn:Alert` | ✅ |

---

#### Action: `on_update`
**Semantic intent:** BPP acknowledges the update with revised itinerary (new transfer at KR Market).

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Updated journey with KR Market transfer | `beckn:Contract` | ✅ |
| [`Itinerary`](../../schema/Itinerary/README.md) | Revised itinerary with two legs | `beckn:Contract` | ✅ |
| [`Transfer`](../../schema/Transfer/README.md) | Transfer details at KR Market | `beckn:FulfillmentStop` | ✅ |

---

#### Action: `cancel`
**Semantic intent:** Ravi decides to cancel the ticket (e.g., the diversion makes the journey impractical).

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Journey order being cancelled | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Bus ticket cancellation policy | `beckn:CancellationPolicy` | ✅ |

---

#### Action: `on_cancel`
**Semantic intent:** BPP processes the cancellation (bus tickets are typically non-refundable, but a platform credit may be issued).

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Cancelled journey contract | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Applied policy | `beckn:CancellationPolicy` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Cancellation receipt (zero refund or platform credit) | `beckn:Invoice` | ✅ |
| [`Entitlement`](../../schema/Entitlement/README.md) | Platform credit entitlement issued | `beckn:Entitlement` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`
**Semantic intent:** Ravi rates the BMTC 500C service — 3 stars (crowded bus, driver was ok).

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | 3-star rating for the service (ratedEntityType: SERVICE) | `beckn:RatingInput` | ✅ |
| [`Feedback`](../../schema/Feedback/README.md) | Tags: OVERCROWDED, ON_TIME | `beckn:Feedback` | ✅ |

---

#### Action: `on_rating`
**Semantic intent:** BPP acknowledges the rating.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | Confirmed rating | `beckn:RatingInput` | ✅ |

---

#### Action: `support`
**Semantic intent:** Ravi was charged ₹42 but the correct fare is ₹32. He raises a billing complaint.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Billing complaint (type: COMPLAINT) | `beckn:SupportRequest` | ✅ |

---

#### Action: `on_support`
**Semantic intent:** BPP provides support contact and reviews the ticket for refund eligibility.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Updated support case with ticket ID | `beckn:SupportRequest` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Original ticket receipt for dispute review | `beckn:Invoice` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | BMTC helpline or chat link | `beckn:SupportInfo` | ✅ |

---

## Coverage Summary

| Class | Actions Used In | Lifecycle Stage |
|-------|----------------|----------------|
| `TripRequest` | search | Discovery |
| `Stop` | search, on_search, on_select, on_confirm | Discovery, Contracting |
| `RiderCategory` | search, select, init | Discovery, Contracting |
| `PassengerGroup` | search | Discovery |
| `TripResult` | on_search | Discovery |
| `Itinerary` | on_search, on_init, confirm, on_confirm, status, track, update, on_update, cancel, on_cancel | All stages |
| `Leg` | on_search | Discovery |
| `Route` | on_search | Discovery |
| `Line` | on_search | Discovery |
| `VehicleJourney` | on_search, select, on_select, on_confirm | Discovery, Contracting |
| `StopTime` | on_search, on_select | Discovery, Contracting |
| `Fare` | on_search, on_select | Discovery, Contracting |
| `FareProduct` | on_search, select, on_confirm | Discovery, Contracting |
| `FareLegRule` | on_search | Discovery |
| `Network` | on_search | Discovery |
| `Operator` | on_search | Discovery |
| `Timetable` | on_search | Discovery |
| `ServiceCalendar` | on_search | Discovery |
| `Frequency` | on_search | Discovery |
| `Transfer` | on_search, on_update | Discovery, Fulfillment |
| `CancellationPolicy` | on_search, on_select, on_init, cancel, on_cancel | Discovery, Contracting, Fulfillment |
| `FareMedium` | on_select, init | Contracting |
| `FareBreakup` | on_select, on_init, on_confirm | Contracting |
| `Passenger` | init, confirm | Contracting |
| `Entitlement` | on_init, on_cancel | Contracting |
| `Ticket` | on_confirm | Contracting |
| `TravelDocument` | on_confirm | Contracting |
| `TripUpdate` | on_status, update, on_update | Fulfillment |
| `VehiclePosition` | on_status, on_track | Fulfillment |
| `StopTimeUpdate` | on_status | Fulfillment |
| `OccupancyStatus` | on_status | Fulfillment |
| `Alert` | on_status, update | Fulfillment |
| `MonitoredVehicleJourney` | on_track | Fulfillment |
| `MonitoredCall` | on_track | Fulfillment |
| `StopMonitoring` | on_track | Fulfillment |
| `Prognosis` | on_track | Fulfillment |
| `AffectedLine` | update | Fulfillment |
| `Receipt` | on_cancel, on_support | Fulfillment, Post-Fulfillment |
| `Rating` | rating, on_rating | Post-Fulfillment |
| `Feedback` | rating | Post-Fulfillment |
| `SupportCase` | support, on_support | Post-Fulfillment |
| `ContactHandle` | on_support | Post-Fulfillment |

---

## Gap Report

| Gap | Description | Severity |
|-----|-------------|----------|
| No gaps detected | All schema classes required for the public transit bus lifecycle exist in the mobility schema. The GTFS, SIRI, and NeTEx concepts are well-represented across `VehicleJourney`, `StopTime`, `MonitoredVehicleJourney`, `MonitoredCall`, `Prognosis`, `Alert`, `AffectedLine`, and `ServiceCalendar`. | — |

> **Design notes:**
> - The `Frequency` class handles headway-based BMTC services where buses run "every 10 minutes" rather than on a fixed timetable.
> - The `ServiceCalendar` and `DayType` classes together define which days the 500C operates (e.g., not on public holidays).
> - The `StopMonitoring` + `MonitoredCall` + `Prognosis` trio faithfully represents the SIRI real-time delivery stack.
