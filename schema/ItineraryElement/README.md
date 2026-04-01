# ItineraryElement

A schema.beckn.io Type

A component of an aviation itinerary such as a flight segment, ground transport leg, or ancillary service.

**Canonical IRI :** `mobility:ItineraryElement`

**Canonical URL:** https://schema.beckn.io/mobility/ItineraryElement

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:ContractItem](https://github.com/beckn/core_schema/tree/draft/schema/ContractItem) | rdfs:subClassOf | Subclass |
| [mobility:Itinerary](https://schema.beckn.io/mobility/Itinerary) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from ItineraryElement](https://schema.beckn.io/mobility/ItineraryElement)** | | |
| [elementType](https://schema.beckn.io/mobility/elementType) | [schema:Text](https://schema.org/Text) | Type of itinerary element (FLIGHT, GROUND_TRANSPORT, ANCILLARY) |
| [segmentRef](https://schema.beckn.io/mobility/segmentRef) | [FlightSegment](https://schema.beckn.io/mobility/FlightSegment) | Reference to a flight segment if this is a flight element |
| [legRef](https://schema.beckn.io/mobility/legRef) | [Leg](https://schema.beckn.io/mobility/Leg) | Reference to a transport leg if this is a surface element |
| [sequence](https://schema.beckn.io/mobility/sequence) | [schema:Number](https://schema.org/Number) | Sequential order of this element within the itinerary |
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
