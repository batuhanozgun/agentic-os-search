# gstack Study — INDEX

## Role

Retrieval router for the durable `garrytan/gstack` external-target study.

Read `STATE.md` first for current progress/authorization, `META.md` for epistemic boundary, and `SOURCE-LEDGER.md` for actual read coverage.

## Current study target

`garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`

Observed 2026-09-05; package version 1.79.0.

## Read routes

| Need | Read first | Then |
|---|---|---|
| Current progress / next work | `STATE.md` | relevant synthesis / ledger |
| Scope / authority / freshness | `META.md` | `METHOD.md` |
| Research method | `METHOD.md` | `inventory/STRUCTURE.md` |
| Actual read coverage | `SOURCE-LEDGER.md` | pinned upstream source |
| Planning / work admission | `syntheses/planning-specification-work-admission.md` | ledger → pinned sources |
| Review / QA / ship qualification | `syntheses/review-qa-ship-delivery-qualification.md` | ledger → pinned sources |
| Browser runtime / security / evidence | `syntheses/browser-runtime-security-evidence.md` | ledger → pinned sources |
| Investigation / causal control | `syntheses/investigation-root-cause-debug-control.md` | ledger → pinned sources |
| Memory / learnings / context / GBrain | `syntheses/memory-learnings-context-gbrain.md` | ledger → checkpoint/learning/brain sources |
| Multi-agent / cross-model coordination | not yet synthesized | **current next cluster** |
| Four-ground projection | not yet produced | only after native model stabilizes |
| Cross-ground mechanisms | not yet produced | keep neutral until later Foundation comparison |

## Current durable syntheses

### 1. Planning / specification / work admission

`planning-specification-work-admission.md`

```text
intent
→ discovery / premise qualification
→ approved durable design
→ scope + engineering review
→ executable specification
→ safety / quality / sink gates
→ issue/archive
→ optional isolated execution
```

### 2. Review / QA / ship / delivery qualification

`review-qa-ship-delivery-qualification.md`

```text
implemented branch
→ merged-code tests + ownership
→ semantic changed-path coverage
→ conditional plan completion
→ optional browser verification
→ fresh pre-landing review
→ specialist/red-team/adversarial challenge
→ fix → re-test → re-review
→ evidence-bearing release / PR
```

Key correction: current qualification can be recomputed; a universal historical `review → QA → ship` ceremony is not required.

### 3. Browser runtime / security / evidence

`browser-runtime-security-evidence.md`

```text
browser contract
→ persistent daemon / BrowserManager / TabSession
→ capability + listener + tab + CDP boundaries
→ external effects
→ browser evidence / audit / activity
→ freshness / ambiguity / trust handling
```

Key corrections: own-only tab isolation is contextual, command READ/WRITE labels are not security capability classes, tunnel exposure is structurally narrowed, CDP is deny-default, headless cross-restart persistence is opt-in, and security failure polarity is heterogeneous.

### 4. Investigation / root-cause / debug control

`investigation-root-cause-debug-control.md`

```text
failure
→ evidence
→ explicit causal hypothesis
→ falsification
   ├─ false → revise / 3-strike escalation
   └─ supported → bounded fix
                  → regression + full suite
                  → fresh original reproduction
                  → durable learning
```

Key corrections: causal-before-fix is mainly behavioral contract; Claude Edit/Write freeze is real but partial/host-specific; `root cause` does not guarantee systemic prevention/detection depth; the causal methodology has weaker direct behavioral coverage than freeze.

### 5. Memory / learnings / context / GBrain

`memory-learnings-context-gbrain.md`

```text
prior information
   ├─ context checkpoint
   ├─ local learning
   └─ brain page/cache
        ↓
provenance / confidence / branch / TTL / scope / type
        ↓
trust + privacy + ingest policy
        ↓
consumer-specific retrieval / budget
        ↓
current planning / investigation context
```

Key results:

- checkpoints are continuity summaries, not automatically revalidated current truth;
- local learnings have source/confidence/files, age decay and strict cross-project trusted-only import;
- persistent-learning injection is treated as a memory threat and filtered at log time;
- brain context is typed, TTL/invalidation/endpoint-aware, skill-routed and byte-budgeted;
- salience has a pre-persistence privacy allowlist;
- repo `read-only`/`deny` policy is enforced before transcript-memory writes and unreadable unattended policy state fails closed;
- **negative finding:** `gstack-brain-cache get` knows when it is serving `stale-fallback`, but the planning resolver suppresses stderr and injects only content. The consuming agent can therefore receive stale brain context without a stale label;
- calibration write-back is plumbed/tested but feature/upstream-capability gated at the pinned revision.

## Synthesis ladder

```text
Level 0  pinned source
   ↓
Level 1  source-grounded mechanism records
   ↓
Level 2  semantic subsystem syntheses
   ↓
Level 3  cross-system synthesis
   ↓
Level 4  four-ground projection + neutral cross-ground mechanisms
   ↓
Level 5  compact gstack core model
```

Higher synthesis never removes source re-entry.

## Provisional subsystem map

1. governing ethos / behavioral policy / skill-generation contract;
2. **planning / specification / work admission — done**;
3. **review / QA / delivery qualification — done**;
4. **browser runtime / security / evidence — done**;
5. **investigation / root-cause / debug control — done**;
6. **memory / learnings / context / GBrain — done**;
7. **multi-agent / cross-model coordination — NEXT**;
8. guarded-action / CSO security-review mechanisms;
9. host adapters / portability fidelity;
10. deploy / canary / production observation / retrospective feedback;
11. testing / eval / routing / compliance infrastructure;
12. repository self-development / generation / update / release mechanisms.

These are research clusters, not Foundation categories.

## Immediate next route

Study **multi-agent / cross-model coordination**.

Central question:

> how does gstack distribute work, authority, context, resources and verification across multiple agents/models while controlling isolation, handoff, partial failure, cancellation and shared-state contamination?

Priorities include `pair-agent`, general Agent/subagent dispatch, `/codex`, v1.79 stranded-run fixes, context/artifact inheritance, browser/worktree/memory isolation, failure aggregation and verification-independence limits.

## Guardrails

- Understand gstack-native mechanism before four-ground projection.
- Keep intended policy, implementation, structural pins and behavioral evidence distinct.
- Do not treat first-party tests or cross-model diversity as independent verification by default.
- Interpret “gate”, “security”, “root cause”, “memory”, “agent”, “parallel” and “coverage” from actual control semantics.
- Preserve source/view differences: generated skill vs template, checkpoint vs current source, warm vs stale brain context.
- Do not generalize pair-agent browser isolation to all local agents.
- Treat prior information as qualified/fallible state, not automatic truth.
- Do not mutate Foundation from this candidate study.
- Do not silently substitute current gstack HEAD for the pinned snapshot.
