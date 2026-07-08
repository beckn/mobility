# Mobility Ontology Documentation

## Overview

This document describes the **Mobility Ontology** for ride-hailing services, defined in `schema/ride-hailing/vocab.jsonld`. The ontology provides a comprehensive semantic model for representing all aspects of ride-hailing operations, from service discovery to trip fulfillment, pricing, and post-trip activities.

The ontology is defined using JSON-LD (JSON for Linking Data) and follows RDF/RDFS standards for semantic web interoperability.

## Namespace

- **Prefix**: `mobility`
- **URI**: `./vocab.jsonld#`
- **Standard vocabularies used**: RDF, RDFS, XSD

## Ontology Structure

The ontology is organized into several conceptual domains:

1. **Core Foundation Classes** - Base entity types
2. **Service & Offerings** - Service descriptions and options
3. **Trip Management** - Request, booking, and fulfillment
4. **Location & Geography** - Places, points, and routing
5. **Actors** - Participants in the system
6. **Vehicles & Features** - Vehicle categories and amenities
7. **Policies** - Rules and governance
8. **Pricing & Payments** - Fare models and breakdowns
9. **Events & Feedback** - Operational events and ratings
10. **Telemetry & Tracking** - Real-time location tracking
11. **State Management** - Lifecycle states

---

## 1. Core Foundation Classes

These are the top-level abstract classes that form the foundation of the ontology.

### MobilityEntity
**Type**: `rdfs:Class`  
**Description**: Top-level class for all ride-hailing mobility ontology entities.  
**Purpose**: Root class from which all other domain entities inherit.

### Actor
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: An entity (person/organization/software agent) that participates in a ride-hailing transaction.  
**Examples**: Riders, Drivers

### Artifact
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A created artifact/document/token produced or consumed during a transaction.  
**Examples**: Receipts, credentials, instructions, documents

### OperationalEvent
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: An operational event that occurs during the lifecycle of a ride.  
**Examples**: Incidents, emergencies, alerts

### Feature
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A capability/amenity/characteristic applicable to a service, vehicle, or experience.  
**Examples**: WiFi, wheelchair accessibility, child seat

### Constraint
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A quantitative or qualitative constraint or limit applicable to an offering or fulfillment.

### State
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A state value within a state machine for ride or fulfillment lifecycle.  
**Examples**: Trip states (requested, in_progress, completed)

---

## 2. Service & Offerings

### RideHailingService
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A service offering on-demand ride-hailing trips.  
**Purpose**: Represents the overall service provided by a platform.

### RideOption
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A selectable option representing a service class + vehicle category + pricing basis.  
**Purpose**: Represents a bookable ride product (e.g., "Economy Sedan", "Premium SUV")

**Key Properties**:
- `serviceClass` → ServiceClass
- `vehicleCategory` → VehicleCategory
- `features` → Feature collection
- `accessibilityFeatures` → AccessibilityFeature collection

### ServiceClass
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A tier/class of service (economy/premium/pool/XL).  
**Examples**: Economy, Premium, Shared

---

## 3. Trip Management

### RideRequest
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A rider's intent specifying pickup/drop, time, preferences and constraints.

**Key Properties**:
- `pickupPoint` → PickupDropoffPoint
- `dropoffPoint` → PickupDropoffPoint
- `waypoints` → PickupDropoffPoint (multiple)
- `requestedPickupTime` → xsd:dateTime
- `pickupTimeWindow` → TimeWindow
- `passengerGroup` → PassengerGroup
- `luggageCount` → xsd:integer
- `otpRequired` → xsd:boolean

### Trip
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A booked ride instance representing the operational fulfillment of a ride request.

**Key Properties**:
- `itinerary` → TripItinerary
- `driver` → Driver
- `vehicle` → Vehicle
- `tripState` → TripStateEnum
- `eta` → xsd:dateTime
- `waitingTime` → Quantity
- `waitingCharge` → MoneyAmount
- `surgeMultiplier` → xsd:decimal
- `receipt` → Receipt
- `trackingStream` → TelemetryStream

### TripItinerary
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A structured itinerary of a trip: ordered stops and legs with estimates.

**Key Properties**:
- `stops` → FulfillmentStop (ordered collection)

### TripLeg
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A segment/leg within a trip (supports waypoints and shared rides).

### FulfillmentStop
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A typed stop in an itinerary (pickup/dropoff/waypoint/stand).

**Key Properties**:
- `arrivalTime` → xsd:dateTime
- `departureTime` → xsd:dateTime
- `eta` → xsd:dateTime

---

## 4. Location & Geography

### PickupDropoffPoint
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A precise pickup/drop point including location reference, geofence and instructions.

### StopPlace
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A named stop/stand/hub/station used as a reference location.

### LocationRef
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A stable reference to a location such as a stand id, POI id, or platform id.

### GeoPoint
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A latitude/longitude point.

### Geofence
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A geographic fence (polygon/circle) constraining pickup/drop/serviceability.

### Route
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A route representation used for constrained, pooled, or suggested routing.

---

## 5. Actors

### Rider
**Type**: `rdfs:Class`  
**Subclass of**: `Actor`  
**Description**: The beneficiary/consumer of the trip (may differ from payer).

### Driver
**Type**: `rdfs:Class`  
**Subclass of**: `Actor`  
**Description**: The operational actor who drives/runs the ride-hailing vehicle.

### DriverIdentity
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: Identity attributes presented to riders (masked contact, display name, photo ref).

### DriverCredential
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: A credential/verification artifact for a driver (license, badge, check).

### DriverSkill
**Type**: `rdfs:Class`  
**Subclass of**: `Feature`  
**Description**: A skill/capability of a driver.

### PassengerGroup
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: Party composition and passenger category counts.

### ContactHandle
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A contact endpoint with masking/consent attributes.

---

## 6. Vehicles & Features

### Vehicle
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A vehicle assigned to a trip (category, registration, make/model, attributes).

**Key Properties**:
- `vehiclePlate` → xsd:string
- `features` → Feature collection
- `vehicleFeatures` → VehicleFeature collection

### VehicleCategory
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A category descriptor for ride-hailing vehicles.  
**Examples**: Sedan, Auto-rickshaw, Bike, SUV

### VehicleFeature
**Type**: `rdfs:Class`  
**Subclass of**: `Feature`  
**Description**: A vehicle amenity/capability feature.  
**Examples**: Air conditioning, leather seats, sunroof

### AccessibilityFeature
**Type**: `rdfs:Class`  
**Subclass of**: `Feature`  
**Description**: An accessibility capability applicable to vehicle/service.  
**Examples**: Wheelchair accessible, ramp, audio assistance

### ConnectivityFeature
**Type**: `rdfs:Class`  
**Subclass of**: `Feature`  
**Description**: A connectivity/digital amenity feature.  
**Examples**: WiFi, USB charging, Bluetooth

### Accessory
**Type**: `rdfs:Class`  
**Subclass of**: `Feature`  
**Description**: A physical accessory offered or required (helmet/child-seat).

---

## 7. Policies

### Policy
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: A set of rules or terms governing behavior, charges, and constraints.

### OperationalPolicy
**Type**: `rdfs:Class`  
**Subclass of**: `Policy`  
**Description**: A policy artifact applicable to a ride lifecycle.

### WaitingPolicy
**Type**: `rdfs:Class`  
**Subclass of**: `OperationalPolicy`  
**Description**: Rules for waiting time, grace periods, and waiting charges.

### NoShowPolicy
**Type**: `rdfs:Class`  
**Subclass of**: `OperationalPolicy`  
**Description**: Rules for rider/driver no-show handling and penalties.

### CancellationPolicy
**Type**: `rdfs:Class`  
**Subclass of**: `OperationalPolicy`  
**Description**: Rules for cancellations and penalties/refunds.

### PickupPolicy
**Type**: `rdfs:Class`  
**Subclass of**: `OperationalPolicy`  
**Description**: Rules for pickup behavior (zones, meet points, verification).

### DropPolicy
**Type**: `rdfs:Class`  
**Subclass of**: `OperationalPolicy`  
**Description**: Rules for dropoff behavior (restrictions, toll handling).

### SafetyPolicy
**Type**: `rdfs:Class`  
**Subclass of**: `OperationalPolicy`  
**Description**: Safety-related rules and emergency protocols.

### Instruction
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: Operational instruction text or structured directive.

---

## 8. Pricing & Payments

### PricingModel
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: The pricing basis used to compute fares (upfront, metered, time-distance).

### FareEstimate
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A pre-booking quote or estimate under assumptions.

**Key Properties**:
- `fareBreakup` → FareBreakup
- `surgeMultiplier` → xsd:decimal

### FareBreakup
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A line-item breakup of the fare.

**Key Properties**:
- `priceComponents` → PriceComponent collection

### PriceComponent
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A single line item in a fare breakup.

**Subtypes**:
- **TollCharge**: A toll line-item component
- **Surcharge**: A surcharge line-item (airport/peak/platform fee)
- **Discount**: A discount line-item
- **Tax**: A tax line-item

### PaymentInstrument
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: Payment method descriptor.

### Receipt
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: Ride receipt/invoice summary for rider.

**Key Properties**:
- `fareBreakup` → FareBreakup

---

## 9. Events & Feedback

### Entitlement
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: A token/voucher/coupon/pass/permit representing rights or benefits.

### Coupon
**Type**: `rdfs:Class`  
**Subclass of**: `Entitlement`  
**Description**: A coupon/promo entitlement.

### Alert
**Type**: `rdfs:Class`  
**Subclass of**: `OperationalEvent`  
**Description**: A notification about an issue, disruption, or notable situation affecting a ride.

### ServiceAlert
**Type**: `rdfs:Class`  
**Subclass of**: `Alert`  
**Description**: Alert affecting a ride (driver delayed, reroute, service disruption).

### Incident
**Type**: `rdfs:Class`  
**Subclass of**: `OperationalEvent`  
**Description**: An incident during or about a ride (safety issue, dispute, accident).

### EmergencyEvent
**Type**: `rdfs:Class`  
**Subclass of**: `OperationalEvent`  
**Description**: An emergency/SOS event.

### SupportCase
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: A support ticket/case raised post-fulfillment.

### Rating
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: Numeric rating provided post-fulfillment.

### Review
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: Textual review provided post-fulfillment.

### Feedback
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: Structured feedback tags/reasons.

### LostAndFoundItem
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: Lost item report artifact.

---

## 10. Telemetry & Tracking

### Telemetry
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: Telemetry and tracking related entities.

### TelemetryStream
**Type**: `rdfs:Class`  
**Subclass of**: `Telemetry`  
**Description**: Tracking channel metadata (URL/channel/token).

### TrackingPoint
**Type**: `rdfs:Class`  
**Subclass of**: `Telemetry`  
**Description**: A telemetry sample point with coordinates and movement.

**Key Properties**:
- `latitude` → xsd:decimal
- `longitude` → xsd:decimal
- `timestamp` → xsd:dateTime

---

## 11. Data Types & Primitives

### MoneyAmount
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A monetary amount with currency.

### Quantity
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A numeric value with unit.

### TimeWindow
**Type**: `rdfs:Class`  
**Subclass of**: `MobilityEntity`  
**Description**: A window or tolerance of time (earliest/latest).

### DocumentRef
**Type**: `rdfs:Class`  
**Subclass of**: `Artifact`  
**Description**: A reference to an external or embedded document/media asset.

---

## 12. State Management

### TripState
**Type**: `rdfs:Class`  
**Subclass of**: `State`  
**Description**: Trip lifecycle state value.

### FulfillmentState
**Type**: `rdfs:Class`  
**Subclass of**: `State`  
**Description**: Fulfillment lifecycle state value.

---

## 13. Controlled Vocabularies (Enumerations)

The ontology defines several controlled term sets:

### VehicleCategoryEnum
**Description**: Controlled set of ride-hailing vehicle categories.  
**Example Terms**:
- `sedan` - Standard sedan car category
- `auto_rickshaw` - Three-wheeler auto-rickshaw category
- `bike` - Two-wheeler bike category

### ServiceClassEnum
**Description**: Controlled set of service class/tier values.  
**Example Terms**:
- `economy` - Economy/standard service tier
- `premium` - Premium service tier

### PricingModelEnum
**Description**: Controlled set of pricing model types.  
**Example Terms**:
- `upfront` - Upfront quoted fare model
- `metered` - Metered fare model

### TripStateEnum
**Description**: Controlled set of ride-hailing trip lifecycle state values.  
**Example Terms**:
- `requested` - Request initiated
- `driver_assigned` - Driver assigned to trip
- `in_progress` - Trip in progress
- `completed` - Trip completed

### CancellationReasonEnum
**Description**: Controlled set of cancellation/no-show reason codes.  
**Example Terms**:
- `cancelled_by_rider` - Cancelled by rider

### PaymentInstrumentEnum
**Description**: Controlled set of payment instrument types.  
**Example Terms**:
- `cash` - Cash payment

### PaymentStatusEnum
**Description**: Controlled set of payment status values.  
**Example Terms**:
- `captured` - Payment captured/settled

---

## Properties (Relationships)

### Core Relationship Properties

#### hasFeature
**Domain**: `MobilityEntity`  
**Range**: `Feature`  
**Description**: Associates an entity with one or more features.

#### hasPolicy
**Domain**: `MobilityEntity`  
**Range**: `Policy`  
**Description**: Associates an entity with one or more policies.

#### hasConstraint
**Domain**: `MobilityEntity`  
**Range**: `Constraint`  
**Description**: Associates an entity with one or more constraints.

#### hasParticipant
**Domain**: `MobilityEntity`  
**Range**: `Actor`  
**Description**: Associates a transaction/fulfillment with one or more participating actors.

#### hasEntitlement
**Domain**: `MobilityEntity`  
**Range**: `Entitlement`  
**Description**: Associates a transaction/ride with applied or issued entitlements.

#### hasInstruction
**Domain**: `MobilityEntity`  
**Range**: `Instruction`  
**Description**: Associates an entity with one or more operational instructions.

#### hasAlert
**Domain**: `MobilityEntity`  
**Range**: `Alert`  
**Description**: Associates an entity with one or more alerts.

#### hasState
**Domain**: `MobilityEntity`  
**Range**: `State`  
**Description**: Associates an entity with a state value.

### Specialized Feature Properties

All of these are subproperties of `hasFeature`:

- **serviceClass**: Associates a RideOption with a ServiceClass
- **vehicleCategory**: Associates a RideOption with a VehicleCategory
- **features**: General features collection
- **accessibilityFeatures**: Accessibility capabilities
- **vehicleFeatures**: Vehicle amenities/capabilities
- **connectivityFeatures**: Connectivity amenities
- **accessories**: Physical accessories

---

## Use Cases & Examples

### Example 1: Defining a Ride Option

```json
{
  "@type": "mobility:RideOption",
  "mobility:serviceClass": {
    "@type": "mobility:ServiceClass",
    "@id": "mobility:ServiceClassEnum/economy"
  },
  "mobility:vehicleCategory": {
    "@type": "mobility:VehicleCategory",
    "@id": "mobility:VehicleCategoryEnum/sedan"
  },
  "mobility:features": [
    {
      "@type": "mobility:VehicleFeature",
      "rdfs:label": "Air Conditioning"
    },
    {
      "@type": "mobility:AccessibilityFeature",
      "rdfs:label": "Wheelchair Accessible"
    }
  ]
}
```

### Example 2: Creating a Ride Request

```json
{
  "@type": "mobility:RideRequest",
  "mobility:pickupPoint": {
    "@type": "mobility:PickupDropoffPoint",
    "mobility:location": {
      "@type": "mobility:GeoPoint",
      "mobility:latitude": 12.9716,
      "mobility:longitude": 77.5946
    }
  },
  "mobility:dropoffPoint": {
    "@type": "mobility:PickupDropoffPoint",
    "mobility:location": {
      "@type": "mobility:GeoPoint",
      "mobility:latitude": 12.9352,
      "mobility:longitude": 77.6245
    }
  },
  "mobility:requestedPickupTime": "2024-01-15T10:00:00Z",
  "mobility:passengerGroup": {
    "@type": "mobility:PassengerGroup",
    "mobility:count": 2
  },
  "mobility:otpRequired": true
}
```

### Example 3: Trip with State and Tracking

```json
{
  "@type": "mobility:Trip",
  "mobility:tripState": {
    "@id": "mobility:TripStateEnum/in_progress"
  },
  "mobility:driver": {
    "@type": "mobility:Driver",
    "rdfs:label": "Driver 123"
  },
  "mobility:vehicle": {
    "@type": "mobility:Vehicle",
    "mobility:vehiclePlate": "KA-01-AB-1234",
    "mobility:vehicleCategory": {
      "@id": "mobility:VehicleCategoryEnum/sedan"
    }
  },
  "mobility:trackingStream": {
    "@type": "mobility:TelemetryStream",
    "mobility:trackingPoint": [
      {
        "@type": "mobility:TrackingPoint",
        "mobility:latitude": 12.9716,
        "mobility:longitude": 77.5946,
        "mobility:timestamp": "2024-01-15T10:05:00Z"
      }
    ]
  },
  "mobility:eta": "2024-01-15T10:30:00Z"
}
```

---

## Design Principles

### 1. Modularity
The ontology is organized into logical modules (actors, policies, pricing, etc.) that can be extended independently.

### 2. Extensibility
Base classes like `Feature`, `Policy`, and `Constraint` allow domain-specific extensions without modifying core structures.

### 3. Interoperability
Uses standard RDF/RDFS/XSD vocabularies ensuring compatibility with semantic web tools and linked data ecosystems.

### 4. Controlled Vocabularies
Enumerations provide standardized term sets while allowing new terms to be added as the domain evolves.

### 5. Separation of Concerns
Clear distinction between:
- **Intent** (RideRequest) vs **Fulfillment** (Trip)
- **Capabilities** (Features) vs **Rules** (Policies)
- **Actors** vs **Artifacts** vs **Events**

---

## Extension Points

The ontology can be extended in several ways:

1. **New Feature Types**: Subclass `Feature` for domain-specific capabilities
2. **New Policy Types**: Subclass `OperationalPolicy` for custom rule sets
3. **New Actor Types**: Extend `Actor` for additional participant types
4. **New Price Components**: Subclass `PriceComponent` for custom charges
5. **New Enumeration Terms**: Add terms to existing enumerations

---

## Integration with Standards

This ontology can integrate with:

- **Schema.org**: For general concepts like Place, Organization, Person
- **GeoSPARQL**: For advanced geospatial queries
- **FOAF**: For actor/agent descriptions
- **PROV-O**: For provenance tracking
- **Beckn Protocol**: As a semantic layer over Beckn messaging

---

## Conclusion

The Mobility Ontology provides a comprehensive, extensible framework for modeling ride-hailing services. Its hierarchical structure, rich property set, and controlled vocabularies enable precise representation of complex mobility scenarios while maintaining interoperability with semantic web standards.

For implementation details and JSON-LD context definitions, refer to:
- `schema/ride-hailing/vocab.jsonld` - Vocabulary definitions
- `schema/ride-hailing/context.jsonld` - JSON-LD context mappings
