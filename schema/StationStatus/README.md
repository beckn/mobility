# StationStatus

A schema.beckn.io Type

The real-time operational state of a shared mobility station, including the number of available docks and vehicles.

**Canonical IRI :** `mobility:StationStatus`

**Canonical URL:** https://schema.beckn.io/mobility/StationStatus

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:State](https://github.com/beckn/core_schema/tree/draft/schema/State) | rdfs:subClassOf | Subclass |
| [schema:ItemAvailability](https://schema.org/ItemAvailability) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from StationStatus](https://schema.beckn.io/mobility/StationStatus)** | | |
| [stationId](https://schema.beckn.io/mobility/stationId) | [schema:Text](https://schema.org/Text) | Unique identifier of the station being reported |
| [numBikesAvailable](https://schema.beckn.io/mobility/numBikesAvailable) | [schema:Number](https://schema.org/Number) | Number of bikes currently available for rental |
| [numDocksAvailable](https://schema.beckn.io/mobility/numDocksAvailable) | [schema:Number](https://schema.org/Number) | Number of empty docking points currently available |
| [isInstalled](https://schema.beckn.io/mobility/isInstalled) | [schema:Boolean](https://schema.org/Boolean) | Whether the station is physically installed and operational |
| [isRenting](https://schema.beckn.io/mobility/isRenting) | [schema:Boolean](https://schema.org/Boolean) | Whether the station is currently renting bikes |
| [isReturning](https://schema.beckn.io/mobility/isReturning) | [schema:Boolean](https://schema.org/Boolean) | Whether the station is currently accepting bike returns |
| [lastReported](https://schema.beckn.io/mobility/lastReported) | [schema:DateTime](https://schema.org/DateTime) | Timestamp of the last status update for this station |
| **[Properties from State](https://github.com/beckn/core_schema/tree/draft/schema/State)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the state |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the state |
| [updatedAt](https://schema.beckn.io/core/updatedAt) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when the state was last updated |

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
