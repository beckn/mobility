# Vehicle — v2.0

A motorized or human-powered mobility asset used to carry passengers or goods between locations.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Vehicle/attributes.yaml](https://schema.beckn.io/Vehicle/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Vehicle/v2.0/attributes.yaml](https://schema.beckn.io/Vehicle/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Vehicle/attributes.jsonschema.yaml](https://schema.beckn.io/Vehicle/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Vehicle/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Vehicle/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Vehicle/context.jsonld](https://schema.beckn.io/Vehicle/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Vehicle/v2.0/context.jsonld](https://schema.beckn.io/Vehicle/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Vehicle/vocab.jsonld](https://schema.beckn.io/Vehicle/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Vehicle/v2.0/vocab.jsonld](https://schema.beckn.io/Vehicle/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `vehicleId` | no | string | Unique identifier for the vehicle |
| `licensePlate` | no | string | Vehicle registration plate number |
| `make` | no | string | Manufacturer of the vehicle |
| `model` | no | string | Model name of the vehicle |
| `year` | no | number | Year of manufacture |
| `color` | no | string | Colour of the vehicle |
| `vehicleType` | no | $ref: https://schema.beckn.io/VehicleType/v2.0/attributes.yaml#/components/schemas/VehicleType | Type classification of the vehicle |
| `id` | no | string | Unique identifier for the item |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the item |
| `categoryId` | no | $ref: https://schema.beckn.io/CategoryCode/v2.1/attributes.yaml#/components/schemas/CategoryCode | Category code classifying the item |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Price specification for this item |
| `quantity` | no | $ref: https://schema.beckn.io/Quantity/v2.0/attributes.yaml#/components/schemas/Quantity | Available quantity of the item |
| `tags` | no | string | Tags associated with the item |
