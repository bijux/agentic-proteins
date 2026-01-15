# HTTP API Schema

The API schema is defined in `agentic_proteins.api.v1.schema` and mirrors the CLI JSON payloads.

Core models:

- `RunRequest`: run a sequence with CLI-aligned options (includes optional `ground_truth`).
- `RunResponse`: run summary payload (same as `run_summary.json`).
- `ResumeRequest`: resume by `run_id` or `candidate_id`.
- `InspectResponse`: candidate metrics, artifacts, and QC status.
- `CompareRequest` / `CompareResponse`: comparison report (same as CLI compare).
- `ErrorResponse`: standardized error shape.

Key fields present in run/resume responses:

- `run_id`, `candidate_id`, `command`
- `execution_status`, `workflow_state`, `outcome`
- `provider`, `tool_status`, `qc_status`
- `artifacts_dir`, `warnings`, `failure`, `version`

Enums are imported from core (`agentic_proteins.core.status` and `agentic_proteins.core.failures`) so their names match the runtime.

Error payloads (RFC 7807 style):

- `type`: URI identifying the problem type
- `title`: short summary
- `status`: HTTP status code
- `detail`: human-readable explanation
- `instance`: request URL

Module refs: agentic_proteins.api.v1.schema.
