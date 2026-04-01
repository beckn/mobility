# Entitlement

A schema.beckn.io Type

A specific right or benefit granted to a passenger or rider, such as free travel, priority boarding, or a concessionary pass.

**Canonical IRI :** `mobility:Entitlement`

**Canonical URL:** https://schema.beckn.io/mobility/Entitlement

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Entitlement](https://github.com/beckn/core_schema/tree/draft/schema/Entitlement) | owl:equivalentClass | Exact |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Entitlement](https://schema.beckn.io/mobility/Entitlement)** | | |
| [entitlementType](https://schema.beckn.io/mobility/entitlementType) | [schema:Text](https://schema.org/Text) | Type of entitlement (e.g. FREE_TRAVEL, CONCESSION, PRIORITY) |
| [eligibilityRules](https://schema.beckn.io/mobility/eligibilityRules) | [schema:Text](https://schema.org/Text) | Rules defining who is eligible for this entitlement |
| [issuingAuthority](https://schema.beckn.io/mobility/issuingAuthority) | [Authority](https://schema.beckn.io/mobility/Authority) | The authority or operator that issued this entitlement |
| [validity](https://schema.beckn.io/mobility/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Validity period of the entitlement |
| **[Properties from Entitlement](https://github.com/beckn/core_schema/tree/draft/schema/Entitlement)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the entitlement |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable information about the entitlement |
| [resource](https://schema.beckn.io/core/resource) | [ContractItem](https://github.com/beckn/core_schema/tree/draft/schema/ContractItem) | The resource being accessed against this entitlement |
| [credentials](https://schema.beckn.io/core/credentials) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Credential descriptors for the entitlement |

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
