# Plan

A schema.beckn.io Type

A journey planning response containing one or more itinerary options for a given trip request.

**Canonical IRI :** `mobility:Plan`

**Canonical URL:** https://schema.beckn.io/mobility/Plan

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Plan](https://schema.beckn.io/mobility/Plan)** | | |
| [requestedTime](https://schema.beckn.io/mobility/requestedTime) | [schema:DateTime](https://schema.org/DateTime) | The departure or arrival time that was requested |
| [itineraries](https://schema.beckn.io/mobility/itineraries) | [Itinerary](https://schema.beckn.io/mobility/Itinerary) | List of itinerary options returned in the plan |
| [from](https://schema.beckn.io/mobility/from) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Origin location for this plan |
| [to](https://schema.beckn.io/mobility/to) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Destination location for this plan |
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
