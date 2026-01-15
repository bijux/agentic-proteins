# style

**Scope:** Documentation style contract for docs/.
**Audience:** Contributors editing docs.
**Guarantees:** Each doc follows the mandatory section order and front-matter block.
**Non-Goals:** Narrative guidance, marketing, or philosophy.

## Overview
Why: Define the single doc contract that all docs obey.

## Contracts
- Order: Overview, Contracts, Invariants, Failure Modes, Extension Points, Exit Criteria.
- Allowed sections: Overview, Contracts, Invariants, Failure Modes, Extension Points, Exit Criteria.
- Max depth: H2 only.

## Invariants
- No forward-looking words.
- One doc, one responsibility.
- First screen states why the doc exists.

## Failure Modes
- Violations fail the docs lint gate.

## Extension Points
- Changes require updates to the docs linter.

## Exit Criteria
- Obsolete when docs lint is removed.
- Replacement: scripts/check_docs_consistency.py.

Code refs: scripts/check_docs_consistency.py, tests/unit/test_docs_contract.py.
