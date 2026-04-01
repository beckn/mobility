# StopPoint

A schema.beckn.io Type

An abstract or scheduled point in a public transport network at which passengers can board or alight from a service.

**Canonical IRI :** `mobility:StopPoint`

**Canonical URL:** https://schema.beckn.io/mobility/StopPoint

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:FulfillmentStop](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentStop) | rdfs:subClassOf | Subclass |
| [geo:Feature](http://www.opengis.net/ont/geosparql#Feature) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from StopPoint](https://schema.beckn.io/mobility/StopPoint)** | | |
| [stopPointId](https://schema.beckn.io/mobility/stopPointId) | [schema:Text](https://schema.org/Text) | Unique identifier for the stop point |
| [shortName](https://schema.beckn.io/mobility/shortName) | [schema:Text](https://schema.org/Text) | Short display name or code |
| [publicCode](https://schema.beckn.io/mobility/publicCode) | [schema:Text](https://schema.org/Text) | Publicly visible code displayed at the stop |
| [stopAreaRef](https://schema.beckn.io/mobility/stopAreaRef) | [StopArea](https://schema.beckn.io/mobility/StopArea) | Reference to the stop area this point belongs to |
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
