# SupportCase

A schema.beckn.io Type

A formal customer service inquiry, complaint, or request raised by a passenger or provider through the mobility platform's support system.

**Canonical IRI :** `mobility:SupportCase`

**Canonical URL:** https://schema.beckn.io/mobility/SupportCase

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:SupportRequest](https://github.com/beckn/core_schema/tree/draft/schema/SupportRequest) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from SupportCase](https://schema.beckn.io/mobility/SupportCase)** | | |
| [caseType](https://schema.beckn.io/mobility/caseType) | [schema:Text](https://schema.org/Text) | Type of support case (e.g. COMPLAINT, INQUIRY, TECHNICAL) |
| [priority](https://schema.beckn.io/mobility/priority) | [schema:Text](https://schema.org/Text) | Priority level of the case (LOW, MEDIUM, HIGH, URGENT) |
| [reportedAt](https://schema.beckn.io/mobility/reportedAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when the case was reported |
| [resolvedAt](https://schema.beckn.io/mobility/resolvedAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when the case was resolved |
| **[Properties from SupportRequest](https://github.com/beckn/core_schema/tree/draft/schema/SupportRequest)** | | |
| [orderId](https://schema.beckn.io/core/orderId) | [schema:Text](https://schema.org/Text) | Identifier of the contract/order against which support is required |
| [ticketIds](https://schema.beckn.io/core/ticketIds) | [SupportTicket](https://github.com/beckn/core_schema/tree/draft/schema/SupportTicket) | Identifiers of any open support tickets |
| [callbackPhone](https://schema.beckn.io/core/callbackPhone) | [schema:Text](https://schema.org/Text) | Telephone number for callback support |

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
