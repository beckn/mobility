# Beckn Protocol — Mobility Domain

> Stable, dereferenceable IRIs for the mobility domain — enabling any Beckn-enabled mobility application to achieve semantic interoperability by binding their data models to a shared set of meanings, not just a shared wire format.

## Contents

- [Latest Version](#latest-version) · [Earlier Versions](#earlier-versions)
- [Status](#status)
- [About](#about)
- [Repository Structure](#repository-structure)
- [Documentation](#documentation)
- [Local Testing — Devkit](#local-testing--devkit)
- [Why This Repository Exists](#why-this-repository-exists)
- [Global Mobility Standards Landscape](#global-mobility-standards-landscape)
- [Beckn Ecosystem & Schema Publishing](#beckn-ecosystem--schema-publishing)
- [Contributing](#contributing)
- [Related Resources](#related-resources)

---

## Latest Version

2.0.0

This version is an adaptation of Beckn protocol [core version 2.0.0 LTS](https://github.com/beckn/protocol-specifications-v2/releases/tag/core-v2.0.0-lts). It replaces the earlier, key-based `mobility.yaml` API specification (v0.x, adapted from Beckn core v1.x) with an IRI-based ontology and mobility-tagged schemas published from [beckn/schemas](https://github.com/beckn/schemas), backed by worked example implementations and a local devkit for end-to-end testing.

## Earlier Versions

Prior to 2.0.0, mobility versioning followed its own independent lineage rather than tracking core version-for-version; the table below shows which core version each was adapted from.

| Version | Release Date | Core Version | Author | Comments |
|---------|--------------|--------------|--------|----------|
| 0.9.0 | March 20, 2024 | 1.0.0 LTS | Ravi Prakash | Adaptation of core v1.0.0 LTS |
| 0.8.0 | April 4, 2023 | 0.9.4 | Ravi Prakash | Compatible with LTS version of core |
| 0.7.0 | November 14, 2022 | 0.9.3 | Ravi Prakash | Re-initialized Mobility Adaptation specification with independent versioning from core |

### Earlier Versions (Deprecated)

| Version | Release Date |
|---------|--------------|
| 0.9.2 | August 3, 2021 (Active) |
| 0.8.2 | August 28, 2020 (Active) |
| 0.8.0 | August 23, 2020 (deprecated) |
| 0.7.1 | April 27, 2020 (deprecated) |

---

## Status

**Released v2.0.0** — Mobility domain schema definitions (YAML/JSON-LD) are authored and published from the separate [beckn/schemas](https://github.com/beckn/schemas) repository, not from this one. This repository holds documentation, the mobility ontology and standards research, worked example payloads for six ride-hailing-adjacent use cases, and a local devkit for exercising the full transaction lifecycle end to end.

---

## About

This repository is the **mobility working area** for [Beckn Protocol v2](https://github.com/beckn/protocol-specifications-v2) — the ontology design, standards research, worked examples, and local test devkit that inform and validate the mobility-tagged schemas published from [beckn/schemas](https://github.com/beckn/schemas). It provides:

- **Ontology design** — the conceptual model for mobility entities (vehicles, ride offers, fare structures, pickup/drop points, driver profiles, and more) and how they map onto Beckn Core types and global standards (GTFS, GBFS, NeTEx, schema.org, and others)
- **Standards landscape analysis** — a comprehensive survey of global mobility standards and their JSON-LD / RDF compatibility, informing how mobility schemas relate to the broader ecosystem
- **Worked example implementations** — complete, schema-validated request/response payloads across the full transaction lifecycle for six use cases (ride-hailing, bike rental, car rental, driver hire, metro fare, multimodal itinerary) — see [`docs/example_implementations/`](./docs/example_implementations/)
- **A local devkit** — a runnable BAP/BPP adapter stack for driving the ride-hailing example lifecycle end to end with Postman — see [`testnet/mobility-devkit/`](./testnet/mobility-devkit/)
- **Documentation** — transaction flows, API usage examples, and ecosystem architecture for mobility networks built on Beckn v2

The actual schema definitions (YAML sources, JSON-LD contexts, RDF vocabularies) are authored and published from **[beckn/schemas](https://github.com/beckn/schemas)**, dereferenceable at **[schema.beckn.io](https://schema.beckn.io)** (e.g. `https://schema.beckn.io/RideOption/v2.0`) and browsable, searchable, and consumable by both human developers and AI agents.

---

## Repository Structure

```
mobility/
├── docs/
│   ├── README.md                                  # Documentation table of contents
│   ├── 1_Overview.md                               # Overview of the mobility adaptation
│   ├── Mobility_Ontology.md                        # Ontology design for the mobility domain
│   ├── Global_Mobility_Standards_Landscape.md      # 19-standard JSON-LD/RDF compatibility survey
│   ├── API-Flows.md
│   ├── example_implementations/                    # Worked payload examples, per use case
│   │   ├── ride_hailing/                           #   discover -> support, 6 transport modes
│   │   ├── cab_rental/
│   │   ├── advance_cab_reservation/
│   │   ├── intercity_bus/
│   │   ├── metro_ticket_booking/
│   │   └── public_transit_bus/
│   └── assets/
│       └── images/
│           └── Ecosystem Architecture.png
├── testnet/
│   └── mobility-devkit/        # Local BAP/BPP adapter stack for the ride-hailing example
│                                #   -- see testnet/mobility-devkit/README.md for setup
├── sandbox-payloads/            # Canned on_* fixtures the devkit's mock BPP serves
├── LICENSE.md
└── README.md                    # This file
```

---

## Documentation

The [`docs/`](./docs/) folder contains:

1. [Overview](./docs/1_Overview.md) — Overview of the mobility domain adaptation
2. [API Flows](./docs/API-Flows.md) — Transaction flows for taxi and bus booking
3. [Mobility Ontology](./docs/Mobility_Ontology.md) — Ontology design for the mobility domain
4. [Global Mobility Standards Landscape](./docs/Global_Mobility_Standards_Landscape.md) — see the [dedicated section](#global-mobility-standards-landscape) below
5. [Ecosystem Architecture](./docs/assets/images/Ecosystem%20Architecture.png) — Reference mobility ecosystem diagram
6. [Example Implementations](./docs/example_implementations/) — Complete, schema-validated request/response payloads across the full transaction lifecycle (`discover` → `support`) for six use cases: ride-hailing, cab rental, advance cab reservation, intercity bus, metro ticket booking, and public transit bus

---

## Local Testing — Devkit

[`testnet/mobility-devkit/`](./testnet/mobility-devkit/) wires the `ride_hailing` (`cab_hailing`) example to a runnable local BAP/BPP adapter stack, so the full lifecycle can be driven with Postman and observed end to end — not just read as static JSON. It bundles ONIX adapter configs, routing rules, a Caddy reverse proxy with optional ngrok tunnel support, a docker-compose stack, and ready-to-import Postman collections.

Its mock BPP is backed by canned response fixtures under [`sandbox-payloads/`](./sandbox-payloads/), resolved from the `ride_hailing` example content.

See **[testnet/mobility-devkit/README.md](./testnet/mobility-devkit/README.md)** for prerequisites, quick start, configuration reference, and known limitations — it currently covers only the `cab_hailing` use case, and `discover`/`on_discover` have no backing mock (there's no local Discover/CDS service to route to).

---

## Why This Repository Exists

### The Problem with Key-Based Integration

Building a Beckn-compatible mobility application today typically means writing a transformer — code that maps your internal data model to specific JSON keys in the Beckn API payload:

```
my internal Trip object  →  { "items": [...], "fulfillments": [...], "quote": {...} }
```

This works, but it is **brittle and non-interoperable at the semantic level**. Two applications that both produce the same JSON keys may mean entirely different things by them. There is no machine-readable way to know whether another application's `"items"` means the same thing as yours.

### The Solution: Map to IRIs, Not Keys

Beckn solves that problem with **stable, dereferenceable IRIs** for every mobility concept — `RideOption`, `Driver`, `PickupDropoffPoint`, `FareEstimate`, and more — authored with input from this repository's ontology work and published from [beckn/schemas](https://github.com/beckn/schemas).

Instead of writing:

> *"My `Trip` maps to `items[0]` in the Beckn payload"*

You declare:

> *"My `Trip` **is a** `https://schema.beckn.io/RideOption/v2.0`"*

Your internal data model is bound to a **meaning** (an IRI), not a position in a JSON structure. The Beckn API payload then becomes a serialization of that meaning — not the source of truth for it.

### The Interoperability Chain

```
Your internal data model
        │
        │  maps to
        ▼
Beckn Mobility IRIs                 ← beckn/schemas (informed by this repo's ontology work)
(schema.beckn.io/RideOption/v2.0,
 schema.beckn.io/Driver/v2.0,
 schema.beckn.io/PickupDropoffPoint/v2.0…)
        │
        │  subClassOf / property mappings
        ▼
Beckn Core IRIs                     ← beckn/schemas + protocol-specifications-v2
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

If **your** ride-hailing platform maps its `Driver` to `beckn:Driver` (`https://schema.beckn.io/Driver/v2.0`), and **another** platform's dispatch system also maps its driver concept to the same IRI — you interoperate **semantically**, not just syntactically.

This means:
- **Design-time validation**: tooling can verify your data model is correctly aligned with Beckn Mobility IRIs before you deploy
- **Run-time composability**: BAPs, BPPs, and intermediaries can inspect `@type` and `@context` in a Beckn message to understand what they are receiving — and decide what they can do with it — without bilateral agreements on field names
- **Future-proofing**: if the Beckn JSON payload structure evolves, your IRI bindings remain valid and your integration does not break
- **Cross-ecosystem reach**: because Beckn Mobility IRIs are aligned with schema.org, your data is interpretable by any system that speaks linked data — not just Beckn networks

---

## Global Mobility Standards Landscape

[`docs/Global_Mobility_Standards_Landscape.md`](./docs/Global_Mobility_Standards_Landscape.md) contains a comprehensive analysis of **19 major global mobility standards**, evaluated for JSON-LD / RDF / OWL compatibility — directly relevant to how Beckn Mobility IRIs are aligned with the broader mobility ecosystem. A related, differently-structured catalogue of mobility standards (validation schema / RDF-OWL ontology / persistent IRI / JSON–RDF mapping criteria) is also available at [`docs/3_Mobility_Standards.md`](./docs/3_Mobility_Standards.md).

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

## Beckn Ecosystem & Schema Publishing

The mobility work in this repository builds on:

| Repository | Role |
|-----------|------|
| [beckn/protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2) | Beckn v2 protocol envelope — universal `/beckn/{action}` API, core JSON-LD context and vocabulary (v2.0.0 LTS) |
| [beckn/schemas](https://github.com/beckn/schemas) | All Beckn v2.0.0 schema definitions — domain-agnostic transaction schemas (`Contract`, `Commitment`, `Fulfillment`, etc.) alongside mobility-tagged (`x-tags: [mobility, ...]`) schemas such as `RideOption`, `Fare`, `Driver`, `VehicleCategory` |
| [schema.beckn.io](https://schema.beckn.io) | Public schema registry — hosts and serves every schema from `beckn/schemas` |

Mobility schemas aren't a separately-versioned pack layered on top of core, and they aren't authored in this repository — they live in the same flat `beckn/schemas` repository as everything else, distinguished by domain tags (`x-tags: [mobility, ...]`) rather than a separate namespace or a separate repo. This repository's ontology and standards research inform that authoring process; the worked examples and devkit here validate against what it publishes.

- **Published at**: [schema.beckn.io](https://schema.beckn.io), flat namespace (no `/mobility/` path segment)
- **IRI format**: `https://schema.beckn.io/<SchemaName>/v<version>` (e.g. `https://schema.beckn.io/RideOption/v2.0`)
- **Sync**: GitHub-first from `beckn/schemas`; schema changes there flow to the registry
- **Representations**: Each IRI returns HTML (for developers), YAML (canonical source), JSON-LD, and Turtle/RDF depending on `Accept` header or URL suffix

---

## Contributing

Contributions to this repository — ontology work, standards research, example implementations, or devkit improvements — are welcome. Contributors must follow the contribution guidelines in the `CONTRIBUTION.md` document in this repository. Contributions to the mobility schemas themselves belong in [beckn/schemas](https://github.com/beckn/schemas).

Each contribution will be peer-reviewed by the Mobility Working Group members before being merged.

To follow discussions related to the mobility specification, visit the [Discussions Forum](https://github.com/beckn/mobility/discussions) on GitHub.

To connect with the Mobility Working Group and the broader Beckn Open Collective, join the [Beckn Open Collective Discord Server](https://discord.gg/vxNjTzsgcP).

---

## Related Resources

| Resource | Link |
|----------|------|
| Beckn Protocol v2 specification | https://github.com/beckn/protocol-specifications-v2 |
| Beckn schema definitions (core + domain-tagged) | https://github.com/beckn/schemas |
| Beckn schema registry | https://schema.beckn.io |
| DeDi protocol (network registry) | https://dedi.global |
| Beckn website | https://beckn.io |
| Beckn Open Collective Discord | https://discord.gg/vxNjTzsgcP |

---

*Last updated: July 2026*
