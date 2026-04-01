# PlaceRequest

A schema.beckn.io Type

A request for a specific accommodation or seat assignment within a transport service during the booking process.

**Canonical IRI :** `mobility:PlaceRequest`

**Canonical URL:** https://schema.beckn.io/mobility/PlaceRequest

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:ContractItem](https://github.com/beckn/core_schema/tree/draft/schema/ContractItem) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from PlaceRequest](https://schema.beckn.io/mobility/PlaceRequest)** | | |
| [accommodationType](https://schema.beckn.io/mobility/accommodationType) | [schema:Text](https://schema.org/Text) | Type of accommodation requested (e.g. SEAT, BERTH, COMPARTMENT) |
| [preferences](https://schema.beckn.io/mobility/preferences) | [schema:Text](https://schema.org/Text) | Passenger preferences (e.g. window, aisle, quiet zone) |
| [seatRef](https://schema.beckn.io/mobility/seatRef) | [Seat](https://schema.beckn.io/mobility/Seat) | Specific seat requested, if applicable |
| **[Properties from ContractItem](https://github.com/beckn/core_schema/tree/draft/schema/ContractItem)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the contract item |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the item |
| [price](https://schema.beckn.io/core/price) | [PriceSpecification](https://github.com/beckn/core_schema/tree/draft/schema/PriceSpecification) | Price for this contract item |
| [quantity](https://schema.beckn.io/core/quantity) | [Quantity](https://github.com/beckn/core_schema/tree/draft/schema/Quantity) | Quantity of this contract item |

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
