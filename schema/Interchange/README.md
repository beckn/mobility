# Interchange

A schema.beckn.io Type

A planned transfer connection point where passengers switch between two or more transport services, with defined timing constraints.

**Canonical IRI :** `mobility:Interchange`

**Canonical URL:** https://schema.beckn.io/mobility/Interchange

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:FulfillmentStop](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentStop) | rdfs:subClassOf | Subclass |
| [mobility:Stop](https://schema.beckn.io/mobility/Stop) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Interchange](https://schema.beckn.io/mobility/Interchange)** | | |
| [minTransferTime](https://schema.beckn.io/mobility/minTransferTime) | [schema:Number](https://schema.org/Number) | Minimum required transfer time in seconds |
| [transferType](https://schema.beckn.io/mobility/transferType) | [schema:Text](https://schema.org/Text) | Type of interchange (e.g. TIMED, GUARANTEED, IN_SEAT) |
| [fromStopId](https://schema.beckn.io/mobility/fromStopId) | [Stop](https://schema.beckn.io/mobility/Stop) | The stop passengers transfer from |
| [toStopId](https://schema.beckn.io/mobility/toStopId) | [Stop](https://schema.beckn.io/mobility/Stop) | The stop passengers transfer to |
| [fromTripId](https://schema.beckn.io/mobility/fromTripId) | [VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney) | The vehicle journey passengers transfer from |
| [toTripId](https://schema.beckn.io/mobility/toTripId) | [VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney) | The vehicle journey passengers transfer to |
| **[Properties from Stop](https://schema.beckn.io/mobility/Stop)** | | |
| [stopId](https://schema.beckn.io/core/stopId) | [schema:Text](https://schema.org/Text) | Unique identifier for the stop |
| [stopCode](https://schema.beckn.io/core/stopCode) | [schema:Text](https://schema.org/Text) | Short public-facing code for the stop |
| [stopName](https://schema.beckn.io/core/stopName) | [schema:Text](https://schema.org/Text) | Human-readable name of the stop |
| [locationType](https://schema.beckn.io/core/locationType) | [schema:Text](https://schema.org/Text) | Classification of location (0=stop, 1=station, 2=entrance, 3=generic_node, 4=boarding_area) |
| [parentStation](https://schema.beckn.io/core/parentStation) | [Station](https://schema.beckn.io/mobility/Station) | Reference to the parent station if this is a platform |
| [wheelchairBoarding](https://schema.beckn.io/core/wheelchairBoarding) | [schema:Text](https://schema.org/Text) | Wheelchair accessibility (0=no info, 1=accessible, 2=not accessible) |

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
