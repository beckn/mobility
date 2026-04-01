# FulfillmentStop

A schema.beckn.io Type

A specific location associated with a fulfillment (trip or journey) at which passengers board, alight, or transfer between services.

**Canonical IRI :** `mobility:FulfillmentStop`

**Canonical URL:** https://schema.beckn.io/mobility/FulfillmentStop

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:FulfillmentStop](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentStop) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from FulfillmentStop](https://schema.beckn.io/mobility/FulfillmentStop)** | | |
| [stopType](https://schema.beckn.io/mobility/stopType) | [schema:Text](https://schema.org/Text) | Role of this stop in the fulfillment (START, END, INTERMEDIATE) |
| [scheduledTime](https://schema.beckn.io/mobility/scheduledTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled arrival or departure time at this stop |
| [actualTime](https://schema.beckn.io/mobility/actualTime) | [schema:DateTime](https://schema.org/DateTime) | Actual arrival or departure time at this stop |
| [stopRef](https://schema.beckn.io/mobility/stopRef) | [Stop](https://schema.beckn.io/mobility/Stop) | Reference to the Stop entity for this fulfillment stop |
| [passengerCount](https://schema.beckn.io/mobility/passengerCount) | [PassengerCount](https://schema.beckn.io/mobility/PassengerCount) | Passenger count at this fulfillment stop |
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
