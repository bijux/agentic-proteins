# index  

**Scope:** Docs entry point.  
**Audience:** Readers starting here.  
**Guarantees:** Points to the spine and scope.  
**Non-Goals:** Deep technical detail.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
Agentic Proteins is a deterministic, artifact-first protein design runtime and CLI.  
Architecture components are defined in [architecture/architecture.md](architecture/architecture.md).  
Read [meta/DOCS_STYLE.md](meta/DOCS_STYLE.md) before edits.  
Read [meta/SPINE.md](meta/SPINE.md) for order.  

## Contracts  
Deterministic runs occur for identical inputs and seeds.  
CLI JSON output schema is stable across releases.  
Run artifacts follow a stable layout.  

## Invariants  
Install with `pipx install agentic-proteins`.  
Run with `agentic-proteins run --sequence "ACDEFGHIKLMNPQRSTVWY"`.  
Inspect with `agentic-proteins inspect-candidate <candidate_id>`.  

## Failure Modes  
Docs: [index.md](index.md).  
Docs spine: [meta/SPINE.md](meta/SPINE.md).  
Getting started: [overview/getting_started.md](overview/getting_started.md).  

## Extension Points  
API doc: [api/overview.md](api/overview.md).  
Core concepts: [concepts/core_concepts.md](concepts/core_concepts.md).  
Docs style: [meta/DOCS_STYLE.md](meta/DOCS_STYLE.md).  

## Exit Criteria  
This entrypoint becomes obsolete when a generated index replaces it.  
The replacement is [meta/SPINE.md](meta/SPINE.md).  
Obsolete copies are removed.  

Code refs: [tests/unit/test_docs_contract.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_docs_contract.py).  
