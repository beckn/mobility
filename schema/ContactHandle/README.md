# ContactHandle

A schema.beckn.io Type

A communication handle (such as a phone number, email address, or chat URL) used to contact a driver or support agent in a mobility service.

**Canonical IRI :** `mobility:ContactHandle`

**Canonical URL:** https://schema.beckn.io/mobility/ContactHandle

**Related Classes:**

| Type | Relationship | Strength |
|------|--------------|----------|
| [beckn:SupportInfo](https://github.com/beckn/core_schema/tree/draft/schema/SupportInfo) | rdfs:subClassOf | Subclass |

## Open Issues

[Open issues](https://github.com/beckn/mobility/issues)

## Properties

| Property | Expected Type | Description |
|---|---|---|
| **[Properties from ContactHandle](https://schema.beckn.io/mobility/ContactHandle)** | | |
| [handleType](https://schema.beckn.io/mobility/handleType) | [schema:Text](https://schema.org/Text) | Type of contact handle (PHONE, EMAIL, CHAT, APP) |
| [handle](https://schema.beckn.io/mobility/handle) | [schema:Text](https://schema.org/Text) | The actual contact handle value (number, address, or URL) |
| [label](https://schema.beckn.io/mobility/label) | [schema:Text](https://schema.org/Text) | Human-readable label for this contact handle |
| **[Properties from SupportInfo](https://github.com/beckn/core_schema/tree/draft/schema/SupportInfo)** | | |
| [phone](https://schema.beckn.io/core/phone) | [schema:Text](https://schema.org/Text) | Support phone number |
| [email](https://schema.beckn.io/core/email) | [schema:Text](https://schema.org/Text) | Support email address |
| [url](https://schema.beckn.io/core/url) | [schema:URL](https://schema.org/URL) | URL to support portal or chat interface |

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
