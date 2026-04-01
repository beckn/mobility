# StopMonitoring

A schema.beckn.io Type

A real-time data service providing predicted arrivals and departures of vehicles at a specific stop.

**Canonical IRI :** `mobility:StopMonitoring`

**Canonical URL:** https://schema.beckn.io/mobility/StopMonitoring

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking) | rdfs:subClassOf | Subclass |
| [mobility:Stop](https://schema.beckn.io/mobility/Stop) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from StopMonitoring](https://schema.beckn.io/mobility/StopMonitoring)** | | |
| [stopRef](https://schema.beckn.io/mobility/stopRef) | [Stop](https://schema.beckn.io/mobility/Stop) | Reference to the stop being monitored |
| [monitoredCalls](https://schema.beckn.io/mobility/monitoredCalls) | [MonitoredCall](https://schema.beckn.io/mobility/MonitoredCall) | List of real-time arrival/departure calls at this stop |
| [responseTimestamp](https://schema.beckn.io/mobility/responseTimestamp) | [schema:DateTime](https://schema.org/DateTime) | Timestamp of this stop monitoring response |
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
