# SystemPricingPlan

A schema.beckn.io Type

A pricing plan defined by a shared mobility system, describing costs and billing rules for vehicle use.

**Canonical IRI :** `mobility:SystemPricingPlan`

**Canonical URL:** https://schema.beckn.io/mobility/SystemPricingPlan

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
| **[Properties from SystemPricingPlan](https://schema.beckn.io/mobility/SystemPricingPlan)** | | |
| [planId](https://schema.beckn.io/mobility/planId) | [schema:Text](https://schema.org/Text) | Unique identifier for the pricing plan |
| [currency](https://schema.beckn.io/mobility/currency) | [schema:Text](https://schema.org/Text) | ISO 4217 currency code |
| [isTaxable](https://schema.beckn.io/mobility/isTaxable) | [schema:Boolean](https://schema.org/Boolean) | Whether tax is applied to this pricing plan |
| [perMinuteChargingRate](https://schema.beckn.io/mobility/perMinuteChargingRate) | [schema:Number](https://schema.org/Number) | Charge per minute of vehicle use |
| [perKmChargingRate](https://schema.beckn.io/mobility/perKmChargingRate) | [schema:Number](https://schema.org/Number) | Charge per kilometre of vehicle use |
| [perTripStartingFee](https://schema.beckn.io/mobility/perTripStartingFee) | [schema:Number](https://schema.org/Number) | Flat fee charged at the start of each trip |
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
