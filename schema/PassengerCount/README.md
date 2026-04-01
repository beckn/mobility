# PassengerCount

A schema.beckn.io Type

The measured number of passengers currently aboard a vehicle, used for real-time capacity and load management.

**Canonical IRI :** `mobility:PassengerCount`

**Canonical URL:** https://schema.beckn.io/mobility/PassengerCount

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Quantity](https://github.com/beckn/core_schema/tree/draft/schema/Quantity) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from PassengerCount](https://schema.beckn.io/mobility/PassengerCount)** | | |
| [boardingCount](https://schema.beckn.io/mobility/boardingCount) | [schema:Number](https://schema.org/Number) | Number of passengers who boarded at the last stop |
| [alightingCount](https://schema.beckn.io/mobility/alightingCount) | [schema:Number](https://schema.org/Number) | Number of passengers who alighted at the last stop |
| [currentOccupancy](https://schema.beckn.io/mobility/currentOccupancy) | [schema:Number](https://schema.org/Number) | Total number of passengers currently on board |
| **[Properties from Quantity](https://github.com/beckn/core_schema/tree/draft/schema/Quantity)** | | |
| [unitCode](https://schema.beckn.io/core/unitCode) | [schema:Text](https://schema.org/Text) | Unit of measure code (UN/ECE Rec 20) |
| [value](https://schema.beckn.io/core/value) | [schema:Number](https://schema.org/Number) | Numeric quantity value |
| [maximum](https://schema.beckn.io/core/maximum) | [schema:Number](https://schema.org/Number) | Maximum allowed quantity |
| [minimum](https://schema.beckn.io/core/minimum) | [schema:Number](https://schema.org/Number) | Minimum required quantity |

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
