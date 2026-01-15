# cli_surface

**Scope:** CLI surface list.
**Audience:** Contributors and reviewers.
**Guarantees:** Documents the full CLI surface used in tests.
**Non-Goals:** Usage examples.

## Overview
Why: Provide a single source for CLI surface auditing.

## Contracts
Public commands:
- api
- run
- resume
- compare
- inspect-candidate
- export-report
- reproduce
- api serve
Stable flags:
- --sequence
- --fasta
- --rounds
- --provider
- --artifacts-dir
- --dry-run
- --no-logs
- --pretty
- --json
- --execution-mode
- --output
- --host
- --port
- --no-docs
Experimental flags:
- --reload

## Invariants
- CLI surface matches the click definitions.

## Failure Modes
- Missing documentation fails tests.

## Extension Points
- Update this list when new flags land.

## Exit Criteria
- Obsolete when CLI surface is generated.
- Replacement: CLI surface generator.

Code refs: src/agentic_proteins/interfaces/cli.py, tests/unit/test_cli_surface_documentation.py.
