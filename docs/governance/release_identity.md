# release_identity  

**Scope:** Release identity selection.  
**Audience:** Reviewers and contributors.  
**Guarantees:** Identity is explicit.  
**Non-Goals:** Marketing framing.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines the release identity.  
Positioning context lives in [positioning.md](positioning.md).  
Version context lives in [semver.md](semver.md).  

## Contracts  
Release identity is research prototype.  
Identity aligns with [core.md](core.md).  
Evidence aligns with [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  

## Invariants  
Identity stays fixed across releases.  
Identity aligns with [positioning.md](positioning.md).  
Identity aligns with [semver.md](semver.md).  

## Failure Modes  
Ambiguity breaks reviewability.  
Identity drift breaks [core.md](core.md).  
Unlinked usage breaks [../meta/DOCS_STYLE.md](../meta/DOCS_STYLE.md).  

## Extension Points  
Extensions follow [architecture/experimental.md](../architecture/experimental.md).  
Review rules align with [../meta/TRIAGE.md](../meta/TRIAGE.md).  
MPI changes align with [../externalization/surface_area.md](../externalization/surface_area.md).  

## Exit Criteria  
This doc is obsolete when identity is encoded.  
The replacement is [core.md](core.md).  
Obsolete docs are removed.  

Code refs: [tests/regression/test_architecture_invariants.py](https://github.com/bijux/agentic-proteins/blob/main/tests/regression/test_architecture_invariants.py).  
