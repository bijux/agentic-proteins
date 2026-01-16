# SPINE  

**Scope:** Single navigation spine for docs/.  
**Audience:** Readers consuming docs top-down.  
**Guarantees:** Lists all docs in order.  
**Non-Goals:** Per-topic READMEs.  
Why: This doc exists to record its single responsibility for review.  

## Overview  
This doc defines one responsibility.  
Architecture components are defined in [../architecture/architecture.md](../architecture/architecture.md).  
Read [../index.md](../index.md) before edits.  
Read [DOCS_STYLE.md](DOCS_STYLE.md) for context.  

## Contracts  
Each statement is a contract.  
Contracts align with [mkdocs.yml](https://github.com/bijux/agentic-proteins/blob/main/mkdocs.yml).  
Contracts link to [../index.md](../index.md) and [DOCS_STYLE.md](DOCS_STYLE.md).  

## Invariants  
Invariants describe stable behavior.  
Checks align with [mkdocs.yml](https://github.com/bijux/agentic-proteins/blob/main/mkdocs.yml).  
Invariants align with [../index.md](../index.md).  

## Failure Modes  
Failures are explicit and tested.  
Failure coverage aligns with [mkdocs.yml](https://github.com/bijux/agentic-proteins/blob/main/mkdocs.yml).  
Failures align with [DOCS_STYLE.md](DOCS_STYLE.md).  

## Extension Points  
Extensions require tests and docs.  
Extensions are tracked in [../index.md](../index.md).  
Extensions align with [mkdocs.yml](https://github.com/bijux/agentic-proteins/blob/main/mkdocs.yml).  

## Exit Criteria  
This doc becomes obsolete when the surface ends.  
The replacement is linked in [DOCS_STYLE.md](DOCS_STYLE.md).  
Obsolete docs are removed.  

Code refs: [tests/unit/test_docs_contract.py](https://github.com/bijux/agentic-proteins/blob/main/tests/unit/test_docs_contract.py).  
Docs list:  
- [meta/DOCS_STYLE.md](DOCS_STYLE.md)  
- [meta/DOCS_VOICE.md](DOCS_VOICE.md)  
- [meta/NAMING.md](NAMING.md)  
- [meta/TRIAGE.md](TRIAGE.md)  
- [meta/SPINE.md](SPINE.md)  
- [index.md](../index.md)  
- [overview/getting_started.md](../overview/getting_started.md)  
- [concepts/core_concepts.md](../concepts/core_concepts.md)  
- [governance/core.md](../governance/core.md)  
- [governance/semver.md](../governance/semver.md)  
- [governance/anti_patterns.md](../governance/anti_patterns.md)  
- [governance/roadmap_ceiling.md](../governance/roadmap_ceiling.md)  
- [governance/positioning.md](../governance/positioning.md)  
- [governance/release_identity.md](../governance/release_identity.md)  
- [research/agentic_criteria.md](../research/agentic_criteria.md)  
- [research/agent_taxonomy.md](../research/agent_taxonomy.md)  
- [research/formal_model.md](../research/formal_model.md)  
- [research/falsifiable_claim.md](../research/falsifiable_claim.md)  
- [research/decisive_experiment.md](../research/decisive_experiment.md)  
- [research/ablation_studies.md](../research/ablation_studies.md)  
- [research/neutral_results.md](../research/neutral_results.md)  
- [research/reviewer_premortem.md](../research/reviewer_premortem.md)  
- [research/system_schematic.md](../research/system_schematic.md)  
- [externalization/mpi.md](../externalization/mpi.md)  
- [externalization/golden_path.md](../externalization/golden_path.md)  
- [externalization/misuse_guards.md](../externalization/misuse_guards.md)  
- [externalization/surface_area.md](../externalization/surface_area.md)  
- [externalization/sandbox.md](../externalization/sandbox.md)  
- [externalization/invariant_visualization.md](../externalization/invariant_visualization.md)  
- [externalization/why_not_x.md](../externalization/why_not_x.md)  
- [architecture/architecture.md](../architecture/architecture.md)  
- [architecture/invariants.md](../architecture/invariants.md)  
- [architecture/experimental.md](../architecture/experimental.md)  
- [architecture/llm_authority.md](../architecture/llm_authority.md)  
- [architecture/execution_model.md](../architecture/execution_model.md)  
- [architecture/execution_lifecycle.md](../architecture/execution_lifecycle.md)  
- [architecture/design_debt.md](../architecture/design_debt.md)  
- [cli/cli.md](../cli/cli.md)  
- [interface/cli_surface.md](../interface/cli_surface.md)  
- [api/overview.md](../api/overview.md)  
- [api/schema.md](../api/schema.md)  
- [security/dependencies.md](../security/dependencies.md)  
- [security/threat_model.md](../security/threat_model.md)  
- [security/citation.md](../security/citation.md)  
