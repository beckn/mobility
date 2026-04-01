# DepartureMessage

A schema.beckn.io Type

A real-time message containing predicted departure times for vehicles at a stop, as used in VDV real-time standards.

**Canonical IRI :** `mobility:DepartureMessage`

**Canonical URL:** https://schema.beckn.io/mobility/DepartureMessage

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Alert](https://github.com/beckn/core_schema/tree/draft/schema/Alert) | rdfs:subClassOf | Subclass |
| [mobility:StopTime](https://schema.beckn.io/mobility/StopTime) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from DepartureMessage](https://schema.beckn.io/mobility/DepartureMessage)** | | |
| [stopRef](https://schema.beckn.io/mobility/stopRef) | [Stop](https://schema.beckn.io/mobility/Stop) | Reference to the stop for which departures are reported |
| [lineRef](https://schema.beckn.io/mobility/lineRef) | [Line](https://schema.beckn.io/mobility/Line) | Reference to the line departing from this stop |
| [vehicleRef](https://schema.beckn.io/mobility/vehicleRef) | [VehicleDescriptor](https://schema.beckn.io/mobility/VehicleDescriptor) | Reference to the departing vehicle |
| [expectedDeparture](https://schema.beckn.io/mobility/expectedDeparture) | [schema:DateTime](https://schema.org/DateTime) | Predicted departure time |
| [delaySeconds](https://schema.beckn.io/mobility/delaySeconds) | [schema:Number](https://schema.org/Number) | Delay in seconds relative to scheduled departure |
| **[Properties from Alert](https://github.com/beckn/core_schema/tree/draft/schema/Alert)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the alert |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the alert |
| [validity](https://schema.beckn.io/core/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Time period during which the alert is active |
| [status](https://schema.beckn.io/core/status) | [State](https://github.com/beckn/core_schema/tree/draft/schema/State) | Current status of the alert |

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
