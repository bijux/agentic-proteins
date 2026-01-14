# Evaluation and Selection

Metrics used:

- Tool outputs provide structural metrics such as mean_plddt, helix_pct, and sheet_pct.
- Quality control derives QCStatus from structured_pct and mean_plddt thresholds.

Confidence propagation:

- Candidate confidence is updated from tool metrics.
- QC status summarizes acceptance, needs_human, or rejection.

Multi-objective ranking:

- Ranking combines confidence, stability, and novelty.
- Scores are deterministic for identical metrics.

Pareto selection:

- Pareto frontier is computed across candidates.
- Top-N selection freezes candidate IDs for review.

Regression and comparison:

- Evaluation reports are compared across runs with compare_runs.

Domain-specific examples:

- Two candidates with similar scores: Pareto frontier retains both and selection freezes top-N by rank.
- High mean_plddt but low structured_pct: QC rejects due to disorder even if pLDDT is high.

Failure modes:

- Missing metrics yield defaulted confidence values.
- QC rejection stops execution in the coordinator.

Module refs: agentic_proteins.domain.metrics, agentic_proteins.domain.candidates.selection, agentic_proteins.agents.verification.quality_control.
