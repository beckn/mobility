# Frequency

A schema.beckn.io Type

A headway-based service specification indicating how often a vehicle runs on a route within a given time window.

**Canonical IRI :** `mobility:Frequency`

**Canonical URL:** https://schema.beckn.io/mobility/Frequency

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Constraint](https://github.com/beckn/core_schema/tree/draft/schema/Constraint) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Frequency](https://schema.beckn.io/mobility/Frequency)** | | |
| [headwaySecs](https://schema.beckn.io/mobility/headwaySecs) | [schema:Number](https://schema.org/Number) | Time in seconds between consecutive vehicle departures |
| [exactTimes](https://schema.beckn.io/mobility/exactTimes) | [schema:Boolean](https://schema.org/Boolean) | Whether departures are at exact scheduled times (true) or headway-based (false) |
| [startTime](https://schema.beckn.io/mobility/startTime) | [schema:Text](https://schema.org/Text) | Time at which this frequency period begins (HH:MM:SS) |
| [endTime](https://schema.beckn.io/mobility/endTime) | [schema:Text](https://schema.org/Text) | Time at which this frequency period ends (HH:MM:SS) |
| **[Properties from Constraint](https://github.com/beckn/core_schema/tree/draft/schema/Constraint)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the constraint |
| [constraintType](https://schema.beckn.io/core/constraintType) | [schema:Text](https://schema.org/Text) | Type of constraint (extensible term) |
| [operator](https://schema.beckn.io/core/operator) | [schema:Text](https://schema.org/Text) | Comparator operator (e.g. <=, >=, =) |
| [value](https://schema.beckn.io/core/value) | [schema:Number](https://schema.org/Number) | Numeric value of the constraint |
| [unitCode](https://schema.beckn.io/core/unitCode) | [schema:Text](https://schema.org/Text) | Unit of measure code (UN/ECE Rec 20) |
| [validity](https://schema.beckn.io/core/validity) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Validity window for this constraint |

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
