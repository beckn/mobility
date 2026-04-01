# BookingRule

A schema.beckn.io Type

A set of rules governing how and when a demand-responsive transport service must be booked in advance.

**Canonical IRI :** `mobility:BookingRule`

**Canonical URL:** https://schema.beckn.io/mobility/BookingRule

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Policy](https://github.com/beckn/core_schema/tree/draft/schema/Policy) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from BookingRule](https://schema.beckn.io/mobility/BookingRule)** | | |
| [latestBookingTime](https://schema.beckn.io/mobility/latestBookingTime) | [schema:Text](https://schema.org/Text) | Latest time before departure that a booking can be made |
| [earliestBookingTime](https://schema.beckn.io/mobility/earliestBookingTime) | [schema:Text](https://schema.org/Text) | Earliest time before departure that a booking can be made |
| [priorNoticeDurationMin](https://schema.beckn.io/mobility/priorNoticeDurationMin) | [schema:Number](https://schema.org/Number) | Minimum advance notice in minutes required for booking |
| [priorNoticeStartDay](https://schema.beckn.io/mobility/priorNoticeStartDay) | [schema:Number](https://schema.org/Number) | Earliest day before service when booking opens |
| [priorNoticeStartTime](https://schema.beckn.io/mobility/priorNoticeStartTime) | [schema:Text](https://schema.org/Text) | Time of day on the start day when booking opens |
| [message](https://schema.beckn.io/mobility/message) | [schema:Text](https://schema.org/Text) | Customer-facing message about booking requirements |
| [phoneNumber](https://schema.beckn.io/mobility/phoneNumber) | [schema:Text](https://schema.org/Text) | Phone number to call for booking |
| [url](https://schema.beckn.io/mobility/url) | [schema:URL](https://schema.org/URL) | URL to booking interface |
| **[Properties from Policy](https://github.com/beckn/core_schema/tree/draft/schema/Policy)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the policy |
| [policyType](https://schema.beckn.io/core/policyType) | [schema:Text](https://schema.org/Text) | Type of policy (extensible term) |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the policy |
| [validity](https://schema.beckn.io/core/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Validity window for this policy version |
| [policyAttributes](https://schema.beckn.io/core/policyAttributes) | [Attributes](https://github.com/beckn/core_schema/tree/draft/schema/Attributes) | Extensible domain-specific policy attributes |

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
