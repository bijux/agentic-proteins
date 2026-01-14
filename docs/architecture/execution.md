# Execution Subsystem

Responsibilities:

- Execute tasks from an execution graph against tool boundaries.
- Materialize observations and update candidates.
- Write artifacts and state snapshots.

Data flow:

- ExecutionContext carries resource limits and initial state.
- Tool results become observations and artifact payloads.
- State snapshots reference artifact metadata.

Constraints:

- Artifacts are written before state snapshots.
- Execution does not interpret biology beyond tool output validation.

Non-goals:

- Planning or replanning decisions.
- Provider I/O implementation.

Module refs: agentic_proteins.execution, agentic_proteins.runtime.control, agentic_proteins.tools.
