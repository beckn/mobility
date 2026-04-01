# Geofence

A schema.beckn.io Type

A virtual geographic boundary used to define service areas, restricted zones, or operational boundaries for mobility assets.

**Canonical IRI :** `mobility:Geofence`

**Canonical URL:** https://schema.beckn.io/mobility/Geofence

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
| **[Properties from Geofence](https://schema.beckn.io/mobility/Geofence)** | | |
| [geofenceType](https://schema.beckn.io/mobility/geofenceType) | [schema:Text](https://schema.org/Text) | Type of geofence (e.g. SERVICE_AREA, RESTRICTED, SPEED_LIMIT) |
| [geometry](https://schema.beckn.io/mobility/geometry) | [GeoJSONGeometry](https://github.com/beckn/core_schema/tree/draft/schema/GeoJSONGeometry) | GeoJSON geometry defining the geofence boundary |
| [rules](https://schema.beckn.io/mobility/rules) | [schema:Text](https://schema.org/Text) | Operational rules applied within this geofence |
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
