# FulfillmentStop — v2.0

A specific location associated with a fulfillment (trip or journey) at which passengers board, alight, or transfer between services.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FulfillmentStop/attributes.yaml](https://schema.beckn.io/FulfillmentStop/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FulfillmentStop/v2.0/attributes.yaml](https://schema.beckn.io/FulfillmentStop/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FulfillmentStop/attributes.jsonschema.yaml](https://schema.beckn.io/FulfillmentStop/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FulfillmentStop/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FulfillmentStop/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FulfillmentStop/context.jsonld](https://schema.beckn.io/FulfillmentStop/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FulfillmentStop/v2.0/context.jsonld](https://schema.beckn.io/FulfillmentStop/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FulfillmentStop/vocab.jsonld](https://schema.beckn.io/FulfillmentStop/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FulfillmentStop/v2.0/vocab.jsonld](https://schema.beckn.io/FulfillmentStop/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `stopType` | no | string | Role of this stop in the fulfillment (START, END, INTERMEDIATE) |
| `scheduledTime` | no | string | Scheduled arrival or departure time at this stop |
| `actualTime` | no | string | Actual arrival or departure time at this stop |
| `stopRef` | no | $ref: https://schema.beckn.io/Stop/v2.0/attributes.yaml#/components/schemas/Stop | Reference to the Stop entity for this fulfillment stop |
| `passengerCount` | no | $ref: https://schema.beckn.io/PassengerCount/v2.0/attributes.yaml#/components/schemas/PassengerCount | Passenger count at this fulfillment stop |
| `id` | no | string | Unique identifier for the fulfillment stop |
| `location` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Geographic location of the stop |
| `type` | no | string | Type of stop (start, end, intermediate) |
| `instructions` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Instructions for passengers at this stop |
| `time` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Expected time window at this stop |
