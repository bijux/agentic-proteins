# falsifiable_claim  

**Scope:** Single falsifiable claim.  
**Audience:** Reviewers and contributors.  
**Guarantees:** Claim is testable.  
**Non-Goals:** Multiple hypotheses.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc states one falsifiable claim.  
Architecture context lives in [architecture/architecture.md](../architecture/architecture.md).  
Vocabulary aligns with [../concepts/core_concepts.md](../concepts/core_concepts.md).  

## Contracts  
Claim: bounded regulator proposals improve recovery rate without raising failure rate.  
Recovery rate is computed in [architecture/metrics.md](../architecture/metrics.md).  
Failure rate is computed in [architecture/metrics.md](../architecture/metrics.md).  
Evidence uses [tests/regression/test_negative_results.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_negative_results.py).  

## Invariants  
Claim wording stays fixed.  
Claim aligns with [../governance/core.md](../governance/core.md).  
Evidence aligns with [tests/regression/test_negative_results.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_negative_results.py).  

## Failure Modes  
Unclear claim blocks experiments.  
Claim drift breaks [../governance/core.md](../governance/core.md).  
Missing evidence breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Claim updates follow [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Extensions align with [architecture/experimental.md](../architecture/experimental.md).  
Evidence updates align with [tests/unit/test_docs_contract.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_docs_contract.py).  

## Exit Criteria  
This doc is obsolete when claim is replaced.  
The replacement is [architecture/metrics.md](../architecture/metrics.md).  
Obsolete docs are removed.  

Code refs: [tests/regression/test_negative_results.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_negative_results.py).  
