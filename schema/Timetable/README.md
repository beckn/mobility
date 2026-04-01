# Timetable

A schema.beckn.io Type

A structured schedule listing planned arrival and departure times for vehicles at each stop along a route.

**Canonical IRI :** `mobility:Timetable`

**Canonical URL:** https://schema.beckn.io/mobility/Timetable

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog) | rdfs:subClassOf | Subclass |
| [schema:Schedule](https://schema.org/Schedule) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Timetable](https://schema.beckn.io/mobility/Timetable)** | | |
| [routeRef](https://schema.beckn.io/mobility/routeRef) | [Route](https://schema.beckn.io/mobility/Route) | Reference to the route this timetable covers |
| [trips](https://schema.beckn.io/mobility/trips) | [VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney) | Vehicle journeys (trips) in this timetable |
| [validFrom](https://schema.beckn.io/mobility/validFrom) | [schema:DateTime](https://schema.org/DateTime) | Date from which this timetable is valid |
| [validUntil](https://schema.beckn.io/mobility/validUntil) | [schema:DateTime](https://schema.org/DateTime) | Date until which this timetable is valid |
| **[Properties from Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the catalog |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the catalog |
| [tags](https://schema.beckn.io/core/tags) | [schema:Text](https://schema.org/Text) | Tags associated with the catalog |

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
