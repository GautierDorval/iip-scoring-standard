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

This repository may include release snapshots under `versions/` with hash lists for reference artifacts.

## Note

No operational hashing procedures or tooling are provided here.
