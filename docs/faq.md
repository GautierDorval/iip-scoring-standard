# FAQ

## Is this an open-source project?

No. This repository is proprietary and restricted. It is a specification surface, not an implementation.

## Can I implement IIP‑Scoring™ from this repository?

No. Implementation details, operational heuristics, calibration, and thresholds are intentionally omitted.

## Why publish schemas if the implementation is private?

Schemas define **interfaces** for interchange and audit record structure. They do not encode algorithms or calibration. Publishing interfaces supports interoperability without disclosing operational recipes.

## What am I allowed to do with this repository?

This repository is published publicly as a **reference surface**. Permitted uses and restrictions are defined in `LICENSE.md`.

In general:
- reading, citing, and internal evaluation are allowed,
- schema-based validation for interoperability is allowed,
- implementing or offering a scoring service based on omitted mechanics is not authorized.

## Are the examples operational?

No. Files under `examples/` are **structure-only** illustrations intended to demonstrate interface shape. Values are not calibrated outputs, thresholds, or operational settings.

## Do you provide audits?

Yes, under licensed engagements.

## Does a high score imply compliance?

No. IIP‑Scoring™ is an evidence layer. Compliance requires a broader program and legal interpretation.

## Where is the canonical doctrine?

The canonical identity and doctrine anchors are published on the canonical site listed in `canonical-urls.md`.
