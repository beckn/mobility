# Line

A schema.beckn.io Type

A named, branded public transport service identified by a number or name, typically operating over one or more routes.

**Canonical IRI :** `mobility:Line`

**Canonical URL:** https://schema.beckn.io/mobility/Line

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Item](https://github.com/beckn/core_schema/tree/draft/schema/Item) | rdfs:subClassOf | Subclass |
| [transmodel:Line](https://w3id.org/transmodel/ontology#Line) | owl:equivalentClass | Exact |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Line](https://schema.beckn.io/mobility/Line)** | | |
| [lineId](https://schema.beckn.io/mobility/lineId) | [schema:Text](https://schema.org/Text) | GTFS or NeTEx identifier for the line |
| [shortName](https://schema.beckn.io/mobility/shortName) | [schema:Text](https://schema.org/Text) | Short public-facing name (e.g. 42, M1, Jubilee) |
| [longName](https://schema.beckn.io/mobility/longName) | [schema:Text](https://schema.org/Text) | Full descriptive name of the line |
| [lineType](https://schema.beckn.io/mobility/lineType) | [schema:Text](https://schema.org/Text) | Mode of transport (e.g. BUS, SUBWAY, RAIL, FERRY) |
| [color](https://schema.beckn.io/mobility/color) | [schema:Text](https://schema.org/Text) | Hex colour code for line display on maps |
| [textColor](https://schema.beckn.io/mobility/textColor) | [schema:Text](https://schema.org/Text) | Hex colour code for text displayed on the line colour |
| [operatorRef](https://schema.beckn.io/mobility/operatorRef) | [Operator](https://schema.beckn.io/mobility/Operator) | Reference to the operator running this line |
| [networkRef](https://schema.beckn.io/mobility/networkRef) | [Network](https://schema.beckn.io/mobility/Network) | Reference to the network this line belongs to |
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
