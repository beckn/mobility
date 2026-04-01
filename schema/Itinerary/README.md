# Itinerary

A schema.beckn.io Type

A complete planned trip containing an ordered sequence of legs, including transfer points, durations, and timing.

**Canonical IRI :** `mobility:Itinerary`

**Canonical URL:** https://schema.beckn.io/mobility/Itinerary

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Contract](https://github.com/beckn/core_schema/tree/draft/schema/Contract) | rdfs:subClassOf | Subclass |
| [schema:Trip](https://schema.org/Trip) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Itinerary](https://schema.beckn.io/mobility/Itinerary)** | | |
| [legs](https://schema.beckn.io/mobility/legs) | [Leg](https://schema.beckn.io/mobility/Leg) | Ordered list of legs making up this itinerary |
| [totalDuration](https://schema.beckn.io/mobility/totalDuration) | [schema:Duration](https://schema.org/Duration) | Total travel duration for the itinerary |
| [totalDistance](https://schema.beckn.io/mobility/totalDistance) | [schema:Number](https://schema.org/Number) | Total distance in metres for the itinerary |
| [transferCount](https://schema.beckn.io/mobility/transferCount) | [schema:Number](https://schema.org/Number) | Number of transfers in the itinerary |
| [departureTime](https://schema.beckn.io/mobility/departureTime) | [schema:DateTime](https://schema.org/DateTime) | Departure time of the first leg |
| [arrivalTime](https://schema.beckn.io/mobility/arrivalTime) | [schema:DateTime](https://schema.org/DateTime) | Arrival time of the last leg |
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
