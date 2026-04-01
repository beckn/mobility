# Rider

A schema.beckn.io Type

A person using a shared mobility service (such as a bike-share, scooter, or car-share) who has a registered account with the provider.

**Canonical IRI :** `mobility:Rider`

**Canonical URL:** https://schema.beckn.io/mobility/Rider

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
| **[Properties from Rider](https://schema.beckn.io/mobility/Rider)** | | |
| [riderId](https://schema.beckn.io/mobility/riderId) | [schema:Text](https://schema.org/Text) | Unique identifier for the rider account |
| [preferredPaymentMethod](https://schema.beckn.io/mobility/preferredPaymentMethod) | [schema:Text](https://schema.org/Text) | Rider preferred payment method |
| [membershipPlan](https://schema.beckn.io/mobility/membershipPlan) | [schema:Text](https://schema.org/Text) | Active membership or subscription plan |
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
