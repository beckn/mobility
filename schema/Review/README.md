# Review

A schema.beckn.io Type

A written review or opinion submitted by a passenger about a completed mobility service, driver, or vehicle.

**Canonical IRI :** `mobility:Review`

**Canonical URL:** https://schema.beckn.io/mobility/Review

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:RatingInput](https://github.com/beckn/core_schema/tree/draft/schema/RatingInput) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Review](https://schema.beckn.io/mobility/Review)** | | |
| [reviewText](https://schema.beckn.io/mobility/reviewText) | [schema:Text](https://schema.org/Text) | The written text of the review |
| [reviewedAt](https://schema.beckn.io/mobility/reviewedAt) | [schema:DateTime](https://schema.org/DateTime) | Date and time the review was submitted |
| [reviewer](https://schema.beckn.io/mobility/reviewer) | [Rider](https://schema.beckn.io/mobility/Rider) | The passenger who submitted this review |
| **[Properties from RatingInput](https://github.com/beckn/core_schema/tree/draft/schema/RatingInput)** | | |
| [target](https://schema.beckn.io/core/target) | [schema:Text](https://schema.org/Text) | The entity being rated, with id and category (Order, Fulfillment, Provider, Agent) |
| [range](https://schema.beckn.io/core/range) | [schema:Text](https://schema.org/Text) | Rating scale definition (numeric range or descriptor array) |
| [ratingValue](https://schema.beckn.io/core/ratingValue) | [schema:Number](https://schema.org/Number) | Numeric rating value selected by the user |
| [feedback](https://schema.beckn.io/core/feedback) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Textual feedback or written review accompanying the rating |

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
