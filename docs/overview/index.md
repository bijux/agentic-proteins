# Overview

System purpose:

- Run a deterministic, artifact-first protein design loop that separates decisions from execution and records every run for audit.

Non-goals:

- Interactive modeling UI.
- Automated wet-lab execution.
- Performance benchmarking beyond recorded artifacts.

Where scripts and pipelines break:

- Decisions are embedded in code paths with no recorded rationale.
- Outputs and intermediate artifacts are overwritten or not stored.
- Human review steps are not captured in a reproducible format.

What is operationally different here:

- Decisions are schema-validated and recorded.
- Tool executions are wrapped by explicit boundaries.
- Artifacts are immutable and referenced by state snapshots.

Module refs: agentic_proteins.runtime, agentic_proteins.runtime.workspace, agentic_proteins.runtime.control.artifacts.
