# Plan

What it is:

- A plan is a task graph that encodes agent assignments, dependencies, and constraints.

Lifecycle:

- Planner emits a PlanDecision.
- Plan is validated for structure and capability constraints.
- Plan is compiled into an ExecutionGraph.

Invariants:

- Task IDs match map keys.
- Dependencies are acyclic and reference existing tasks.
- Plan fingerprints are stable for identical content.

Failure semantics:

- Missing tasks or invalid dependency edges fail validation.
- Unknown agent names or missing capabilities fail validation.
- Cycles in the dependency graph fail validation.

Module refs: agentic_proteins.agents.planning.schemas, agentic_proteins.agents.planning.validation.
