# pathway_limits  

**Scope:** Hard limits for agent interactions.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Limits are enforced at runtime.  
**Non-Goals:** Adaptive scaling.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines pathway interaction limits.  
Architecture components are defined in [architecture.md](architecture.md).  
Read [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) for structure.  

## Contracts  
Incoming signals per tick are capped.  
Outgoing signals per tick are capped.  
Dependency depth is capped.  

## Invariants  
Limits apply to every pathway.  
Limit violations stop execution.  
Limits are recorded in tests.  

## Failure Modes  
Limit violations raise errors.  
Silent overflow is rejected.  
Cycles are blocked by contract rules.  

## Extension Points  
Limit changes update [execution_cost.md](execution_cost.md).  
Contract changes update [architecture.md](architecture.md).  
Documentation updates follow [../../meta/TRIAGE.md](../meta/TRIAGE.md).  

## Exit Criteria  
This doc becomes obsolete when limits are generated.  
The replacement is [architecture.md](architecture.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/biology/pathway.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/pathway.py).  
