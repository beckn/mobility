# GeneralMessageDelivery

A schema.beckn.io Type

A real-time delivery of textual messages or alerts related to service disruptions or passenger information.

**Canonical IRI :** `mobility:GeneralMessageDelivery`

**Canonical URL:** https://schema.beckn.io/mobility/GeneralMessageDelivery

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
| **[Properties from GeneralMessageDelivery](https://schema.beckn.io/mobility/GeneralMessageDelivery)** | | |
| [responseTimestamp](https://schema.beckn.io/mobility/responseTimestamp) | [schema:DateTime](https://schema.org/DateTime) | Timestamp of this general message delivery |
| [infoMessages](https://schema.beckn.io/mobility/infoMessages) | [Alert](https://schema.beckn.io/mobility/Alert) | List of informational messages in this delivery |
| [channel](https://schema.beckn.io/mobility/channel) | [schema:Text](https://schema.org/Text) | Distribution channel for this message (e.g. WEB, SMS, APP) |
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
