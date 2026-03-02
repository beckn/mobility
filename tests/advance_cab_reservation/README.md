# Advance Cab Reservation — Lifecycle Stress Test

## Use Case Narrative

Arjun is traveling to Mumbai airport tomorrow morning for a 6 AM flight. He opens a cab app the night before, enters his home address, the airport as destination, and requests a cab pickup at 3:30 AM. The app shows him available cab options with fixed advance-booking fares (no surge at 3:30 AM). He selects a Sedan, enters his phone number, and confirms the booking with pre-payment. At 2:45 AM, the driver is assigned and his vehicle is visible on a map. Arjun is dropped at the departure terminal on time. Post-trip, he rates the driver and requests an invoice for reimbursement.

## Actors

| Actor | Role | Beckn Entity |
|-------|------|-------------|
| Arjun | Consumer — advance-booking traveler | Represented by BAP |
| Cab App | BAP — renders options, relays Arjun's selections | `beckn:BAP` |
| Cab Aggregator | BPP — manages fleet, pre-booking slots, pricing | `beckn:BPP` |
| Driver | Fulfillment agent — picks Arjun up at 3:30 AM | `mobility:Driver` |

---

## Lifecycle Stage Walkthrough

### Stage 1 — Discovery

---

#### Action: `search`
**Semantic intent:** Arjun expresses his intent — origin, destination, future pickup time, passenger count, and preference for a Sedan.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`RideRequest`](../../schema/RideRequest/README.md) | Top-level intent with future `requestedTime` | `beckn:Intent` | ✅ |
| [`Place`](../../schema/Place/README.md) | Home address (pickup origin) | `beckn:Location` | ✅ |
| [`Place`](../../schema/Place/README.md) | Airport terminal (dropoff destination) | `beckn:Location` | ✅ |
| [`VehicleCategory`](../../schema/VehicleCategory/README.md) | Arjun's preference — Sedan | `beckn:CategoryCode` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Passenger type (Adult) | `beckn:CategoryCode` | ✅ |
| [`PassengerGroup`](../../schema/PassengerGroup/README.md) | Number of passengers (1 adult) | `beckn:Quantity` | ✅ |

**Notes:** The key differentiator from instant ride hailing is `RideRequest.requestedTime` set to a future timestamp (3:30 AM). The BPP MUST recognise this as an advance reservation and apply pre-booking pricing (no surge for off-peak slots). `Place` with `placeType: AIRPORT` identifies the destination as an airport terminal.

---

#### Action: `on_search`
**Semantic intent:** The BPP returns available sedan options for the pre-booked 3:30 AM slot with fixed advance fares and relevant policies.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`PlanningResult`](../../schema/PlanningResult/README.md) | Catalog of advance-booking options | `beckn:Catalog` | ✅ |
| [`RideOption`](../../schema/RideOption/README.md) | A sedan option with pre-assigned fare | `beckn:Offer` | ✅ |
| [`VehicleCategory`](../../schema/VehicleCategory/README.md) | Sedan category details | `beckn:CategoryCode` | ✅ |
| [`FareEstimate`](../../schema/FareEstimate/README.md) | Fixed advance fare (locked, no surge) | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Base fare + toll estimate + platform fee | `beckn:PriceComponent` | ✅ |
| [`PricingModel`](../../schema/PricingModel/README.md) | Fixed pricing model (upfront quote, not metered) | `beckn:Offer` | ✅ |
| [`BookingRule`](../../schema/BookingRule/README.md) | Advance booking terms (earliest/latest booking time) | `beckn:Policy` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | Waiting time terms at 3:30 AM slot | `beckn:Policy` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Advance booking cancellation terms (may differ from instant) | `beckn:CancellationPolicy` | ✅ |
| [`NoShowPolicy`](../../schema/NoShowPolicy/README.md) | No-show fee if Arjun is not at pickup at 3:30 AM | `beckn:Policy` | ✅ |
| [`Operator`](../../schema/Operator/README.md) | The cab fleet operator | `beckn:Provider` | ✅ |

**Notes:** `BookingRule` is the key differentiator here — it specifies `latestBookingTime` (e.g., must book at least 1 hour in advance), `priorNoticeDurationMin`, and `earliestBookingTime`. `NoShowPolicy` is critical for airport runs since the driver arrives at 3:30 AM sharp.

---

### Stage 2 — Contracting

---

#### Action: `select`
**Semantic intent:** Arjun selects the Sedan with fixed fare and accepts the booking terms.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`RideOption`](../../schema/RideOption/README.md) | Selected Sedan option (by id) | `beckn:Offer` | ✅ |
| [`ServiceClass`](../../schema/ServiceClass/README.md) | Premium tier confirmation | `beckn:CategoryCode` | ✅ |
| [`PickupPolicy`](../../schema/PickupPolicy/README.md) | Pickup gate or exact address for 3:30 AM | `beckn:Policy` | ✅ |

---

#### Action: `on_select`
**Semantic intent:** The BPP confirms slot availability, locks the fare, and returns updated terms for the advance booking.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`RideOption`](../../schema/RideOption/README.md) | Confirmed option with guaranteed 3:30 AM slot | `beckn:Offer` | ✅ |
| [`FareEstimate`](../../schema/FareEstimate/README.md) | Guaranteed fixed advance fare | `beckn:Offer` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final component breakdown | `beckn:PriceComponent` | ✅ |
| [`Vehicle`](../../schema/Vehicle/README.md) | Vehicle type confirmed (model/fuel) | `beckn:Item` | ✅ |
| [`VehicleType`](../../schema/VehicleType/README.md) | Type details (capacity, AC, accessibility) | `beckn:CategoryCode` | ✅ |
| [`BookingRule`](../../schema/BookingRule/README.md) | Confirmed advance booking rules | `beckn:Policy` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | Waiting policy reconfirmed | `beckn:Policy` | ✅ |
| [`PickupPolicy`](../../schema/PickupPolicy/README.md) | Confirmed pickup instructions | `beckn:Policy` | ✅ |
| [`DropPolicy`](../../schema/DropPolicy/README.md) | Airport drop restrictions (terminal, zone) | `beckn:Policy` | ✅ |

---

#### Action: `init`
**Semantic intent:** Arjun submits his phone number, name, and pre-payment details to initiate the booking.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rider`](../../schema/Rider/README.md) | Arjun's contact info and payment preference | `beckn:Participant` | ✅ |
| [`RiderCategory`](../../schema/RiderCategory/README.md) | Adult passenger classification | `beckn:CategoryCode` | ✅ |

---

#### Action: `on_init`
**Semantic intent:** The BPP returns the complete advance booking contract terms — fare, policies, and payment instructions.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Draft advance booking contract | `beckn:Contract` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final fare components before payment | `beckn:PriceComponent` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Advance cancellation terms (e.g., full refund >4 hrs, 50% <2 hrs) | `beckn:CancellationPolicy` | ✅ |
| [`NoShowPolicy`](../../schema/NoShowPolicy/README.md) | Full fare charged if Arjun is absent at 3:30 AM | `beckn:Policy` | ✅ |
| [`WaitingPolicy`](../../schema/WaitingPolicy/README.md) | Final waiting time terms | `beckn:Policy` | ✅ |
| [`SafetyPolicy`](../../schema/SafetyPolicy/README.md) | Safety instructions and emergency contact | `beckn:Policy` | ✅ |

---

#### Action: `confirm`
**Semantic intent:** Arjun confirms the advance booking with pre-payment. The booking is now locked in until the next morning.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Order being confirmed with payment | `beckn:Contract` | ✅ |
| [`Rider`](../../schema/Rider/README.md) | Confirming rider identity and payment | `beckn:Participant` | ✅ |

---

#### Action: `on_confirm`
**Semantic intent:** The BPP confirms the advance booking, stores it, and returns a booking confirmation with details to be shown to Arjun.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Confirmed advance booking contract | `beckn:Contract` | ✅ |
| [`Driver`](../../schema/Driver/README.md) | Assigned driver (may be placeholder until near pickup time) | `beckn:FulfillmentAgent` | ⚠️ |
| [`Vehicle`](../../schema/Vehicle/README.md) | Vehicle details (may be allocated closer to pickup) | `beckn:Item` | ⚠️ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Final binding fare breakup | `beckn:PriceComponent` | ✅ |
| [`PickupDropoffPoint`](../../schema/PickupDropoffPoint/README.md) | Confirmed pickup location and landmark | `beckn:FulfillmentStop` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | Emergency support contact (driver assigned later) | `beckn:SupportInfo` | ✅ |

**Notes (⚠️):** For advance bookings, the specific `Driver` and `Vehicle` are typically not allocated at `on_confirm` time — they are assigned closer to the pickup slot. The BPP MAY return placeholder driver info or omit it, with the actual assignment pushed via `on_status` nearer the time. This is a valid lifecycle pattern and does NOT represent a schema gap.

---

### Stage 3 — Fulfillment

---

#### Action: `status` (polled ~30 minutes before pickup)
**Semantic intent:** Arjun's app polls at 3:00 AM to check if a driver has been assigned.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Advance booking being queried | `beckn:Contract` | ✅ |

---

#### Action: `on_status`
**Semantic intent:** The BPP confirms driver assignment, returns live location, and signals "Driver En Route."

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`TripUpdate`](../../schema/TripUpdate/README.md) | State snapshot: driver assigned + en route | `beckn:Contract` | ✅ |
| [`Driver`](../../schema/Driver/README.md) | Newly assigned driver details | `beckn:FulfillmentAgent` | ✅ |
| [`Vehicle`](../../schema/Vehicle/README.md) | Allocated vehicle with plate number | `beckn:Item` | ✅ |
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Driver's live location at 3:00 AM | `beckn:Tracking` | ✅ |
| [`Event`](../../schema/Event/README.md) | `DRIVER_ASSIGNED`, `DRIVER_EN_ROUTE` | `beckn:State` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | Driver's masked contact now available | `beckn:SupportInfo` | ✅ |

---

#### Action: `track`
**Semantic intent:** Arjun opens the live map to watch the driver approach.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Advance booking being tracked | `beckn:Contract` | ✅ |

---

#### Action: `on_track`
**Semantic intent:** BPP returns live tracking feed for the assigned driver.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`VehiclePosition`](../../schema/VehiclePosition/README.md) | Real-time driver coordinates and ETA | `beckn:Tracking` | ✅ |
| [`Telemetry`](../../schema/Telemetry/README.md) | Speed and bearing for animated map display | `beckn:Tracking` | ✅ |

---

#### Action: `cancel` (if Arjun cancels the night before)
**Semantic intent:** Arjun's plans change — he cancels the advance booking 6 hours before the slot.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Advance booking being cancelled | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Policy governing >4 hr advance cancellation | `beckn:CancellationPolicy` | ✅ |

---

#### Action: `on_cancel`
**Semantic intent:** BPP applies the advance cancellation policy (full refund since >4 hrs before pickup) and returns a cancellation receipt.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Trip`](../../schema/Trip/README.md) | Cancelled advance booking contract | `beckn:Contract` | ✅ |
| [`CancellationPolicy`](../../schema/CancellationPolicy/README.md) | Applied policy with refund amount | `beckn:CancellationPolicy` | ✅ |
| [`Receipt`](../../schema/Receipt/README.md) | Cancellation receipt with full refund | `beckn:Invoice` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Net settlement (refund breakdown) | `beckn:PriceComponent` | ✅ |

---

### Stage 4 — Post-Fulfillment

---

#### Action: `rating`
**Semantic intent:** Arjun rates the on-time pickup and smooth airport drop — 5 stars.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | 5-star rating for driver (ratedEntityType: DRIVER) | `beckn:RatingInput` | ✅ |
| [`Review`](../../schema/Review/README.md) | "Driver was on time at 3:30 AM!" review text | `beckn:RatingInput` | ✅ |
| [`Feedback`](../../schema/Feedback/README.md) | Tags: ON_TIME, SMOOTH_RIDE | `beckn:Feedback` | ✅ |

---

#### Action: `on_rating`
**Semantic intent:** BPP acknowledges rating.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Rating`](../../schema/Rating/README.md) | Confirmed rating record | `beckn:RatingInput` | ✅ |

---

#### Action: `support`
**Semantic intent:** Arjun requests an itemised receipt for travel reimbursement from his employer.

**Schema classes required (BAP → BPP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`SupportCase`](../../schema/SupportCase/README.md) | Support case (type: INVOICE_REQUEST) | `beckn:SupportRequest` | ✅ |

---

#### Action: `on_support`
**Semantic intent:** BPP returns the itemised receipt.

**Schema classes required (BPP → BAP):**

| Class | Role in Message | Lifecycle Parent | Status |
|-------|----------------|-----------------|--------|
| [`Receipt`](../../schema/Receipt/README.md) | Full itemised receipt with all components | `beckn:Invoice` | ✅ |
| [`FareBreakup`](../../schema/FareBreakup/README.md) | Itemised components for reimbursement | `beckn:PriceComponent` | ✅ |
| [`ContactHandle`](../../schema/ContactHandle/README.md) | Support contact if more help needed | `beckn:SupportInfo` | ✅ |

---

## Coverage Summary

| Class | Actions Used In | Lifecycle Stage |
|-------|----------------|----------------|
| `RideRequest` | search | Discovery |
| `Place` | search | Discovery |
| `VehicleCategory` | search, on_search, select | Discovery, Contracting |
| `RiderCategory` | search, init | Discovery, Contracting |
| `PassengerGroup` | search | Discovery |
| `PlanningResult` | on_search | Discovery |
| `RideOption` | on_search, select, on_select | Discovery, Contracting |
| `FareEstimate` | on_search, on_select | Discovery, Contracting |
| `FareBreakup` | on_search, on_select, on_init, on_confirm, on_cancel, on_support | All stages |
| `PricingModel` | on_search | Discovery |
| `BookingRule` | on_search, on_select | Discovery, Contracting |
| `WaitingPolicy` | on_search, on_select, on_init | Contracting |
| `CancellationPolicy` | on_search, on_init, cancel, on_cancel | Contracting, Fulfillment |
| `NoShowPolicy` | on_search, on_init | Discovery, Contracting |
| `Operator` | on_search | Discovery |
| `ServiceClass` | select | Contracting |
| `PickupPolicy` | select, on_select | Contracting |
| `DropPolicy` | on_select | Contracting |
| `Vehicle` | on_select, on_confirm, on_status | Contracting, Fulfillment |
| `VehicleType` | on_select | Contracting |
| `Rider` | init, confirm | Contracting |
| `Trip` | on_init, confirm, on_confirm, status, track, cancel, on_cancel | Contracting, Fulfillment |
| `SafetyPolicy` | on_init | Contracting |
| `Driver` | on_confirm, on_status | Contracting, Fulfillment |
| `PickupDropoffPoint` | on_confirm | Contracting |
| `ContactHandle` | on_confirm, on_status, on_support | Contracting, Fulfillment, Post |
| `TripUpdate` | on_status | Fulfillment |
| `VehiclePosition` | on_status, on_track | Fulfillment |
| `Event` | on_status | Fulfillment |
| `Telemetry` | on_track | Fulfillment |
| `Receipt` | on_cancel, on_support | Fulfillment, Post-Fulfillment |
| `Rating` | rating, on_rating | Post-Fulfillment |
| `Review` | rating | Post-Fulfillment |
| `Feedback` | rating | Post-Fulfillment |
| `SupportCase` | support | Post-Fulfillment |

---

## Gap Report

| Gap | Description | Severity |
|-----|-------------|----------|
| No gaps detected | All schema classes required for the advance cab reservation lifecycle exist in the mobility schema. `BookingRule` correctly handles the advance booking time window; `NoShowPolicy` handles airport no-shows; `CancellationPolicy` handles tiered refunds. | — |

> **Design note:** The deferred driver/vehicle assignment pattern (driver allocated close to pickup time, not at `on_confirm`) is a real-world advance booking behavior. It is handled by the `TripUpdate.stateUpdate` carrying a `DRIVER_ASSIGNED` event in `on_status` — no additional schema class is needed.
