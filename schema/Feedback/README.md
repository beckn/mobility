# Feedback

A schema.beckn.io Type

A passenger's qualitative assessment or textual comment about a completed trip, driver, or mobility service.

**Canonical IRI :** `mobility:Feedback`

**Canonical URL:** https://schema.beckn.io/mobility/Feedback

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Feedback](https://github.com/beckn/core_schema/tree/draft/schema/Feedback) | owl:equivalentClass | Exact |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Feedback](https://schema.beckn.io/mobility/Feedback)** | | |
| [feedbackText](https://schema.beckn.io/mobility/feedbackText) | [schema:Text](https://schema.org/Text) | Textual content of the feedback |
| [feedbackType](https://schema.beckn.io/mobility/feedbackType) | [schema:Text](https://schema.org/Text) | Category of feedback (e.g. COMPLIMENT, COMPLAINT, SUGGESTION) |
| [serviceComponent](https://schema.beckn.io/mobility/serviceComponent) | [schema:Text](https://schema.org/Text) | Component of the service being reviewed (e.g. DRIVER, VEHICLE, APP) |
| **[Properties from Feedback](https://github.com/beckn/core_schema/tree/draft/schema/Feedback)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the feedback |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Feedback content and form |
| [rating](https://schema.beckn.io/core/rating) | [Rating](https://github.com/beckn/core_schema/tree/draft/schema/Rating) | Rating associated with this feedback |

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
