# IIP‑Scoring™ Standard (Restricted Specification)

**Repository status:** restricted-public-spec  
**Version:** 0.1.0  
**Language:** English (primary)

This repository contains a **restricted, non-operational normative specification** for **IIP‑Scoring™** (Interpretive Integrity Protocol).

It exists to:
- fix terminology and scope,
- declare canonical references and interfaces,
- provide machine-readable schemas for interchange,
- establish a stable, timestampable reference surface.

It is intentionally **not implementable** as-is.

## What this repository is

- A **normative vocabulary** for interpretive integrity audits
- An **interface reference** (schemas for reports, QBank structure, corpus snapshot manifests)
- A **canonical pointer surface** to authoritative doctrine and definitions
- A **versioned reference** suitable for citation and internal governance

## What this repository is not

- Not an implementation
- Not a scoring calculator
- Not a test suite
- Not a dataset
- Not a “how‑to” guide
- Not a compliance guarantee
- Not an SEO/GEO “visibility” framework

## Deliberate omissions (by design)

To protect the integrity of the protocol and prevent diluted implementations, this repository **does not publish**:
- calibrated thresholds,
- scoring weights,
- sector-specific risk matrices,
- operational heuristics,
- executable tooling,
- complete QBank sets,
- report templates used in client delivery.

Those elements exist, but are **licensable under contract** only.

## Canonical references

- Canonical identity: https://gautierdorval.com/
- GitHub repository (recommended): https://github.com/GautierDorval/iip-scoring-standard
- Canonical doctrinal page: https://gautierdorval.com/iip-scoring-cadre-doctrinal/

## Parent doctrine (normative)

IIP-Scoring™ is a measurement layer conceptually derived from the broader **Interpretive Governance**
doctrinal architecture.

Normative reference:
- https://github.com/GautierDorval/interpretive-governance-manifest

## Directory overview

- `manifest/` — declarative manifest + concept registry
- `schemas/` — JSON Schemas (interfaces, not algorithms)
- `docs/` — restricted specification documents (normative, non-operational)
- `versions/` — release snapshots (hashes, version metadata)

## License

This repository is **proprietary**. See `LICENSE.md`.

## Contact / Licensing

For licensed audits, deployments, or private implementation access:
- https://gautierdorval.com/
