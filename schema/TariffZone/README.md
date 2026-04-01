# TariffZone

A schema.beckn.io Type

A geographic zone used to define and apply fare structures, within which a single fare or set of rules applies.

**Canonical IRI :** `mobility:TariffZone`

**Canonical URL:** https://schema.beckn.io/mobility/TariffZone

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
| **[Properties from TariffZone](https://schema.beckn.io/mobility/TariffZone)** | | |
| [zoneId](https://schema.beckn.io/mobility/zoneId) | [schema:Text](https://schema.org/Text) | Unique identifier for the tariff zone |
| [zoneName](https://schema.beckn.io/mobility/zoneName) | [schema:Text](https://schema.org/Text) | Human-readable name of the tariff zone |
| [geometry](https://schema.beckn.io/mobility/geometry) | [GeoJSONGeometry](https://github.com/beckn/core_schema/tree/draft/schema/GeoJSONGeometry) | GeoJSON geometry defining the zone boundary |
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
