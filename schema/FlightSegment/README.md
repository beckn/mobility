# FlightSegment

A schema.beckn.io Type

A single non-stop flight operated between two airports, forming a unit of an air travel itinerary.

**Canonical IRI :** `mobility:FlightSegment`

**Canonical URL:** https://schema.beckn.io/mobility/FlightSegment

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Fulfillment](https://github.com/beckn/core_schema/tree/draft/schema/Fulfillment) | rdfs:subClassOf | Subclass |
| [mobility:Leg](https://schema.beckn.io/mobility/Leg) | rdfs:subClassOf | Subclass |
| [schema:Flight](https://schema.org/Flight) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from FlightSegment](https://schema.beckn.io/mobility/FlightSegment)** | | |
| [flightNumber](https://schema.beckn.io/mobility/flightNumber) | [schema:Text](https://schema.org/Text) | IATA/ICAO flight number (e.g. AI101) |
| [departureAirport](https://schema.beckn.io/mobility/departureAirport) | [schema:Text](https://schema.org/Text) | IATA airport code of the departure airport |
| [arrivalAirport](https://schema.beckn.io/mobility/arrivalAirport) | [schema:Text](https://schema.org/Text) | IATA airport code of the arrival airport |
| [departureTime](https://schema.beckn.io/mobility/departureTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled local departure date and time |
| [arrivalTime](https://schema.beckn.io/mobility/arrivalTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled local arrival date and time |
| [airline](https://schema.beckn.io/mobility/airline) | [schema:Text](https://schema.org/Text) | IATA airline code of the operating carrier |
| [aircraftType](https://schema.beckn.io/mobility/aircraftType) | [schema:Text](https://schema.org/Text) | IATA aircraft type code |
| **[Properties from Leg](https://schema.beckn.io/mobility/Leg)** | | |
| [mode](https://schema.beckn.io/core/mode) | [schema:Text](https://schema.org/Text) | Transport mode for this leg (e.g. BUS, RAIL, WALK, BICYCLE) |
| [origin](https://schema.beckn.io/core/origin) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Start location of the leg |
| [destination](https://schema.beckn.io/core/destination) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | End location of the leg |
| [startTime](https://schema.beckn.io/core/startTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled or actual start time of the leg |
| [endTime](https://schema.beckn.io/core/endTime) | [schema:DateTime](https://schema.org/DateTime) | Scheduled or actual end time of the leg |
| [distance](https://schema.beckn.io/core/distance) | [schema:Number](https://schema.org/Number) | Distance of this leg in metres |
| [headsign](https://schema.beckn.io/core/headsign) | [schema:Text](https://schema.org/Text) | Destination sign text displayed on the vehicle |
| [routeRef](https://schema.beckn.io/core/routeRef) | [Route](https://schema.beckn.io/mobility/Route) | Reference to the route served on this leg |

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
