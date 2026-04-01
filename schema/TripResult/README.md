# TripResult

A schema.beckn.io Type

The result of a trip planning request, containing one or more journey options with leg details and timing.

**Canonical IRI :** `mobility:TripResult`

**Canonical URL:** https://schema.beckn.io/mobility/TripResult

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from TripResult](https://schema.beckn.io/mobility/TripResult)** | | |
| [itineraries](https://schema.beckn.io/mobility/itineraries) | [Itinerary](https://schema.beckn.io/mobility/Itinerary) | List of itinerary options in the result |
| [requestRef](https://schema.beckn.io/mobility/requestRef) | [TripRequest](https://schema.beckn.io/mobility/TripRequest) | Reference to the originating trip request |
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
