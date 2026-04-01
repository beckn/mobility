# Vehicle

A schema.beckn.io Type

A motorized or human-powered mobility asset used to carry passengers or goods between locations.

**Canonical IRI :** `mobility:Vehicle`

**Canonical URL:** https://schema.beckn.io/mobility/Vehicle

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Item](https://github.com/beckn/core_schema/tree/draft/schema/Item) | rdfs:subClassOf | Subclass |
| [schema:Vehicle](https://schema.org/Vehicle) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Vehicle](https://schema.beckn.io/mobility/Vehicle)** | | |
| [vehicleId](https://schema.beckn.io/mobility/vehicleId) | [schema:Text](https://schema.org/Text) | Unique identifier for the vehicle |
| [licensePlate](https://schema.beckn.io/mobility/licensePlate) | [schema:Text](https://schema.org/Text) | Vehicle registration plate number |
| [make](https://schema.beckn.io/mobility/make) | [schema:Text](https://schema.org/Text) | Manufacturer of the vehicle |
| [model](https://schema.beckn.io/mobility/model) | [schema:Text](https://schema.org/Text) | Model name of the vehicle |
| [year](https://schema.beckn.io/mobility/year) | [schema:Number](https://schema.org/Number) | Year of manufacture |
| [color](https://schema.beckn.io/mobility/color) | [schema:Text](https://schema.org/Text) | Colour of the vehicle |
| [vehicleType](https://schema.beckn.io/mobility/vehicleType) | [VehicleType](https://schema.beckn.io/mobility/VehicleType) | Type classification of the vehicle |
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
