# Rating

A schema.beckn.io Type

A numerical or categorical score assigned by a user to a driver, vehicle, or mobility service experience.

**Canonical IRI :** `mobility:Rating`

**Canonical URL:** https://schema.beckn.io/mobility/Rating

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:RatingInput](https://github.com/beckn/core_schema/tree/draft/schema/RatingInput) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Rating](https://schema.beckn.io/mobility/Rating)** | | |
| [ratedEntityId](https://schema.beckn.io/mobility/ratedEntityId) | [schema:Text](https://schema.org/Text) | Identifier of the entity being rated (driver, vehicle, service) |
| [ratedEntityType](https://schema.beckn.io/mobility/ratedEntityType) | [schema:Text](https://schema.org/Text) | Type of entity being rated (DRIVER, VEHICLE, SERVICE) |
| [comment](https://schema.beckn.io/mobility/comment) | [schema:Text](https://schema.org/Text) | Optional text comment accompanying the rating |
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
