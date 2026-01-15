# invariants

**Scope:** Architectural invariants.
**Audience:** Contributors.
**Guarantees:** Invariants map to tests.
**Non-Goals:** Rationale narrative.

## Overview
Why: Provide the invariant set that gates changes.

## Contracts
- Determinism: identical inputs and seeds yield identical outputs.
- State transitions: lifecycle states change only via allowed transitions.
- Artifact immutability: artifacts are content-addressed.
- Provider boundary: runs invoke only selected providers.
- Failure containment: failures emit error artifacts without partial tool outputs.

## Invariants
- Invariant tests pass in CI.

## Failure Modes
- Violations fail tests.

## Extension Points
- Add invariants with matching tests.

## Exit Criteria
- Obsolete when invariants move to code metadata.
- Replacement: invariants registry.

Code refs: tests/regression/test_architecture_invariants.py, src/agentic_proteins/runtime/control/state_machine.py.
