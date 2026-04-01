# Segment

A schema.beckn.io Type

A portion of a rail journey operated continuously by a single carrier between two consecutive stops or stations.

**Canonical IRI :** `mobility:Segment`

**Canonical URL:** https://schema.beckn.io/mobility/Segment

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Fulfillment](https://github.com/beckn/core_schema/tree/draft/schema/Fulfillment) | rdfs:subClassOf | Subclass |
| [mobility:Leg](https://schema.beckn.io/mobility/Leg) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Segment](https://schema.beckn.io/mobility/Segment)** | | |
| [carrierCode](https://schema.beckn.io/mobility/carrierCode) | [schema:Text](https://schema.org/Text) | Code of the carrier operating this segment |
| [segmentNumber](https://schema.beckn.io/mobility/segmentNumber) | [schema:Number](https://schema.org/Number) | Sequence number of this segment within the journey |
| [trainNumber](https://schema.beckn.io/mobility/trainNumber) | [schema:Text](https://schema.org/Text) | Train or service number for this segment |
| [coachNumber](https://schema.beckn.io/mobility/coachNumber) | [schema:Text](https://schema.org/Text) | Coach or carriage number |
| **[Properties from Leg](https://schema.beckn.io/mobility/Leg)** | | |
| [mode](https://schema.beckn.io/core/mode) | [schema:Text](https://schema.org/Text) | Transport mode for this leg (e.g. BUS, RAIL, WALK, BICYCLE) |
| [origin](https://schema.beckn.io/core/origin) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Start location of the leg |
| [destination](https://schema.beckn.io/core/destination) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | End location of the leg |
| [startTime](https://schema.beckn.io/core/startTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled or actual start time of the leg |
| [endTime](https://schema.beckn.io/core/endTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled or actual end time of the leg |
| [distance](https://schema.beckn.io/core/distance) | [schema:Number](https://schema.org/Number) | Distance of this leg in metres |
| [headsign](https://schema.beckn.io/core/headsign) | [schema:Text](https://schema.org/Text) | Destination sign text displayed on the vehicle |
| [routeRef](https://schema.beckn.io/core/routeRef) | [Route](https://schema.beckn.io/mobility/Route) | Reference to the route served on this leg |

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
