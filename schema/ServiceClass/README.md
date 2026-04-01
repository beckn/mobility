# ServiceClass

A schema.beckn.io Type

A classification of the level of service offered by a transport service, such as economy, business, or first class.

**Canonical IRI :** `mobility:ServiceClass`

**Canonical URL:** https://schema.beckn.io/mobility/ServiceClass

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:CategoryCode](https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from ServiceClass](https://schema.beckn.io/mobility/ServiceClass)** | | |
| [serviceClassCode](https://schema.beckn.io/mobility/serviceClassCode) | [schema:Text](https://schema.org/Text) | Code identifying the service class (e.g. ECONOMY, BUSINESS, FIRST) |
| [features](https://schema.beckn.io/mobility/features) | [schema:ItemList](https://schema.org/ItemList) | List of features and amenities included in this service class |
| **[Properties from CategoryCode](https://github.com/beckn/core_schema/tree/draft/schema/CategoryCode)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the category code |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable label for the category |
| [parentCategoryId](https://schema.beckn.io/core/parentCategoryId) | [schema:Text](https://schema.org/Text) | Identifier of the parent category if hierarchical |

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
