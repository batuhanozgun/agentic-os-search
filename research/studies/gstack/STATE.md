# gstack Study — STATE

**Status:** ACTIVE / IN PROGRESS  
**Study type:** external-target  
**User authorization:** broad gstack research and durable repository work authorised through the current operational boundary  
**Pinned target:** `garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`  
**Observed:** 2026-09-05  
**Current phase:** S2 — subsystem reconstruction; **six bounded syntheses complete**  
**Foundation mutation:** NONE / NOT AUTHORISED BY THIS STUDY

## Protected research question

Build a source-grounded model of gstack as an implemented software-development operating system / software factory, then determine what it does across Information, Work, Actors and Environment and how its important mechanisms connect those areas.

The Foundation four-ground frame remains an upper-level projection/comparison frame, not the initial source taxonomy.

## Method

Research units are semantic mechanisms/subsystems, not fixed file batches.

Load-bearing mechanisms are reconstructed from the strongest available combination of:

```text
behavior/policy contract
+ generated/composed instruction surfaces
+ orchestration/helper code
+ runtime capability
+ persistent artifacts/state
+ tests/evals/compliance checks
```

Evidence classes remain distinct:

1. intended policy;
2. implemented composition/runtime contract;
3. structurally pinned contract;
4. behavioral evidence;
5. independent verification — not established for gstack as a whole.

Higher-level syntheses retain source re-entry routes through `SOURCE-LEDGER.md`.

---

## Completed durable subsystem syntheses

### 1 — Planning / specification / work admission

`research/studies/gstack/syntheses/planning-specification-work-admission.md`

Discovery, premise challenge, durable design lineage, CEO/engineering review, `/autoplan` delegated authority, specification, quality/redaction/sink gates, issue/archive and optional isolated execution.

### 2 — Review / QA / ship / delivery qualification

`research/studies/gstack/syntheses/review-qa-ship-delivery-qualification.md`

Review, browser QA, merged-code tests, failure ownership, semantic changed-path coverage, conditional plan completion, fresh pre-landing review, specialist/red-team/adversarial challenge, fix→test→review convergence and PR/release evidence.

### 3 — Browser runtime / security / evidence

`research/studies/gstack/syntheses/browser-runtime-security-evidence.md`

Persistent browser daemon, per-tab state/ref semantics, root/scoped authority, own-only versus shared tab policy, local/tunnel listener separation, deny-default CDP, URL/SSRF/path controls, opt-in persistence, content/prompt-injection defenses, audit/activity evidence and heterogeneous security failure polarity.

### 4 — Investigation / root-cause / debug control

`research/studies/gstack/syntheses/investigation-root-cause-debug-control.md`

Evidence before hypothesis, explicit falsifiable causal claims, 3-strike escalation, Claude-host freeze enforcement, host differences, minimal intervention, regression + fresh original-symptom verification, durable investigation learnings, and the causal-depth limit between local confirmed mechanism and systemic RCA.

### 5 — Memory / learnings / context / GBrain

`research/studies/gstack/syntheses/memory-learnings-context-gbrain.md`

Distinguishes context checkpoints, local sourced/confidence-tagged learnings, typed/budgeted/TTL-aware GBrain planning digests, and trust/privacy/ingest authority. Includes the negative source-fidelity finding that `stale-fallback` state is computed by the cache but hidden from planning consumers because the resolver suppresses stderr.

### 6 — Multi-agent / cross-model coordination

`research/studies/gstack/syntheses/multi-agent-cross-model-coordination.md`

Reconstructs six materially different coordination modes:

```text
A. fresh-context specialization
B. parallel specialist fan-out
C. parallel generative fan-out
D. spawned workflow delegation
E. cross-model challenge
F. remote capability pairing / optional worktree-parallel execution
```

Key results:

- fresh-context separation and model diversity are distinct; same-family Claude subagents are not outside-model verification;
- v1.79 is a causal record of a third recurring stranded-parent failure class after Claude Code changed Agent calls to background-by-default;
- the proximate fix is explicit `run_in_background: false`, but the deeper failure was treating a load-bearing synchronization property as prose/default behavior instead of a first-class dispatch-interface invariant;
- critical `/ship` → `/document-release` delegation has a machine-readable child-result contract, spawned-session decision adaptation, authority subtraction, parent type validation, timeout/cancellation and shared-working-tree reconciliation;
- fresh context does not imply filesystem/worktree/process isolation;
- Review Army parallel fan-out normalizes/fingerprints/deduplicates child findings but same-model specialist agreement remains correlated evidence;
- Autoplan deliberately withholds prior-phase context from Claude subagents while giving accumulated findings to Codex, separating de-anchored reread from integrated outside-model challenge;
- nested Codex is suppressed when already running under Codex because same-model self-review does not provide the intended diversity;
- pair-agent browser-tab isolation is resource-specific and cannot be generalized to ordinary Agent subagents;
- partial failure semantics depend on child criticality: additive reviewers may fail and degrade, while a still-mutating shared-state child can stop parent continuation;
- multi-agent behavioral coverage is heterogeneous: ship docs handoff/spawned gates are strongly exercised, while Review Army's actual parallel topology and Design Shotgun are much more structurally than behaviorally established;
- non-Claude host dispatch fidelity is a known pinned-revision gap: Codex-host ship can still receive Claude-specific Agent-tool instructions it cannot execute.

---

## Current cross-subsystem findings

### C1 — gstack is a qualification-driven work system

**Status:** strengthened working hypothesis, not whole-system conclusion.

Across six syntheses:

```text
Planning/spec
→ qualifies intent before work admission

Review/ship
→ qualifies implementation before delivery

Browser/runtime
→ qualifies capability, effect and evidence at execution boundaries

Investigate
→ qualifies causal explanation before corrective mutation

Memory/context
→ qualifies prior informational state before reuse

Multi-agent coordination
→ qualifies delegation itself:
   context, authority, completion, result validity and failure continuation
```

### C2 — qualification can be recomputed instead of requiring historical ceremony

**Status:** strong cross-source inference.

Current qualified standing often matters more than whether a named prior ceremony occurred. Ship can recompute review standing; browser evidence is invalidated by state change; children can independently recompute findings in fresh contexts.

### C3 — durable artifacts and typed handoffs can become active control inputs

**Status:** strong cross-subsystem inference.

Plans, decisions, QA artifacts, review results, checkpoints, learnings and child JSON results can alter later admission, verification, release or parent continuation.

### C4 — authority is explicit, movable and resource-specific

**Status:** strong cross-subsystem inference.

User approval, delegated autoplan decisions, ship overrides, browser capabilities, GBrain repo policy, investigate escalation and child scope guards are distinct authority transitions rather than one universal autonomy level.

### C5 — freshness is object-relative

**Status:** strong synthesis conclusion.

Diffs, plans, browser refs, checkpoints, learnings, brain digests and child results become invalid/stale for different reasons.

### C6 — evidence diversity is not automatically verification independence

**Status:** strong synthesis conclusion.

Static reasoning, tests, browser observation, same-family fresh subagents and outside-model Codex challenge differ in oracle and common-cause dependence. Agreement is useful but not automatically independent verification.

### C7 — failure polarity is deliberately heterogeneous

**Status:** strong synthesis conclusion.

Some conditions hard-deny, some degrade, some require explicit override, some preserve stale-but-usable information, some continue with partial reviewers, and some stop specifically to avoid uncontrolled shared-state mutation.

### C8 — source→view fidelity is a system-level concern

**Status:** strong cross-subsystem conclusion.

Examples include generated skill vs template/resolver provenance, checkpoint summary vs current source, browser stale refs, removed false-green security state, hidden GBrain stale-fallback state, and child-output data that must not become parent instructions merely because a trusted child produced it.

### C9 — “root cause” can stop at a proximate confirmed mechanism

**Status:** strong causal-depth qualification.

Investigate encourages causal evidence/falsification but does not mandate a prevention/detection/systemic second layer.

### C10 — test strength varies materially by subsystem

**Status:** direct coverage conclusion.

A named E2E can test production topology, a simplified inline approximation or merely output format. Confidence follows the actual oracle/topology, not the filename.

### C11 — coordination correctness includes liveness, not only logical task decomposition

**Status:** strong multi-agent causal conclusion.

The v1.79 recurrence shows that a correct child task is insufficient if parent wait/completion semantics are implicit. Work-system correctness includes timeout, cancellation, duplicate-suppression and reconciliation after partial effects.

### C12 — isolation must name the resource

**Status:** strong corrective conclusion.

Fresh context, browser-tab ownership, worktree separation, filesystem side effects, memory scope and model separation are different properties. No universal “agent isolation” standing exists in the inspected system.

### C13 — multi-agent aggregation is itself a control mechanism

**Status:** strong source observation.

Parent workflows parse, validate, fingerprint, deduplicate, confidence-gate and synthesize child results. Child output is not automatically authoritative parent state.

### C14 — host portability is a distinct validity dimension

**Status:** direct known-gap observation.

A behavior proven on Claude-host Agent semantics cannot be silently generalized to Codex/Factory/OpenClaw/Hermes renders. Dedicated portability research remains necessary.

---

## Verification limits currently protected

- no independent external replication of gstack as a whole;
- same-family fresh-context agents are not independent verification;
- cross-model challenge is not automatically independent verification;
- several E2Es are scenario-bounded or approximate production orchestration;
- Review Army's core parallel Agent topology has weaker behavioral coverage than its structural/checklist coverage;
- a dedicated Design Shotgun production-topology E2E was not found in the targeted search;
- v1.79 foreground semantics are structurally pinned across many carriers but not runtime-enforced by a universal hook at the pinned revision;
- not every foreground child site has Step-18-level timeout/cancellation/reconciliation;
- cross-host subagent dispatch semantics are known incomplete;
- browser/runtime security has no independent penetration validation;
- live hostile/public ngrok behavior was not reproduced by inspected tests;
- optional ML prompt-injection defense is fail-open;
- GBrain semantic correctness is not independently validated;
- restored checkpoint semantics are not automatically revalidated against current source;
- stale GBrain fallback loses its freshness label in the planning preflight view;
- production deploy/canary/retro closure remains unsynthesized;
- four-ground/cross-ground projection remains premature.

---

## Known cautions / inconsistencies

1. `docs/PROJECT_STRUCTURE.md` is a derived view and contains at least one stale/non-resolving path; actual pinned tree/source wins.
2. Long sources marked `SUBSTANTIAL / CONTINUE` require re-entry before stronger whole-file claims.
3. First-party tests/evals are evidence, not independent external verification.
4. Upstream `main` is fast-moving; all conclusions are pinned-revision conclusions.
5. “Gate,” “required,” “always-on,” “root cause,” “security,” “coverage,” “memory,” “agent,” “parallel,” and “independent” must be interpreted from actual control semantics.
6. Pair-agent own-only isolation does not generalize to shared local browser clients or filesystem/worktree isolation.
7. Browser between-call persistence does not imply default headless cross-daemon persistence.
8. Investigate freeze is not a full filesystem sandbox and is host-specific.
9. Investigate text inconsistently refers to three failed hypotheses versus three failed fix attempts.
10. Brain-cache spec comments reference a non-existent `test/autoplan-preflight-budget.test.ts`; equivalent current assertions exist elsewhere. Actual tests win.
11. A warm/stale distinction exists inside brain cache but the current planning preflight hides non-warm status by suppressing stderr.
12. `MULTI-SPECIALIST CONFIRMED` and cross-model consensus are workflow confidence heuristics, not calibrated independent probabilities.
13. Review Army E2Es frequently inline specialist checklists instead of exercising actual parallel child dispatch.
14. Codex-host ship dispatch fidelity has an explicit unresolved TODO at the pinned revision.
15. The v1.79 PreToolUse runtime enforcement follow-up remains TODO; current protection is guidance + structural scanning + selected behavioral E2Es.

---

## Current coverage gaps

Major unresolved clusters:

- **guarded-action / CSO security-review mechanisms beyond browser/freeze — NEXT**;
- host adapters / portability fidelity as a dedicated subsystem;
- deploy / canary / production observation / retrospective feedback;
- test/eval/judge/routing/compliance/flake lifecycle;
- repository self-development / generation / update / release mechanisms;
- chronology/evolution stream from changelog/release diffs;
- independent/adversarial validation of selected security, memory, coordination and causal-workflow claims.

---

## Next work

The immediate next native subsystem is **guarded-action / CSO security-review mechanisms beyond browser/freeze**.

Research question:

> outside the already-synthesized browser security and investigate freeze controls, how does gstack constrain dangerous action, represent security standing, verify candidate vulnerabilities, separate advisory findings from enforced blocks, and decide when uncertainty should deny, degrade, escalate or remain informational?

Priority route:

1. reconstruct `/cso` scan → candidate → fresh verifier → standing/report lifecycle without duplicating the multi-agent analysis;
2. inspect `/careful`, `/guard`, dangerous-operation hooks and other mutation guards;
3. distinguish policy prose from actual runtime deny/enforcement;
4. trace security finding confidence/verification states and false-positive controls;
5. inspect persistence/audit/receipt paths and whether security standing can become stale;
6. inspect host-specific hook loss or advisory substitutions only as required for this subsystem, deferring full portability synthesis;
7. map structural tests versus live behavioral E2Es;
8. write a bounded guarded-action/security-review synthesis before production/deploy feedback or host portability.

Only after several more native subsystem syntheses should the study begin the four-ground/cross-ground projection.
