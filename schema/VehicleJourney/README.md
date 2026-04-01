# VehicleJourney

A schema.beckn.io Type

A specific operational instance of a vehicle traveling a defined route at a scheduled time on a given service day.

**Canonical IRI :** `mobility:VehicleJourney`

**Canonical URL:** https://schema.beckn.io/mobility/VehicleJourney

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Fulfillment](https://github.com/beckn/core_schema/tree/draft/schema/Fulfillment) | owl:equivalentClass | Exact |
| [transmodel:VehicleJourney](https://w3id.org/transmodel/ontology#VehicleJourney) | owl:equivalentClass | Exact |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney)** | | |
| [vehicleJourneyCode](https://schema.beckn.io/mobility/vehicleJourneyCode) | [schema:Text](https://schema.org/Text) | Unique code for this vehicle journey |
| [routeRef](https://schema.beckn.io/mobility/routeRef) | [Route](https://schema.beckn.io/mobility/Route) | Reference to the route being served |
| [serviceCalendarRef](https://schema.beckn.io/mobility/serviceCalendarRef) | [ServiceCalendar](https://schema.beckn.io/mobility/ServiceCalendar) | Calendar defining when this journey operates |
| [vehicleRef](https://schema.beckn.io/mobility/vehicleRef) | [Vehicle](https://schema.beckn.io/mobility/Vehicle) | Vehicle assigned to this journey |
| [patternRef](https://schema.beckn.io/mobility/patternRef) | [Pattern](https://schema.beckn.io/mobility/Pattern) | Journey pattern being followed |
| [stopTimes](https://schema.beckn.io/mobility/stopTimes) | [StopTime](https://schema.beckn.io/mobility/StopTime) | Scheduled stop times for each stop on this journey |
| **[Properties from Fulfillment](https://github.com/beckn/core_schema/tree/draft/schema/Fulfillment)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the fulfillment |
| [type](https://schema.beckn.io/core/type) | [schema:Text](https://schema.org/Text) | Type of fulfillment (extensible term) |
| [agent](https://schema.beckn.io/core/agent) | [FulfillmentAgent](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentAgent) | The entity responsible for performing the fulfillment |
| [mode](https://schema.beckn.io/core/mode) | [FulfillmentMode](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentMode) | Mode of fulfillment |
| [state](https://schema.beckn.io/core/state) | [State](https://github.com/beckn/core_schema/tree/draft/schema/State) | Current state of the fulfillment |
| [participants](https://schema.beckn.io/core/participants) | [Participant](https://github.com/beckn/core_schema/tree/draft/schema/Participant) | Participants entitled to receive this fulfillment |
| [stages](https://schema.beckn.io/core/stages) | [FulfillmentStage](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentStage) | Stages in the fulfillment lifecycle |
| [instructions](https://schema.beckn.io/core/instructions) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Instructions for fulfillment |

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
