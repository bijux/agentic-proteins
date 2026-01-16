# execution_model  

**Scope:** Deterministic versus agentic boundary.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Boundaries are explicit and testable.  
**Non-Goals:** Provider-specific behavior.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines deterministic and agentic boundaries.  
Read [architecture.md](architecture.md) for component context.  
Read [../../concepts/core_concepts.md](../concepts/core_concepts.md) for vocabulary.  

## Contracts  
Deterministic behavior covers state transitions and artifact hashing.  
The execution contract is recorded in [src/agentic_proteins/core/contracts.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/core/contracts.py).  
Agentic behavior is limited to provider outputs and selection.  

## Invariants  
Deterministic paths use fixed inputs and seeds.  
Agentic paths record every decision and output.  
Boundaries align with [invariants.md](invariants.md).  

## Failure Modes  
Untracked stochastic output breaks reproducibility.  
Missing logs break traceability.  
Boundary drift breaks [architecture.md](architecture.md).  

## Extension Points  
Boundary changes update [execution_lifecycle.md](execution_lifecycle.md).  
Boundary changes update [invariants.md](invariants.md).  
Boundary changes update [../../concepts/core_concepts.md](../concepts/core_concepts.md).  

## Exit Criteria  
This doc becomes obsolete when execution is generated.  
The replacement is [architecture.md](architecture.md).  
Obsolete docs are removed.  

Code refs: [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  
