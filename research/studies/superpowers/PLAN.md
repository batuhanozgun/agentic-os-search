# Superpowers Study — Plan v0.1

Date: 2026-09-17. Scope and method: [METHOD.md](METHOD.md). Current execution state and authorization: [STATE.md](STATE.md).

## Main question

How do shared skill instructions, host-specific delivery/tool mappings, work artifacts and verification mechanisms compose into Superpowers' development methodology, and where do their guarantees stop?

The units below are provisional research questions, not a declaration of the target's final architecture. A unit can span several sessions; a session can close more than one bounded unit. File count and token consumption are not completion criteria.

## Investigation units

| Unit | Question and main surfaces | Required bounded output |
|---|---|---|
| U00 — Corpus and orientation | What is the exact target? Root and skills trees, README, manifests, documentation/runtime/test families. Expand subtrees as subsequent questions require. | Pinned source identity, native source map, read ledger, scope and open coverage. Initial root-level map is not recursive completeness. |
| U01 — Entry, discovery and host delivery | How do instructions become available and get selected? `using-superpowers`, hook configurations/scripts/wrappers, native skill discovery, tool references and relevant adapter implementations/tests. Separate startup and compaction. | Delivery/selection chain; procedural versus executable controls; host-difference matrix; capability gaps and evidence limits. |
| U02 — Intent, scope, approval and planning | How do spike/bounded/architectural requests differ? `brainstorming`, `writing-plans`, `using-git-worktrees`, helper references and resulting spec/plan/workspace artifacts. | Request-to-work state transitions, approval boundaries, artifact identities and invalidation/reclassification behavior. |
| U03 — Execution and delegation | How do `subagent-driven-development`, `executing-plans` and `dispatching-parallel-agents` allocate work and context? Read their prompt templates and related reviewer surfaces. | Controller/implementer/reviewer contracts, context packets, parallelism/conflicts, fallback, resumption and completion handoffs. |
| U04 — Evidence, testing and correction | What do TDD, systematic debugging, requesting/receiving review and verification-before-completion actually require and verify? Include supporting test guidance and representative actual tests/evals. | Intended quality loop versus implemented checks; oracle/independence limits; failure/recovery paths; evidence-to-verdict binding. |
| U05 — Delivery and lifecycle | What makes work ready to merge or hand over? `finishing-a-development-branch`, worktree provenance, merge/PR/test/cleanup paths, explicit destructive-action handling and persistent artifacts. | Delivery transitions, actual-result checks, cleanup authority, unsuccessful merge/test paths and continuity boundaries. |
| U06 — Skill authoring and evolution | How are skills written, challenged, revised and distributed? `writing-skills`, contributor docs, relevant tests/evals/CI/release surfaces; separately pin external evaluation dependencies if needed. | Skill-change lifecycle, behavioral evaluation criteria, evidence quality, regression/freshness and maintenance ownership. |
| U07 — Supporting runtime and distribution closure | Which supporting regions would a skill-only model miss? Optional visual companion, assets/server/client paths, installation/update/packaging, remaining adapter families and telemetry-related implementation. | Native subsystem coverage review; runtime/dependency/trust boundaries. Installation or network behavior remains source-only unless separately tested. |
| U08 — Composition, projection and closure | How do the recovered subsystems form one system? What can later SOUL/Development OS work reuse or reject? Re-enter current Foundation and selected study sources at this stage. | Subsystem syntheses → cross-system model → four-ground and cross-boundary projection → CORE → reverse-source omission/freshness audit. |

## U01 split established in the first round

**U01-A:** inspect and probe the exact shell hook's output mechanism; inspect its registration, bootstrap instruction contract, first-party test oracle and the Codex manifest contrast. This is a bounded transport/script question.

**U01-B:** recover the remaining delivery/selection chain: wrapper invocation; native discovery versus full-context injection; tool mapping; at least the materially distinct in-process/instructions-file paths; startup versus post-compaction behavior. Finish the porting guide and read actual selected adapter implementations before closing U01.

The absence of a real host/model run remains a declared boundary, not something that may be closed by inspecting another manifest. Do not make real-host product qualification a hidden prerequisite for every later source unit.

## Next concrete research sequence

1. Re-enter STATE, METHOD, this plan, SOURCE-LEDGER and the U01 note.
2. Complete the porting guide beyond line 310, then inspect the named live wrapper/adapter/tool-reference paths. Use the current pinned tree to confirm paths before fetching guessed implementations.
3. Build a matrix separating file presence, bootstrap delivery, native discovery, invocation, compaction recovery and model compliance; put each observation at its actual evidence level.
4. Close only the source-covered part of U01, preserving live-execution limits; proceed to U02's artifact/approval handoffs. The brainstorming SKILL.md has already been read completely and need not be treated as unseen.

## First-round changes from the conversational sketch

- The README-level linear workflow is insufficient: the actual brainstorming contract has three paths with different outputs and artifacts. Plan expansion must follow branches, not force every task through a written specification and plan.
- A shared skill body does not imply one delivery mechanism on every host. The shell-hook and Codex manifest contrast makes host-conditioned analysis necessary.
- Successful hook output is not sufficient bootstrap-readiness evidence. The local missing/empty-file challenges are recorded as failed study-defined health criteria; they do not establish a production incident or general model failure.

## Return conditions and scope protection

Return each round after a meaningful bounded result and durable handoff are available. Maintain a working question queue instead of manufacturing a fixed number of sessions.

Do not modify Foundation, gstack, Hermes, Development OS, agent-control or upstream Superpowers as a consequence of this research. Cross-study/architecture questions discovered during reading are candidate future reuse work, not implicit implementation authorization.

No work is scheduled in the background. STATE describes where a subsequent authorised research turn resumes.
