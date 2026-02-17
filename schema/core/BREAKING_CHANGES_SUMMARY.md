# Breaking Changes Summary - Schema.org Alignment

## Date: 2026-11-02

## Overview
Performed breaking changes to align Beckn vocabulary with schema.org by remapping context keys and removing redundant vocabulary definitions that override schema.org IRIs.

## Files Modified

### 1. context.jsonld
**Changes:** Updated 6 term mappings from `beckn:*` to `schema:*`

| Term | Previous Mapping | New Mapping |
|------|-----------------|-------------|
| `displayName` | `beckn:displayName` | `schema:alternateName` |
| `PriceSpecification` | `beckn:PriceSpecification` | `schema:PriceSpecification` |
| `price` | `beckn:price` | `schema:price` |
| `eligibleQuantity` | `beckn:eligibleQuantity` | `schema:eligibleQuantity` |
| `unitText` | `beckn:unitText` | `schema:unitText` |
| `unitCode` | `beckn:unitCode` | `schema:unitCode` |

**Impact:** This is a BREAKING CHANGE. All JSON documents using these terms will now expand to schema.org IRIs instead of Beckn IRIs.

### 2. vocab.jsonld
**Changes:** Removed 8 @graph entries (1 class + 7 properties)

**Removed Entries:**
- `beckn:PriceSpecification` (Class)
- `beckn:price` (Property)
- `beckn:unitText` (Property)
- `beckn:unitCode` (Property)
- `beckn:eligibleQuantity` (Property)
- `beckn:displayName` (Property)
- `schema:telephone` (Property - was overriding schema.org)
- `schema:email` (Property - was overriding schema.org)

**Updated References:** 8 properties that referenced `beckn:PriceSpecification` in their domain/range were updated to reference `schema:PriceSpecification`

**Entry Count:** 430 → 423 entries

### 3. updated.vocab.jsonld
**Changes:** Same 8 @graph entries removed as vocab.jsonld

**Entry Count:** 431 → 423 entries

## Rationale
- **Avoid Override:** Beckn should not override standard schema.org terms with custom definitions
- **Direct Schema.org Usage:** Where terms directly map to schema.org, use the schema.org IRIs directly
- **Semantic Alignment:** `displayName` mapped to `schema:alternateName` as it represents an alternate name for display purposes

## Validation Results
✓ All JSON files are valid
✓ No orphaned references to removed IRIs
✓ All domain/range references updated correctly

## Migration Path for Consumers
1. **JSON Documents:** No changes required - context mapping handles the IRI expansion
2. **RDF/SPARQL Queries:** Update queries to use `schema:*` IRIs instead of `beckn:*` for the 6 remapped terms
3. **Semantic Consumers:** Update any hardcoded references to the removed Beckn IRIs

## Terms Kept "On Standby" (Group B - 40 banking/payment terms)
These terms have schema.org equivalences but were NOT changed in this iteration:
- Payment-related terms (paymentDueDate, paymentStatus, etc.)
- Banking terms (accountId, bankCode, ifscCode, etc.)
- Financial instrument terms

Decision: Keep for potential future alignment after ecosystem consultation.
