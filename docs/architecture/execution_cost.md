# execution_cost  

**Scope:** Canonical execution cost per tick.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Cost fields are defined and recorded.  
**Non-Goals:** Benchmark optimization.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines canonical execution cost.  
Architecture components are defined in [architecture.md](architecture.md).  
Read [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) for structure.  

## Contracts  
CPU time is recorded per tick.  
Memory usage is recorded per tick.  
Agent count and signal volume are recorded per tick.  

## Invariants  
Cost records are appended per step.  
Cost fields are numeric and non-negative.  
Cost recording does not mutate state.  

## Failure Modes  
Missing cost records fail tests.  
Negative values fail validation.  
Inconsistent ticks fail review.  

## Extension Points  
Cost changes update [metrics.md](metrics.md).  
Stress tests update [pathway_limits.md](pathway_limits.md).  
Documentation updates follow [../../meta/TRIAGE.md](../meta/TRIAGE.md).  

## Exit Criteria  
This doc becomes obsolete when costs are generated.  
The replacement is [metrics.md](metrics.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/biology/pathway.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/pathway.py).  
