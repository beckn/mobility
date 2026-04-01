# TripRequest

A schema.beckn.io Type

A request submitted to a journey planning system specifying origin, destination, travel time, and preferences.

**Canonical IRI :** `mobility:TripRequest`

**Canonical URL:** https://schema.beckn.io/mobility/TripRequest

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Intent](https://github.com/beckn/core_schema/tree/draft/schema/Intent) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from TripRequest](https://schema.beckn.io/mobility/TripRequest)** | | |
| [origin](https://schema.beckn.io/mobility/origin) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Origin location for the trip |
| [destination](https://schema.beckn.io/mobility/destination) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Destination location for the trip |
| [departureTime](https://schema.beckn.io/mobility/departureTime) | [schema:DateTime](https://schema.org/DateTime) | Requested departure time |
| [arrivalTime](https://schema.beckn.io/mobility/arrivalTime) | [schema:DateTime](https://schema.org/DateTime) | Requested arrival time (alternative to departureTime) |
| [modes](https://schema.beckn.io/mobility/modes) | [schema:Text](https://schema.org/Text) | Permitted transport modes (e.g. BUS, RAIL, WALK) |
| [numItineraries](https://schema.beckn.io/mobility/numItineraries) | [schema:Number](https://schema.org/Number) | Number of itinerary alternatives requested |
| **[Properties from Intent](https://github.com/beckn/core_schema/tree/draft/schema/Intent)** | | |
| [textSearch](https://schema.beckn.io/core/textSearch) | [schema:Text](https://schema.org/Text) | Free-text search query expressing what the traveler is looking for |
| [filters](https://schema.beckn.io/core/filters) | [schema:Text](https://schema.org/Text) | JSONPath filter criteria applied to the search results |
| [spatial](https://schema.beckn.io/core/spatial) | [SpatialConstraint](https://github.com/beckn/core_schema/tree/draft/schema/SpatialConstraint) | Geographic constraints on the search area |
| [provider](https://schema.beckn.io/core/provider) | [schema:Text](https://schema.org/Text) | Identifier of a specific provider to search within |

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
