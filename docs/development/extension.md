# Extension

Extension points:

- Add agents under agentic_proteins.agents with explicit schemas.
- Add tools under agentic_proteins.tools with deterministic contracts.
- Add providers under agentic_proteins.providers with metadata and error mapping.

Failure modes:

- Missing schemas or invalid tool requests block agent registration.
- Provider metadata without tool mappings prevents CLI selection.

Module refs: agentic_proteins.agents, agentic_proteins.tools, agentic_proteins.providers.
