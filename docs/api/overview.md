# overview

**Scope:** HTTP API summary.
**Audience:** API users.
**Guarantees:** API mirrors CLI capabilities.
**Non-Goals:** Authentication.

## Overview
Why: Define the API surface at a glance.

## Contracts
- Endpoints map to CLI commands.

## Invariants
- API returns structured envelopes.

## Failure Modes
- Invalid inputs return error envelopes.

## Extension Points
- Add endpoints with schema updates.

## Exit Criteria
- Obsolete when API is removed.
- Replacement: none.

Code refs: src/agentic_proteins/api/app.py, src/agentic_proteins/api/v1/router.py.
