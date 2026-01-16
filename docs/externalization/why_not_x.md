# why_not_x  

**Scope:** Why-not-X contrasts.  
**Audience:** Reviewers and contributors.  
**Guarantees:** Contrasts are explicit.  
**Non-Goals:** Full survey.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc lists explicit contrasts.  
Architecture context lives in [architecture/architecture.md](../architecture/architecture.md).  
MPI context lives in [mpi.md](mpi.md).  

## Contracts  
Workflow engines focus on orchestration, while this system focuses on bounded state transitions.  
Classic MAS frameworks optimize global coordination, while this system enforces local contracts.  
End-to-end LLM agents blur control, while this system enforces regulator boundaries.  

## Invariants  
Contrasts align with [../governance/core.md](../governance/core.md).  
Contrasts align with [architecture/execution_model.md](../architecture/execution_model.md).  
Evidence aligns with [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  

## Failure Modes  
Missing contrasts weakens reviewability.  
Contrast drift breaks [../governance/core.md](../governance/core.md).  
Unlinked usage breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Review rules align with [../meta/TRIAGE.md](../meta/TRIAGE.md).  
MPI changes align with [surface_area.md](surface_area.md).  

## Exit Criteria  
This doc is obsolete when contrasts are encoded.  
The replacement is [../governance/core.md](../governance/core.md).  
Obsolete docs are removed.  

Code refs: [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  
