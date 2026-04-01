# Telemetry

A schema.beckn.io Type

Time-series data streams reporting the real-time location, speed, and operational state of a mobility vehicle or asset.

**Canonical IRI :** `mobility:Telemetry`

**Canonical URL:** https://schema.beckn.io/mobility/Telemetry

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking) | rdfs:subClassOf | Subclass |
| [schema:Vehicle](https://schema.org/Vehicle) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Telemetry](https://schema.beckn.io/mobility/Telemetry)** | | |
| [vehicleId](https://schema.beckn.io/mobility/vehicleId) | [schema:Text](https://schema.org/Text) | Identifier of the vehicle transmitting telemetry |
| [timestamp](https://schema.beckn.io/mobility/timestamp) | [schema:DateTime](https://schema.org/DateTime) | Timestamp of the telemetry reading |
| [latitude](https://schema.beckn.io/mobility/latitude) | [schema:Number](https://schema.org/Number) | Latitude in WGS-84 decimal degrees |
| [longitude](https://schema.beckn.io/mobility/longitude) | [schema:Number](https://schema.org/Number) | Longitude in WGS-84 decimal degrees |
| [speed](https://schema.beckn.io/mobility/speed) | [schema:Number](https://schema.org/Number) | Current speed in kilometres per hour |
| [bearing](https://schema.beckn.io/mobility/bearing) | [schema:Number](https://schema.org/Number) | Direction of travel in degrees (0=north, 90=east) |
| [batteryLevel](https://schema.beckn.io/mobility/batteryLevel) | [schema:Number](https://schema.org/Number) | Battery charge percentage (for electric vehicles) |
| [odometer](https://schema.beckn.io/mobility/odometer) | [schema:Number](https://schema.org/Number) | Odometer reading in metres since vehicle start |
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
