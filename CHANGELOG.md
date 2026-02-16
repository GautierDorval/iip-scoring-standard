# Changelog

## 0.1.2 — 2026-02-16

- Hotfix release to avoid retagging the existing `v0.1.1` Git tag.
- Updated pinned schema `$id` values and canonical URLs to reference `v0.1.2`.
- Added `versions/0.1.2/` snapshot metadata and SHA256SUMS for opposability.
- No changes to public interface semantics (schemas and structures).

## 0.1.1 — 2026-02-16

- Clarified licensing terms for a public, reference-only specification surface (schemas remain usable for interoperability; scoring implementation remains private).
- Added non-operational examples (`examples/`) for report, QBank, and corpus snapshot manifests (structure only; no recipes).
- Added a minimal JSON-LD term set for machine-readable concept alignment (`manifest/iip-scoring.terms.jsonld`).
- Added minimal CI to validate JSON syntax, schema integrity, example validity, and release snapshot hashes.
- Expanded canonical URL registry and added a 1-page overview for prospects (`docs/overview.md`).

## 0.1.0 — 2026-02-15

- Initial restricted public specification release.
- Added interface schemas for report exchange and QBank structure.
- Added non-operational documentation for scope, non-goals, and validation scale outline.
