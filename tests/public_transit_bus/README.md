# Public Transit (Bus) — Lifecycle Stress Test

## Use Case Narrative

Ravi wants to travel from Silk Board bus stop to Majestic Bus Stand in Bengaluru via BMTC. He opens a transit app, selects his boarding stop and alighting stop, and the app shows two options — direct Route 500C and a two-bus option via KR Market. He selects the direct route, picks an Adult single-trip fare, pays online, and receives a QR code ticket. At Silk Board he scans the QR to board. The bus departs; Ravi checks live location on the app. A route diversion is announced mid-journey. He rates the service and raises a billing complaint afterwards.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Ravi | Consumer — bus passenger | Represented by BAP |
| Transit App | BAP — renders routes and tickets | `beckn:BAP` |
| BMTC Platform | BPP — manages timetables, ticketing, real-time | `beckn:BPP` |

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Ravi selects his boarding stop and alighting stop. No GPS needed — transit search is station-to-station.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Top-level transit intent | [`TripRequest`](../../schema/TripRequest/README.md) | `origin`, `destination`, `departureTime`, `modes: BUS` | ✅ |
| Boarding stop (Silk Board) | [`Stop`](../../schema/Stop/README.md) | `stopId`, `stopName` | ✅ |
| Alighting stop (Majestic) | [`Stop`](../../schema/Stop/README.md) | `stopId`, `stopName` | ✅ |
| Passenger type | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId: ADULT` | ✅ |
| Number of passengers | [`PassengerGroup`](../../schema/PassengerGroup/README.md) | `groupSize: 1` | ✅ |

**Notes:** Transit search is STOP-TO-STOP, not GPS. `TripRequest.origin` and `.destination` embed `Stop` references (not `Place` with GPS coordinates). This is a fundamental difference from ride hailing.

---

#### Action: `on_search`
**Semantic intent:** BMTC returns available routes, timetables, and fare products for the journey.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Catalog of journey options | [`TripResult`](../../schema/TripResult/README.md) | — | ✅ |
| Each journey option (direct / with transfer) | [`Itinerary`](../../schema/Itinerary/README.md) | `legs`, `totalDuration`, `departureTime`, `arrivalTime` | ✅ |
| Each bus segment | [`Leg`](../../schema/Leg/README.md) | `mode: BUS`, `origin`, `destination`, `startTime` | ✅ |
| **Route 500C details** | [`Route`](../../schema/Route/README.md) | `routeId`, `shortName: 500C`, `routeType: BUS` | ✅ |
| Specific bus trip at requested time | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode`, `stopTimes` | ✅ |
| Scheduled stop times | [`StopTime`](../../schema/StopTime/README.md) | `arrivalTime`, `departureTime`, `stopSequence` | ✅ |
| **Adult single-trip fare product** | [`FareProduct`](../../schema/FareProduct/README.md) | `fareProductId`, `riderCategoryId: ADULT`, `durationType: SINGLE_TRIP` | ✅ |
| Fare amount (₹32) | [`Fare`](../../schema/Fare/README.md) | `amount: 32`, `currency: INR` | ✅ |
| Fare leg rule | [`FareLegRule`](../../schema/FareLegRule/README.md) | `fareProductId`, `fromAreaId`, `toAreaId` | ✅ |
| BMTC network | [`Network`](../../schema/Network/README.md) | `networkId`, `networkName: BMTC` | ✅ |
| BMTC as operator | [`Operator`](../../schema/Operator/README.md) | `operatorId`, `operatingRegions: Bengaluru` | ✅ |
| Route timetable | [`Timetable`](../../schema/Timetable/README.md) | `routeRef`, `validFrom`, `validUntil` | ✅ |
| Operating days | [`ServiceCalendar`](../../schema/ServiceCalendar/README.md) | `monday–sunday`, `exceptionDates` | ✅ |
| Headway (bus every 10 min) | [`Frequency`](../../schema/Frequency/README.md) | `headwaySecs: 600` | ✅ |
| Transfer rule at KR Market | [`Transfer`](../../schema/Transfer/README.md) | `minTransferTime`, `transferType: 2` | ✅ |
| Cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `cancellationTerms: NON_REFUNDABLE` | ✅ |

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Ravi selects Route 500C direct journey, Adult fare, for 1 passenger. This is the start of the CONTRACT.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Specific bus trip selected | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode` | ✅ |
| Route selected | [`Route`](../../schema/Route/README.md) | `routeId: 500C` | ✅ |
| Fare product selected | [`FareProduct`](../../schema/FareProduct/README.md) | `fareProductId` | ✅ |
| Quantity (1 passenger) | [`PassengerGroup`](../../schema/PassengerGroup/README.md) | `groupSize: 1` | ✅ |
| Boarding stop (Silk Board) | [`Stop`](../../schema/Stop/README.md) | `stopId` | ✅ |
| Alighting stop (Majestic) | [`Stop`](../../schema/Stop/README.md) | `stopId` | ✅ |
| Passenger category | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId: ADULT` | ✅ |

---

#### Action: `on_select`
**Semantic intent:** BPP confirms seat availability on the 500C, confirms the fare, and returns boarding details.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed bus journey | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode`, `stopTimes` | ✅ |
| Route | [`Route`](../../schema/Route/README.md) | `routeId: 500C` | ✅ |
| Confirmed fare | [`Fare`](../../schema/Fare/README.md) | `amount: 32`, `currency: INR` | ✅ |
| Fare breakdown | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base fare + any taxes | ✅ |
| Boarding stop with departure time | [`Stop`](../../schema/Stop/README.md) | `stopId`, `stopName` | ✅ |
| Departure time from Silk Board | [`StopTime`](../../schema/StopTime/README.md) | `departureTime`, `stopSequence` | ✅ |
| Ticket medium (QR code) | [`FareMedium`](../../schema/FareMedium/README.md) | `mediumType: QR_CODE` | ✅ |
| Cancellation policy (non-refundable) | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `cancellationTerms` | ✅ |

---

#### Action: `init`
**Semantic intent:** Ravi submits his passenger details for ticket issuance.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Billing participant | [`Passenger`](../../schema/Passenger/README.md) | `passengerId`, `passengerType: ADULT` | ✅ |
| Passenger category | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId` | ✅ |
| Ticket delivery medium | [`FareMedium`](../../schema/FareMedium/README.md) | `mediumType: QR_CODE` | ✅ |

---

#### Action: `on_init`
**Semantic intent:** BPP returns the final ticket price and pre-payment terms.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Draft journey contract | [`Itinerary`](../../schema/Itinerary/README.md) | Journey details | ✅ |
| Final fare before payment | [`FareBreakup`](../../schema/FareBreakup/README.md) | ₹32 total | ✅ |
| **Pre-payment terms** | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Non-refundable once issued | ✅ |
| Travel entitlement | [`Entitlement`](../../schema/Entitlement/README.md) | Boarding entitlement for Silk Board → Majestic | ✅ |

---

#### Action: `confirm`
**Semantic intent:** Ravi pays ₹32 and confirms the ticket purchase.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Journey order confirmed | [`Itinerary`](../../schema/Itinerary/README.md) | `id` | ✅ |
| Billing passenger | [`Passenger`](../../schema/Passenger/README.md) | `passengerId` | ✅ |
| Payment reference | [`Itinerary`](../../schema/Itinerary/README.md) | `descriptor.tags: PAYMENT_REF` | ⚠️ |

---

#### Action: `on_confirm`
**Semantic intent:** BPP issues the digital bus ticket and returns the confirmed journey contract with invoice link.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed journey contract | [`Itinerary`](../../schema/Itinerary/README.md) | All journey details binding | ✅ |
| Route + bus journey reference | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode` | ✅ |
| Boarding stop | [`Stop`](../../schema/Stop/README.md) | `stopId`, `stopName: Silk Board` | ✅ |
| Fare product purchased | [`FareProduct`](../../schema/FareProduct/README.md) | `fareProductId`, `validFrom`, `validUntil` | ✅ |
| Fare breakdown (binding) | [`FareBreakup`](../../schema/FareBreakup/README.md) | ₹32 binding | ✅ |
| **QR code ticket (as VC)** | [`TravelDocument`](../../schema/TravelDocument/README.md) | `documentType: QR_CODE`, QR token as verifiable credential | ✅ |
| Issued ticket record | [`Ticket`](../../schema/Ticket/README.md) | `ticketId`, `ticketType: SINGLE`, `validFrom`, `validUntil` | ✅ |
| **Print-at-kiosk instructions (if no smartphone)** | [`TravelDocument`](../../schema/TravelDocument/README.md) | `documentType: BARCODE` + counter instructions | ✅ |
| **Invoice link (attached receipt)** | [`Receipt`](../../schema/Receipt/README.md) | `receiptId`, invoice URL | ✅ |

**Notes:** At `on_confirm`, BPP issues the ticket as a **Verifiable Credential (VC)** — `TravelDocument.documentType: QR_CODE` with a signed token. For passengers without smartphones, `TravelDocument` can carry kiosk print instructions. `Receipt` at `on_confirm` represents the pro-forma invoice/booking receipt with the fare breakup.

---

### Stage 3 — Fulfillment

---

#### Action: `status`
**Semantic intent:** Ravi checks how far the bus is from Silk Board.

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Journey state snapshot | [`TripUpdate`](../../schema/TripUpdate/README.md) | `stateUpdate`, `trackingEndpoint` | ✅ |
| Live bus location | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude` | ✅ |
| Predicted arrival delays | [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | `arrivalDelay`, `departureDelay` | ✅ |
| Bus occupancy level | [`OccupancyStatus`](../../schema/OccupancyStatus/README.md) | `occupancyLevel` | ✅ |
| Service alert (if any) | [`Alert`](../../schema/Alert/README.md) | `cause`, `effect`, `activePeriod` | ✅ |

---

#### Action: `track`
**Semantic intent:** Ravi opens the live bus map.

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Live bus GPS + speed | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude`, `speed`, `bearing` | ✅ |
| Real-time monitored journey | [`MonitoredVehicleJourney`](../../schema/MonitoredVehicleJourney/README.md) | `vehicleLocation`, `delay` | ✅ |
| Predicted arrival at Silk Board | [`MonitoredCall`](../../schema/MonitoredCall/README.md) | `expectedArrivalTime`, `arrivalStatus` | ✅ |
| All stops predicted times | [`StopMonitoring`](../../schema/StopMonitoring/README.md) | `monitoredCalls` | ✅ |
| Arrival confidence | [`Prognosis`](../../schema/Prognosis/README.md) | `estimatedTime`, `certainty` | ✅ |

---

#### Action: `update` / `on_update`
**Semantic intent:** Route diversion announced — BPP pushes update. **No contract changes for bus** (ticket remains valid; only route physically changes).

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Diversion alert | [`Alert`](../../schema/Alert/README.md) | `cause: ROAD_CLOSED`, `effect: DETOUR` | ✅ |
| Affected line | [`AffectedLine`](../../schema/AffectedLine/README.md) | `lineRef: 500C`, `cause` | ✅ |

> **Ravi's guidance: bus `on_update` carries NOTHING in terms of contract changes.** The ticket remains valid. Only informational alerts (diversion, delay) are pushed. No `TripUpdate.contractChanges` needed for bus.

---

#### Action: `cancel`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Cancellation | [`Itinerary`](../../schema/Itinerary/README.md) | `id` | ✅ |
| Applied policy (non-refundable) | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `refundPercentage: 0` | ✅ |
| Cancellation receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Service rating | [`Rating`](../../schema/Rating/README.md) | `ratingValue: 3`, `ratedEntityType: SERVICE` | ✅ |
| Feedback tags | [`Feedback`](../../schema/Feedback/README.md) | `feedbackType` | ✅ |

---

#### Action: `support` *(billing complaint — overcharged ₹42 vs correct ₹32)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Billing complaint | [`SupportCase`](../../schema/SupportCase/README.md) | `caseType: COMPLAINT`, `priority: MEDIUM` | ✅ |
| Original ticket receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId` — issued at `on_confirm` | ✅ |
| Operator helpline | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE` | ✅ |

---

## Gap Report

| # | Gap | Description | Severity |
|---|-----|-------------|----------|
| No functional gaps | The bus transit lifecycle is well-covered. `TravelDocument` handles VC/QR ticket issuance. `Receipt` handles invoice links at `on_confirm`. The bus `on_update` correctly carries only alerts (`Alert`, `AffectedLine`) — no contract modifications. | — |

> **Key design distinction:** Bus transit does NOT use GPS-based `Place` for the search intent. It uses `Stop` (station-to-station). This is semantically different from ride hailing and must be implemented distinctly by BAP/BPP.
>
> **Payment reference** is currently expressed via `Itinerary.descriptor.tags` — a payment-specific property on the contract object would be cleaner. This is a minor schema improvement opportunity.
