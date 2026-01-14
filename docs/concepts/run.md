# Run

What it is:

- A run is the complete execution record for a single input sequence.

Lifecycle:

- Run context is created with configuration and workspace paths.
- Iterations write artifacts and state snapshots.
- Human decisions are applied when required.

Invariants:

- State snapshots are immutable.
- Run outputs and summaries are stored in the workspace.

Failure semantics:

- Input validation failure produces input_invalid.
- Tool failures and invalid outputs produce tool_* or invalid_output.
- Missing human decision produces human_decision_missing.

Module refs: agentic_proteins.runtime.context, agentic_proteins.runtime.control.execution, agentic_proteins.core.failures.
