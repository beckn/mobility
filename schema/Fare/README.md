# Fare

A schema.beckn.io Type

The monetary cost of travel for a specific journey or service, calculated based on applicable fare rules and passenger categories.

**Canonical IRI :** `mobility:Fare`

**Canonical URL:** https://schema.beckn.io/mobility/Fare

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
| **[Properties from Fare](https://schema.beckn.io/mobility/Fare)** | | |
| [fareId](https://schema.beckn.io/mobility/fareId) | [schema:Text](https://schema.org/Text) | Unique identifier for the fare |
| [amount](https://schema.beckn.io/mobility/amount) | [schema:Number](https://schema.org/Number) | Total fare amount |
| [currency](https://schema.beckn.io/mobility/currency) | [schema:Text](https://schema.org/Text) | ISO 4217 currency code |
| [fareAttributes](https://schema.beckn.io/mobility/fareAttributes) | [schema:Text](https://schema.org/Text) | Transfer permissions, agency, and transfer limit |
| [fareRules](https://schema.beckn.io/mobility/fareRules) | [FareLegRule](https://schema.beckn.io/mobility/FareLegRule) | Leg rules that determine when this fare applies |
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
