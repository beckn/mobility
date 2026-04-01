# PricingModel

A schema.beckn.io Type

The pricing structure or tariff model used by a mobility service provider to calculate fares.

**Canonical IRI :** `mobility:PricingModel`

**Canonical URL:** https://schema.beckn.io/mobility/PricingModel

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Offer](https://github.com/beckn/core_schema/tree/draft/schema/Offer) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from PricingModel](https://schema.beckn.io/mobility/PricingModel)** | | |
| [modelType](https://schema.beckn.io/mobility/modelType) | [schema:Text](https://schema.org/Text) | Type of pricing model (e.g. FIXED, METERED, SUBSCRIPTION, SURGE) |
| [baseRate](https://schema.beckn.io/mobility/baseRate) | [schema:Number](https://schema.org/Number) | Base fare charged at the start of a trip |
| [perMinuteRate](https://schema.beckn.io/mobility/perMinuteRate) | [schema:Number](https://schema.org/Number) | Additional charge per minute of travel |
| [perKmRate](https://schema.beckn.io/mobility/perKmRate) | [schema:Number](https://schema.org/Number) | Additional charge per kilometre of travel |
| [currency](https://schema.beckn.io/mobility/currency) | [schema:Text](https://schema.org/Text) | ISO 4217 currency code |
| [surgeEnabled](https://schema.beckn.io/mobility/surgeEnabled) | [schema:Boolean](https://schema.org/Boolean) | Whether surge pricing can be applied |
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
