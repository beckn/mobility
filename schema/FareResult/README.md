# FareResult

A schema.beckn.io Type

The calculated fare for a requested trip, returned as part of a trip planning or fare enquiry response.

**Canonical IRI :** `mobility:FareResult`

**Canonical URL:** https://schema.beckn.io/mobility/FareResult

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Offer](https://github.com/beckn/core_schema/tree/draft/schema/Offer) | rdfs:subClassOf | Subclass |
| [schema:PriceSpecification](https://schema.org/PriceSpecification) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from FareResult](https://schema.beckn.io/mobility/FareResult)** | | |
| [totalAmount](https://schema.beckn.io/mobility/totalAmount) | [schema:Number](https://schema.org/Number) | Total calculated fare amount |
| [currency](https://schema.beckn.io/mobility/currency) | [schema:Text](https://schema.org/Text) | ISO 4217 currency code |
| [fareProducts](https://schema.beckn.io/mobility/fareProducts) | [FareProduct](https://schema.beckn.io/mobility/FareProduct) | Fare products applicable to the result |
| [fareBreakup](https://schema.beckn.io/mobility/fareBreakup) | [FareBreakup](https://schema.beckn.io/mobility/FareBreakup) | Itemised breakdown of the calculated fare |
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
