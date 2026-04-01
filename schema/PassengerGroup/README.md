# PassengerGroup

A schema.beckn.io Type

A collection of passengers traveling together as a group, with a group size and a designated lead passenger.

**Canonical IRI :** `mobility:PassengerGroup`

**Canonical URL:** https://schema.beckn.io/mobility/PassengerGroup

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Quantity](https://github.com/beckn/core_schema/tree/draft/schema/Quantity) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from PassengerGroup](https://schema.beckn.io/mobility/PassengerGroup)** | | |
| [groupId](https://schema.beckn.io/mobility/groupId) | [schema:Text](https://schema.org/Text) | Unique identifier for this passenger group |
| [groupSize](https://schema.beckn.io/mobility/groupSize) | [schema:Number](https://schema.org/Number) | Total number of passengers in the group |
| [leadPassenger](https://schema.beckn.io/mobility/leadPassenger) | [Passenger](https://schema.beckn.io/mobility/Passenger) | The lead or primary passenger for the group |
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
