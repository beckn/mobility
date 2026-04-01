# TripDescriptor

A schema.beckn.io Type

An identifier that uniquely references a specific vehicle journey in a real-time transit feed.

**Canonical IRI :** `mobility:TripDescriptor`

**Canonical URL:** https://schema.beckn.io/mobility/TripDescriptor

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | rdfs:subClassOf | Subclass |
| [mobility:VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from TripDescriptor](https://schema.beckn.io/mobility/TripDescriptor)** | | |
| [tripId](https://schema.beckn.io/mobility/tripId) | [schema:Text](https://schema.org/Text) | GTFS trip_id of the trip being referenced |
| [routeId](https://schema.beckn.io/mobility/routeId) | [schema:Text](https://schema.org/Text) | GTFS route_id associated with the trip |
| [directionId](https://schema.beckn.io/mobility/directionId) | [schema:Text](https://schema.org/Text) | Direction of travel (0 or 1) |
| [startTime](https://schema.beckn.io/mobility/startTime) | [schema:Text](https://schema.org/Text) | Scheduled start time of the trip in HH:MM:SS |
| [startDate](https://schema.beckn.io/mobility/startDate) | [schema:Text](https://schema.org/Text) | Start date of the trip in YYYYMMDD format |
| [scheduleRelationship](https://schema.beckn.io/mobility/scheduleRelationship) | [schema:Text](https://schema.org/Text) | Relationship to the GTFS schedule (SCHEDULED, ADDED, UNSCHEDULED, CANCELED) |
| **[Properties from Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor)** | | |
| [name](https://schema.beckn.io/core/name) | [schema:Text](https://schema.org/Text) | Short display name of the entity |
| [short_desc](https://schema.beckn.io/core/short_desc) | [schema:Text](https://schema.org/Text) | Brief textual description |
| [long_desc](https://schema.beckn.io/core/long_desc) | [schema:Text](https://schema.org/Text) | Detailed or long-form description |
| [media](https://schema.beckn.io/core/media) | [schema:URL](https://schema.org/URL) | Media resource URLs (images, audio, video) |
| [images](https://schema.beckn.io/core/images) | [schema:URL](https://schema.org/URL) | Image URLs for visual display |

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
