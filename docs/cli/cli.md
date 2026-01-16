# cli  

**Scope:** CLI command contract.  
**Audience:** Users and contributors.  
**Guarantees:** Commands listed here are stable.  
**Non-Goals:** Usage examples.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines one responsibility.  
Architecture components are defined in [../architecture/architecture.md](../architecture/architecture.md).  
Read [../../concepts/core_concepts.md](../concepts/core_concepts.md) for vocabulary.  
Read [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) before edits.  
Read [../interface/cli_surface.md](../interface/cli_surface.md) for context.  

## Contracts  
Each statement is a contract.  
Contracts align with [tests/integration/test_cli.py](https://github.com/bijux/agentic-proteins/blob/main/tests/integration/test_cli.py).  
Contracts link to [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md) and [../interface/cli_surface.md](../interface/cli_surface.md).  

## Invariants  
Invariants describe stable behavior.  
Checks align with [tests/integration/test_cli.py](https://github.com/bijux/agentic-proteins/blob/main/tests/integration/test_cli.py).  
Invariants align with [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Failure Modes  
Failures are explicit and tested.  
Failure coverage aligns with [tests/integration/test_cli.py](https://github.com/bijux/agentic-proteins/blob/main/tests/integration/test_cli.py).  
Failures align with [../interface/cli_surface.md](../interface/cli_surface.md).  

## Extension Points  
Extensions require tests and docs.  
Extensions are tracked in [../../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  
Extensions align with [tests/integration/test_cli.py](https://github.com/bijux/agentic-proteins/blob/main/tests/integration/test_cli.py).  

## Exit Criteria  
This doc becomes obsolete when the surface ends.  
The replacement is linked in [../interface/cli_surface.md](../interface/cli_surface.md).  
Obsolete docs are removed.  

Code refs: [tests/integration/test_cli.py](https://github.com/bijux/agentic-proteins/blob/main/tests/integration/test_cli.py).  
