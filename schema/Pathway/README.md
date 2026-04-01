# Pathway

A schema.beckn.io Type

A connection between two points within a transit station (e.g., stairway, elevator, walkway) used for indoor navigation and accessibility routing.

**Canonical IRI :** `mobility:Pathway`

**Canonical URL:** https://schema.beckn.io/mobility/Pathway

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | rdfs:subClassOf | Subclass |
| [geo:Feature](http://www.opengis.net/ont/geosparql#Feature) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Pathway](https://schema.beckn.io/mobility/Pathway)** | | |
| [pathwayId](https://schema.beckn.io/mobility/pathwayId) | [schema:Text](https://schema.org/Text) | Unique identifier for the pathway |
| [fromStopId](https://schema.beckn.io/mobility/fromStopId) | [Stop](https://schema.beckn.io/mobility/Stop) | Stop at the start of the pathway |
| [toStopId](https://schema.beckn.io/mobility/toStopId) | [Stop](https://schema.beckn.io/mobility/Stop) | Stop at the end of the pathway |
| [pathwayMode](https://schema.beckn.io/mobility/pathwayMode) | [schema:Text](https://schema.org/Text) | Type of pathway (1=walkway, 2=stairs, 3=moving_sidewalk, 4=escalator, 5=elevator, 6=fare_gate, 7=exit_gate) |
| [isBidirectional](https://schema.beckn.io/mobility/isBidirectional) | [schema:Boolean](https://schema.org/Boolean) | Whether the pathway can be traversed in both directions |
| [length](https://schema.beckn.io/mobility/length) | [schema:Number](https://schema.org/Number) | Length of the pathway in metres |
| [traversalTime](https://schema.beckn.io/mobility/traversalTime) | [schema:Number](https://schema.org/Number) | Time in seconds to traverse the pathway |
| **[Properties from Location](https://github.com/beckn/core_schema/tree/draft/schema/Location)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the location |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the location |
| [gps](https://schema.beckn.io/core/gps) | [schema:Text](https://schema.org/Text) | GPS coordinates as a latitude,longitude string |
| [address](https://schema.beckn.io/core/address) | [Address](https://github.com/beckn/core_schema/tree/draft/schema/Address) | Physical address of the location |
| [city](https://schema.beckn.io/core/city) | [schema:Text](https://schema.org/Text) | City name |
| [country](https://schema.beckn.io/core/country) | [schema:Text](https://schema.org/Text) | ISO 3166-1 alpha-2 country code |
| [geojson](https://schema.beckn.io/core/geojson) | [GeoJSONGeometry](https://github.com/beckn/core_schema/tree/draft/schema/GeoJSONGeometry) | GeoJSON geometry object representing this location |

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
