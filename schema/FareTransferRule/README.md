# FareTransferRule

A schema.beckn.io Type

A rule defining how fares from different legs are combined when a passenger makes a transfer between services.

**Canonical IRI :** `mobility:FareTransferRule`

**Canonical URL:** https://schema.beckn.io/mobility/FareTransferRule

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Policy](https://github.com/beckn/core_schema/tree/draft/schema/Policy) | rdfs:subClassOf | Subclass |
| [mobility:FareProduct](https://schema.beckn.io/mobility/FareProduct) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from FareTransferRule](https://schema.beckn.io/mobility/FareTransferRule)** | | |
| [fareProductId](https://schema.beckn.io/mobility/fareProductId) | [schema:Text](https://schema.org/Text) | Identifier of the fare product this transfer rule applies to |
| [transferCount](https://schema.beckn.io/mobility/transferCount) | [schema:Number](https://schema.org/Number) | Number of transfers permitted under this rule |
| [durationLimit](https://schema.beckn.io/mobility/durationLimit) | [schema:Number](https://schema.org/Number) | Maximum duration in minutes for the transfer window |
| [fareTransferType](https://schema.beckn.io/mobility/fareTransferType) | [schema:Text](https://schema.org/Text) | Type of fare adjustment on transfer (e.g. FREE, DISCOUNT, ADDITIONAL_FARE) |
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
