# StopTime

A schema.beckn.io Type

The scheduled arrival and departure times for a vehicle at a specific stop within a vehicle journey.

**Canonical IRI :** `mobility:StopTime`

**Canonical URL:** https://schema.beckn.io/mobility/StopTime

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | rdfs:subClassOf | Subclass |
| [transmodel:PassingTime](https://w3id.org/transmodel/ontology#PassingTime) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from StopTime](https://schema.beckn.io/mobility/StopTime)** | | |
| [arrivalTime](https://schema.beckn.io/mobility/arrivalTime) | [schema:Text](https://schema.org/Text) | Scheduled arrival time in HH:MM:SS format |
| [departureTime](https://schema.beckn.io/mobility/departureTime) | [schema:Text](https://schema.org/Text) | Scheduled departure time in HH:MM:SS format |
| [stopSequence](https://schema.beckn.io/mobility/stopSequence) | [schema:Number](https://schema.org/Number) | Order of this stop within the vehicle journey |
| [stopRef](https://schema.beckn.io/mobility/stopRef) | [Stop](https://schema.beckn.io/mobility/Stop) | Reference to the stop for this stop time |
| [pickupType](https://schema.beckn.io/mobility/pickupType) | [schema:Text](https://schema.org/Text) | How passengers board at this stop (0=regular, 1=no_pickup, 2=phone_agency, 3=coordinate_with_driver) |
| [dropOffType](https://schema.beckn.io/mobility/dropOffType) | [schema:Text](https://schema.org/Text) | How passengers alight at this stop (0=regular, 1=no_drop_off, 2=phone_agency, 3=coordinate_with_driver) |
| [distanceTraveled](https://schema.beckn.io/mobility/distanceTraveled) | [schema:Number](https://schema.org/Number) | Distance from the route origin to this stop in metres |
| **[Properties from TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod)** | | |
| [startDate](https://schema.beckn.io/core/startDate) | [schema:DateTime](https://schema.org/DateTime) | Start date and time of the period |
| [endDate](https://schema.beckn.io/core/endDate) | [schema:DateTime](https://schema.org/DateTime) | End date and time of the period |
| [startTime](https://schema.beckn.io/core/startTime) | [schema:Text](https://schema.org/Text) | Start time of day in HH:MM:SS format |
| [endTime](https://schema.beckn.io/core/endTime) | [schema:Text](https://schema.org/Text) | End time of day in HH:MM:SS format |

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
