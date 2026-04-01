# Stop

A schema.beckn.io Type

A designated location where vehicles stop to allow passengers to board or alight from a transport service.

**Canonical IRI :** `mobility:Stop`

**Canonical URL:** https://schema.beckn.io/mobility/Stop

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:FulfillmentStop](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentStop) | rdfs:subClassOf | Subclass |
| [schema:BusStop](https://schema.org/BusStop) | rdfs:seeAlso | Related |
| [transmodel:ScheduledStopPoint](https://w3id.org/transmodel/ontology#ScheduledStopPoint) | rdfs:seeAlso | Related |
| [geo:Feature](http://www.opengis.net/ont/geosparql#Feature) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Stop](https://schema.beckn.io/mobility/Stop)** | | |
| [stopId](https://schema.beckn.io/mobility/stopId) | [schema:Text](https://schema.org/Text) | Unique identifier for the stop |
| [stopCode](https://schema.beckn.io/mobility/stopCode) | [schema:Text](https://schema.org/Text) | Short public-facing code for the stop |
| [stopName](https://schema.beckn.io/mobility/stopName) | [schema:Text](https://schema.org/Text) | Human-readable name of the stop |
| [locationType](https://schema.beckn.io/mobility/locationType) | [schema:Text](https://schema.org/Text) | Classification of location (0=stop, 1=station, 2=entrance, 3=generic_node, 4=boarding_area) |
| [parentStation](https://schema.beckn.io/mobility/parentStation) | [Station](https://schema.beckn.io/mobility/Station) | Reference to the parent station if this is a platform |
| [wheelchairBoarding](https://schema.beckn.io/mobility/wheelchairBoarding) | [schema:Text](https://schema.org/Text) | Wheelchair accessibility (0=no info, 1=accessible, 2=not accessible) |
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
