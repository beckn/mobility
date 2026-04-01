# Ticket

A schema.beckn.io Type

A document or digital record granting the holder the right to travel on a specific transport service or within a defined validity scope.

**Canonical IRI :** `mobility:Ticket`

**Canonical URL:** https://schema.beckn.io/mobility/Ticket

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Entitlement](https://github.com/beckn/core_schema/tree/draft/schema/Entitlement) | rdfs:subClassOf | Subclass |
| [schema:Ticket](https://schema.org/Ticket) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Ticket](https://schema.beckn.io/mobility/Ticket)** | | |
| [ticketId](https://schema.beckn.io/mobility/ticketId) | [schema:Text](https://schema.org/Text) | Unique identifier or serial number of the ticket |
| [ticketType](https://schema.beckn.io/mobility/ticketType) | [schema:Text](https://schema.org/Text) | Type of ticket (e.g. SINGLE, RETURN, SEASON, FLEXI) |
| [validFrom](https://schema.beckn.io/mobility/validFrom) | [schema:DateTime](https://schema.org/DateTime) | Date and time from which the ticket is valid |
| [validUntil](https://schema.beckn.io/mobility/validUntil) | [schema:DateTime](https://schema.org/DateTime) | Date and time until which the ticket is valid |
| [fareProductRef](https://schema.beckn.io/mobility/fareProductRef) | [FareProduct](https://schema.beckn.io/mobility/FareProduct) | Reference to the fare product this ticket is issued under |
| [passengerRef](https://schema.beckn.io/mobility/passengerRef) | [Passenger](https://schema.beckn.io/mobility/Passenger) | Reference to the passenger this ticket is issued to |
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
