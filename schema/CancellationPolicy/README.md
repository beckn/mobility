# CancellationPolicy

A schema.beckn.io Type

A policy defining the terms and conditions under which a transport booking can be cancelled, including applicable refund percentages and cancellation deadlines.

**Canonical IRI :** `mobility:CancellationPolicy`

**Canonical URL:** https://schema.beckn.io/mobility/CancellationPolicy

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:CancellationPolicy](https://github.com/beckn/core_schema/tree/draft/schema/CancellationPolicy) | owl:equivalentClass | Exact |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from CancellationPolicy](https://schema.beckn.io/mobility/CancellationPolicy)** | | |
| [cancellationFee](https://schema.beckn.io/mobility/cancellationFee) | [schema:Number](https://schema.org/Number) | Flat cancellation fee charged upon cancellation |
| [gracePeriodMinutes](https://schema.beckn.io/mobility/gracePeriodMinutes) | [schema:Number](https://schema.org/Number) | Number of minutes after booking during which cancellation is free |
| [fareComponent](https://schema.beckn.io/mobility/fareComponent) | [FareBreakup](https://schema.beckn.io/mobility/FareBreakup) | Fare components affected by this cancellation policy |
| **[Properties from CancellationPolicy](https://github.com/beckn/core_schema/tree/draft/schema/CancellationPolicy)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the cancellation policy |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the policy |
| [cancellationTerms](https://schema.beckn.io/core/cancellationTerms) | [schema:Text](https://schema.org/Text) | Terms and conditions governing cancellation |
| [refundPercentage](https://schema.beckn.io/core/refundPercentage) | [schema:Number](https://schema.org/Number) | Percentage of the fare refunded on cancellation |
| [cancelByTime](https://schema.beckn.io/core/cancelByTime) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Deadline by which cancellation must be made |

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
