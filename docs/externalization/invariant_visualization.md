# invariant_visualization  

**Scope:** Invariant visualization tooling.  
**Audience:** External users and contributors.  
**Guarantees:** Per-tick invariants are observable.  
**Non-Goals:** GUI tooling.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc describes invariant visualization.  
Architecture context lives in [architecture/conservation.md](../architecture/conservation.md).  
Metrics context lives in [architecture/metrics.md](../architecture/metrics.md).  

## Contracts  
Per-tick invariant snapshots are recorded by [PathwayExecutor](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/pathway.py).  
Violations are captured in the invariant log.  
Visualization uses [scripts/visualize_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/visualize_invariants.py).  

## Invariants  
Invariant visibility aligns with [architecture/invariants.md](../architecture/invariants.md).  
Snapshot format aligns with [tests/unit/test_execution_cost.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_execution_cost.py).  
MPI meaning aligns with [mpi.md](mpi.md).  

## Failure Modes  
Missing snapshots hide violations.  
Drift in logs breaks [architecture/conservation.md](../architecture/conservation.md).  
Unlinked usage breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Review rules align with [../meta/TRIAGE.md](../meta/TRIAGE.md).  
MPI changes align with [surface_area.md](surface_area.md).  

## Exit Criteria  
This doc is obsolete when visualization is generated.  
The replacement is [architecture/metrics.md](../architecture/metrics.md).  
Obsolete docs are removed.  

Code refs: [scripts/visualize_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/visualize_invariants.py).  
