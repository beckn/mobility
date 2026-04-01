# Event

A schema.beckn.io Type

A discrete state change in the lifecycle of a vehicle or mobility asset, such as a trip starting, vehicle reserved, or battery low.

**Canonical IRI :** `mobility:Event`

**Canonical URL:** https://schema.beckn.io/mobility/Event

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:State](https://github.com/beckn/core_schema/tree/draft/schema/State) | rdfs:subClassOf | Subclass |
| [schema:Event](https://schema.org/Event) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Event](https://schema.beckn.io/mobility/Event)** | | |
| [eventType](https://schema.beckn.io/mobility/eventType) | [schema:Text](https://schema.org/Text) | Type of lifecycle event (e.g. TRIP_START, VEHICLE_RESERVED, BATTERY_LOW) |
| [entityId](https://schema.beckn.io/mobility/entityId) | [schema:Text](https://schema.org/Text) | Identifier of the entity that generated the event |
| [triggeredAt](https://schema.beckn.io/mobility/triggeredAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when the event was triggered |
| [payload](https://schema.beckn.io/mobility/payload) | [schema:Text](https://schema.org/Text) | Additional event-specific data payload |
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
