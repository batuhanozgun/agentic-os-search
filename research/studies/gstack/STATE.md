# gstack Study — STATE

**Status:** ACTIVE / IN PROGRESS  
**Study type:** external-target  
**User authorization:** broad gstack research and durable repository work authorised through the current operational boundary  
**Pinned target:** `garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`  
**Observed:** 2026-09-05  
**Current phase:** S2 — subsystem reconstruction; **five bounded syntheses complete**  
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

Reconstructs four distinct memory/continuity mechanisms:

```text
A. explicit context checkpoints
B. local sourced/confidence-tagged learnings
C. typed/budgeted/TTL-aware GBrain planning digests
D. trust/privacy/ingest authority controlling persistent brain interaction
```

Key results include:

- context checkpoints are branch/timestamp-qualified handoff summaries, not mechanically revalidated current truth;
- local learnings carry source/confidence/files, age decay for observed/inferred rows, latest-winner semantics and strict cross-project `trusted === true` gating;
- learning ingestion rejects instruction-like suspicious payloads before persistence;
- GBrain planning memory is routed by consumer skill, entity type and byte budget rather than globally injected;
- cache validity depends on TTL, endpoint identity, schema identity and explicit invalidation;
- salience applies a privacy-prefix allowlist before cache persistence;
- per-remote GBrain policy (`read-write` / `read-only` / `deny`) is enforced before transcript-memory writes, with unattended corrupt-policy state failing closed;
- **negative source-fidelity finding:** the cache CLI distinguishes `stale-fallback` and prints that state to stderr, but `generateBrainPreflight()` redirects cache stderr to `/dev/null` and injects only stdout. Planning models can therefore consume stale fallback content **without being told it is stale**;
- some calibration write-back plumbing exists but remains feature/upstream-capability gated at the pinned revision.

## Current cross-subsystem findings

### C1 — gstack is a qualification-driven work system

**Status:** strengthened working hypothesis, not whole-system conclusion.

Across the first five syntheses:

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
```

This pattern appears in behavioral contracts, durable artifacts, runtime capability gates, freshness checks, explicit authority transitions and evidence states.

### C2 — qualification can be recomputed instead of requiring historical ceremony

**Status:** strong cross-source inference.

Examples include ship recomputing current Eng Review standing and browser/ref state requiring fresh observation after state changes. The system often cares more about a current qualified condition than whether a named prior ceremony happened.

### C3 — durable artifacts can become active control inputs

**Status:** strong cross-subsystem inference.

Plans, decisions, QA artifacts, review results, context checkpoints and learnings are rediscovered later and can alter questions, admission, verification, release or investigation behavior.

Their authority varies by artifact type and consumer.

### C4 — authority is explicit and movable

**Status:** strong cross-subsystem inference.

User approval, delegated autoplan decisions, ship overrides, browser token capabilities, repo memory policy and investigate escalation all represent different authority transitions rather than one universal “agent autonomy” state.

### C5 — freshness is object-relative

**Status:** strong synthesis conclusion.

A diff, plan, browser ref, context checkpoint, local learning and brain digest become stale for different reasons. “Recent” alone is not a universal validity criterion.

### C6 — verification/evidence channels are heterogeneous but not uniformly independent

**Status:** strong synthesis conclusion.

Static reasoning, tests, browser observation, specialist agents, cross-model challenge and persistent evidence channels differ in oracle and independence. First-party diversity is valuable but does not automatically create independent verification.

### C7 — failure polarity is deliberately heterogeneous

**Status:** strong synthesis conclusion.

Some conditions hard-deny; some degrade; some require user override; some preserve stale-but-usable data; some fail closed only at unattended authority/data-movement boundaries. Labels such as “gate”, “security” or “memory available” are too coarse without actual continuation semantics.

### C8 — source→view fidelity is an emerging system-level concern

**Status:** strong cross-subsystem conclusion.

Examples now include:

- generated skill output versus template/resolver provenance;
- checkpoint summary versus current repository truth;
- browser evidence ambiguity and stale refs;
- stale security-status removal;
- **GBrain stale state computed upstream but lost before planning consumption.**

The last item is a concrete implementation violation of the system's otherwise strong qualification pattern.

### C9 — “root cause” discipline is useful but can stop at proximate confirmed mechanism

**Status:** strong causal-depth qualification.

Investigate requires evidence and falsification, but not a mandatory second layer explaining prevention/detection/systemic failure.

### C10 — test strength varies materially by subsystem

**Status:** direct coverage conclusion.

Browser/runtime, context and several low-level controls have real behavioral tests. `/investigate` causal ordering has only the generic structural skill floor despite stronger tests for its freeze submechanism. Test existence must not be flattened into one confidence score.

## Verification limits currently protected

- no independent external replication of gstack as a whole;
- cross-model challenge is not automatically independent verification;
- several E2Es are scenario-bounded or approximate production orchestration;
- browser/runtime security has no independent penetration validation;
- live hostile/public ngrok behavior not reproduced by inspected tests;
- optional ML prompt-injection defense is fail-open;
- local audit/permission-hardening include best-effort semantics;
- GBrain semantic correctness is not independently validated;
- restored checkpoint semantics are not automatically revalidated against current source;
- stale GBrain fallback loses its freshness label in the planning preflight view;
- production deploy/canary/retro closure remains unsynthesized;
- four-ground/cross-ground projection remains premature.

## Known cautions / inconsistencies

1. `docs/PROJECT_STRUCTURE.md` is a derived view and contains at least one stale/non-resolving path; actual pinned tree/source wins.
2. Long sources marked `SUBSTANTIAL / CONTINUE` require re-entry before stronger whole-file claims.
3. First-party tests/evals are evidence, not independent external verification.
4. Upstream `main` is fast-moving; all conclusions are pinned-revision conclusions.
5. “Gate,” “required,” “always-on,” “root cause,” “security,” “coverage,” and “memory” must be interpreted from actual control semantics.
6. Pair-agent own-only isolation does not generalize to shared local browser clients.
7. Browser between-call persistence does not imply default headless cross-daemon persistence.
8. Investigate freeze is not a full filesystem sandbox and is host-specific.
9. Investigate text inconsistently refers to three failed hypotheses versus three failed fix attempts.
10. Brain-cache spec comments reference a non-existent `test/autoplan-preflight-budget.test.ts`; equivalent budget assertions exist in current `brain-cache-spec.test.ts` and `skill-preflight-budget.test.ts`. Actual tests win over the stale comment.
11. A warm/stale distinction exists inside the brain cache but the current planning preflight hides non-warm status by suppressing stderr.

## Current coverage gaps

Major unresolved clusters:

- **multi-agent / cross-model coordination — NEXT**;
- guarded-action / CSO security-review mechanisms beyond browser/freeze;
- host adapters / portability fidelity as a dedicated subsystem;
- deploy / canary / production observation / retrospective feedback;
- test/eval/judge/routing/compliance/flake lifecycle;
- repository self-development / generation / update / release mechanisms;
- chronology/evolution stream from changelog/release diffs;
- independent/adversarial validation of selected security, memory and causal-workflow claims.

## Next work

The immediate next native subsystem is **multi-agent / cross-model coordination**.

Research question:

> how does gstack distribute work, authority, context and verification across multiple agents/models while controlling isolation, handoff, result aggregation, cancellation/failure, and shared-state contamination?

Priorities:

1. reconstruct `pair-agent` and browser-pair authority/handoff beyond the already-read browser ceremony;
2. inspect general subagent dispatch/Agent tool patterns and v1.79 stranded-run fix context;
3. inspect `/codex` second-opinion behavior independently of ship's embedded use;
4. inspect how agents receive context/artifacts and whether they inherit or recompute standing;
5. inspect cancellation/timeouts/partial failure and whether parent work can become stranded;
6. distinguish parallelism, specialization, adversarial diversity and actual verification independence;
7. inspect tests/E2Es for production topology rather than inline checklist approximations;
8. track shared browser/memory/worktree/resource isolation;
9. write a bounded multi-agent synthesis before moving to guarded-action or production feedback.

Only after several more native subsystem syntheses should the study begin the four-ground/cross-ground projection.
