#!/usr/bin/env python3
"""
Generate mobility/schema/vocab.jsonld from mobility/docs/4_Beckn_Mobility_Concepts.md
"""
import json
import re

# Read the markdown file
with open('/home/ravi/www/spec_work/mobility/docs/4_Beckn_Mobility_Concepts.md', 'r') as f:
    content = f.read()

# Extract table rows (rows that start with | and have a number in the first column)
rows = []
lines = content.split('\n')
in_table = False
for line in lines:
    if '| # |' in line and 'Concept' in line:
        in_table = True
        continue
    if in_table and re.match(r'^\|[-:]+', line):
        continue  # skip separator row
    if in_table and re.match(r'^\|\s*\d+\s*\|', line):
        # Split the row into cells
        parts = [p.strip() for p in line.split('|')]
        parts = [p for p in parts if p != '']  # remove empty edge items
        if len(parts) >= 5:
            rows.append(parts)

print(f"Parsed {len(rows)} concept rows from markdown table")


def strip_backticks(s):
    return s.strip('`').strip()


def parse_equivalences(eq_str):
    """
    Parse equivalence string like:
      `owl:equivalentClass transmodel:Operator` ; `rdfs:subClassOf schema:Organization`
    Returns dict: { "predicate": [list of object strings] }
    """
    eq_str = eq_str.strip()
    if eq_str == '—' or not eq_str or eq_str == '-':
        return {}

    result = {}
    # Split by ' ; ' (with spaces around semicolon)
    parts = re.split(r'\s*;\s*', eq_str)
    for part in parts:
        part = strip_backticks(part).strip()
        if not part or part == '—' or part == '-':
            continue
        # Split on first whitespace to get predicate and object
        tokens = part.split(None, 1)
        if len(tokens) == 2:
            pred = tokens[0].strip()
            obj = tokens[1].strip()
            if pred not in result:
                result[pred] = []
            result[pred].append(obj)
    return result


# Build the @graph array
graph = []

# Add ontology-level metadata node
graph.append({
    "@id": "https://schema.beckn.io/mobility/",
    "@type": "owl:Ontology",
    "rdfs:label": {
        "@language": "en",
        "@value": "Beckn Mobility Vocabulary"
    },
    "rdfs:comment": {
        "@language": "en",
        "@value": (
            "A vocabulary of unique mobility domain concepts derived from major global standards "
            "(GTFS, GBFS, MDS, SIRI, NeTEx, Transmodel, IATA NDC, IATA ONE Order, BOB, OSDM, "
            "TAP TSI, OCPI, OCPP, SAE J2735, C-ITS, TOMP-API, OpenMaaS, IXSI, OTP, APDS, ERA, "
            "LDES, CityGML, GeoSPARQL, INSPIRE, and more), consolidated into a single ontology "
            "vocabulary for the Beckn mobility domain."
        )
    },
    "owl:versionInfo": "0.1.0"
})

# Process each concept row
for row in rows:
    num = row[0]
    label = row[1].strip()
    description = row[2].strip()
    equivalences_str = row[3].strip()
    beckn_iri_raw = row[4].strip()

    # Clean beckn IRI (remove backticks)
    beckn_id = strip_backticks(beckn_iri_raw)

    # Build the class entry
    entry = {
        "@id": beckn_id,
        "@type": "owl:Class",
        "rdfs:label": {
            "@language": "en",
            "@value": label
        },
        "rdfs:comment": {
            "@language": "en",
            "@value": description
        }
    }

    # Parse and add semantic equivalences
    eq = parse_equivalences(equivalences_str)
    for pred, objects in eq.items():
        obj_nodes = [{"@id": obj} for obj in objects]
        if len(obj_nodes) == 1:
            entry[pred] = obj_nodes[0]
        else:
            entry[pred] = obj_nodes

    graph.append(entry)

# Assemble the complete JSON-LD document
vocab = {
    "@context": {
        "mobility": "https://schema.beckn.io/mobility/",
        "schema": "https://schema.org/",
        "geo": "http://www.opengis.net/ont/geosparql#",
        "transmodel": "https://w3id.org/transmodel/ontology#",
        "ldes": "https://w3id.org/ldes/",
        "oslo": "https://data.vlaanderen.be/ns/mobiliteit#",
        "inspire": "https://inspire.ec.europa.eu/ontology/",
        "era": "https://data.europa.eu/949/",
        "owl": "http://www.w3.org/2002/07/owl#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@graph": graph
}

# Write to file
output_path = '/home/ravi/www/spec_work/mobility/schema/vocab.jsonld'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(vocab, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {output_path}")
print(f"  Ontology node + {len(rows)} concept classes = {len(graph)} total graph nodes")
