# BikeAllowed

A schema.beckn.io Type

An indicator specifying whether bicycles are permitted on board a particular route or vehicle journey.

**Canonical IRI :** `mobility:BikeAllowed`

**Canonical URL:** https://schema.beckn.io/mobility/BikeAllowed

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Feature](https://github.com/beckn/core_schema/tree/draft/schema/Feature) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from BikeAllowed](https://schema.beckn.io/mobility/BikeAllowed)** | | |
| [bikeAllowedValue](https://schema.beckn.io/mobility/bikeAllowedValue) | [schema:Text](https://schema.org/Text) | Indicates whether bikes are allowed: yes, no, or unknown |
| **[Properties from Feature](https://schema.beckn.io/core/Feature)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the feature |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable label of the feature |
| [value](https://schema.beckn.io/core/value) | [schema:Text](https://schema.org/Text) | Value of the feature (e.g. yes, no, unknown) |

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
