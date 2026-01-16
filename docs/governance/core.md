# core  

**Scope:** Non-negotiable core definition.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Core meaning does not drift.  
**Non-Goals:** Feature rationale.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines the immutable core.  
Core terms align with [../concepts/core_concepts.md](../concepts/core_concepts.md).  
Architecture context lives in [architecture/architecture.md](../architecture/architecture.md).  

## Contracts  
Core meaning binds agent, pathway, and cell roles.  
Contract locks live in [architecture/invariants.md](../architecture/invariants.md).  
Evidence uses [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  

## Invariants  
Core meaning stays fixed across releases.  
Core meaning aligns with [architecture/invariants.md](../architecture/invariants.md).  
Evidence aligns with [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  

## Failure Modes  
Core drift breaks [architecture/invariants.md](../architecture/invariants.md).  
Untracked changes break [../concepts/core_concepts.md](../concepts/core_concepts.md).  
Missing evidence breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Extension rules align with [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Evidence updates align with [tests/unit/test_docs_contract.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_docs_contract.py).  

## Exit Criteria  
This doc is obsolete when the core is encoded.  
The replacement is [architecture/architecture.md](../architecture/architecture.md).  
Obsolete docs are removed.  

Code refs: [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  
