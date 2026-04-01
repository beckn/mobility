# Receipt

A schema.beckn.io Type

A payment receipt issued to a passenger upon completion and settlement of a transport service trip.

**Canonical IRI :** `mobility:Receipt`

**Canonical URL:** https://schema.beckn.io/mobility/Receipt

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Invoice](https://github.com/beckn/core_schema/tree/draft/schema/Invoice) | owl:equivalentClass | Exact |
| [schema:Invoice](https://schema.org/Invoice) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Receipt](https://schema.beckn.io/mobility/Receipt)** | | |
| [receiptId](https://schema.beckn.io/mobility/receiptId) | [schema:Text](https://schema.org/Text) | Unique identifier for the receipt |
| [issuedAt](https://schema.beckn.io/mobility/issuedAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when the receipt was issued |
| [paymentMethod](https://schema.beckn.io/mobility/paymentMethod) | [schema:Text](https://schema.org/Text) | Method of payment used (e.g. CARD, UPI, CASH, WALLET) |
| [tripRef](https://schema.beckn.io/mobility/tripRef) | [Trip](https://schema.beckn.io/mobility/Trip) | Reference to the trip for which this receipt is issued |
| **[Properties from Invoice](https://github.com/beckn/core_schema/tree/draft/schema/Invoice)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the invoice |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the invoice |
| [price](https://schema.beckn.io/core/price) | [PriceSpecification](https://github.com/beckn/core_schema/tree/draft/schema/PriceSpecification) | Total price for the invoice |
| [breakup](https://schema.beckn.io/core/breakup) | [PriceSpecification](https://github.com/beckn/core_schema/tree/draft/schema/PriceSpecification) | Itemised price breakup |
| [validity](https://schema.beckn.io/core/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Validity period of the invoice |

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
