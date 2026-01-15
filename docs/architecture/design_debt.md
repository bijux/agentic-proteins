# design_debt

**Scope:** Design debt ledger.
**Audience:** Contributors.
**Guarantees:** Ledger contains <=10 items with exit conditions.
**Non-Goals:** Issue tracking.

## Overview
Why: Record deliberate debt with explicit exits.

## Contracts
- Artifact hashes are not yet signed; why: signature workflow not defined; exit: signed hash format and verification shipped.

## Invariants
- Each item includes why and exit.

## Failure Modes
- More than 10 items fails CI.

## Extension Points
- Add items only with exit conditions.

## Exit Criteria
- Obsolete when debt tracking moves to code metadata.
- Replacement: debt registry.

Code refs: scripts/check_design_debt.py, src/agentic_proteins/runtime/control/artifacts.py.
