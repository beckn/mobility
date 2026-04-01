# FareComponent

A schema.beckn.io Type

A component of an air travel fare that applies to a specific flight segment or leg, used in aviation pricing.

**Canonical IRI :** `mobility:FareComponent`

**Canonical URL:** https://schema.beckn.io/mobility/FareComponent

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:PriceComponent](https://github.com/beckn/core_schema/tree/draft/schema/PriceComponent) | rdfs:subClassOf | Subclass |
| [mobility:Fare](https://schema.beckn.io/mobility/Fare) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from FareComponent](https://schema.beckn.io/mobility/FareComponent)** | | |
| [fareBasisCode](https://schema.beckn.io/mobility/fareBasisCode) | [schema:Text](https://schema.org/Text) | IATA fare basis code identifying the fare type |
| [cabin](https://schema.beckn.io/mobility/cabin) | [schema:Text](https://schema.org/Text) | Cabin class (ECONOMY, BUSINESS, FIRST) |
| [bookingCode](https://schema.beckn.io/mobility/bookingCode) | [schema:Text](https://schema.org/Text) | Booking class code (e.g. Y, M, K) |
| [amount](https://schema.beckn.io/mobility/amount) | [schema:Number](https://schema.org/Number) | Fare amount for this component |
| [currency](https://schema.beckn.io/mobility/currency) | [schema:Text](https://schema.org/Text) | ISO 4217 currency code |
| [segmentRef](https://schema.beckn.io/mobility/segmentRef) | [FlightSegment](https://schema.beckn.io/mobility/FlightSegment) | Flight segment this fare component applies to |
| **[Properties from PriceComponent](https://schema.beckn.io/core/PriceComponent)** | | |
| [title](https://schema.beckn.io/core/title) | [schema:Text](https://schema.org/Text) | Title or label of this price component |
| [price](https://schema.beckn.io/core/price) | [PriceSpecification](https://github.com/beckn/core_schema/tree/draft/schema/PriceSpecification) | Monetary value of this component |
| [tags](https://schema.beckn.io/core/tags) | [schema:Text](https://schema.org/Text) | Tags associated with this price component |

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
