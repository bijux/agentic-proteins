# reviewer_premortem  

**Scope:** Reviewer pre-mortem.  
**Audience:** Reviewers and contributors.  
**Guarantees:** Anticipated critiques are explicit.  
**Non-Goals:** Debate.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc lists common review critiques.  
Architecture context lives in [architecture/architecture.md](../architecture/architecture.md).  
Claim context lives in [falsifiable_claim.md](falsifiable_claim.md).  

## Contracts  
Critique: “This is orchestration.” Response: signal scopes and pathway contracts show locality.  
Critique: “No intelligence.” Response: regulator proposals are bounded and measured.  
Critique: “Biology metaphor.” Response: constrained agents and pathways are explicit.  
Critique: “Over-engineered.” Response: invariants and failures are enforced.  
Evidence uses [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  

## Invariants  
Critique list stays visible.  
Responses align with [../governance/core.md](../governance/core.md).  
Evidence aligns with [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  

## Failure Modes  
Missing critiques weakens review readiness.  
Response drift breaks [../governance/core.md](../governance/core.md).  
Missing evidence breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Updates follow [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Extensions align with [architecture/experimental.md](../architecture/experimental.md).  
Evidence updates align with [tests/unit/test_docs_contract.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_docs_contract.py).  

## Exit Criteria  
This doc is obsolete when critiques are encoded.  
The replacement is [architecture/metrics.md](../architecture/metrics.md).  
Obsolete docs are removed.  

Code refs: [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  
