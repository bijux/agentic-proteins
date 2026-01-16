# design_debt  

**Scope:** Design debt ledger.  
**Audience:** Contributors.  
**Guarantees:** Ledger contains <=10 items with exits.  
**Non-Goals:** Issue tracking.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines one responsibility.  
Architecture components are defined in [architecture.md](architecture.md).  
Read [../../meta/TRIAGE.md](../meta/TRIAGE.md) before edits.  
Read [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) for context.  

## Contracts  
Each statement is a contract.  
Contracts align with [scripts/check_design_debt.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_design_debt.py).  
Contracts link to [../../meta/TRIAGE.md](../meta/TRIAGE.md) and [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Invariants  
Invariants describe stable behavior.  
Checks align with [scripts/check_design_debt.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_design_debt.py).  
Invariants align with [../../meta/TRIAGE.md](../meta/TRIAGE.md).  

## Failure Modes  
Failures are explicit and tested.  
Failure coverage aligns with [scripts/check_design_debt.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_design_debt.py).  
Failures align with [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions require tests and docs.  
Extensions are tracked in [../../meta/TRIAGE.md](../meta/TRIAGE.md).  
Extensions align with [scripts/check_design_debt.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_design_debt.py).  

## Exit Criteria  
This doc becomes obsolete when the surface ends.  
The replacement is linked in [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Obsolete docs are removed.  

Code refs: [scripts/check_design_debt.py](https://github.com/bijux/agentic-proteins/blob/main/scripts/check_design_debt.py).  
