# roadmap_ceiling  

**Scope:** Research roadmap ceiling.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Out-of-scope areas are explicit.  
**Non-Goals:** Feature backlog.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc states explicit research ceilings.  
Ceilings align with [core.md](core.md).  
Architecture context lives in [architecture/architecture.md](../architecture/architecture.md).  

## Contracts  
The system avoids unsupervised topology mutation.  
The system avoids hidden state mutation in [src/agentic_proteins/biology/protein_agent.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/protein_agent.py).  
The system avoids replacing contract locks in [src/agentic_proteins/core/api_lock.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/core/api_lock.py).  

## Invariants  
Ceilings align with [architecture/invariants.md](../architecture/invariants.md).  
Ceilings align with [architecture/experimental.md](../architecture/experimental.md).  
Checks align with [tests/unit/test_core_api_lock.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_core_api_lock.py).  

## Failure Modes  
Scope drift breaks [core.md](core.md).  
Implicit expansion breaks [architecture/invariants.md](../architecture/invariants.md).  
Untracked changes break [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Extension docs align with [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Extension checks align with [tests/unit/test_module_stability.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_module_stability.py).  

## Exit Criteria  
This doc is obsolete when scope is encoded.  
The replacement is [core.md](core.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/core/api_lock.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/core/api_lock.py).  
