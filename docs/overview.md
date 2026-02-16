# Overview (restricted public specification)

This repository exposes the **public interface** of **IIP‑Scoring™** (Interpretive Integrity Protocol) as a restricted specification:
- terminology and scope,
- interface schemas (JSON Schema),
- versioning and opposability discipline,
- canonical pointers.

It is intentionally **non-operational**: formulas, weights, calibrated thresholds, and operational heuristics are omitted by design.

## What IIP‑Scoring™ measures (conceptually)

IIP‑Scoring™ evaluates **interpretive integrity under uncertainty** by comparing model outputs to a **declared corpus snapshot** and its canonical surfaces.

A claim may be “true in reality” but still be treated as **ungrounded** if it cannot be anchored to the declared snapshot within the regime of the audit.

## What you get (in a licensed engagement)

Exact deliverables vary by engagement, but typically include:
- an **IIP report** (structured; schema-aligned),
- a **corpus snapshot manifest** (declared truth base),
- a **QBank** (question bank) and segment structure,
- integrity signals (hashes) enabling reconstruction and contestation,
- an evidence archive and traceability notes (where applicable).

This repository publishes the **interfaces** for those artifacts, not the operational scoring mechanics.

## What this repository publishes

- `schemas/`  
  JSON Schemas for:
  - IIP reports
  - QBank structure
  - corpus snapshot manifest structure

- `manifest/`  
  A concept registry and a JSON-LD term set to enable machine-readable alignment across tools and documents.

- `docs/`  
  Non-operational, normative documentation: scope boundaries, validation scale outline, opposability discipline.

## What this repository omits (by design)

This repository does not publish:
- scoring recipes or calculators,
- calibrated thresholds,
- scoring weights,
- sector-specific profiles,
- complete QBank sets used in client delivery,
- client delivery templates.

## How to use this repo as a prospect (without access to the private implementation)

You can still evaluate fit by:
1. Reading the scope boundaries (`docs/scope.md`, `docs/non-goals.md`).
2. Reviewing the report exchange interface (`schemas/iip-report.schema.json`).
3. Inspecting the examples under `examples/` (structure only).
4. Using the schemas to validate your own candidate artifacts (format validation only).

If you need an operational audit or deployment, that is available only under license.
