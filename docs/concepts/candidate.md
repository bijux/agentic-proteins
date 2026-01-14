# Candidate

What it is:

- A candidate is the persistent biological object tracked across planning, execution, and review.

Lifecycle:

- Created from an input sequence.
- Updated after tool execution with proxy metrics and optional structure placeholders.
- Versioned and stored in the candidate store.

Invariants:

- Versions are append-only.
- Proxy structure metrics are derived from tool outputs; coordinates are not implied.

Failure semantics:

- Tool failures mark candidate flags.
- Invalid outputs prevent candidate updates.

Module refs: agentic_proteins.domain.candidates, agentic_proteins.domain.candidates.updates.
