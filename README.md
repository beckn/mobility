# Beckn Protocol — Mobility Domain Schema Pack

> Stable, dereferenceable IRIs for the mobility domain — enabling any Beckn-enabled mobility application to achieve semantic interoperability by binding their data models to a shared set of meanings, not just a shared wire format.

## 🚧 Status

**Work in Progress** — This repository is being set up as a Beckn v2 domain schema pack for the mobility sector. Schema YAML files are in progress. Documentation and the global mobility standards landscape analysis are available now.

---

## Why This Repository Exists

### The Problem with Key-Based Integration

Building a Beckn-compatible mobility application today typically means writing a transformer — code that maps your internal data model to specific JSON keys in the Beckn API payload:

```
my internal Trip object  →  { "items": [...], "fulfillments": [...], "quote": {...} }
```

This works, but it is **brittle and non-interoperable at the semantic level**. Two applications that both produce the same JSON keys may mean entirely different things by them. There is no machine-readable way to know whether another application's `"items"` means the same thing as yours.

### The Solution: Map to IRIs, Not Keys

This repository solves that problem by providing **stable, dereferenceable IRIs** for every mobility concept — `RideOffer`, `Driver`, `PickupPoint`, `FareEstimate`, and more.

Instead of writing:

> *"My `Trip` maps to `items[0]` in the Beckn payload"*

You declare:

> *"My `Trip` **is a** `https://schema.beckn.io/mobility/RideOffer`"*

Your internal data model is bound to a **meaning** (an IRI), not a position in a JSON structure. The Beckn API payload then becomes a serialization of that meaning — not the source of truth for it.

### The Interoperability Chain

```
Your internal data model
        │
        │  maps to
        ▼
Beckn Mobility IRIs                 ← this repository
(schema.beckn.io/mobility/RideOffer,
 schema.beckn.io/mobility/Driver,
 schema.beckn.io/mobility/PickupPoint…)
        │
        │  subClassOf / property mappings
        ▼
Beckn Core IRIs                     ← beckn/core_schema + protocol-specifications-v2
(schema.beckn.io/Item,
 schema.beckn.io/Provider,
 schema.beckn.io/Location…)
        │
        │  aligned with
        ▼
schema.org + global vocabularies
(schema:Vehicle, schema:Offer,
 schema:Order, schema:GeoCoordinates…)
        │
        │  understood by
        ▼
Any Beckn-enabled mobility application
```

### The Developer Payoff

If **your** ride-hailing platform maps its `Driver` to `beckn-mobility:Driver`, and **another** platform's dispatch system also maps its driver concept to `beckn-mobility:Driver` — you interoperate **semantically**, not just syntactically.

This means:
- **Design-time validation**: tooling can verify your data model is correctly aligned with Beckn Mobility IRIs before you deploy
- **Run-time composability**: BAPs, BPPs, and intermediaries can inspect `@type` and `@context` in a Beckn message to understand what they are receiving — and decide what they can do with it — without bilateral agreements on field names
- **Future-proofing**: if the Beckn JSON payload structure evolves, your IRI bindings remain valid and your integration does not break
- **Cross-ecosystem reach**: because Beckn Mobility IRIs are aligned with schema.org, your data is interpretable by any system that speaks linked data — not just Beckn networks

---

## About

This repository is the **mobility domain schema pack** for [Beckn Protocol v2](https://github.com/beckn/protocol-specifications-v2). It provides:

- **Mobility IRIs** — stable, dereferenceable identifiers for every mobility concept: vehicle types, ride offers, fare structures, pickup/drop points, driver profiles, and more
- **Ontology mappings** — formal alignment of Beckn Mobility IRIs with Beckn Core IRIs and global standards (GTFS, GBFS, NeTEx, schema.org, and others)
- **Standards landscape analysis** — a comprehensive survey of 19 global mobility standards and their JSON-LD / RDF compatibility, informing how Beckn Mobility IRIs relate to the broader ecosystem
- **Documentation** — transaction flows, API usage examples, and ecosystem architecture for mobility networks built on Beckn v2

Schemas from this repository are published at **[schema.beckn.io/mobility](https://schema.beckn.io/mobility)** and are browsable, searchable, and consumable by both human developers and AI agents.

---

## Repository Structure

```
mobility/
├── schema/
│   └── README.md           # Global mobility standards landscape & JSON-LD alignment research
├── docs/
│   ├── README.md           # Documentation table of contents
│   ├── 1_Overview.md       # Overview of the mobility adaptation
│   ├── Mobility_Ontology.md
│   ├── API-Flows.md
│   └── assets/
│       └── images/
│           └── Ecosystem Architecture.png
├── LICENSE.md
└── README.md               # This file
```

---

## Global Mobility Standards Landscape

The [`schema/README.md`](./schema/README.md) contains a comprehensive analysis of **19 major global mobility standards**, evaluated for JSON-LD / RDF / OWL compatibility — directly relevant to how Beckn Mobility IRIs are aligned with the broader mobility ecosystem.

| Category | Standards Covered |
|----------|------------------|
| Public transit schedules & realtime | GTFS Static, GTFS-RT, SIRI, NeTEx |
| Shared & micromobility | GBFS, MDS |
| Aviation distribution & orders | IATA NDC, IATA ONE Order |
| Rail | railML, OSDM |
| Journey planning | OJP, TRIAS |
| Parking & kerbside | APDS, CDS |
| Ticketing & entitlement | Calypso, ITSO, CIPURSE |
| Regulation & policy | MDS, DATEX II |
| Reference semantics | Transmodel (EN 12896) |

The analysis also includes a **MaaS layer heat map** showing which standards apply across the discovery, availability, journey planning, booking, ticketing, and policy layers of a Mobility-as-a-Service stack — and where each standard provides usable JSON-LD contexts that Beckn Mobility IRIs can align with.

---

## schema.beckn.io Integration

This repository feeds into [schema.beckn.io](https://schema.beckn.io) — the authoritative Beckn schema registry — as a domain schema source under the `mobility` namespace.

- **Published namespace**: `https://schema.beckn.io/mobility/`
- **Sync**: GitHub-first; schema changes in this repo flow automatically to the registry
- **IRI format**: `https://schema.beckn.io/mobility/<Term>` (e.g. `https://schema.beckn.io/mobility/RideOffer`)
- **Representations**: Each IRI returns HTML (for developers), YAML (canonical source), JSON-LD, and Turtle/RDF depending on `Accept` header or URL suffix

---

## Beckn v2 Foundation

This schema pack is built on top of:

| Repository | Role |
|-----------|------|
| [beckn/protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2) | Beckn v2 protocol envelope — universal `/beckn/{action}` API, core JSON-LD context and vocabulary (v2.0.1 LTS) |
| [beckn/core_schema](https://github.com/beckn/core_schema) | Domain-agnostic transaction schemas (`RequestAction`, `CallbackAction`, `Ack`, `Order`, `Fulfillment`, etc.) — the Core IRIs that Mobility IRIs map to |
| [schema.beckn.io](https://schema.beckn.io) | Public schema registry — hosts and serves all Beckn schemas including this domain pack |

Domain schema packs like this one extend the core with vertical-specific types and properties. The base protocol and core schemas remain minimal and stable; mobility semantics evolve independently here.

---

## Documentation

The [`docs/`](./docs/) folder contains:

1. [Overview](./docs/1_Overview.md) — Schema adaptation for the mobility domain
2. [API Flows](./docs/API-Flows.md) — Transaction flows for taxi and bus booking
3. [Mobility Ontology](./docs/Mobility_Ontology.md) — Ontology design for the mobility domain
4. [Ecosystem Architecture](./docs/assets/images/Ecosystem%20Architecture.png) — Reference mobility ecosystem diagram

---

## Contributing

Contributions to this schema pack are welcome. Contributors must follow the contribution guidelines in the `CONTRIBUTION.md` document in this repository.

Each contribution will be peer-reviewed by the Mobility Working Group members. If approved, the contribution will be merged into the applicable version of the mobility schema pack.

To follow discussions related to the mobility specification, visit the [Discussions Forum](https://github.com/beckn/mobility/discussions) on GitHub.

To connect with the Mobility Working Group and the broader Beckn Open Collective, join the [Beckn Open Collective Discord Server](https://discord.gg/vxNjTzsgcP).

---

## Related Resources

| Resource | Link |
|----------|------|
| Beckn Protocol v2 specification | https://github.com/beckn/protocol-specifications-v2 |
| Beckn core transaction schema | https://github.com/beckn/core_schema |
| Beckn schema registry | https://schema.beckn.io |
| DeDi protocol (network registry) | https://dedi.global |
| Beckn website | https://beckn.io |
| Beckn Open Collective Discord | https://discord.gg/vxNjTzsgcP |

---

*Last updated: February 2026*
