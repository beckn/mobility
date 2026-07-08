# Public Transit (Metro) — Lifecycle Stress Test

## Use Case Narrative

Kavya needs to travel from MG Road metro station to Whitefield on Kochi Metro's Purple Line. She opens the Kochi Metro app, selects MG Road station as origin and Whitefield as destination. The app shows her a ₹45 Adult single-trip fare. She pays via UPI and receives a QR code ticket. At MG Road she taps the QR on the fare gate, takes the escalator to Platform 2. The app shows a real-time departure board (metro live updates link). She boards, travels, and exits at Whitefield. Post-journey she rates the service and raises a fare gate complaint.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Kavya | Consumer — metro commuter | Represented by BAP |
| Metro App | BAP — ticket purchase and journey info | `beckn:BAP` |
| Kochi Metro Platform | BPP — ticketing, timetables, real-time | `beckn:BPP` |

> **Key differentiators from bus:** Metro uses `StopPlace` (complex multi-level facility) rather than `Stop`. Additional station infrastructure classes (`Quay`, `Level`, `Pathway`) are returned at `on_confirm` for in-station wayfinding. **`on_confirm` includes a metro live updates link** — a URL to the real-time departure board. **`on_update` carries NOTHING** (same as bus).

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Kavya selects her origin station and destination station. Search is STATION-TO-STATION, not GPS.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Top-level metro intent | [`TripRequest`](../../schema/TripRequest/README.md) | `origin`, `destination`, `departureTime`, `modes: METRO` | ✅ |
| **Origin metro station** | [`StopPlace`](../../schema/StopPlace/README.md) | `stopPlaceId`, `stopPlaceType: METRO_STATION` | ✅ |
| **Destination metro station** | [`StopPlace`](../../schema/StopPlace/README.md) | `stopPlaceId`, `stopPlaceType: METRO_STATION` | ✅ |
| Passenger category | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId: ADULT` | ✅ |
| Number of passengers | [`PassengerGroup`](../../schema/PassengerGroup/README.md) | `groupSize: 1` | ✅ |

**Notes:** Metro uses `StopPlace` (not `Stop`) because metro stations are complex multi-level facilities. `StopPlace` contains `quays` (platforms), `entrances` (fare gate pathways), and accessibility information — all of which are unavailable at the simpler `Stop` level.

---

#### Action: `on_search`
**Semantic intent:** Kochi Metro returns Purple Line trips, fare products, and zone-based pricing.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Catalog of metro journey options | [`TripResult`](../../schema/TripResult/README.md) | — | ✅ |
| Metro journey | [`Itinerary`](../../schema/Itinerary/README.md) | `legs`, `totalDuration`, `departureTime` | ✅ |
| Metro leg | [`Leg`](../../schema/Leg/README.md) | `mode: METRO`, `origin`, `destination` | ✅ |
| Purple Line route | [`Route`](../../schema/Route/README.md) | `routeId`, `routeType: SUBWAY` | ✅ |
| Purple Line service | [`Line`](../../schema/Line/README.md) | `lineId`, `longName: Purple Line` | ✅ |
| Specific train departure | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode`, `stopTimes` | ✅ |
| Departure time from MG Road | [`StopTime`](../../schema/StopTime/README.md) | `departureTime`, `stopSequence` | ✅ |
| **Adult single-trip fare product** | [`FareProduct`](../../schema/FareProduct/README.md) | `fareProductId`, `durationType: SINGLE_TRIP` | ✅ |
| ₹45 fare | [`Fare`](../../schema/Fare/README.md) | `amount: 45`, `currency: INR` | ✅ |
| **Fare zone computation** | [`TariffZone`](../../schema/TariffZone/README.md) | `zoneId`, `zoneName` (origin + destination zones) | ✅ |
| Fare leg rule (zone-based) | [`FareLegRule`](../../schema/FareLegRule/README.md) | `fromAreaId`, `toAreaId`, `fareProductId` | ✅ |
| Transfer discount (if multi-line) | [`FareTransferRule`](../../schema/FareTransferRule/README.md) | `fareProductId`, `durationLimit` | ✅ |
| Kochi Metro network | [`Network`](../../schema/Network/README.md) | `networkId` | ✅ |
| Kochi Metro operator | [`Operator`](../../schema/Operator/README.md) | `operatorId` | ✅ |
| Metro timetable | [`Timetable`](../../schema/Timetable/README.md) | `routeRef`, `validFrom` | ✅ |
| Operating calendar | [`ServiceCalendar`](../../schema/ServiceCalendar/README.md) | `monday–sunday` | ✅ |
| Cancellation policy | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `cancellationTerms: NON_REFUNDABLE_ONCE_SCANNED` | ✅ |

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Kavya selects a specific train, Adult single-trip QR ticket. This starts the CONTRACT.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Specific train trip | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode` | ✅ |
| Fare product | [`FareProduct`](../../schema/FareProduct/README.md) | `fareProductId` | ✅ |
| Ticket medium (QR code) | [`FareMedium`](../../schema/FareMedium/README.md) | `mediumType: QR_CODE` | ✅ |
| Quantity | [`PassengerGroup`](../../schema/PassengerGroup/README.md) | `groupSize: 1` | ✅ |
| Boarding station | [`StopPlace`](../../schema/StopPlace/README.md) | `stopPlaceId: MG_ROAD` | ✅ |
| Alighting station | [`StopPlace`](../../schema/StopPlace/README.md) | `stopPlaceId: WHITEFIELD` | ✅ |
| Passenger category | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId: ADULT` | ✅ |

---

#### Action: `on_select`
**Semantic intent:** BPP confirms train availability and returns locked ₹45 fare with boarding platform details.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed metro trip | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode`, `stopTimes` | ✅ |
| Confirmed ₹45 fare | [`Fare`](../../schema/Fare/README.md) | `amount: 45`, `currency: INR` | ✅ |
| Fare breakdown | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base fare + taxes | ✅ |
| **Boarding platform at MG Road** | [`Quay`](../../schema/Quay/README.md) | `quayId`, `publicCode: Platform 2` | ✅ |
| Departure time from Platform 2 | [`StopTime`](../../schema/StopTime/README.md) | `departureTime` | ✅ |
| Fare gate entry zone | [`StopArea`](../../schema/StopArea/README.md) | `areaId`, `areaName: MG_ROAD_FARE_GATE` | ✅ |
| Confirmed QR medium | [`FareMedium`](../../schema/FareMedium/README.md) | `mediumType: QR_CODE` | ✅ |
| Cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `cancellationTerms` | ✅ |

---

#### Action: `init`
**Semantic intent:** Kavya submits her identity for ticket issuance.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Billing passenger | [`Passenger`](../../schema/Passenger/README.md) | `passengerId`, `passengerType: ADULT` | ✅ |
| Passenger category | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId` | ✅ |
| Delivery medium | [`FareMedium`](../../schema/FareMedium/README.md) | `mediumType: QR_CODE` | ✅ |

---

#### Action: `on_init`
**Semantic intent:** BPP returns final ₹45 fare and pre-payment terms.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Draft metro journey contract | [`Itinerary`](../../schema/Itinerary/README.md) | `legs`, `departureTime` | ✅ |
| Final ₹45 fare | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base fare total | ✅ |
| **Pre-payment terms** | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Non-refundable once scanned | ✅ |
| Travel entitlement | [`Entitlement`](../../schema/Entitlement/README.md) | MG Road → Whitefield single-trip | ✅ |

> **Pass scenario:** If Kavya already has a metro pass, `on_init` and beyond may contain no fare — only entitlement validation. `FareProduct` with `durationType: MONTHLY` would already be active in her account; `select` would carry only the pass reference.

---

#### Action: `confirm`
**Semantic intent:** Kavya pays ₹45 via UPI and confirms.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Journey order confirmed | [`Itinerary`](../../schema/Itinerary/README.md) | `id` | ✅ |
| Billing passenger | [`Passenger`](../../schema/Passenger/README.md) | `passengerId` | ✅ |
| Payment reference | [`Itinerary`](../../schema/Itinerary/README.md) | `descriptor.tags: PAYMENT_REF` | ⚠️ |

---

#### Action: `on_confirm`
**Semantic intent:** BPP issues QR ticket, returns complete journey contract with **metro live updates link** — a URL to the real-time departure board for the Purple Line.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed metro journey contract | [`Itinerary`](../../schema/Itinerary/README.md) | All journey details binding | ✅ |
| Train trip reference | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode` | ✅ |
| Fare product purchased | [`FareProduct`](../../schema/FareProduct/README.md) | `fareProductId`, `validFrom`, `validUntil` | ✅ |
| Fare breakdown (binding) | [`FareBreakup`](../../schema/FareBreakup/README.md) | ₹45 binding | ✅ |
| **QR code ticket (VC)** | [`TravelDocument`](../../schema/TravelDocument/README.md) | `documentType: QR_CODE`, signed VC token | ✅ |
| Issued ticket record | [`Ticket`](../../schema/Ticket/README.md) | `ticketId`, `ticketType: SINGLE`, `validFrom`, `validUntil` | ✅ |
| **Kiosk print instructions** | [`TravelDocument`](../../schema/TravelDocument/README.md) | `documentType: BARCODE` + kiosk location | ✅ |
| **Invoice link** | [`Receipt`](../../schema/Receipt/README.md) | `receiptId`, invoice URL | ✅ |
| **Boarding platform** | [`Quay`](../../schema/Quay/README.md) | `quayId: Platform 2`, `publicCode` | ✅ |
| **Floor/level to reach platform** | [`Level`](../../schema/Level/README.md) | `levelName: Platform Level`, `elevation` | ✅ |
| **Escalator route to platform** | [`Pathway`](../../schema/Pathway/README.md) | `pathwayMode: 4 (ESCALATOR)`, `traversalTime` | ✅ |
| **Metro live updates link** | [`TripUpdate`](../../schema/TripUpdate/README.md) | `trackingEndpoint.url` (real-time departure board) | ✅ |

**Notes on metro live updates link:** At `on_confirm`, the BPP includes the `trackingEndpoint.url` — a URL to the Purple Line's live departure board (e.g., `https://kochimetro.org/live?line=purple&station=mg_road`). This is distinct from the polling `track` action. It is the link the passenger clicks to see the real-time arrival board in-app. `TripUpdate.trackingEndpoint` (from `beckn:Tracking`) carries this URL.

---

### Stage 3 — Fulfillment

---

#### Action: `status`
**Semantic intent:** Kavya checks next Purple Line train ETA at Platform 2.

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Journey state snapshot | [`TripUpdate`](../../schema/TripUpdate/README.md) | `stateUpdate`, `trackingEndpoint` | ✅ |
| Train live position | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude` | ✅ |
| Predicted arrival delay | [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | `arrivalDelay`, `departureDelay` | ✅ |
| Estimated timetable | [`EstimatedTimetableDelivery`](../../schema/EstimatedTimetableDelivery/README.md) | `estimatedVehicleJourneys`, `validUntil` | ✅ |
| Train car occupancy | [`OccupancyStatus`](../../schema/OccupancyStatus/README.md) | `occupancyLevel: MANY_SEATS_AVAILABLE` | ✅ |
| Signal fault alert | [`Alert`](../../schema/Alert/README.md) | `cause: TECHNICAL_PROBLEM`, `effect: REDUCED_SERVICE` | ✅ |

---

#### Action: `track`
**Semantic intent:** Kavya taps the live updates link from `on_confirm` or polls directly.

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Train live GPS | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude`, `speed` | ✅ |
| Monitored Purple Line journey | [`MonitoredVehicleJourney`](../../schema/MonitoredVehicleJourney/README.md) | `vehicleLocation`, `delay`, `occupancy` | ✅ |
| Predicted arrival at Platform 2 | [`MonitoredCall`](../../schema/MonitoredCall/README.md) | `expectedArrivalTime`, `aimedArrivalTime` | ✅ |
| All upcoming services at MG Road | [`StopMonitoring`](../../schema/StopMonitoring/README.md) | `monitoredCalls`, `stopRef` | ✅ |
| SIRI service delivery envelope | [`ServiceDelivery`](../../schema/ServiceDelivery/README.md) | `stopMonitoring`, `vehicleMonitoring` | ✅ |

---

#### Action: `update` / `on_update`
**Semantic intent:** Signal fault — 8-minute delay pushed to all passengers. **No contract changes for metro.**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Delay alert | [`Alert`](../../schema/Alert/README.md) | `cause: TECHNICAL_PROBLEM`, `effect: SIGNIFICANT_DELAYS` | ✅ |
| Affected entities | [`EntitySelector`](../../schema/EntitySelector/README.md) | `routeId: PURPLE`, `stopId: MG_ROAD` | ✅ |
| Passenger information text | [`GeneralMessageDelivery`](../../schema/GeneralMessageDelivery/README.md) | `infoMessages`, `channel: APP` | ✅ |
| Revised stop time predictions | [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | `arrivalDelay: 480` (8 minutes) | ✅ |

> **Ravi's guidance: metro `on_update` carries NOTHING in terms of contract changes.** Only informational alerts and revised arrival times are pushed. No `TripUpdate.contractChanges` needed.

---

#### Action: `cancel`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Journey cancellation | [`Itinerary`](../../schema/Itinerary/README.md) | `id` | ✅ |
| Applied policy | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Full refund if delay-caused | ✅ |
| QR ticket invalidated | [`Ticket`](../../schema/Ticket/README.md) | `ticketId`, status: CANCELLED | ✅ |
| Cancellation receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Service rating | [`Rating`](../../schema/Rating/README.md) | `ratingValue: 4`, `ratedEntityType: SERVICE` | ✅ |
| Review text | [`Review`](../../schema/Review/README.md) | `reviewText` | ✅ |
| Feedback tags | [`Feedback`](../../schema/Feedback/README.md) | `feedbackType` | ✅ |

---

#### Action: `support` *(fare gate scan failure — double-charged)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Fare dispute complaint | [`SupportCase`](../../schema/SupportCase/README.md) | `caseType: COMPLAINT` | ✅ |
| Original ticket receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId` | ✅ |
| Metro helpdesk contact | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE` | ✅ |

---

## Gap Report

| # | Gap | Description | Severity |
|---|-----|-------------|----------|
| No functional gaps | The metro lifecycle is fully covered. `StopPlace` + `Quay` + `Level` + `Pathway` handle NeTEx station model. `TariffZone` + `FareLegRule` + `FareTransferRule` handle GTFS Fares v2 zone pricing. `TravelDocument` (VC/QR) handles smart ticketing. `TripUpdate.trackingEndpoint` carries the metro live updates link at `on_confirm`. SIRI real-time stack (`ServiceDelivery`, `MonitoredVehicleJourney`, `EstimatedTimetableDelivery`) handles fulfillment. | — |

> **Pass scenario:** When Kavya has a monthly pass (`FareProduct.durationType: MONTHLY`), the `select` and `on_select` messages carry only the pass reference — no fare calculation needed. `init` / `on_init` may return zero fare. `on_confirm` returns a journey authorization rather than a ticket. This variant is handled by the existing `FareProduct` and `Entitlement` classes.
