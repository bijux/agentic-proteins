# Evaluation Subsystem

Responsibilities:

- Evaluate tool outputs against expected properties.
- Produce evaluation reports for regression checks.

Data flow:

- Execution outputs are mapped to evaluation inputs.
- Evaluation reports are generated without modifying runtime state.

Constraints:

- Deterministic outputs for identical inputs.

Non-goals:

- Running tools or producing artifacts for runtime.
- Modifying candidate state.

Module refs: agentic_proteins.execution.evaluation, agentic_proteins.report.compute, agentic_proteins.domain.metrics.
