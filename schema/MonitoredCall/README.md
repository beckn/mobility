# MonitoredCall

A schema.beckn.io Type

A real-time arrival or departure prediction for a specific vehicle at a specific stop within a monitored journey.

**Canonical IRI :** `mobility:MonitoredCall`

**Canonical URL:** https://schema.beckn.io/mobility/MonitoredCall

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking) | rdfs:subClassOf | Subclass |
| [mobility:StopTime](https://schema.beckn.io/mobility/StopTime) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from MonitoredCall](https://schema.beckn.io/mobility/MonitoredCall)** | | |
| [stopPointRef](https://schema.beckn.io/mobility/stopPointRef) | [StopPoint](https://schema.beckn.io/mobility/StopPoint) | Reference to the stop point for this call |
| [visitNumber](https://schema.beckn.io/mobility/visitNumber) | [schema:Number](https://schema.org/Number) | Visit sequence number for loop services |
| [vehicleAtStop](https://schema.beckn.io/mobility/vehicleAtStop) | [schema:Boolean](https://schema.org/Boolean) | Whether the vehicle is currently at the stop |
| [expectedArrivalTime](https://schema.beckn.io/mobility/expectedArrivalTime) | [schema:DateTime](https://schema.org/DateTime) | Predicted arrival time at this stop |
| [expectedDepartureTime](https://schema.beckn.io/mobility/expectedDepartureTime) | [schema:DateTime](https://schema.org/DateTime) | Predicted departure time from this stop |
| [aimedArrivalTime](https://schema.beckn.io/mobility/aimedArrivalTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled arrival time from the timetable |
| [aimedDepartureTime](https://schema.beckn.io/mobility/aimedDepartureTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled departure time from the timetable |
| [arrivalStatus](https://schema.beckn.io/mobility/arrivalStatus) | [schema:Text](https://schema.org/Text) | Arrival status (e.g. onTime, delayed, early) |
| [departureStatus](https://schema.beckn.io/mobility/departureStatus) | [schema:Text](https://schema.org/Text) | Departure status (e.g. onTime, delayed, early) |
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
