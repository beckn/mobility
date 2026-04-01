# Asset

A schema.beckn.io Type

A specific mobility resource (vehicle, bike, scooter, or car) managed and made available for use by a mobility provider.

**Canonical IRI :** `mobility:Asset`

**Canonical URL:** https://schema.beckn.io/mobility/Asset

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Item](https://github.com/beckn/core_schema/tree/draft/schema/Item) | rdfs:subClassOf | Subclass |
| [schema:Product](https://schema.org/Product) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Asset](https://schema.beckn.io/mobility/Asset)** | | |
| [assetId](https://schema.beckn.io/mobility/assetId) | [schema:Text](https://schema.org/Text) | Provider-assigned unique identifier for the asset |
| [assetType](https://schema.beckn.io/mobility/assetType) | [VehicleType](https://schema.beckn.io/mobility/VehicleType) | Vehicle type classification of this asset |
| [currentStatus](https://schema.beckn.io/mobility/currentStatus) | [VehicleStatus](https://schema.beckn.io/mobility/VehicleStatus) | Real-time operational status of this asset |
| [currentLocation](https://schema.beckn.io/mobility/currentLocation) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Current geographic location of the asset |
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
