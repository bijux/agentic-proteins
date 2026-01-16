# positioning  

**Scope:** Final positioning choice.  
**Audience:** Reviewers and contributors.  
**Guarantees:** Position is explicit.  
**Non-Goals:** Market analysis.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines the final positioning.  
Architecture context lives in [architecture/architecture.md](../architecture/architecture.md).  
Vocabulary aligns with [../concepts/core_concepts.md](../concepts/core_concepts.md).  

## Contracts  
Positioning is agent systems research.  
Computational biology context is modeled, not claimed as primary.  
Hybrid simulation framing is limited to pathway execution.  
Evidence uses [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  

## Invariants  
Positioning stays fixed across releases.  
Positioning aligns with [core.md](core.md).  
Evidence aligns with [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  

## Failure Modes  
Ambiguous positioning weakens reviewability.  
Position drift breaks [core.md](core.md).  
Missing evidence breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Position updates follow [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Extensions align with [architecture/experimental.md](../architecture/experimental.md).  
Evidence updates align with [tests/unit/test_docs_contract.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_docs_contract.py).  

## Exit Criteria  
This doc is obsolete when positioning is encoded.  
The replacement is [core.md](core.md).  
Obsolete docs are removed.  

Code refs: [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  
