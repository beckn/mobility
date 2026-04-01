# Direction

A schema.beckn.io Type

The direction of travel of a transport service along a route, typically expressed as inbound or outbound.

**Canonical IRI :** `mobility:Direction`

**Canonical URL:** https://schema.beckn.io/mobility/Direction

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | rdfs:subClassOf | Subclass |
| [schema:Direction](https://schema.org/Direction) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Direction](https://schema.beckn.io/mobility/Direction)** | | |
| [directionId](https://schema.beckn.io/mobility/directionId) | [schema:Text](https://schema.org/Text) | Binary direction identifier (0 for one direction, 1 for the other) |
| [directionCode](https://schema.beckn.io/mobility/directionCode) | [schema:Text](https://schema.org/Text) | Named direction code (e.g. INBOUND, OUTBOUND, CLOCKWISE) |
| **[Properties from Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor)** | | |
| [name](https://schema.beckn.io/core/name) | [schema:Text](https://schema.org/Text) | Short display name of the entity |
| [short_desc](https://schema.beckn.io/core/short_desc) | [schema:Text](https://schema.org/Text) | Brief textual description |
| [long_desc](https://schema.beckn.io/core/long_desc) | [schema:Text](https://schema.org/Text) | Detailed or long-form description |
| [media](https://schema.beckn.io/core/media) | [schema:URL](https://schema.org/URL) | Media resource URLs (images, audio, video) |
| [images](https://schema.beckn.io/core/images) | [schema:URL](https://schema.org/URL) | Image URLs for visual display |

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
