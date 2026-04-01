# SurgeMultiplier

A schema.beckn.io Type

A dynamic pricing factor applied during periods of high demand that increases base fares proportionally to balance supply and demand.

**Canonical IRI :** `mobility:SurgeMultiplier`

**Canonical URL:** https://schema.beckn.io/mobility/SurgeMultiplier

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:PriceComponent](https://github.com/beckn/core_schema/tree/draft/schema/PriceComponent) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from SurgeMultiplier](https://schema.beckn.io/mobility/SurgeMultiplier)** | | |
| [multiplierValue](https://schema.beckn.io/mobility/multiplierValue) | [schema:Number](https://schema.org/Number) | The surge multiplier value (e.g. 1.5 for 1.5x surge) |
| [validUntil](https://schema.beckn.io/mobility/validUntil) | [schema:DateTime](https://schema.org/DateTime) | Timestamp until which the surge multiplier is active |
| [reason](https://schema.beckn.io/mobility/reason) | [schema:Text](https://schema.org/Text) | Reason for the surge (e.g. HIGH_DEMAND, SPECIAL_EVENT) |
| [geofenceRef](https://schema.beckn.io/mobility/geofenceRef) | [Geofence](https://schema.beckn.io/mobility/Geofence) | Geographic area where the surge pricing applies |
| **[Properties from PriceComponent](https://schema.beckn.io/core/PriceComponent)** | | |
| [title](https://schema.beckn.io/core/title) | [schema:Text](https://schema.org/Text) | Title or label of this price component |
| [price](https://schema.beckn.io/core/price) | [PriceSpecification](https://github.com/beckn/core_schema/tree/draft/schema/PriceSpecification) | Monetary value of this component |
| [tags](https://schema.beckn.io/core/tags) | [schema:Text](https://schema.org/Text) | Tags associated with this price component |

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
