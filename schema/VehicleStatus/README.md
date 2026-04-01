# VehicleStatus

A schema.beckn.io Type

The real-time operational state of a vehicle or mobility asset, such as available, in use, reserved, or disabled.

**Canonical IRI :** `mobility:VehicleStatus`

**Canonical URL:** https://schema.beckn.io/mobility/VehicleStatus

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:State](https://github.com/beckn/core_schema/tree/draft/schema/State) | rdfs:subClassOf | Subclass |
| [schema:ItemAvailability](https://schema.org/ItemAvailability) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from VehicleStatus](https://schema.beckn.io/mobility/VehicleStatus)** | | |
| [statusCode](https://schema.beckn.io/mobility/statusCode) | [schema:Text](https://schema.org/Text) | Operational status code (e.g. AVAILABLE, IN_USE, RESERVED, DISABLED, CHARGING) |
| [batteryLevel](https://schema.beckn.io/mobility/batteryLevel) | [schema:Number](https://schema.org/Number) | Current battery charge percentage |
| [rangeMeters](https://schema.beckn.io/mobility/rangeMeters) | [schema:Number](https://schema.org/Number) | Estimated remaining range in metres |
| [lastReportedAt](https://schema.beckn.io/mobility/lastReportedAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp of the last status update |
| **[Properties from State](https://github.com/beckn/core_schema/tree/draft/schema/State)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the state |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the state |
| [updatedAt](https://schema.beckn.io/core/updatedAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when the state was last updated |

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
