#!/usr/bin/env python3
import copy
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TARGET_SCHEMA_ROOT = ROOT / "schema"
MOBILITY_SCHEMA_ROOT = ROOT / "schema"
SOURCE_LOGISTICS_ROOT = (ROOT / ".." / "logistics").resolve()
SOURCE_LOGISTICS_SCHEMA_ROOT = SOURCE_LOGISTICS_ROOT / "schema"
DOC_ONTOLOGY = SOURCE_LOGISTICS_ROOT / "docs" / "Logistics_Ontology.md"
DOC_SEMANTIC = SOURCE_LOGISTICS_ROOT / "docs" / "3_Semantic_Relationships_With_Beckn.md"


def list_schema_dirs(base: Path):
    out = []
    for p in sorted(base.iterdir()):
        if p.is_dir() and (p / "v2.0" / "attributes.yaml").exists():
            out.append(p.name)
    return out


def parse_logistics_ontology(md: str):
    classes = {}
    for m in re.finditer(r"^###\s+\d+\.\d+\s+([^\n(]+)\s*\(`log:([^`]+)`\)\s*$", md, flags=re.M):
        label = m.group(1).strip()
        iri_name = m.group(2).strip()
        start = m.end()
        end_match = re.search(r"^###\s+\d+\.\d+\s+", md[start:], flags=re.M)
        end = start + end_match.start() if end_match else len(md)
        block = md[start:end]
        desc = ""
        for line in block.splitlines():
            s = line.strip()
            if not s or s.startswith("**") or s.startswith("```"):
                continue
            desc = s
            break
        classes[iri_name] = {"label": label, "description": desc or f"Logistics concept: {iri_name}"}
    return classes


def parse_semantic(md: str):
    rels = defaultdict(lambda: defaultdict(set))
    for line in md.splitlines():
        m = re.match(r"^\|\s*`log:([^`]+)`\s*\|\s*`beckn:([^`]+)`\s*\|\s*`([^`]+)`\s*\|", line.strip())
        if m:
            rels[m.group(1).strip()][m.group(3).strip()].add(m.group(2).strip())
    return rels


def build_name_map(logistics_names, existing_names):
    collisions = sorted(set(logistics_names) & set(existing_names))
    mapping = {n: (f"Logistics{n}" if n in collisions else n) for n in logistics_names}
    return mapping, collisions


def rewrite_refs(node, name_map, fmt, use_remote):
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k == "$ref" and isinstance(v, str):
                m = re.match(r"^#/components/schemas/([^/]+)$", v)
                if m:
                    t = name_map.get(m.group(1), m.group(1))
                    if use_remote:
                        if fmt == "openapi":
                            out[k] = f"https://schema.beckn.io/{t}/v2.0/attributes.yaml#/components/schemas/{t}"
                        else:
                            out[k] = (
                                f"https://schema.beckn.io/{t}/v2.0/attributes.jsonschema.yaml"
                                f"#/properties/components/properties/schemas/properties/{t}"
                            )
                    else:
                        out[k] = f"#/components/schemas/{t}" if fmt == "openapi" else f"#/$defs/{t}"
                else:
                    out[k] = v
            else:
                out[k] = rewrite_refs(v, name_map, fmt, use_remote)
        return out
    if isinstance(node, list):
        return [rewrite_refs(i, name_map, fmt, use_remote) for i in node]
    return node


def write_yaml(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def jsonschema_doc(schema_name, schema_obj):
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": f"{schema_name} JSON Schema",
        "type": "object",
        "properties": {
            "components": {
                "type": "object",
                "properties": {
                    "schemas": {
                        "type": "object",
                        "properties": {schema_name: {"$ref": f"#/$defs/{schema_name}"}},
                        "additionalProperties": False,
                    }
                },
                "required": ["schemas"],
                "additionalProperties": False,
            }
        },
        "required": ["components"],
        "additionalProperties": False,
        "$defs": {schema_name: schema_obj},
    }


def master_jsonschema(schema_map):
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Logistics JSON Schema",
        "type": "object",
        "properties": {
            "components": {
                "type": "object",
                "properties": {
                    "schemas": {
                        "type": "object",
                        "properties": {k: {"$ref": f"#/$defs/{k}"} for k in sorted(schema_map)},
                        "additionalProperties": False,
                    }
                },
                "required": ["schemas"],
                "additionalProperties": False,
            }
        },
        "required": ["components"],
        "additionalProperties": False,
        "$defs": {k: schema_map[k] for k in sorted(schema_map)},
    }


def main():
    ontology = parse_logistics_ontology(DOC_ONTOLOGY.read_text(encoding="utf-8"))
    semantic = parse_semantic(DOC_SEMANTIC.read_text(encoding="utf-8"))

    canonical_names = sorted(set(ontology.keys()) | set(semantic.keys()))
    source_names = [n for n in canonical_names if (SOURCE_LOGISTICS_SCHEMA_ROOT / n / "v2.0" / "attributes.yaml").exists()]

    mobility_master = TARGET_SCHEMA_ROOT / "Mobility" / "v2.0" / "attributes.yaml"
    if mobility_master.exists():
        mob_doc = yaml.safe_load(mobility_master.read_text(encoding="utf-8"))
        collision_basis = list((mob_doc.get("components", {}) or {}).get("schemas", {}).keys())
    else:
        collision_basis = [p.name for p in TARGET_SCHEMA_ROOT.iterdir() if p.is_dir()]
    name_map, collisions = build_name_map(source_names, collision_basis)

    master_openapi_schemas = {}
    master_json_schemas = {}

    for old in source_names:
        new = name_map[old]
        src_doc = yaml.safe_load((SOURCE_LOGISTICS_SCHEMA_ROOT / old / "v2.0" / "attributes.yaml").read_text(encoding="utf-8"))
        old_schema = src_doc.get("components", {}).get("schemas", {}).get(old, {})

        per_openapi_schema = rewrite_refs(copy.deepcopy(old_schema), name_map, "openapi", True)
        per_json_schema = rewrite_refs(copy.deepcopy(old_schema), name_map, "jsonschema", True)
        if isinstance(per_openapi_schema, dict):
            per_openapi_schema["title"] = new
            per_openapi_schema.setdefault("description", ontology.get(old, {}).get("description", f"Logistics schema for {new}"))
        if isinstance(per_json_schema, dict):
            per_json_schema["title"] = new
            per_json_schema.setdefault("description", ontology.get(old, {}).get("description", f"Logistics schema for {new}"))

        per_openapi_doc = {
            "openapi": "3.1.0",
            "info": {
                "title": new,
                "version": "2.0.0",
                "description": f"Schema definition for the {new} entity in the Beckn Logistics domain.",
                "contact": {"name": "Beckn Foundation", "url": "https://beckn.org"},
                "license": {"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
            },
            "paths": {},
            "components": {"schemas": {new: per_openapi_schema}},
        }

        out_dir = TARGET_SCHEMA_ROOT / new / "v2.0"
        write_yaml(out_dir / "attributes.yaml", per_openapi_doc)
        write_yaml(out_dir / "attributes.jsonschema.yaml", jsonschema_doc(new, per_json_schema))

        readme = (
            f"# {new}\n\n"
            "A schema.beckn.io Type\n\n"
            f"{ontology.get(old, {}).get('description', f'Logistics schema for {new}.')}\n\n"
            f"**Canonical IRI :** `log:{new}`\n\n"
            f"**Canonical URL:** https://schema.beckn.io/logistics/{new}\n\n"
            "## Open Issues\n\n"
            "[Open issues](https://github.com/beckn/logistics/issues)\n"
        )
        (TARGET_SCHEMA_ROOT / new / "README.md").write_text(readme, encoding="utf-8")

        master_openapi = rewrite_refs(copy.deepcopy(old_schema), name_map, "openapi", False)
        master_json = rewrite_refs(copy.deepcopy(old_schema), name_map, "jsonschema", False)
        if isinstance(master_openapi, dict):
            master_openapi["title"] = new
        if isinstance(master_json, dict):
            master_json["title"] = new
        master_openapi_schemas[new] = master_openapi
        master_json_schemas[new] = master_json

    logistics_master_dir = TARGET_SCHEMA_ROOT / "Logistics" / "v2.0"
    master_openapi_doc = {
        "openapi": "3.1.0",
        "info": {
            "title": "Logistics",
            "version": "2.0.0",
            "description": "Master schema package for Beckn Logistics domain.",
            "contact": {"name": "Beckn Foundation", "url": "https://beckn.org"},
            "license": {"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
        },
        "paths": {},
        "components": {"schemas": {k: master_openapi_schemas[k] for k in sorted(master_openapi_schemas)}},
    }
    write_yaml(logistics_master_dir / "attributes.yaml", master_openapi_doc)
    write_yaml(logistics_master_dir / "attributes.jsonschema.yaml", master_jsonschema(master_json_schemas))

    vocab_graph = [{
        "@id": "https://schema.beckn.io/logistics/v2.0/",
        "@type": "owl:Ontology",
        "rdfs:label": {"@language": "en", "@value": "Beckn Logistics Vocabulary"},
        "rdfs:comment": {"@language": "en", "@value": "Unified ontology graph for Beckn Logistics v2.0."},
        "owl:versionInfo": "2.0.0",
    }]

    for old in sorted(source_names):
        new = name_map[old]
        node = {
            "@id": f"log:{new}",
            "@type": "owl:Class",
            "rdfs:label": {"@language": "en", "@value": new},
            "rdfs:comment": {"@language": "en", "@value": ontology.get(old, {}).get("description", f"Logistics concept: {new}")},
        }
        for pred, objs in sorted(semantic.get(old, {}).items()):
            ids = [{"@id": f"beckn:{o}"} for o in sorted(objs)]
            node[pred] = ids[0] if len(ids) == 1 else ids
        vocab_graph.append(node)

    vocab = {
        "@context": {
            "log": "https://schema.beckn.io/logistics/v2.0/",
            "beckn": "https://schema.beckn.io/core/v2.0/",
            "owl": "http://www.w3.org/2002/07/owl#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "skos": "http://www.w3.org/2004/02/skos/core#",
        },
        "@graph": vocab_graph,
    }
    (logistics_master_dir / "vocab.jsonld").write_text(json.dumps(vocab, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    ctx = {"beckn": "https://schema.beckn.io/core/v2.0/", "@vocab": "https://schema.beckn.io/core/v2.0/"}
    for old in sorted(source_names):
        new = name_map[old]
        mapped = None
        for pred in ["owl:equivalentClass", "skos:exactMatch", "rdfs:subClassOf", "skos:closeMatch", "skos:broadMatch"]:
            vals = semantic.get(old, {}).get(pred)
            if vals:
                mapped = sorted(vals)[0]
                break
        ctx[new] = f"beckn:{mapped or old}"
    (logistics_master_dir / "context.jsonld").write_text(json.dumps({"@context": ctx}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    (TARGET_SCHEMA_ROOT / "Logistics" / "README.md").write_text(
        "# Logistics\n\n"
        "A schema.beckn.io Type\n\n"
        "Master schema package for Beckn Logistics v2.0 containing consolidated OpenAPI attributes, JSON Schema attributes, vocabulary graph, and context mappings.\n\n"
        "**Canonical IRI :** `log:Logistics`\n\n"
        "**Canonical URL:** https://schema.beckn.io/logistics/Logistics\n\n"
        "## Open Issues\n\n"
        "[Open issues](https://github.com/beckn/logistics/issues)\n",
        encoding="utf-8",
    )

    print(f"Generated logistics schemas in {TARGET_SCHEMA_ROOT}")
    print(f"Source logistics schemas: {len(source_names)}")
    print(f"Prefixed collisions: {', '.join(collisions) if collisions else 'None'}")


if __name__ == "__main__":
    main()
