# SalesOfferPackage

A schema.beckn.io Type

A combination of one or more fare products bundled for sale through a specific distribution channel.

**Canonical IRI :** `mobility:SalesOfferPackage`

**Canonical URL:** https://schema.beckn.io/mobility/SalesOfferPackage

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Offer](https://github.com/beckn/core_schema/tree/draft/schema/Offer) | rdfs:subClassOf | Subclass |
| [schema:Offer](https://schema.org/Offer) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from SalesOfferPackage](https://schema.beckn.io/mobility/SalesOfferPackage)** | | |
| [fareProducts](https://schema.beckn.io/mobility/fareProducts) | [FareProduct](https://schema.beckn.io/mobility/FareProduct) | Fare products included in this sales package |
| [distributions](https://schema.beckn.io/mobility/distributions) | [DistributionChannel](https://schema.beckn.io/mobility/DistributionChannel) | Channels through which this package can be purchased |
| [conditionsOfTravel](https://schema.beckn.io/mobility/conditionsOfTravel) | [schema:Text](https://schema.org/Text) | Conditions applying to the use of this package |
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
