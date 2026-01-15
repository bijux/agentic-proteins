# cli

**Scope:** CLI command contract.
**Audience:** Users and contributors.
**Guarantees:** CLI commands listed here are stable.
**Non-Goals:** Usage examples.

## Overview
Why: Define the CLI contract in one place.

## Contracts
- Commands: run, resume, compare, inspect-candidate, export-report, reproduce, api serve.

## Invariants
- JSON output schema is stable.

## Failure Modes
- Invalid inputs return error envelopes.

## Extension Points
- Add commands with tests and docs updates.

## Exit Criteria
- Obsolete when CLI is removed.
- Replacement: CLI API reference generator.

Code refs: src/agentic_proteins/interfaces/cli.py, tests/unit/test_cli_surface_documentation.py.
