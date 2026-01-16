# surface_area  

**Scope:** Surface-area budgeting.  
**Audience:** External users and contributors.  
**Guarantees:** Public surface stays bounded.  
**Non-Goals:** Full API listing.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines surface-area budgets.  
MPI context lives in [mpi.md](mpi.md).  
Architecture context lives in [architecture/invariants.md](../architecture/invariants.md).  

## Contracts  
Public entry points are capped by [src/agentic_proteins/core/surface_area.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/core/surface_area.py).  
Extension points are capped by the same budget.  
Configuration knobs are capped by the same budget.  

## Invariants  
Budgets align with [../governance/core.md](../governance/core.md).  
Budget checks align with [tests/unit/test_surface_area_budget.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_surface_area_budget.py).  
Budget changes update [mpi.md](mpi.md).  

## Failure Modes  
Budget overruns trigger review.  
Untracked entry points break [../governance/core.md](../governance/core.md).  
Unlinked usage breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Review rules align with [../meta/TRIAGE.md](../meta/TRIAGE.md).  
MPI changes align with [mpi.md](mpi.md).  

## Exit Criteria  
This doc is obsolete when budgets are generated.  
The replacement is [mpi.md](mpi.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/core/surface_area.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/core/surface_area.py).  
