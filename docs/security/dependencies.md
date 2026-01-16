# dependencies  

**Scope:** Runtime dependency allowlist.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Allowlist covers project.dependencies.  
**Non-Goals:** Dev dependency tracking.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines one responsibility.  
Architecture components are defined in [../architecture/architecture.md](../architecture/architecture.md).  
Read [threat_model.md](threat_model.md) before edits.  
Read [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) for context.  

## Contracts  
Each statement is a contract.  
Contracts align with [scripts/check_dependency_allowlist.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_dependency_allowlist.py).  
Contracts link to [threat_model.md](threat_model.md) and [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Invariants  
Invariants describe stable behavior.  
Checks align with [scripts/check_dependency_allowlist.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_dependency_allowlist.py).  
Invariants align with [threat_model.md](threat_model.md).  

## Failure Modes  
Failures are explicit and tested.  
Failure coverage aligns with [scripts/check_dependency_allowlist.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_dependency_allowlist.py).  
Failures align with [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions require tests and docs.  
Extensions are tracked in [threat_model.md](threat_model.md).  
Extensions align with [scripts/check_dependency_allowlist.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_dependency_allowlist.py).  

## Exit Criteria  
This doc becomes obsolete when the surface ends.  
The replacement is linked in [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Obsolete docs are removed.  

Code refs: [scripts/check_dependency_allowlist.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_dependency_allowlist.py).  
Allowlist:  
- requests  
- biopython  
- numpy  
- click  
- fastapi  
- uvicorn  
- pydantic  
- loguru  
- slowapi  
- boto3  
