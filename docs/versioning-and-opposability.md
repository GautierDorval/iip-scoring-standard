# Versioning and opposability (restricted)

IIP‑Scoring™ is designed for opposable audits. Opposability requires that evidence and conditions be reconstructible and verifiable.

## Evidence chain (conceptual)

A run should be supported by a minimal evidence chain:
- corpus snapshot manifest (versioned)
- QBank (versioned)
- run configuration (documented parameters)
- raw outputs (archived)
- annotation logs (archived)
- integrity signals (hashes)

## Integrity signals

Integrity signals are intended to:
- detect drift,
- support audit reconstruction,
- prevent silent rewriting of evidence surfaces.

This repository includes release snapshots under `versions/` with hash lists for reference artifacts.

## Repository integrity (non-operational)

This repository may include:
- SHA-256 sum lists in `versions/<version>/SHA256SUMS.txt`,
- minimal CI checks to validate JSON syntax and verify the published hash lists.

These checks support **reference integrity** of this public specification surface.
They do not publish scoring recipes, weights, or calibrated thresholds.

## Note

No operational hashing procedures, scoring formulas, or end-to-end audit tooling are provided here.
