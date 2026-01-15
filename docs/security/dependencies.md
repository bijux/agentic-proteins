# dependencies

**Scope:** Runtime dependency allowlist.
**Audience:** Contributors and reviewers.
**Guarantees:** Only listed dependencies are allowed in pyproject.toml.
**Non-Goals:** Dev dependency tracking.

## Overview
Why: Make dependency changes explicit.

## Contracts
- Allowlist entries cover project.dependencies.

## Invariants
- New deps require allowlist updates.

## Failure Modes
- Missing entries fail CI.

## Extension Points
- Add entries with justification.

## Exit Criteria
- Obsolete when dependency policy is automated.
- Replacement: automated dependency policy.

Allowlist:
- requests
- biopython
- numpy
- click
- fastapi
- uvicorn
- pydantic
- loguru
- slowapi
- boto3

Code refs: src/agentic_proteins/runtime/context/context.py, scripts/check_dependency_allowlist.py.
