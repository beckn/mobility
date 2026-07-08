# Ride Hailing — Lifecycle Stress Test

## Use Case Narrative

Priya opens a ride-hailing app on her phone. She sets her current GPS location as pickup and drops a pin on her office as destination. The app shows several ride options — Auto, Mini, Sedan — each with an estimated fare and ETA. She selects a Mini with an insurance add-on, sees the fare breakup with surge pricing applied, is asked to choose toll vs non-toll route, selects online payment, and confirms the booking. The BPP acknowledges the booking and starts searching for a driver. Shortly after, a driver is assigned — the app shows his name, rating, vehicle plate, and current live location, along with the ride-start OTP. She completes the ride and receives a receipt. Later she rates the driver and raises a support case for a lost umbrella.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Priya | Consumer — the person requesting the ride | Represented by BAP |
| MaaS App | BAP — renders options, relays decisions | `beckn:BAP` |
| Ride Platform | BPP — manages driver supply, dispatching, pricing | `beckn:BPP` |
| Driver | Fulfillment agent | `mobility:Driver` |

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Priya expresses her ride intent — exact GPS pickup location, exact GPS drop location, and preferences.

**Information in message (BAP → BPP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Top-level intent | [`RideRequest`](../../schema/RideRequest/README.md) | — | ✅ |
| Pickup GPS coordinates | [`Place`](../../schema/Place/README.md) | `gps` (via beckn:Location) | ✅ |
| Pickup place name | [`Place`](../../schema/Place/README.md) | `placeName` | ✅ |
| Drop GPS coordinates | [`Place`](../../schema/Place/README.md) | `gps` (via beckn:Location) | ✅ |
| Drop place name | [`Place`](../../schema/Place/README.md) | `placeName` | ✅ |
| Preferred vehicle class | [`VehicleCategory`](../../schema/VehicleCategory/README.md) | `vehicleCategoryCode` | ✅ |
| Passenger type (Adult) | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId` | ✅ |
| Number of passengers | [`PassengerGroup`](../../schema/PassengerGroup/README.md) | `groupSize` | ✅ |

**Notes:** `Place.gps` carries the raw GPS string (lat,lon). `RideRequest.origin` and `.destination` embed two `Place` instances. The BAP sends exact GPS at search time — the BPP uses this to compute ETAs and check serviceability.

---

#### Action: `on_search`
**Semantic intent:** The BPP returns available ride products, vehicle features, driver platform features, insurance add-ons, and pricing.

**Information in message (BPP → BAP):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Catalog container | [`PlanningResult`](../../schema/PlanningResult/README.md) | — | ✅ |
| Each ride product (Auto / Mini / Sedan) | [`RideOption`](../../schema/RideOption/README.md) | — | ✅ |
| Vehicle class for each option | [`VehicleCategory`](../../schema/VehicleCategory/README.md) | `vehicleCategoryCode` | ✅ |
| Vehicle type details (capacity, fuel) | [`VehicleType`](../../schema/VehicleType/README.md) | `maxCapacity`, `propulsionType`, `wheelchairAccessible` | ✅ |
| Boot space / luggage capacity | [`VehicleType`](../../schema/VehicleType/README.md) | `tags` (inherited) | ⚠️ |
| A/C availability | [`VehicleType`](../../schema/VehicleType/README.md) | `tags` (inherited) | ⚠️ |
| Platform rating / driver quality indicator | [`Operator`](../../schema/Operator/README.md) | `rating` (inherited) | ✅ |
| Insurance add-on option | [`AncillaryService`](../../schema/AncillaryService/README.md) | `serviceCode`, `serviceCategory` | ✅ |
| Fare estimate (min–max range) | [`FareEstimate`](../../schema/FareEstimate/README.md) | `estimatedAmount`, `minimumAmount`, `maximumAmount` | ✅ |
| Fare component breakdown | [`FareBreakup`](../../schema/FareBreakup/README.md) | `componentTitle`, `amount` | ✅ |
| Surge multiplier (if applied) | [`SurgeMultiplier`](../../schema/SurgeMultiplier/README.md) | `multiplierValue`, `reason` | ✅ |
| Pricing model (metered vs upfront) | [`PricingModel`](../../schema/PricingModel/README.md) | `modelType`, `baseRate`, `perKmRate`, `perMinuteRate` | ✅ |
| Waiting time policy | [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | `freeWaitingTimeMinutes`, `chargePerExtraMinute` | ✅ |
| Cancellation terms at discovery | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `cancellationTerms`, `refundPercentage` | ✅ |
| Platform/operator details | [`Operator`](../../schema/Operator/README.md) | `operatorId`, `operatingRegions` | ✅ |
| ETA to pickup | [`RideOption`](../../schema/RideOption/README.md) | `estimatedArrival` | ✅ |

**⚠️ Notes on vehicle features:** `VehicleType` does not have explicit properties for `bootSpace` or `hasAC`. These are currently expressed via inherited `tags` from `beckn:Item`. A dedicated `VehicleFeature` class (following the `BikeAllowed` pattern) would provide cleaner semantics. **Identified Gap #1: no structured vehicle feature class beyond `BikeAllowed`.**

**Notes on driver features:** At catalog (search) time, individual driver details are NOT available — only platform-level quality indicators. Driver details arrive at `on_update` after assignment. `Operator.rating` covers platform-level aggregated quality.

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Priya selects the Mini option, provides her EXACT GPS pickup and drop locations (possibly refined from search), and selects any add-ons.

**This action initiates the CONTRACT. The BAP sends:**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Selected ride product | [`RideOption`](../../schema/RideOption/README.md) | `id` | ✅ |
| Exact GPS pickup location | [`Place`](../../schema/Place/README.md) | `gps`, `placeName` | ✅ |
| Exact GPS drop location | [`Place`](../../schema/Place/README.md) | `gps`, `placeName` | ✅ |
| Service tier (Economy/Premium) | [`ServiceClass`](../../schema/ServiceClass/README.md) | `serviceClassCode` | ✅ |
| Insurance add-on selected | [`AncillaryService`](../../schema/AncillaryService/README.md) | `serviceCode: INSURANCE` | ✅ |
| Pickup meet-point preference | [`PickupPolicy`](../../schema/PickupPolicy/README.md) | `pickupConditions` | ✅ |

**Notes:** The exact GPS from `select` may differ from search (e.g., Priya walked to the actual pickup gate). The BPP MUST re-compute ETA and serviceability with the refined coordinates.

---

#### Action: `on_select`
**Semantic intent:** The BPP confirms the exact pickup/drop is serviceable, locks the fare, and returns the contract draft.

**BPP returns everything from `select` PLUS:**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Locked fare estimate | [`FareEstimate`](../../schema/FareEstimate/README.md) | `estimatedAmount`, `currency` | ✅ |
| Fare component breakdown | [`FareBreakup`](../../schema/FareBreakup/README.md) | Base fare, surge, platform fee, taxes | ✅ |
| Confirmed vehicle type details | [`VehicleType`](../../schema/VehicleType/README.md) | `maxCapacity`, `propulsionType` | ✅ |
| Confirmed waiting policy | [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | `freeWaitingTimeMinutes` | ✅ |
| Confirmed pickup zone | [`PickupPolicy`](../../schema/PickupPolicy/README.md) | `allowedPickupAreas` | ✅ |
| Drop zone rules | [`DropPolicy`](../../schema/DropPolicy/README.md) | `dropConditions` | ✅ |

---

#### Action: `init`
**Semantic intent:** Priya submits her billing participant details — name, phone, payment preference.

**BAP sends everything from `on_select` PLUS:**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Billing participant identity | [`Rider`](../../schema/Rider/README.md) | `riderId`, `preferredPaymentMethod` | ✅ |
| Passenger category | [`RiderCategory`](../../schema/RiderCategory/README.md) | `riderCategoryId` | ✅ |

---

#### Action: `on_init`
**Semantic intent:** The BPP returns the full pre-payment contract terms — including a FORM asking Priya to choose toll or non-toll route, the available payment channels, and binding cancellation terms.

**BPP returns everything from `init` PLUS:**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Draft order object | [`Trip`](../../schema/Trip/README.md) | `tripId`, `state` | ✅ |
| Post-payment terms | [`Trip`](../../schema/Trip/README.md) | `descriptor` (payment instructions) | ✅ |
| Binding cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `cancellationTerms`, `refundPercentage`, `cancelByTime` | ✅ |
| No-show fee terms | [`NoShowPolicy`](../../schema/NoShowPolicy/README.md) | `noShowFee`, `gracePeriodMinutes` | ✅ |
| **Toll / non-toll route selection form** | ❌ No dedicated class | — | ❌ |
| Payment channel options (online / cash) | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags` (payment options) | ⚠️ |
| Safety policy and emergency contact | [`SafetyPolicy`](../../schema/SafetyPolicy/README.md) | `safetyInstructions`, `emergencyContact` | ✅ |
| Applied voucher/promo discount | [`Entitlement`](../../schema/Entitlement/README.md) | `entitlementType: PROMOTION` | ✅ |

**❌ Gap #2 — Toll/Non-toll Route Selection Form:**
The `on_init` for ride hailing MUST include a form that collects the rider's route preference (toll vs non-toll road). This is a critical pre-payment decision that affects the final fare. In Beckn protocol, this uses the `XInput` (extended input) mechanism — a form URL or schema returned by the BPP. The mobility schema has no dedicated class for `RoutePreference`. This is a confirmed gap: a `RoutePreference` class (or `JourneyPreference`) is needed, extending `beckn:Form` or carrying structured preference options.

---

#### Action: `confirm`
**Semantic intent:** Priya selects the toll/non-toll option from the form, selects "Pay Online" as the payment channel, and confirms.

**BAP sends everything from `on_init` PLUS:**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Selected route preference (toll/non-toll) | ❌ No dedicated class | — | ❌ |
| Selected payment channel | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags: PAYMENT_CHANNEL=ONLINE` | ⚠️ |
| Payment reference (if online pre-pay) | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags: PAYMENT_REF` | ⚠️ |

---

#### Action: `on_confirm`
**Semantic intent:** The BPP creates the confirmed booking, returns the contract with a booking ID, and signals that driver allocation has STARTED — but does NOT yet return driver/vehicle details.

**BPP returns:**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Confirmed booking contract | [`Trip`](../../schema/Trip/README.md) | `tripId`, `state` | ✅ |
| Exact confirmed pickup (GPS) | [`Place`](../../schema/Place/README.md) | `gps`, `placeName` | ✅ |
| Exact confirmed drop (GPS) | [`Place`](../../schema/Place/README.md) | `gps`, `placeName` | ✅ |
| Confirmed ride offer | [`RideOption`](../../schema/RideOption/README.md) | `id`, `vehicleType` | ✅ |
| Confirmed add-ons | [`AncillaryService`](../../schema/AncillaryService/README.md) | `serviceCode`, `serviceCategory` | ✅ |
| Billing participant reference | [`Rider`](../../schema/Rider/README.md) | `riderId` | ✅ |
| Confirmed fare estimate with breakup | [`FareBreakup`](../../schema/FareBreakup/README.md) | All components | ✅ |
| Binding cancellation terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `cancellationTerms` | ✅ |
| Selected payment channel | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags` | ⚠️ |
| **Driver allocation status — SEARCHING** | [`Event`](../../schema/Event/README.md) | `eventType: DRIVER_ALLOCATION_SEARCHING` | ✅ |
| Confirmed pickup meet-point | [`PickupDropoffPoint`](../../schema/PickupDropoffPoint/README.md) | `landmark`, `accessNotes` | ✅ |
| Platform support contact | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE`, `handle` | ✅ |

> **⚠️ Critical design note:** `on_confirm` does NOT include driver details or vehicle details. These arrive later via `on_update` when a driver actually accepts the job. At `on_confirm` time, the BPP only confirms the booking is accepted and that it is SEARCHING for a driver.

---

### Stage 3 — Fulfillment

---

#### Action: `on_update` *(BPP-initiated push — driver assignment)*
**Semantic intent:** After a driver accepts the job, the BPP pushes the FULL updated order state to the BAP. This is the most information-dense message in the ride lifecycle. It carries everything from `on_confirm` PLUS the newly assigned driver, vehicle, live location, tracking active flag, and the ride-start OTP.

**BPP pushes (full order state + new fulfillment elements):**

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Full updated contract | [`Trip`](../../schema/Trip/README.md) | `tripId`, `state: DRIVER_ASSIGNED` | ✅ |
| Exact pickup (GPS) | [`Place`](../../schema/Place/README.md) | `gps` | ✅ |
| Exact drop (GPS) | [`Place`](../../schema/Place/README.md) | `gps` | ✅ |
| Confirmed ride offer + add-ons | [`RideOption`](../../schema/RideOption/README.md) | `id` | ✅ |
| Billing participant reference | [`Rider`](../../schema/Rider/README.md) | `riderId` | ✅ |
| Fare estimate with breakup | [`FareBreakup`](../../schema/FareBreakup/README.md) | All components | ✅ |
| Payment terms | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `cancellationTerms` | ✅ |
| Selected payment channel | [`Trip`](../../schema/Trip/README.md) | `descriptor.tags` | ⚠️ |
| **Assigned driver details** | [`Driver`](../../schema/Driver/README.md) | `licenseNumber`, `yearsOfExperience` | ✅ |
| **Driver aggregated rating** | [`Driver`](../../schema/Driver/README.md) | via `beckn:FulfillmentAgent.rating` | ✅ |
| **Assigned vehicle details** | [`Vehicle`](../../schema/Vehicle/README.md) | `licensePlate`, `make`, `model`, `color`, `year` | ✅ |
| **Vehicle type** | [`VehicleType`](../../schema/VehicleType/README.md) | `vehicleTypeCode`, `maxCapacity` | ✅ |
| **Driver live location** | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude`, `bearing`, `speed` | ✅ |
| **Driver masked contact** | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE`, masked number | ✅ |
| **Tracking now ACTIVE** | [`TripUpdate`](../../schema/TripUpdate/README.md) | `trackingEndpoint` (status: ACTIVE) | ✅ |
| Driver assignment event | [`Event`](../../schema/Event/README.md) | `eventType: DRIVER_ASSIGNED` | ✅ |
| **Ride start OTP / fulfillment auth** | ❌ No dedicated mobility class | `beckn:Fulfillment.start.authorization` | ❌ |

**❌ Gap #3 — Fulfillment Start Authorization (OTP):**
When the BPP assigns a driver, it issues a ride-start OTP. The driver shows this OTP to the rider (or vice versa) to authenticate the trip start. In Beckn core, this is `beckn:Fulfillment.start.authorization` with `type: OTP` and `token: "1234"`. The mobility `Trip` class doesn't explicitly surface this relationship. The `Trip` class needs a `startAuthorization` property linking to `beckn:Authorization` from core. **This is Gap #3.**

---

#### Action: `status`
**Semantic intent:** BAP polls for current trip state (driver en route, arrived, trip started, trip ended).

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Trip being queried | [`Trip`](../../schema/Trip/README.md) | `tripId` | ✅ |
| Current state snapshot | [`TripUpdate`](../../schema/TripUpdate/README.md) | `stateUpdate`, `trackingEndpoint` | ✅ |
| Driver live location | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude` | ✅ |
| Trip lifecycle event | [`Event`](../../schema/Event/README.md) | `DRIVER_EN_ROUTE`, `DRIVER_ARRIVED`, `TRIP_STARTED`, `TRIP_ENDED` | ✅ |
| Seat availability (shared ride) | [`OccupancyStatus`](../../schema/OccupancyStatus/README.md) | `occupancyLevel` | ✅ |

---

#### Action: `track`
**Semantic intent:** Priya opens the live map — BAP requests the tracking endpoint.

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Live driver coordinates + speed | [`VehiclePosition`](../../schema/VehiclePosition/README.md) | `latitude`, `longitude`, `speed`, `bearing` | ✅ |
| Telemetry stream (odometer, battery) | [`Telemetry`](../../schema/Telemetry/README.md) | `speed`, `bearing`, `odometer` | ✅ |

---

#### Action: `update` *(BAP-initiated — mid-ride change)*
**Semantic intent:** Priya requests an intermediate stop to pick up a friend.

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Contract modification | [`TripUpdate`](../../schema/TripUpdate/README.md) | `contractChanges` (new stop) | ✅ |
| New intermediate stop | [`PickupDropoffPoint`](../../schema/PickupDropoffPoint/README.md) | `pdpType: PICKUP`, `landmark` | ✅ |
| Revised fare breakup | [`FareBreakup`](../../schema/FareBreakup/README.md) | Updated total | ✅ |

---

#### Action: `cancel`
**Semantic intent:** Priya cancels before driver arrives.

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Contract cancellation | [`Trip`](../../schema/Trip/README.md) | `tripId` | ✅ |
| Applied policy + refund | [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | `refundPercentage`, `gracePeriodMinutes` | ✅ |
| Cancellation receipt | [`Receipt`](../../schema/Receipt/README.md) | `receiptId`, `paymentMethod` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Numeric driver rating | [`Rating`](../../schema/Rating/README.md) | `ratingValue`, `ratedEntityType: DRIVER` | ✅ |
| Free-text review | [`Review`](../../schema/Review/README.md) | `reviewText` | ✅ |
| Structured feedback tags | [`Feedback`](../../schema/Feedback/README.md) | `feedbackType` | ✅ |

---

#### Action: `support`

| Information | Schema Class | Property | Status |
|-------------|-------------|----------|--------|
| Lost item report | [`LostAndFoundItem`](../../schema/LostAndFoundItem/README.md) | `itemType`, `itemDescription` | ✅ |
| Support case | [`SupportCase`](../../schema/SupportCase/README.md) | `caseType: LOST_ITEM` | ✅ |
| Driver contact for item recovery | [`ContactHandle`](../../schema/ContactHandle/README.md) | `handleType: PHONE` | ✅ |

---

## Coverage Summary

| Class | Actions Used In | Lifecycle Stage |
|-------|----------------|----------------|
| `RideRequest` | search | Discovery |
| `Place` | search, select, on_select, on_confirm, on_update | All |
| `VehicleCategory` | search, on_search, select | Discovery, Contracting |
| `RiderCategory` | search, init | Discovery, Contracting |
| `PassengerGroup` | search | Discovery |
| `PlanningResult` | on_search | Discovery |
| `RideOption` | on_search, select, on_select, on_confirm, on_update | Discovery, Contracting |
| `VehicleType` | on_search, on_select, on_update | Discovery, Contracting, Fulfillment |
| `AncillaryService` | on_search, select, on_confirm, on_update | All |
| `FareEstimate` | on_search, on_select | Discovery, Contracting |
| `FareBreakup` | on_search, on_select, on_init, on_confirm, on_update, update, on_cancel | All stages |
| `SurgeMultiplier` | on_search | Discovery |
| `PricingModel` | on_search | Discovery |
| `WaitingPolicy` | on_search, on_select | Discovery, Contracting |
| `CancellationPolicy` | on_search, on_init, on_confirm, on_update, cancel | Contracting, Fulfillment |
| `Operator` | on_search | Discovery |
| `ServiceClass` | select | Contracting |
| `PickupPolicy` | select, on_select | Contracting |
| `DropPolicy` | on_select | Contracting |
| `Rider` | init, on_confirm, on_update | Contracting |
| `Trip` | on_init, confirm, on_confirm, on_update, status, cancel | Contracting, Fulfillment |
| `NoShowPolicy` | on_init | Contracting |
| `SafetyPolicy` | on_init | Contracting |
| `Entitlement` | on_init | Contracting |
| `Event` | on_confirm, on_update, status | Contracting, Fulfillment |
| `PickupDropoffPoint` | on_confirm, update | Contracting, Fulfillment |
| `ContactHandle` | on_confirm, on_update, on_support | Contracting, Fulfillment, Post |
| `Driver` | on_update | Fulfillment |
| `Vehicle` | on_update | Fulfillment |
| `VehiclePosition` | on_update, status, on_track | Fulfillment |
| `TripUpdate` | on_update, status, update | Fulfillment |
| `OccupancyStatus` | status | Fulfillment |
| `Telemetry` | on_track | Fulfillment |
| `Receipt` | on_cancel | Fulfillment |
| `Rating` | rating | Post-Fulfillment |
| `Review` | rating | Post-Fulfillment |
| `Feedback` | rating | Post-Fulfillment |
| `SupportCase` | support, on_support | Post-Fulfillment |
| `LostAndFoundItem` | support | Post-Fulfillment |

---

## Gap Report

| # | Gap | Description | Severity | Proposed Resolution |
|---|-----|-------------|----------|---------------------|
| 1 | **VehicleFeature** | `VehicleType` has no structured properties for boot space, A/C availability, child seat capacity. These vehicle attributes are shown at catalog time (`on_search`) for rider to compare options. Currently only expressible via inherited `tags`. | Medium | Create `VehicleFeature` class extending `beckn:Feature` (following `BikeAllowed` pattern) with properties: `featureCode`, `featureValue`. Instances: `BootSpace`, `AirConditioning`, `ChildSeat`. |
| 2 | **RoutePreference** | No mobility class for capturing ride route preferences (toll vs non-toll road, highway vs city road). The BPP must present a form in `on_init` to collect this. Currently, Beckn core's `XInput` mechanism handles the form delivery but there is no semantically-typed `RoutePreference` class in the mobility schema. | Medium | Create `RoutePreference` class extending `beckn:Form` (or `beckn:Descriptor`) with properties: `tollPreference` (TOLL / NO_TOLL / ANY), `routeType` (HIGHWAY / CITY), `acPreference` (AC / NON_AC). |
| 3 | **FulfillmentAuthorization** | The ride-start OTP (sent by BPP at driver assignment via `on_update`) has no dedicated mobility class. It uses `beckn:Fulfillment.start.authorization` from core, but the `Trip` class does not expose this relationship explicitly. BAP implementations must know to look in `fulfillments[].start.authorization`. | Medium | Add `startAuthorization` property to `Trip` class, typed as `beckn:Authorization` from core. Or create a `FulfillmentAuthorization` class with `type` (OTP / PIN / QR) and `token` properties. |
