# FareEstimate

A schema.beckn.io Type

An estimated fare for a requested trip, typically returned in response to a search before the booking is confirmed.

**Canonical IRI :** `mobility:FareEstimate`

**Canonical URL:** https://schema.beckn.io/mobility/FareEstimate

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Offer](https://github.com/beckn/core_schema/tree/draft/schema/Offer) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from FareEstimate](https://schema.beckn.io/mobility/FareEstimate)** | | |
| [estimatedAmount](https://schema.beckn.io/mobility/estimatedAmount) | [schema:Number](https://schema.org/Number) | Estimated total fare amount |
| [currency](https://schema.beckn.io/mobility/currency) | [schema:Text](https://schema.org/Text) | ISO 4217 currency code |
| [minimumAmount](https://schema.beckn.io/mobility/minimumAmount) | [schema:Number](https://schema.org/Number) | Minimum possible fare |
| [maximumAmount](https://schema.beckn.io/mobility/maximumAmount) | [schema:Number](https://schema.org/Number) | Maximum possible fare |
| [fareBreakup](https://schema.beckn.io/mobility/fareBreakup) | [FareBreakup](https://schema.beckn.io/mobility/FareBreakup) | Itemised breakdown of the estimated fare |
| **[Properties from Offer](https://github.com/beckn/core_schema/tree/draft/schema/Offer)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the offer |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the offer |
| [price](https://schema.beckn.io/core/price) | [PriceSpecification](https://github.com/beckn/core_schema/tree/draft/schema/PriceSpecification) | Price specification for this offer |
| [validity](https://schema.beckn.io/core/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Validity period of the offer |
| [tags](https://schema.beckn.io/core/tags) | [schema:Text](https://schema.org/Text) | Tags or labels associated with the offer |

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
