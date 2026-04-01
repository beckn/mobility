# BaggageAllowance

A schema.beckn.io Type

The quantity and weight of baggage a passenger is permitted to carry or check in without incurring additional charges.

**Canonical IRI :** `mobility:BaggageAllowance`

**Canonical URL:** https://schema.beckn.io/mobility/BaggageAllowance

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Constraint](https://github.com/beckn/core_schema/tree/draft/schema/Constraint) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from BaggageAllowance](https://schema.beckn.io/mobility/BaggageAllowance)** | | |
| [cabinBaggageCount](https://schema.beckn.io/mobility/cabinBaggageCount) | [schema:Number](https://schema.org/Number) | Maximum number of cabin (carry-on) bags allowed |
| [cabinBaggageWeight](https://schema.beckn.io/mobility/cabinBaggageWeight) | [schema:Number](https://schema.org/Number) | Maximum weight in kilograms for cabin baggage |
| [checkedBaggageCount](https://schema.beckn.io/mobility/checkedBaggageCount) | [schema:Number](https://schema.org/Number) | Maximum number of checked bags allowed |
| [checkedBaggageWeight](https://schema.beckn.io/mobility/checkedBaggageWeight) | [schema:Number](https://schema.org/Number) | Maximum weight in kilograms per checked bag |
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
