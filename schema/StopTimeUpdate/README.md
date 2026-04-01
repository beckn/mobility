# StopTimeUpdate

A schema.beckn.io Type

A real-time update to the predicted arrival or departure time of a vehicle at a specific stop within a journey.

**Canonical IRI :** `mobility:StopTimeUpdate`

**Canonical URL:** https://schema.beckn.io/mobility/StopTimeUpdate

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
| **[Properties from StopTimeUpdate](https://schema.beckn.io/mobility/StopTimeUpdate)** | | |
| [stopId](https://schema.beckn.io/mobility/stopId) | [Stop](https://schema.beckn.io/mobility/Stop) | Reference to the stop being updated |
| [stopSequence](https://schema.beckn.io/mobility/stopSequence) | [schema:Number](https://schema.org/Number) | Sequence of this stop in the trip |
| [arrivalDelay](https://schema.beckn.io/mobility/arrivalDelay) | [schema:Number](https://schema.org/Number) | Arrival delay in seconds (negative = early) |
| [departureDelay](https://schema.beckn.io/mobility/departureDelay) | [schema:Number](https://schema.org/Number) | Departure delay in seconds (negative = early) |
| [scheduleRelationship](https://schema.beckn.io/mobility/scheduleRelationship) | [schema:Text](https://schema.org/Text) | Relationship to schedule (SCHEDULED, SKIPPED, NO_DATA) |
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
