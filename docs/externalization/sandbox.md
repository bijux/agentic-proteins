# sandbox  

**Scope:** Sandbox separation.  
**Audience:** External users and contributors.  
**Guarantees:** Core and sandbox remain distinct.  
**Non-Goals:** Sandbox feature catalog.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines the sandbox split.  
Core context lives in [../governance/core.md](../governance/core.md).  
Experimental context lives in [architecture/experimental.md](../architecture/experimental.md).  

## Contracts  
Core modules live under [src/agentic_proteins/core](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/core).  
Sandbox modules live under [src/agentic_proteins/sandbox](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/sandbox/__init__.py).  
Sandbox code is marked experimental.  

## Invariants  
Core stability aligns with [architecture/invariants.md](../architecture/invariants.md).  
Sandbox usage aligns with [architecture/experimental.md](../architecture/experimental.md).  
Evidence aligns with [tests/unit/test_module_stability.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_module_stability.py).  

## Failure Modes  
Mixing core and sandbox breaks [../governance/core.md](../governance/core.md).  
Unlabeled sandbox code breaks [architecture/experimental.md](../architecture/experimental.md).  
Unlinked usage breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Review rules align with [../meta/TRIAGE.md](../meta/TRIAGE.md).  
MPI changes align with [mpi.md](mpi.md).  

## Exit Criteria  
This doc is obsolete when sandbox is removed.  
The replacement is [architecture/experimental.md](../architecture/experimental.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/sandbox/__init__.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/sandbox/__init__.py).  
