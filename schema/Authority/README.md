# Authority

A schema.beckn.io Type

A governmental or administrative body responsible for planning, regulating, and overseeing transport services within a jurisdiction.

**Canonical IRI :** `mobility:Authority`

**Canonical URL:** https://schema.beckn.io/mobility/Authority

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Provider](https://github.com/beckn/core_schema/tree/draft/schema/Provider) | rdfs:subClassOf | Subclass |
| [schema:GovernmentOrganization](https://schema.org/GovernmentOrganization) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Authority](https://schema.beckn.io/mobility/Authority)** | | |
| [authorityId](https://schema.beckn.io/mobility/authorityId) | [schema:Text](https://schema.org/Text) | Unique identifier for the authority |
| [jurisdiction](https://schema.beckn.io/mobility/jurisdiction) | [schema:Text](https://schema.org/Text) | Geographic or administrative jurisdiction of this authority |
| [regulatoryScope](https://schema.beckn.io/mobility/regulatoryScope) | [schema:Text](https://schema.org/Text) | Scope of regulatory powers (e.g. national, regional, local) |
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
