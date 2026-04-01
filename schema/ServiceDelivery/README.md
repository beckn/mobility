# ServiceDelivery

A schema.beckn.io Type

The top-level response container in SIRI encapsulating one or more real-time data delivery types.

**Canonical IRI :** `mobility:ServiceDelivery`

**Canonical URL:** https://schema.beckn.io/mobility/ServiceDelivery

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from ServiceDelivery](https://schema.beckn.io/mobility/ServiceDelivery)** | | |
| [responseTimestamp](https://schema.beckn.io/mobility/responseTimestamp) | [schema:DateTime](https://schema.org/DateTime) | Timestamp when this service delivery was generated |
| [producerRef](https://schema.beckn.io/mobility/producerRef) | [schema:Text](https://schema.org/Text) | Identifier of the system producing this delivery |
| [requestMessageRef](https://schema.beckn.io/mobility/requestMessageRef) | [schema:Text](https://schema.org/Text) | Reference to the request that triggered this delivery |
| [stopMonitoring](https://schema.beckn.io/mobility/stopMonitoring) | [StopMonitoring](https://schema.beckn.io/mobility/StopMonitoring) | Stop monitoring delivery payloads |
| [vehicleMonitoring](https://schema.beckn.io/mobility/vehicleMonitoring) | [VehicleMonitoringDelivery](https://schema.beckn.io/mobility/VehicleMonitoringDelivery) | Vehicle monitoring delivery payloads |
| [estimatedTimetable](https://schema.beckn.io/mobility/estimatedTimetable) | [EstimatedTimetableDelivery](https://schema.beckn.io/mobility/EstimatedTimetableDelivery) | Estimated timetable delivery payloads |
| **[Properties from Catalog](https://github.com/beckn/core_schema/tree/draft/schema/Catalog)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the catalog |
| [descriptor](https://schema.beckn.io/core/descriptor) | [Descriptor](https://github.com/beckn/core_schema/tree/draft/schema/Descriptor) | Human-readable description of the catalog |
| [tags](https://schema.beckn.io/core/tags) | [schema:Text](https://schema.org/Text) | Tags associated with the catalog |

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
