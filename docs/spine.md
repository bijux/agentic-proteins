# spine

**Scope:** Single navigation spine for docs/.
**Audience:** Readers consuming docs top-down.
**Guarantees:** Lists all docs and their order.
**Non-Goals:** Per-topic READMEs.

## Overview
Why: Provide one entry point and reading order.

## Contracts
- Read order: index, style, triage, architecture, cli, api, policy.

## Invariants
- No nested README sprawl.

## Failure Modes
- Missing docs break the spine.

## Extension Points
- Add new docs here and in mkdocs.yml.

## Exit Criteria
- Obsolete when docs nav is generated from code.
- Replacement: generated nav manifest.

Docs list:
- docs/index.md
- docs/style.md
- docs/triage.md
- docs/architecture/invariants.md
- docs/architecture/experimental.md
- docs/architecture/design_debt.md
- docs/cli/cli.md
- docs/interface/cli_surface.md
- docs/api/overview.md
- docs/api/schema.md
- docs/security/dependencies.md
- docs/security/threat_model.md

Code refs: src/agentic_proteins/__init__.py, scripts/check_docs_consistency.py.
