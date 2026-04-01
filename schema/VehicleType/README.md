# VehicleType

A schema.beckn.io Type

A class or category of vehicle defined by its mode of transport, capacity, propulsion type, and accessibility features.

**Canonical IRI :** `mobility:VehicleType`

**Canonical URL:** https://schema.beckn.io/mobility/VehicleType

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:CategoryCode](https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode) | rdfs:subClassOf | Subclass |
| [schema:Vehicle](https://schema.org/Vehicle) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from VehicleType](https://schema.beckn.io/mobility/VehicleType)** | | |
| [vehicleTypeCode](https://schema.beckn.io/mobility/vehicleTypeCode) | [schema:Text](https://schema.org/Text) | Code identifying the vehicle type (e.g. BUS, TRAM, METRO, BICYCLE, SCOOTER) |
| [maxCapacity](https://schema.beckn.io/mobility/maxCapacity) | [schema:Number](https://schema.org/Number) | Maximum number of passengers the vehicle type can carry |
| [propulsionType](https://schema.beckn.io/mobility/propulsionType) | [schema:Text](https://schema.org/Text) | Propulsion type (e.g. ELECTRIC, COMBUSTION, HUMAN, HYBRID) |
| [wheelchairAccessible](https://schema.beckn.io/mobility/wheelchairAccessible) | [schema:Boolean](https://schema.org/Boolean) | Whether vehicles of this type are wheelchair accessible |
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
