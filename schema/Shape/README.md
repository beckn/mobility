# Shape

A schema.beckn.io Type

The geographic path traced by a vehicle along a route, represented as an ordered sequence of geographic coordinates.

**Canonical IRI :** `mobility:Shape`

**Canonical URL:** https://schema.beckn.io/mobility/Shape

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:GeoJSONGeometry](https://github.com/beckn/core_schema/tree/draft/schema/GeoJSONGeometry) | rdfs:subClassOf | Subclass |
| [geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Shape](https://schema.beckn.io/mobility/Shape)** | | |
| [shapeId](https://schema.beckn.io/mobility/shapeId) | [schema:Text](https://schema.org/Text) | Unique identifier for the shape |
| [distanceTraveled](https://schema.beckn.io/mobility/distanceTraveled) | [schema:Number](https://schema.org/Number) | Distance along the shape in metres up to this point |
| **[Properties from GeoJSONGeometry](https://github.com/beckn/core_schema/tree/draft/schema/GeoJSONGeometry)** | | |
| [type](https://schema.beckn.io/core/type) | [schema:Text](https://schema.org/Text) | GeoJSON geometry type (Point, Polygon, LineString, etc.) |
| [coordinates](https://schema.beckn.io/core/coordinates) | [schema:ItemList](https://schema.org/ItemList) | Coordinate array per RFC 7946 |

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
