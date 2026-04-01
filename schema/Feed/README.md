# Feed

A schema.beckn.io Type

A data publication providing transit or mobility information in a standardised format for consumption by applications or planners.

**Canonical IRI :** `mobility:Feed`

**Canonical URL:** https://schema.beckn.io/mobility/Feed

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog) | rdfs:subClassOf | Subclass |
| [schema:DataFeed](https://schema.org/DataFeed) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Feed](https://schema.beckn.io/mobility/Feed)** | | |
| [feedType](https://schema.beckn.io/mobility/feedType) | [schema:Text](https://schema.org/Text) | Format of the feed (e.g. GTFS, GTFS_RT, GBFS, NeTEx) |
| [feedId](https://schema.beckn.io/mobility/feedId) | [schema:Text](https://schema.org/Text) | Unique identifier for the feed |
| [feedPublisher](https://schema.beckn.io/mobility/feedPublisher) | [schema:Text](https://schema.org/Text) | Name of the organisation publishing this feed |
| [feedLanguage](https://schema.beckn.io/mobility/feedLanguage) | [schema:Text](https://schema.org/Text) | BCP-47 language code for the feed content |
| [feedStartDate](https://schema.beckn.io/mobility/feedStartDate) | [schema:DateTime](https://schema.org/DateTime) | Date from which the feed data is valid |
| [feedEndDate](https://schema.beckn.io/mobility/feedEndDate) | [schema:DateTime](https://schema.org/DateTime) | Date until which the feed data is valid |
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
