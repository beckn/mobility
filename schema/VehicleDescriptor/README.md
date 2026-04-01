# VehicleDescriptor

A schema.beckn.io Type

An identifier that uniquely references a specific vehicle in a real-time transit feed.

**Canonical IRI :** `mobility:VehicleDescriptor`

**Canonical URL:** https://schema.beckn.io/mobility/VehicleDescriptor

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | rdfs:subClassOf | Subclass |
| [mobility:Vehicle](https://schema.beckn.io/mobility/Vehicle) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from VehicleDescriptor](https://schema.beckn.io/mobility/VehicleDescriptor)** | | |
| [vehicleId](https://schema.beckn.io/mobility/vehicleId) | [schema:Text](https://schema.org/Text) | Internal system identifier for the vehicle |
| [label](https://schema.beckn.io/mobility/label) | [schema:Text](https://schema.org/Text) | User-visible label or number for the vehicle |
| [licensePlate](https://schema.beckn.io/mobility/licensePlate) | [schema:Text](https://schema.org/Text) | Vehicle license plate number |
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
