# anti_patterns  

**Scope:** Non-agentic anti-patterns.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Anti-patterns are explicit and rejected.  
**Non-Goals:** Exhaustive catalog.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc lists rejected patterns.  
Anti-patterns align with [core.md](core.md).  
Architecture context lives in [architecture/architecture.md](../architecture/architecture.md).  

## Contracts  
Direct state mutation bypasses [src/agentic_proteins/biology/protein_agent.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/protein_agent.py).  
Hidden stochastic paths violate [architecture/invariants.md](../architecture/invariants.md).  
Undeclared transitions violate [src/agentic_proteins/biology/validation.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/validation.py).  

## Invariants  
Agent behavior stays within [../concepts/core_concepts.md](../concepts/core_concepts.md).  
Transition rules align with [architecture/execution_model.md](../architecture/execution_model.md).  
Checks align with [tests/unit/test_protein_agent.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_protein_agent.py).  

## Failure Modes  
Bypass attempts break [architecture/invariants.md](../architecture/invariants.md).  
Silent changes break [core.md](core.md).  
Drift detection aligns with [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Extension checks align with [tests/unit/test_module_stability.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_module_stability.py).  
Extension docs align with [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Exit Criteria  
This doc is obsolete when anti-patterns are encoded.  
The replacement is [architecture/invariants.md](../architecture/invariants.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/biology/protein_agent.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/protein_agent.py).  
