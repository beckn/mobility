# ExchangePoints

A schema.beckn.io Type

Locations in a transport network where fixed-route and flexible services connect, enabling passenger interchange.

**Canonical IRI :** `mobility:ExchangePoints`

**Canonical URL:** https://schema.beckn.io/mobility/ExchangePoints

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:FulfillmentStop](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentStop) | rdfs:subClassOf | Subclass |
| [geo:Feature](http://www.opengis.net/ont/geosparql#Feature) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from ExchangePoints](https://schema.beckn.io/mobility/ExchangePoints)** | | |
| [exchangePointType](https://schema.beckn.io/mobility/exchangePointType) | [schema:Text](https://schema.org/Text) | Type of exchange point (e.g. FIXED_TO_FLEX, FLEX_TO_FLEX) |
| [connectingServices](https://schema.beckn.io/mobility/connectingServices) | [VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney) | Services that connect at this exchange point |
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
