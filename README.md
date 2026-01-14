# Agentic Proteins

<a id="top"></a>

**Deterministic, artifact-first protein design runtime and CLI** for traceable runs, human review, and reproducible decision trails.

[![PyPI](https://img.shields.io/pypi/v/agentic-proteins.svg)](https://pypi.org/project/agentic-proteins/)
[![Python](https://img.shields.io/pypi/pyversions/agentic-proteins?logo=python&logoColor=white)](https://pypi.org/project/agentic-proteins/)
[![License](https://img.shields.io/pypi/l/agentic-proteins.svg)](https://github.com/bijux/agentic-proteins/blob/main/LICENSE)
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue.svg)](https://bijux.github.io/agentic-proteins/)
[![CI](https://github.com/bijux/agentic-proteins/actions/workflows/ci.yml/badge.svg)](https://github.com/bijux/agentic-proteins/actions/workflows/ci.yml)

> **At a glance:** Deterministic runs • artifact-first output • human-in-the-loop gating • stable JSON contracts  
> **Audience:** Computational biology teams and lab workflows that require auditability and reproducibility.

---

## Table of Contents

* [Why Agentic Proteins?](#why-agentic-proteins)
* [Try It in 30 Seconds](#try-it-in-30-seconds)
* [Installation](#installation)
* [Quick Start](#quick-start)
* [What This Does](#what-this-does)
* [What This Does Not Do](#what-this-does-not-do)
* [Stable Public Surface](#stable-public-surface)
* [Docs & Resources](#docs--resources)
* [Contributing](#contributing)
* [License](#license)

[Back to top](#top)

---

<a id="why-agentic-proteins"></a>

## Why Agentic Proteins?

Protein design workflows need traceable decisions, stable artifacts, and reproducible execution paths. Agentic Proteins provides a deterministic loop that separates planning, execution, evaluation, and human decision points so that labs can audit and reproduce runs without digging into internal code.
The public entry points live in `agentic_proteins.runtime` and `agentic_proteins.interfaces.cli`.

[Back to top](#top)

---

<a id="try-it-in-30-seconds"></a>

## Try It in 30 Seconds

```bash
pipx install agentic-proteins  # Or: pip install agentic-proteins
agentic-proteins run --sequence "ACDEFGHIKLMNPQRSTVWY"
agentic-proteins inspect-candidate --latest
```

[Back to top](#top)

---

<a id="installation"></a>

## Installation

Requires **Python 3.11+**.

```bash

# Isolated install (recommended)

pipx install agentic-proteins

# Standard

pip install agentic-proteins
```

[Back to top](#top)

---

<a id="quick-start"></a>

## Quick Start

```bash

# Run a deterministic loop

agentic-proteins run --sequence "ACDEFGHIKLMNPQRSTVWY"

# Resume a run by ID

agentic-proteins resume --run-id <run_id>

# Compare two runs

agentic-proteins compare --left <run_id> --right <run_id>
```

[Back to top](#top)

---

<a id="what-this-does"></a>

## What This Does

* Runs a deterministic agentic loop with traceable artifacts and telemetry.
* Produces proxy structure-quality signals from sequence heuristics by default.
* Requires explicit opt-in to run real structure predictors via `--provider`.

[Back to top](#top)

---

<a id="what-this-does-not-do"></a>

## What This Does Not Do

* It does not run real structure prediction unless `--provider esmfold|rosettafold|openprotein` is specified and requirements are met.
* It does not finalize candidate selection without a signed human decision artifact.
* It does not expose internal modules as stable APIs.

[Back to top](#top)

---

<a id="stable-public-surface"></a>

## Stable Public Surface

* Supported CLI commands: `run`, `resume`, `compare`, `inspect-candidate`, `export-report`.
* Stable artifacts: `artifacts/<run_id>/` layout and JSON payloads.
* Stable CLI JSON output schema (see docs).

[Back to top](#top)

---

<a id="docs--resources"></a>

## Docs & Resources

Start here:

* **Getting Started**: https://bijux.github.io/agentic-proteins/overview/
* **CLI Reference**: https://bijux.github.io/agentic-proteins/cli/cli/
* **Architecture**: https://bijux.github.io/agentic-proteins/architecture/architecture/
* **Concepts**: https://bijux.github.io/agentic-proteins/concepts/terminology/

* **Site**: https://bijux.github.io/agentic-proteins/
* **Changelog**: https://github.com/bijux/agentic-proteins/blob/main/CHANGELOG.md
* **Repository**: https://github.com/bijux/agentic-proteins
* **Issues**: https://github.com/bijux/agentic-proteins/issues
* **Security**: https://github.com/bijux/agentic-proteins/security/advisories/new

[Back to top](#top)

---

<a id="contributing"></a>

## Contributing

See **[CONTRIBUTING.md](https://github.com/bijux/agentic-proteins/blob/main/CONTRIBUTING.md)** for setup, style, and tests.

[Back to top](#top)

---

<a id="license"></a>

## License

Apache-2.0 — see **[LICENSE](https://github.com/bijux/agentic-proteins/blob/main/LICENSE)**.
© 2025 Bijan Mousavi.

[Back to top](#top)
