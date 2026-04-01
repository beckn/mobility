# ServiceCalendar

A schema.beckn.io Type

A schedule defining on which dates a transport service operates, including regular service days and exceptional dates.

**Canonical IRI :** `mobility:ServiceCalendar`

**Canonical URL:** https://schema.beckn.io/mobility/ServiceCalendar

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | rdfs:subClassOf | Subclass |
| [schema:Schedule](https://schema.org/Schedule) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from ServiceCalendar](https://schema.beckn.io/mobility/ServiceCalendar)** | | |
| [serviceId](https://schema.beckn.io/mobility/serviceId) | [schema:Text](https://schema.org/Text) | Unique identifier for the service calendar |
| [monday](https://schema.beckn.io/mobility/monday) | [schema:Boolean](https://schema.org/Boolean) | Whether service operates on Mondays |
| [tuesday](https://schema.beckn.io/mobility/tuesday) | [schema:Boolean](https://schema.org/Boolean) | Whether service operates on Tuesdays |
| [wednesday](https://schema.beckn.io/mobility/wednesday) | [schema:Boolean](https://schema.org/Boolean) | Whether service operates on Wednesdays |
| [thursday](https://schema.beckn.io/mobility/thursday) | [schema:Boolean](https://schema.org/Boolean) | Whether service operates on Thursdays |
| [friday](https://schema.beckn.io/mobility/friday) | [schema:Boolean](https://schema.org/Boolean) | Whether service operates on Fridays |
| [saturday](https://schema.beckn.io/mobility/saturday) | [schema:Boolean](https://schema.org/Boolean) | Whether service operates on Saturdays |
| [sunday](https://schema.beckn.io/mobility/sunday) | [schema:Boolean](https://schema.org/Boolean) | Whether service operates on Sundays |
| [exceptionDates](https://schema.beckn.io/mobility/exceptionDates) | [schema:DateTime](https://schema.org/DateTime) | Dates on which service is added or removed from the regular schedule |
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
