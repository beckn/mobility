# TripSpecification

A schema.beckn.io Type

A description of the desired journey used as input to search and price transport options.

**Canonical IRI :** `mobility:TripSpecification`

**Canonical URL:** https://schema.beckn.io/mobility/TripSpecification

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Intent](https://github.com/beckn/core_schema/tree/draft/schema/Intent) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from TripSpecification](https://schema.beckn.io/mobility/TripSpecification)** | | |
| [origin](https://schema.beckn.io/mobility/origin) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Desired origin of the trip |
| [destination](https://schema.beckn.io/mobility/destination) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Desired destination of the trip |
| [time](https://schema.beckn.io/mobility/time) | [schema:DateTime](https://schema.org/DateTime) | Desired departure or arrival time |
| [numTravelers](https://schema.beckn.io/mobility/numTravelers) | [schema:Number](https://schema.org/Number) | Number of travelers for whom to price options |
| [modes](https://schema.beckn.io/mobility/modes) | [schema:Text](https://schema.org/Text) | Preferred transport modes for the trip |
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
