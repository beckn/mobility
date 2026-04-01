# Seat

A schema.beckn.io Type

A specific seat position reserved or assigned to a passenger on a flight, train, or other transport service.

**Canonical IRI :** `mobility:Seat`

**Canonical URL:** https://schema.beckn.io/mobility/Seat

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Entitlement](https://github.com/beckn/core_schema/tree/draft/schema/Entitlement) | rdfs:subClassOf | Subclass |
| [schema:Seat](https://schema.org/Seat) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Seat](https://schema.beckn.io/mobility/Seat)** | | |
| [seatId](https://schema.beckn.io/mobility/seatId) | [schema:Text](https://schema.org/Text) | Unique identifier or label for the seat |
| [row](https://schema.beckn.io/mobility/row) | [schema:Text](https://schema.org/Text) | Row designation (number or letter) |
| [column](https://schema.beckn.io/mobility/column) | [schema:Text](https://schema.org/Text) | Column or seat letter within the row |
| [seatType](https://schema.beckn.io/mobility/seatType) | [schema:Text](https://schema.org/Text) | Type of seat (e.g. WINDOW, AISLE, MIDDLE, UPPER_BERTH) |
| [seatCharacteristics](https://schema.beckn.io/mobility/seatCharacteristics) | [schema:Text](https://schema.org/Text) | Additional characteristics (e.g. EXTRA_LEGROOM, QUIET_ZONE, ACCESSIBLE) |
| [deckLevel](https://schema.beckn.io/mobility/deckLevel) | [schema:Text](https://schema.org/Text) | Deck or level (UPPER, LOWER, MAIN) |
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
