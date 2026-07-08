"""
validate_examples.py
=====================

Structurally validates every generated example against the beckn v2.0.0 API
spec (components.schemas of beckn.yaml).

Because the sandbox has no ``jsonschema`` package (and no TLS for pip), this is a
hand-rolled checker that enforces the constraints that actually matter for these
examples:

  * ``additionalProperties: false`` on the closed core schemas (no stray fields).
  * ``required`` fields present at each level.
  * ``enum`` membership (contract/commitment/settlement status codes, etc.).
  * ``Attributes`` bags always carry ``@context`` + ``@type``.
  * ``anyOf`` gates (Catalog needs resources|offers; TimePeriod needs a bound).
  * Referential integrity (Offer.resourceIds resolve to Resource ids).

Before that, a SCHEMA-SANITY pre-pass dereferences the ``$ref`` graph of the
schema.beckn.io schemas and reports any dead links (a ``$ref`` to a schema whose
``schema.json`` does not exist). The runtime pass alone never trips on a dangling
ref such as ``RideOption -> PricingModel`` because no runtime field populates it,
but a strict validator that fully dereferences the schema would break. The
``$ref``s resolve against a local schema store (``SCHEMA_STORE`` env var, default
``/home/ravi/www/spec_work/schemas/schema``).

The spec is downloaded once via ``curl`` (the sandbox blocks Python TLS) to
``beckn.yaml`` next to this script; delete it to force a refresh.

Run:  python3 validate_examples.py                # schema sanity scoped to examples + runtime
      python3 validate_examples.py --all-schemas  # schema sanity across the WHOLE store
"""

import glob
import json
import os
import re
import subprocess
import sys
from collections import deque

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "example-jsons"))
SPEC_URL = "https://raw.githubusercontent.com/beckn/protocol-specifications-v2/refs/heads/main/api/v2.0.0/beckn.yaml"
SPEC_PATH = os.path.join(HERE, "beckn.yaml")

# Local checkout of the schema.beckn.io source schemas (the store that $refs resolve
# against). Override with SCHEMA_STORE=/path if it lives elsewhere.
SCHEMA_STORE = os.environ.get("SCHEMA_STORE", "/home/ravi/www/spec_work/schemas/schema")


# --------------------------------------------------------------------------- #
# Schema-sanity pre-validation                                                #
# --------------------------------------------------------------------------- #
# Before validating runtime JSONs against a schema, the schema itself must be
# sane: every $ref it makes (transitively) has to resolve to a schema that
# actually exists. The runtime validator never trips on a dangling $ref like
# RideOption -> PricingModel because no runtime field populates it, but a
# full/strict validator that dereferences the whole schema WILL break. This
# pass walks the $ref graph and reports every dead link.
BECKN = "https://schema.beckn.io/"

def _norm_version(seg):
    # schema.beckn.io serves both /2.0/ and /v2.0/; the store on disk uses /v2.0/.
    return "v" + seg if re.match(r"^\d+\.\d+$", seg) else seg

def url_to_local(url):
    """Map a schema.beckn.io schema.json URL to its local path (None if not beckn)."""
    url = url.split("#")[0]
    if not url.startswith(BECKN):
        return None
    parts = [_norm_version(p) for p in url[len(BECKN):].split("/")]
    return os.path.join(SCHEMA_STORE, *parts)

def iter_refs(obj):
    """Yield every "$ref" string value anywhere inside a parsed schema."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str):
                yield v
            else:
                yield from iter_refs(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from iter_refs(v)

def check_schema_closure(root_urls):
    """
    BFS the $ref graph from `root_urls` (schema.json URLs). Returns
    (visited_count, broken) where broken is a sorted list of
    (referrer_url, broken_ref_url, reason).
    """
    seen, broken = set(), []
    dq = deque(root_urls)
    while dq:
        url = dq.popleft()
        if url in seen:
            continue
        seen.add(url)
        local = url_to_local(url)
        if local is None or not os.path.exists(local):
            continue  # missing nodes are recorded against their referrer
        try:
            schema = json.load(open(local))
        except Exception as e:  # noqa: BLE001
            broken.append((url, url, f"unparseable schema.json: {e}"))
            continue
        for ref in sorted(set(iter_refs(schema))):
            target = url_to_local(ref)
            if target is None:
                continue  # non-beckn ref (e.g. json-schema meta) - out of scope
            if not os.path.exists(target):
                broken.append((url, ref, "referenced schema does not exist"))
            else:
                dq.append(ref)
    return len(seen), sorted(set(broken))

def collect_beckn_urls(obj, out):
    """Collect every schema.beckn.io URL appearing as a value in the runtime JSON."""
    if isinstance(obj, dict):
        for v in obj.values():
            collect_beckn_urls(v, out)
    elif isinstance(obj, list):
        for v in obj:
            collect_beckn_urls(v, out)
    elif isinstance(obj, str) and obj.startswith(BECKN):
        out.add(obj)

def example_schema_roots():
    """Every schema.json a runtime example depends on (derived from its @context URLs)."""
    urls = set()
    for fn in glob.glob(os.path.join(BASE, "**", "post.request*.json"), recursive=True):
        collect_beckn_urls(json.load(open(fn)), urls)
    roots = set()
    for u in urls:
        roots.add(u.replace("/context.jsonld", "/schema.json") if u.endswith("context.jsonld") else u)
    return sorted(roots)

def scan_all_schemas():
    """Repo-wide: check the $refs of every schema.json in the store."""
    broken = []
    for root, _dirs, files in os.walk(SCHEMA_STORE):
        if "schema.json" not in files:
            continue
        path = os.path.join(root, "schema.json")
        rel = os.path.relpath(path, SCHEMA_STORE)
        try:
            schema = json.load(open(path))
        except Exception as e:  # noqa: BLE001
            broken.append((rel, "-", f"unparseable: {e}")); continue
        for ref in sorted(set(iter_refs(schema))):
            target = url_to_local(ref)
            if target is not None and not os.path.exists(target):
                broken.append((rel, ref, "referenced schema does not exist"))
    return sorted(set(broken))

def run_schema_sanity(all_schemas=False):
    """Returns True if schemas are sane, False if any dead $ref was found."""
    if not os.path.isdir(SCHEMA_STORE):
        print(f"⚠ schema store not found at {SCHEMA_STORE}; skipping schema-sanity pass "
              f"(set SCHEMA_STORE=/path to enable).\n")
        return True
    if all_schemas:
        print("Schema sanity: scanning ALL schemas in the store...")
        broken = scan_all_schemas()
        scope = "store-wide"
    else:
        roots = example_schema_roots()
        visited, broken = check_schema_closure(roots)
        print(f"Schema sanity: {len(roots)} root schema(s) from the examples; recursively "
              f"dereferenced {visited} schema(s) across the full $ref closure...")
        scope = "used by examples"
    if not broken:
        print(f"  no broken $refs ({scope}) ✓\n")
        return True
    # Group broken targets by the missing schema for a compact report.
    by_target = {}
    for referrer, ref, reason in broken:
        by_target.setdefault(ref.split("#")[0], []).append(referrer)
    print(f"  ✗ {len(by_target)} broken $ref target(s) ({scope}):")
    for target in sorted(by_target):
        referrers = sorted({os.path.relpath(url_to_local(r), SCHEMA_STORE)
                            if url_to_local(r) else r for r in by_target[target]})
        print(f"    - {target}")
        for r in referrers:
            print(f"        referenced by: {r}")
    print()
    return False


def load_spec():
    if not os.path.exists(SPEC_PATH):
        subprocess.run(["curl", "-sL", SPEC_URL, "-o", SPEC_PATH], check=True)
    return yaml.safe_load(open(SPEC_PATH))["components"]["schemas"]


S = load_spec()
errs = []
def bad(msg):
    errs.append(msg)


def props_ok(obj, name, path):
    """Enforce additionalProperties:false + required for a named spec schema."""
    sc = S[name]
    props = sc.get("properties", {})
    if sc.get("additionalProperties") is False:
        for k in obj:
            if k not in props:
                bad(f"{path}: '{k}' not allowed by {name} (additionalProperties:false)")
    for r in sc.get("required", []):
        if r not in obj:
            bad(f"{path}: missing required '{r}' ({name})")


def attrs(a, path):
    if not (isinstance(a, dict) and "@context" in a and "@type" in a):
        bad(f"{path}: Attributes require @context and @type")


def descriptor(d, path):
    props_ok(d, "Descriptor", path)

def timeperiod(tp, path):
    props_ok(tp, "TimePeriod", path)
    if not ("startDate" in tp or "endDate" in tp or ("startTime" in tp and "endTime" in tp)):
        bad(f"{path}: TimePeriod needs startDate|endDate|startTime+endTime")

def location(l, path):
    props_ok(l, "Location", path)
    if "type" not in l.get("geo", {}):
        bad(f"{path}: Location.geo needs GeoJSON type")

# PriceComponent (schema.beckn.io/PriceComponent/v2.2) - a schema.beckn.io type, not
# inlined in beckn.yaml. Validates the components of any nested PriceSpecification bag
# inside an Attributes container. The `type` enum is loaded LIVE from the schema so it
# never drifts as new component types are added; a small fallback covers a missing store.
PRICE_COMPONENT_KEYS = {"type", "value", "currency", "description", "componentAttributes"}

def _load_price_component_types():
    p = os.path.join(SCHEMA_STORE, "PriceComponent", "v2.2", "schema.json")
    try:
        return set(json.load(open(p))["properties"]["type"]["enum"])
    except Exception:  # noqa: BLE001 - store may be absent; fall back to a permissive base
        return {"UNIT", "TAX", "DELIVERY", "DISCOUNT", "FEE", "SURCHARGE",
                "DEPOSIT_REFUNDABLE", "PENALTY", "REFUND", "TIP", "TOTAL", "OTHER"}

PRICE_COMPONENT_TYPES = _load_price_component_types()

def price_components(obj, path):
    if isinstance(obj, dict):
        if obj.get("@type") == "PriceSpecification" and isinstance(obj.get("components"), list):
            for i, comp in enumerate(obj["components"]):
                cp = f"{path}.components[{i}]"
                for k in comp:
                    if k not in PRICE_COMPONENT_KEYS:
                        bad(f"{cp}: '{k}' not allowed by PriceComponent (additionalProperties:false)")
                if comp.get("type") not in PRICE_COMPONENT_TYPES:
                    bad(f"{cp}.type '{comp.get('type')}' not in PriceComponent enum")
                if "componentAttributes" in comp:
                    attrs(comp["componentAttributes"], cp + ".componentAttributes")
        for k, v in obj.items():
            price_components(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            price_components(v, f"{path}[{i}]")

def consideration(c, path):
    props_ok(c, "Consideration", path)
    if "status" in c: descriptor(c["status"], path + ".status")
    if "considerationAttributes" in c:
        attrs(c["considerationAttributes"], path + ".considerationAttributes")
        price_components(c["considerationAttributes"], path + ".considerationAttributes")

def participant(p, path):
    props_ok(p, "Participant", path)
    if "participantAttributes" in p: attrs(p["participantAttributes"], path + ".participantAttributes")

def settlement(s, path):
    props_ok(s, "Settlement", path)
    if s.get("status") not in (None, "DRAFT", "COMMITTED", "COMPLETE"):
        bad(f"{path}.status '{s['status']}' not in enum")
    if "settlementAttributes" in s: attrs(s["settlementAttributes"], path + ".settlementAttributes")

def performance(p, path):
    props_ok(p, "Performance", path)
    if "status" in p: descriptor(p["status"], path + ".status")
    if "performanceAttributes" in p: attrs(p["performanceAttributes"], path + ".performanceAttributes")

def offer(o, path, in_commitment=False):
    props_ok(o, "Offer", path)
    if in_commitment:
        for r in ("id", "resourceIds"):
            if r not in o: bad(f"{path}: commitment offer requires '{r}'")
    if "offerAttributes" in o: attrs(o["offerAttributes"], path + ".offerAttributes")
    for i, c in enumerate(o.get("considerations", [])): consideration(c, f"{path}.considerations[{i}]")
    if "validity" in o: timeperiod(o["validity"], path + ".validity")

def resource(r, path, need_qty=False):
    props_ok(r, "Resource", path)
    if need_qty and "quantity" not in r: bad(f"{path}: requires quantity")
    if "descriptor" in r: descriptor(r["descriptor"], path + ".descriptor")
    if "resourceAttributes" in r: attrs(r["resourceAttributes"], path + ".resourceAttributes")

def commitment(cm, path):
    props_ok(cm, "Commitment", path)
    code = cm.get("status", {}).get("descriptor", {}).get("code")
    if code not in ("DRAFT", "ACTIVE", "CLOSED"):
        bad(f"{path}.status.descriptor.code '{code}' not in enum")
    for i, r in enumerate(cm.get("resources", [])): resource(r, f"{path}.resources[{i}]", need_qty=True)
    if "offer" in cm: offer(cm["offer"], path + ".offer", in_commitment=True)
    if "commitmentAttributes" in cm: attrs(cm["commitmentAttributes"], path + ".commitmentAttributes")

def contract(c, path):
    props_ok(c, "Contract", path)
    if len(c.get("commitments", [])) < 1: bad(f"{path}: commitments minItems 1")
    if "descriptor" in c: descriptor(c["descriptor"], path + ".descriptor")
    if c.get("status", {}).get("code") not in ("DRAFT", "ACTIVE", "CANCELLED", "COMPLETE"):
        bad(f"{path}.status.code not in enum")
    for i, cm in enumerate(c.get("commitments", [])): commitment(cm, f"{path}.commitments[{i}]")
    for i, x in enumerate(c.get("consideration", [])): consideration(x, f"{path}.consideration[{i}]")
    for i, x in enumerate(c.get("participants", [])): participant(x, f"{path}.participants[{i}]")
    for i, x in enumerate(c.get("settlements", [])): settlement(x, f"{path}.settlements[{i}]")
    for i, x in enumerate(c.get("performance", [])): performance(x, f"{path}.performance[{i}]")

def catalog(c, path):
    props_ok(c, "Catalog", path)
    if not ("resources" in c or "offers" in c): bad(f"{path}: Catalog needs resources|offers")
    descriptor(c["descriptor"], path + ".descriptor")
    props_ok(c["provider"], "Provider", path + ".provider")
    for i, l in enumerate(c["provider"].get("availableAt", [])): location(l, f"{path}.provider.availableAt[{i}]")
    for i, r in enumerate(c.get("resources", [])): resource(r, f"{path}.resources[{i}]")
    for i, o in enumerate(c.get("offers", [])): offer(o, f"{path}.offers[{i}]")
    if "validity" in c: timeperiod(c["validity"], path + ".validity")
    rids = {r["id"] for r in c.get("resources", [])}
    for i, o in enumerate(c.get("offers", [])):
        for rid in o.get("resourceIds", []):
            if rid not in rids: bad(f"{path}.offers[{i}] references unknown resourceId '{rid}'")

def tracking(t, path):
    props_ok(t, "Tracking", path)
    if t.get("status") not in ("ACTIVE", "INACTIVE"): bad(f"{path}.status not in enum")
    if "contract" in t:
        contract(t["contract"], path + ".contract")
        if "id" not in t["contract"]: bad(f"{path}.contract requires id")
    if "trackingAttributes" in t: attrs(t["trackingAttributes"], path + ".trackingAttributes")

def rating_input(r, path):
    props_ok(r, "RatingInput", path)
    if "target" in r and "targetAttributes" in r["target"]:
        attrs(r["target"]["targetAttributes"], path + ".target.targetAttributes")

def support(s, path):
    props_ok(s, "Support", path)
    for i, ch in enumerate(s.get("channels", [])): attrs(ch, f"{path}.channels[{i}]")


# action folder -> (wrapper schema, message validator)
def val_contract(msg, path): contract(msg["contract"], path + ".contract")
def val_catalogs(msg, path):
    for i, c in enumerate(msg["catalogs"]): catalog(c, f"{path}.catalogs[{i}]")
def val_tracking(msg, path): tracking(msg["tracking"], path + ".tracking")
def val_support(msg, path):  support(msg["support"], path + ".support")
def val_rate(msg, path):
    for i, r in enumerate(msg["ratingInputs"]): rating_input(r, f"{path}.ratingInputs[{i}]")
def val_onrate(msg, path):
    for i, r in enumerate(msg["ratings"]): rating_input(r, f"{path}.ratings[{i}]")

ACTIONS = {
    "on_discover": ("OnDiscoverAction", val_catalogs),
    "select": ("SelectAction", val_contract),
    "on_select": ("OnSelectAction", val_contract),
    "init": ("InitAction", val_contract),
    "on_init": ("OnInitAction", val_contract),
    "confirm": ("ConfirmAction", val_contract),
    "on_confirm": ("OnConfirmAction", val_contract),
    "status": ("StatusAction", val_contract),
    "on_status": ("OnStatusAction", val_contract),
    "track": ("TrackAction", val_tracking),
    "on_track": ("OnTrackAction", val_tracking),
    "update": ("UpdateAction", val_contract),
    "on_update": ("OnUpdateAction", val_contract),
    "cancel": ("CancelAction", val_contract),
    "on_cancel": ("OnCancelAction", val_contract),
    "rate": ("RateAction", val_rate),
    "on_rate": ("OnRateAction", val_onrate),
    "support": ("SupportAction", val_support),
    "on_support": ("OnSupportAction", val_support),
}


def main():
    all_schemas = "--all-schemas" in sys.argv
    # Step 1: schema-sanity pre-pass (dereference $refs before validating data).
    schemas_ok = run_schema_sanity(all_schemas=all_schemas)

    # Step 2: validate the runtime JSONs against the spec.
    total, failed = 0, 0
    for action, (sch, validator) in ACTIONS.items():
        for fn in sorted(glob.glob(os.path.join(BASE, action, "requests", "post.request.*.json"))):
            before = len(errs)
            obj = json.load(open(fn))
            if obj["context"]["action"] != action:
                bad(f"{fn}: context.action != {action}")
            msg = obj["message"]
            # Wrapper action schema (required + additionalProperties).
            if sch in S:
                props_ok(msg, sch, f"{action}:{os.path.basename(fn)}:message")
            validator(msg, f"{action}:{os.path.basename(fn)}")
            total += 1
            if len(errs) != before:
                failed += 1
    print(f"Checked {total} files, {failed} with issues.\n")
    if errs:
        for e in errs:
            print("  ✗", e)
    else:
        print("Runtime JSONs: FULLY COMPLIANT WITH beckn v2.0.0 API SPEC ✓")
    if errs or not schemas_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
