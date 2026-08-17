# ServiceClass — v2.0

A classification of the level of service offered by a transport service, such as economy, business, or first class.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/ServiceClass/attributes.yaml](https://schema.beckn.io/ServiceClass/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/ServiceClass/v2.0/attributes.yaml](https://schema.beckn.io/ServiceClass/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/ServiceClass/attributes.jsonschema.yaml](https://schema.beckn.io/ServiceClass/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/ServiceClass/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/ServiceClass/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/ServiceClass/context.jsonld](https://schema.beckn.io/ServiceClass/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/ServiceClass/v2.0/context.jsonld](https://schema.beckn.io/ServiceClass/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/ServiceClass/vocab.jsonld](https://schema.beckn.io/ServiceClass/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/ServiceClass/v2.0/vocab.jsonld](https://schema.beckn.io/ServiceClass/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `serviceClassCode` | no | string | Code identifying the service class (e.g. ECONOMY, BUSINESS, FIRST) |
| `features` | no | array | List of features and amenities included in this service class |
| `id` | no | string | Unique identifier for the category code |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable label for the category |
| `parentCategoryId` | no | string | Identifier of the parent category if hierarchical |
