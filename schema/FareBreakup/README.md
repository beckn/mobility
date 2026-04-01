# FareBreakup

A schema.beckn.io Type

A detailed breakdown of the total fare into its constituent components, including base fare, taxes, surcharges, and discounts.

**Canonical IRI :** `mobility:FareBreakup`

**Canonical URL:** https://schema.beckn.io/mobility/FareBreakup

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:PriceComponent](https://github.com/beckn/core_schema/tree/draft/schema/PriceComponent) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from FareBreakup](https://schema.beckn.io/mobility/FareBreakup)** | | |
| [componentTitle](https://schema.beckn.io/mobility/componentTitle) | [schema:Text](https://schema.org/Text) | Human-readable title for this fare component |
| [amount](https://schema.beckn.io/mobility/amount) | [schema:Number](https://schema.org/Number) | Monetary amount for this fare component |
| [currency](https://schema.beckn.io/mobility/currency) | [schema:Text](https://schema.org/Text) | ISO 4217 currency code for this component |
| [taxAmount](https://schema.beckn.io/mobility/taxAmount) | [schema:Number](https://schema.org/Number) | Tax amount included in this component |
| [taxRate](https://schema.beckn.io/mobility/taxRate) | [schema:Number](https://schema.org/Number) | Tax rate percentage applied |
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
