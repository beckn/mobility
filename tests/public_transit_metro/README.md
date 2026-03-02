# Public Transit (Metro) — Lifecycle Stress Test

## Use Case Narrative

Kavya needs to travel from MG Road metro station to Whitefield on the Kochi Metro's Purple Line. She opens the Kochi Metro app, searches for her journey, and is shown a single-trip fare of ₹45 for an Adult. She taps to purchase, pays via UPI, and receives a QR code. At MG Road station she scans the QR code at the fare gate on the concourse level. She checks the next train arrival on the app (live ETA board), boards the train at Platform 2, and travels to Whitefield. The app shows a service alert mid-journey — a delay due to signal maintenance. She exits via the QR gate at Whitefield. Post-journey, she rates the service.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Kavya | Consumer — the metro commuter | Represented by BAP |
| Metro App | BAP — ticket purchase and journey tracking | `beckn:BAP` |
| Kochi Metro Platform | BPP — manages ticketing, timetables, real-time data | `beckn:BPP` |
| Metro Train | Fulfillment vehicle — operates the Purple Line | `mobility:Vehicle` |

---

## Key Differentiators vs Bus Transit

Metro stress testing introduces several additional schema classes not needed for bus:

| Additional Class | Why Metro-Specific |
|-----------------|-------------------|
| `StopPlace` | Metro stations are complex multi-level facilities (not simple roadside stops) |
| `Quay` | Metro platforms (Platform 1, Platform 2) within a station |
| `Level` | Station concourse level, platform level, street level |
| `Pathway` | Lifts, escalators, stairways within station for accessibility routing |
| `Interchange` | Timed connections at interchange stations (e.g., MG Road to Green Line) |
| `FareMedium` | Contactless smart card (Metro card / NCMC) or QR code |
| `TariffZone` | Metro fare zones determining the ₹45 fare |
| `FareTransferRule` | Free or discounted transfer between metro lines |
| `StopArea` | Station entry/exit zones for gating |

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Kavya submits a metro journey search — origin station, destination station, departure time, and passenger category.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripRequest`](../../schema/TripRequest/README.md) | Top-level metro journey intent | `beckn:Intent` | ✅ |
| [`StopPlace`](../../schema/StopPlace/README.md) | MG Road metro station (origin) | `beckn:Location` | ✅ |
| [`StopPlace`](../../schema/StopPlace/README.md) | Whitefield metro station (destination) | `beckn:Location` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult passenger category | `beckn:CategoryCode` | ✅ |
| [`PassengerGroup`](../../schema/PassengerGroup/README.md) | Number of passengers | `beckn:Quantity` | ✅ |

**Notes:** Unlike bus, metro search uses `StopPlace` (a complex station facility) rather than bare `Stop`. The `StopPlace.quays` carry the specific platform boarding information. `TripRequest.modes` = METRO.

---

#### Action: `on_search`
**Semantic intent:** The Kochi Metro platform returns available metro trips, fare products, and station details.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripResult`](../../schema/TripResult/README.md) | Top-level catalog of metro journey options | `beckn:Catalog` | ✅ |
| [`Itinerary`](../../schema/Itinerary/README.md) | The direct MG Road → Whitefield journey | `beckn:Contract` | ✅ |
| [`Leg`](../../schema/Leg/README.md) | The metro leg (single uninterrupted segment) | `beckn:Fulfillment` | ✅ |
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | Specific Purple Line train service | `beckn:Fulfillment` | ✅ |
| [`StopTime`](../../schema/StopTime/README.md) | Scheduled departure from MG Road and arrival at Whitefield | `beckn:TimePeriod` | ✅ |
| [`Line`](../../schema/Line/README.md) | Kochi Metro Purple Line details | `beckn:Item` | ✅ |
| [`Route`](../../schema/Route/README.md) | Purple Line route from Airport to Whitefield | `beckn:Item` | ✅ |
| [`Quay`](../../schema/Quay/README.md) | Platform 2 at MG Road station (boarding platform) | `beckn:FulfillmentStop` | ✅ |
| [`StopPlace`](../../schema/StopPlace/README.md) | Full station details for MG Road and Whitefield | `beckn:Location` | ✅ |
| [`Level`](../../schema/Level/README.md) | Platform level and concourse level within MG Road station | `beckn:Location` | ✅ |
| [`Pathway`](../../schema/Pathway/README.md) | Escalator from concourse to platform at MG Road | `beckn:Location` | ✅ |
| [`FareProduct`](../../schema/FareProduct/README.md) | Adult single-trip QR ticket fare product | `beckn:Offer` | ✅ |
| [`Fare`](../../schema/Fare/README.md) | ₹45 fare for the MG Road → Whitefield journey | `beckn:Offer` | ✅ |
| [`FareLegRule`](../../schema/FareLegRule/README.md) | Rules applying this fare to the specific leg and zone | `beckn:Policy` | ✅ |
| [`TariffZone`](../../schema/TariffZone/README.md) | Metro fare zones for computing the ₹45 | `beckn:Location` | ✅ |
| [`FareTransferRule`](../../schema/FareTransferRule/README.md) | Transfer discount if Kavya changes lines at an interchange | `beckn:Policy` | ✅ |
| [`Network`](../../schema/Network/README.md) | Kochi Metro network | `beckn:Catalog` | ✅ |
| [`Operator`](../../schema/Operator/README.md) | Kochi Metro Rail Limited | `beckn:Provider` | ✅ |
| [`Timetable`](../../schema/Timetable/README.md) | Published metro timetable | `beckn:Catalog` | ✅ |
| [`ServiceCalendar`](../../schema/ServiceCalendar/README.md) | Metro operating days | `beckn:TimePeriod` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Metro ticket cancellation terms | `beckn:CancellationPolicy` | ✅ |

**Notes:** `TariffZone` + `FareLegRule` determine the ₹45 fare based on origin and destination zones. `Quay` identifies Platform 2 specifically. `Level` + `Pathway` enable the app to show Kavya which escalator leads from the fare gate to the platform — critical for accessibility routing.

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Kavya selects the specific train departure and confirms the Adult single-trip QR code ticket.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | Specific metro train trip (by id) | `beckn:Fulfillment` | ✅ |
| [`FareProduct`](../../schema/FareProduct/README.md) | Adult single-trip QR ticket | `beckn:Offer` | ✅ |
| [`FareMedium`](../../schema/FareMedium/README.md) | QR code (mobile app) as the preferred fare medium | `beckn:Entitlement` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult category confirmation | `beckn:CategoryCode` | ✅ |

---

#### Action: `on_select`
**Semantic intent:** The BPP confirms the train availability and returns the locked fare with boarding station details.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | Confirmed metro trip with full stop times | `beckn:Fulfillment` | ✅ |
| [`Fare`](../../schema/Fare/README.md) | Locked ₹45 fare | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Base fare + any taxes | `beckn:PriceComponent` | ✅ |
| [`Quay`](../../schema/Quay/README.md) | Confirmed boarding platform (Platform 2, MG Road) | `beckn:FulfillmentStop` | ✅ |
| [`StopTime`](../../schema/StopTime/README.md) | Exact departure time from Platform 2 | `beckn:TimePeriod` | ✅ |
| [`FareMedium`](../../schema/FareMedium/README.md) | Confirmed QR code medium | `beckn:Entitlement` | ✅ |
| [`StopArea`](../../schema/StopArea/README.md) | Fare gate entry zone at MG Road station | `beckn:Location` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Metro ticket policy (typically non-refundable once used) | `beckn:CancellationPolicy` | ✅ |

---

#### Action: `init`
**Semantic intent:** Kavya submits her identity for ticket issuance and chooses QR code delivery.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Passenger`](../../schema/Passenger/README.md) | Kavya's passenger identity | `beckn:Participant` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult category | `beckn:CategoryCode` | ✅ |
| [`FareMedium`](../../schema/FareMedium/README.md) | QR code delivery method | `beckn:Entitlement` | ✅ |

---

#### Action: `on_init`
**Semantic intent:** BPP returns the final ticketing contract before payment.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Draft metro journey contract | `beckn:Contract` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | ₹45 final fare before payment | `beckn:PriceComponent` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Binding: no refund once the QR is scanned | `beckn:CancellationPolicy` | ✅ |
| [`Entitlement`](../../schema/Entitlement/README.md) | Travel entitlement for the MG Road → Whitefield leg | `beckn:Entitlement` | ✅ |

---

#### Action: `confirm`
**Semantic intent:** Kavya pays ₹45 via UPI and confirms the purchase.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Confirmed metro journey order | `beckn:Contract` | ✅ |
| [`Passenger`](../../schema/Passenger/README.md) | Confirming passenger | `beckn:Participant` | ✅ |

---

#### Action: `on_confirm`
**Semantic intent:** BPP issues the QR code ticket and returns the complete journey contract.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Confirmed metro journey contract | `beckn:Contract` | ✅ |
| [`Ticket`](../../schema/Ticket/README.md) | Issued QR code ticket (validFrom, validUntil) | `beckn:Entitlement` | ✅ |
| [`TravelDocument`](../../schema/TravelDocument/README.md) | QR code as the digital travel document (type: QR_CODE) | `beckn:Entitlement` | ✅ |
| [`FareProduct`](../../schema/FareProduct/README.md) | Adult single-trip product with validity scope | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final ₹45 binding fare breakup | `beckn:PriceComponent` | ✅ |
| [`Quay`](../../schema/Quay/README.md) | Boarding platform (Platform 2, MG Road) | `beckn:FulfillmentStop` | ✅ |
| [`Level`](../../schema/Level/README.md) | Platform level at MG Road (for wayfinding) | `beckn:Location` | ✅ |
| [`Pathway`](../../schema/Pathway/README.md) | Escalator route from station entrance to Platform 2 | `beckn:Location` | ✅ |
| [`VehicleJourney`](../../schema/VehicleJourney/README.md) | Train departure reference | `beckn:Fulfillment` | ✅ |

---

### Stage 3 — Fulfillment

---

#### Action: `status`
**Semantic intent:** Kavya checks when the next Purple Line train is due at Platform 2.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Metro journey being queried | `beckn:Contract` | ✅ |

---

#### Action: `on_status`
**Semantic intent:** BPP returns real-time train status — next departure ETA, platform, and any delays.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Journey state snapshot | `beckn:Contract` | ✅ |
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Current position of the Purple Line train | `beckn:Tracking` | ✅ |
| [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | Predicted arrival at MG Road (delay in seconds) | `beckn:Tracking` | ✅ |
| [`EstimatedTimetableDelivery`](../../schema/EstimatedTimetableDelivery/README.md) | Full estimated timetable for upcoming Purple Line services | `beckn:Tracking` | ✅ |
| [`OccupancyStatus`](../../schema/OccupancyStatus/README.md) | Train car occupancy (MANY_SEATS_AVAILABLE) | `beckn:State` | ✅ |
| [`Alert`](../../schema/Alert/README.md) | Signal maintenance alert causing a 5-minute delay | `beckn:Alert` | ✅ |
| [`Incident`](../../schema/Incident/README.md) | Signal maintenance classified as infrastructure incident | `beckn:Alert` | ✅ |

---

#### Action: `track`
**Semantic intent:** Kavya checks the live ETA board on the app while waiting on Platform 2.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Journey being tracked | `beckn:Contract` | ✅ |

---

#### Action: `on_track`
**Semantic intent:** BPP returns real-time vehicle position and platform-specific arrival prediction.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Train's live coordinates and speed | `beckn:Tracking` | ✅ |
| [`MonitoredVehicleJourney`](../../schema/MonitoredVehicleJourney/README.md) | Real-time monitored Purple Line journey | `beckn:Tracking` | ✅ |
| [`MonitoredCall`](../../schema/MonitoredCall/README.md) | Predicted arrival at MG Road Platform 2 | `beckn:Tracking` | ✅ |
| [`StopMonitoring`](../../schema/StopMonitoring/README.md) | All upcoming services at MG Road Platform 2 | `beckn:Tracking` | ✅ |
| [`ServiceDelivery`](../../schema/ServiceDelivery/README.md) | SIRI-compliant service delivery container | `beckn:Catalog` | ✅ |

---

#### Action: `update`
**Semantic intent:** During the journey, a signal fault is reported — all trains are running 8 minutes late.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Contract update: delay notification | `beckn:Contract` | ✅ |
| [`Alert`](../../schema/Alert/README.md) | Service disruption alert (SIGNAL_FAULT) | `beckn:Alert` | ✅ |
| [`EntitySelector`](../../schema/EntitySelector/README.md) | Identifies which trains/stops are affected | `beckn:Alert` | ✅ |
| [`GeneralMessageDelivery`](../../schema/GeneralMessageDelivery/README.md) | SIRI general message with passenger information text | `beckn:Alert` | ✅ |

---

#### Action: `on_update`
**Semantic intent:** BPP acknowledges with revised arrival times.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Updated journey with revised ETA at Whitefield | `beckn:Contract` | ✅ |
| [`StopTimeUpdate`](../../schema/StopTimeUpdate/README.md) | 8-minute delay applied to all upcoming stops | `beckn:Tracking` | ✅ |

---

#### Action: `cancel`
**Semantic intent:** Kavya cancels her ticket before boarding due to the extended delay.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Metro journey order being cancelled | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Metro ticket cancellation policy | `beckn:CancellationPolicy` | ✅ |

---

#### Action: `on_cancel`
**Semantic intent:** BPP invalidates the QR code and processes refund (operator-discretion full refund for delay-caused cancellations).

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Itinerary`](../../schema/Itinerary/README.md) | Cancelled journey contract | `beckn:Contract` | ✅ |
| [`Ticket`](../../schema/Ticket/README.md) | Invalidated QR code ticket | `beckn:Entitlement` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Applied policy (full refund due to delay) | `beckn:CancellationPolicy` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Cancellation receipt with full refund | `beckn:Invoice` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`
**Semantic intent:** Kavya rates the metro service — 4 stars (clean station, delay was frustrating).

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | 4-star service rating (ratedEntityType: SERVICE) | `beckn:RatingInput` | ✅ |
| [`Review`](../../schema/Review/README.md) | "Clean stations but the delay was unexpected" | `beckn:RatingInput` | ✅ |
| [`Feedback`](../../schema/Feedback/README.md) | Tags: CLEAN_STATION, PUNCTUALITY_ISSUE | `beckn:Feedback` | ✅ |

---

#### Action: `on_rating`
**Semantic intent:** BPP acknowledges the rating.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | Confirmed rating | `beckn:RatingInput` | ✅ |

---

#### Action: `support`
**Semantic intent:** Kavya's QR code didn't scan at the exit gate — she was double-charged. She raises a fare recovery support case.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Fare gate / billing complaint (type: COMPLAINT) | `beckn:SupportRequest` | ✅ |

---

#### Action: `on_support`
**Semantic intent:** BPP returns the station helpdesk contact and ticket details for resolution.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Updated case with ticket ID | `beckn:SupportRequest` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Original ticket for dispute evidence | `beckn:Invoice` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | Kochi Metro helpdesk number and chat | `beckn:SupportInfo` | ✅ |

---

## Coverage Summary

| Class | Actions Used In | Lifecycle Stage |
|-------|----------------|----------------|
| `TripRequest` | search | Discovery |
| `StopPlace` | search, on_search, on_select | Discovery, Contracting |
| `RiderCategory` | search, select, init | Discovery, Contracting |
| `PassengerGroup` | search | Discovery |
| `TripResult` | on_search | Discovery |
| `Itinerary` | on_search, on_init, confirm, on_confirm, status, track, update, on_update, cancel, on_cancel | All stages |
| `Leg` | on_search | Discovery |
| `VehicleJourney` | on_search, select, on_select, on_confirm | Discovery, Contracting |
| `StopTime` | on_search, on_select | Discovery, Contracting |
| `Line` | on_search | Discovery |
| `Route` | on_search | Discovery |
| `Quay` | on_search, on_select, on_confirm | Discovery, Contracting |
| `Level` | on_search, on_confirm | Discovery, Contracting |
| `Pathway` | on_search, on_confirm | Discovery, Contracting |
| `FareProduct` | on_search, select, on_confirm | Discovery, Contracting |
| `Fare` | on_search, on_select | Discovery, Contracting |
| `FareLegRule` | on_search | Discovery |
| `TariffZone` | on_search | Discovery |
| `FareTransferRule` | on_search | Discovery |
| `Network` | on_search | Discovery |
| `Operator` | on_search | Discovery |
| `Timetable` | on_search | Discovery |
| `ServiceCalendar` | on_search | Discovery |
| `CancellationPolicy` | on_search, on_select, on_init, cancel, on_cancel | Discovery, Contracting, Fulfillment |
| `FareMedium` | select, on_select, init | Contracting |
| `FareBreakup` | on_select, on_init, on_confirm | Contracting |
| `StopArea` | on_select | Contracting |
| `Passenger` | init, confirm | Contracting |
| `Entitlement` | on_init | Contracting |
| `Ticket` | on_confirm, on_cancel | Contracting, Fulfillment |
| `TravelDocument` | on_confirm | Contracting |
| `TripUpdate` | on_status, update, on_update | Fulfillment |
| `VehiclePosition` | on_status, on_track | Fulfillment |
| `StopTimeUpdate` | on_status, on_update | Fulfillment |
| `EstimatedTimetableDelivery` | on_status | Fulfillment |
| `OccupancyStatus` | on_status | Fulfillment |
| `Alert` | on_status, update | Fulfillment |
| `Incident` | on_status | Fulfillment |
| `MonitoredVehicleJourney` | on_track | Fulfillment |
| `MonitoredCall` | on_track | Fulfillment |
| `StopMonitoring` | on_track | Fulfillment |
| `ServiceDelivery` | on_track | Fulfillment |
| `EntitySelector` | update | Fulfillment |
| `GeneralMessageDelivery` | update | Fulfillment |
| `Receipt` | on_cancel, on_support | Fulfillment, Post-Fulfillment |
| `Rating` | rating, on_rating | Post-Fulfillment |
| `Review` | rating | Post-Fulfillment |
| `Feedback` | rating | Post-Fulfillment |
| `SupportCase` | support, on_support | Post-Fulfillment |
| `ContactHandle` | on_support | Post-Fulfillment |
| `Interchange` | (used in multi-line journey variant) | Contracting |

---

## Gap Report

| Gap | Description | Severity |
|-----|-------------|----------|
| No gaps detected | All schema classes required for the metro lifecycle exist in the mobility schema. The NeTEx station model (`StopPlace`, `Quay`, `Level`, `Pathway`), SIRI real-time stack (`MonitoredVehicleJourney`, `MonitoredCall`, `ServiceDelivery`, `GeneralMessageDelivery`, `EstimatedTimetableDelivery`), GTFS Fares v2 (`TariffZone`, `FareLegRule`, `FareTransferRule`), and the full Beckn entitlement model (`Ticket`, `TravelDocument`, `FareMedium`) are all well-represented. | — |

> **Design notes:**
> - The `Interchange` class handles multi-line journeys where Kavya transfers between the Purple Line and the Blue Line at a timed interchange station — it specifies `minTransferTime` and `transferType: TIMED`.
> - The `GeneralMessageDelivery` + `EntitySelector` pair maps directly to the SIRI GM Service for passenger information broadcasts.
> - The `ServiceDelivery` class acts as the SIRI-compliant envelope wrapping `StopMonitoring`, `VehicleMonitoringDelivery`, and `EstimatedTimetableDelivery`.
