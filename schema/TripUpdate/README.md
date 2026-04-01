# TripUpdate

A schema.beckn.io Type

A multi-dimensional update to an in-progress or upcoming mobility trip, covering contract modifications (added/removed services, route changes), status notifications (driver arriving, trip started), and real-time tracking endpoint information.

**Canonical IRI :** `mobility:TripUpdate`

**Canonical URL:** https://schema.beckn.io/mobility/TripUpdate

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Contract](https://github.com/beckn/core_schema/tree/draft/schema/Contract) | rdfs:subClassOf | Subclass |
| [beckn:State](https://github.com/beckn/core_schema/tree/draft/schema/State) | rdfs:seeAlso | Related |
| [beckn:Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking) | rdfs:seeAlso | Related |
| [beckn:TrackingRequest](https://github.com/beckn/core_schema/tree/draft/schema/TrackingRequest) | rdfs:seeAlso | Related |
| [mobility:VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from TripUpdate](https://schema.beckn.io/mobility/TripUpdate)** | | |
| [contractChanges](https://schema.beckn.io/mobility/contractChanges) | [ContractItem](https://github.com/beckn/core_schema/tree/draft/schema/ContractItem) | Items added or modified in the trip contract (new stop, route change, add-on service) |
| [cancelledItems](https://schema.beckn.io/mobility/cancelledItems) | [ContractItem](https://github.com/beckn/core_schema/tree/draft/schema/ContractItem) | Items removed from the original trip contract |
| [stateUpdate](https://schema.beckn.io/mobility/stateUpdate) | [State](https://github.com/beckn/core_schema/tree/draft/schema/State) | Status notification for the traveler (e.g. driver arriving, trip started, trip ended, driver changed) |
| [trackingEndpoint](https://schema.beckn.io/mobility/trackingEndpoint) | [Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking) | Real-time tracking endpoint including URL, protocol, and data schema reference |
| [driverRef](https://schema.beckn.io/mobility/driverRef) | [Driver](https://schema.beckn.io/mobility/Driver) | Reference to the current driver if changed from the originally assigned driver |
| [updatedAt](https://schema.beckn.io/mobility/updatedAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when this trip update was issued |
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
