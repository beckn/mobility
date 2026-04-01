# GeofencingZone

A schema.beckn.io Type

A virtual geographic boundary used to define operational areas, speed limits, parking rules, or restrictions for shared mobility services.

**Canonical IRI :** `mobility:GeofencingZone`

**Canonical URL:** https://schema.beckn.io/mobility/GeofencingZone

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | rdfs:subClassOf | Subclass |
| [geo:Feature](http://www.opengis.net/ont/geosparql#Feature) | rdfs:subClassOf | Subclass |
| [schema:GeoShape](https://schema.org/GeoShape) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from GeofencingZone](https://schema.beckn.io/mobility/GeofencingZone)** | | |
| [featureType](https://schema.beckn.io/mobility/featureType) | [schema:Text](https://schema.org/Text) | Type of geofencing zone feature (e.g. parking, restricted, slow) |
| [geometry](https://schema.beckn.io/mobility/geometry) | [GeoJSONGeometry](https://github.com/beckn/core_schema/tree/draft/schema/GeoJSONGeometry) | GeoJSON geometry defining the zone boundary |
| [rideAllowed](https://schema.beckn.io/mobility/rideAllowed) | [schema:Boolean](https://schema.org/Boolean) | Whether riding is permitted within this zone |
| [rideThroughAllowed](https://schema.beckn.io/mobility/rideThroughAllowed) | [schema:Boolean](https://schema.org/Boolean) | Whether riding through without stopping is permitted |
| [stationParking](https://schema.beckn.io/mobility/stationParking) | [schema:Boolean](https://schema.org/Boolean) | Whether docking at a station is required to end a trip here |
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
