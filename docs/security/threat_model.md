# threat_model

**Scope:** Threat model skeleton.
**Audience:** Contributors.
**Guarantees:** Captures abuse cases, resource risks, and trust assumptions.
**Non-Goals:** Mitigations.

## Overview
Why: Track threat model placeholders in one file.

## Contracts
Abuse cases:
- Path traversal via candidate IDs to read/write outside the candidate store.
- Crafted sequence inputs to bypass validation and inject unsupported characters.
- Unauthorized resume requests to force execution of stale or unapproved runs.
Resource exhaustion risks:
- Large batch runs exhausting local disk through artifact growth.
- Oversized sequences driving unbounded memory usage in planning and tooling.
- High-frequency API requests saturating CPU and log I/O.
Trust assumptions:
- Local filesystem permissions prevent cross-tenant artifact access.
- Provider backends return deterministic results for the same inputs and seed.
- CI artifacts and version metadata are not tampered with between steps.

## Invariants
- This skeleton remains unmitigated by design.

## Failure Modes
- Missing sections block security reviews.

## Extension Points
- Add mitigations in SECURITY.md only.

## Exit Criteria
- Obsolete when a full threat model replaces this skeleton.
- Replacement: full threat model doc.

Code refs: tests/unit/test_abuse_case_path_traversal.py, src/agentic_proteins/domain/candidates/store.py.
