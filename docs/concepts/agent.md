# Agent

What it is:

- An agent is a decision unit that emits a structured output from a validated input schema.

Lifecycle:

- Input payload is validated against the agent input model.
- The agent produces a decision output.
- The decision is consumed by the runtime coordinator.

Invariants:

- input_model and output_model are explicit Pydantic schemas.
- allowed_tools bounds any tool requests.
- read_scopes and write_scopes restrict memory access.

Failure semantics:

- Schema validation failures stop the decision.
- Tool requests outside allowed_tools are rejected.
- Invalid memory scope writes are rejected.

Module refs: agentic_proteins.agents.base, agentic_proteins.agents.schemas, agentic_proteins.validation.agents.
