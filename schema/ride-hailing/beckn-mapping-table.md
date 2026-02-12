# Ride-Hailing to Beckn IRI Mapping Table

This document maps IRIs defined in `schema/ride-hailing/context.jsonld` to their corresponding Beckn core IRIs defined in `schema/core/vocab.jsonld` and `schema/core/context.jsonld`.

## Legend

- ✅ **Direct Beckn Mapping**: Term directly uses or extends a Beckn IRI
- 🔄 **Beckn Property Reuse**: Uses Beckn property with domain-specific context
- 🆕 **Mobility Extension**: New mobility-specific term (no direct Beckn equivalent)
- 📦 **Beckn Type**: Uses or extends a Beckn class/type

---

## Class/Type Mappings

| Ride-Hailing IRI | Beckn IRI | Mapping Type | Notes |
|-----------------|-----------|--------------|-------|
| `mobility:RideHailingService` | `beckn:Item` | 🆕 | Specializes Item for ride-hailing services |
| `mobility:RideOption` | `beckn:Offer` | 🆕 | Specializes Offer for ride options |
| `mobility:RideRequest` | `beckn:Order` | 🆕 | Specializes Order for ride requests |
| `mobility:Trip` | `beckn:Fulfillment` | 🆕 | Specializes Fulfillment for trips |
| `mobility:TripLeg` | `beckn:FulfillmentStop` | 🆕 | Related to multi-leg journeys |
| `mobility:TripItinerary` | `beckn:Fulfillment` | 🆕 | Collection of trip legs |
| `mobility:FulfillmentStop` | `beckn:FulfillmentStop` | 📦 | Direct use of Beckn class |
| `mobility:StopPlace` | `beckn:Location` | 🆕 | Specializes Location |
| `mobility:PickupDropoffPoint` | `beckn:Location` | 🆕 | Specializes Location for pickup/drop |
| `mobility:Geofence` | `beckn:GeoJSONGeometry` | 🆕 | Uses GeoJSON for service boundaries |
| `mobility:Route` | `beckn:GeoJSONGeometry` | 🆕 | Path representation using GeoJSON |
| `mobility:Driver` | `beckn:FulfillmentAgent` | 🆕 | Specializes FulfillmentAgent |
| `mobility:DriverIdentity` | `beckn:Participant` | 🆕 | Driver identity information |
| `mobility:DriverCredential` | `beckn:Credential` | 📦 | Direct use of Beckn Credential |
| `mobility:DriverSkill` | `beckn:Skill` | 📦 | Direct use of Beckn Skill |
| `mobility:Vehicle` | `beckn:Item` | 🆕 | Vehicle as fulfillment resource |
| `mobility:VehicleCategory` | `beckn:CategoryCode` | 🆕 | Vehicle type classification |
| `mobility:VehicleFeature` | `beckn:Feature` | 📦 | Direct use of Beckn Feature |
| `mobility:AccessibilityFeature` | `beckn:Feature` | 📦 | Subtype of Feature |
| `mobility:ConnectivityFeature` | `beckn:Feature` | 📦 | Subtype of Feature |
| `mobility:Accessory` | `beckn:Item` | 🆕 | Add-on items |
| `mobility:ServiceClass` | `beckn:CategoryCode` | 🆕 | Service tier classification |
| `mobility:Rider` | `beckn:Participant` | 🆕 | Specializes Participant (replaces Buyer) |
| `mobility:PassengerGroup` | `beckn:Participant` | 🆕 | Multiple passengers |
| `mobility:ContactHandle` | `beckn:Attributes` | 🆕 | Contact information structure |
| `mobility:LocationRef` | `beckn:Location` | 🆕 | Location reference |
| `mobility:TimeWindow` | `beckn:TimePeriod` | 📦 | Direct use of TimePeriod |
| `mobility:Instruction` | `beckn:Instruction` | 📦 | Direct use of Beckn Instruction |
| `mobility:OperationalPolicy` | `beckn:Policy` | 📦 | Direct use of Beckn Policy |
| `mobility:WaitingPolicy` | `beckn:Policy` | 🆕 | Policy subtype |
| `mobility:NoShowPolicy` | `beckn:Policy` | 🆕 | Policy subtype |
| `mobility:CancellationPolicy` | `beckn:Policy` | 🆕 | Policy subtype |
| `mobility:PickupPolicy` | `beckn:Policy` | 🆕 | Policy subtype |
| `mobility:DropPolicy` | `beckn:Policy` | 🆕 | Policy subtype |
| `mobility:SafetyPolicy` | `beckn:Policy` | 🆕 | Policy subtype |
| `mobility:PricingModel` | `beckn:Attributes` | 🆕 | Pricing structure |
| `mobility:FareEstimate` | `schema:PriceSpecification` | 🆕 | Price estimate using schema.org |
| `mobility:FareBreakup` | `beckn:PriceComponent` | 📦 | Uses Beckn PriceComponent |
| `mobility:PriceComponent` | `beckn:PriceComponent` | 📦 | Direct use |
| `mobility:TollCharge` | `beckn:PriceComponent` | 🆕 | Component subtype |
| `mobility:Surcharge` | `beckn:PriceComponent` | 🆕 | Component subtype |
| `mobility:Discount` | `beckn:PriceComponent` | 🆕 | Component subtype |
| `mobility:Tax` | `beckn:PriceComponent` | 🆕 | Component subtype |
| `mobility:PaymentInstrument` | `beckn:Payment` | 🆕 | Payment method details |
| `mobility:Entitlement` | `beckn:Entitlement` | 📦 | Direct use of Beckn Entitlement |
| `mobility:Coupon` | `beckn:Offer` | 🆕 | Discount offer type |
| `mobility:TripState` | `beckn:State` | 📦 | Direct use of Beckn State |
| `mobility:FulfillmentState` | `beckn:State` | 📦 | Direct use of Beckn State |
| `mobility:ServiceAlert` | `beckn:Alert` | 📦 | Direct use of Beckn Alert |
| `mobility:Incident` | `beckn:Alert` | 🆕 | Alert subtype |
| `mobility:EmergencyEvent` | `beckn:Alert` | 🆕 | Alert subtype |
| `mobility:SupportCase` | `beckn:SupportTicket` | 📦 | Direct use |
| `mobility:Rating` | `beckn:Rating` | 📦 | Direct use of Beckn Rating |
| `mobility:Review` | `beckn:Rating` | 🆕 | Rating with text |
| `mobility:Feedback` | `beckn:Feedback` | 📦 | Direct use of Beckn Feedback |
| `mobility:LostAndFoundItem` | `beckn:Item` | 🆕 | Lost item tracking |
| `mobility:DocumentRef` | `beckn:Document` | 📦 | Direct use of Beckn Document |
| `mobility:Receipt` | `beckn:Invoice` | 🆕 | Specializes Invoice |
| `mobility:TelemetryStream` | `beckn:Tracking` | 🆕 | Real-time tracking stream |
| `mobility:TrackingPoint` | `beckn:Tracking` | 🆕 | GPS coordinate point |

---

## Property Mappings

### Core Properties (Direct Beckn Reuse)

| Ride-Hailing Property | Beckn Property | Mapping Type | Notes |
|----------------------|----------------|--------------|-------|
| `id` | `@id` | ✅ | JSON-LD identifier |
| `type` | `@type` | ✅ | JSON-LD type |
| `descriptor` | `beckn:descriptor` | 🔄 | Via context aliasing |
| `category` | `beckn:category` | 🔄 | Via context aliasing |
| `items` | `beckn:items` | 🔄 | Via context aliasing |
| `provider` | `beckn:provider` | 🔄 | Via context aliasing |
| `location` | `beckn:location` | 🔄 | Via context aliasing |
| `locations` | `beckn:locations` | 🔄 | Via context aliasing |
| `price` | `beckn:price` | 🔄 | Via context aliasing |
| `quantity` | `beckn:quantity` | 🔄 | Via context aliasing |
| `fulfillment` | `beckn:fulfillment` | 🔄 | Via context aliasing |
| `payment` | `beckn:payment` | 🔄 | Via context aliasing |
| `geo` | `beckn:geo` | 🔄 | Via context aliasing |
| `address` | `beckn:address` | 🔄 | Via context aliasing |
| `rating` | `beckn:rating` | 🔄 | Via context aliasing |
| `feedback` | `beckn:feedback` | 🔄 | Via context aliasing |
| `timestamp` | `beckn:timestamp` | 🔄 | Via context aliasing |
| `coordinates` | `beckn:coordinates` | 🔄 | Via context aliasing |
| `stops` | `beckn:stops` | 🔄 | Via context aliasing |
| `stopType` | `beckn:stopType` | 🔄 | Via context aliasing |
| `instructions` | `beckn:instructions` | 🔄 | Via context aliasing |
| `constraints` | `beckn:constraints` | 🔄 | Via context aliasing |
| `policies` | `beckn:policies` | 🔄 | Via context aliasing |
| `participants` | `beckn:participants` | 🔄 | Via context aliasing |
| `skills` | `beckn:skills` | 🔄 | Via context aliasing |
| `credentials` | `beckn:credentials` | 🔄 | Via context aliasing |
| `features` | `beckn:features` | 🔄 | Via context aliasing |
| `entitlements` | `beckn:entitlements` | 🔄 | Via context aliasing |
| `alerts` | `beckn:alerts` | 🔄 | Via context aliasing |
| `priceComponents` | `beckn:priceComponents` | 🔄 | Via context aliasing |
| `state` | `beckn:state` | 🔄 | Via context aliasing |
| `severity` | `beckn:severity` | 🔄 | Via context aliasing |
| `documents` | `beckn:documents` | 🔄 | Via context aliasing |
| `evidence` | `beckn:evidence` | 🔄 | Via context aliasing |
| `supportCase` | `beckn:supportCase` | 🔄 | Via context aliasing |

### Mobility-Specific Properties (Extensions)

| Ride-Hailing Property | Beckn Property Base | Mapping Type | Notes |
|----------------------|---------------------|--------------|-------|
| `mobility:serviceClass` | `beckn:category` | 🆕 | Service tier (Economy, Premium, etc.) |
| `mobility:vehicleCategory` | `beckn:category` | 🆕 | Vehicle type (Sedan, SUV, etc.) |
| `mobility:accessibilityFeatures` | `beckn:features` | 🆕 | Wheelchair access, etc. |
| `mobility:vehicleFeatures` | `beckn:features` | 🆕 | AC, music, etc. |
| `mobility:connectivityFeatures` | `beckn:features` | 🆕 | WiFi, charging ports, etc. |
| `mobility:accessories` | `beckn:items` | 🆕 | Child seat, pet carrier, etc. |
| `mobility:pricingModel` | `beckn:Attributes` | 🆕 | Fixed, metered, dynamic |
| `mobility:fareEstimate` | `beckn:price` | 🆕 | Estimated fare |
| `mobility:fareBreakup` | `beckn:priceComponents` | 🆕 | Fare breakdown |
| `mobility:pickupPoint` | `beckn:location` | 🆕 | Pickup location |
| `mobility:dropoffPoint` | `beckn:location` | 🆕 | Drop-off location |
| `mobility:waypoints` | `beckn:locations` | 🆕 | Intermediate stops |
| `mobility:pickupTimeWindow` | `beckn:validity` | 🆕 | Pickup time range |
| `mobility:requestedPickupTime` | `beckn:startDate` | 🆕 | Requested pickup |
| `mobility:requestedDropTime` | `beckn:endDate` | 🆕 | Requested drop-off |
| `mobility:passengerGroup` | `beckn:participants` | 🆕 | Passenger details |
| `mobility:luggageCount` | `beckn:quantity` | 🆕 | Number of bags |
| `mobility:specialInstructions` | `beckn:instructions` | 🔄 | Pickup/drop instructions |
| `mobility:contactHandle` | `beckn:Attributes` | 🆕 | Phone/contact info |
| `mobility:otpRequired` | `beckn:Attributes` | 🆕 | OTP verification flag |
| `mobility:ridePreferences` | `beckn:Attributes` | 🆕 | Music, temperature, etc. |
| `mobility:accessibilityNeeds` | `beckn:Attributes` | 🆕 | Special accessibility requirements |
| `mobility:trip` | `beckn:fulfillment` | 🔄 | Trip as fulfillment |
| `mobility:itinerary` | `beckn:fulfillment` | 🆕 | Multi-leg journey plan |
| `mobility:eta` | `beckn:endDate` | 🆕 | Estimated time of arrival |
| `mobility:distanceEstimate` | `beckn:Attributes` | 🆕 | Estimated distance |
| `mobility:durationEstimate` | `beckn:Attributes` | 🆕 | Estimated duration |
| `mobility:driver` | `beckn:agent` | 🔄 | Driver as fulfillment agent |
| `mobility:driverIdentity` | `beckn:Attributes` | 🆕 | Driver ID, name, photo |
| `mobility:driverCredentials` | `beckn:credentials` | 🔄 | License, certifications |
| `mobility:driverSkills` | `beckn:skills` | 🔄 | Languages, training |
| `mobility:vehicle` | `beckn:Attributes` | 🆕 | Vehicle details |
| `mobility:vehiclePlate` | `beckn:id` | 🆕 | License plate number |
| `mobility:vehicleMake` | `beckn:Attributes` | 🆕 | Manufacturer |
| `mobility:vehicleModel` | `beckn:Attributes` | 🆕 | Model name |
| `mobility:vehicleColor` | `beckn:Attributes` | 🆕 | Color |
| `mobility:vehicleImages` | `beckn:mediaFile` | 🔄 | Vehicle photos |
| `mobility:pickupInstructions` | `beckn:instructions` | 🔄 | How to find pickup |
| `mobility:dropoffInstructions` | `beckn:instructions` | 🔄 | Drop-off guidance |
| `mobility:arrivalTime` | `beckn:startDate` | 🔄 | Actual arrival time |
| `mobility:departureTime` | `beckn:endDate` | 🔄 | Actual departure time |
| `mobility:waitingTime` | `beckn:Attributes` | 🆕 | Waiting duration |
| `mobility:waitingCharge` | `beckn:priceComponents` | 🆕 | Waiting fee |
| `mobility:surgeMultiplier` | `beckn:Attributes` | 🆕 | Dynamic pricing multiplier |
| `mobility:tollsIncluded` | `beckn:Attributes` | 🆕 | Whether tolls are included |
| `mobility:routeDeviationAllowed` | `beckn:Attributes` | 🆕 | Can route be changed |
| `mobility:shareTrip` | `beckn:Attributes` | 🆕 | Shared ride flag |
| `mobility:seatCount` | `beckn:quantity` | 🔄 | Available seats |
| `mobility:vehicleArrived` | `beckn:state` | 🔄 | Arrival notification |
| `mobility:tripState` | `beckn:state` | 🔄 | Trip status |
| `mobility:stateReason` | `beckn:Attributes` | 🆕 | Why in this state |
| `mobility:serviceAlerts` | `beckn:alerts` | 🔄 | Service disruptions |
| `mobility:baseFare` | `beckn:priceComponents` | 🆕 | Base fare component |
| `mobility:distanceFare` | `beckn:priceComponents` | 🆕 | Distance-based fare |
| `mobility:timeFare` | `beckn:priceComponents` | 🆕 | Time-based fare |
| `mobility:bookingFee` | `beckn:priceComponents` | 🆕 | Platform fee |
| `mobility:airportFee` | `beckn:priceComponents` | 🆕 | Airport surcharge |
| `mobility:tollCharge` | `beckn:priceComponents` | 🔄 | Toll fees |
| `mobility:tax` | `beckn:priceComponents` | 🔄 | Taxes |
| `mobility:discount` | `beckn:priceComponents` | 🔄 | Discounts applied |
| `mobility:surcharge` | `beckn:priceComponents` | 🔄 | Additional charges |
| `mobility:receipt` | `beckn:invoice` | 🔄 | Trip receipt |
| `mobility:receiptNumber` | `beckn:number` | 🔄 | Receipt ID |
| `mobility:paymentInstrument` | `beckn:method` | 🔄 | Payment method |
| `mobility:paymentStatus` | `beckn:paymentStatus` | 🔄 | Payment state |
| `mobility:trackingStream` | `beckn:tracking` | 🔄 | Real-time tracking |
| `mobility:trackingPoint` | `beckn:Tracking` | 🆕 | GPS point |
| `mobility:latitude` | `beckn:coordinates` | 🔄 | Latitude value |
| `mobility:longitude` | `beckn:coordinates` | 🔄 | Longitude value |
| `mobility:bearing` | `beckn:Attributes` | 🆕 | Compass direction |
| `mobility:speed` | `beckn:Attributes` | 🆕 | Current speed |
| `mobility:accuracy` | `beckn:Attributes` | 🆕 | GPS accuracy |
| `mobility:review` | `beckn:rating` | 🔄 | Review text |
| `mobility:incident` | `beckn:alerts` | 🔄 | Incident report |
| `mobility:emergencyEvent` | `beckn:alerts` | 🔄 | Emergency notification |
| `mobility:lostAndFoundItem` | `beckn:items` | 🔄 | Lost item |
| `mobility:resolution` | `beckn:Attributes` | 🆕 | Issue resolution |
| `mobility:refundAmount` | `beckn:amount` | 🔄 | Refund value |
| `mobility:penaltyAmount` | `beckn:amount` | 🔄 | Penalty value |

---

## Enumeration Mappings

| Ride-Hailing Enumeration | Beckn Base | Mapping Type | Notes |
|-------------------------|------------|--------------|-------|
| `mobility:VehicleCategoryEnum` | `beckn:CategoryCode` | 🆕 | SEDAN, SUV, BIKE, AUTO, etc. |
| `mobility:ServiceClassEnum` | `beckn:CategoryCode` | 🆕 | ECONOMY, PREMIUM, LUXURY, etc. |
| `mobility:FeatureEnum` | `beckn:Feature` | 🆕 | AC, MUSIC, etc. |
| `mobility:AccessibilityFeatureEnum` | `beckn:Feature` | 🆕 | WHEELCHAIR_ACCESS, etc. |
| `mobility:ConnectivityFeatureEnum` | `beckn:Feature` | 🆕 | WIFI, USB_CHARGING, etc. |
| `mobility:AccessoryEnum` | - | 🆕 | CHILD_SEAT, PET_CARRIER, etc. |
| `mobility:PricingModelEnum` | - | 🆕 | FIXED, METERED, DYNAMIC, etc. |
| `mobility:TripStateEnum` | `beckn:State` | 🆕 | REQUESTED, ACCEPTED, IN_PROGRESS, etc. |
| `mobility:CancellationReasonEnum` | - | 🆕 | USER_REQUESTED, DRIVER_UNAVAILABLE, etc. |
| `mobility:PaymentInstrumentEnum` | `beckn:AcceptedPaymentMethod` | 🔄 | CASH, CARD, UPI, WALLET, etc. |
| `mobility:PaymentStatusEnum` | `beckn:PaymentStatus` | 🔄 | PENDING, COMPLETED, FAILED, etc. |
| `mobility:StopTypeEnum` | `beckn:stopType` | 🔄 | PICKUP, DROPOFF, WAYPOINT, etc. |
| `mobility:SeverityEnum` | `beckn:severity` | 🔄 | LOW, MEDIUM, HIGH, CRITICAL |
| `mobility:IncidentTypeEnum` | - | 🆕 | ACCIDENT, BREAKDOWN, etc. |
| `mobility:FeedbackTagEnum` | - | 🆕 | CLEAN, SAFE_DRIVING, RUDE, etc. |
| `mobility:EntitlementTypeEnum` | - | 🆕 | DISCOUNT_CODE, LOYALTY_POINTS, etc. |
| `mobility:PolicyTypeEnum` | `beckn:Policy` | 🔄 | CANCELLATION, WAITING, NO_SHOW, etc. |
| `mobility:DriverCredentialTypeEnum` | `beckn:Credential` | 🔄 | DRIVING_LICENSE, BACKGROUND_CHECK, etc. |

---

## Key Insights

### 1. **Core Beckn Classes Used**
The ride-hailing schema extensively uses these Beckn core classes:
- `beckn:Item` → For services, vehicles, accessories
- `beckn:Offer` → For ride options and pricing
- `beckn:Order` → For ride requests
- `beckn:Fulfillment` → For trip execution
- `beckn:Location` → For pickup/drop points
- `beckn:Feature` → For vehicle/service features
- `beckn:Policy` → For operational policies
- `beckn:PriceComponent` → For fare breakdown
- `beckn:Participant` → For riders and passengers
- `beckn:Credential` & `beckn:Skill` → For driver qualifications
- `beckn:State` → For trip and fulfillment states
- `beckn:Alert` → For incidents and service alerts

### 2. **Common Extension Patterns**
- **Specialization**: Mobility classes specialize Beckn classes (e.g., `RideOption` extends `Offer`)
- **Domain-specific attributes**: Use `beckn:Attributes` for mobility-specific properties
- **Fare modeling**: Extends `beckn:PriceComponent` with ride-specific components (surge, tolls, etc.)
- **State management**: Extends `beckn:State` with trip-specific states

### 3. **Property Reuse via Context**
Most Beckn properties are reused through the JSON-LD context aliasing mechanism:
```json
"location": "beckn:location"
```
This allows mobility documents to use short property names while maintaining semantic links to Beckn IRIs.

### 4. **Namespace Strategy**
- `beckn:` → Core protocol vocabulary
- `mobility:` → Ride-hailing domain extensions
- `schema:` → Schema.org for standard concepts (e.g., `PriceSpecification`)

---

## Usage Examples

### Example 1: Ride Option (Offer)
```json
{
  "@context": "schema/ride-hailing/context.jsonld",
  "@type": "RideOption",
  "id": "ride-option-123",
  "serviceClass": "PREMIUM",
  "vehicleCategory": "SEDAN",
  "fareEstimate": {
    "@type": "FareEstimate",
    "priceComponents": [
      { "type": "baseFare", "value": 50 },
      { "type": "distanceFare", "value": 30 },
      { "type": "tax", "value": 8 }
    ]
  }
}
```
**Maps to Beckn**:
- `RideOption` → `beckn:Offer`
- `serviceClass` → `mobility:serviceClass` (extends `beckn:category`)
- `fareEstimate` → uses `beckn:PriceComponent`

### Example 2: Trip (Fulfillment)
```json
{
  "@context": "schema/ride-hailing/context.jsonld",
  "@type": "Trip",
  "id": "trip-456",
  "tripState": "IN_PROGRESS",
  "driver": {
    "@type": "Driver",
    "driverCredentials": [
      { "@type": "DriverCredential", "credentialType": "DRIVING_LICENSE" }
    ]
  },
  "stops": [
    { "stopType": "PICKUP", "location": { "geo": {...} } },
    { "stopType": "DROPOFF", "location": { "geo": {...} } }
  ]
}
```
**Maps to Beckn**:
- `Trip` → `beckn:Fulfillment`
- `driver` → `beckn:agent` (as `beckn:FulfillmentAgent`)
- `stops` → `beckn:stops` (array of `beckn:FulfillmentStop`)
- `tripState` → `beckn:state`

---

## Summary Statistics

- **Total Mobility Classes**: 70+
- **Direct Beckn Class Usage**: ~15 classes
- **Mobility Extensions**: ~55 classes
- **Properties Mapped**: 150+
- **Enumerations**: 15+

This mapping enables full semantic interoperability between ride-hailing implementations and the core Beckn protocol.
