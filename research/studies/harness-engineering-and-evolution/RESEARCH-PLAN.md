# Research plan — staged assimilation, v0.1

**Date:** 2026-09-12. Campaign remains ACTIVE. This is a revisable dependency plan, not a promise to finish in a fixed number of turns. Several turns may be required for one unit; a unit may split when its mechanisms differ materially.

## Research progression

| Unit | Question and work | Exit evidence / status |
|---|---|---|
| U00 | Identify sources; recover project scope; map each source natively; expose initial validity boundaries | COMPLETE as intake. Note01/Note02, source identities and next question exist. Not full research closure. |
| U01 | Trace Meta-Harness candidate generation, permitted changes, validation, scoring, history and selection in actual source; distinguish framework from output artifact | NEXT. Exact code/caller/result chain, negative paths, evaluator ownership and paper-to-release correspondence. Split U01-A/B if needed. |
| U02 | Critically reconstruct all ten video responsibilities and the evolution loop using primary mechanisms, not only labels | PENDING. Every component has function, inputs/outputs, enforcement limits, interaction and counterexample; ambiguous spoken claims checked against original media. Product examples revalidated rather than assumed current. |
| U03 | Audit three experimental families and comparison claims; recover logs/data/implementations where available | PENDING. Separate classification/OOD, math task/model transfer and coding benchmark discovery; units/budgets/uncertainty/selection leakage resolved or bounded. Primary comparisons with ACE/GEPA and other relevant methods. |
| U04 | Build source-native operating and change models; compare with selected HERMES/GSTACK and other study evidence | PENDING. At least one normal path and one failure/authority/continuity path for each load-bearing family. Existing studies reopened only at needed evidence, preserving their limits. |
| U05 | Challenge the model and candidate explanations; design or execute justified bounded probes | PENDING. Holdouts, rivals, regressions, no-change/simpler alternatives; named untested boundaries. Actual execution optional according to claim, never silently assumed. |
| U06 | Project to current Foundation and separately to SOUL/Development OS | PENDING. Reuse conditions, nontransferable elements, unresolved authority/evaluation decisions and evidence-to-use requirements. No architecture adoption. |
| U07 | Reverse omission/distortion/freshness audit; compact core and retrieval closure | PENDING. Re-enter source regions not used to build the first model; assess whether closure is justified or which units reopen. |

U02 and U03 can exchange order or feed U01. U04 does not wait for all HERMES research to finish: use a pinned, bounded result and keep that study's open boundaries. U06 is not the first time SOUL is considered; it is the point at which project-facing conclusions may become more than hypotheses.

## Immediate U01 source route

Framework pin: `stanford-iris-lab/meta-harness@0cbc31e97c9e6d24232d1dc754827c02e1ec415c`.

1. `ONBOARDING.md` (external contract, not an instruction to execute onboarding).
2. `reference_examples/text_classification/README.md` and its actual directory tree; follow `meta_harness.py` and the real proposer/evaluator/interface paths exposed there.
3. `reference_examples/terminal_bench_2/README.md`, actual tree and search/eval path; determine which evidence represents the paper run and which is cleaned-up reference code.
4. Compare the discovered-output repository at `57fefdb2ff84af3fd81b69d67814acbe69bd0743`: `pyproject.toml`, `agent.py`, `anthropic_caching.py`, actual `prompt-templates/` contents. Its root README and root tree alone have been read so far.

Stop after a coherent source unit; save a caller/symbol map rather than making unverifiable general claims about the full system. Do not run quick starts by default.

## Open questions

| ID | Question | Current route / standing |
|---|---|---|
| Q01 | What is mutable, what is protected, and is protection mechanical or merely prompted? | U01; open, decisive for safe interpretation of end-to-end search. |
| Q02 | Can generated code influence the evaluator, oracle, search data, history or score attribution? | U01; open. Separate process is not automatically independent authority. |
| Q03 | How are candidate code, model/config, task subset, traces and score joined? Can stale results be selected? | U01; open. |
| Q04 | Which parts of the published framework reconstruct the paper experiment, and which are later examples? | U01/U03; root README explicitly calls it cleaned-up code with limited testing. |
| Q05 | Does the selected TerminalBench artifact implement the bootstrap/fallback and inherited control paths as described? | U01-B; no code read or execution yet. |
| Q06 | Are the video's component boundaries useful across work classes, or do they hide cross-cutting responsibilities? | U02/U04; map exists, no universal ten-layer taxonomy accepted. |
| Q07 | Is improvement caused by diagnostic evidence, extra budget, proposer priors, task-specific tuning or selection effects? | U03/U05; paper ablations are relevant but do not settle all alternatives. |
| Q08 | How much evidence supports unseen-task and unseen-model transfer, separately for each experiment? | U03; coding has no task holdout; math reporting ambiguity recorded in Note02. |
| Q09 | What are total proposer/search/evaluation/run-time costs and regression risks? | U03/U05; context and evaluation-count headline metrics are insufficient. |
| Q10 | What distinguishes a good candidate from an accepted operational change, and who can stop or reverse it? | U04/U06; bridge question, not an implemented SOUL decision. |
| Q11 | How do stored sources, traces, summaries and memories retain authority, fidelity and relevance when consumed? | U02/U04/U06; use existing Information/knowledge studies selectively. |
| Q12 | When should a component be removed, a model changed, the objective revised, or no action taken? | U02/U05; counters harness-expansion bias. |
| Q13 | How does bounded local success survive delegation, session restart, environment drift and actual external effects? | U04/U05; HERMES/GSTACK evidence candidates, not yet fresh comparisons. |
| Q14 | What source-native mechanism or rival account is missing from the first synthesis? | U07 and each interim reverse pass. |

## Primary-source expansion queue

Do not open everything at once. For a material comparison, first recover the referenced source rather than repeat the paper's characterization:

- ACE, arXiv:2510.04618 — comparator for context/memory evolution and feedback compression.
- GEPA, arXiv:2507.19457 — comparator for trace-based reflective optimisation; test whether claimed restrictions are intrinsic or implementation-specific.
- Meta Context Engineering, arXiv:2601.21557; MemEvolve, arXiv:2512.18746 — compare what is actually being changed.
- AFlow, arXiv:2410.10762 — workflow search as a rival decomposition.
- Terminus-KIRA/Harbor and task evaluator sources — only as the candidate-to-effect chain requires them.

These are discovered dependency candidates, not already-read evidence. A missing exact experiment artifact may be more important than another survey.

## Revision log

**v0.1, U00:** Sources do not form one ready-made architecture. The video is broad and explicitly provisional; the paper targets code search. Coding search/final evaluation share 89 tasks; the public optimiser release is cleaned up and minimally tested by its own README. Therefore inspect mutability/evaluator/source correspondence first, before expanding a broad feature taxonomy or proposing implementation.

Reopen or change order when source code contradicts prose, a mechanism cannot be reproduced from released artifacts, a stronger rival explains improvement, or a new workload invalidates assumed reuse.
