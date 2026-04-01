# StopEvent

A schema.beckn.io Type

A departure or arrival event at a stop, used to retrieve the next or previous vehicle movements at a specific location.

**Canonical IRI :** `mobility:StopEvent`

**Canonical URL:** https://schema.beckn.io/mobility/StopEvent

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:FulfillmentStop](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentStop) | rdfs:subClassOf | Subclass |
| [beckn:DiscoveryIntent](https://github.com/beckn/core_schema/tree/draft/schema/DiscoveryIntent) | rdfs:subClassOf | Subclass |
| [mobility:StopTime](https://schema.beckn.io/mobility/StopTime) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from StopEvent](https://schema.beckn.io/mobility/StopEvent)** | | |
| [stopEventType](https://schema.beckn.io/mobility/stopEventType) | [schema:Text](https://schema.org/Text) | Type of event (DEPARTURE, ARRIVAL) |
| [timetabledTime](https://schema.beckn.io/mobility/timetabledTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled time for the event |
| [estimatedTime](https://schema.beckn.io/mobility/estimatedTime) | [schema:DateTime](https://schema.org/DateTime) | Estimated actual time for the event |
| [serviceJourneyRef](https://schema.beckn.io/mobility/serviceJourneyRef) | [VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney) | Reference to the vehicle journey for this event |
| [stopPointRef](https://schema.beckn.io/mobility/stopPointRef) | [StopPoint](https://schema.beckn.io/mobility/StopPoint) | Reference to the stop point where the event occurs |
| **[Properties from FulfillmentStop](https://schema.beckn.io/core/FulfillmentStop)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the fulfillment stop |
| [location](https://schema.beckn.io/core/location) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Geographic location of the stop |
| [type](https://schema.beckn.io/core/type) | [schema:Text](https://schema.org/Text) | Type of stop (start, end, intermediate) |
| [instructions](https://schema.beckn.io/core/instructions) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Instructions for passengers at this stop |
| [time](https://schema.beckn.io/core/time) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Expected time window at this stop |

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
