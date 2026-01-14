# Artifacts and Provenance

Artifact layout:

- artifacts/<run_id>/artifacts/<artifact_id>.json
- plan.json, execution.json, report.json
- state.json, telemetry.json, run_output.json, run_summary.json
- candidate_selection.json and human_decision.json when required

Immutability:

- Artifact payloads are immutable after write.
- State snapshots reference artifact metadata only.

Signed and fingerprinted data:

- Artifact IDs are content-based fingerprints.
- Human decisions are signed by payload hash.

Reproducing a run:

- Load artifacts by ID from the run workspace.
- Rebuild state snapshots from artifact payloads.
- Compare fingerprints and telemetry fields.

Scientific comparison:

- compare_runs reads run outputs and analysis artifacts.
- Candidate timelines and iteration deltas are compared.

Failure modes:

- Missing artifacts referenced by state invalidate the run.
- Signature mismatches invalidate human decisions.

Module refs: agentic_proteins.runtime.control.artifacts, agentic_proteins.runtime.workspace, agentic_proteins.state.schemas.
