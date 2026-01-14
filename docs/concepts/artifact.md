# Artifact

What it is:

- An artifact is an immutable payload stored in the run workspace and referenced by state snapshots.

Lifecycle:

- Artifact payload is written and fingerprinted.
- Artifact metadata is stored in the state snapshot.

Invariants:

- Artifact IDs are content-based fingerprints.
- State snapshots reference artifacts by ID only.

Failure semantics:

- Missing artifact files referenced by state are invalid.
- Human decision artifacts require valid signatures.

Module refs: agentic_proteins.runtime.control.artifacts, agentic_proteins.state.schemas.
