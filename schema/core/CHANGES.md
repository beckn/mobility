# Changes from Core Schema v2.0 → v2.1

**File:** `schema/core/v*/attributes.yaml`  
**Compared:** v2.0.0 → v2.1.0  
**Date:** 2026-11-02

---

## Overview

This document details all changes made to the core Beckn schema file (`attributes.yaml`) between versions 2.0 and 2.1. Version 2.1 introduces significant structural and semantic improvements, including:

- **Prefix-free schema keys** for structural decoupling
- **Expanded order/payment/fulfillment models** to support complex, multi-party transactions
- **New discovery capabilities** including multimodal search and spatial constraints
- **Improved naming consistency** (camelCase convention throughout)
- **Enhanced fulfillment modeling** with stages, authorization, and state management
- **Settlement-focused payment architecture** separating terms, actions, and settlement flows

---

## Architecture Principle: Prefix-Free Structural Schema

### What Changed
All field names in `attributes.yaml` are now **prefix-free** (e.g., `id` instead of `beckn:id` or `schema:name` instead of `"schema:name"`). JSON-LD semantics are preserved through `@context`, `@type`, and `x-jsonld` annotations.

### Why This Matters

**1. Structural contract independence**  
`attributes.yaml` serves as the structural contract (JSON Schema/OpenAPI). Hard-coding prefixes like `beckn:` or `schema:` into field names couples validation to a single semantic binding. This breaks when contexts are mixed, swapped, or versioned independently.

**2. Namespace resolution via JSON-LD only**  
Namespace and type resolution happens exclusively through JSON-LD mechanisms. The `@context` resolves terms to IRIs, and `@type` declares the class. Conflicts are resolved using scoped or layered contexts, or fully-qualified IRIs—not by embedding prefixes into the core YAML structure.

**3. Strict 3-layer separation**  
This architecture enforces a clean split:
- **`attributes.yaml`** = structure (what fields exist, their types, constraints)
- **`context.jsonld`** = term→IRI binding (how terms map to vocabularies)
- **`vocab.jsonld`** = semantics + mappings (ontological relationships, schema.org alignment)

This separation keeps the schema version-proof and prevents semantic validation errors from bleeding into structural validation.

### Forward Compatibility
This architecture allows multiple Network Protocol (NP) versions to coexist on a single Beckn network. Newer NPs only require a new context linked to an extended vocabulary. The ontological relationships in `vocab.jsonld` enable automatic mapping between protocol versions, allowing v2.0 and v2.1 (and future versions) to interoperate seamlessly.

---

## Metadata Changes

### `info` Section Updates

| Change | v2.0 | v2.1 | Rationale |
|--------|------|------|-----------|
| **Title** | Same | Same | No change |
| **Description** | Multi-line YAML block | Single-line concise description | Improved clarity; expanded description moved to documentation |
| **Version** | `2.0.0` | `2.1.0` | Version bump for breaking changes |
| **Contact name** | `Beckn Protocol` | `Beckn Labs` | Organizational update |
| **Contact URL** | `https://becknprotocol.io` | `https://beckn.io` | Official domain change |
| **License** | `MIT` | `CC-BY-NC-SA 4.0 International` | License change to Creative Commons for schema artifacts |
| **License URL** | `https://opensource.org/licenses/MIT` | `https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en` | Updated license URL |

**Rationale:** Reflects organizational changes and a move to a Creative Commons license appropriate for data schema/vocabulary artifacts rather than software code.

---

## Schema Additions

### New Core Schemas in v2.1

#### Discovery & Search
- **`DiscoveryIntent`** - Structured declaration of catalog discovery intent (text search, filters, spatial constraints, media search)
- **`MediaSearch`** - Container for multimodal search inputs (images, audio, video)
- **`MediaInput`** - Reference to media resources used in search (image/audio/video)
- **`MediaSearchOptions`** - Configuration for how discovery engines process media (OCR, ASR, object detection, semantic matching)
- **`SpatialConstraint`** - OGC CQL2-compliant spatial predicates for location-based discovery

**Rationale:** Enable richer discovery experiences beyond text-only search, supporting visual search, voice search, and precise geospatial queries using industry-standard formats (GeoJSON, CQL2).

#### Transaction Participants
- **`Consumer`** - Replaces `Buyer`; polymorphic (Person or Organization) with extensible attributes
- **`Participant`** - Generic participant in fulfillment (passengers, recipients, riders, operators, etc.)
- **`FulfillmentAgent`** - Entity performing fulfillment (person, organization, machine, AI agent)

**Rationale:** Support complex multi-party transactions where the buyer, payer, recipient, and other roles may be different entities. Aligns with schema.org's `Person`/`Organization` model.

#### Fulfillment Management
- **`FulfillmentStage`** - Individual stage within a fulfillment journey
- **`FulfillmentStageEndpoint`** - Entry/exit point in fulfillment (pickup, delivery, handover, border crossing, etc.)
- **`FulfillmentStageAuthorization`** - Credentials/documents/proofs required at fulfillment endpoints
- **`State`** - Generic state container with descriptor

**Rationale:** Model complex fulfillment scenarios (multi-leg journeys, staged deliveries, border crossings, appointment-based fulfillment) where authorization and stage-specific requirements must be tracked.

#### Payment & Settlement
- **`PaymentTerms`** - Terms of payment agreed upon (collector, checkout location, settlement terms, triggers)
- **`PaymentAction`** - Act of payment execution (status, method, transaction reference)
- **`SettlementTerm`** - Individual settlement disbursement term (amount, schedule, payee account)
- **`SettlementSchedule`** - When settlement occurs (T+X days or absolute timestamp)
- **`PaymentTrigger`** - Lifecycle stage when payment/settlement is triggered
- **`CheckoutTerminal`** - Physical/virtual location where payment is made

**Rationale:** Separate payment *terms* (contractual) from payment *action* (execution) from *settlement* (disbursement). Enables multi-party settlement scenarios, escrow, delayed payments, and complex B2B payment flows.

#### Documents & Credentials
- **`Document`** - Parsable/printable document with security attributes (signature, checksum)
- **`MediaFile`** - Display-oriented media (images, audio, video)
- **`Credential`** - Verifiable credential or license
- **`Entitlement`** - Ticket, voucher, pass, or token granting access

**Rationale:** Distinguish between display media and documents requiring verification. Support verifiable credentials and entitlements across use cases (ticketing, healthcare, education, finance).

#### Operational & Governance
- **`Alert`** - Notifications about service disruptions, order issues, etc.
- **`Policy`** - Formal policy declaration (cancellation, return, refund, terms of service)
- **`Constraint`** - Quantitative constraint with operator (≤, ≥, =, etc.)
- **`Instruction`** - Actionable instruction for users or systems
- **`Skill`** - Required or offered skill (for matching agents to tasks)
- **`SupportTicket`** - Support ticket raised against an order

**Rationale:** Provide first-class support for operational scenarios (service alerts, policy enforcement, support workflows) and enable skill-based fulfillment matching.

#### Catalog & Discovery Results
- **`CatalogProcessingResult`** - Outcome of catalog submission/processing
- **`ProcessingNotice`** - Non-fatal issue encountered during processing

**Rationale:** Enable catalog publication workflows with detailed validation feedback.

#### Tracking
- **`TrackingRequest`** - Request for tracking handle (with callback, mode hints)
- **`TrackAction`** - Minimal schema.org TrackAction for clickable tracking

**Rationale:** Separate tracking *request* from tracking *handle*, support streaming updates via callbacks/websockets.

#### Ratings
- **`DisplayedRating`** - Read-only rating display (aggregated)
- **`RatingInput`** - User-submitted rating with category and feedback

**Rationale:** Distinguish between displayed aggregate ratings and user input for new ratings.

#### Supporting Types
- **`CancellationOutcome`** - Outcome of cancellation request
- **`CancellationPolicy`** - Cancellation policy declaration
- **`CancellationReason`** - Reason for cancellation
- **`RefundTerms`** - Refund destination and terms (placeholder for future expansion)

**Rationale:** Formalize cancellation workflows with policies, reasons, and outcomes.

---

## Schema Modifications

### `AckResponse` (Breaking)

**Changes:**
- **Field name changes:**
  - `transaction_id` → `transactionId` (camelCase)
  - `ack_status` → `ackStatus` (camelCase)
- **Moved to top of schema list** (alphabetical ordering)
- **Added TODO comment:** "Signature spec to be added as per Abhishek's Issue"

**Rationale:** Naming consistency (camelCase). TODO indicates planned cryptographic signature support for non-repudiation.

---

### `Attributes` (Non-breaking)

**Changes:**
- **Removed** `minProperties: 2` constraint
- **Updated description** from "bag" to "container"
- **Updated example values** for clarity

**Rationale:** Removed artificial minimum property constraint. Clearer wording.

---

### `Catalog` (Breaking)

**v2.0 structure (prefixed):**
```yaml
properties:
  "@context": enum with hardcoded v2 URL
  "@type": example "beckn:Catalog"
  "beckn:id": string
  "beckn:descriptor": $ref
  "beckn:providerId": string
  "beckn:bppId": string
  "beckn:bppUri": uri
  "beckn:validity": TimePeriod
  "beckn:isActive": boolean
  beckn:items: array of Item
  beckn:offers: array of Offer
```

**v2.1 structure (prefix-free):**
```yaml
properties:
  '@context': const with v2.1 URL
  "@type": const "beckn:Catalog"
  id: string
  descriptor: $ref (with added description)
  providerId: string
  bppId: string
  bppUri: uri
  validity: TimePeriod
  isActive: boolean
  items: array of Item (with added description)
  offers: array of Offer
```

**Key changes:**
- All `beckn:*` prefixes removed from property names
- `@context` changed from `enum` to `const` (stricter validation)
- `@context` URL updated to v2.1 path (`draft` branch)
- `@type` changed from example to `const` (stricter validation)
- Added verbose descriptions to several properties

**Rationale:** Implement prefix-free architecture. Stricter validation via `const`. Updated URLs to reflect new repository structure. Improved self-documentation.

---

### `Item` (Breaking)

**v2.0 structure (prefixed):**
```yaml
properties:
  "@context": enum with v2 URL
  "@type": enum ["beckn:Item"]
  "beckn:id": string
  "beckn:descriptor": $ref
  "beckn:category": CategoryCode
  "beckn:availableAt": Location[]
  "beckn:availabilityWindow": TimePeriod[]
  "beckn:rateable": boolean
  "beckn:rating": Rating
  "beckn:isActive": boolean
  "beckn:networkId": string[]
  "beckn:provider": Provider
  "beckn:itemAttributes": Attributes
```

**v2.1 structure (prefix-free):**
```yaml
properties:
  '@context': const with v2.1 URL
  "@type": enum ["Item"]
  id: string
  descriptor: $ref
  category: CategoryCode
  availableAt: Location[]
  availabilityWindow: TimePeriod[]
  rateable: boolean
  rating: Rating (undefined ref)
  isActive: boolean
  networkId: string[]
  provider: Provider
  itemAttributes: Attributes
  constraints: Constraint[] (NEW)
  policies: Policy[] (NEW)
```

**Key changes:**
- Prefix removal across all properties
- **Added fields:**
  - `constraints` - Array of constraints applicable to this item
  - `policies` - Array of policies (return, warranty, etc.)
- URL and validation tightening (same as Catalog)

**Rationale:** Enable item-level constraints (min/max quantity, geographic restrictions) and policies (essential for retail/commerce).

---

### `Offer` (Breaking)

**v2.0 structure:**
```yaml
properties:
  beckn:id, beckn:descriptor, beckn:provider, beckn:items,
  beckn:addOns, beckn:addOnItems, beckn:isActive,
  beckn:validity, beckn:price, beckn:eligibleRegion,
  beckn:acceptedPaymentMethod, beckn:offerAttributes
```

**v2.1 structure:**
```yaml
properties:
  id, descriptor, provider, items, addOns, addOnItems,
  isActive, validity, price, eligibleRegion, acceptedPaymentMethod,
  offerAttributes,
  constraints (NEW), policies (NEW), features (NEW)
```

**Key changes:**
- Prefix removal
- **Added fields:**
  - `constraints` - Offer-specific constraints
  - `policies` - Offer-specific policies
  - `features` - Highlighted features of the offer

**Rationale:** Support promotional offers with feature highlights, constraints (limited-time, quantity limits), and policies (non-refundable, etc.).

---

### `Provider` (Breaking)

**v2.0 structure:**
```yaml
properties:
  "beckn:id", "beckn:descriptor", "beckn:validity",
  "beckn:locations", "beckn:rateable", "beckn:rating",
  "beckn:providerAttributes"
```

**v2.1 structure:**
```yaml
properties:
  '@context': const (NEW)
  "@type": default "beckn:Provider" (NEW)
  id, descriptor, validity, locations, rateable, rating,
  providerAttributes,
  alerts: Alert[] (NEW),
  policies: Policy[] (NEW)
```

**Key changes:**
- Added `@context` and `@type` (Provider is now a first-class JSON-LD entity)
- **Added fields:**
  - `alerts` - Service disruption alerts
  - `policies` - Provider-level policies

**Rationale:** Enable providers to communicate service alerts and formal policies. Make Provider independently addressable as a JSON-LD entity.

---

### `Descriptor` (Breaking)

**v2.0 structure:**
```yaml
properties:
  "@type": enum ["beckn:Descriptor"]
  "schema:name": string
  "beckn:shortDesc": string
  "beckn:longDesc": string
  "schema:image": array of uri
```

**v2.1 structure:**
```yaml
properties:
  "@context": uri (NEW, default to v2.1)
  "@type": string (default "beckn:Descriptor")
  name: string
  shortDesc: string
  longDesc: string
  thumbnailImage: uri (NEW)
  docs: Document[] (NEW)
  mediaFile: MediaFile[] (NEW)
```

**Key changes:**
- Prefix removal from all property names
- **Removed** `schema:image` array
- **Added fields:**
  - `@context` - Allows context-specific descriptors
  - `thumbnailImage` - Single thumbnail URL
  - `docs` - Array of structured documents
  - `mediaFile` - Array of structured media files

**Rationale:** Replace generic `image` array with structured, typed media and document arrays. Separate thumbnails from gallery media. Enable rich media descriptions with MIME types, labels, security attributes.

---

### `CategoryCode` (Minor breaking)

**Changes:**
- **Added** `@context` property (default "schema:CategoryCode")
- **Changed** `@type` from enum to default (allows override)
- Prefix removal from `schema:*` properties (now direct properties)

**Rationale:** Allow context-specific category code systems while defaulting to schema.org CategoryCode.

---

### `TimePeriod` (Minor breaking)

**Changes:**
- Prefix removal from `schema:*` properties
- Changed `@type` from example to typed property
- Validation cleanup (anyOf remains)

**Rationale:** Consistency with prefix-free architecture.

---

### `Order` (Breaking - Major restructure)

**v2.0 structure:**
```yaml
properties:
  beckn:id, beckn:orderStatus, beckn:orderNumber,
  beckn:seller (Provider ref),
  beckn:buyer (Buyer ref),
  beckn:orderItems (OrderItem[]),
  beckn:acceptedOffers (Offer[]),
  beckn:orderValue (PriceSpecification),
  beckn:invoice (Invoice ref),
  beckn:payment (Payment ref),
  beckn:fulfillment (Fulfillment ref),
  beckn:orderAttributes (Attributes)
```

**v2.1 structure:**
```yaml
properties:
  '@context': const
  "@type": enum ["Order"]
  id, orderStatus, orderNumber, orderValue, orderAttributes,
  provider (Provider, was seller),
  consumer (Consumer, was buyer),
  orderItems (OrderItem[]),
  fulfillments (Fulfillment[], was singular),
  invoices (Invoice[], was singular),
  paymentTerms (PaymentTerms, NEW),
  paymentAction (PaymentAction, NEW),
  participants (Participant[], NEW),
  orderDocs (Document[], NEW),
  policies (Policy[], NEW)
```

**Key changes:**
- **Renamed:** `seller` → `provider`, `buyer` → `consumer`
- **Removed:** `acceptedOffers` (captured per line item), `payment` (replaced by paymentTerms + paymentAction)
- **Changed cardinality:** `invoice` → `invoices[]`, `fulfillment` → `fulfillments[]`
- **Added:**
  - `paymentTerms` - Contractual payment terms
  - `paymentAction` - Payment execution status
  - `participants` - All transaction participants
  - `orderDocs` - Order-level documents
  - `policies` - Order-level policies
- **Added order status:** `UNDER_NEGOTIATION` (for dynamic pricing/negotiation flows)

**Rationale:**
1. Separate buyer (commercial entity) from consumer (end recipient) to support B2B2C flows
2. Support multiple fulfillments per order (split shipments, multi-leg journeys)
3. Support multiple invoices per order (partial invoicing, multiple sellers)
4. Separate payment *terms* from payment *action* for clearer settlement modeling
5. Explicit participant tracking for compliance/audit

---

### `OrderItem` (Breaking)

**v2.0 structure:**
```yaml
properties:
  beckn:lineId, beckn:orderedItem (Item ref),
  beckn:acceptedOffer (Offer),
  beckn:quantity (Quantity),
  beckn:price (PriceSpecification),
  beckn:orderItemAttributes (Attributes)
```

**v2.1 structure:**
```yaml
properties:
  lineId, itemId (Item ref, was orderedItem),
  acceptedOffer (Offer),
  quantity (Quantity),
  price (PriceSpecification),
  orderItemAttributes (Attributes)
```

**Key changes:**
- Prefix removal
- **Renamed:** `orderedItem` → `itemId` for consistency

**Rationale:** Naming consistency across schemas.

---

### `Invoice` (Breaking)

**v2.0 structure:**
```yaml
properties:
  beckn:id, beckn:number, beckn:issueDate, beckn:dueDate,
  beckn:payee (Provider id ref),
  beckn:payer (Buyer id ref),
  beckn:totals (PriceSpecification),
  beckn:invoiceAttributes (Attributes)
```

**v2.1 structure:**
```yaml
properties:
  '@context': const, "@type": enum ["Invoice"],
  id, number, issueDate, dueDate,
  payee (full Provider object),
  payer (full Consumer object),
  costBreakup (PriceSpecification[]),
  invoiceAttributes (Attributes)
```

**Key changes:**
- Prefix removal
- **Replaced:** `totals: PriceSpecification` → `costBreakup: PriceSpecification[]`
- **Changed:** `payee/payer` from ID references to full objects

**Rationale:**
1. Support itemized invoices with multiple cost components (tax, fees, discounts)
2. Embed full party details in invoice for regulatory compliance and offline readability
3. Align with commercial invoice requirements (full party addresses, tax IDs, etc.)

---

### `Fulfillment` (Breaking - Complete rewrite)

**v2.0 structure:**
```yaml
properties:
  beckn:id, beckn:fulfillmentStatus, beckn:mode (enum),
  trackingAction (TrackAction),
  beckn:deliveryAttributes (Attributes)
```

**v2.1 structure:**
```yaml
properties:
  '@context': const, "@type": enum ["Fulfillment"],
  id, mode (FulfillmentMode ref),
  agent (FulfillmentAgent),
  fulfillmentAttributes (Attributes),
  currentState (Descriptor),
  instructions (Descriptor[]),
  participants (Participant[]),
  state (State),
  stages (FulfillmentStage[]),
  trackingEnabled (boolean)
```

**Key changes:**
- Removed `fulfillmentStatus` and `trackingAction` (moved to attributes or stages)
- **Added:**
  - `agent` - Entity performing fulfillment
  - `currentState` - Current fulfillment state (human-readable)
  - `instructions` - Fulfillment instructions
  - `participants` - Who is entitled to fulfillment
  - `state` - Structured state object
  - `stages` - Multi-stage fulfillment journey
  - `trackingEnabled` - Whether tracking is available
- **Changed:** `mode` from enum to complex object reference

**Rationale:** Model complex fulfillment scenarios (multi-leg journeys, staged delivery, appointment-based fulfillment) with explicit agent assignment, participant tracking, and stage-by-stage authorization.

---

### `Tracking` (Breaking)

**v2.0 structure:**
```yaml
properties:
  "@context", "@type": ["beckn:Tracking"],
  tl_method: enum [http/get, http/post, ...],
  url: uri,
  trackingStatus: enum [ACTIVE, DISABLED, COMPLETED],
  expires_at: date-time
required: ["@context", "@type", "tl_method", "url", "trackingStatus"]
```

**v2.1 structure:**
```yaml
properties:
  '@context': const, "@type": default "beckn:Tracking",
  url: uri,
  trackingStatus: enum [ACTIVE, DISABLED, COMPLETED],
  expiresAt: date-time (was expires_at)
required: ["@context", "@type", "url", "trackingStatus"]
```

**Key changes:**
- **Removed:** `tl_method` (transport/method field)
- **Renamed:** `expires_at` → `expiresAt` (camelCase)
- **Removed** `tl_method` from required fields

**Rationale:** 
1. Naming consistency (camelCase convention)
2. `tl_method` was rarely used and added complexity; tracking URL alone is sufficient for modern implementations
3. Transport/method can be inferred from URL scheme or specified in extended attributes if needed

---

### `RatingInput` (Breaking)

**Changes:**
- Prefix removal from all fields
- Changed from v2 `RatingInput` to cleaner v2.1 structure
- Added `@context` as required field

**Rationale:** Consistency with prefix-free architecture and JSON-LD requirements.

---

### `Form` (Minor breaking)

**v2.0 structure:**
```yaml
properties:
  url, data, mime_type (enum), submission_id
```

**v2.1 structure:**
```yaml
properties:
  '@context': const, "@type": enum ["Form"],
  url, data, mimeType (string, not enum), submissionId
```

**Key changes:**
- **Renamed:** `mime_type` → `mimeType`, `submission_id` → `submissionId`
- **Changed:** `mimeType` from enum to open string
- **Added:** `@context` and `@type`

**Rationale:** CamelCase consistency. Remove MIME type restrictions (allow any valid MIME type). Make Form a first-class JSON-LD entity.

---

### `SupportInfo` (Minor breaking)

**Changes:**
- Prefix removal
- Added `@context` and `@type` as required
- No functional changes to support channel properties

**Rationale:** Consistency with JSON-LD architecture.

---

## Schema Removals

### `Buyer` (Removed)

**v2.0 definition:**
```yaml
Buyer:
  properties:
    beckn:id, beckn:role, beckn:displayName,
    beckn:telephone, beckn:email, beckn:taxID,
    beckn:buyerAttributes
```

**v2.1 replacement:** `Consumer` (polymorphic Person/Organization)

**Rationale:** "Buyer" conflates commercial role with identity. `Consumer` better represents end users while supporting both individual and organizational identities. This enables B2B2C scenarios where buyer ≠ consumer.

---

### `Payment` (Removed)

**v2.0 definition:**
```yaml
Payment:
  properties:
    beckn:id, beckn:paymentStatus, beckn:amount,
    beckn:paymentURL, beckn:txnRef, beckn:paidAt,
    beckn:acceptedPaymentMethod, beckn:beneficiary,
    beckn:paymentAttributes
```

**v2.1 replacements:**
- `PaymentTerms` (contractual terms)
- `PaymentAction` (execution/status)
- `SettlementTerm` (disbursement details)

**Rationale:** Single `Payment` object conflated three concerns: payment agreement (terms), payment execution (action), and fund disbursement (settlement). Separation enables:
1. Multi-party settlement (marketplace, escrow, split payments)
2. Delayed payment triggers (pre-order, on-delivery, post-fulfillment)
3. Explicit settlement schedules (T+7, T+30, etc.)
4. Compliance with financial regulations requiring separation of concerns

---

## Known Gaps / TODOs - Resolution Summary

All previously identified gaps in v2.1 `attributes.yaml` have been **resolved** as of 2026-11-02:

### ✅ Resolved Gaps

1. **`Person`** - ✅ **ADDED** - Defined with schema.org alignment (name, age, knowsLanguage, worksFor, contact details)
2. **`Organization`** - ✅ **ADDED** - Defined with schema.org alignment (name, address, contact, organizationAttributes for domain-specific extensions)
3. **`Rating`** - ✅ **ADDED** - Defined aligning with DisplayedRating shape (ratingValue, ratingCount, reviewText, bestRating, worstRating)
4. **`Feature`** - ✅ **REMOVED** - Explicitly removed as it was determined to be unnecessary (features can be expressed through Descriptor or Attributes)
5. **`Description`** - ✅ **FIXED** - Typo in `Policy.descriptor` corrected to properly reference `Descriptor` schema
6. **`Time`** - ✅ **ADDED** - Defined with schema.org alignment supporting timestamps, durations, time ranges (TimePeriod), and labels
7. **`FulfillmentMode`** - ✅ **ADDED** - Defined as generic, extensible schema without hardcoded enums to allow domain-specific fulfillment modes

### Context Mappings

All new schemas and their properties have been added to `context.jsonld` with appropriate semantic mappings:
- Person and Organization mapped to schema.org equivalents
- Schema-specific properties (age, knowsLanguage, worksFor) mapped to schema.org
- Time, Rating, and FulfillmentMode mapped to beckn namespace
- Feature references removed from context

### Architectural Principles Maintained

- ✅ Prefix-free property names in attributes.yaml
- ✅ Schema.org vocabulary reuse where applicable
- ✅ Generic/extensible patterns (no hardcoded enums in core types)
- ✅ Strict 3-layer separation (structure/context/semantics)

### Outstanding Context Coverage

A context-checker validation identified 47 keywords in `attributes.yaml` not yet mapped in `context.jsonld`:
- 1 schema name (PaymentTrigger with scoped enums)
- 8 properties (checksumAlgorithm, duration, keyId, range, required, signatureAlgorithm, textSearch, x-jsonld)
- 38 enumeration values (spatial operators, geometry types, price component types, media search goals, etc.)

These are **not gaps** in schema definitions but rather unmapped terms that exist in the structural schema. They can be added to context.jsonld incrementally as needed for semantic validation.

---

## Notable Breaking Changes Summary

This section provides a high-level overview of changes that **will break** existing v2.0 implementations without code/payload modifications:

### 1. **Field Name Changes (Structural)**
- **All** `beckn:*` and `schema:*` prefixed field names are now prefix-free
- **Examples:** `"beckn:id"` → `id`, `"schema:name"` → `name`
- **Impact:** JSON payloads using prefixed keys will fail schema validation

### 2. **Actor Model Changes**
- `Buyer` schema removed → replaced by `Consumer`
- `Order.seller` → `Order.provider`
- `Order.buyer` → `Order.consumer`
- **Impact:** Order payloads must use new field names and Consumer structure

### 3. **Payment Architecture Changes**
- `Payment` schema removed
- Replaced by `PaymentTerms` + `PaymentAction` + `SettlementTerm`
- **Impact:** Payment modeling must be refactored to separate terms/actions/settlement

### 4. **Fulfillment Model Changes**
- `Fulfillment.mode` changed from enum to complex object
- `Fulfillment.fulfillmentStatus` removed (use `state` or `currentState`)
- Added `stages`, `agent`, `participants`, etc.
- **Impact:** Fulfillment payloads must adopt new structure

### 5. **Invoice Model Changes**
- `Invoice.totals` → `Invoice.costBreakup[]` (now array)
- `Invoice.payee/payer` changed from ID reference to full object
- **Impact:** Invoice generation logic must adapt

### 6. **Tracking Changes**
- `tl_method` field removed
- `expires_at` → `expiresAt`
- **Impact:** Tracking implementations relying on `tl_method` must be updated

### 7. **Cardinality Changes**
- `Order.invoice` → `Order.invoices[]` (singular to array)
- `Order.fulfillment` → `Order.fulfillments[]` (singular to array)
- **Impact:** Order processing must handle multiple invoices/fulfillments

### 8. **Context URL Changes**
- All `@context` URLs updated from `/main/schema/core/v2/` to `/draft/schema/core/v2.1/`
- **Impact:** JSON-LD processors must fetch from new URL

### 9. **Validation Strictness**
- Many `example` annotations changed to `const` or `enum`
- **Impact:** More rigid validation; invalid values will fail

### 10. **Naming Convention**
- `snake_case` → `camelCase` throughout (e.g., `transaction_id` → `transactionId`)
- **Impact:** All field references must be updated

---

## Migration Considerations

While this document does not provide a full migration guide, implementers should note:

1. **JSON-LD processing unchanged** - Despite structural changes, JSON-LD expansion/compaction produces compatible RDF
2. **Semantic equivalence** - Most changes are structural; semantic meaning preserved through `vocab.jsonld` mappings
3. **Coexistence possible** - v2.0 and v2.1 can coexist on the same network with proper context handling
4. **Gradual migration** - Networks can support both versions during transition period

A detailed field-by-field migration guide will be provided separately.

---

## Conclusion

Version 2.1 represents a significant evolution of the Beckn core schema, driven by real-world implementation experience and the need for clearer separation between structure and semantics. The prefix-free architecture, expanded transaction models, and enhanced fulfillment capabilities position Beckn to support increasingly complex commerce scenarios while maintaining backward compatibility at the semantic level.

For questions or clarification on specific changes, please refer to the Beckn community forums or raise an issue in the protocol-specifications-v2 repository.
