# Intercity Bus Transport — Lifecycle Stress Test

## Use Case Narrative

Sanjay wants to travel from Bengaluru to Mysuru by KSRTC Volvo bus for 2 adults. He opens the RedBus app and searches "Bengaluru → Mysuru" on a specific date. The app shows multiple KSRTC and private operators with their bus features, departure times, and pickup locations in Bengaluru. He selects the 6 AM KSRTC Volvo Sleeper, picks seats 12A (window) and 12B (aisle) at the Kempegowda Bus Terminal, Bay 7. He submits both passenger details, pays ₹700 (2 × ₹350), and receives QR code tickets with pickup point instructions and an invoice link. On travel day, the bus is 15 minutes late — pushed via BPP as a tracking update with live bus location link. He arrives in Mysuru, rates the service, and raises a support case because seat 12A was occupied.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Sanjay | Consumer — intercity bus traveler | Represented by BAP |
| RedBus App | BAP — search, booking, ticketing | `beckn:BAP` |
| KSRTC Platform | BPP — routes, seat inventory, timetables | `beckn:BPP` |

> **Key differentiators from city bus transit:**
> - Search is CITY-TO-CITY (not stop-to-stop): `Place` carries the city name, not a `Stop`
> - Catalog includes OPERATORS (KSRTC, Orange Travels, etc.) — passengers pick an operator first
> - Catalog includes bus FEATURES, DEPARTURE TIMES, and lists of PICKUP/DROP locations per operator
> - Catalog may include SHUTTLE AVAILABILITY (connecting service at destination)
> - Contract is a `Journey` (not `Itinerary`) — bilateral with seat assignment, baggage terms, multi-passenger identity
> - `on_update` carries a TRACKING ACTIVE FLAG and optional tracking ref (bus GPS URL)

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Sanjay searches buses from Bengaluru city to Mysuru city on a specific date for 2 adults, preferring Volvo Sleeper class.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Top-level intercity trip intent | [`TripSpecification`](../../schema/TripSpecification/README.md) | `origin`, `destination`, `time`, `numTravelers: 2`, `modes: BUS` | ✅ |
| **Origin city** | [`Place`](../../schema/Place/README.md) | `placeName: Bengaluru`, `placeType: CITY` | ✅ |
| **Destination city** | [`Place`](../../schema/Place/README.md) | `placeName: Mysuru`, `placeType: CITY` | ✅ |
| Passenger type | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId: ADULT` | ✅ |
| Number of passengers | [`PassengerGroup`](../../schema/PassengerGroup/README.md) | `groupSize: 2` | ✅ |
| Service class preference | [`ServiceClass`](../../schema/ServiceClass/README.md) | `serviceClassCode: VOLVO_SLEEPER` | ✅ |

**Notes:** Search is CITY-TO-CITY using `Place` with `placeType: CITY`. This is different from city bus (STOP-TO-STOP) and ride hailing (GPS coordinates). The specific pickup/drop stations within each city are NOT known at search time — they are presented in `on_search` per operator and selected in `select`.

---

#### Action: `on_search`
**Semantic intent:** BPP returns operators, their bus features, departure times, pickup locations at Bengaluru, drop locations at Mysuru, and shuttle availability.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Catalog of available buses | [`TripResult`](../../schema/TripResult/README.md) | — | ✅ |
| Each intercity bus journey | [`Journey`](../../schema/Journey/README.md) | `origin: Bengaluru`, `destination: Mysuru`, `departureTime`, `arrivalTime` | ✅ |
| Journey leg | [`Leg`](../../schema/Leg/README.md) | `mode: BUS`, `distance` | ✅ |
| Sub-leg (stops en route) | [`Segment`](../../schema/Segment/README.md) | `trainNumber` (bus number), `segmentNumber` | ✅ |
| KSRTC as operator | [`Operator`](../../schema/Operator/README.md) | `operatorId: KSRTC`, `licenseNumber`, `contactInfo` | ✅ |
| **KSRTC bus features** | [`VehicleType`](../../schema/VehicleType/README.md) | `vehicleTypeCode: BUS`, `maxCapacity`, `propulsionType` | ✅ |
| A/C, WiFi, charging points | [`VehicleType`](../../schema/VehicleType/README.md) | `tags` | ⚠️ |
| **Departure times** | [`StopTime`](../../schema/StopTime/README.md) | `departureTime: 06:00`, `stopRef: KBS_BAY7` | ✅ |
| **Pickup locations at Bengaluru** | [`Stop`](../../schema/Stop/README.md) | `stopId: KBS_BAY7`, `stopName: Kempegowda BS Bay 7` | ✅ |
| **Drop locations at Mysuru** | [`Stop`](../../schema/Stop/README.md) | `stopId: MYSURU_BS`, `stopName: Mysuru Central Bus Stand` | ✅ |
| **Shuttle availability at Mysuru** | [`AncillaryService`](../../schema/AncillaryService/README.md) | `serviceCategory: SHUTTLE`, `serviceCode: CITY_SHUTTLE_MYS` | ✅ |
| Seat availability map | [`Seat`](../../schema/Seat/README.md) | `seatId`, `seatType: WINDOW/AISLE/LOWER_BERTH` | ✅ |
| Volvo Sleeper Adult fare | [`FareProduct`](../../schema/FareProduct/README.md) | `fareProductId`, `riderCategoryId: ADULT`, `durationType: SINGLE_TRIP` | ✅ |
| ₹350 per adult | [`Fare`](../../schema/Fare/README.md) | `amount: 350`, `currency: INR` | ✅ |
| Fare leg rule | [`FareLegRule`](../../schema/FareLegRule/README.md) | `fareProductId`, `containsServiceId` | ✅ |
| Bundle offer (ticket + insurance) | [`SalesOfferPackage`](../../schema/SalesOfferPackage/README.md) | `fareProducts`, `conditionsOfTravel` | ✅ |
| Baggage policy | [`BaggageAllowance`](../../schema/BaggageAllowance/README.md) | `checkedBaggageCount: 1`, `checkedBaggageWeight: 15` | ✅ |
| Advance booking window | [`BookingRule`](../../schema/BookingRule/README.md) | `latestBookingTime: 1 hr before departure` | ✅ |
| Cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | 100% >24h, 50% 4–24h, 0% <4h | ✅ |
| Route | [`Route`](../../schema/Route/README.md) | `routeId`, `routeType: BUS` | ✅ |
| Timetable | [`Timetable`](../../schema/Timetable/README.md) | `routeRef`, `validFrom` | ✅ |
| Service calendar | [`ServiceCalendar`](../../schema/ServiceCalendar/README.md) | `monday–sunday` | ✅ |

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Sanjay selects the 6 AM KSRTC Volvo, picks seats 12A and 12B, and selects **actual pickup station** (Bay 7, Kempegowda BS) and **actual drop station** (Mysuru Central BS). This starts the CONTRACT.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Selected KSRTC 6 AM trip | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode` | ✅ |
| Operator selected | [`Operator`](../../schema/Operator/README.md) | `operatorId: KSRTC` | ✅ |
| Seat request — Passenger 1 (12A window) | [`PlaceRequest`](../../schema/PlaceRequest/README.md) | `accommodationType: SEAT`, `preferences: WINDOW`, `seatRef: 12A` | ✅ |
| Seat request — Passenger 2 (12B aisle) | [`PlaceRequest`](../../schema/PlaceRequest/README.md) | `accommodationType: SEAT`, `preferences: AISLE`, `seatRef: 12B` | ✅ |
| Specific seats | [`Seat`](../../schema/Seat/README.md) | `seatId: 12A`, `seatId: 12B` | ✅ |
| Fare product | [`FareProduct`](../../schema/FareProduct/README.md) | `fareProductId` | ✅ |
| Quantity (2 adults) | [`PassengerGroup`](../../schema/PassengerGroup/README.md) | `groupSize: 2` | ✅ |
| **Actual pickup station at Bengaluru** | [`Stop`](../../schema/Stop/README.md) | `stopId: KBS_BAY7`, `stopName: Kempegowda BS Bay 7` | ✅ |
| **Actual drop station at Mysuru** | [`Stop`](../../schema/Stop/README.md) | `stopId: MYSURU_BS`, `stopName: Mysuru Central BS` | ✅ |
| Passenger categories | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId: ADULT` (×2) | ✅ |

**Notes:** The `select` action is when the passenger commits to a specific operator, specific departure, and SPECIFIC pickup/drop stations. These may differ from what was shown at city level in `on_search` (e.g., passenger could choose a different pickup point in the same city).

---

#### Action: `on_select`
**Semantic intent:** KSRTC confirms seats 12A and 12B are available (locked for 10 minutes), returns ₹700 total fare.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed KSRTC 6 AM trip | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode`, `stopTimes` | ✅ |
| Operator | [`Operator`](../../schema/Operator/README.md) | `operatorId: KSRTC` | ✅ |
| **Confirmed seats 12A + 12B (held 10 min)** | [`Seat`](../../schema/Seat/README.md) | `seatId`, `row`, `column`, `seatType` | ✅ |
| ₹700 total fare (2 × ₹350) | [`Fare`](../../schema/Fare/README.md) | `amount: 700`, `currency: INR` | ✅ |
| Fare breakdown | [`FareBreakup`](../../schema/FareBreakup/README.md) | 2× base + taxes | ✅ |
| Baggage allowance (binding) | [`BaggageAllowance`](../../schema/BaggageAllowance/README.md) | `checkedBaggageWeight: 15 kg per passenger` | ✅ |
| Boarding point | [`Stop`](../../schema/Stop/README.md) | `stopId: KBS_BAY7`, boarding opens 5:45 AM | ✅ |
| Departure time | [`StopTime`](../../schema/StopTime/README.md) | `departureTime: 06:00` | ✅ |
| Cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Refund schedule | ✅ |
| Booking window closes | [`BookingRule`](../../schema/BookingRule/README.md) | `latestBookingTime: 05:00` | ✅ |
| Service class | [`ServiceClass`](../../schema/ServiceClass/README.md) | `serviceClassCode: VOLVO_SLEEPER` | ✅ |

---

#### Action: `init`
**Semantic intent:** Sanjay submits both passenger details (billing + travel).

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| **Billing participant** (Sanjay) | [`Passenger`](../../schema/Passenger/README.md) | `passengerId`, `name`, `telephone` (billing contact) | ✅ |
| **Travel participant** (co-traveler) | [`Passenger`](../../schema/Passenger/README.md) | `passengerId`, `name` (for ticket issuance) | ✅ |
| Passenger group | [`PassengerGroup`](../../schema/PassengerGroup/README.md) | `groupSize: 2`, `leadPassenger` | ✅ |
| Passenger categories | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId: ADULT` (×2) | ✅ |

---

#### Action: `on_init`
**Semantic intent:** KSRTC returns the full journey contract terms including pre-payment details.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Draft journey contract | [`Journey`](../../schema/Journey/README.md) | `origin`, `destination`, `departureTime`, `arrivalTime` | ✅ |
| Reserved seats | [`Seat`](../../schema/Seat/README.md) | `seatId: 12A`, `seatId: 12B` | ✅ |
| Total ₹700 fare | [`FareBreakup`](../../schema/FareBreakup/README.md) | 2× base + taxes | ✅ |
| Baggage allowance (binding) | [`BaggageAllowance`](../../schema/BaggageAllowance/README.md) | Per passenger | ✅ |
| Cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Binding refund schedule | ✅ |
| **Pre-payment terms** | [`Journey`](../../schema/Journey/README.md) | `descriptor.tags: PAYMENT_METHOD=PREPAID` | ⚠️ |
| Travel entitlements | [`Entitlement`](../../schema/Entitlement/README.md) | Per-passenger boarding entitlements | ✅ |

---

#### Action: `confirm`
**Semantic intent:** Sanjay pays ₹700 and confirms the booking for both passengers.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed journey order | [`Journey`](../../schema/Journey/README.md) | `id` | ✅ |
| Both passengers confirming | [`Passenger`](../../schema/Passenger/README.md) | `passengerId` (×2) | ✅ |
| Payment reference | [`Journey`](../../schema/Journey/README.md) | `descriptor.tags: PAYMENT_REF` | ⚠️ |

---

#### Action: `on_confirm`
**Semantic intent:** KSRTC confirms the booking, issues QR tickets for both passengers, and returns pickup instructions and invoice link.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed intercity journey contract | [`Journey`](../../schema/Journey/README.md) | `origin`, `destination`, `departureTime`, `arrivalTime` | ✅ |
| Bus trip reference | [`VehicleJourney`](../../schema/VehicleJourney/README.md) | `vehicleJourneyCode` | ✅ |
| Operator | [`Operator`](../../schema/Operator/README.md) | `operatorId: KSRTC`, `contactInfo` | ✅ |
| Reserved seats (binding) | [`Seat`](../../schema/Seat/README.md) | `seatId: 12A`, `seatId: 12B`, `deckLevel` | ✅ |
| Both passengers | [`Passenger`](../../schema/Passenger/README.md) | `passengerId`, `name` | ✅ |
| **QR ticket for Passenger 1 (seat 12A)** | [`TravelDocument`](../../schema/TravelDocument/README.md) | `documentType: QR_CODE`, VC for Sanjay | ✅ |
| **QR ticket for Passenger 2 (seat 12B)** | [`TravelDocument`](../../schema/TravelDocument/README.md) | `documentType: QR_CODE`, VC for co-traveler | ✅ |
| Issued ticket records | [`Ticket`](../../schema/Ticket/README.md) | `ticketId` (×2), `validFrom`, `validUntil`, `passengerRef` | ✅ |
| Fare breakdown (binding) | [`FareBreakup`](../../schema/FareBreakup/README.md) | 2× ₹350 + taxes | ✅ |
| Baggage allowance | [`BaggageAllowance`](../../schema/BaggageAllowance/README.md) | 1 bag / 15 kg per passenger | ✅ |
| **Pickup point instructions** | [`FulfillmentStop`](../../schema/FulfillmentStop/README.md) | `stopRef: KBS_BAY7`, `instructions: Report to Bay 7 by 5:45 AM` | ✅ |
| **Invoice link** | [`Receipt`](../../schema/Receipt/README.md) | `receiptId`, invoice URL | ✅ |
| Operator helpline | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE`, KSRTC helpline | ✅ |

**Notes:** `FulfillmentStop` carries the pickup instructions — the specific bay number, boarding opening time, and any special instructions (e.g., "show QR code to conductor"). `Receipt` at `on_confirm` is the pro-forma invoice/booking receipt with full fare breakup.

---

### Stage 3 — Fulfillment

---

#### Action: `status`
**Semantic intent:** Sanjay checks bus status on travel morning — is it on time?

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Journey state snapshot | [`TripUpdate`](../../schema/TripUpdate/README.md) | `stateUpdate` | ✅ |
| Bus current location | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude` | ✅ |
| Revised departure time | [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | `departureDelay: 900` (15 min late) | ✅ |
| Delay alert | [`Alert`](../../schema/Alert/README.md) | `cause: TECHNICAL_PROBLEM`, `effect: MODIFIED_SERVICE` | ✅ |
| Lifecycle event | [`Event`](../../schema/Event/README.md) | `eventType: SERVICE_DELAYED` | ✅ |

---

#### Action: `track`
**Semantic intent:** Sanjay tracks the bus location en route to Mysuru.

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Live bus location + speed | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude`, `speed`, `bearing` | ✅ |
| Odometer / distance covered | [`Telemetry`](../../schema/Telemetry/README.md) | `odometer`, `speed` | ✅ |
| Revised arrival ETA at Mysuru | [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | Revised Mysuru arrival time | ✅ |

---

#### Action: `on_update` *(BPP-initiated push — tracking activated after departure)*
**Semantic intent:** After the bus departs Bay 7, BPP pushes full updated contract with tracking active flag and live tracking URL.

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Full updated journey contract | [`Journey`](../../schema/Journey/README.md) | All original elements, `state: IN_PROGRESS` | ✅ |
| Seat assignments | [`Seat`](../../schema/Seat/README.md) | `seatId: 12A`, `seatId: 12B` | ✅ |
| Both passenger references | [`Passenger`](../../schema/Passenger/README.md) | `passengerId` (×2) | ✅ |
| Pickup instructions | [`FulfillmentStop`](../../schema/FulfillmentStop/README.md) | `instructions` | ✅ |
| Tickets | [`TravelDocument`](../../schema/TravelDocument/README.md) | VC tokens (unchanged) | ✅ |
| **Tracking ACTIVE** | [`TripUpdate`](../../schema/TripUpdate/README.md) | `trackingEndpoint.status: ACTIVE` | ✅ |
| **Tracking ref / bus GPS URL** *(optional)* | [`TripUpdate`](../../schema/TripUpdate/README.md) | `trackingEndpoint.url` (live bus GPS stream) | ✅ |
| Journey progress event | [`Event`](../../schema/Event/README.md) | `eventType: JOURNEY_STARTED` | ✅ |

> **Ravi's guidance:** Intercity bus `on_update` carries the **tracking active flag** and optionally a **tracking ref** (URL to the bus's live GPS stream). This differs from metro and city bus which carry nothing in `on_update`. The tracking URL enables the BAP to show a live map of the bus's journey from Bengaluru to Mysuru.

---

#### Action: `cancel`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Journey cancellation (2 hrs before) | [`Journey`](../../schema/Journey/README.md) | `id` | ✅ |
| Applied policy (50% refund) | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `refundPercentage: 50` | ✅ |
| Tickets invalidated | [`Ticket`](../../schema/Ticket/README.md) | `ticketId` (×2), status: CANCELLED | ✅ |
| Cancellation receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId`, ₹350 refund | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Service rating (3 stars — seat issue) | [`Rating`](../../schema/Rating/README.md) | `ratingValue: 3`, `ratedEntityType: SERVICE` | ✅ |
| Vehicle cleanliness rating | [`Rating`](../../schema/Rating/README.md) | `ratingValue: 4`, `ratedEntityType: VEHICLE` | ✅ |
| Review text | [`Review`](../../schema/Review/README.md) | `reviewText: "Seat 12A was occupied"` | ✅ |
| Feedback tags | [`Feedback`](../../schema/Feedback/README.md) | `feedbackType: SEAT_ISSUE, DELAY` | ✅ |

---

#### Action: `support` *(seat occupied — dispute)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Seat dispute complaint (HIGH priority) | [`SupportCase`](../../schema/SupportCase/README.md) | `caseType: COMPLAINT`, `priority: HIGH` | ✅ |
| Original journey receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId` | ✅ |
| Travel voucher as resolution | [`Entitlement`](../../schema/Entitlement/README.md) | `entitlementType: TRAVEL_VOUCHER` | ✅ |
| KSRTC grievance contact | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE` | ✅ |

---

## Gap Report

| # | Gap | Description | Severity |
|---|-----|-------------|----------|
| 1 | **VehicleFeature** | Bus amenity features (A/C, WiFi, charging points, reclining seats) are not structured properties of `VehicleType`. Currently expressible only via `tags`. The intercity bus catalog is heavily feature-driven — passengers compare operators on these amenities. | Medium |
| No other gaps | `TripSpecification` correctly handles city-level origin/destination. `Journey` correctly handles intercity contracts with bilateral obligations. `Segment` handles sub-legs. `PlaceRequest` + `Seat` handle seat selection. `BaggageAllowance` handles luggage constraints. `FulfillmentStop` handles pickup point instructions. `TravelDocument` handles VC tickets for multiple passengers. `TripUpdate.trackingEndpoint` handles the tracking active flag and GPS URL at `on_update`. | — |

> **Key semantic distinctions for intercity bus:**
> 1. Search is CITY-TO-CITY (`Place` with `placeType: CITY`), not stop-to-stop or GPS
> 2. Catalog presents OPERATORS first — passenger evaluates KSRTC vs private operator
> 3. Specific pickup/drop STATIONS within the city are shown per operator and confirmed at `select`
> 4. Contract type is `Journey` (not `Itinerary`) — reflects the richer intercity booking model with bilateral identity verification and seat assignment
> 5. `on_update` carries tracking active flag + optional GPS URL — unlike bus and metro which carry nothing in `on_update`
