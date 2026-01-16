# abstraction_removal  

**Scope:** Removal of unused abstraction layers.  
**Audience:** Contributors and reviewers.  
**Guarantees:** Removed layers are documented and tested.  
**Non-Goals:** Historical narrative.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc records the abstraction removal.  
Architecture components are defined in [architecture.md](architecture.md).  
Read [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) for structure.  

## Contracts  
The contracts interface layer was removed.  
The registry base class was removed.  
The registry re-export indirection was removed.  

## Invariants  
Direct imports replace removed layers.  
Registry behavior remains explicit.  
Public interfaces remain tested.  

## Failure Modes  
Missing imports fail tests.  
Unexpected coupling fails review.  
Undefined layers are rejected.  

## Extension Points  
Removals update [design_debt.md](design_debt.md).  
Public interface changes update [../governance/core.md](../governance/core.md).  
Documentation updates follow [../../meta/TRIAGE.md](../meta/TRIAGE.md).  

## Exit Criteria  
This doc becomes obsolete when removals are generated.  
The replacement is [../governance/core.md](../governance/core.md).  
Obsolete docs are removed.  

Code refs: [src/agentic_proteins/registry/agents.py](https://github.com/bijux/agentic-proteins/blob/main/src/agentic_proteins/registry/agents.py).  
