# DayType

A schema.beckn.io Type

A classification of a day (e.g., weekday, weekend, public holiday) used to define when a service pattern is valid.

**Canonical IRI :** `mobility:DayType`

**Canonical URL:** https://schema.beckn.io/mobility/DayType

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | rdfs:subClassOf | Subclass |
| [schema:DayOfWeek](https://schema.org/DayOfWeek) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from DayType](https://schema.beckn.io/mobility/DayType)** | | |
| [dayTypeCode](https://schema.beckn.io/mobility/dayTypeCode) | [schema:Text](https://schema.org/Text) | Code identifying the day type (e.g. WEEKDAY, WEEKEND, HOLIDAY) |
| [daysOfWeek](https://schema.beckn.io/mobility/daysOfWeek) | [schema:ItemList](https://schema.org/ItemList) | List of days of the week applicable to this day type |
| **[Properties from TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod)** | | |
| [startDate](https://schema.beckn.io/core/startDate) | [schema:DateTime](https://schema.org/DateTime) | Start date and time of the period |
| [endDate](https://schema.beckn.io/core/endDate) | [schema:DateTime](https://schema.org/DateTime) | End date and time of the period |
| [startTime](https://schema.beckn.io/core/startTime) | [schema:Text](https://schema.org/Text) | Start time of day in HH:MM:SS format |
| [endTime](https://schema.beckn.io/core/endTime) | [schema:Text](https://schema.org/Text) | End time of day in HH:MM:SS format |

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
