# OccupancyStatus

A schema.beckn.io Type

An indicator of the current passenger load level of a vehicle, such as empty, many seats available, or full.

**Canonical IRI :** `mobility:OccupancyStatus`

**Canonical URL:** https://schema.beckn.io/mobility/OccupancyStatus

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:State](https://github.com/beckn/core_schema/tree/draft/schema/State) | rdfs:subClassOf | Subclass |
| [schema:ItemAvailability](https://schema.org/ItemAvailability) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from OccupancyStatus](https://schema.beckn.io/mobility/OccupancyStatus)** | | |
| [occupancyLevel](https://schema.beckn.io/mobility/occupancyLevel) | [schema:Text](https://schema.org/Text) | Occupancy level (EMPTY, MANY_SEATS_AVAILABLE, FEW_SEATS_AVAILABLE, STANDING_ROOM_ONLY, FULL, NOT_ACCEPTING_PASSENGERS) |
| [availableSeats](https://schema.beckn.io/mobility/availableSeats) | [schema:Number](https://schema.org/Number) | Estimated number of seats currently available |
| [totalSeats](https://schema.beckn.io/mobility/totalSeats) | [schema:Number](https://schema.org/Number) | Total seating capacity of the vehicle |
| **[Properties from State](https://github.com/beckn/core_schema/tree/draft/schema/State)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the state |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the state |
| [updatedAt](https://schema.beckn.io/core/updatedAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when the state was last updated |

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
