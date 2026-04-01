# TravelDocument

A schema.beckn.io Type

A document (physical or digital) issued to a passenger proving entitlement to travel, used for validation or inspection.

**Canonical IRI :** `mobility:TravelDocument`

**Canonical URL:** https://schema.beckn.io/mobility/TravelDocument

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Entitlement](https://github.com/beckn/core_schema/tree/draft/schema/Entitlement) | rdfs:subClassOf | Subclass |
| [schema:CreativeWork](https://schema.org/CreativeWork) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from TravelDocument](https://schema.beckn.io/mobility/TravelDocument)** | | |
| [documentType](https://schema.beckn.io/mobility/documentType) | [schema:Text](https://schema.org/Text) | Type of travel document (e.g. E_TICKET, PDF_TICKET, SMARTCARD, BARCODE) |
| [documentNumber](https://schema.beckn.io/mobility/documentNumber) | [schema:Text](https://schema.org/Text) | Unique document number or serial |
| [issuingAuthority](https://schema.beckn.io/mobility/issuingAuthority) | [Operator](https://schema.beckn.io/mobility/Operator) | The operator or authority that issued this document |
| [validFrom](https://schema.beckn.io/mobility/validFrom) | [schema:DateTime](https://schema.org/DateTime) | Start date of the document validity |
| [validUntil](https://schema.beckn.io/mobility/validUntil) | [schema:DateTime](https://schema.org/DateTime) | Expiry date of the document |
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
