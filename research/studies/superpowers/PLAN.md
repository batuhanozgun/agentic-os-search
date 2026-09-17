# Superpowers Study — Plan v0.4

Date: 2026-09-17. Method remains [METHOD.md v0.1](METHOD.md). Current work/authorization belongs to [STATE.md](STATE.md).

## Main question

How do shared skill instructions, host-specific delivery/tool mappings, work artifacts and verification mechanisms compose into Superpowers' development methodology, and where do their guarantees stop?

Units remain provisional research questions, not the target's final architecture. A unit may span sessions; a session may close more than one bounded unit. File count and token consumption are not completion criteria.

## Investigation units

| Unit | Question and main surfaces | Required bounded output / current direction |
|---|---|---|
| U00 — Corpus and orientation | Exact target, root/skills trees, README, manifests, runtime/test/docs families. | Pin and progressive read ledger exist. Selected subtrees only; not recursive whole-repository coverage. |
| U01 — Entry, discovery and host delivery | Bootstrap, hooks/config/wrapper, native discovery, adapters/tool references/tests, startup versus compaction. | Bounded source model complete after U01-A/B; host/cache/failure limits retained. Not full host qualification. |
| U02 — Intent, scope, approval and planning | Brainstorming, planning, worktrees, spec/plan/workspace and execution entry. | Bounded source/helper complete: phase authority, artifact map, ledger identity, requirement transfer/materialization, E05/E06. |
| U03 — Execution and delegation | SDD, executing-plans, parallel dispatch, implementer/review templates, review packaging. | Bounded source/helper complete: one two-verdict task reviewer, evidence packets, scoped corrections, qualified completion, role/context/parallelism boundaries; F20–F27 and E07/E08. Not live actor behavior. |
| U04 — Evidence, testing and correction | TDD, debugging, receiving review, verification-before-completion, supporting guidance/tests. | NEXT: expectation/oracle, actual observations, claimed evidence, report/revision binding, correction and completion claims. Reuse U03 review topology rather than repeating it. |
| U05 — Delivery and lifecycle | Finishing branch, worktree provenance, merge/PR/test/cleanup and destructive actions. | Delivery transitions, current-result checks, unresolved-finding disposition and durable retention of rulings/evidence. |
| U06 — Skill authoring and evolution | Writing-skills, contributor docs, tests/evals/CI/release sources; separately pinned external evaluation. | Behavioral criteria, oracle freshness, regression, ownership and distribution. Description-predicate probes do not close this unit. |
| U07 — Supporting runtime and distribution closure | Visual companion, server/client/assets, installation/update/packaging, remaining adapters/telemetry. | Runtime/dependency/trust boundaries and coverage review; resolve stale examples and uninvestigated host routes. |
| U08 — Composition, projection and closure | Native subsystem/cross-system model, then current Foundation and selected comparison sources. | Subsystem syntheses → cross-system model → four-ground/cross-boundary projection → CORE → reverse-source/freshness challenge. Not begun. |

## Completed bounded units

**U01-A:** exact shell probes and entry contract; four transport successes, two failed study-defined health criteria and one negative control. [Original note](notes/U01-entry-routing-and-bootstrap.md).

**U01-B:** completed porting guide, 17 new full reads, host matrix, F07–F12 and exact OpenCode experiment. Module/session/source and semantic-health limits remain explicit. [Note](notes/U01B-host-delivery-and-continuity.md).

**U02:** S10 re-read and nine new full files S28–S36; F13–F19, artifact/transition map, exact workspace/task-brief helpers and a literal ignore predicate. Thirteen cases included two failed health criteria. Review sources read for U02 were not treated as completed U03 at that time. [Note](notes/U02-approval-plan-workspace-handoff.md).

**U03:** seven additional full files S37–S43; direct re-entry of S30 review/fix sections and S34. [Note](notes/U03-delegation-review-and-acceptance.md) records role/packet/acceptance topology, F20–F27, source composition seams and E07/E08. Nine cases: seven expected helper/scope/control observations, two failed verbal-oracle alignment criteria. No agent/model, real approval, installation or upstream suite was run.

The old [SOURCE-LEDGER.md](SOURCE-LEDGER.md) retains S00–S36/E01–E06 unchanged. [SOURCE-LEDGER-U03.md](SOURCE-LEDGER-U03.md) adds S37–S43/E07–E08 and updates current source topology. The split preserves evidence rather than resetting read status.

## Next concrete sequence — U04

1. Recover STATE's current cold-start, including the U03 ledger supplement and full U03 note. Preserve completion-with-parked-findings, reviewer-coverage and exact-range distinctions.
2. Fully read pinned `skills/test-driven-development/SKILL.md` and follow the actual supporting test-guidance reference. Do not assume an older anti-pattern filename still exists; confirm through the pinned tree.
3. Fully read pinned `skills/systematic-debugging/SKILL.md`, `skills/verification-before-completion/SKILL.md` and `skills/receiving-code-review/SKILL.md`. Follow their load-bearing supporting techniques without turning every historical example into a mandatory new study.
4. Trace intended behavior → expected result/oracle → observed test/failure → report/evidence → diagnosis/correction → current completion claim. Distinguish test-before-code discipline from the test's actual error sensitivity and target coverage.
5. Reconcile reuse of implementer evidence in U03 with fresh verification before success claims. Determine what identifies the tested code, environment, command/output and any subsequent changes. A report can exist while its applicability has expired.
6. Inspect selected test/evaluation surfaces when needed to distinguish mechanisms. S42's description test is not behavioral evaluation. A narrowly safe local check is optional when it resolves a consequential uncertainty; do not create a ceremonial test for prose.
7. Preserve questions requiring live model/host or broader external eval access as explicit limits. U05 retains final delivery/retention; U06 retains skill-evaluation architecture and criterion freshness.
8. Return a bounded source result with durable source/evidence/STATE updates. No installation, upstream issue or architecture/adoption phase follows automatically.

## Method/plan evolution record

### v0.1 — establishment

- Adopt gstack's source-grounded synthesis method without its subsystem taxonomy/conclusions.
- Replace the introductory linear workflow with the actual three-path contract.
- Split shared skill content from host-dependent delivery; distinguish output envelopes from usable bootstrap.

### v0.2 — U01-B refinement

- Separate description visibility, full-body delivery, invocation, tool mapping and re-entry.
- Separate source revision, module lifetime, session events and message arrays.
- Tool mapping can change actor/context/task semantics, not just names.
- Procedure re-entry versus work recovery motivates U02 without implying whole-system absence.
- Q09–Q12 retain host/module, marker, Hermes aliases and distribution seams; no compulsory live-host campaign.

### v0.3 — U02 refinement

- SDD ledger/artifacts establish a work-recovery mechanism; identity/revision limits remain.
- Phase/route authority differs: brainstorming approval, SDD rulings and inline escalation.
- Read instructions, helper and receiving workspace together; neither prose nor scripts alone explain consent and transfer.
- Distinguish full plan path, plan revision, task brief and completion state; retain the ledger-header safeguard alongside basename collisions.
- Task extraction does not automatically carry globals; controller information transfer becomes a U03 question.
- Failed local health criteria remain failed; descriptive observations are not safety certificates.

### v0.4 — U03 refinement

- Replace the introductory two-stage/two-seat assumption with the actual one-reviewer/two-verdict task topology and separate scoped/final reviews.
- Separate reviewer detection from controller acceptance: DONE, clean review, parked completion and merge readiness are not synonyms.
- Evaluate efficiency controls as trade-offs: bounded context, reused evidence and fix caps are not proof of preserved coverage or correctness.
- Follow exact artifact consumers: a successful Git packet is only as task-complete as the caller's BASE, and committed endpoints do not describe uncommitted test state.
- Test one verbal predicate against current source obligations rather than equating a test's existence with valid assurance; keep constructed-answer results distinct from live model outcomes.
- Add an incremental source-ledger volume to avoid retranscribing prior source identities. Current STATE/INDEX route to both volumes; logical evidence lineage and full-read status are preserved.
- METHOD v0.1 and whole-study closure criteria remain unchanged. These are evidence-led plan/representation refinements, not independent validation of this research method.

## Return conditions and protected scope

Return each round after a meaningful bounded result and durable handoff. Use a working question queue rather than fixed session quotas or empty future syntheses.

Only this package and necessary library discovery entries may change. Foundation, other study content, Development OS, agent-control and upstream Superpowers are protected. Cross-study questions are candidate reuse work, not implementation authority.

No background work is scheduled. STATE owns where a subsequent authorised research turn resumes.
