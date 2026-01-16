# index  

**Scope:** Docs entry point.  
**Audience:** Readers starting here.  
**Guarantees:** Points to the spine and scope.  
**Non-Goals:** Deep technical detail.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
Agentic Proteins is a deterministic, artifact-first protein design runtime and CLI.  
Architecture components are defined in [Architecture](architecture/architecture.md).  
Read [Docs Style](meta/DOCS_STYLE.md) before edits.  
Read [Spine](meta/SPINE.md) for order.  

## Contracts  
Deterministic runs occur for identical inputs and seeds.  
CLI JSON output schema is stable across releases.  
Run artifacts follow a stable layout.  

## Invariants  
Install with `pipx install agentic-proteins`.  
Run with `agentic-proteins run --sequence "ACDEFGHIKLMNPQRSTVWY"`.  
Inspect with `agentic-proteins inspect-candidate <candidate_id>`.  

## Failure Modes  
Docs: [Index](index.md).  
Docs spine: [Spine](meta/SPINE.md).  
Getting started: [Getting Started](overview/getting_started.md).  

## Extension Points  
API doc: [Overview](api/overview.md).  
Core concepts: [Core Concepts](concepts/core_concepts.md).  
Docs style: [Docs Style](meta/DOCS_STYLE.md).  

## Exit Criteria  
This entrypoint becomes obsolete when a generated index replaces it.  
The replacement is [Spine](meta/SPINE.md).  
Obsolete copies are removed.  

Code refs: [tests/unit/test_docs_contract.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_docs_contract.py).  
