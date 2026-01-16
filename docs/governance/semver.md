# semver  

**Scope:** Semantic version meaning.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Version semantics are explicit.  
**Non-Goals:** Release tooling.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines semantic version meaning.  
Version meaning aligns with [core.md](core.md).  
Release history is tracked in [../CHANGELOG.md](https://github.com/bijux/agentic-proteins/blob/main/CHANGELOG.md).  

## Contracts  
MAJOR means semantic model change.  
MINOR means new capability without meaning shift.  
PATCH means bug fix only.  

## Invariants  
Version changes align with [architecture/invariants.md](../architecture/invariants.md).  
Contract locks align with [src/agentic_proteins/core/api_lock.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/core/api_lock.py).  
Checks align with [tests/unit/test_core_api_lock.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_core_api_lock.py).  

## Failure Modes  
Meaning drift breaks [core.md](core.md).  
Mismatched versions break [../CHANGELOG.md](https://github.com/bijux/agentic-proteins/blob/main/CHANGELOG.md).  
Untracked changes break [architecture/invariants.md](../architecture/invariants.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Extension checks align with [tests/unit/test_module_stability.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_module_stability.py).  
Extension docs align with [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Exit Criteria  
This doc is obsolete when versioning is generated.  
The replacement is [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/core/api_lock.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/core/api_lock.py).  
