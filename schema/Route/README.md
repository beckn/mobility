# Route

A schema.beckn.io Type

The physical or logical path followed by a transport service, defined as an ordered sequence of stops or waypoints.

**Canonical IRI :** `mobility:Route`

**Canonical URL:** https://schema.beckn.io/mobility/Route

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Item](https://github.com/beckn/core_schema/tree/draft/schema/Item) | rdfs:subClassOf | Subclass |
| [transmodel:Route](https://w3id.org/transmodel/ontology#Route) | rdfs:seeAlso | Related |
| [schema:Trip](https://schema.org/Trip) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Route](https://schema.beckn.io/mobility/Route)** | | |
| [routeId](https://schema.beckn.io/mobility/routeId) | [schema:Text](https://schema.org/Text) | Unique identifier for the route |
| [shortName](https://schema.beckn.io/mobility/shortName) | [schema:Text](https://schema.org/Text) | Short public-facing name (e.g. 42A) |
| [longName](https://schema.beckn.io/mobility/longName) | [schema:Text](https://schema.org/Text) | Full descriptive name of the route |
| [routeType](https://schema.beckn.io/mobility/routeType) | [schema:Text](https://schema.org/Text) | Mode of transport (e.g. BUS, RAIL, TRAM, FERRY) |
| [operatorRef](https://schema.beckn.io/mobility/operatorRef) | [Operator](https://schema.beckn.io/mobility/Operator) | Operator providing this route |
| [networkRef](https://schema.beckn.io/mobility/networkRef) | [Network](https://schema.beckn.io/mobility/Network) | Network this route belongs to |
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
