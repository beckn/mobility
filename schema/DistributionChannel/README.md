# DistributionChannel

A schema.beckn.io Type

A channel or platform through which fare products or tickets are sold or distributed to end customers.

**Canonical IRI :** `mobility:DistributionChannel`

**Canonical URL:** https://schema.beckn.io/mobility/DistributionChannel

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog) | skos:closeMatch | Close Match |
| [schema:ItemList](https://schema.org/ItemList) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from DistributionChannel](https://schema.beckn.io/mobility/DistributionChannel)** | | |
| [channelType](https://schema.beckn.io/mobility/channelType) | [schema:Text](https://schema.org/Text) | Type of distribution channel (e.g. ONLINE, TICKET_OFFICE, MOBILE_APP) |
| [channelName](https://schema.beckn.io/mobility/channelName) | [schema:Text](https://schema.org/Text) | Human-readable name of this distribution channel |
| [url](https://schema.beckn.io/mobility/url) | [schema:URL](https://schema.org/URL) | URL to access this distribution channel |
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
