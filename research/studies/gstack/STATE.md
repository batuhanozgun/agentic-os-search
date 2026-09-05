# gstack Study — STATE

**Status:** ACTIVE / IN PROGRESS  
**Study type:** external-target  
**User authorization:** broad gstack research and durable repository work authorised through the current operational boundary  
**Pinned target:** `garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`  
**Observed:** 2026-09-05  
**Current phase:** S2 — subsystem reconstruction; **eight bounded syntheses complete**  
**Foundation mutation:** NONE / NOT AUTHORISED BY THIS STUDY

## Protected research question

Build a source-grounded model of gstack as an implemented software-development operating system / software factory, then determine what it does across Information, Work, Actors and Environment and how its important mechanisms connect those areas.

The Foundation four-ground frame remains an upper-level projection/comparison frame, not the initial source taxonomy.

## Evidence method

Research units are semantic mechanisms/subsystems. Load-bearing claims distinguish:

1. authored/intended policy;
2. implemented composition/runtime contract;
3. structural tests/pins;
4. behavioral E2E evidence;
5. independent verification — not established for gstack as a whole.

Higher synthesis never removes source re-entry through `SOURCE-LEDGER.md`.

---

## Completed durable subsystem syntheses

1. `syntheses/planning-specification-work-admission.md`
   - discovery → premise qualification → planning/review → spec → work admission.

2. `syntheses/review-qa-ship-delivery-qualification.md`
   - implementation → tests/coverage → review/QA → specialist/adversarial challenge → delivery qualification.

3. `syntheses/browser-runtime-security-evidence.md`
   - persistent browser runtime, capability/tab/listener/CDP boundaries, evidence freshness and security failure polarity.

4. `syntheses/investigation-root-cause-debug-control.md`
   - evidence → falsifiable causal hypothesis → bounded fix → regression/fresh reproduction; strong debugging discipline but not mandatory systemic RCA.

5. `syntheses/memory-learnings-context-gbrain.md`
   - checkpoints, sourced/decayed learnings, typed/TTL/budgeted GBrain context, trust/privacy/ingest controls; negative finding: `stale-fallback` status is lost before planning consumption.

6. `syntheses/multi-agent-cross-model-coordination.md`
   - fresh-context specialization, parallel fan-out, spawned workflow delegation, Codex outside-model challenge, remote pairing, liveness/partial-failure semantics; negative findings include implicit-dispatch recurrence and non-Claude host mismatch.

7. `syntheses/guarded-action-security-review.md`
   - preventive tool interposition, one-way decision authority, CSO detective/advisory qualification, and host-dependent enforcement strength.

8. `syntheses/host-adapters-portability-fidelity.md`
   - typed host adaptation, generation/compilation, model overlays, setup/runtime materialization and host-specific verification standing.

### Portability synthesis — key results

```text
canonical skill/resolver source
→ HostConfig + model overlay
→ preserve / rewrite / suppress / inline / advisory / unsupported
→ generated host artifact
→ install + runtime assets
→ actual host capability
→ host-specific behavioral evidence
```

Important corrections:

- the pinned registry has ten hosts, but registry membership is not one uniform support level;
- first-class setup install arms exist for Claude, Codex, Kiro, Factory, OpenCode and Cursor;
- Slate is explicitly not yet first-class; OpenClaw/Hermes use methodology/instruction-tier integration; GBrain is a separate mod/integration surface;
- `host != model`; model overlays are an independent behavioral dimension;
- generator-level all-host freshness, YAML/path/frontmatter checks and golden fixtures establish strong generated-surface coherence, not runtime behavioral equivalence;
- Claude carved sections remain lazy/on-demand files while external hosts inline section content into monolithic skills — content can be preserved while context-loading topology changes;
- Claude safety hooks can degrade to external-host Safety Advisory prose; this preserves intent but not enforcement strength;
- Codex has the strongest inspected external-host behavioral harness, yet a known ship Agent-dispatch instruction remains semantically invalid on Codex;
- `docs/ADDING_A_HOST.md` overstates declarative maturity: it says setup/tooling require zero host-specific code, while canonical `host-config-export.ts` explicitly says setup is **not yet wired** to the registry and still hand-rolls host lists;
- actual setup contains duplicated per-host runtime-root/link functions; `TODOS.md` records their independent drift risk;
- `skill-check` can report generated external-host files fresh/valid even when the host is not first-class install/runtime supported;
- Codex periodic CI has a known false-green all-skip defect because the CI image lacks the Codex CLI;
- targeted searches found no comparable real-host behavioral runner for Factory/Kiro/OpenCode/Cursor; strongest inspected evidence there is generation/setup/static correctness;
- portability standing therefore must name host, model, capability, install/runtime topology and verification level.

---

## Current cross-subsystem findings

### C1 — gstack is a qualification-driven work system
**Status:** strengthened working hypothesis, not whole-system conclusion.

```text
Planning/spec        → qualifies intent before admission
Review/ship          → qualifies implementation before delivery
Browser/runtime      → qualifies capability, effect and evidence
Investigate          → qualifies causal explanation before corrective mutation
Memory/context       → qualifies prior information before reuse
Multi-agent          → qualifies delegation, completion and child evidence
Guarded/security     → qualifies effect authority and security claims
Host portability     → qualifies whether a workflow/control still means the same thing on a target host/model/runtime
```

### C2 — qualification can be recomputed; ceremony history is secondary
Current standing often matters more than prior named ceremony. Browser refs, diff reviews, security evidence, child results and host-render validity have distinct invalidation conditions.

### C3 — artifacts and typed representations can become active control inputs
Plans, reports, decisions, checkpoints, learnings, child JSON and generated host skills alter later work. Their authority is consumer-, freshness- and runtime-specific.

### C4 — authority is explicit, movable and resource-specific
User approval, delegated decisions, runtime capabilities, GBrain policy, one-way doors, child scope guards and escalation are different authority relations.

### C5 — freshness is object-relative
Diff, plan, browser state, checkpoint, learning, brain digest, child result, security report and generated host render become stale for different reasons.

### C6 — evidence diversity is not automatically verification independence
Same-family fresh agents, Codex, tests, browser observation and CSO verifiers share varying common causes/oracles. Agreement is useful, not automatic independent verification.

### C7 — failure polarity is deliberately heterogeneous
Depending on mechanism, uncertainty can deny, ask, degrade, preserve stale state, suppress a claim, continue with partial evidence, stop to prevent uncontrolled mutation, or render a host feature unsupported.

### C8 — source→view fidelity is system-level
Known examples: generated skill vs template/resolver, checkpoint vs current source, browser stale refs, false-green security state, hidden GBrain stale label, child data vs parent instruction, historical CSO report vs current security truth, and stale/aspirational host documentation vs actual setup implementation.

### C9 — causal depth remains bounded
`/investigate` can terminate at a confirmed proximate mechanism; v1.79 multi-agent analysis demonstrates why recurrence/prevention/detection layers sometimes require deeper RCA.

### C10 — test names do not imply equal verification strength
Some E2Es reproduce production topology; others inline checklists, test presentation, skip on missing runtimes or validate only generated structure. Confidence follows actual oracle/topology/execution.

### C11 — work-system correctness includes liveness
Parent/child wait, timeout, cancellation, duplicate suppression and partial-effect reconciliation are correctness properties.

### C12 — isolation must name the resource
Fresh context, browser tab, worktree, filesystem, memory and model separation are distinct.

### C13 — aggregation is itself control
Child/security findings are parsed, filtered, validated, deduplicated and status-qualified before affecting parent/user decisions.

### C14 — host portability is a distinct validity dimension
A rule proven on Claude hooks/Agent semantics cannot be silently generalized to Codex/Factory/OpenClaw/Hermes or other hosts.

### C15 — prevention, authority and detection are different security layers
A warning/deny hook, a mandatory human confirmation, and a CSO finding have different effects and must remain separate.

### C16 — host capability can downgrade enforcement to advice
The careful/freeze/guard external render is concrete: runtime interposition on Claude becomes prose self-policing.

### C17 — support is a ladder, not a boolean
**Status:** strong portability conclusion.

```text
registered
< generated
< structurally valid
< installable
< runtime-capable
< workflow-executed
< failure-path exercised
< independently validated
```

Different gstack hosts occupy different positions. A single `supported=true` or “green generation” label is insufficient.

### C18 — host adaptation is compilation plus capability negotiation
**Status:** strong synthesis conclusion.

Literal path/tool rewriting is adequate only when semantics are equivalent. Agent dispatch, hooks, user-question gates, memory integration and runtime assets require explicit capability-sensitive adaptation: preserve, replace with native primitive, inline, suppress, degrade visibly, or declare unsupported.

### C19 — repository self-description can outrun implementation
**Status:** direct source-fidelity finding.

`docs/ADDING_A_HOST.md` says setup/tooling are fully config-driven; `host-config-export.ts`, `setup` and `TODOS.md` show they are not. Derived architecture docs must not be used as sole evidence for current implementation standing.

### C20 — test execution itself needs standing
**Status:** direct verification-validity finding.

A configured E2E shard is not evidence of execution. Codex periodic CI can report green after skipping everything because the required CLI is absent. Verification systems need proof that the intended oracle actually ran.

---

## Protected verification limits

- no independent external replication of gstack as a whole;
- same-family subagents and cross-model challenge are not automatically independent verification;
- Review Army production parallelism has weaker behavioral coverage than structural/checklist coverage;
- foreground Agent semantics are not universally runtime-enforced at the pinned revision;
- cross-host subagent dispatch fidelity is incomplete;
- careful regex classification is not a complete shell semantic parser/sandbox;
- careful/freeze/guard enforcement does not port unchanged to external hosts;
- CSO confidence scores are authored calibration heuristics, not externally validated probabilities;
- CSO does not automatically gate delivery and historical reports do not prove current security;
- browser/runtime security has no independent penetration validation;
- GBrain semantic correctness is not independently validated;
- stale GBrain fallback loses its freshness label in planning view;
- non-Claude host behavioral validation is sparse outside Codex;
- Codex periodic CI has a known all-skip false-green;
- targeted searches did not establish dedicated real-host E2E runners for Factory/Kiro/OpenCode/Cursor;
- setup remains partly host-hardcoded despite the typed registry;
- production deploy/canary/retro closure remains unsynthesized;
- four-ground/cross-ground projection remains premature.

---

## Known cautions

1. Derived docs never override pinned source/tree.
2. `SUBSTANTIAL / CONTINUE` sources require re-entry for stronger whole-file claims.
3. First-party tests/evals are evidence, not external independent verification.
4. All conclusions are pinned-revision conclusions; upstream is fast-moving.
5. Terms such as gate/security/root-cause/memory/agent/parallel/independent/isolation/read-only/support/portable must be interpreted from actual control semantics.
6. Pair-agent own-only isolation is browser-tab-specific.
7. Investigate freeze is not a full filesystem sandbox and is host-specific.
8. GBrain warm/stale distinction is lost in current planning preflight representation.
9. Multi-specialist/cross-model agreement is a workflow heuristic, not calibrated independence.
10. Codex-host ship has a known Agent-dispatch fidelity gap.
11. `/careful` HIGH deny is session-scoped and explicitly not a universal policy boundary.
12. `/guard` does not make Bash filesystem mutations obey the freeze Edit/Write boundary.
13. CSO code “read-only” behavior is not enforced by a source-write capability sandbox.
14. Historical CSO report presence is not current security proof.
15. `docs/ADDING_A_HOST.md` is stale/aspirational where it claims setup is already fully config-driven; canonical implementation/TODO wins.
16. Host registry membership is not evidence of a first-class install path or runtime behavior.
17. Generated-host freshness is not behavioral portability proof.
18. A green test lane that skipped its actual runtime is not positive verification evidence.

---

## Current coverage gaps

- **deploy / canary / production observation / retrospective feedback — NEXT**;
- test/eval/judge/routing/compliance/flake lifecycle;
- repository self-development / generation / update / release mechanisms;
- chronology/evolution stream from changelog/release diffs;
- independent/adversarial validation of selected security, memory, coordination, portability and causal-workflow claims.

---

## Next work

The immediate next native subsystem is **deploy / canary / production observation / retrospective feedback**.

Research question:

> after code is reviewed/shipped, how does gstack move changes toward deployment, qualify rollout state, observe production behavior, decide rollback/continuation, connect incidents or outcomes back into future work, and preserve evidence across that feedback loop?

Priority route:

1. reconstruct `/land-and-deploy`, `/canary`, `/health`, `/retro` and deployment setup surfaces;
2. distinguish merge, deploy, release and production-success standing;
3. inspect one-way authority gates for merge/rollback/irreversible actions;
4. trace production observation/evidence sources and freshness;
5. inspect canary thresholds, failure polarity, rollback semantics and manual/provider-specific gaps;
6. determine whether retrospective learnings actually feed later work or are only reports;
7. inspect behavioral tests/evals and false-green risks;
8. write a bounded production-feedback synthesis before the dedicated test/eval infrastructure cluster.
