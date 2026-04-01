# AffectedLine

A schema.beckn.io Type

A reference to a transport line that is affected by a service disruption or alert.

**Canonical IRI :** `mobility:AffectedLine`

**Canonical URL:** https://schema.beckn.io/mobility/AffectedLine

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Alert](https://github.com/beckn/core_schema/tree/draft/schema/Alert) | rdfs:subClassOf | Subclass |
| [mobility:Line](https://schema.beckn.io/mobility/Line) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from AffectedLine](https://schema.beckn.io/mobility/AffectedLine)** | | |
| [lineId](https://schema.beckn.io/mobility/lineId) | [schema:Text](https://schema.org/Text) | Identifier of the affected transport line |
| [lineRef](https://schema.beckn.io/mobility/lineRef) | [Line](https://schema.beckn.io/mobility/Line) | Reference to the affected Line entity |
| [affectedStops](https://schema.beckn.io/mobility/affectedStops) | [Stop](https://schema.beckn.io/mobility/Stop) | Stops on this line affected by the disruption |
| [cause](https://schema.beckn.io/mobility/cause) | [schema:Text](https://schema.org/Text) | Cause of the disruption affecting this line |
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
