# Cab Rental — Lifecycle Stress Test

## Use Case Narrative

Meera is visiting Goa for three days. She wants a self-drive car for local exploration, or alternatively a cab with driver for an 8-hour package. She opens a rental app, selects "Cab Rental — 8 Hours / 80 km" as the package type, and sets the pickup point as her hotel. The app shows her available packages — Hatchback (₹1,200), Sedan (₹1,800), SUV (₹2,400) — each with a pricing plan that includes base package, extra km rate, and extra hour rate. She picks the Sedan, confirms for the next morning at 9 AM, and pays upfront. The driver arrives; the cab is at her service all day. At the end, she is billed for extra kms driven. She then rates the experience.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Meera | Consumer — the renter | Represented by BAP |
| Rental App | BAP — renders packages, handles booking | `beckn:BAP` |
| Rental Operator | BPP — manages cab fleet and packages | `beckn:BPP` |
| Driver | Fulfillment agent — chauffeurs Meera | `mobility:Driver` |

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Meera specifies her rental requirements — pickup location, start time, package type (8-hour/80-km), and vehicle preference.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`RideRequest`](../../schema/RideRequest/README.md) | Top-level intent with rental package context | `beckn:Intent` | ✅ |
| [`Place`](../../schema/Place/README.md) | Pickup location (hotel address) | `beckn:Location` | ✅ |
| [`VehicleCategory`](../../schema/VehicleCategory/README.md) | Preferred vehicle class (Sedan preferred) | `beckn:CategoryCode` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Passenger type (Adult) | `beckn:CategoryCode` | ✅ |

**Notes:** `RideRequest.requestedTime` is set to the next morning's 9 AM. The package type (8-hr / 80-km) is expressed through the search intent — the BPP interprets this and returns matching `SystemPricingPlan` entries. Unlike point-to-point rides, the destination is left open (Meera will choose routes throughout the day).

---

#### Action: `on_search`
**Semantic intent:** The BPP returns available rental packages with vehicle categories, base pricing plans, and overage rates.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`PlanningResult`](../../schema/PlanningResult/README.md) | Catalog container for rental packages | `beckn:Catalog` | ✅ |
| [`RideOption`](../../schema/RideOption/README.md) | Each vehicle category + package combination | `beckn:Offer` | ✅ |
| [`VehicleCategory`](../../schema/VehicleCategory/README.md) | Hatchback / Sedan / SUV class | `beckn:CategoryCode` | ✅ |
| [`SystemPricingPlan`](../../schema/SystemPricingPlan/README.md) | Rental pricing plan (base package + per-km + per-hour rates) | `beckn:Offer` | ✅ |
| [`FareEstimate`](../../schema/FareEstimate/README.md) | Estimated total for the base 8-hr / 80-km package | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Base package fee + fuel surcharge + platform fee | `beckn:PriceComponent` | ✅ |
| [`PricingModel`](../../schema/PricingModel/README.md) | Package model (base + per-km overage + per-hour overage) | `beckn:Offer` | ✅ |
| [`BookingRule`](../../schema/BookingRule/README.md) | Advance booking window for the rental | `beckn:Policy` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Rental cancellation terms | `beckn:CancellationPolicy` | ✅ |
| [`PickupPolicy`](../../schema/PickupPolicy/README.md) | Where the driver will meet Meera | `beckn:Policy` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | Driver waiting time at hotel at 9 AM | `beckn:Policy` | ✅ |
| [`Operator`](../../schema/Operator/README.md) | The rental fleet operator | `beckn:Provider` | ✅ |

**Notes:** `SystemPricingPlan` is the key class for cab rental — it captures `perKmChargingRate` (extra km rate), `perMinuteChargingRate` (extra hour rate beyond base package), and `perTripStartingFee` (base package). This is distinct from the instant ride `PricingModel` which is typically metered from the start.

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Meera selects the Sedan 8-hr package.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`RideOption`](../../schema/RideOption/README.md) | Selected rental package (by id) | `beckn:Offer` | ✅ |
| [`ServiceClass`](../../schema/ServiceClass/README.md) | Standard (not premium) tier | `beckn:CategoryCode` | ✅ |
| [`PickupPolicy`](../../schema/PickupPolicy/README.md) | Hotel lobby as pickup point | `beckn:Policy` | ✅ |

---

#### Action: `on_select`
**Semantic intent:** BPP confirms vehicle availability for the 9 AM slot and locks the package pricing.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`RideOption`](../../schema/RideOption/README.md) | Confirmed Sedan rental option | `beckn:Offer` | ✅ |
| [`SystemPricingPlan`](../../schema/SystemPricingPlan/README.md) | Locked package pricing with overage rates | `beckn:Offer` | ✅ |
| [`FareEstimate`](../../schema/FareEstimate/README.md) | Base package fare (₹1,800 for 8 hr / 80 km) | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Component breakdown (base + taxes) | `beckn:PriceComponent` | ✅ |
| [`Vehicle`](../../schema/Vehicle/README.md) | Vehicle type and fuel type confirmed | `beckn:Item` | ✅ |
| [`VehicleType`](../../schema/VehicleType/README.md) | Sedan type details | `beckn:CategoryCode` | ✅ |
| [`PickupPolicy`](../../schema/PickupPolicy/README.md) | Confirmed pickup at hotel lobby | `beckn:Policy` | ✅ |
| [`DropPolicy`](../../schema/DropPolicy/README.md) | Drop-off location constraints (return to base or anywhere) | `beckn:Policy` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | Waiting time limit at 9 AM | `beckn:Policy` | ✅ |

---

#### Action: `init`
**Semantic intent:** Meera submits her details and payment method.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rider`](../../schema/Rider/README.md) | Meera's identity and payment method | `beckn:Participant` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult passenger classification | `beckn:CategoryCode` | ✅ |

---

#### Action: `on_init`
**Semantic intent:** BPP returns the full rental contract terms — base fare, overage rates, and all policies — before payment confirmation.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Draft rental contract | `beckn:Contract` | ✅ |
| [`SystemPricingPlan`](../../schema/SystemPricingPlan/README.md) | Full pricing plan including overage rates | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Pre-payment fare breakup | `beckn:PriceComponent` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Rental cancellation terms | `beckn:CancellationPolicy` | ✅ |
| [`SafetyPolicy`](../../schema/SafetyPolicy/README.md) | Vehicle safety and insurance terms | `beckn:Policy` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | Confirmed waiting time policy | `beckn:Policy` | ✅ |

---

#### Action: `confirm`
**Semantic intent:** Meera pays the base package fare upfront and confirms the booking.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Rental order being confirmed | `beckn:Contract` | ✅ |
| [`Rider`](../../schema/Rider/README.md) | Confirming renter identity | `beckn:Participant` | ✅ |

---

#### Action: `on_confirm`
**Semantic intent:** BPP confirms the rental booking, assigns driver and vehicle, and returns the full rental contract.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Confirmed rental contract with binding terms | `beckn:Contract` | ✅ |
| [`Driver`](../../schema/Driver/README.md) | Assigned driver for the rental | `beckn:FulfillmentAgent` | ✅ |
| [`Vehicle`](../../schema/Vehicle/README.md) | Specific vehicle assigned (plate, make, model, color) | `beckn:Item` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | Driver's masked contact for Meera | `beckn:SupportInfo` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Confirmed base package breakup | `beckn:PriceComponent` | ✅ |
| [`SystemPricingPlan`](../../schema/SystemPricingPlan/README.md) | Binding overage rates for km/hour overages | `beckn:Offer` | ✅ |
| [`PickupDropoffPoint`](../../schema/PickupDropoffPoint/README.md) | Hotel lobby pickup with instructions | `beckn:FulfillmentStop` | ✅ |

---

### Stage 3 — Fulfillment

---

#### Action: `status`
**Semantic intent:** Meera's app checks the driver's status during the rental day.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Rental order being queried | `beckn:Contract` | ✅ |

---

#### Action: `on_status`
**Semantic intent:** BPP returns the current rental state — total kms driven so far, hours elapsed, and any overage accruing.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Running contract state with live km/hr summary | `beckn:Contract` | ✅ |
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Vehicle's current location | `beckn:Tracking` | ✅ |
| [`Event`](../../schema/Event/README.md) | `RENTAL_STARTED`, `OVERAGE_WARNING`, `RENTAL_COMPLETED` | `beckn:State` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Running fare (base + accruing overage) | `beckn:PriceComponent` | ✅ |
| [`Telemetry`](../../schema/Telemetry/README.md) | Odometer reading to calculate km consumed | `beckn:Tracking` | ✅ |

**Notes:** `TripUpdate.contractChanges` carries the updated km/hour count as a `ContractItem` modification — the running fare is reflected in `FareBreakup`. The `OVERAGE_WARNING` event alerts Meera that she is approaching the 80-km limit.

---

#### Action: `track`
**Semantic intent:** Meera checks vehicle location on the map.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Rental being tracked | `beckn:Contract` | ✅ |

---

#### Action: `on_track`
**Semantic intent:** BPP returns vehicle position feed.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Live coordinates and speed of the rented vehicle | `beckn:Tracking` | ✅ |
| [`Telemetry`](../../schema/Telemetry/README.md) | Odometer + speed + fuel level (if available) | `beckn:Tracking` | ✅ |

---

#### Action: `update` (extra kms accrued, end-of-rental settlement)
**Semantic intent:** At the end of the rental, the BPP triggers an update to add the overage charges (22 extra km = ₹220 extra).

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Contract amendment with overage line item | `beckn:Contract` | ✅ |

---

#### Action: `on_update`
**Semantic intent:** BPP returns the final rental fare including overage charges.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | Final contract state with overage applied | `beckn:Contract` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final fare: base ₹1,800 + overage ₹220 + taxes | `beckn:PriceComponent` | ✅ |

---

#### Action: `cancel`
**Semantic intent:** Meera cancels the rental the evening before pickup.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Rental order being cancelled | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Policy governing cancellation terms | `beckn:CancellationPolicy` | ✅ |

---

#### Action: `on_cancel`
**Semantic intent:** BPP applies cancellation policy and issues a receipt.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Cancelled contract | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Applied policy with refund amount | `beckn:CancellationPolicy` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Cancellation receipt with refund details | `beckn:Invoice` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Net settlement after cancellation fee | `beckn:PriceComponent` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`
**Semantic intent:** Meera rates the 8-hour experience — driver, vehicle cleanliness, and overall service.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | Overall 4-star rating (ratedEntityType: SERVICE) | `beckn:RatingInput` | ✅ |
| [`Rating`](../../schema/Rating/README.md) | Separate driver rating (ratedEntityType: DRIVER) | `beckn:RatingInput` | ✅ |
| [`Rating`](../../schema/Rating/README.md) | Vehicle cleanliness rating (ratedEntityType: VEHICLE) | `beckn:RatingInput` | ✅ |
| [`Review`](../../schema/Review/README.md) | "Great car, helpful driver" free-text review | `beckn:RatingInput` | ✅ |
| [`Feedback`](../../schema/Feedback/README.md) | Tags: CLEAN_VEHICLE, HELPFUL_DRIVER | `beckn:Feedback` | ✅ |

**Notes:** Cab rental supports multi-entity rating — the rider can separately rate the driver, the vehicle, and the overall service. `Rating.ratedEntityType` distinguishes these. All three use the same `Rating` class.

---

#### Action: `on_rating`
**Semantic intent:** BPP acknowledges all ratings.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | Acknowledged ratings | `beckn:RatingInput` | ✅ |

---

#### Action: `support`
**Semantic intent:** Meera found that the final bill seems higher than expected and raises a billing dispute.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Billing dispute support case | `beckn:SupportRequest` | ✅ |

---

#### Action: `on_support`
**Semantic intent:** BPP provides support contact and confirms receipt details.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Updated case with ticket ID | `beckn:SupportRequest` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Itemised receipt showing km overage calculation | `beckn:Invoice` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Detailed overage calculation for Meera's review | `beckn:PriceComponent` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | Support team contact | `beckn:SupportInfo` | ✅ |

---

## Coverage Summary

| Class | Actions Used In | Lifecycle Stage |
|-------|----------------|----------------|
| `RideRequest` | search | Discovery |
| `Place` | search | Discovery |
| `VehicleCategory` | search, on_search, select | Discovery, Contracting |
| `RiderCategory` | search, init | Discovery, Contracting |
| `PlanningResult` | on_search | Discovery |
| `RideOption` | on_search, select, on_select | Discovery, Contracting |
| `SystemPricingPlan` | on_search, on_select, on_init, on_confirm | Discovery, Contracting |
| `FareEstimate` | on_search, on_select | Discovery, Contracting |
| `FareBreakup` | on_search, on_select, on_init, on_confirm, on_status, on_update, on_cancel, on_support | All stages |
| `PricingModel` | on_search | Discovery |
| `BookingRule` | on_search | Discovery |
| `CancellationPolicy` | on_search, on_init, cancel, on_cancel | Contracting, Fulfillment |
| `PickupPolicy` | on_search, select, on_select | Discovery, Contracting |
| `WaitingPolicy` | on_search, on_select, on_init | Contracting |
| `DropPolicy` | on_select | Contracting |
| `Operator` | on_search | Discovery |
| `ServiceClass` | select | Contracting |
| `Vehicle` | on_select, on_confirm | Contracting |
| `VehicleType` | on_select | Contracting |
| `Rider` | init, confirm | Contracting |
| `Trip` | on_init, confirm, on_confirm, status, track, update, cancel, on_cancel | Contracting, Fulfillment |
| `SafetyPolicy` | on_init | Contracting |
| `Driver` | on_confirm | Contracting |
| `ContactHandle` | on_confirm, on_support | Contracting, Post-Fulfillment |
| `PickupDropoffPoint` | on_confirm | Contracting |
| `TripUpdate` | on_status, update, on_update | Fulfillment |
| `VehiclePosition` | on_status, on_track | Fulfillment |
| `Event` | on_status | Fulfillment |
| `Telemetry` | on_status, on_track | Fulfillment |
| `Receipt` | on_cancel, on_support | Fulfillment, Post-Fulfillment |
| `Rating` | rating, on_rating | Post-Fulfillment |
| `Review` | rating | Post-Fulfillment |
| `Feedback` | rating | Post-Fulfillment |
| `SupportCase` | support, on_support | Post-Fulfillment |

---

## Gap Report

| Gap | Description | Severity |
|-----|-------------|----------|
| No gaps detected | All schema classes required for the cab rental lifecycle exist in the mobility schema. `SystemPricingPlan` correctly captures the package + overage pricing model; `Telemetry.odometer` supports km tracking; `TripUpdate.contractChanges` supports overage amendment. | — |

> **Design note:** The key semantic distinction between cab rental and instant ride hailing is the pricing model: rentals use a **time-bounded package** (base fee + overage) captured by `SystemPricingPlan`, whereas instant rides use a **per-trip metered or upfront-quoted** fare captured by `PricingModel`. Both classes exist in the schema.
