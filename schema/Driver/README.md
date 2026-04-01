# Driver

A schema.beckn.io Type

A person who operates a transport vehicle and is responsible for the safe delivery of passengers during a mobility service trip.

**Canonical IRI :** `mobility:Driver`

**Canonical URL:** https://schema.beckn.io/mobility/Driver

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:FulfillmentAgent](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentAgent) | owl:equivalentClass | Exact |
| [schema:Person](https://schema.org/Person) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from Driver](https://schema.beckn.io/mobility/Driver)** | | |
| [licenseNumber](https://schema.beckn.io/mobility/licenseNumber) | [schema:Text](https://schema.org/Text) | Driver's license number |
| [vehicleNumber](https://schema.beckn.io/mobility/vehicleNumber) | [schema:Text](https://schema.org/Text) | Registration number of the vehicle being driven |
| [yearsOfExperience](https://schema.beckn.io/mobility/yearsOfExperience) | [schema:Number](https://schema.org/Number) | Number of years of professional driving experience |
| **[Properties from FulfillmentAgent](https://github.com/beckn/core_schema/tree/draft/schema/FulfillmentAgent)** | | |
| [id](https://schema.beckn.io/core/id) | [schema:Text](https://schema.org/Text) | Unique identifier for the fulfillment agent |
| [person](https://schema.beckn.io/core/person) | [Person](https://github.com/beckn/core_schema/tree/draft/schema/Person) | Personal details of the agent |
| [organization](https://schema.beckn.io/core/organization) | [Organization](https://github.com/beckn/core_schema/tree/draft/schema/Organization) | Organisation the agent belongs to |
| [contact](https://schema.beckn.io/core/contact) | [schema:Text](https://schema.org/Text) | Contact information for the agent |
| [rating](https://schema.beckn.io/core/rating) | [Rating](https://github.com/beckn/core_schema/tree/draft/schema/Rating) | Overall rating of the agent |

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
