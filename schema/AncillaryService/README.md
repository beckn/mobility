# AncillaryService

A schema.beckn.io Type

An optional or additional service available for purchase alongside base transport, such as extra baggage or lounge access.

**Canonical IRI :** `mobility:AncillaryService`

**Canonical URL:** https://schema.beckn.io/mobility/AncillaryService

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Offer](https://github.com/beckn/core_schema/tree/draft/schema/Offer) | rdfs:subClassOf | Subclass |
| [schema:Service](https://schema.org/Service) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from AncillaryService](https://schema.beckn.io/mobility/AncillaryService)** | | |
| [serviceCode](https://schema.beckn.io/mobility/serviceCode) | [schema:Text](https://schema.org/Text) | IATA service code (e.g. BG for extra baggage) |
| [serviceCategory](https://schema.beckn.io/mobility/serviceCategory) | [schema:Text](https://schema.org/Text) | Category of the ancillary service |
| [maxQuantity](https://schema.beckn.io/mobility/maxQuantity) | [schema:Number](https://schema.org/Number) | Maximum quantity of this service that can be purchased |
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
