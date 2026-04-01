# Provider

A schema.beckn.io Type

A mobility service provider registered on a MaaS platform, offering transport options to end users.

**Canonical IRI :** `mobility:Provider`

**Canonical URL:** https://schema.beckn.io/mobility/Provider

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Provider](https://github.com/beckn/core_schema/tree/draft/schema/Provider) | owl:equivalentClass | Exact |
| [schema:Organization](https://schema.org/Organization) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Provider](https://schema.beckn.io/mobility/Provider)** | | |
| [providerId](https://schema.beckn.io/mobility/providerId) | [schema:Text](https://schema.org/Text) | Unique identifier for the mobility provider |
| [providerName](https://schema.beckn.io/mobility/providerName) | [schema:Text](https://schema.org/Text) | Human-readable name of the provider |
| [categories](https://schema.beckn.io/mobility/categories) | [schema:Text](https://schema.org/Text) | Categories of mobility services offered (e.g. RIDE_HAILING, BIKE_SHARE) |
| **[Properties from Provider](https://github.com/beckn/core_schema/tree/draft/schema/Provider)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the provider |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the provider |
| [categories](https://schema.beckn.io/core/categories) | [CategoryCode](https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode) | Service categories offered by the provider |
| [locations](https://schema.beckn.io/core/locations) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Locations where the provider offers services |
| [items](https://schema.beckn.io/core/items) | [Item](https://github.com/beckn/core_schema/tree/draft/schema/Item) | Items available for discovery from this provider |
| [fulfillments](https://schema.beckn.io/core/fulfillments) | [Fulfillment](https://github.com/beckn/core_schema/tree/draft/schema/Fulfillment) | Fulfillment options offered by this provider |
| [ratingsTotal](https://schema.beckn.io/core/ratingsTotal) | [schema:Number](https://schema.org/Number) | Total number of ratings received |
| [rating](https://schema.beckn.io/core/rating) | [Rating](https://github.com/beckn/core_schema/tree/draft/schema/Rating) | Aggregate rating of the provider |

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
