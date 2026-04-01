# SafetyPolicy

A schema.beckn.io Type

A set of rules, protocols, and standards governing safety requirements for drivers, vehicles, and passengers on a mobility platform.

**Canonical IRI :** `mobility:SafetyPolicy`

**Canonical URL:** https://schema.beckn.io/mobility/SafetyPolicy

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Policy](https://github.com/beckn/core_schema/tree/draft/schema/Policy) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from SafetyPolicy](https://schema.beckn.io/mobility/SafetyPolicy)** | | |
| [safetyInstructions](https://schema.beckn.io/mobility/safetyInstructions) | [schema:Text](https://schema.org/Text) | Instructions and guidelines for passenger and driver safety |
| [emergencyContact](https://schema.beckn.io/mobility/emergencyContact) | [ContactHandle](https://schema.beckn.io/mobility/ContactHandle) | Emergency contact handle for safety incidents |
| [insuranceCoverage](https://schema.beckn.io/mobility/insuranceCoverage) | [schema:Text](https://schema.org/Text) | Description of insurance coverage under this policy |
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
