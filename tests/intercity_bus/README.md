# Intercity Bus Transport — Lifecycle Stress Test

## Use Case Narrative

Sanjay is traveling from Bengaluru to Mysuru by an intercity Volvo bus operated by KSRTC. He opens the RedBus app, searches for buses on his preferred date, selects a Volvo A/C Sleeper with a window seat, and pays for two adults. Tickets are issued as QR codes. On the day of travel, he checks the app for bus status (delayed by 15 minutes). He boards at Kempegowda Bus Terminal (Majestic) and arrives at Mysuru Bus Stand. Post-trip, he rates the service and raises a support case because his reserved seat was occupied and he had to sit elsewhere.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Sanjay | Consumer — intercity bus traveler | Represented by BAP |
| RedBus App | BAP — search, booking, ticketing | `beckn:BAP` |
| KSRTC Platform | BPP — manages routes, timetables, seat inventory, pricing | `beckn:BPP` |
| Bus Driver | Fulfillment agent | `mobility:Driver` |

---

## Key Differentiators vs City Bus Transit

Intercity bus stress testing introduces several additional schema classes:

| Additional Class | Why Intercity-Specific |
|-----------------|----------------------|
| `TripSpecification` | Multi-passenger booking with specific class/seat preferences |
| `Journey` | Intercity bookings are full Journey contracts (not just legs) |
| `Segment` | Sub-portions of the intercity leg if bus stops at multiple towns |
| `Seat` | Specific seat assignment (window/aisle, upper/lower berth) |
| `PlaceRequest` | Passenger's seat/berth preference during booking |
| `BaggageAllowance` | Baggage policy for intercity (luggage compartment limit) |
| `SalesOfferPackage` | Bundled offers (bus + seat + travel insurance) |
| `BookingRule` | Advance booking requirements (min 1 hour before departure) |
| `ServiceClass` | Class of service (Ordinary, Express, Volvo, Volvo Sleeper) |

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Sanjay searches for available buses from Bengaluru to Mysuru on a specific date, for 2 adult passengers.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripSpecification`](../../schema/TripSpecification/README.md) | Top-level intercity trip specification — origin, destination, date, preferences | `beckn:Intent` | ✅ |
| [`Place`](../../schema/Place/README.md) | Origin: Bengaluru (city or specific bus terminal) | `beckn:Location` | ✅ |
| [`Place`](../../schema/Place/README.md) | Destination: Mysuru (city or bus stand) | `beckn:Location` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult passenger category (2 adults) | `beckn:CategoryCode` | ✅ |
| [`PassengerGroup`](../../schema/PassengerGroup/README.md) | 2 adult passengers traveling together | `beckn:Quantity` | ✅ |
| [`ServiceClass`](../../schema/ServiceClass/README.md) | Preference for Volvo A/C Sleeper class | `beckn:CategoryCode` | ✅ |

**Notes:** `TripSpecification` extends `beckn:Intent` and is used (vs `TripRequest`) when passengers have a specific multi-traveler booking with class preferences. `TripSpecification.numTravelers` = 2, `TripSpecification.modes` = BUS. `ServiceClass` preference filters results to Volvo Sleeper options.

---

#### Action: `on_search`
**Semantic intent:** KSRTC returns available bus services for the Bengaluru → Mysuru route on that date, with seat maps, fares, and policies.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripResult`](../../schema/TripResult/README.md) | Catalog of available bus options | `beckn:Catalog` | ✅ |
| [`Journey`](../../schema/Journey/README.md) | Each available intercity bus journey option | `beckn:Contract` | ✅ |
| [`Leg`](../../schema/Leg/README.md) | Primary Bengaluru → Mysuru leg | `beckn:Fulfillment` | ✅ |
| [`Segment`](../../schema/Segment/README.md) | Sub-leg if bus stops at Ramanagara/Mandya en route | `beckn:Fulfillment` | ✅ |
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | Specific bus service instance (departure time, bus number) | `beckn:Fulfillment` | ✅ |
| [`Route`](../../schema/Route/README.md) | KSRTC Bengaluru–Mysuru route | `beckn:Item` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Kempegowda Bus Terminal (boarding) | `beckn:FulfillmentStop` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Mysuru Bus Stand (alighting) | `beckn:FulfillmentStop` | ✅ |
| [`StopTime`](../../schema/StopTime/README.md) | Departure (6:00 AM) and arrival (9:30 AM) schedule | `beckn:TimePeriod` | ✅ |
| [`ServiceClass`](../../schema/ServiceClass/README.md) | Volvo A/C Sleeper service class | `beckn:CategoryCode` | ✅ |
| [`Vehicle`](../../schema/Vehicle/README.md) | Volvo bus details (model, capacity, A/C) | `beckn:Item` | ✅ |
| [`VehicleType`](../../schema/VehicleType/README.md) | Bus vehicle type (BUS, capacity, wheelchair accessible) | `beckn:CategoryCode` | ✅ |
| [`Seat`](../../schema/Seat/README.md) | Available window and aisle seats (seat map) | `beckn:Entitlement` | ✅ |
| [`FareProduct`](../../schema/FareProduct/README.md) | Volvo Sleeper Adult fare product | `beckn:Offer` | ✅ |
| [`Fare`](../../schema/Fare/README.md) | ₹350 per adult fare for Volvo Sleeper | `beckn:Offer` | ✅ |
| [`FareLegRule`](../../schema/FareLegRule/README.md) | Fare rule for Bengaluru → Mysuru on Volvo Sleeper | `beckn:Policy` | ✅ |
| [`SalesOfferPackage`](../../schema/SalesOfferPackage/README.md) | Bundle: bus seat + travel insurance option | `beckn:Offer` | ✅ |
| [`BaggageAllowance`](../../schema/BaggageAllowance/README.md) | Luggage policy (1 bag per passenger, max 15 kg) | `beckn:Constraint` | ✅ |
| [`BookingRule`](../../schema/BookingRule/README.md) | Must book at least 1 hour before departure | `beckn:Policy` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Cancellation refund schedule | `beckn:CancellationPolicy` | ✅ |
| [`Operator`](../../schema/Operator/README.md) | KSRTC as the intercity bus operator | `beckn:Provider` | ✅ |
| [`Timetable`](../../schema/Timetable/README.md) | Full day timetable for Bengaluru–Mysuru route | `beckn:Catalog` | ✅ |
| [`ServiceCalendar`](../../schema/ServiceCalendar/README.md) | Operating days for this service | `beckn:TimePeriod` | ✅ |

**Notes:** `Seat` appears in the `on_search` response as a seat map — showing available seats numbered 1–40 with their type (WINDOW, AISLE, LOWER_BERTH, UPPER_BERTH). `SalesOfferPackage` bundles the base ticket with optional travel insurance as a single purchasable offer. `BaggageAllowance` is a `beckn:Constraint` specifying `checkedBaggageCount: 1` and `checkedBaggageWeight: 15`.

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Sanjay selects the 6:00 AM Volvo Sleeper and chooses seats 12A (window) and 12B (aisle) for 2 passengers.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | Selected 6:00 AM Volvo Sleeper service | `beckn:Fulfillment` | ✅ |
| [`PlaceRequest`](../../schema/PlaceRequest/README.md) | Seat request — 12A (window) for Passenger 1 | `beckn:ContractItem` | ✅ |
| [`PlaceRequest`](../../schema/PlaceRequest/README.md) | Seat request — 12B (aisle) for Passenger 2 | `beckn:ContractItem` | ✅ |
| [`Seat`](../../schema/Seat/README.md) | Specific seats 12A and 12B | `beckn:Entitlement` | ✅ |
| [`FareProduct`](../../schema/FareProduct/README.md) | Volvo Sleeper Adult fare product | `beckn:Offer` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult (both passengers) | `beckn:CategoryCode` | ✅ |

---

#### Action: `on_select`
**Semantic intent:** KSRTC confirms seats 12A and 12B are available, locks the fare, and returns boarding details.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | Confirmed 6:00 AM service with full schedule | `beckn:Fulfillment` | ✅ |
| [`Seat`](../../schema/Seat/README.md) | Confirmed seats 12A and 12B (locked for 10 minutes) | `beckn:Entitlement` | ✅ |
| [`Fare`](../../schema/Fare/README.md) | ₹700 total fare (2 × ₹350) | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | 2 × base fare + taxes | `beckn:PriceComponent` | ✅ |
| [`BaggageAllowance`](../../schema/BaggageAllowance/README.md) | 1 bag / 15 kg per passenger — binding | `beckn:Constraint` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Boarding point: Bay 7, Kempegowda Bus Terminal | `beckn:FulfillmentStop` | ✅ |
| [`StopTime`](../../schema/StopTime/README.md) | Boarding opens at 5:45 AM, departs 6:00 AM | `beckn:TimePeriod` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Refund schedule: 100% >24h, 50% 4-24h, 0% <4h | `beckn:CancellationPolicy` | ✅ |
| [`BookingRule`](../../schema/BookingRule/README.md) | Booking closes 1 hour before departure | `beckn:Policy` | ✅ |
| [`ServiceClass`](../../schema/ServiceClass/README.md) | Volvo A/C Sleeper class confirmed | `beckn:CategoryCode` | ✅ |

---

#### Action: `init`
**Semantic intent:** Sanjay submits details for both passengers and payment method.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Passenger`](../../schema/Passenger/README.md) | Passenger 1: Sanjay (name, phone, ID proof type) | `beckn:Participant` | ✅ |
| [`Passenger`](../../schema/Passenger/README.md) | Passenger 2: co-traveler (name, phone) | `beckn:Participant` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult category for both passengers | `beckn:CategoryCode` | ✅ |
| [`PassengerGroup`](../../schema/PassengerGroup/README.md) | 2 passengers as a group | `beckn:Quantity` | ✅ |

---

#### Action: `on_init`
**Semantic intent:** KSRTC returns the full journey contract terms including total fare, baggage policy, and all applicable policies.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Journey`](../../schema/Journey/README.md) | Draft intercity journey contract | `beckn:Contract` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Total ₹700 fare before payment | `beckn:PriceComponent` | ✅ |
| [`BaggageAllowance`](../../schema/BaggageAllowance/README.md) | Binding baggage policy | `beckn:Constraint` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Binding cancellation schedule | `beckn:CancellationPolicy` | ✅ |
| [`Seat`](../../schema/Seat/README.md) | Reserved seats 12A and 12B | `beckn:Entitlement` | ✅ |
| [`Entitlement`](../../schema/Entitlement/README.md) | Travel entitlement on this service | `beckn:Entitlement` | ✅ |

---

#### Action: `confirm`
**Semantic intent:** Sanjay pays ₹700 and confirms the booking.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Journey`](../../schema/Journey/README.md) | Journey order being confirmed | `beckn:Contract` | ✅ |
| [`Passenger`](../../schema/Passenger/README.md) | Both passengers confirming identity | `beckn:Participant` | ✅ |

---

#### Action: `on_confirm`
**Semantic intent:** KSRTC confirms the booking, issues digital QR code tickets for both passengers, and assigns seats.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Journey`](../../schema/Journey/README.md) | Confirmed intercity journey contract | `beckn:Contract` | ✅ |
| [`Ticket`](../../schema/Ticket/README.md) | QR code ticket for Passenger 1 (seat 12A) | `beckn:Entitlement` | ✅ |
| [`Ticket`](../../schema/Ticket/README.md) | QR code ticket for Passenger 2 (seat 12B) | `beckn:Entitlement` | ✅ |
| [`TravelDocument`](../../schema/TravelDocument/README.md) | Digital QR ticket document for both passengers | `beckn:Entitlement` | ✅ |
| [`Seat`](../../schema/Seat/README.md) | Confirmed seats 12A and 12B | `beckn:Entitlement` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final ₹700 binding fare breakup | `beckn:PriceComponent` | ✅ |
| [`BaggageAllowance`](../../schema/BaggageAllowance/README.md) | Binding baggage allowance | `beckn:Constraint` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Boarding: Bay 7, Kempegowda Bus Terminal (with map link) | `beckn:FulfillmentStop` | ✅ |
| [`Vehicle`](../../schema/Vehicle/README.md) | Specific Volvo bus (registration number, model) | `beckn:Item` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | KSRTC helpline for travel day issues | `beckn:SupportInfo` | ✅ |

---

### Stage 3 — Fulfillment

---

#### Action: `status`
**Semantic intent:** On the morning of travel, Sanjay checks if the bus is on time.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Journey`](../../schema/Journey/README.md) | Intercity journey being queried | `beckn:Contract` | ✅ |

---

#### Action: `on_status`
**Semantic intent:** KSRTC confirms the bus is 15 minutes late and returns current vehicle location.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Journey state snapshot — 15-minute delay | `beckn:Contract` | ✅ |
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Current bus location (still in depot) | `beckn:Tracking` | ✅ |
| [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | Revised departure time (6:15 AM from Bay 7) | `beckn:Tracking` | ✅ |
| [`Alert`](../../schema/Alert/README.md) | Service delay notification (TECHNICAL_PROBLEM) | `beckn:Alert` | ✅ |
| [`Event`](../../schema/Event/README.md) | `SERVICE_DELAYED` lifecycle event | `beckn:State` | ✅ |

---

#### Action: `track`
**Semantic intent:** During the journey, Sanjay tracks the bus location to estimate arrival at Mysuru.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Journey`](../../schema/Journey/README.md) | Journey being tracked | `beckn:Contract` | ✅ |

---

#### Action: `on_track`
**Semantic intent:** KSRTC returns live bus location and ETA at Mysuru Bus Stand.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Current live coordinates, speed, bearing | `beckn:Tracking` | ✅ |
| [`Telemetry`](../../schema/Telemetry/README.md) | Speed and odometer for ETA calculation | `beckn:Tracking` | ✅ |
| [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | Revised arrival ETA at Mysuru Bus Stand | `beckn:Tracking` | ✅ |

---

#### Action: `update`
**Semantic intent:** KSRTC notifies that the bus will make an unscheduled 5-minute stop at Ramanagara (e.g., driver break).

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Contract modification — unscheduled stop added | `beckn:Contract` | ✅ |
| [`Stop`](../../schema/Stop/README.md) | Ramanagara unscheduled stop reference | `beckn:FulfillmentStop` | ✅ |

---

#### Action: `on_update`
**Semantic intent:** BPP acknowledges update with revised arrival ETA.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Updated journey with revised Mysuru ETA | `beckn:Contract` | ✅ |
| [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | New Mysuru arrival: 10:10 AM (was 9:30 AM) | `beckn:Tracking` | ✅ |

---

#### Action: `cancel` (if Sanjay cancels before boarding due to delay)
**Semantic intent:** Sanjay decides the delay is too long and cancels 2 hours before departure.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Journey`](../../schema/Journey/README.md) | Journey order being cancelled | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Policy at 2-hour window (50% refund) | `beckn:CancellationPolicy` | ✅ |

---

#### Action: `on_cancel`
**Semantic intent:** KSRTC applies the 50% cancellation refund and issues a cancellation receipt.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Journey`](../../schema/Journey/README.md) | Cancelled journey contract | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Applied policy (50% refund) | `beckn:CancellationPolicy` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Cancellation receipt showing ₹350 refund | `beckn:Invoice` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Net settlement: ₹350 charged, ₹350 refunded | `beckn:PriceComponent` | ✅ |
| [`Ticket`](../../schema/Ticket/README.md) | Both tickets invalidated | `beckn:Entitlement` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`
**Semantic intent:** After completing the trip, Sanjay rates the service — 3 stars due to the seat issue.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | 3-star service rating (ratedEntityType: SERVICE) | `beckn:RatingInput` | ✅ |
| [`Rating`](../../schema/Rating/README.md) | Vehicle cleanliness rating (ratedEntityType: VEHICLE) | `beckn:RatingInput` | ✅ |
| [`Review`](../../schema/Review/README.md) | "Seat was taken, had to sit elsewhere" free-text review | `beckn:RatingInput` | ✅ |
| [`Feedback`](../../schema/Feedback/README.md) | Tags: SEAT_ISSUE, DELAY, CLEAN_BUS | `beckn:Feedback` | ✅ |

---

#### Action: `on_rating`
**Semantic intent:** BPP acknowledges the rating.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | Confirmed ratings | `beckn:RatingInput` | ✅ |

---

#### Action: `support`
**Semantic intent:** Sanjay raises a support case — his reserved seat 12A was occupied and he had to sit in an unreserved seat for the entire journey.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Seat dispute complaint (type: COMPLAINT, priority: HIGH) | `beckn:SupportRequest` | ✅ |

---

#### Action: `on_support`
**Semantic intent:** KSRTC acknowledges the complaint, opens a ticket, and offers a partial refund or travel voucher.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Updated case with KSRTC ticket ID and resolution status | `beckn:SupportRequest` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Partial refund receipt or travel voucher | `beckn:Invoice` | ✅ |
| [`Entitlement`](../../schema/Entitlement/README.md) | Travel voucher for future KSRTC journey | `beckn:Entitlement` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | KSRTC grievance redressal contact | `beckn:SupportInfo` | ✅ |

---

## Coverage Summary

| Class | Actions Used In | Lifecycle Stage |
|-------|----------------|----------------|
| `TripSpecification` | search | Discovery |
| `Place` | search | Discovery |
| `RiderCategory` | search, select, init | Discovery, Contracting |
| `PassengerGroup` | search, init | Discovery, Contracting |
| `ServiceClass` | search, on_search, on_select | Discovery, Contracting |
| `TripResult` | on_search | Discovery |
| `Journey` | on_search, on_init, confirm, on_confirm, status, track, cancel, on_cancel | All stages |
| `Leg` | on_search | Discovery |
| `Segment` | on_search | Discovery |
| `VehicleJourney` | on_search, select, on_select | Discovery, Contracting |
| `Route` | on_search | Discovery |
| `Stop` | on_search, on_select, on_confirm, update | Discovery, Contracting, Fulfillment |
| `StopTime` | on_search, on_select | Discovery, Contracting |
| `Vehicle` | on_search, on_confirm | Discovery, Contracting |
| `VehicleType` | on_search | Discovery |
| `Seat` | on_search, select, on_select, on_init, on_confirm, on_cancel | Discovery → Fulfillment |
| `FareProduct` | on_search, select | Discovery, Contracting |
| `Fare` | on_search, on_select | Discovery, Contracting |
| `FareLegRule` | on_search | Discovery |
| `SalesOfferPackage` | on_search | Discovery |
| `BaggageAllowance` | on_search, on_select, on_init, on_confirm | Discovery, Contracting |
| `BookingRule` | on_search, on_select | Discovery, Contracting |
| `CancellationPolicy` | on_search, on_select, on_init, cancel, on_cancel | Discovery, Contracting, Fulfillment |
| `Operator` | on_search | Discovery |
| `Timetable` | on_search | Discovery |
| `ServiceCalendar` | on_search | Discovery |
| `PlaceRequest` | select | Contracting |
| `FareBreakup` | on_select, on_init, on_confirm, on_cancel, on_support | Contracting, Fulfillment, Post |
| `Passenger` | init, confirm | Contracting |
| `Entitlement` | on_init, on_support | Contracting, Post-Fulfillment |
| `Ticket` | on_confirm, on_cancel | Contracting, Fulfillment |
| `TravelDocument` | on_confirm | Contracting |
| `ContactHandle` | on_confirm, on_support | Contracting, Post-Fulfillment |
| `TripUpdate` | on_status, update, on_update | Fulfillment |
| `VehiclePosition` | on_status, on_track | Fulfillment |
| `StopTimeUpdate` | on_status, on_track, on_update | Fulfillment |
| `Alert` | on_status | Fulfillment |
| `Event` | on_status | Fulfillment |
| `Telemetry` | on_track | Fulfillment |
| `Receipt` | on_cancel, on_support | Fulfillment, Post-Fulfillment |
| `Rating` | rating, on_rating | Post-Fulfillment |
| `Review` | rating | Post-Fulfillment |
| `Feedback` | rating | Post-Fulfillment |
| `SupportCase` | support, on_support | Post-Fulfillment |

---

## Gap Report

| Gap | Description | Severity |
|-----|-------------|----------|
| No gaps detected | All schema classes required for the intercity bus lifecycle exist in the mobility schema. `TripSpecification`, `Journey`, `Segment`, `Seat`, `PlaceRequest`, `BaggageAllowance`, and `SalesOfferPackage` collectively handle the richer intercity booking model. | — |

> **Design notes:**
> - The key semantic distinction between city bus and intercity bus is the **contract type**: city bus uses `Itinerary` (a planned journey from the passenger's perspective), while intercity uses `Journey` (a full operator-defined travel contract with bilateral obligations including seat assignment, baggage terms, and multi-passenger identity verification).
> - `Segment` captures sub-segments of an intercity leg (e.g., Bengaluru → Ramanagara → Mysuru) — this is used in the TAP TSI / BOB / OSDM interoperable rail model and maps identically to intercity bus operations.
> - `PlaceRequest` is the pre-booking seat selection mechanism, while `Seat` is the actual allocated seat entity issued in `on_confirm`.
> - The `SalesOfferPackage` bundles the bus seat with optional services (travel insurance) — this maps the NeTEx `SalesOfferPackage` pattern to intercity bus.
> - Multi-passenger bookings require multiple `Passenger` and `Ticket` instances — all within a single `Journey` contract bound to a single payment.
