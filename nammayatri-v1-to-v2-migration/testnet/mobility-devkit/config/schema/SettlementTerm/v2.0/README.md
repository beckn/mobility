# SettlementTerm — v2.0

Describes the terms of settlement associated with a given transaction. This is not to be confused with the PaymentAction as it describes all the places where the money gets disbursed after reconciliation.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SettlementTerm/attributes.yaml](https://schema.beckn.io/SettlementTerm/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/SettlementTerm/v2.0/attributes.yaml](https://schema.beckn.io/SettlementTerm/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SettlementTerm/attributes.jsonschema.yaml](https://schema.beckn.io/SettlementTerm/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/SettlementTerm/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/SettlementTerm/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/SettlementTerm/context.jsonld](https://schema.beckn.io/SettlementTerm/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/SettlementTerm/v2.0/context.jsonld](https://schema.beckn.io/SettlementTerm/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SettlementTerm/vocab.jsonld](https://schema.beckn.io/SettlementTerm/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/SettlementTerm/v2.0/vocab.jsonld](https://schema.beckn.io/SettlementTerm/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | no | string | - |
| `@type` | no | string | - |
| `amount` | no | object | Amount associated with this settlement action |
| `paymentTrigger` | no | $ref: https://schema.beckn.io/PaymentTrigger/v2.0/attributes.yaml#/components/schemas/PaymentTrigger | Describes the event which triggers the payment against this settlement term |
| `settlementStatus` | no | string | - |
| `settlementSchedule` | no | $ref: https://schema.beckn.io/SettlementSchedule/v2.0/attributes.yaml#/components/schemas/SettlementSchedule | - |
| `payTo` | no | any | Describes the details of the account where the money must be remited. It could be a bank account, a payment gateway, or a virtual payment address (like a UPI ID) |
| `acceptedPaymentMethods` | no | array | Describes the methods or mechanisms accepted by the payee (described in the payTo property) for the purpose of this settlement. |
| `settlementTermAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Additional use case specific settlement terms that must be adhered to |
