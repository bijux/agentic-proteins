# misuse_guards  

**Scope:** Runtime misuse guards.  
**Audience:** External users and contributors.  
**Guarantees:** Guardrails fail loudly.  
**Non-Goals:** Error recovery policy.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc lists misuse guards.  
MPI context lives in [mpi.md](mpi.md).  
Architecture context lives in [architecture/invariants.md](../architecture/invariants.md).  

## Contracts  
Direct state mutation is rejected by [ProteinAgent](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/protein_agent.py).  
Invariant checks run per tick in [PathwayExecutor](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/pathway.py).  
Unauthorized LLM actions raise in [LLMRegulator](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/regulator.py).  

## Invariants  
Guards align with [../governance/core.md](../governance/core.md).  
Guard tests align with [tests/unit/test_protein_agent.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_protein_agent.py).  
Guard tests align with [tests/unit/test_llm_regulator.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_llm_regulator.py).  

## Failure Modes  
Bypass attempts break [architecture/invariants.md](../architecture/invariants.md).  
Silent failures break [../governance/core.md](../governance/core.md).  
Unlinked usage breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Review rules align with [../meta/TRIAGE.md](../meta/TRIAGE.md).  
MPI changes align with [surface_area.md](surface_area.md).  

## Exit Criteria  
This doc is obsolete when guards are generated.  
The replacement is [architecture/invariants.md](../architecture/invariants.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/biology/protein_agent.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/protein_agent.py).  
