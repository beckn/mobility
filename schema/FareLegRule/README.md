# FareLegRule

A schema.beckn.io Type

A rule defining how a fare is applied to a single leg of a journey based on origin, destination, network, and time.

**Canonical IRI :** `mobility:FareLegRule`

**Canonical URL:** https://schema.beckn.io/mobility/FareLegRule

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
| **[Properties from FareLegRule](https://schema.beckn.io/mobility/FareLegRule)** | | |
| [fareProductId](https://schema.beckn.io/mobility/fareProductId) | [schema:Text](https://schema.org/Text) | Identifier of the fare product this rule applies to |
| [legGroupId](https://schema.beckn.io/mobility/legGroupId) | [schema:Text](https://schema.org/Text) | Leg group identifier for grouping related rules |
| [networkId](https://schema.beckn.io/mobility/networkId) | [schema:Text](https://schema.org/Text) | Network to which this rule is restricted |
| [fromAreaId](https://schema.beckn.io/mobility/fromAreaId) | [TariffZone](https://schema.beckn.io/mobility/TariffZone) | Origin tariff zone for this fare leg rule |
| [toAreaId](https://schema.beckn.io/mobility/toAreaId) | [TariffZone](https://schema.beckn.io/mobility/TariffZone) | Destination tariff zone for this fare leg rule |
| [containsServiceId](https://schema.beckn.io/mobility/containsServiceId) | [Route](https://schema.beckn.io/mobility/Route) | Specific route this rule applies to |
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
