# MonitoredVehicleJourney

A schema.beckn.io Type

A real-time representation of a vehicle journey being actively tracked, including position and schedule adherence data.

**Canonical IRI :** `mobility:MonitoredVehicleJourney`

**Canonical URL:** https://schema.beckn.io/mobility/MonitoredVehicleJourney

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Tracking](https://github.com/beckn/core_schema/tree/draft/schema/Tracking) | rdfs:subClassOf | Subclass |
| [mobility:VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from MonitoredVehicleJourney](https://schema.beckn.io/mobility/MonitoredVehicleJourney)** | | |
| [lineRef](https://schema.beckn.io/mobility/lineRef) | [Line](https://schema.beckn.io/mobility/Line) | Reference to the line being monitored |
| [directionRef](https://schema.beckn.io/mobility/directionRef) | [Direction](https://schema.beckn.io/mobility/Direction) | Direction of travel being monitored |
| [vehicleRef](https://schema.beckn.io/mobility/vehicleRef) | [VehicleDescriptor](https://schema.beckn.io/mobility/VehicleDescriptor) | Reference to the monitored vehicle |
| [vehicleLocation](https://schema.beckn.io/mobility/vehicleLocation) | [VehiclePosition](https://schema.beckn.io/mobility/VehiclePosition) | Current geographic position of the vehicle |
| [bearing](https://schema.beckn.io/mobility/bearing) | [schema:Number](https://schema.org/Number) | Compass bearing of travel in degrees |
| [delay](https://schema.beckn.io/mobility/delay) | [schema:Number](https://schema.org/Number) | Delay in seconds relative to schedule (negative = early) |
| [occupancy](https://schema.beckn.io/mobility/occupancy) | [OccupancyStatus](https://schema.beckn.io/mobility/OccupancyStatus) | Current passenger occupancy of the vehicle |
| **[Properties from VehicleJourney](https://schema.beckn.io/mobility/VehicleJourney)** | | |
| [vehicleJourneyCode](https://schema.beckn.io/core/vehicleJourneyCode) | [schema:Text](https://schema.org/Text) | Unique code for this vehicle journey |
| [routeRef](https://schema.beckn.io/core/routeRef) | [Route](https://schema.beckn.io/mobility/Route) | Reference to the route being served |
| [serviceCalendarRef](https://schema.beckn.io/core/serviceCalendarRef) | [ServiceCalendar](https://schema.beckn.io/mobility/ServiceCalendar) | Calendar defining when this journey operates |
| [vehicleRef](https://schema.beckn.io/core/vehicleRef) | [Vehicle](https://schema.beckn.io/mobility/Vehicle) | Vehicle assigned to this journey |
| [patternRef](https://schema.beckn.io/core/patternRef) | [Pattern](https://schema.beckn.io/mobility/Pattern) | Journey pattern being followed |
| [stopTimes](https://schema.beckn.io/core/stopTimes) | [StopTime](https://schema.beckn.io/mobility/StopTime) | Scheduled stop times for each stop on this journey |

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
