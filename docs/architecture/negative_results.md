# negative_results  

**Scope:** Negative results criteria.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Failure scenarios are explicit and tested.  
**Non-Goals:** Success narratives.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines negative results scenarios.  
Architecture components are defined in [architecture.md](architecture.md).  
Read [metrics.md](metrics.md) for measurement context.  

## Contracts  
A cyclic pathway must fail validation.  
A proposal that increases energy cost must worsen stability.  
Degraded proteins must not recover.  

## Invariants  
Negative results are enforced by tests.  
Failures are structured and observable.  
No hidden recovery is allowed.  

## Failure Modes  
Silent success invalidates results.  
Missing failures invalidate tests.  
Undefined scenarios are rejected.  

## Extension Points  
Scenario changes update [metrics.md](metrics.md).  
Contract changes update [pathway_limits.md](pathway_limits.md).  
Documentation updates follow [../../meta/TRIAGE.md](../meta/TRIAGE.md).  

## Exit Criteria  
This doc becomes obsolete when results are generated.  
The replacement is [metrics.md](metrics.md).  
Obsolete docs are removed.  

Code refs: [tests/regression/test_negative_results.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_negative_results.py).  
