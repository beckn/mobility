# RideOption

A schema.beckn.io Type

A specific ride-hailing vehicle category and pricing option presented to a passenger in response to a ride request.

**Canonical IRI :** `mobility:RideOption`

**Canonical URL:** https://schema.beckn.io/mobility/RideOption

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Offer](https://github.com/beckn/core_schema/tree/draft/schema/Offer) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from RideOption](https://schema.beckn.io/mobility/RideOption)** | | |
| [vehicleType](https://schema.beckn.io/mobility/vehicleType) | [VehicleCategory](https://schema.beckn.io/mobility/VehicleCategory) | Category of vehicle for this ride option |
| [estimatedArrival](https://schema.beckn.io/mobility/estimatedArrival) | [schema:DateTime](https://schema.org/DateTime) | Estimated vehicle arrival time at the pickup point |
| [estimatedDuration](https://schema.beckn.io/mobility/estimatedDuration) | [schema:Duration](https://schema.org/Duration) | Estimated trip duration |
| [estimatedDistance](https://schema.beckn.io/mobility/estimatedDistance) | [schema:Number](https://schema.org/Number) | Estimated trip distance in kilometres |
| [pricingModel](https://schema.beckn.io/mobility/pricingModel) | [PricingModel](https://schema.beckn.io/mobility/PricingModel) | Pricing model applicable to this ride option |
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
