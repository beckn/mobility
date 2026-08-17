# Passenger — v2.0

A person who travels using a transport service and is identified in a booking or travel document.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Passenger/attributes.yaml](https://schema.beckn.io/Passenger/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Passenger/v2.0/attributes.yaml](https://schema.beckn.io/Passenger/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Passenger/attributes.jsonschema.yaml](https://schema.beckn.io/Passenger/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Passenger/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Passenger/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Passenger/context.jsonld](https://schema.beckn.io/Passenger/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Passenger/v2.0/context.jsonld](https://schema.beckn.io/Passenger/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Passenger/vocab.jsonld](https://schema.beckn.io/Passenger/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Passenger/v2.0/vocab.jsonld](https://schema.beckn.io/Passenger/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `passengerId` | no | string | Unique identifier for the passenger in this booking |
| `passengerType` | no | string | Classification of passenger (e.g. ADULT, CHILD, SENIOR, STUDENT) |
| `specialRequirements` | no | string | Accessibility or special assistance requirements |
| `id` | no | string | Unique identifier for the participant |
| `person` | no | $ref: https://schema.beckn.io/Person/v2.0/attributes.yaml#/components/schemas/Person | Personal details of the participant |
| `organization` | no | $ref: https://schema.beckn.io/Organization/v2.0/attributes.yaml#/components/schemas/Organization | Organisation the participant belongs to |
| `entitlements` | no | $ref: https://schema.beckn.io/Entitlement/v2.0/attributes.yaml#/components/schemas/Entitlement | Entitlements held by the participant |
