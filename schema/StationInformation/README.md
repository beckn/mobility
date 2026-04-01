# StationInformation

A schema.beckn.io Type

Static descriptive information about a shared mobility docking station, including its location, capacity, and features.

**Canonical IRI :** `mobility:StationInformation`

**Canonical URL:** https://schema.beckn.io/mobility/StationInformation

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | rdfs:subClassOf | Subclass |
| [schema:CivicStructure](https://schema.org/CivicStructure) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from StationInformation](https://schema.beckn.io/mobility/StationInformation)** | | |
| [stationId](https://schema.beckn.io/mobility/stationId) | [schema:Text](https://schema.org/Text) | Unique identifier for the docking station |
| [shortName](https://schema.beckn.io/mobility/shortName) | [schema:Text](https://schema.org/Text) | Shortened name of the station for display |
| [capacity](https://schema.beckn.io/mobility/capacity) | [schema:Number](https://schema.org/Number) | Total number of docking points at this station |
| [hasKiosk](https://schema.beckn.io/mobility/hasKiosk) | [schema:Boolean](https://schema.org/Boolean) | Whether this station has a kiosk for key cards or passes |
| [rentalMethods](https://schema.beckn.io/mobility/rentalMethods) | [schema:Text](https://schema.org/Text) | Methods by which bikes can be rented (e.g. KEY, CREDITCARD, APP) |
| [regionId](https://schema.beckn.io/mobility/regionId) | [schema:Text](https://schema.org/Text) | Identifier of the system region this station belongs to |
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
