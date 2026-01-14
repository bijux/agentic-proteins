# Planning Subsystem

Responsibilities:

- Define plan schemas and task graph structure.
- Validate plans against agent registry and capability constraints.
- Compile plans into execution graphs.

Data flow:

- Planner agent emits PlanDecision.
- Planning validation enforces structural constraints.
- Compiler produces ExecutionGraph for execution.

Constraints:

- Task identifiers must match plan keys.
- Dependency graph must be acyclic.
- Required capabilities must match agent capabilities.

Non-goals:

- Executing tools or updating runtime state.
- Selecting tools at runtime beyond plan compilation.

Module refs: agentic_proteins.agents.planning, agentic_proteins.validation.state, agentic_proteins.registry.agents.
