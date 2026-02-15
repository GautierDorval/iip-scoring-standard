# Metrics registry (conceptual)

This registry defines metric names and their intended meaning, without publishing formulas, weights, or calibrated thresholds.

## Coverage

A coverage indicator for how much of the QBank yields qualifiable outputs under the protocol’s verdict taxonomy.

## MVS™ (anchored voice share)

A signal describing the share of outputs that remain grounded in the declared corpus snapshot.

## IR™ (inference rate)

A signal describing the share of outputs that extend beyond admissible evidence within the snapshot-bounded regime.

## IDI™ (interpretive distortion index)

A signal describing the presence of contradictory or false claims relative to the snapshot-bounded truth base.

## NSS™ (narrative stability signal)

A signal describing output stability across controlled runs and/or across systems (depending on the configured audit mode).

## IIS™ (interpretive integrity score)

A composite indicator intended for communication, not for validation. It must never override gates or critical segment constraints.

## Important constraint

This public repository does not publish:
- formulas,
- weights,
- calibrated thresholds,
- sector-specific calibrations,
- benchmark distributions.

Those elements are private and exist only within licensed operational deployments.
