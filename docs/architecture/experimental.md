# experimental

**Scope:** Experimental provider rules.
**Audience:** Contributors and opt-in users.
**Guarantees:** Experimental providers are namespaced under api_.
**Non-Goals:** Provider-specific behavior.

## Overview
Why: Define the experimental contract in one place.

## Contracts
- Experimental means opt-in and unvalidated.
- Experimental guarantees exclude stability, compatibility, and determinism.
- Experimental behavior can break without notice.

## Invariants
- Experimental providers are namespaced and tagged.

## Failure Modes
- Violations fail tests.

## Extension Points
- Add providers with namespace tests.

## Exit Criteria
- Obsolete when experimental providers are removed.
- Replacement: stable provider policy.

Code refs: src/agentic_proteins/providers/experimental/__init__.py, tests/unit/test_experimental_provider_namespace.py.
