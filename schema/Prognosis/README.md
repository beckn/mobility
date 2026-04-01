# Prognosis

A schema.beckn.io Type

A real-time prediction of a vehicle's arrival or departure time at a stop, including an indication of prediction confidence.

**Canonical IRI :** `mobility:Prognosis`

**Canonical URL:** https://schema.beckn.io/mobility/Prognosis

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking) | rdfs:subClassOf | Subclass |
| [mobility:StopTime](https://schema.beckn.io/mobility/StopTime) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Prognosis](https://schema.beckn.io/mobility/Prognosis)** | | |
| [scheduledTime](https://schema.beckn.io/mobility/scheduledTime) | [schema:DateTime](https://schema.org/DateTime) | Timetabled scheduled time |
| [estimatedTime](https://schema.beckn.io/mobility/estimatedTime) | [schema:DateTime](https://schema.org/DateTime) | Predicted actual time |
| [certainty](https://schema.beckn.io/mobility/certainty) | [schema:Text](https://schema.org/Text) | Confidence of the prognosis (e.g. real, prognosis, calculated, unknown) |
| [delaySeconds](https://schema.beckn.io/mobility/delaySeconds) | [schema:Number](https://schema.org/Number) | Delay in seconds relative to the scheduled time |
| **[Properties from Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the tracking record |
| [url](https://schema.beckn.io/core/url) | [schema:URL](https://schema.org/URL) | URL endpoint for real-time tracking information |
| [status](https://schema.beckn.io/core/status) | [State](https://github.com/beckn/core_schema/tree/draft/schema/State) | Current tracking status |
| [validity](https://schema.beckn.io/core/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Validity period for this tracking record |

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
