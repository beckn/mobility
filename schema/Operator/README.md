# Operator

A schema.beckn.io Type

An organization that provides and operates public transport or shared mobility services under a defined service agreement.

**Canonical IRI :** `mobility:Operator`

**Canonical URL:** https://schema.beckn.io/mobility/Operator

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Provider](https://github.com/beckn/core_schema/tree/draft/schema/Provider) | owl:equivalentClass | Exact |
| [transmodel:Operator](https://w3id.org/transmodel/ontology#Operator) | owl:equivalentClass | Exact |
| [schema:Organization](https://schema.org/Organization) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Operator](https://schema.beckn.io/mobility/Operator)** | | |
| [operatorId](https://schema.beckn.io/mobility/operatorId) | [schema:Text](https://schema.org/Text) | Unique identifier for the operator |
| [operatingRegions](https://schema.beckn.io/mobility/operatingRegions) | [schema:Text](https://schema.org/Text) | Geographic regions where the operator provides services |
| [licenseNumber](https://schema.beckn.io/mobility/licenseNumber) | [schema:Text](https://schema.org/Text) | Regulatory license or accreditation number |
| [contactInfo](https://schema.beckn.io/mobility/contactInfo) | [schema:Text](https://schema.org/Text) | Public contact information for the operator |
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
