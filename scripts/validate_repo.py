#!/usr/bin/env python3
"""
validate_repo.py

Validation script for the IIP‑Scoring™ restricted public specification surface.

Checks:
- JSON syntax for key artifacts
- Cross-file version consistency
- JSON Schema validity (Draft 2020-12)
- Example artifacts validate against schemas (structure-only)
- Release snapshot SHA256SUMS matches computed hashes

This script does NOT implement scoring, calibration, or operational heuristics.
"""

from __future__ import annotations

import json
import hashlib
import sys
from pathlib import Path
from typing import Dict, Any

from jsonschema import Draft202012Validator, FormatChecker

# `referencing` is a dependency of jsonschema (v4+)
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[1]
FORMAT_CHECKER = FormatChecker()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> Any:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON: {path} ({e})") from e


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def load_schemas() -> Dict[str, Dict[str, Any]]:
    schema_paths = [
        ROOT / "schemas" / "iip-report.schema.json",
        ROOT / "schemas" / "qbank.schema.json",
        ROOT / "schemas" / "corpus-snapshot.manifest.schema.json",
    ]
    schemas: Dict[str, Dict[str, Any]] = {}
    for p in schema_paths:
        s = read_json(p)
        sid = s.get("$id")
        if not isinstance(sid, str) or not sid:
            fail(f"Schema missing $id: {p}")
        schemas[sid] = s
        ok(f"Loaded schema: {p} ($id={sid})")
    return schemas


def build_registry(schema_store: Dict[str, Dict[str, Any]]) -> Registry:
    registry = Registry()
    for uri, schema in schema_store.items():
        registry = registry.with_resource(uri, Resource.from_contents(schema))
    return registry


def validate_examples(schema_store: Dict[str, Dict[str, Any]]) -> None:
    registry = build_registry(schema_store)

    # Validate QBank
    qbank_schema_id = next(k for k in schema_store.keys() if k.endswith("/qbank.schema.json"))
    qbank_schema = schema_store[qbank_schema_id]
    qbank_example = read_json(ROOT / "examples" / "qbank.example.json")

    Draft202012Validator(qbank_schema, format_checker=FORMAT_CHECKER, registry=registry).validate(qbank_example)
    ok("Validated examples/qbank.example.json against qbank schema")

    # Validate corpus snapshot
    snap_schema_id = next(k for k in schema_store.keys() if k.endswith("/corpus-snapshot.manifest.schema.json"))
    snap_schema = schema_store[snap_schema_id]
    snap_example = read_json(ROOT / "examples" / "corpus-snapshot.manifest.example.json")

    Draft202012Validator(snap_schema, format_checker=FORMAT_CHECKER, registry=registry).validate(snap_example)
    ok("Validated examples/corpus-snapshot.manifest.example.json against snapshot schema")

    # Validate report (resolves $ref via registry, no network)
    report_schema_id = next(k for k in schema_store.keys() if k.endswith("/iip-report.schema.json"))
    report_schema = schema_store[report_schema_id]
    report_example = read_json(ROOT / "examples" / "iip-report.example.json")

    Draft202012Validator(report_schema, format_checker=FORMAT_CHECKER, registry=registry).validate(report_example)
    ok("Validated examples/iip-report.example.json against report schema")


def validate_versions() -> str:
    version = read_text(ROOT / "VERSION").strip()
    if not version:
        fail("VERSION file is empty")
    ok(f"Read VERSION={version}")

    repo_meta = read_json(ROOT / "repo-metadata.json")
    if repo_meta.get("version") != version:
        fail(f"repo-metadata.json version mismatch: {repo_meta.get('version')} != {version}")
    ok("repo-metadata.json version matches")

    manifest = read_json(ROOT / "manifest" / "iip-scoring.standard.manifest.json")
    if manifest.get("version") != version:
        fail(f"manifest/iip-scoring.standard.manifest.json version mismatch: {manifest.get('version')} != {version}")
    ok("Standard manifest version matches")

    vdir = ROOT / "versions" / version
    if not vdir.exists():
        fail(f"Missing versions snapshot directory: {vdir}")
    ok(f"Found versions snapshot directory: {vdir}")

    vmeta = read_json(vdir / "VERSION.json")
    if vmeta.get("version") != version:
        fail(f"versions/{version}/VERSION.json mismatch: {vmeta.get('version')} != {version}")
    ok("versions/<version>/VERSION.json version matches")

    return version


def verify_sha256sums(version: str) -> None:
    sums_path = ROOT / "versions" / version / "SHA256SUMS.txt"
    if not sums_path.exists():
        fail(f"Missing SHA256SUMS.txt: {sums_path}")

    lines = [ln.strip() for ln in read_text(sums_path).splitlines() if ln.strip()]
    if not lines:
        fail(f"Empty SHA256SUMS.txt: {sums_path}")

    for ln in lines:
        # Format: <hash><two spaces><path>
        try:
            expected, relpath = ln.split("  ", 1)
        except ValueError:
            fail(f"Malformed SHA256SUMS line: {ln}")

        if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
            fail(f"Invalid sha256 in SHA256SUMS line: {ln}")

        target = ROOT / relpath
        if not target.exists():
            fail(f"SHA256SUMS references missing file: {relpath}")

        actual = sha256_file(target)
        if actual != expected:
            fail(f"SHA256 mismatch for {relpath}: expected {expected}, got {actual}")

    ok(f"Verified SHA256SUMS for {len(lines)} files")


def main() -> None:
    version = validate_versions()
    schemas = load_schemas()
    validate_examples(schemas)
    verify_sha256sums(version)
    ok("All checks passed")


if __name__ == "__main__":
    main()
