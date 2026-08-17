# Driver — v2.0

A person who operates a transport vehicle and is responsible for the safe delivery of passengers during a mobility service trip.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Driver/attributes.yaml](https://schema.beckn.io/Driver/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Driver/v2.0/attributes.yaml](https://schema.beckn.io/Driver/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Driver/attributes.jsonschema.yaml](https://schema.beckn.io/Driver/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Driver/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Driver/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Driver/context.jsonld](https://schema.beckn.io/Driver/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Driver/v2.0/context.jsonld](https://schema.beckn.io/Driver/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Driver/vocab.jsonld](https://schema.beckn.io/Driver/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Driver/v2.0/vocab.jsonld](https://schema.beckn.io/Driver/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `licenseNumber` | no | string | Driver's license number |
| `vehicleNumber` | no | string | Registration number of the vehicle being driven |
| `yearsOfExperience` | no | number | Number of years of professional driving experience |
| `id` | no | string | Unique identifier for the fulfillment agent |
| `person` | no | $ref: https://schema.beckn.io/Person/v2.0/attributes.yaml#/components/schemas/Person | Personal details of the agent |
| `organization` | no | $ref: https://schema.beckn.io/Organization/v2.0/attributes.yaml#/components/schemas/Organization | Organisation the agent belongs to |
| `contact` | no | string | Contact information for the agent |
| `rating` | no | $ref: https://schema.beckn.io/Rating/v2.0/attributes.yaml#/components/schemas/Rating | Overall rating of the agent |
