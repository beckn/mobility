# How to navigate this folder

You’re looking at a **three-file schema package** where each file plays a distinct role in the data contract. Read them in this order and with a clear objective per file.


## What each file is for

### 1) `attributes.yaml` — **structural contract + validation surface**

This file defines the **JSON shape**:

* which object types exist (e.g., `Order`, `Item`, `Payment`)
* required fields
* field types (`string`, `array`, `object`)
* constraints (`enum`, formats, min/max, etc.)

In most setups like this, the actionable content is under:

* `components.schemas.<Type>.required`
* `components.schemas.<Type>.properties`

You also typically see an extension like `x-jsonld` on fields. Treat that as a **semantic pointer** that ties a JSON field to a JSON-LD term IRI.

**Primary question this file answers:**

> “What fields are allowed and what constitutes a valid instance?”


### 2) `context.jsonld` — **term mapping and compaction/expansion rules**

This file defines how JSON keys map to **IRIs** and how values should be interpreted during JSON-LD expansion.

Typical contents:

* prefix definitions (e.g., `schema`, `rdf`, `xsd`, plus your domain prefix like `beckn`)
* term definitions (mapping `"name"` → `schema:name`, `"orderStatus"` → `beckn:orderStatus`, etc.)
* value mappings for enums (mapping `"CANCELLED"` → `beckn:OrderCancelled`, etc.)
* `@type` coercion rules (e.g., treat a field as an `@id`)

**Primary question this file answers:**

> “When a payload contains key `X` and value `Y`, what exact IRIs do they correspond to?”


### 3) `vocab.jsonld` — **vocabulary/ontology definitions**

This is the **domain vocabulary**: the canonical definitions for classes, properties, and enumerations.

Typical contents (usually in `@graph`):

* classes (`rdfs:Class`)
* properties (domain/range, labels, comments)
* enumerations and their members

**Primary question this file answers:**

> “What does this term represent in the domain model?”

## How to read them effectively: trace one field end-to-end

Pick a single property and resolve it across all three layers. This prevents you from reading the files as three disconnected artifacts.

### Example: `Order.orderStatus`

#### Step A — Start in `attributes.yaml` (constraints)

Locate:

* `components.schemas.Order.properties["beckn:orderStatus"]`

Extract:

* the JSON type (e.g., `string`)
* allowed values (`enum`: `CREATED`, `PENDING`, `CONFIRMED`, …)
* the semantic binding if present:

  * `x-jsonld: { "@id": "beckn:orderStatus" }`

Outcome:

* You know the **validation rule set** for the field.
* You know which **semantic property** it is intended to represent.

#### Step B — Go to `context.jsonld` (mapping behavior)

Find the context entry for `orderStatus` (or the equivalent compact term).

You should see:

* the property mapping to `beckn:orderStatus`
* a rule such as `@type: "@id"` if the value is intended to expand into an IRI
* a nested mapping for enum tokens:

  * `"CREATED"` → `beckn:OrderCreated`
  * `"CANCELLED"` → `beckn:OrderCancelled`
  * etc.

Outcome:

* You know **exactly how** the string enum token is transformed into an identifier in the expanded JSON-LD/RDF representation.

#### Step C — Validate meaning in `vocab.jsonld` (domain definition)

In `vocab.jsonld`, locate:

* the definition of `beckn:OrderStatus` (likely an enumeration)
* the member terms such as `beckn:OrderCancelled`, `beckn:OrderCreated`, etc.

Outcome:

* You know how the term is defined conceptually (labels/comments), and you can verify the enum member inventory is consistent with the YAML/context.


## Recommended reading order and workflow

1. **Inventory object types and required fields** from `attributes.yaml`.
   This gives you the “API surface area” quickly.

2. For any field you care about, use `x-jsonld.@id` (if present) to jump to the corresponding term in `context.jsonld` / `vocab.jsonld`.

3. Use `context.jsonld` to determine:

   * the **exact IRI** for each field
   * whether values are interpreted as strings vs identifiers (`@type: "@id"`)
   * how enums map from tokens to term IRIs

4. Use `vocab.jsonld` as the authoritative **domain glossary** for:

   * term definitions
   * class/property relationships
   * enumeration membership


## Important boundary: mapping vs validation

* `context.jsonld` + `vocab.jsonld` establish **semantics** (meaning and identifiers).
* `attributes.yaml` establishes **syntactic validity** (shape/type/enums/required).

JSON-LD by itself does **not** enforce constraints like “required field” or “enum membership.” If you need **semantic validation** on the expanded graph (e.g., constraints based on RDF types and relationships), that is typically done with **SHACL** or **ShEx** after expansion.

