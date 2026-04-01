# TransportObject

A schema.beckn.io Type

A generic transport entity in the OSLO mobility ontology representing any object involved in transport operations.

**Canonical IRI :** `mobility:TransportObject`

**Canonical URL:** https://schema.beckn.io/mobility/TransportObject

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Item](https://github.com/beckn/core_schema/tree/draft/schema/Item) | rdfs:subClassOf | Subclass |
| [oslo:TransportObject](https://data.vlaanderen.be/ns/mobiliteit#TransportObject) | owl:equivalentClass | Exact |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from TransportObject](https://schema.beckn.io/mobility/TransportObject)** | | |
| [objectType](https://schema.beckn.io/mobility/objectType) | [schema:Text](https://schema.org/Text) | Type of transport object (e.g. VEHICLE, INFRASTRUCTURE, ASSET) |
| [attributes](https://schema.beckn.io/mobility/attributes) | [schema:Text](https://schema.org/Text) | Additional extensible attributes for this transport object |
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
