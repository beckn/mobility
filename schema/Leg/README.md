# Leg

A schema.beckn.io Type

A single uninterrupted segment of a journey made using one transport mode or service between two consecutive locations.

**Canonical IRI :** `mobility:Leg`

**Canonical URL:** https://schema.beckn.io/mobility/Leg

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Fulfillment](https://github.com/beckn/core_schema/tree/draft/schema/Fulfillment) | rdfs:subClassOf | Subclass |
| [schema:Trip](https://schema.org/Trip) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Leg](https://schema.beckn.io/mobility/Leg)** | | |
| [mode](https://schema.beckn.io/mobility/mode) | [schema:Text](https://schema.org/Text) | Transport mode for this leg (e.g. BUS, RAIL, WALK, BICYCLE) |
| [origin](https://schema.beckn.io/mobility/origin) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Start location of the leg |
| [destination](https://schema.beckn.io/mobility/destination) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | End location of the leg |
| [startTime](https://schema.beckn.io/mobility/startTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled or actual start time of the leg |
| [endTime](https://schema.beckn.io/mobility/endTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled or actual end time of the leg |
| [distance](https://schema.beckn.io/mobility/distance) | [schema:Number](https://schema.org/Number) | Distance of this leg in metres |
| [headsign](https://schema.beckn.io/mobility/headsign) | [schema:Text](https://schema.org/Text) | Destination sign text displayed on the vehicle |
| [routeRef](https://schema.beckn.io/mobility/routeRef) | [Route](https://schema.beckn.io/mobility/Route) | Reference to the route served on this leg |
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
