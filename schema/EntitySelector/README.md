# EntitySelector

A schema.beckn.io Type

A selector that identifies which transport entities (routes, trips, stops, or agencies) are affected by a given alert.

**Canonical IRI :** `mobility:EntitySelector`

**Canonical URL:** https://schema.beckn.io/mobility/EntitySelector

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Alert](https://github.com/beckn/core_schema/tree/draft/schema/Alert) | rdfs:subClassOf | Subclass |
| [mobility:Alert](https://schema.beckn.io/mobility/Alert) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from EntitySelector](https://schema.beckn.io/mobility/EntitySelector)** | | |
| [agencyId](https://schema.beckn.io/mobility/agencyId) | [schema:Text](https://schema.org/Text) | Identifier of the affected agency |
| [routeId](https://schema.beckn.io/mobility/routeId) | [schema:Text](https://schema.org/Text) | Identifier of the affected route |
| [routeType](https://schema.beckn.io/mobility/routeType) | [schema:Text](https://schema.org/Text) | Type of the affected route (e.g. BUS, RAIL) |
| [tripDescriptor](https://schema.beckn.io/mobility/tripDescriptor) | [TripDescriptor](https://schema.beckn.io/mobility/TripDescriptor) | Descriptor identifying the affected trip |
| [stopId](https://schema.beckn.io/mobility/stopId) | [schema:Text](https://schema.org/Text) | Identifier of the affected stop |
| **[Properties from Alert](https://github.com/beckn/core_schema/tree/draft/schema/Alert)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the alert |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the alert |
| [validity](https://schema.beckn.io/core/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Time period during which the alert is active |
| [status](https://schema.beckn.io/core/status) | [State](https://github.com/beckn/core_schema/tree/draft/schema/State) | Current status of the alert |

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
