# NoShowPolicy

A schema.beckn.io Type

Rules governing the consequences and fees applied when a passenger fails to appear for a confirmed transport service booking.

**Canonical IRI :** `mobility:NoShowPolicy`

**Canonical URL:** https://schema.beckn.io/mobility/NoShowPolicy

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Policy](https://github.com/beckn/core_schema/tree/draft/schema/Policy) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from NoShowPolicy](https://schema.beckn.io/mobility/NoShowPolicy)** | | |
| [noShowFee](https://schema.beckn.io/mobility/noShowFee) | [schema:Number](https://schema.org/Number) | Flat fee charged for a no-show |
| [gracePeriodMinutes](https://schema.beckn.io/mobility/gracePeriodMinutes) | [schema:Number](https://schema.org/Number) | Grace period in minutes before a no-show is recorded |
| [currency](https://schema.beckn.io/mobility/currency) | [schema:Text](https://schema.org/Text) | ISO 4217 currency code for the no-show fee |
| **[Properties from Policy](https://github.com/beckn/core_schema/tree/draft/schema/Policy)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the policy |
| [policyType](https://schema.beckn.io/core/policyType) | [schema:Text](https://schema.org/Text) | Type of policy (extensible term) |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the policy |
| [validity](https://schema.beckn.io/core/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Validity window for this policy version |
| [policyAttributes](https://schema.beckn.io/core/policyAttributes) | [Attributes](https://github.com/beckn/core_schema/tree/draft/schema/Attributes) | Extensible domain-specific policy attributes |

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
