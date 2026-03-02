# Ride Hailing — Lifecycle Stress Test

## Use Case Narrative

Priya opens a ride-hailing app on her phone. She sets her current location as pickup and her office as the destination. The app shows her several ride options — Auto, Mini, Sedan — each with a fare estimate and ETA. She selects a Mini, sees the final fare breakup with surge pricing applied, enters her name and payment preference, and confirms the booking. A driver accepts the ride; she can see his location on a live map. When she arrives at the office, a receipt is issued. Later, she rates the driver and leaves a short review. Her forgotten umbrella prompts her to raise a support case.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Priya | Consumer — the person requesting the ride | Represented by BAP |
| MaaS App | BAP — renders options, relays Priya's decisions | `beckn:BAP` |
| Ride Platform | BPP — manages driver supply, dispatching, pricing | `beckn:BPP` |
| Driver | Fulfillment agent — operates the vehicle | `mobility:Driver` |

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Priya expresses her ride intent — pickup, dropoff, time, passenger count, and preferred vehicle type.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`RideRequest`](../../schema/RideRequest/README.md) | Top-level intent carrying pickup, dropoff, time, preferences | `beckn:Intent` | ✅ |
| [`Place`](../../schema/Place/README.md) | Pickup location (origin) | `beckn:Location` | ✅ |
| [`Place`](../../schema/Place/README.md) | Dropoff location (destination) | `beckn:Location` | ✅ |
| [`VehicleCategory`](../../schema/VehicleCategory/README.md) | Rider's preferred vehicle class (Auto, Mini, Sedan) | `beckn:CategoryCode` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Passenger type (Adult) — affects surge/concession eligibility | `beckn:CategoryCode` | ✅ |
| [`PassengerGroup`](../../schema/PassengerGroup/README.md) | Number and type of passengers in this ride | `beckn:Quantity` | ✅ |

**Notes:** `RideRequest.origin` and `RideRequest.destination` use `beckn:Location`. The `Place` subclass adds `placeType` and `placeName` for human-readable identification (e.g., "Indiranagar Metro Station"). The BAP SHOULD include `RiderCategory` when the rider has a registered category (student, senior) so BPP can compute concessions early.

---

#### Action: `on_search`
**Semantic intent:** The BPP returns a catalog of available ride options matching Priya's intent — each option is a combination of vehicle category, ETA, and pricing model.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`PlanningResult`](../../schema/PlanningResult/README.md) | Top-level catalog container for ride options | `beckn:Catalog` | ✅ |
| [`RideOption`](../../schema/RideOption/README.md) | A single selectable ride product (e.g., Mini, Sedan) | `beckn:Offer` | ✅ |
| [`VehicleCategory`](../../schema/VehicleCategory/README.md) | Vehicle class for each option | `beckn:CategoryCode` | ✅ |
| [`FareEstimate`](../../schema/FareEstimate/README.md) | Pre-booking price estimate with min/max range | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Itemised components of the estimate (base, surge, tax) | `beckn:PriceComponent` | ✅ |
| [`SurgeMultiplier`](../../schema/SurgeMultiplier/README.md) | Dynamic demand multiplier applied to base fare | `beckn:PriceComponent` | ✅ |
| [`PricingModel`](../../schema/PricingModel/README.md) | Tariff structure — metered, upfront quote, subscription | `beckn:Offer` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | How long driver will wait, and waiting charges | `beckn:Policy` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Pre-confirmation cancellation terms | `beckn:CancellationPolicy` | ✅ |
| [`Operator`](../../schema/Operator/README.md) | The ride platform or fleet operator | `beckn:Provider` | ✅ |

**Notes:** `PlanningResult` contains an array of `RideOption` entries, each referencing a `VehicleCategory` and a `FareEstimate`. The `SurgeMultiplier` is attached to `FareBreakup` as a distinct price component — this preserves the breakdown so riders understand why the fare is elevated. `PricingModel` describes whether the fare is a fixed upfront quote or metered (distance + time).

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Priya taps on "Mini" — she selects a specific ride option and optionally specifies additional preferences (e.g., quiet ride, AC).

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`RideOption`](../../schema/RideOption/README.md) | The selected ride product (identified by id) | `beckn:Offer` | ✅ |
| [`ServiceClass`](../../schema/ServiceClass/README.md) | Service tier preference (Economy, Premium, Shared) | `beckn:CategoryCode` | ✅ |
| [`PickupPolicy`](../../schema/PickupPolicy/README.md) | Preferred pickup zone or meet-point instructions | `beckn:Policy` | ✅ |

---

#### Action: `on_select`
**Semantic intent:** The BPP confirms the selected option is available, locks the fare estimate, and returns driver/vehicle assignment if pre-assigned.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`RideOption`](../../schema/RideOption/README.md) | Confirmed ride option with updated ETA | `beckn:Offer` | ✅ |
| [`FareEstimate`](../../schema/FareEstimate/README.md) | Locked fare estimate (not yet final breakup) | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Component-level fare breakdown | `beckn:PriceComponent` | ✅ |
| [`Vehicle`](../../schema/Vehicle/README.md) | The specific vehicle to be dispatched | `beckn:Item` | ✅ |
| [`VehicleType`](../../schema/VehicleType/README.md) | Type details (fuel, capacity, accessibility) | `beckn:CategoryCode` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | Waiting time terms — confirmed at this stage | `beckn:Policy` | ✅ |
| [`PickupPolicy`](../../schema/PickupPolicy/README.md) | Confirmed pickup zone/meet-point | `beckn:Policy` | ✅ |
| [`DropPolicy`](../../schema/DropPolicy/README.md) | Drop zone rules and any restrictions | `beckn:Policy` | ✅ |

---

#### Action: `init`
**Semantic intent:** Priya submits her personal details and payment method preference to initiate the order.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rider`](../../schema/Rider/README.md) | Priya's identity, payment preference, membership plan | `beckn:Participant` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Passenger classification (Adult) | `beckn:CategoryCode` | ✅ |
| [`PassengerGroup`](../../schema/PassengerGroup/README.md) | Number of passengers traveling | `beckn:Quantity` | ✅ |

---

#### Action: `on_init`
**Semantic intent:** The BPP returns the full terms of the contract — final pricing, all applicable policies, and payment breakup — prior to payment confirmation.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Draft contract (order) — not yet confirmed | `beckn:Contract` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final fare breakup before payment | `beckn:PriceComponent` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Cancellation terms now binding | `beckn:CancellationPolicy` | ✅ |
| [`NoShowPolicy`](../../schema/NoShowPolicy/README.md) | No-show fee if rider doesn't appear | `beckn:Policy` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | Confirmed waiting time and charge | `beckn:Policy` | ✅ |
| [`SafetyPolicy`](../../schema/SafetyPolicy/README.md) | Emergency contact and safety instructions | `beckn:Policy` | ✅ |
| [`Entitlement`](../../schema/Entitlement/README.md) | Any applied voucher, coupon, or promo discount | `beckn:Entitlement` | ✅ |

---

#### Action: `confirm`
**Semantic intent:** Priya confirms payment — the booking is locked in. Payment is transmitted.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Order being confirmed (by id) | `beckn:Contract` | ✅ |
| [`Rider`](../../schema/Rider/README.md) | Confirming rider identity | `beckn:Participant` | ✅ |

---

#### Action: `on_confirm`
**Semantic intent:** The BPP creates the confirmed booking, assigns a driver and vehicle, and returns the full contract with fulfillment details.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Confirmed contract with all binding terms | `beckn:Contract` | ✅ |
| [`Driver`](../../schema/Driver/README.md) | Assigned driver's details and ratings | `beckn:FulfillmentAgent` | ✅ |
| [`Vehicle`](../../schema/Vehicle/README.md) | Assigned vehicle with plate number and type | `beckn:Item` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | Masked phone or chat handle to reach driver | `beckn:SupportInfo` | ✅ |
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Driver's current live location | `beckn:Tracking` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final fare breakup (now binding) | `beckn:PriceComponent` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | Binding waiting time terms | `beckn:Policy` | ✅ |
| [`PickupDropoffPoint`](../../schema/PickupDropoffPoint/README.md) | Confirmed pickup meet-point with landmark | `beckn:FulfillmentStop` | ✅ |

---

### Stage 3 — Fulfillment

---

#### Action: `status`
**Semantic intent:** Priya's app polls the BPP to check the current state of the trip (driver en route, arrived, trip started, etc.).

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Order being queried (by id) | `beckn:Contract` | ✅ |

---

#### Action: `on_status`
**Semantic intent:** The BPP returns the current fulfillment state, including driver location and trip phase.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Multi-dimensional state snapshot (contract + status + tracking) | `beckn:Contract` | ✅ |
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Real-time driver GPS position | `beckn:Tracking` | ✅ |
| [`Driver`](../../schema/Driver/README.md) | Driver reference (in case of reassignment) | `beckn:FulfillmentAgent` | ✅ |
| [`OccupancyStatus`](../../schema/OccupancyStatus/README.md) | Seats available (for shared ride variant) | `beckn:State` | ✅ |
| [`Event`](../../schema/Event/README.md) | Lifecycle event (DRIVER_ARRIVED, TRIP_STARTED, TRIP_ENDED) | `beckn:State` | ✅ |

**Notes:** The `TripUpdate.stateUpdate` carries the `Event` (e.g., `DRIVER_ARRIVED`). The `TripUpdate.trackingEndpoint` carries the `VehiclePosition` live URL. These three dimensions — contract state, status event, and tracking endpoint — are unified in `TripUpdate` by design.

---

#### Action: `track`
**Semantic intent:** Priya's app opens the live map — it requests the real-time tracking endpoint from the BPP.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Order being tracked (by id) | `beckn:Contract` | ✅ |

---

#### Action: `on_track`
**Semantic intent:** The BPP returns the tracking URL or data stream for live driver location.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Current driver coordinates, bearing, speed | `beckn:Tracking` | ✅ |
| [`Telemetry`](../../schema/Telemetry/README.md) | Detailed time-series data (speed, battery, odometer) | `beckn:Tracking` | ✅ |

---

#### Action: `update`
**Semantic intent:** Priya adds a stop mid-ride (to collect a friend). The BPP updates the contract and recalculates the fare.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Updated contract with new stop | `beckn:Contract` | ✅ |
| [`PickupDropoffPoint`](../../schema/PickupDropoffPoint/README.md) | The new intermediate stop location | `beckn:FulfillmentStop` | ✅ |

---

#### Action: `on_update`
**Semantic intent:** The BPP acknowledges the stop addition and returns an updated fare.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Updated contract state including revised fare | `beckn:Contract` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Revised fare breakup with additional stop component | `beckn:PriceComponent` | ✅ |

---

#### Action: `cancel`
**Semantic intent:** Priya cancels the booking before the driver arrives.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Order being cancelled (by id) | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Referenced policy under which cancellation is requested | `beckn:CancellationPolicy` | ✅ |

---

#### Action: `on_cancel`
**Semantic intent:** The BPP applies the cancellation policy, calculates refund (if any), and returns the final receipt.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Cancelled contract with final state | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | The policy applied, including refund percentage | `beckn:CancellationPolicy` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Cancellation receipt (with refund amount) | `beckn:Invoice` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Net settlement after applying cancellation charges | `beckn:PriceComponent` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`
**Semantic intent:** Priya rates the driver 4 stars and selects "Clean Vehicle" as a positive tag.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | Numeric score for the driver (ratedEntityType: DRIVER) | `beckn:RatingInput` | ✅ |
| [`Review`](../../schema/Review/README.md) | Free-text review submitted alongside the rating | `beckn:RatingInput` | ✅ |
| [`Feedback`](../../schema/Feedback/README.md) | Structured tags (e.g., CLEAN_VEHICLE, SAFE_DRIVER) | `beckn:Feedback` | ✅ |

---

#### Action: `on_rating`
**Semantic intent:** The BPP acknowledges the rating submission.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | Acknowledged rating record with confirmation | `beckn:RatingInput` | ✅ |

---

#### Action: `support`
**Semantic intent:** Priya realizes she left her umbrella in the cab. She raises a lost-and-found support case.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Top-level support request (type: LOST_ITEM) | `beckn:SupportRequest` | ✅ |
| [`LostAndFoundItem`](../../schema/LostAndFoundItem/README.md) | Description, type, and time of the lost umbrella | `beckn:SupportRequest` | ✅ |

---

#### Action: `on_support`
**Semantic intent:** The BPP returns a contact handle to reach the driver or support team.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Updated case with ticket ID and status | `beckn:SupportRequest` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | Driver or support agent contact (masked phone/chat) | `beckn:SupportInfo` | ✅ |

---

## Coverage Summary

| Class | Actions Used In | Lifecycle Stage |
|-------|----------------|----------------|
| `RideRequest` | search | Discovery |
| `Place` | search | Discovery |
| `VehicleCategory` | search, on_search, select | Discovery, Contracting |
| `RiderCategory` | search, init | Discovery, Contracting |
| `PassengerGroup` | search, init | Discovery, Contracting |
| `PlanningResult` | on_search | Discovery |
| `RideOption` | on_search, select, on_select | Discovery, Contracting |
| `FareEstimate` | on_search, on_select | Discovery, Contracting |
| `FareBreakup` | on_search, on_select, on_init, on_confirm, on_update, on_cancel | All stages |
| `SurgeMultiplier` | on_search | Discovery |
| `PricingModel` | on_search | Discovery |
| `WaitingPolicy` | on_search, on_select, on_init, on_confirm | Contracting |
| `CancellationPolicy` | on_search, on_init, cancel, on_cancel | Contracting, Fulfillment |
| `Operator` | on_search | Discovery |
| `ServiceClass` | select | Contracting |
| `PickupPolicy` | select, on_select | Contracting |
| `DropPolicy` | on_select | Contracting |
| `Vehicle` | on_select, on_confirm | Contracting |
| `VehicleType` | on_select | Contracting |
| `Rider` | init, confirm | Contracting |
| `Trip` | on_init, confirm, on_confirm, status, track, cancel, on_cancel | Contracting, Fulfillment |
| `NoShowPolicy` | on_init | Contracting |
| `SafetyPolicy` | on_init | Contracting |
| `Entitlement` | on_init | Contracting |
| `Driver` | on_confirm, on_status | Contracting, Fulfillment |
| `ContactHandle` | on_confirm, on_support | Contracting, Post-Fulfillment |
| `VehiclePosition` | on_confirm, on_status, on_track | Fulfillment |
| `PickupDropoffPoint` | on_confirm, update | Contracting, Fulfillment |
| `TripUpdate` | on_status, update, on_update | Fulfillment |
| `OccupancyStatus` | on_status | Fulfillment |
| `Event` | on_status | Fulfillment |
| `Telemetry` | on_track | Fulfillment |
| `Receipt` | on_cancel | Fulfillment |
| `Rating` | rating, on_rating | Post-Fulfillment |
| `Review` | rating | Post-Fulfillment |
| `Feedback` | rating | Post-Fulfillment |
| `SupportCase` | support, on_support | Post-Fulfillment |
| `LostAndFoundItem` | support | Post-Fulfillment |

---

## Gap Report

| Gap | Description | Severity |
|-----|-------------|----------|
| No gaps detected | All schema classes required for the canonical ride hailing lifecycle exist in the mobility schema and carry appropriate properties inherited from correct Beckn core parent classes. | — |

> **Note:** The shared-ride variant (multiple passengers sharing one vehicle) would additionally require a `PassengerGroup` at the `on_confirm` stage to identify co-passengers. This is already covered by the existing `PassengerGroup` class.
