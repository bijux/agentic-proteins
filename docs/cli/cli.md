# CLI Interface Spec

Use `--json` for structured output. Without `--json`, commands emit human-readable summaries.

JSON output schema (use `--json`):
```json
run/resume:
{
  "run_id": "...",
  "candidate_id": "...",
  "command": "run|resume",
  "execution_status": "completed|errored|aborted",
  "workflow_state": "running|paused|awaiting_human_review|done",
  "outcome": "accepted|rejected|needs_review|inconclusive",
  "provider": "heuristic_proxy|local_esmfold|local_rosettafold|...",
  "tool_status": "success|degraded|failed|skipped",
  "qc_status": "acceptable|reject|...",
  "artifacts_dir": "artifacts/<run_id>",
  "warnings": [],
  "failure": "failure_type|null",
  "version": {}
}
```

Errors with `--json` return:
```json
{
  "status": "error",
  "command": "run|resume|compare|inspect-candidate|export-report",
  "error": "string"
}
```

run

- intent: execute a new run from a sequence or FASTA input.
- inputs: --sequence or --fasta.
- optional: --provider esmfold|rosettafold|openprotein to run real predictors; otherwise uses heuristic_proxy.
- outputs: run summary JSON on stdout with `--json`; human-readable summary otherwise.
- filesystem side effects: creates artifacts/<run_id>/ with plan, execution, report, telemetry, logs.
- failure behavior: input_invalid, capability_missing, invalid_plan, tool_* failures.

resume

- intent: continue a run using a stored candidate.
- inputs: candidate_id.
- optional: --provider esmfold|rosettafold|openprotein to run real predictors; otherwise uses heuristic_proxy.
- outputs: run summary JSON on stdout with `--json`; human-readable summary otherwise.
- filesystem side effects: creates a new run workspace and updates candidate store.
- failure behavior: missing candidate, capability_missing, invalid_plan, tool_* failures.

compare

- intent: compare two run outputs.
- inputs: run_a and run_b paths.
- outputs: comparison JSON on stdout (use `--json` for structured output).
- filesystem side effects: none.
- failure behavior: missing run outputs or malformed files.

inspect-candidate

- intent: read a candidate from the store.
- inputs: candidate_id.
- outputs: candidate JSON on stdout (use `--json` for structured output).
- filesystem side effects: none.
- failure behavior: missing candidate.

export-report

- intent: output a stored report for a run.
- inputs: run_id.
- outputs: report JSON on stdout or written to --output (use `--json` for structured output).
- filesystem side effects: optional output file write.
- failure behavior: missing report.

Module refs: agentic_proteins.interfaces.cli, agentic_proteins.runtime.workspace, agentic_proteins.core.failures.
