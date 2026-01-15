# triage

**Scope:** Triage rules for documentation lifecycle.
**Audience:** Contributors deciding doc changes.
**Guarantees:** Defines when docs exist, merge, or delete.
**Non-Goals:** Content authoring guidance.

## Overview
Why: Keep the docs set minimal and intentional.

## Contracts
- A doc exists only when it maps to a code surface.
- A doc is deleted when it cannot state a concrete guarantee.
- A doc is merged when two docs cover the same responsibility.

## Invariants
- Triage rules apply before adding new docs.

## Failure Modes
- Violations fail docs lint or are removed.

## Extension Points
- Update this file before adding new doc classes.

## Exit Criteria
- Obsolete when docs are auto-generated from code.
- Replacement: automated doc generator policy.

Code refs: src/agentic_proteins/__init__.py, tests/unit/test_docs_contract.py.
