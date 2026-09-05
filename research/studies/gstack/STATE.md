# gstack Study — STATE

**Status:** ACTIVE / IN PROGRESS  
**Study type:** external-target  
**User authorization:** broad gstack research and durable repository work authorised through the current operational boundary  
**Pinned target:** `garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`  
**Observed:** 2026-09-05  
**Current phase:** S2 — subsystem reconstruction; **nine bounded syntheses complete**  
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

Higher synthesis never removes source re-entry through `SOURCE-LEDGER.md` and the pinned upstream source.

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

9. `syntheses/deploy-canary-production-retrospective-feedback.md`
   - release-readiness → merge authority/state → deploy standing → live verification → extended canary → revert → operational history/retro feedback.

---

## Production-feedback synthesis — key results

```text
qualified PR
→ readiness evidence
→ one-way human merge authority
→ authoritative merge state
→ deploy strategy + completion evidence
→ immediate live verification
→ optional extended canary
→ deploy/canary history
→ retro/trends/learnings
→ recommendation / candidate future work
```

Important corrections:

- merge command result and actual GitHub merge state are deliberately separated; after any non-zero merge mutation the workflow reads authoritative PR state and does not retry blindly;
- merge queue is an intermediate standing, not “merged”;
- GitHub Actions deploy evidence can be bound to merge SHA; URL/platform-CLI auto-deploy strategies have weaker/heterogeneous release-identity proof;
- deploy completion and live health are separate standings;
- `/land-and-deploy` performs single-pass verification, while `/canary` provides bounded longitudinal monitoring;
- Canary is a relative-regression monitor only when a genuine pre-deploy baseline exists; without one, the skill correctly reduces its meaning to a health check;
- Canary baseline/report schemas do not bind observation to merge SHA/deployment ID, so live health is stronger evidence than exact-release identity;
- merge and rollback decisions are typed `one-way` doors; automation preferences cannot silently suppress human confirmation;
- readiness text says failing free tests are a `BLOCKER` / “Cannot merge,” but its final decision menu still exposes “merge anyway” and only recommends holding when blockers exist. The inspected source therefore does not establish a deterministic non-overridable failed-test merge block;
- rollback closure is incomplete: after revert commit/push, the workflow can report `REVERTED` without mandatory wait-for-revert-deploy + post-rollback canary proving production restoration;
- `/health` is code-quality health, not production health;
- Retro has explicit stale-base/today-anchor guards, saves `.context/retros/*.json`, compares trends and can feed learnings/GBrain context;
- Retro recommendations/habits are informational feedback, not automatically admitted work or Actor obligation;
- `test/skill-e2e-deploy.test.ts` uses a real agent but explicitly **simulates** GitHub merge, provider deployment and Canary browser behavior; it is not a live production integration test;
- Canary has a coverage-routing inconsistency: a `canary-workflow` scenario exists in the deploy E2E file and touchfile tier data, while the canonical skill coverage matrix attributes Canary only the generic structural floor.

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
Host portability     → qualifies semantic/control fidelity on target host/model/runtime
Production feedback  → qualifies merge, deploy, live health and historical outcome separately
```

### C2 — qualification can be recomputed; ceremony history is secondary
Current standing often matters more than prior named ceremony. Reviews, tests, browser refs, deploy config, deployment evidence and retro histories have distinct invalidation conditions.

### C3 — artifacts and typed representations can become active control inputs
Plans, reports, decisions, checkpoints, learnings, child JSON, generated host skills, deploy config and review/evidence ledgers alter later work. Their authority is consumer-, freshness- and runtime-specific.

### C4 — authority is explicit, movable and resource-specific
User approval, delegated decisions, runtime capabilities, GBrain policy, one-way doors, child scope guards, merge/rollback approvals and escalation are different authority relations.

### C5 — freshness is object-relative
Diff, plan, browser state, checkpoint, learning, brain digest, child result, security report, host render, deploy config and retro data become stale for different reasons.

### C6 — evidence diversity is not automatically verification independence
Same-family fresh agents, Codex, tests, browser observation, CSO verifiers and production probes share varying common causes/oracles. Agreement is useful, not automatic independent verification.

### C7 — failure polarity is deliberately heterogeneous
Uncertainty can deny, ask, degrade, preserve stale state, suppress a claim, continue with partial evidence, stop mutation, allow an explicit human override or declare a host/provider unsupported.

### C8 — source→view fidelity is system-level
Known examples: generated skill vs template/resolver, checkpoint vs current source, browser stale refs, false-green security state, hidden GBrain stale label, child data vs parent instruction, historical report vs current state, stale host docs vs setup implementation, deployment report vs current production truth.

### C9 — causal depth remains bounded
`/investigate` can terminate at a confirmed proximate mechanism; v1.79 and rollback closure show why prevention/detection/restoration layers sometimes require deeper RCA.

### C10 — test names do not imply equal verification strength
Some E2Es reproduce production topology; others inline/simulate dangerous effects, test presentation, skip on missing runtimes or validate generated structure. Confidence follows actual oracle/topology/execution.

### C11 — work-system correctness includes liveness
Parent/child wait, timeout, cancellation, merge queue polling, deploy waiting and partial-effect reconciliation are correctness properties.

### C12 — isolation must name the resource
Fresh context, browser tab, worktree, filesystem, memory and model separation are distinct.

### C13 — aggregation is itself control
Child/security/release findings are parsed, filtered, validated, deduplicated and status-qualified before affecting parent/user decisions.

### C14 — host portability is a distinct validity dimension
A rule proven on Claude hooks/Agent semantics cannot be silently generalized across hosts.

### C15 — prevention, authority and detection are different security layers
A warning/deny hook, mandatory human confirmation and security finding have different effects.

### C16 — host capability can downgrade enforcement to advice
Claude runtime interposition can become external-host prose self-policing.

### C17 — support is a ladder, not a boolean
```text
registered < generated < structurally valid < installable < runtime-capable < workflow-executed < failure-path exercised < independently validated
```

### C18 — host adaptation is compilation plus capability negotiation
Literal rewrites are insufficient when semantics differ; preserve/native-replace/inline/suppress/degrade/unsupported must be explicit choices.

### C19 — repository self-description can outrun implementation
Derived docs can describe intended architecture before canonical runtime/setup reaches it.

### C20 — test execution itself needs standing
A configured/green test lane is not evidence unless the intended runtime/oracle actually executed.

### C21 — transition completion is not target-condition completion
**Status:** strong production-control conclusion.

```text
merge completed  ≠ deploy completed
deploy completed ≠ application healthy
revert pushed    ≠ prior healthy production restored
```

The workflow preserves the distinction well in the forward path and weakens it in rollback closure.

### C22 — operational feedback can remain informational
**Status:** strong boundary conclusion.

Retro recommendations and trends can update later context without automatically becoming admitted Work or Actor obligations.

### C23 — release identity and live health are separate evidence problems
**Status:** strong production-evidence conclusion.

A healthy URL is evidence about an observed service surface. It proves the intended merge is live only when release identity is separately bound (e.g. merge-SHA-bound deployment evidence or application version identity).

### C24 — coverage routing is part of verification truth
**Status:** direct repository finding.

Canary demonstrates that a test can exist and even have a gate-tier scenario while the canonical skill coverage matrix still represents only structural coverage. Test existence, routing and execution are separate standings.

---

## Protected verification limits

- no independent external replication of gstack as a whole;
- same-family subagents and cross-model challenge are not automatically independent verification;
- several workflow E2Es simulate dangerous/external effects rather than reproduce them;
- no live GitHub merge + real provider deploy + browser canary integration validation was established in this production pass;
- provider-specific deploy evidence has heterogeneous release-identity strength;
- Canary without a true pre-deploy baseline cannot establish before/after regression attribution;
- Canary observation is not bound to merge SHA/deployment ID in the inspected manifest schema;
- rollback does not require post-revert production restoration verification before `REVERTED` closure;
- readiness failed-test blocker semantics are textually inconsistent with the final override menu;
- careful/freeze/guard enforcement does not port unchanged to external hosts;
- CSO is not equivalent to professional pentesting or a live delivery gate;
- browser/runtime security has no independent penetration validation;
- GBrain semantic correctness is not independently validated;
- non-Claude host behavioral validation remains sparse outside Codex;
- Codex periodic CI has a known all-skip false-green;
- setup remains partly host-hardcoded despite the typed registry;
- full Retro semantic quality has much weaker direct behavioral coverage than its stale-base guard;
- four-ground/cross-ground projection remains premature until remaining native system clusters are synthesized.

---

## Known cautions

1. Derived docs never override pinned source/tree.
2. `SUBSTANTIAL / CONTINUE` sources require re-entry for stronger whole-file claims.
3. First-party tests/evals are evidence, not external independent verification.
4. All conclusions are pinned-revision conclusions; upstream is fast-moving.
5. Terms such as gate/security/root-cause/memory/agent/parallel/independent/isolation/read-only/support/portable/deployed/reverted/healthy must be interpreted from actual control semantics.
6. Pair-agent own-only isolation is browser-tab-specific.
7. Investigate freeze is not a full filesystem sandbox and is host-specific.
8. GBrain warm/stale distinction is lost in current planning preflight representation.
9. Multi-specialist/cross-model agreement is a workflow heuristic, not calibrated independence.
10. Codex-host ship has a known Agent-dispatch fidelity gap.
11. `/careful` HIGH deny is session-scoped and explicitly not a universal policy boundary.
12. `/guard` does not make Bash filesystem mutations obey the freeze Edit/Write boundary.
13. Historical CSO/deploy/canary report presence is not current security/production proof.
14. `docs/ADDING_A_HOST.md` is stale/aspirational where it says setup is already fully config-driven.
15. Host registry membership is not first-class runtime support evidence.
16. Generated-host freshness is not behavioral portability proof.
17. A green test lane that skipped its actual runtime is not positive verification evidence.
18. `REVERTED` in land-and-deploy is not proven `PRODUCTION RESTORED`.
19. `/health` is code-quality health, not service/deploy health.
20. Retro recommendation is not Work admission.
21. Canary test existence and canonical coverage-matrix attribution currently disagree.

---

## Current coverage gaps

- **testing / eval / judge / routing / compliance / flake lifecycle — NEXT**;
- repository self-development / generation / update / release mechanisms;
- chronology/evolution stream from changelog/release diffs;
- independent/adversarial validation of selected security, memory, coordination, portability, production and causal-workflow claims.

---

## Next work

The immediate next native subsystem is **testing / eval / judge / routing / compliance / flake lifecycle**.

Research question:

> how does gstack decide which tests/evals should run, prove that they actually executed against the intended runtime and oracle, aggregate their results, classify flakes/false greens, and convert those results into release confidence or repair work?

Priority route:

1. reconstruct free/static → behavioral E2E → LLM-judge → periodic/deep tier model;
2. inspect `skill-coverage-matrix`, diff/touchfile routing, shard selection and proof-of-execution;
3. inspect E2E session runners and how skip/degraded states are represented;
4. inspect LLM judges/oracles, cross-model evals and their independence limits;
5. inspect eval artifacts, compare/summary/flake-rank tooling and recurrence management;
6. inspect compliance/audit/slop scans and what is truly blocking;
7. use known counterexamples (Codex all-skip, Canary coverage-route mismatch, simulated deploy E2E) as falsification cases;
8. write a bounded testing/eval synthesis before repository self-development/release mechanics.
