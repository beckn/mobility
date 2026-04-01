# LostAndFoundItem

A schema.beckn.io Type

An item that has been reported lost or found in connection with a transport service.

**Canonical IRI :** `mobility:LostAndFoundItem`

**Canonical URL:** https://schema.beckn.io/mobility/LostAndFoundItem

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:SupportRequest](https://github.com/beckn/core_schema/tree/draft/schema/SupportRequest) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from LostAndFoundItem](https://schema.beckn.io/mobility/LostAndFoundItem)** | | |
| [itemType](https://schema.beckn.io/mobility/itemType) | [schema:Text](https://schema.org/Text) | Type of the lost/found item (e.g. BAG, PHONE, WALLET) |
| [itemDescription](https://schema.beckn.io/mobility/itemDescription) | [schema:Text](https://schema.org/Text) | Detailed description of the item |
| [foundAt](https://schema.beckn.io/mobility/foundAt) | [schema:DateTime](https://schema.org/DateTime) | Date and time the item was found |
| [lostAt](https://schema.beckn.io/mobility/lostAt) | [schema:DateTime](https://schema.org/DateTime) | Date and time the item was lost |
| [vehicleRef](https://schema.beckn.io/mobility/vehicleRef) | [Vehicle](https://schema.beckn.io/mobility/Vehicle) | Vehicle on which the item was found or lost |
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
