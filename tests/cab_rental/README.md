# Cab Rental — Lifecycle Stress Test

## Use Case Narrative

Meera is in Goa for three days and wants a cab for the full day — 8 hours / 80 km package. She opens a rental app, enters her hotel GPS location as pickup, and requests a 9 AM start. The app shows Hatchback (₹1,200), Sedan (₹1,800), SUV (₹2,400) packages with per-km and per-hour overage rates. She picks the Sedan with insurance, sees the toll preference form, selects non-toll, pays online, and confirms. The driver is assigned shortly after confirmation and the OTP arrives. At end of day, extra kms are billed. She rates the service.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Meera | Consumer — renter | Represented by BAP |
| Rental App | BAP — renders packages | `beckn:BAP` |
| Rental Operator | BPP — fleet and package management | `beckn:BPP` |
| Driver | Fulfillment agent — chauffeurs Meera for 8 hrs | `mobility:Driver` |

> **Key differentiator from instant ride hailing:** Rental uses a time-and-distance package (`SystemPricingPlan`) instead of a per-trip metered or upfront quote (`PricingModel`). The destination is OPEN at search time. Overage charges are added via `on_update` at trip end.

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Meera specifies pickup GPS, start time, package type (8-hr/80-km), and vehicle preference.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Top-level rental intent | [`RideRequest`](../../schema/RideRequest/README.md) | `requestedTime: 9 AM` (no fixed destination) | ✅ |
| Pickup GPS (hotel) | [`Place`](../../schema/Place/README.md) | `gps`, `placeName` | ✅ |
| Preferred vehicle class | [`VehicleCategory`](../../schema/VehicleCategory/README.md) | `vehicleCategoryCode` | ✅ |
| Passenger type | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId` | ✅ |

**Notes:** No `destination` in rental search — Meera's routes are open. The BPP returns packages based on pickup location and time. Drop is wherever Meera ends the rental.

---

#### Action: `on_search`
**Semantic intent:** BPP returns rental packages — base package price, overage rates, vehicle features.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Catalog container | [`PlanningResult`](../../schema/PlanningResult/README.md) | — | ✅ |
| Each rental package (Hatchback/Sedan/SUV) | [`RideOption`](../../schema/RideOption/README.md) | `vehicleType`, `pricingModel` | ✅ |
| Vehicle class | [`VehicleCategory`](../../schema/VehicleCategory/README.md) | `vehicleCategoryCode` | ✅ |
| Vehicle type (capacity, fuel) | [`VehicleType`](../../schema/VehicleType/README.md) | `maxCapacity`, `propulsionType` | ✅ |
| Boot space | [`VehicleType`](../../schema/VehicleType/README.md) | `tags` | ⚠️ |
| A/C availability | [`VehicleType`](../../schema/VehicleType/README.md) | `tags` | ⚠️ |
| Insurance add-on | [`AncillaryService`](../../schema/AncillaryService/README.md) | `serviceCode: INSURANCE` | ✅ |
| Base package fare estimate | [`FareEstimate`](../../schema/FareEstimate/README.md) | `estimatedAmount: ₹1,800` (8hr/80km) | ✅ |
| Fare breakdown (base + taxes) | [`FareBreakup`](../../schema/FareBreakup/README.md) | `componentTitle`, `amount` | ✅ |
| **Rental pricing plan with overage rates** | [`SystemPricingPlan`](../../schema/SystemPricingPlan/README.md) | `perTripStartingFee: 1800`, `perKmChargingRate: 10`, `perMinuteChargingRate: 2` | ✅ |
| General pricing model type | [`PricingModel`](../../schema/PricingModel/README.md) | `modelType: PACKAGE` | ✅ |
| Booking window | [`BookingRule`](../../schema/BookingRule/README.md) | `latestBookingTime`, `priorNoticeDurationMin` | ✅ |
| Cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `cancellationTerms` | ✅ |
| Waiting policy | [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | `freeWaitingTimeMinutes` | ✅ |
| Operator details | [`Operator`](../../schema/Operator/README.md) | `operatorId` | ✅ |

**Notes:** `SystemPricingPlan` is the **key differentiator** for rental. It captures the base package (`perTripStartingFee`), the extra km rate (`perKmChargingRate`), and the extra hour rate (`perMinuteChargingRate`). This is distinct from `PricingModel` which describes instant ride metering.

---

### Stage 2 — Contracting

---

#### Action: `select`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Selected Sedan rental package | [`RideOption`](../../schema/RideOption/README.md) | `id` | ✅ |
| Exact GPS pickup (hotel lobby) | [`Place`](../../schema/Place/README.md) | `gps`, `placeName` | ✅ |
| No fixed destination (open rental) | — | `destination: null` | ✅ |
| Service tier | [`ServiceClass`](../../schema/ServiceClass/README.md) | `serviceClassCode: STANDARD` | ✅ |
| Insurance add-on selected | [`AncillaryService`](../../schema/AncillaryService/README.md) | `serviceCode: INSURANCE` | ✅ |
| Pickup meet-point | [`PickupPolicy`](../../schema/PickupPolicy/README.md) | `pickupConditions: HOTEL_LOBBY` | ✅ |

---

#### Action: `on_select`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed Sedan rental option | [`RideOption`](../../schema/RideOption/README.md) | `id`, `estimatedArrival: 9 AM` | ✅ |
| **Locked rental pricing plan** | [`SystemPricingPlan`](../../schema/SystemPricingPlan/README.md) | Base ₹1,800 + ₹10/km overage + ₹2/min overage | ✅ |
| Base fare estimate | [`FareEstimate`](../../schema/FareEstimate/README.md) | `estimatedAmount: ₹1,800` | ✅ |
| Fare breakdown | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base package + taxes | ✅ |
| Vehicle type | [`VehicleType`](../../schema/VehicleType/README.md) | `vehicleTypeCode` | ✅ |
| Pickup policy confirmed | [`PickupPolicy`](../../schema/PickupPolicy/README.md) | `allowedPickupAreas` | ✅ |
| Drop policy (return to base or anywhere) | [`DropPolicy`](../../schema/DropPolicy/README.md) | `dropConditions` | ✅ |
| Waiting policy | [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | `freeWaitingTimeMinutes` | ✅ |

---

#### Action: `init`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Billing participant | [`Rider`](../../schema/Rider/README.md) | `riderId`, phone, `preferredPaymentMethod` | ✅ |
| Passenger type | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId` | ✅ |

---

#### Action: `on_init`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Draft rental contract | [`Trip`](../../schema/Trip/README.md) | `tripId`, `startTime: 9 AM` | ✅ |
| **Full rental pricing plan (binding)** | [`SystemPricingPlan`](../../schema/SystemPricingPlan/README.md) | All overage rates locked | ✅ |
| Pre-payment fare breakdown | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base + insurance + taxes | ✅ |
| Cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Binding | ✅ |
| Safety and insurance terms | [`SafetyPolicy`](../../schema/SafetyPolicy/README.md) | `insuranceCoverage` | ✅ |
| Waiting policy | [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | `freeWaitingTimeMinutes` | ✅ |
| **Toll/non-toll route form** | ❌ No dedicated class | — | ❌ |
| Payment channel options | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags` | ⚠️ |

---

#### Action: `confirm`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Rental confirmed with payment | [`Trip`](../../schema/Trip/README.md) | `tripId` | ✅ |
| Route preference selected | ❌ No dedicated class | — | ❌ |
| Payment channel selected | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags: PAYMENT_CHANNEL=ONLINE` | ⚠️ |
| Payment reference | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags: PAYMENT_REF` | ⚠️ |

---

#### Action: `on_confirm`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed rental booking contract | [`Trip`](../../schema/Trip/README.md) | `tripId`, `startTime: 9 AM` | ✅ |
| Exact pickup GPS | [`Place`](../../schema/Place/README.md) | `gps` | ✅ |
| Confirmed rental package + insurance | [`RideOption`](../../schema/RideOption/README.md) | `id` | ✅ |
| Billing participant | [`Rider`](../../schema/Rider/README.md) | `riderId` | ✅ |
| Base package fare breakup | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base + insurance + taxes | ✅ |
| **Binding rental pricing plan** | [`SystemPricingPlan`](../../schema/SystemPricingPlan/README.md) | Overage rates Meera agreed to | ✅ |
| Cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Binding | ✅ |
| **Driver allocation status — SEARCHING** | [`Event`](../../schema/Event/README.md) | `eventType: DRIVER_ALLOCATION_SEARCHING` | ✅ |
| Pickup meet-point | [`PickupDropoffPoint`](../../schema/PickupDropoffPoint/README.md) | `landmark: HOTEL_LOBBY` | ✅ |
| Platform support contact | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE` | ✅ |

---

### Stage 3 — Fulfillment

---

#### Action: `on_update` *(BPP-initiated push — driver assigned + rental started)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Full updated rental contract | [`Trip`](../../schema/Trip/README.md) | `state: DRIVER_ASSIGNED`, `startTime: 9 AM` | ✅ |
| Pickup GPS | [`Place`](../../schema/Place/README.md) | `gps` | ✅ |
| Rental package + insurance | [`RideOption`](../../schema/RideOption/README.md) | `id` | ✅ |
| Billing participant | [`Rider`](../../schema/Rider/README.md) | `riderId` | ✅ |
| Base fare + overage rates | [`SystemPricingPlan`](../../schema/SystemPricingPlan/README.md) | All rates | ✅ |
| Fare breakup | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base + taxes | ✅ |
| **Assigned driver details** | [`Driver`](../../schema/Driver/README.md) | `licenseNumber`, `yearsOfExperience` | ✅ |
| **Assigned vehicle** | [`Vehicle`](../../schema/Vehicle/README.md) | `licensePlate`, `make`, `model`, `color` | ✅ |
| **Driver live location** | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude` | ✅ |
| **Driver masked contact** | [`ContactHandle`](../../schema/ContactHandle/README.md) | masked phone | ✅ |
| **Tracking ACTIVE** | [`TripUpdate`](../../schema/TripUpdate/README.md) | `trackingEndpoint.status: ACTIVE` | ✅ |
| Booking status | [`Event`](../../schema/Event/README.md) | `eventType: RENTAL_STARTED` | ✅ |
| **Rental start OTP** | ❌ No dedicated mobility class | `beckn:Fulfillment.start.authorization` | ❌ |

---

#### Action: `status` *(mid-day — km/hr usage check)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Running rental contract state | [`TripUpdate`](../../schema/TripUpdate/README.md) | `contractChanges` (km used), `stateUpdate` | ✅ |
| Current vehicle location | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude` | ✅ |
| Odometer reading (km consumed) | [`Telemetry`](../../schema/Telemetry/README.md) | `odometer` | ✅ |
| Running fare (base + accruing overage) | [`FareBreakup`](../../schema/FareBreakup/README.md) | Updated total | ✅ |
| Overage warning event | [`Event`](../../schema/Event/README.md) | `eventType: OVERAGE_WARNING` | ✅ |

---

#### Action: `update` / `on_update` *(end of rental — overage settlement)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Contract amendment — overage charges | [`TripUpdate`](../../schema/TripUpdate/README.md) | `contractChanges` (22 extra km) | ✅ |
| Final fare: base + overage | [`FareBreakup`](../../schema/FareBreakup/README.md) | ₹1,800 base + ₹220 overage + taxes | ✅ |
| Rental completion event | [`Event`](../../schema/Event/README.md) | `eventType: RENTAL_COMPLETED` | ✅ |

---

#### Action: `cancel`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Cancellation | [`Trip`](../../schema/Trip/README.md) | `tripId` | ✅ |
| Applied policy | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `refundPercentage` | ✅ |
| Refund receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Driver rating | [`Rating`](../../schema/Rating/README.md) | `ratingValue`, `ratedEntityType: DRIVER` | ✅ |
| Vehicle rating | [`Rating`](../../schema/Rating/README.md) | `ratingValue`, `ratedEntityType: VEHICLE` | ✅ |
| Service rating | [`Rating`](../../schema/Rating/README.md) | `ratingValue`, `ratedEntityType: SERVICE` | ✅ |
| Review text | [`Review`](../../schema/Review/README.md) | `reviewText` | ✅ |
| Feedback tags | [`Feedback`](../../schema/Feedback/README.md) | `feedbackType` | ✅ |

---

#### Action: `support` *(billing dispute — overage seemed wrong)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Billing dispute case | [`SupportCase`](../../schema/SupportCase/README.md) | `caseType: COMPLAINT` | ✅ |
| Itemised receipt with overage calculation | [`Receipt`](../../schema/Receipt/README.md) | all `FareBreakup` components + `SystemPricingPlan` rates | ✅ |
| Support contact | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE` | ✅ |

---

## Gap Report

*(Same gaps as Ride Hailing — this use case inherits all three gaps.)*

| # | Gap | Description | Severity |
|---|-----|-------------|----------|
| 1 | **VehicleFeature** | Boot space, A/C not structured properties in `VehicleType` | Medium |
| 2 | **RoutePreference** | No class for toll/non-toll form in `on_init` | Medium |
| 3 | **FulfillmentAuthorization** | Rental-start OTP not explicitly surfaced in `Trip` class | Medium |

> **Design note:** The core semantic distinction between rental and instant ride hailing is the **pricing model**: rentals use `SystemPricingPlan` (base package + per-km + per-hour overage), while instant rides use `PricingModel` (metered or upfront-quoted per trip). Both classes exist in the schema and are mutually exclusive.
