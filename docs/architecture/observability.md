# Observability Subsystem

Responsibilities:

- Emit structured logs and telemetry for each run.
- Persist telemetry and logs in the run workspace.

Data flow:

- Telemetry records events, timers, and cost metrics.
- Logs are scoped by component and written to logs/run.jsonl.

Constraints:

- Required telemetry fields must be present.
- Logs and telemetry are stored under the workspace layout.

Non-goals:

- External metrics aggregation.
- Run control decisions based on telemetry.

Module refs: agentic_proteins.runtime.infra.observability, agentic_proteins.runtime.infra.telemetry, agentic_proteins.runtime.workspace.
