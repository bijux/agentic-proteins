# Agentic Proteins

<a id="top"></a>

**Deterministic, artifact-first protein design runtime and CLI.**

[![PyPI](https://img.shields.io/pypi/v/agentic-proteins.svg)](https://pypi.org/project/agentic-proteins/)
[![Python](https://img.shields.io/pypi/pyversions/agentic-proteins?logo=python&logoColor=white)](https://pypi.org/project/agentic-proteins/)
[![License](https://img.shields.io/pypi/l/agentic-proteins.svg)](https://github.com/bijux/agentic-proteins/blob/main/LICENSE)
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue.svg)](https://bijux.github.io/agentic-proteins/)
[![HTTP API](https://img.shields.io/badge/http%20api-available-brightgreen.svg)](https://bijux.github.io/agentic-proteins/api/overview/)
[![CI](https://github.com/bijux/agentic-proteins/actions/workflows/ci.yml/badge.svg)](https://github.com/bijux/agentic-proteins/actions/workflows/ci.yml)

## What It Is

Agentic Proteins is a deterministic, artifact-first protein design runtime and CLI.

## Guarantees

- Deterministic runs for identical inputs and seeds.
- Stable artifact layout under `artifacts/<run_id>/`.
- Stable CLI JSON output schema.

## Run It

```bash
pipx install agentic-proteins
agentic-proteins run --sequence "ACDEFGHIKLMNPQRSTVWY"
agentic-proteins inspect-candidate <candidate_id>
```

## Docs

- Docs spine: https://bijux.github.io/agentic-proteins/spine/
- CLI: https://bijux.github.io/agentic-proteins/cli/cli/
- API: https://bijux.github.io/agentic-proteins/api/overview/
- Architecture: https://bijux.github.io/agentic-proteins/architecture/invariants/
- Security: https://bijux.github.io/agentic-proteins/security/dependencies/
© 2025 Bijan Mousavi.

[Back to top](#top)
