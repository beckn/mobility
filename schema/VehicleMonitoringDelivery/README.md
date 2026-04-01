# VehicleMonitoringDelivery

A schema.beckn.io Type

A real-time data delivery providing current positions and operational states of a set of vehicles.

**Canonical IRI :** `mobility:VehicleMonitoringDelivery`

**Canonical URL:** https://schema.beckn.io/mobility/VehicleMonitoringDelivery

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking) | rdfs:subClassOf | Subclass |
| [mobility:VehiclePosition](https://schema.beckn.io/mobility/VehiclePosition) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from VehicleMonitoringDelivery](https://schema.beckn.io/mobility/VehicleMonitoringDelivery)** | | |
| [responseTimestamp](https://schema.beckn.io/mobility/responseTimestamp) | [schema:DateTime](https://schema.org/DateTime) | Timestamp of this monitoring delivery |
| [vehicleActivities](https://schema.beckn.io/mobility/vehicleActivities) | [MonitoredVehicleJourney](https://schema.beckn.io/mobility/MonitoredVehicleJourney) | List of vehicle activity records in this delivery |
| [validUntil](https://schema.beckn.io/mobility/validUntil) | [schema:DateTime](https://schema.org/DateTime) | Time until which this delivery data is valid |
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
