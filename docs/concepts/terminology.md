# Terminology

candidate vs version vs run:

- candidate: the biological entity tracked across decisions and tool outputs.
- version: a stored snapshot of a candidate in the candidate store.
- run: the full execution record for a single input sequence.

evaluation vs verification vs critique:

- evaluation: metrics derived from tool outputs and candidate state.
- verification: validation checks on inputs and outputs.
- critique: a decision about whether prior outputs should block continuation.

confidence vs score vs metric:

- metric: a raw numeric output (e.g., mean_plddt).
- score: a ranking value derived from multiple metrics.
- confidence: a bounded [0,1] summary stored on the candidate.

Module refs: agentic_proteins.domain.metrics, agentic_proteins.domain.candidates, agentic_proteins.agents.verification.
