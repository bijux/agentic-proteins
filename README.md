# Agentic Proteins  

A deterministic, artifact-first protein design runtime and CLI with enforced invariants, reproducible runs, and strict execution boundaries.  

[![PyPI](https://img.shields.io/pypi/v/agentic-proteins.svg)](https://pypi.org/project/agentic-proteins/) 
[![Python Version](https://img.shields.io/pypi/pyversions/agentic-proteins.svg)](https://pypi.org/project/agentic-proteins/) 
[![Typing: typed](https://img.shields.io/badge/typing-typed-2b6cb0.svg)](https://peps.python.org/pep-0561/) 
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](https://github.com/bijux/agentic-proteins/blob/main/LICENSE) 
[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue.svg)](https://bijux.github.io/agentic-proteins/) 
[![CI](https://github.com/bijux/agentic-proteins/actions/workflows/ci.yml/badge.svg)](https://github.com/bijux/agentic-proteins/actions/workflows/ci.yml)  

> **At a glance**: deterministic execution • artifact immutability • reproducible runs • invariant enforcement • API + CLI surfaces • structured telemetry  
> **Quality**: coverage floors enforced per module, benchmark regression gate active, docs linted and built in CI, no telemetry.  

## Overview  
Agentic Proteins is a deterministic, artifact-first protein design runtime and CLI.  
Architecture components are defined in [docs/architecture/architecture.md](docs/architecture/architecture.md).  
Read [docs/meta/DOCS_STYLE.md](docs/meta/DOCS_STYLE.md) before edits.  
Read [docs/meta/SPINE.md](docs/meta/SPINE.md) for order.  

## Contracts  
Deterministic runs occur for identical inputs and seeds.  
CLI JSON output schema is stable across releases.  
Run artifacts follow a stable layout.  

## Invariants  
Install with `pipx install agentic-proteins`.  
Run with `agentic-proteins run --sequence "ACDEFGHIKLMNPQRSTVWY"`.  
Inspect with `agentic-proteins inspect-candidate <candidate_id>`.  

## Failure Modes  
Docs: [docs/index.md](docs/index.md).  
Docs spine: [docs/meta/SPINE.md](docs/meta/SPINE.md).  
Getting started: [docs/overview/getting_started.md](docs/overview/getting_started.md).  

## Extension Points  
API doc: [docs/api/overview.md](docs/api/overview.md).  
Core concepts: [docs/concepts/core_concepts.md](docs/concepts/core_concepts.md).  
Docs style: [docs/meta/DOCS_STYLE.md](docs/meta/DOCS_STYLE.md).  

## Exit Criteria  
This README becomes obsolete when a generated entrypoint replaces it.  
The replacement is `docs/index.md`.  
Obsolete copies are removed.  
