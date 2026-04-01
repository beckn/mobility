# Trip

A schema.beckn.io Type

A confirmed and booked journey from an origin to a destination, representing a completed mobility service order.

**Canonical IRI :** `mobility:Trip`

**Canonical URL:** https://schema.beckn.io/mobility/Trip

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Contract](https://github.com/beckn/core_schema/tree/draft/schema/Contract) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Trip](https://schema.beckn.io/mobility/Trip)** | | |
| [tripId](https://schema.beckn.io/mobility/tripId) | [schema:Text](https://schema.org/Text) | Unique identifier for the trip |
| [origin](https://schema.beckn.io/mobility/origin) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Pickup location |
| [destination](https://schema.beckn.io/mobility/destination) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Dropoff location |
| [startTime](https://schema.beckn.io/mobility/startTime) | [schema:DateTime](https://schema.org/DateTime) | Actual start time of the trip |
| [endTime](https://schema.beckn.io/mobility/endTime) | [schema:DateTime](https://schema.org/DateTime) | Actual end time of the trip |
| [distance](https://schema.beckn.io/mobility/distance) | [schema:Number](https://schema.org/Number) | Total distance of the trip in kilometres |
| [driverRef](https://schema.beckn.io/mobility/driverRef) | [Driver](https://schema.beckn.io/mobility/Driver) | Reference to the driver for this trip |
| [vehicleRef](https://schema.beckn.io/mobility/vehicleRef) | [Vehicle](https://schema.beckn.io/mobility/Vehicle) | Reference to the vehicle for this trip |
| **[Properties from Contract](https://github.com/beckn/core_schema/tree/draft/schema/Contract)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the contract |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the contract |
| [items](https://schema.beckn.io/core/items) | [ContractItem](https://github.com/beckn/core_schema/tree/draft/schema/ContractItem) | Line items within the contract |
| [fulfillments](https://schema.beckn.io/core/fulfillments) | [Fulfillment](https://github.com/beckn/core_schema/tree/draft/schema/Fulfillment) | Fulfillments associated with this contract |
| [state](https://schema.beckn.io/core/state) | [State](https://github.com/beckn/core_schema/tree/draft/schema/State) | Current state of the contract |

## Example

[Insert brief description of the example]

```json
[Insert Example JSON-LD]
```

## Example Beckn Protocol Requests Payload using this Schema

> [Brief description of the request with container schema, core schema, and mobility bindings]

```json
[Insert Example JSON-LD]
```
