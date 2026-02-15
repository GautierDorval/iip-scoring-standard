# QBank Construction Protocol (QBCP) — outline

This document describes a **non-operational** outline for QBank construction and governance.

It defines requirements for structure, traceability, and bias control without publishing implementation recipes, quotas, or sector calibrations.

## Objectives

- Ensure QBank is an audit instrument, not a marketing questionnaire.
- Preserve comparability across runs, models, and time points.
- Prevent “easy QBank” bias and under-coverage of critical segments.
- Provide versioned, opposable QBank artifacts.

## Minimum requirements (conceptual)

A QBank should:
- define stable question identifiers,
- include question typing (e.g., factual / interpretive / boundary),
- include segmentation and critical segment markers,
- include evidence targets (where applicable),
- provide a changelog and integrity signals,
- support a stable core subset for temporal analysis.

## Governance outline

- Define segments and critical segments in a stable taxonomy.
- Map segments to canonical evidence surfaces (snapshot-aware).
- Produce candidate pools per segment and normalize for atomicity.
- Run pilot checks to detect ambiguity and structural bias.
- Freeze and version the QBank and record integrity signals.

## Temporal core (concept)

A QBank may define:
- **QCore** (stable subset) for temporal comparability, and
- **QRot** (rotating subset) for evolving risk probes.

This repository does not publish operational requirements (counts, ratios, or schedules).
