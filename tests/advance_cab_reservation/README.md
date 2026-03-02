# Advance Cab Reservation — Lifecycle Stress Test

## Use Case Narrative

Arjun has a 6 AM flight tomorrow. He opens a cab app the night before, sets his GPS home location as pickup, the airport terminal as destination, and requests pickup at 3:30 AM. The app returns available options with fixed advance-booking fares (no surge). He picks a Sedan with insurance, chooses non-toll route, pays online and confirms. The platform acknowledges with "BOOKING CONFIRMED — DRIVER WILL BE ASSIGNED BY 2:45 AM". At 2:45 AM the driver is assigned — Arjun gets the driver's name, vehicle plate, live location, and OTP. He lands safely and later requests a reimbursement receipt.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Arjun | Consumer — advance-booking traveler | Represented by BAP |
| Cab App | BAP — renders options, relays selections | `beckn:BAP` |
| Cab Aggregator | BPP — manages fleet, pre-booking slots, pricing | `beckn:BPP` |
| Driver | Fulfillment agent — assigned ~45 min before pickup | `mobility:Driver` |

> **Key differentiator from instant ride hailing:** `RideRequest.requestedTime` is set to a FUTURE timestamp (3:30 AM). Everything else in the lifecycle is structurally identical to ride hailing — with the critical addition of `BookingRule` and `NoShowPolicy` in the catalog, and the deferred driver assignment pattern (driver assigned close to pickup time, not immediately after `on_confirm`).

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Arjun expresses his advance booking intent — GPS pickup, future pickup time, GPS destination.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Top-level advance intent | [`RideRequest`](../../schema/RideRequest/README.md) | `requestedTime: "2026-02-04T03:30:00+05:30"` | ✅ |
| Pickup GPS (home) | [`Place`](../../schema/Place/README.md) | `gps`, `placeName` | ✅ |
| Destination GPS (airport terminal) | [`Place`](../../schema/Place/README.md) | `gps`, `placeType: AIRPORT` | ✅ |
| Preferred vehicle class (Sedan) | [`VehicleCategory`](../../schema/VehicleCategory/README.md) | `vehicleCategoryCode` | ✅ |
| Passenger type | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId` | ✅ |
| Number of passengers | [`PassengerGroup`](../../schema/PassengerGroup/README.md) | `groupSize` | ✅ |

**Notes:** `RideRequest.requestedTime` carries the future pickup time. The BPP MUST interpret a non-null, future `requestedTime` as an advance reservation request and apply advance-booking pricing (no surge for off-peak slots).

---

#### Action: `on_search`
**Semantic intent:** BPP returns advance-booking options with fixed fares, booking window rules, and no-show terms.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Catalog container | [`PlanningResult`](../../schema/PlanningResult/README.md) | — | ✅ |
| Each advance ride product | [`RideOption`](../../schema/RideOption/README.md) | `estimatedArrival`, `pricingModel` | ✅ |
| Vehicle class | [`VehicleCategory`](../../schema/VehicleCategory/README.md) | `vehicleCategoryCode` | ✅ |
| Vehicle type details | [`VehicleType`](../../schema/VehicleType/README.md) | `maxCapacity`, `propulsionType` | ✅ |
| Boot space | [`VehicleType`](../../schema/VehicleType/README.md) | `tags` | ⚠️ |
| Insurance add-on | [`AncillaryService`](../../schema/AncillaryService/README.md) | `serviceCode: INSURANCE` | ✅ |
| Fixed advance fare estimate | [`FareEstimate`](../../schema/FareEstimate/README.md) | `estimatedAmount` (no range — fixed) | ✅ |
| Fare breakdown | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base fare, toll estimate, platform fee | ✅ |
| Fixed pricing model | [`PricingModel`](../../schema/PricingModel/README.md) | `modelType: FIXED` | ✅ |
| **Advance booking window rules** | [`BookingRule`](../../schema/BookingRule/README.md) | `latestBookingTime`, `earliestBookingTime`, `priorNoticeDurationMin` | ✅ |
| Waiting policy at 3:30 AM | [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | `freeWaitingTimeMinutes` | ✅ |
| Advance cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Tiered: 100% >4h, 50% 2–4h, 0% <2h | ✅ |
| **No-show fee (airport run critical)** | [`NoShowPolicy`](../../schema/NoShowPolicy/README.md) | `noShowFee`, `gracePeriodMinutes: 5` | ✅ |
| Operator details | [`Operator`](../../schema/Operator/README.md) | `operatorId` | ✅ |

---

### Stage 2 — Contracting

*(All contracting actions are identical to Ride Hailing. Key addition: `BookingRule` persists through select → on_init.)*

---

#### Action: `select`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Selected Sedan option | [`RideOption`](../../schema/RideOption/README.md) | `id` | ✅ |
| Exact GPS pickup (home gate) | [`Place`](../../schema/Place/README.md) | `gps`, `placeName` | ✅ |
| Exact GPS drop (departure terminal) | [`Place`](../../schema/Place/README.md) | `gps`, `placeType: AIRPORT` | ✅ |
| Service tier | [`ServiceClass`](../../schema/ServiceClass/README.md) | `serviceClassCode: PREMIUM` | ✅ |
| Insurance add-on | [`AncillaryService`](../../schema/AncillaryService/README.md) | `serviceCode: INSURANCE` | ✅ |
| Pickup instructions at 3:30 AM | [`PickupPolicy`](../../schema/PickupPolicy/README.md) | `pickupConditions` | ✅ |

---

#### Action: `on_select`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed 3:30 AM slot guaranteed | [`RideOption`](../../schema/RideOption/README.md) | `estimatedArrival: 3:30 AM` | ✅ |
| Locked advance fare | [`FareEstimate`](../../schema/FareEstimate/README.md) | `estimatedAmount` (fixed, no range) | ✅ |
| Fare breakdown | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base + toll + fee | ✅ |
| Vehicle type details | [`VehicleType`](../../schema/VehicleType/README.md) | `vehicleTypeCode` | ✅ |
| Confirmed booking window | [`BookingRule`](../../schema/BookingRule/README.md) | `latestBookingTime` | ✅ |
| Waiting policy | [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | `freeWaitingTimeMinutes` | ✅ |
| Airport drop zone rules | [`DropPolicy`](../../schema/DropPolicy/README.md) | `dropConditions: DEPARTURE_TERMINAL_ONLY` | ✅ |

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
| Draft advance booking contract | [`Trip`](../../schema/Trip/README.md) | `tripId`, `startTime: 3:30 AM` | ✅ |
| Final fare before payment | [`FareBreakup`](../../schema/FareBreakup/README.md) | All components | ✅ |
| Advance cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Tiered refund schedule | ✅ |
| No-show fee (binding) | [`NoShowPolicy`](../../schema/NoShowPolicy/README.md) | `noShowFee` | ✅ |
| Waiting terms at airport run | [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | `freeWaitingTimeMinutes: 5` | ✅ |
| Safety policy | [`SafetyPolicy`](../../schema/SafetyPolicy/README.md) | `emergencyContact` | ✅ |
| **Toll/non-toll route form** | ❌ No dedicated class | — | ❌ |
| Payment channel options | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags` | ⚠️ |

---

#### Action: `confirm`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Order confirmed with payment | [`Trip`](../../schema/Trip/README.md) | `tripId` | ✅ |
| Route preference selected | ❌ No dedicated class | — | ❌ |
| Payment channel selected | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags: PAYMENT_CHANNEL=ONLINE` | ⚠️ |
| Payment reference | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags: PAYMENT_REF` | ⚠️ |

---

#### Action: `on_confirm`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed advance booking contract | [`Trip`](../../schema/Trip/README.md) | `tripId`, `startTime: 3:30 AM` | ✅ |
| Pickup GPS | [`Place`](../../schema/Place/README.md) | `gps` | ✅ |
| Drop GPS | [`Place`](../../schema/Place/README.md) | `gps` | ✅ |
| Confirmed ride offer + insurance | [`RideOption`](../../schema/RideOption/README.md) | `id` | ✅ |
| Fare estimate + breakup | [`FareBreakup`](../../schema/FareBreakup/README.md) | All components | ✅ |
| Cancellation and no-show terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Binding | ✅ |
| **Driver status: WILL BE ASSIGNED BY 2:45 AM** | [`Event`](../../schema/Event/README.md) | `eventType: DRIVER_ALLOCATION_DEFERRED` | ✅ |
| Platform support contact | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE` | ✅ |
| Pickup meet-point | [`PickupDropoffPoint`](../../schema/PickupDropoffPoint/README.md) | `landmark`, `accessNotes` | ✅ |

> **⚠️ Deferred driver assignment:** Unlike instant ride hailing, advance bookings do NOT search for a driver immediately. The BPP stores the booking and triggers driver assignment ~30–45 minutes before the pickup slot. `on_confirm` returns `Event.eventType: DRIVER_ALLOCATION_DEFERRED` with the expected assignment time (e.g., 2:45 AM).

---

### Stage 3 — Fulfillment

---

#### Action: `on_update` *(BPP-initiated push at 2:45 AM — driver assigned)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Full updated contract | [`Trip`](../../schema/Trip/README.md) | `state: DRIVER_ASSIGNED` | ✅ |
| Pickup + drop GPS | [`Place`](../../schema/Place/README.md) | `gps` | ✅ |
| Confirmed ride offer | [`RideOption`](../../schema/RideOption/README.md) | `id` | ✅ |
| Billing participant | [`Rider`](../../schema/Rider/README.md) | `riderId` | ✅ |
| Fare breakup | [`FareBreakup`](../../schema/FareBreakup/README.md) | All components | ✅ |
| **Assigned driver** | [`Driver`](../../schema/Driver/README.md) | `licenseNumber`, `yearsOfExperience` | ✅ |
| **Driver rating** | [`Driver`](../../schema/Driver/README.md) | via `beckn:FulfillmentAgent.rating` | ✅ |
| **Assigned vehicle** | [`Vehicle`](../../schema/Vehicle/README.md) | `licensePlate`, `make`, `model`, `color` | ✅ |
| **Driver current location** | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude` | ✅ |
| **Driver masked contact** | [`ContactHandle`](../../schema/ContactHandle/README.md) | masked phone | ✅ |
| **Tracking ACTIVE** | [`TripUpdate`](../../schema/TripUpdate/README.md) | `trackingEndpoint.status: ACTIVE` | ✅ |
| Driver assignment event | [`Event`](../../schema/Event/README.md) | `eventType: DRIVER_ASSIGNED` | ✅ |
| **Ride start OTP** | ❌ No dedicated mobility class | `beckn:Fulfillment.start.authorization` | ❌ |

---

#### Action: `track` / `status`

*(Identical to ride hailing — see ride hailing stress test)*

---

#### Action: `cancel` *(6 hours before — full refund)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Cancellation request | [`Trip`](../../schema/Trip/README.md) | `tripId` | ✅ |
| Applied advance policy (full refund) | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `refundPercentage: 100` | ✅ |
| Refund receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `support` *(invoice for employer reimbursement)*

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Invoice request support case | [`SupportCase`](../../schema/SupportCase/README.md) | `caseType: INVOICE_REQUEST` | ✅ |
| Itemised receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId`, all `FareBreakup` components | ✅ |
| Support contact | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE` | ✅ |

---

## Gap Report

*(Same gaps as Ride Hailing — this use case inherits all three gaps.)*

| # | Gap | Description | Severity |
|---|-----|-------------|----------|
| 1 | **VehicleFeature** | Boot space, A/C not structured in `VehicleType` | Medium |
| 2 | **RoutePreference** | No class for toll/non-toll form in `on_init` | Medium |
| 3 | **FulfillmentAuthorization** | Ride-start OTP not surfaced in `Trip` class | Medium |
