# golden_path  

**Scope:** Canonical golden path example.  
**Audience:** External users and contributors.  
**Guarantees:** Example uses MPI only.  
**Non-Goals:** Full tutorial.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc points to the canonical example.  
MPI context lives in [mpi.md](mpi.md).  
Architecture context lives in [architecture/architecture.md](../architecture/architecture.md).  

## Contracts  
The example uses only MPI entry points.  
The example shows agenticity, failure, and recovery.  
The example runtime stays under 60 seconds on default hardware.  
Example code lives in [scripts/golden_path_example.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/golden_path_example.py).  

## Invariants  
The golden path remains single and canonical.  
Evidence aligns with [tests/regression/test_negative_results.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_negative_results.py).  
MPI meaning aligns with [../concepts/core_concepts.md](../concepts/core_concepts.md).  

## Failure Modes  
Multiple examples dilute [mpi.md](mpi.md).  
Hidden dependencies break [../governance/core.md](../governance/core.md).  
Unlinked usage breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Review rules align with [../meta/TRIAGE.md](../meta/TRIAGE.md).  
MPI changes align with [surface_area.md](surface_area.md).  

## Exit Criteria  
This doc is obsolete when examples are generated.  
The replacement is [mpi.md](mpi.md).  
Obsolete docs are removed.  

Code refs: [scripts/golden_path_example.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/golden_path_example.py).  
