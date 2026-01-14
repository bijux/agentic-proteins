# Design Loop

Iterative candidate generation:

- Each iteration runs the pipeline on the current candidate.
- Candidate updates are computed from tool outputs.

Stagnation detection:

- Improvement deltas track score changes between iterations.
- Stagnation window triggers stopping when improvement falls below threshold.

Convergence criteria:

- Convergence failure is set when stagnation stops the loop.
- Max iterations also terminates the loop.

Human-in-the-loop decision points:

- The loop ends before human review.
- Human decisions are enforced after loop completion by runtime control.

Domain-specific examples:

- Low-confidence C-terminal tail: low structured_pct triggers QC rejection, stopping the loop.
- Two candidates with similar scores: Pareto frontier retains both; selection freezes top-N by rank.
- High mean_plddt but low structured_pct: QC rejects despite confidence metric, stopping execution.

Module refs: agentic_proteins.design_loop.loop, agentic_proteins.runtime.control.execution, agentic_proteins.domain.candidates.selection.
