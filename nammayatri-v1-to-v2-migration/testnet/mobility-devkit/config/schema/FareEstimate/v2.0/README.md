# FareEstimate — v2.0

An estimated fare for a requested trip, typically returned in response to a search before the booking is confirmed.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FareEstimate/attributes.yaml](https://schema.beckn.io/FareEstimate/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FareEstimate/v2.0/attributes.yaml](https://schema.beckn.io/FareEstimate/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FareEstimate/attributes.jsonschema.yaml](https://schema.beckn.io/FareEstimate/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FareEstimate/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FareEstimate/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FareEstimate/context.jsonld](https://schema.beckn.io/FareEstimate/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FareEstimate/v2.0/context.jsonld](https://schema.beckn.io/FareEstimate/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FareEstimate/vocab.jsonld](https://schema.beckn.io/FareEstimate/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FareEstimate/v2.0/vocab.jsonld](https://schema.beckn.io/FareEstimate/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `estimatedAmount` | no | number | Estimated total fare amount |
| `currency` | no | string | ISO 4217 currency code |
| `minimumAmount` | no | number | Minimum possible fare |
| `maximumAmount` | no | number | Maximum possible fare |
| `fareBreakup` | no | $ref: https://schema.beckn.io/FareBreakup/v2.0/attributes.yaml#/components/schemas/FareBreakup | Itemised breakdown of the estimated fare |
| `id` | no | string | Unique identifier for the offer |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the offer |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Price specification for this offer |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity period of the offer |
| `tags` | no | string | Tags or labels associated with the offer |
