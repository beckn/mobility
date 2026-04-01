# PickupDropoffPoint

A schema.beckn.io Type

A designated location used as a pickup or dropoff point for passengers in a ride-hailing or demand-responsive transport service.

**Canonical IRI :** `mobility:PickupDropoffPoint`

**Canonical URL:** https://schema.beckn.io/mobility/PickupDropoffPoint

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:FulfillmentStop](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentStop) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from PickupDropoffPoint](https://schema.beckn.io/mobility/PickupDropoffPoint)** | | |
| [pdpType](https://schema.beckn.io/mobility/pdpType) | [schema:Text](https://schema.org/Text) | Type of point (PICKUP, DROPOFF, BOTH) |
| [landmark](https://schema.beckn.io/mobility/landmark) | [schema:Text](https://schema.org/Text) | Nearby landmark or reference point |
| [accessNotes](https://schema.beckn.io/mobility/accessNotes) | [schema:Text](https://schema.org/Text) | Instructions for accessing this pickup/dropoff point |
| **[Properties from FulfillmentStop](https://schema.beckn.io/core/FulfillmentStop)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the fulfillment stop |
| [location](https://schema.beckn.io/core/location) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Geographic location of the stop |
| [type](https://schema.beckn.io/core/type) | [schema:Text](https://schema.org/Text) | Type of stop (start, end, intermediate) |
| [instructions](https://schema.beckn.io/core/instructions) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Instructions for passengers at this stop |
| [time](https://schema.beckn.io/core/time) | [TimePeriod](https://github.com/beckn/core_schema/tree/draft/schema/TimePeriod) | Expected time window at this stop |

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
