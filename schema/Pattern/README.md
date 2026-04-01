# Pattern

A schema.beckn.io Type

A unique sequence of stops visited by trips on a route, grouping trips with identical stop sequences and timing structures.

**Canonical IRI :** `mobility:Pattern`

**Canonical URL:** https://schema.beckn.io/mobility/Pattern

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Item](https://github.com/beckn/core_schema/tree/draft/schema/Item) | rdfs:subClassOf | Subclass |
| [transmodel:JourneyPattern](https://w3id.org/transmodel/ontology#JourneyPattern) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Pattern](https://schema.beckn.io/mobility/Pattern)** | | |
| [patternId](https://schema.beckn.io/mobility/patternId) | [schema:Text](https://schema.org/Text) | Unique identifier for the journey pattern |
| [routeRef](https://schema.beckn.io/mobility/routeRef) | [Route](https://schema.beckn.io/mobility/Route) | Reference to the route this pattern belongs to |
| [directionId](https://schema.beckn.io/mobility/directionId) | [schema:Text](https://schema.org/Text) | Direction of travel (0 or 1) |
| [stops](https://schema.beckn.io/mobility/stops) | [Stop](https://schema.beckn.io/mobility/Stop) | Ordered list of stops in this pattern |
| [shapeRef](https://schema.beckn.io/mobility/shapeRef) | [Shape](https://schema.beckn.io/mobility/Shape) | Reference to the geographic shape of this pattern |
| **[Properties from Item](https://github.com/beckn/core_schema/tree/draft/schema/Item)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the item |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the item |
| [categoryId](https://schema.beckn.io/core/categoryId) | [CategoryCode](https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode) | Category code classifying the item |
| [price](https://schema.beckn.io/core/price) | [PriceSpecification](https://github.com/beckn/core_schema/tree/draft/schema/PriceSpecification) | Price specification for this item |
| [quantity](https://schema.beckn.io/core/quantity) | [Quantity](https://github.com/beckn/core_schema/tree/draft/schema/Quantity) | Available quantity of the item |
| [tags](https://schema.beckn.io/core/tags) | [schema:Text](https://schema.org/Text) | Tags associated with the item |

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
