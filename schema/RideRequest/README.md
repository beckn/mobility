# RideRequest

A schema.beckn.io Type

A passenger's request for an on-demand transport service between two points, specifying origin, destination, and travel preferences.

**Canonical IRI :** `mobility:RideRequest`

**Canonical URL:** https://schema.beckn.io/mobility/RideRequest

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Intent](https://github.com/beckn/core_schema/tree/draft/schema/Intent) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from RideRequest](https://schema.beckn.io/mobility/RideRequest)** | | |
| [origin](https://schema.beckn.io/mobility/origin) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Pickup location for the ride |
| [destination](https://schema.beckn.io/mobility/destination) | [Location](https://github.com/beckn/core_schema/tree/draft/schema/Location) | Dropoff location for the ride |
| [requestedTime](https://schema.beckn.io/mobility/requestedTime) | [schema:DateTime](https://schema.org/DateTime) | Requested pickup time |
| [passengerCount](https://schema.beckn.io/mobility/passengerCount) | [schema:Number](https://schema.org/Number) | Number of passengers |
| [vehiclePreference](https://schema.beckn.io/mobility/vehiclePreference) | [VehicleCategory](https://schema.beckn.io/mobility/VehicleCategory) | Preferred vehicle category |
| **[Properties from Intent](https://github.com/beckn/core_schema/tree/draft/schema/Intent)** | | |
| [textSearch](https://schema.beckn.io/core/textSearch) | [schema:Text](https://schema.org/Text) | Free-text search query expressing what the traveler is looking for |
| [filters](https://schema.beckn.io/core/filters) | [schema:Text](https://schema.org/Text) | JSONPath filter criteria applied to the search results |
| [spatial](https://schema.beckn.io/core/spatial) | [SpatialConstraint](https://github.com/beckn/core_schema/tree/draft/schema/SpatialConstraint) | Geographic constraints on the search area |
| [provider](https://schema.beckn.io/core/provider) | [schema:Text](https://schema.org/Text) | Identifier of a specific provider to search within |

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
