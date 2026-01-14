# Limits

Operational limits:

- Remote providers are treated as non-deterministic and marked experimental.
- Human-in-the-loop decisions are external inputs; the system records them but does not resolve ambiguity.
- Artifact loss is a hard failure; runtime does not attempt reconstruction from partial state.
- Tool timeouts terminate the active step and emit failure artifacts for review.
- Default tools emit heuristic structure metrics only; no coordinates are produced.

Provider capability matrix:

| Provider | GPU | CPU | External | Deterministic |
| --- | --- | --- | --- | --- |
| heuristic_proxy | no | yes | no | yes |
| local_esmfold | yes | yes | no | yes |
| local_rosettafold | yes | no | no | yes |
| api_colabfold | no | yes | yes | no |
| api_openprotein_esmfold | no | yes | yes | no |
| api_openprotein_alphafold | no | yes | yes | no |

Assumptions:

- Inputs are valid amino acid sequences or validated plan objects.
- Run workspaces are writable and preserved for the full audit window.
- Providers return structured outputs that pass validation contracts.

Module refs: agentic_proteins.providers, agentic_proteins.runtime.workspace, agentic_proteins.runtime.control.artifacts.
