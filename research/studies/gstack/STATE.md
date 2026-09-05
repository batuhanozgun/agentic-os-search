# gstack Study — STATE

**Status:** ACTIVE / IN PROGRESS  
**Study type:** external-target  
**User authorization:** broad gstack research and durable repository work authorised through the current operational boundary  
**Pinned target:** `garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`  
**Observed:** 2026-09-05  
**Current phase:** S2 — subsystem reconstruction; **seven bounded syntheses complete**  
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

### Security-control synthesis — key results

```text
Preventive controls
  /careful → Bash PreToolUse allow / ask / narrow HIGH deny
  /freeze  → Edit/Write path deny
  /guard   → careful + freeze composition

Decision authority
  typed one-way-door registry
  + secondary destructive keyword net
  + AUQ preference hook
  → convenience preferences cannot suppress destructive/high-stakes human confirmation

Detective/advisory security
  /cso
  → candidates
  → hard FP filtering
  → active source verification
  → fresh verifier
  → confidence/status gate
  → exploit scenario/remediation
  → timestamped report/trend
```

Important corrections:

- `/careful` is mainly an **ask gate**, with a deliberately tiny hard-deny subset; source calls HIGH a best-effort advisory hard-stop, not a universal policy boundary.
- malformed/obfuscated/unreadable Bash payloads fail toward `ask`, not silent allow.
- `/guard` is composition, not a filesystem/process sandbox; Bash and Edit/Write are controlled by different partial mechanisms.
- on Claude, careful/freeze/guard use real PreToolUse hooks; common external-host renders remove hook frontmatter and inject **Safety Advisory prose** instead. Same skill name therefore does not imply equivalent enforcement.
- typed one-way-door standing is primary; keyword classification is defense-in-depth because prose wording is too brittle for the primary safety boundary.
- `never-ask` preference cannot auto-decide a one-way door; ambiguous recommendations also refuse auto-decision.
- CSO daily mode favors precision (`>=8/10`); comprehensive mode favors recall (`>=2/10`) and labels weak results `TENTATIVE`.
- CSO separates severity, confidence and verification status (`VERIFIED` / `UNVERIFIED` / `TENTATIVE`).
- inability to quote the motivating current source forces confidence down and suppresses the finding from the main report.
- fresh verifier reduces anchoring but is not independent external verification.
- CSO’s “read-only” rule is behavioral rather than capability-enforced: the skill has Write authority for report persistence and no inspected source-write sandbox.
- `.gstack/security-reports/*` are timestamped historical audit artifacts; no targeted pinned-repo evidence showed them acting as automatic live ship/deploy blockers.

---

## Current cross-subsystem findings

### C1 — gstack is a qualification-driven work system

**Status:** strengthened working hypothesis, not whole-system conclusion.

```text
Planning/spec
→ qualifies intent before admission

Review/ship
→ qualifies implementation before delivery

Browser/runtime
→ qualifies capability, effect and evidence

Investigate
→ qualifies causal explanation before corrective mutation

Memory/context
→ qualifies prior information before reuse

Multi-agent coordination
→ qualifies delegation, completion and child evidence

Guarded action/security
→ qualifies whether effects may proceed,
   whether the human must decide,
   and whether security claims deserve standing
```

### C2 — qualification can be recomputed; ceremony history is secondary
Current standing often matters more than prior named ceremony. Browser refs, diff reviews, security evidence and child results have their own invalidation conditions.

### C3 — artifacts and typed representations can become active control inputs
Plans, reports, decisions, checkpoints, learnings and child JSON can alter later work. Their authority is consumer- and freshness-specific.

### C4 — authority is explicit, movable and resource-specific
User approval, delegated decisions, runtime capabilities, GBrain policy, one-way doors, child scope guards and escalation are different authority relations.

### C5 — freshness is object-relative
Diff, plan, browser state, checkpoint, learning, brain digest, child result and security report become stale for different reasons.

### C6 — evidence diversity is not automatically verification independence
Same-family fresh agents, Codex, tests, browser observation and CSO verifiers share varying common causes/oracles. Agreement is useful, not automatic independent verification.

### C7 — failure polarity is deliberately heterogeneous
Depending on mechanism, uncertainty can deny, ask, degrade, preserve stale state, suppress a claim, continue with partial evidence, or stop to prevent uncontrolled mutation.

### C8 — source→view fidelity is system-level
Known examples: generated skill vs template/resolver, checkpoint vs current source, browser stale refs, false-green security-state removal, hidden GBrain stale label, typed child data vs parent instruction, and historical CSO report vs current security truth.

### C9 — causal depth remains bounded
`/investigate` can terminate at a confirmed proximate mechanism; v1.79 multi-agent analysis demonstrates why recurrence/prevention/detection layers sometimes require deeper RCA.

### C10 — test names do not imply equal verification strength
Some E2Es reproduce production topology; others inline checklists or test presentation. Confidence follows actual oracle/topology.

### C11 — work-system correctness includes liveness
Parent/child wait, timeout, cancellation, duplicate suppression and partial-effect reconciliation are correctness properties.

### C12 — isolation must name the resource
Fresh context, browser tab, worktree, filesystem, memory and model separation are distinct.

### C13 — aggregation is itself control
Child/security findings are parsed, filtered, validated, deduplicated and status-qualified before affecting parent/user decisions.

### C14 — host portability is a distinct validity dimension
A rule proven on Claude hooks/Agent semantics cannot be silently generalized to Codex/Factory/OpenClaw/Hermes.

### C15 — prevention, authority and detection are different security layers
A warning/deny hook, a mandatory human confirmation, and a CSO finding have different effects and must remain separate in later system modeling.

### C16 — host capability can downgrade enforcement to advice
The careful/freeze/guard generator path is a concrete example: runtime interposition on Claude becomes prose self-policing on external hosts.

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
- CSO is not equivalent to professional pentesting and does not automatically gate delivery;
- CSO report freshness is not automatically recomputed by another control plane;
- browser/runtime security has no independent penetration validation;
- GBrain semantic correctness is not independently validated;
- stale GBrain fallback loses its freshness label in planning view;
- production deploy/canary/retro closure remains unsynthesized;
- four-ground/cross-ground projection remains premature.

---

## Known cautions

1. Derived docs never override pinned source/tree.
2. `SUBSTANTIAL / CONTINUE` sources require re-entry for stronger whole-file claims.
3. First-party tests/evals are evidence, not external independent verification.
4. All conclusions are pinned-revision conclusions; upstream is fast-moving.
5. Terms such as gate/security/root-cause/memory/agent/parallel/independent/isolation/read-only must be interpreted from actual control semantics.
6. Pair-agent own-only isolation is browser-tab-specific.
7. Investigate freeze is not a full filesystem sandbox and is host-specific.
8. GBrain warm/stale distinction is lost in current planning preflight representation.
9. Multi-specialist/cross-model agreement is a workflow heuristic, not calibrated independence.
10. Codex-host ship has a known Agent-dispatch fidelity gap.
11. `/careful` HIGH deny is session-scoped and explicitly not a universal policy boundary.
12. `/guard` does not make Bash filesystem mutations obey the freeze Edit/Write boundary.
13. CSO code “read-only” behavior is not enforced by a source-write capability sandbox.
14. Historical CSO report presence is not current security proof.

---

## Current coverage gaps

- **host adapters / portability fidelity — NEXT**;
- deploy / canary / production observation / retrospective feedback;
- test/eval/judge/routing/compliance/flake lifecycle;
- repository self-development / generation / update / release mechanisms;
- chronology/evolution stream from changelog/release diffs;
- independent/adversarial validation of selected security, memory, coordination and causal-workflow claims.

---

## Next work

The immediate next native subsystem is **host adapters / portability fidelity**.

Research question:

> when gstack renders one conceptual workflow for Claude, Codex, Factory/Droid, Cursor, OpenClaw, Hermes and other supported hosts, which semantics are preserved, rewritten, suppressed, approximated, or weakened — and how can a consumer tell whether a cross-host skill still has the same effective behavior and control strength?

Priority route:

1. reconstruct host config/type model and generation pipeline;
2. compare frontmatter/tool/path/resolver suppression across representative hosts;
3. inspect safety-hook → prose degradation, Agent dispatch gaps and GBrain/cross-model suppression;
4. distinguish surface syntax portability from semantic fidelity;
5. inspect golden/generated fixtures and host-specific tests;
6. identify whether host capability differences are visible to users/workflows or can become silent behavioral drift;
7. write a bounded portability synthesis before production/deploy feedback.
