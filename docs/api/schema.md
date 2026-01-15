# schema

**Scope:** OpenAPI schema contract.
**Audience:** API users and contributors.
**Guarantees:** api/v1/schema.yaml is authoritative.
**Non-Goals:** Client SDK generation.

## Overview
Why: Point to the schema source of truth.

## Contracts
- Schema lives at api/v1/schema.yaml.

## Invariants
- Breaking changes require version bump.

## Failure Modes
- Schema drift fails CI.

## Extension Points
- Add schemas with tests.

## Exit Criteria
- Obsolete when schema is generated.
- Replacement: generated schema docs.

Code refs: src/agentic_proteins/api/app.py, scripts/check_openapi_drift.py.
