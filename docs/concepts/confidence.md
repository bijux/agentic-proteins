# Confidence

What it is:

- Confidence is a structured summary of candidate quality derived from tool metrics and QC evaluation.

Lifecycle:

- Tool outputs update candidate confidence.
- QC status reflects confidence thresholds.

Invariants:

- Confidence values are bounded in [0, 1].
- Updates are derived from deterministic tool outputs.

Failure semantics:

- Missing or invalid metrics degrade confidence updates.
- QC rejection flags low-confidence candidates.

Module refs: agentic_proteins.domain.metrics.quality, agentic_proteins.domain.candidates.updates.
