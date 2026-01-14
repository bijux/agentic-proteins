# Architecture

This architecture exists to make protein design runs auditable and reproducible under lab constraints. The system separates decision-making from execution so that a run can be replayed from artifacts without relying on in-memory state or ambiguous side effects.

Why it is structured this way:

- Interfaces stay thin so that API/CLI changes do not leak into runtime behavior.
- Runtime owns orchestration only; domain logic lives outside runtime to keep scientific interpretation isolated and testable.
- Artifacts are first-class outputs; state snapshots reference artifact IDs so evidence and decisions are preserved.
- Providers are isolated from tools to keep I/O and external nondeterminism explicit.

What this does NOT solve:

- It does not guarantee determinism for external APIs.
- It does not perform real structure prediction unless an explicit provider is enabled.
- It does not infer or correct missing lab decisions; humans remain responsible for final selection.

Module map:

- interfaces/: CLI entrypoints.
- runtime/: orchestration and run control.
  - runtime/control/: execution loop, state transitions, artifacts.
  - runtime/context/: request/response models and lifecycle context.
  - runtime/infra/: logging, telemetry, config.
  - runtime/workspace.py: run layout and artifact paths.
- agents/: role-based decisions and schemas.
- execution/: tool execution and evaluation helpers.
- tools/: thin adapters that invoke providers.
- providers/: external integrations.
- domain/: biology and scoring logic.
- report/: report model, compute, and rendering.
- contracts/: stable interfaces.
- core/: cross-cutting primitives.
- registry/: agent/tool registries.
- state/: immutable state snapshots.
- memory/: session memory.
- validation/: validation helpers.

Data flow (plan -> execution -> artifacts -> selection):

- Planning produces a Plan and compiled ExecutionGraph.
- Execution runs tools and materializes observations.
- Artifacts are written before state snapshots; snapshots store artifact IDs only.
- Candidate selection and human decisions are recorded as artifacts.

State machine overview:

- PLANNED -> EXECUTING -> EVALUATED -> HUMAN_REVIEW
- HUMAN_REVIEW -> CANDIDATE_READY only after signed human decision

Artifact-first principle:

- Artifacts exist before any state update.
- State snapshots reference artifact IDs, not raw payloads.
- Reproduction relies on artifact replay and fingerprints.

Module refs: agentic_proteins.runtime, agentic_proteins.runtime.control, agentic_proteins.agents, agentic_proteins.domain.
