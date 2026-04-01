# Incident

A schema.beckn.io Type

A reported event on the transport network that affects normal service operations, such as a disruption, roadblock, or infrastructure failure.

**Canonical IRI :** `mobility:Incident`

**Canonical URL:** https://schema.beckn.io/mobility/Incident

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Alert](https://github.com/beckn/core_schema/tree/draft/schema/Alert) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Incident](https://schema.beckn.io/mobility/Incident)** | | |
| [incidentType](https://schema.beckn.io/mobility/incidentType) | [schema:Text](https://schema.org/Text) | Type of incident (e.g. DISRUPTION, ROADBLOCK, MAINTENANCE) |
| [severity](https://schema.beckn.io/mobility/severity) | [schema:Text](https://schema.org/Text) | Severity level of the incident (LOW, MEDIUM, HIGH) |
| [affectedArea](https://schema.beckn.io/mobility/affectedArea) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Geographic area affected by the incident |
| [startTime](https://schema.beckn.io/mobility/startTime) | [schema:DateTime](https://schema.org/DateTime) | Date and time the incident started |
| [endTime](https://schema.beckn.io/mobility/endTime) | [schema:DateTime](https://schema.org/DateTime) | Expected or actual end date and time of the incident |
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
