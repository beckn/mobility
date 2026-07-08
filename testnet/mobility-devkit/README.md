# Mobility Devkit — Beckn Protocol v2.0.0

Wires the `cab_hailing` ride-hailing example (see
[`docs/example_implementations/ride_hailing`](../../docs/example_implementations/ride_hailing))
to a runnable local BAP/BPP adapter stack, so the full ride-hailing lifecycle can be
driven with Postman and actually observed end to end — not just read as static JSON.

Modelled on [beckn-onix's `generic-devkit`](https://github.com/beckn/beckn-onix/tree/testnet/testnet/generic-devkit),
reusing its shared `bap.example.com` / `bpp.example.com` testnet sandbox credentials,
with a `sandbox-bpp` payload mount (pattern borrowed from `local-retail`'s
`retail-devkit`) so responses are realistic ride-hailing content instead of generic stubs.

> **Scope note:** this devkit only wires up the `cab_hailing` use case. The
> `ride-hailing-examples` branch also has metro fare, bike rental, driver hire, car
> rental, and multimodal itinerary examples — none of those are wired here yet.
>
> **Known content caveats** (inherited from the source example set, not fixed by this
> devkit): the flow never reaches a `COMPLETE` contract status (only `ACTIVE`, post
> `update`, or `CANCELLED`, via `cancel`), `on_cancel`'s settlements have a duplicate
> `id`, and `rate`/`support` don't fully match the `RatingInput`/`SupportRequest`
> core schemas. See the review this devkit was scoped from for detail. Once the
> source example-jsons are fixed, re-run `scripts/resolve_sandbox_payloads.py` and
> `scripts/build_postman_collections.py` to refresh this devkit's fixtures/collections.

---

## Prerequisites

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) — installed and running
2. [Git](https://git-scm.com/downloads) — on your system path
3. [Postman](https://www.postman.com/downloads/) — for sending API calls

---

## Repository Structure

```text
mobility-devkit/
├── config/          # ONIX adapter configs (keys, schema validator, routing)
├── install/         # docker-compose stack, Caddy reverse proxy, ngrok tunnel config
├── postman/         # BAP and BPP Postman collections for the full ride-hailing lifecycle
└── scripts/         # generator scripts that (re)build postman/ and sandbox-payloads/
                      #   from docs/example_implementations/ride_hailing/example-jsons/
```

The mock BPP's canned response fixtures live outside this folder, at
[`sandbox-payloads/nfh.global/testnet-mobility/response/`](../../sandbox-payloads/nfh.global/testnet-mobility/response)
(repo root), mirroring the `local-retail` convention of keeping sandbox fixtures
alongside — not inside — the devkit directory.

---

## Quick Start

**1. Start the adapter stack**

```bash
cd testnet/mobility-devkit/install
docker compose -f docker-compose-mobility.yml up -d
docker ps
```

You should see six containers: `beckn-router`, `redis`, `onix-bap`,
`onix-bpp`, `sandbox-bap`, `sandbox-bpp`.

> These container/network names match `generic-devkit` and `retail-devkit` exactly.
> Only one of these devkit stacks can run at a time on this machine — stop any other
> running Beckn devkit first (`docker compose down` in its `install/` folder), since
> container names and ports (8081/8082/3001/3002/6379/9000) would otherwise collide.

**2. Import the Postman collections**

Import both files from `postman/`:
- **BAP — Beckn Mobility Ride-Hailing Devkit** — the 10 outbound requests a rider's app sends
- **BPP — Beckn Mobility Ride-Hailing Devkit** — the 10 `on_*` callbacks, for testing the BAP receiver directly with unsolicited pushes (e.g. a driver-arriving push mid-trip)

**3. Run the flow**

Use the **BAP collection**, in order:

| # | Action | Folder |
|---|---|---|
| 1 | `discover` | 1 — Discovery |
| 2 | `select` → `init` → `confirm` | 2 — Transaction |
| 3 | `status` → `track` → `update` → `cancel` | 3 — Fulfillment |
| 4 | `rate` → `support` | 4 — Post-Fulfillment |

Each request returns a synchronous `ACK`. The matching `on_*` callback (served from the
`sandbox-bpp` fixture) arrives back at `onix-bap`'s receiver and is
forwarded to `sandbox-bap`, where it can be seen in logs:

```bash
docker logs -f onix-bap
docker logs -f sandbox-bap
```

`cancel` and `update` in this set are illustrative alternate endings from the same
contract (see the scope note above) rather than one continuous story — run them as
separate demonstrations, not back-to-back on the same "trip."

---

## Configuration Reference

### Postman Collection Variables

| Variable | Default value | Notes |
|---|---|---|
| `version` | `2.0.0` | Beckn protocol version |
| `networkId` | `nfh.global/testnet-mobility` | Matches `context.networkId` |
| `bap_id` | `bap.example.com` | BAP subscriber ID (shared testnet sandbox credential) |
| `bap_uri` | `{{public_url}}/bap/receiver` | BAP callback URL, routed via `beckn-router` |
| `bpp_id` | `bpp.example.com` | BPP subscriber ID (shared testnet sandbox credential) |
| `bpp_uri` | `{{public_url}}/bpp/receiver` | BPP endpoint URL, routed via `beckn-router` |
| `bap_adapter_url` | `http://localhost:8081/bap/caller` | BAP collection target |
| `bpp_adapter_url` | `http://localhost:8082/bpp/caller` | BPP collection target |
| `transaction_id` | fixed UUID | Shared across the full flow; change for a new session |

`messageId` and `timestamp` are auto-generated per request via Postman's `{{$guid}}`
and `{{$isoTimestamp}}`.

### Why fixed URLs instead of registry-resolved routing

Unlike `generic-devkit` (which routes `select`/`init`/`confirm`/... to `targetType: bpp`,
resolved via the live DeDi registry), every routing rule here uses `targetType: url`
pointing directly at the other adapter's container (`onix-bap:8081` /
`onix-bpp:8082`). The shared `bap.example.com`/`bpp.example.com` sandbox
credentials are registered under `beckn.one/testnet` in the DeDi registry, not under
this devkit's own `nfh.global/testnet-mobility` network ID, so a registry-resolved
route wouldn't resolve here. Fixed URLs keep the devkit fully self-contained (no
external registry dependency) while still exercising both adapters' full pipeline —
sign, schema validation, ack — rather than skipping straight to the mock.

For the same reason, `discover` is also routed through `onix-bpp` rather than
to a live Discover Service URL (as `generic-devkit` does) — there's no registered
mobility discovery service to point at yet.

### Adapter Endpoints

| Adapter | Path | Purpose |
|---|---|---|
| BAP | `http://localhost:8081/bap/caller/` | Send outbound action requests (Postman target) |
| BAP | `http://localhost:8081/bap/receiver/` | Receive inbound `on_*` callbacks |
| BPP | `http://localhost:8082/bpp/caller/` | Send outbound `on_*` callbacks (Postman target) |
| BPP | `http://localhost:8082/bpp/receiver/` | Receive inbound action requests |

### Registry & Keys

Ships with the same **testnet sandbox credentials** as `beckn-onix`'s `generic-devkit`
(`bap.example.com` / `bpp.example.com`, pre-registered on `beckn.one/testnet` via the
DeDi registry). To register your own subscriber IDs and keys, follow the
[DeDi registration guide](https://developers.becknprotocol.io/) and update the
`keyManager` block in `config/mobility-bap.yaml` / `config/mobility-bpp.yaml`.

### Schema Validation

Both adapters validate all payloads against the canonical Beckn v2.0.0 OpenAPI spec,
with extended (domain-specific) schema validation enabled against `schema.beckn.io`
and `raw.githubusercontent.com` (needed for the mobility `*Attributes` schema types
used throughout these examples — `RideOption`, `FareEstimate`, `SurgeMultiplier`,
`Driver`, `Passenger`, etc.).

### Remote/public callbacks (ngrok)

```bash
cp install/ngrok.yml.example install/ngrok.yml   # fill in authtoken (+ static domain)
ngrok start --all --config install/ngrok.yml
```

Then point `public_url` (used to derive `bap_uri`/`bpp_uri`) at the tunnel URL instead
of `http://beckn-router:9000`.

---

## Message Flow

```
Postman (BAP coll.) ──POST /bap/caller/<action>──► onix-bap:8081
                                                         │ signs, routes by fixed URL
                                                         ▼
                                                  onix-bpp:8082
                                                         │ forwards to sandbox-bpp
                                                         ▼
                                                  sandbox-bpp:3002
                                                         │ returns canned on_<action> fixture
                                                         ▼
                                                  onix-bpp:8082 ──POST /bpp/caller/on_<action>──►
                                                         │ signs, routes by fixed URL          onix-bap:8081
                                                         ▼                                            │ forwards to sandbox-bap
                                                                                                       ▼
                                                                                                sandbox-bap:3001
                                                                                                (view response in logs)
```

---

## Regenerating fixtures and collections

If the `cab_hailing` content under `docs/example_implementations/ride_hailing/example-jsons/`
changes (e.g. once the known content caveats above are fixed):

```bash
python3 scripts/resolve_sandbox_payloads.py      # refreshes sandbox-payloads/.../response/*.json
python3 scripts/build_postman_collections.py     # refreshes postman/*.postman_collection.json
```

Both scripts only read from `example-jsons/` and write to `sandbox-payloads/` /
`postman/` — they never modify the source example files.

---

## Stopping the Environment

```bash
docker compose -f docker-compose-mobility.yml down
```

---

## Troubleshooting

**Container fails to start**
```bash
docker pull fidedocker/onix-adapter
docker pull fidedocker/sandbox-2.0:latest
```

**Schema validation error** — verify the payload matches the v2.0.0 spec:
```bash
docker logs onix-bap 2>&1 | grep -i "schema\|error"
```

**`on_*` callback not received** — check BAP receiver logs:
```bash
docker logs -f onix-bap
```

**Sandbox health check fails** — allow 10–15 seconds for sandbox containers to
initialise:
```bash
docker logs sandbox-bap
docker logs sandbox-bpp
```
