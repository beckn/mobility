# FareMedium

A schema.beckn.io Type

The physical or digital medium used to carry or present a fare product, such as a contactless card, mobile app, or paper ticket.

**Canonical IRI :** `mobility:FareMedium`

**Canonical URL:** https://schema.beckn.io/mobility/FareMedium

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Entitlement](https://github.com/beckn/core_schema/tree/draft/schema/Entitlement) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from FareMedium](https://schema.beckn.io/mobility/FareMedium)** | | |
| [mediumType](https://schema.beckn.io/mobility/mediumType) | [schema:Text](https://schema.org/Text) | Type of fare medium (e.g. CONTACTLESS_CARD, MOBILE_APP, PAPER_TICKET, QR_CODE) |
| [mediumId](https://schema.beckn.io/mobility/mediumId) | [schema:Text](https://schema.org/Text) | Unique identifier or number of the physical or digital medium |
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
