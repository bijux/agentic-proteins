# execution_lifecycle  

**Scope:** Execution lifecycle state machine.  
**Audience:** Contributors and reviewers.  
**Guarantees:** States and transitions are explicit.  
**Non-Goals:** Alternate lifecycles.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines the execution lifecycle state machine.  
Read [architecture.md](architecture.md) for component context.  
Read [../../concepts/core_concepts.md](../concepts/core_concepts.md) for vocabulary.  

## Contracts  
States and transitions are listed below.  
The lifecycle uses a single linear progression.  
Deviations are failures.  
- init -> plan  
- plan -> act  
- act -> observe  
- observe -> evaluate  
- evaluate -> terminate  
- terminate -> terminate  

## Invariants  
State order is init, plan, act, observe, evaluate, terminate.  
Each execution unit records its state.  
Transitions align with [execution_model.md](execution_model.md).  

## Failure Modes  
Out-of-order transitions break traceability.  
Missing states break evaluation artifact records.  
Lifecycle drift breaks [architecture.md](architecture.md).  

## Extension Points  
Lifecycle changes update [execution_model.md](execution_model.md).  
Lifecycle changes update [invariants.md](invariants.md).  
Lifecycle changes update [../../concepts/core_concepts.md](../concepts/core_concepts.md).  

## Exit Criteria  
This doc becomes obsolete when execution is generated.  
The replacement is [architecture.md](architecture.md).  
Obsolete docs are removed.  

Code refs: [tests/integration/test_runtime_flow.py](https://github.com/bijux/agentic-proteins/blob/main/tests/integration/test_runtime_flow.py).  
