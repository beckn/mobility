# Level

A schema.beckn.io Type

A floor or vertical level within a multi-level transit station or facility, used to define internal navigation paths.

**Canonical IRI :** `mobility:Level`

**Canonical URL:** https://schema.beckn.io/mobility/Level

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | rdfs:subClassOf | Subclass |
| [schema:Floor](https://schema.org/Floor) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Level](https://schema.beckn.io/mobility/Level)** | | |
| [levelId](https://schema.beckn.io/mobility/levelId) | [schema:Text](https://schema.org/Text) | Unique identifier for this level within the station |
| [levelName](https://schema.beckn.io/mobility/levelName) | [schema:Text](https://schema.org/Text) | Human-readable name of the level (e.g. Ground Floor, Level 1) |
| [elevation](https://schema.beckn.io/mobility/elevation) | [schema:Number](https://schema.org/Number) | Elevation of this level in metres above ground |
| [stationRef](https://schema.beckn.io/mobility/stationRef) | [Station](https://schema.beckn.io/mobility/Station) | Reference to the station this level belongs to |
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
