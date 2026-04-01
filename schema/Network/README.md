# Network

A schema.beckn.io Type

A grouping of routes and lines operated under a common brand or authority, used for fare and operational management.

**Canonical IRI :** `mobility:Network`

**Canonical URL:** https://schema.beckn.io/mobility/Network

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog) | rdfs:subClassOf | Subclass |
| [schema:Organization](https://schema.org/Organization) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Network](https://schema.beckn.io/mobility/Network)** | | |
| [networkId](https://schema.beckn.io/mobility/networkId) | [schema:Text](https://schema.org/Text) | Unique identifier for the network |
| [networkName](https://schema.beckn.io/mobility/networkName) | [schema:Text](https://schema.org/Text) | Human-readable name of the network |
| [operatorRef](https://schema.beckn.io/mobility/operatorRef) | [Operator](https://schema.beckn.io/mobility/Operator) | Operator(s) running services within this network |
| [lines](https://schema.beckn.io/mobility/lines) | [Line](https://schema.beckn.io/mobility/Line) | Lines that belong to this network |
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
