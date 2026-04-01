# FareProduct

A schema.beckn.io Type

A purchasable entitlement to travel defining conditions of use, validity, and applicable passenger categories.

**Canonical IRI :** `mobility:FareProduct`

**Canonical URL:** https://schema.beckn.io/mobility/FareProduct

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Offer](https://github.com/beckn/core_schema/tree/draft/schema/Offer) | owl:equivalentClass | Exact |
| [schema:Offer](https://schema.org/Offer) | rdfs:seeAlso | Related |
| [schema:Product](https://schema.org/Product) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from FareProduct](https://schema.beckn.io/mobility/FareProduct)** | | |
| [fareProductId](https://schema.beckn.io/mobility/fareProductId) | [schema:Text](https://schema.org/Text) | Unique identifier for the fare product |
| [riderCategoryId](https://schema.beckn.io/mobility/riderCategoryId) | [RiderCategory](https://schema.beckn.io/mobility/RiderCategory) | Passenger category eligible for this fare product |
| [durationType](https://schema.beckn.io/mobility/durationType) | [schema:Text](https://schema.org/Text) | Duration basis (e.g. SINGLE_TRIP, DAILY, MONTHLY) |
| [mediaDuration](https://schema.beckn.io/mobility/mediaDuration) | [schema:Duration](https://schema.org/Duration) | Duration for which the fare product is valid |
| [fixedStartDate](https://schema.beckn.io/mobility/fixedStartDate) | [schema:DateTime](https://schema.org/DateTime) | Fixed start date for calendar-based fare products |
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
