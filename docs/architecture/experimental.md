# experimental  

**Scope:** Experimental provider rules.  
**Audience:** Contributors and opt-in users.  
**Guarantees:** Experimental providers are namespaced.  
**Non-Goals:** Provider-specific behavior.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines one responsibility.  
Architecture components are defined in [architecture.md](architecture.md).  
Read [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) before edits.  
Read [../../meta/NAMING.md](../meta/NAMING.md) for context.  

## Contracts  
Each statement is a contract.  
Contracts align with [tests/unit/test_experimental_provider_namespace.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_experimental_provider_namespace.py).  
Contracts link to [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) and [../../meta/NAMING.md](../meta/NAMING.md).  

## Invariants  
Invariants describe stable behavior.  
Checks align with [tests/unit/test_experimental_provider_namespace.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_experimental_provider_namespace.py).  
Invariants align with [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Failure Modes  
Failures are explicit and tested.  
Failure coverage aligns with [tests/unit/test_experimental_provider_namespace.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_experimental_provider_namespace.py).  
Failures align with [../../meta/NAMING.md](../meta/NAMING.md).  

## Extension Points  
Extensions require tests and docs.  
Extensions are tracked in [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Extensions align with [tests/unit/test_experimental_provider_namespace.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_experimental_provider_namespace.py).  

## Exit Criteria  
This doc becomes obsolete when the surface ends.  
The replacement is linked in [../../meta/NAMING.md](../meta/NAMING.md).  
Obsolete docs are removed.  

Code refs: [tests/unit/test_experimental_provider_namespace.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_experimental_provider_namespace.py).  
