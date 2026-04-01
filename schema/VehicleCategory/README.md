# VehicleCategory

A schema.beckn.io Type

A broad classification of vehicles by their physical type, such as two-wheeler, three-wheeler, four-wheeler, or bus.

**Canonical IRI :** `mobility:VehicleCategory`

**Canonical URL:** https://schema.beckn.io/mobility/VehicleCategory

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:CategoryCode](https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from VehicleCategory](https://schema.beckn.io/mobility/VehicleCategory)** | | |
| [vehicleCategoryCode](https://schema.beckn.io/mobility/vehicleCategoryCode) | [schema:Text](https://schema.org/Text) | Code for the vehicle category (e.g. TWO_WHEELER, THREE_WHEELER, FOUR_WHEELER, BUS) |
| [maxPassengers](https://schema.beckn.io/mobility/maxPassengers) | [schema:Number](https://schema.org/Number) | Maximum number of passengers for vehicles in this category |
| **[Properties from CategoryCode](https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the category code |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable label for the category |
| [parentCategoryId](https://schema.beckn.io/core/parentCategoryId) | [schema:Text](https://schema.org/Text) | Identifier of the parent category if hierarchical |

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
