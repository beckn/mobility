# Station

A schema.beckn.io Type

A major transit facility serving as a hub for one or more transport modes, typically offering waiting areas, ticketing, and interchange facilities.

**Canonical IRI :** `mobility:Station`

**Canonical URL:** https://schema.beckn.io/mobility/Station

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | rdfs:subClassOf | Subclass |
| [schema:CivicStructure](https://schema.org/CivicStructure) | rdfs:subClassOf | Subclass |
| [schema:TrainStation](https://schema.org/TrainStation) | rdfs:seeAlso | Related |
| [schema:BusStation](https://schema.org/BusStation) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Station](https://schema.beckn.io/mobility/Station)** | | |
| [stationId](https://schema.beckn.io/mobility/stationId) | [schema:Text](https://schema.org/Text) | Unique identifier for the station |
| [stationName](https://schema.beckn.io/mobility/stationName) | [schema:Text](https://schema.org/Text) | Human-readable name of the station |
| [stationType](https://schema.beckn.io/mobility/stationType) | [schema:Text](https://schema.org/Text) | Primary transport mode served (e.g. RAIL, BUS, METRO, FERRY) |
| [platforms](https://schema.beckn.io/mobility/platforms) | [Quay](https://schema.beckn.io/mobility/Quay) | Platforms or quays within this station |
| [levels](https://schema.beckn.io/mobility/levels) | [Level](https://schema.beckn.io/mobility/Level) | Levels or floors within the station |
| [pathways](https://schema.beckn.io/mobility/pathways) | [Pathway](https://schema.beckn.io/mobility/Pathway) | Internal navigation pathways within the station |
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
