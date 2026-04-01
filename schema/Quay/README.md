# Quay

A schema.beckn.io Type

A specific platform, bay, or boarding area within a Stop Place at which passengers board or alight from a vehicle.

**Canonical IRI :** `mobility:Quay`

**Canonical URL:** https://schema.beckn.io/mobility/Quay

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
| **[Properties from Quay](https://schema.beckn.io/mobility/Quay)** | | |
| [quayId](https://schema.beckn.io/mobility/quayId) | [schema:Text](https://schema.org/Text) | Unique identifier for the quay |
| [publicCode](https://schema.beckn.io/mobility/publicCode) | [schema:Text](https://schema.org/Text) | Publicly displayed platform or bay code |
| [quayType](https://schema.beckn.io/mobility/quayType) | [schema:Text](https://schema.org/Text) | Type of quay (e.g. RAIL_PLATFORM, BUS_BAY, FERRY_BERTH) |
| [stopPlaceRef](https://schema.beckn.io/mobility/stopPlaceRef) | [StopPlace](https://schema.beckn.io/mobility/StopPlace) | Reference to the parent Stop Place |
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
