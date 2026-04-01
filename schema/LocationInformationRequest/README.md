# LocationInformationRequest

A schema.beckn.io Type

A request for details about a specific geographic location, stop, or point of interest in the transport network.

**Canonical IRI :** `mobility:LocationInformationRequest`

**Canonical URL:** https://schema.beckn.io/mobility/LocationInformationRequest

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Intent](https://github.com/beckn/core_schema/tree/draft/schema/Intent) | rdfs:subClassOf | Subclass |
| [mobility:Place](https://schema.beckn.io/mobility/Place) | rdfs:seeAlso | Related |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from LocationInformationRequest](https://schema.beckn.io/mobility/LocationInformationRequest)** | | |
| [requestType](https://schema.beckn.io/mobility/requestType) | [schema:Text](https://schema.org/Text) | Type of location information requested (e.g. STOP, ADDRESS, POI) |
| [locationName](https://schema.beckn.io/mobility/locationName) | [schema:Text](https://schema.org/Text) | Name or keyword to search for |
| [coordinates](https://schema.beckn.io/mobility/coordinates) | [GeoJSONGeometry](https://github.com/beckn/core_schema/tree/draft/schema/GeoJSONGeometry) | Geographic coordinates to query around |
| [radius](https://schema.beckn.io/mobility/radius) | [schema:Number](https://schema.org/Number) | Search radius in metres |
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
