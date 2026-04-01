# Alert

A schema.beckn.io Type

A notification of a service disruption, delay, or advisory affecting one or more routes, stops, or vehicle journeys.

**Canonical IRI :** `mobility:Alert`

**Canonical URL:** https://schema.beckn.io/mobility/Alert

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
| **[Properties from Alert](https://schema.beckn.io/mobility/Alert)** | | |
| [cause](https://schema.beckn.io/mobility/cause) | [schema:Text](https://schema.org/Text) | Cause of the alert (e.g. TECHNICAL_PROBLEM, STRIKE, ACCIDENT) |
| [effect](https://schema.beckn.io/mobility/effect) | [schema:Text](https://schema.org/Text) | Effect on service (e.g. DETOUR, REDUCED_SERVICE, NO_SERVICE) |
| [url](https://schema.beckn.io/mobility/url) | [schema:URL](https://schema.org/URL) | URL to a page with more information about the alert |
| [headerText](https://schema.beckn.io/mobility/headerText) | [schema:Text](https://schema.org/Text) | Short header text for the alert |
| [descriptionText](https://schema.beckn.io/mobility/descriptionText) | [schema:Text](https://schema.org/Text) | Detailed description of the alert |
| [activePeriod](https://schema.beckn.io/mobility/activePeriod) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Time period during which the alert is active |
| [informedEntity](https://schema.beckn.io/mobility/informedEntity) | [EntitySelector](https://schema.beckn.io/mobility/EntitySelector) | Transport entities affected by this alert |
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
