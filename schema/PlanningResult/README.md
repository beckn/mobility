# PlanningResult

A schema.beckn.io Type

The output of a MaaS platform planning request, listing available transport options for a requested trip.

**Canonical IRI :** `mobility:PlanningResult`

**Canonical URL:** https://schema.beckn.io/mobility/PlanningResult

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from PlanningResult](https://schema.beckn.io/mobility/PlanningResult)** | | |
| [origin](https://schema.beckn.io/mobility/origin) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Origin location for the planning query |
| [destination](https://schema.beckn.io/mobility/destination) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Destination location for the planning query |
| [options](https://schema.beckn.io/mobility/options) | [RideOption](https://schema.beckn.io/mobility/RideOption) | Available transport options returned |
| [itineraries](https://schema.beckn.io/mobility/itineraries) | [Itinerary](https://schema.beckn.io/mobility/Itinerary) | Multi-modal itinerary options if applicable |
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
