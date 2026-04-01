# Transfer

A schema.beckn.io Type

A defined connection rule between two routes or services at a common stop, specifying minimum transfer time or transfer type.

**Canonical IRI :** `mobility:Transfer`

**Canonical URL:** https://schema.beckn.io/mobility/Transfer

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:FulfillmentStop](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentStop) | rdfs:subClassOf | Subclass |
| [transmodel:Interchange](https://w3id.org/transmodel/ontology#Interchange) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Transfer](https://schema.beckn.io/mobility/Transfer)** | | |
| [fromStopId](https://schema.beckn.io/mobility/fromStopId) | [Stop](https://schema.beckn.io/mobility/Stop) | Stop passengers transfer from |
| [toStopId](https://schema.beckn.io/mobility/toStopId) | [Stop](https://schema.beckn.io/mobility/Stop) | Stop passengers transfer to |
| [fromRouteId](https://schema.beckn.io/mobility/fromRouteId) | [Route](https://schema.beckn.io/mobility/Route) | Route passengers transfer from |
| [toRouteId](https://schema.beckn.io/mobility/toRouteId) | [Route](https://schema.beckn.io/mobility/Route) | Route passengers transfer to |
| [transferType](https://schema.beckn.io/mobility/transferType) | [schema:Text](https://schema.org/Text) | Type of transfer (0=recommended, 1=timed, 2=min_time, 3=not_possible) |
| [minTransferTime](https://schema.beckn.io/mobility/minTransferTime) | [schema:Number](https://schema.org/Number) | Minimum transfer time in seconds |
| **[Properties from FulfillmentStop](https://schema.beckn.io/core/FulfillmentStop)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the fulfillment stop |
| [location](https://schema.beckn.io/core/location) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Geographic location of the stop |
| [type](https://schema.beckn.io/core/type) | [schema:Text](https://schema.org/Text) | Type of stop (start, end, intermediate) |
| [instructions](https://schema.beckn.io/core/instructions) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Instructions for passengers at this stop |
| [time](https://schema.beckn.io/core/time) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Expected time window at this stop |

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
