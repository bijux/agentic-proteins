# llm_authority  

**Scope:** LLM authority boundary.  
**Audience:** Contributors and reviewers.  
**Guarantees:** LLM actions are bounded and enforced.  
**Non-Goals:** Model benchmarking.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines the LLM authority boundary.  
Architecture components are defined in [architecture.md](architecture.md).  
Read [../../concepts/core_concepts.md](../concepts/core_concepts.md) for vocabulary.  
Read [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) for structure.  

## Contracts  
Allowed actions are tuning only.  
Forbidden actions include any state mutation.  
Read-only and write-through permissions are explicit.  

## Invariants  
Proposals never mutate state directly.  
Validation rejects invalid proposals.  
Approvals gate all proposal application.  

## Failure Modes  
Forbidden actions raise errors.  
Invalid proposals are rejected and logged.  
Missing approvals block proposal application.  

## Extension Points  
Authority changes update [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Authority changes update [../../concepts/core_concepts.md](../concepts/core_concepts.md).  
Authority changes update [architecture.md](architecture.md).  

## Exit Criteria  
This doc becomes obsolete when authority is generated.  
The replacement is [architecture.md](architecture.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/biology/regulator.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/biology/regulator.py).  
