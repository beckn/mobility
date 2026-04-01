# DropPolicy

A schema.beckn.io Type

A set of rules governing the locations and conditions under which passengers may be dropped off at the end of a ride-hailing or on-demand transport service.

**Canonical IRI :** `mobility:DropPolicy`

**Canonical URL:** https://schema.beckn.io/mobility/DropPolicy

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Policy](https://github.com/beckn/core_schema/tree/draft/schema/Policy) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from DropPolicy](https://schema.beckn.io/mobility/DropPolicy)** | | |
| [allowedDropAreas](https://schema.beckn.io/mobility/allowedDropAreas) | [Geofence](https://schema.beckn.io/mobility/Geofence) | Geographic areas where drop-off is permitted |
| [dropConditions](https://schema.beckn.io/mobility/dropConditions) | [schema:Text](https://schema.org/Text) | Conditions that must be met for a valid drop-off |
| [dropNote](https://schema.beckn.io/mobility/dropNote) | [schema:Text](https://schema.org/Text) | Customer-facing note about drop-off rules |
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
