# VehiclePosition

A schema.beckn.io Type

The current real-time geographic position, bearing, and speed of a vehicle operating a transport service.

**Canonical IRI :** `mobility:VehiclePosition`

**Canonical URL:** https://schema.beckn.io/mobility/VehiclePosition

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking) | rdfs:subClassOf | Subclass |
| [schema:Vehicle](https://schema.org/Vehicle) | rdfs:seeAlso | Related |
| [geo:Feature](http://www.opengis.net/ont/geosparql#Feature) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from VehiclePosition](https://schema.beckn.io/mobility/VehiclePosition)** | | |
| [tripDescriptor](https://schema.beckn.io/mobility/tripDescriptor) | [TripDescriptor](https://schema.beckn.io/mobility/TripDescriptor) | Identifies the trip this vehicle is operating |
| [vehicleDescriptor](https://schema.beckn.io/mobility/vehicleDescriptor) | [VehicleDescriptor](https://schema.beckn.io/mobility/VehicleDescriptor) | Identifies the reporting vehicle |
| [latitude](https://schema.beckn.io/mobility/latitude) | [schema:Number](https://schema.org/Number) | Current latitude in WGS-84 decimal degrees |
| [longitude](https://schema.beckn.io/mobility/longitude) | [schema:Number](https://schema.org/Number) | Current longitude in WGS-84 decimal degrees |
| [bearing](https://schema.beckn.io/mobility/bearing) | [schema:Number](https://schema.org/Number) | Current bearing in degrees (0=north, 90=east) |
| [speed](https://schema.beckn.io/mobility/speed) | [schema:Number](https://schema.org/Number) | Current speed in metres per second |
| [currentStopSequence](https://schema.beckn.io/mobility/currentStopSequence) | [schema:Number](https://schema.org/Number) | Stop sequence index of the stop the vehicle is at or approaching |
| [currentStatus](https://schema.beckn.io/mobility/currentStatus) | [schema:Text](https://schema.org/Text) | Vehicle status relative to the stop (INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO) |
| [timestamp](https://schema.beckn.io/mobility/timestamp) | [schema:DateTime](https://schema.org/DateTime) | Timestamp of this position report |
| **[Properties from Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the tracking record |
| [url](https://schema.beckn.io/core/url) | [schema:URL](https://schema.org/URL) | URL endpoint for real-time tracking information |
| [status](https://schema.beckn.io/core/status) | [State](https://github.com/beckn/core_schema/tree/draft/schema/State) | Current tracking status |
| [validity](https://schema.beckn.io/core/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Validity period for this tracking record |

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
