# EmergencyEvent

A schema.beckn.io Type

A critical safety or operational event requiring immediate response, such as an accident, vehicle breakdown, or passenger emergency.

**Canonical IRI :** `mobility:EmergencyEvent`

**Canonical URL:** https://schema.beckn.io/mobility/EmergencyEvent

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Alert](https://github.com/beckn/core_schema/tree/draft/schema/Alert) | rdfs:subClassOf | Subclass |
| [schema:Event](https://schema.org/Event) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from EmergencyEvent](https://schema.beckn.io/mobility/EmergencyEvent)** | | |
| [emergencyType](https://schema.beckn.io/mobility/emergencyType) | [schema:Text](https://schema.org/Text) | Type of emergency (e.g. ACCIDENT, BREAKDOWN, MEDICAL) |
| [severity](https://schema.beckn.io/mobility/severity) | [schema:Text](https://schema.org/Text) | Severity level of the emergency (LOW, MEDIUM, HIGH, CRITICAL) |
| [reportedAt](https://schema.beckn.io/mobility/reportedAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when the emergency was reported |
| [location](https://schema.beckn.io/mobility/location) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Geographic location of the emergency |
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
