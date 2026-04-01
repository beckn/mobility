# Journey

A schema.beckn.io Type

A complete travel itinerary from origin to destination, potentially comprising multiple legs using different transport modes.

**Canonical IRI :** `mobility:Journey`

**Canonical URL:** https://schema.beckn.io/mobility/Journey

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
| **[Properties from Journey](https://schema.beckn.io/mobility/Journey)** | | |
| [origin](https://schema.beckn.io/mobility/origin) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Origin location of the journey |
| [destination](https://schema.beckn.io/mobility/destination) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Destination location of the journey |
| [departureTime](https://schema.beckn.io/mobility/departureTime) | [schema:DateTime](https://schema.org/DateTime) | Planned departure time |
| [arrivalTime](https://schema.beckn.io/mobility/arrivalTime) | [schema:DateTime](https://schema.org/DateTime) | Planned arrival time |
| [legs](https://schema.beckn.io/mobility/legs) | [Leg](https://schema.beckn.io/mobility/Leg) | Ordered list of legs comprising this journey |
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
