# RiderCategory

A schema.beckn.io Type

A classification of passenger type (e.g., adult, child, senior, student) used to determine applicable fare entitlements.

**Canonical IRI :** `mobility:RiderCategory`

**Canonical URL:** https://schema.beckn.io/mobility/RiderCategory

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:CategoryCode](https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode) | rdfs:subClassOf | Subclass |
| [schema:Person](https://schema.org/Person) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from RiderCategory](https://schema.beckn.io/mobility/RiderCategory)** | | |
| [riderCategoryId](https://schema.beckn.io/mobility/riderCategoryId) | [schema:Text](https://schema.org/Text) | Unique identifier for the rider category |
| [eligibilityRules](https://schema.beckn.io/mobility/eligibilityRules) | [schema:Text](https://schema.org/Text) | Rules defining who qualifies for this rider category |
| [proofRequired](https://schema.beckn.io/mobility/proofRequired) | [schema:Text](https://schema.org/Text) | Type of proof required to qualify (e.g. student ID, senior card) |
| **[Properties from CategoryCode](https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the category code |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable label for the category |
| [parentCategoryId](https://schema.beckn.io/core/parentCategoryId) | [schema:Text](https://schema.org/Text) | Identifier of the parent category if hierarchical |

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
