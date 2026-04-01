# Passenger

A schema.beckn.io Type

A person who travels using a transport service and is identified in a booking or travel document.

**Canonical IRI :** `mobility:Passenger`

**Canonical URL:** https://schema.beckn.io/mobility/Passenger

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:Participant](https://github.com/beckn/core_schema/tree/draft/schema/Participant) | rdfs:subClassOf | Subclass |
| [schema:Person](https://schema.org/Person) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Passenger](https://schema.beckn.io/mobility/Passenger)** | | |
| [passengerId](https://schema.beckn.io/mobility/passengerId) | [schema:Text](https://schema.org/Text) | Unique identifier for the passenger in this booking |
| [passengerType](https://schema.beckn.io/mobility/passengerType) | [schema:Text](https://schema.org/Text) | Classification of passenger (e.g. ADULT, CHILD, SENIOR, STUDENT) |
| [specialRequirements](https://schema.beckn.io/mobility/specialRequirements) | [schema:Text](https://schema.org/Text) | Accessibility or special assistance requirements |
| **[Properties from Participant](https://github.com/beckn/core_schema/tree/draft/schema/Participant)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the participant |
| [person](https://schema.beckn.io/core/person) | [Person](https://github.com/beckn/core_schema/tree/draft/schema/Person) | Personal details of the participant |
| [organization](https://schema.beckn.io/core/organization) | [Organization](https://github.com/beckn/core_schema/tree/draft/schema/Organization) | Organisation the participant belongs to |
| [entitlements](https://schema.beckn.io/core/entitlements) | [Entitlement](https://github.com/beckn/core_schema/tree/draft/schema/Entitlement) | Entitlements held by the participant |

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
