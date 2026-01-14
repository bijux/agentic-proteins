# CLI Workflows

Single protein analysis:

- Inputs: sequence string.
- Commands: agentic-proteins run --sequence <SEQ>
- Artifacts produced: plan.json, execution.json, report.json, state.json, telemetry.json, run_output.json.
- Failure behavior: input_invalid, invalid_plan, tool_* failures, human_decision_missing.

Batch exploration:

- Inputs: multiple sequences in FASTA files.
- Commands: run once per sequence with distinct working directories.
- Artifacts produced: one run workspace per sequence.
- Failure behavior: per-run failures recorded in error.json.

Resume and inspect:

- Inputs: candidate_id.
- Commands: agentic-proteins resume <CANDIDATE_ID> --rounds 1; agentic-proteins inspect-candidate <CANDIDATE_ID>.
- Artifacts produced: new run workspace and updated candidate store.
- Failure behavior: missing candidate, tool_* failures.

Compare runs:

- Inputs: paths to run directories or run_output.json files.
- Commands: agentic-proteins compare <run_a> <run_b>.
- Artifacts produced: none.
- Failure behavior: missing or malformed run outputs.

Module refs: agentic_proteins.interfaces.cli, agentic_proteins.runtime.workspace, agentic_proteins.runtime.control.artifacts.
