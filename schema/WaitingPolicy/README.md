# WaitingPolicy

A schema.beckn.io Type

Rules governing the maximum time a driver is required to wait for a passenger at the pickup location before being permitted to cancel the booking.

**Canonical IRI :** `mobility:WaitingPolicy`

**Canonical URL:** https://schema.beckn.io/mobility/WaitingPolicy

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Policy](https://github.com/beckn/core_schema/tree/draft/schema/Policy) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from WaitingPolicy](https://schema.beckn.io/mobility/WaitingPolicy)** | | |
| [freeWaitingTimeMinutes](https://schema.beckn.io/mobility/freeWaitingTimeMinutes) | [schema:Number](https://schema.org/Number) | Number of minutes the driver waits for free before charging |
| [maxWaitingTimeMinutes](https://schema.beckn.io/mobility/maxWaitingTimeMinutes) | [schema:Number](https://schema.org/Number) | Maximum total minutes the driver will wait before auto-cancelling |
| [chargePerExtraMinute](https://schema.beckn.io/mobility/chargePerExtraMinute) | [schema:Number](https://schema.org/Number) | Additional charge per minute beyond the free waiting time |
| [currency](https://schema.beckn.io/mobility/currency) | [schema:Text](https://schema.org/Text) | ISO 4217 currency code for waiting charges |
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
