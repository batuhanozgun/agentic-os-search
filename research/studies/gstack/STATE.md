# gstack Study — STATE

**Status:** ACTIVE / IN PROGRESS  
**Study type:** external-target  
**User authorization:** broad gstack research and durable repository work authorised through the current operational boundary  
**Pinned target:** `garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`  
**Observed:** 2026-09-05  
**Current phase:** S2 — subsystem reconstruction; four bounded syntheses complete  
**Foundation mutation:** NONE / NOT AUTHORISED BY THIS STUDY

## Protected research question

Build a source-grounded model of gstack as an implemented software-development operating system / software factory, then determine what it does across Information, Work, Actors and Environment and how its important mechanisms connect those areas.

The Foundation four-ground frame is an upper-level projection/comparison frame, not the initial source taxonomy.

## Method

Research units are semantic mechanisms/subsystems, not fixed file batches.

A load-bearing mechanism is reconstructed from the strongest relevant combination of:

```text
behavior/policy contract
+ shared/generated instruction surfaces
+ orchestration/helper code
+ runtime capability
+ tests/evals/compliance checks
+ persistent artifacts/state
```

Higher-level summaries retain source re-entry paths. Intended policy, implementation, structural pins, behavioral evidence and independent verification remain distinct evidence classes.

## Completed durable checkpoints

### 1 — Planning / specification / work admission

`research/studies/gstack/syntheses/planning-specification-work-admission.md`

Bounded reconstruction of discovery, premise challenge, durable design lineage, CEO/engineering review, delegated `/autoplan` decisions, specification, quality/redaction/sink gates, issue/archive and optional isolated execution.

### 2 — Review / QA / ship / delivery qualification

`research/studies/gstack/syntheses/review-qa-ship-delivery-qualification.md`

Bounded reconstruction of review, browser QA, merged-code testing, failure ownership, semantic changed-path coverage, conditional plan completion, fresh pre-landing review, specialist/red-team/adversarial challenge, fix→test→review convergence and PR/release evidence.

### 3 — Browser runtime / security / evidence

`research/studies/gstack/syntheses/browser-runtime-security-evidence.md`

Bounded reconstruction of the persistent browser daemon, per-tab state/ref semantics, root/scoped browser authority, own-only versus shared tab policy, local/tunnel listener separation, deny-default CDP, URL/SSRF/path controls, opt-in persistence, content/prompt-injection defenses, audit/activity evidence and heterogeneous security failure polarity.

### 4 — Investigation / root-cause / debug control

`research/studies/gstack/syntheses/investigation-root-cause-debug-control.md`

Bounded reconstruction of:

- evidence gathering before hypothesis formation;
- explicit testable root-cause hypotheses;
- hypothesis falsification and return to investigation;
- 3-strike escalation and authority transfer to user/human choice;
- Claude-host Edit/Write freeze coupling and its shell-level enforcement;
- host-specific scope-lock differences;
- minimal intervention, regression testing and fresh original-symptom verification;
- structured debug completion states;
- durable investigation-learning handoff;
- causal-depth limit: strong hypothesis-driven debugging is not the same as mandatory systemic/prevention-detection RCA;
- test-coverage asymmetry: causal workflow has mainly structural coverage while freeze has stronger runtime tests.

## Current strongest findings

### F1 — gstack is more than a prompt/skill collection

**Status:** strong observation/inference.

The pinned system combines generated behavioral contracts, durable artifacts, persistent runtime capability, actor/decision authority, testing/eval infrastructure, security/control surfaces and lifecycle workflows.

### F2 — generated skills are composed behavioral programs

**Status:** strong implementation observation.

`.tmpl` skeletons, shared resolvers, carved sections, host-specific rendering and parent-child composition jointly define behavior. Generated `SKILL.md` files are runtime artifacts, not sufficient provenance by themselves.

### F3 — planning is a sequence of qualification transitions

**Status:** strong subsystem inference.

Continuation repeatedly requires a more qualified state: framed problem, accepted premise, chosen approach, accepted scope, resolved target, decided findings, confirmed spec, safe outbound content and authorised execution.

### F4 — durable artifacts participate in control flow

**Status:** strong cross-subsystem inference.

Plans, review reports, decision logs, issues, QA/test-plan artifacts, worktree metadata and PR bodies are later rediscovered and can alter admission, staleness, execution or delivery decisions.

### F5 — decision authority is explicit and movable

**Status:** strong subsystem inference.

Interactive workflows retain granular user authority; `/autoplan` delegates declared classes; ship-time residual-risk decisions are explicit overrides; investigate's 3-strike rule ends automatic agent continuation and returns the next-investment decision to the user/human.

### F6 — `/spec` is a work-admission boundary

**Status:** strong structural observation + bounded behavioral support.

Why/scope/current-state/code evidence precede filing; quality/confidentiality/sink and isolated-spawn controls constrain admission.

### F7 — `/ship` is a delivery-qualification boundary

**Status:** strong subsystem inference.

Ship recomputes/consumes merged-code tests, semantic path coverage, plan completion, optional browser verification, fresh diff review, specialist/red-team review, adversarial challenge and release/documentation state.

### F8 — required qualification is decoupled from prior ceremony

**Status:** strong source/inference.

A current Eng Review standing is required by default, but a prior standalone review ceremony is not: ship can recompute it. Discoverable plan artifacts can instead become conditional control objects at ship time.

### F9 — verdict freshness is object-relative

**Status:** strong source/inference.

Diff review, plan review, browser refs/state and post-fix evidence each have different freshness conditions. A prior clean verdict is not authoritative merely because it exists.

### F10 — verification is heterogeneous but not uniformly independent

**Status:** strong synthesis conclusion.

Static reasoning, executable tests, browser observation, semantic coverage, specialist contexts and cross-model challenge are different evidence channels; common artifacts/framing/orchestration prevent automatic independence claims.

### F11 — control failure polarity varies by evidence class

**Status:** strong synthesis conclusion.

Known invalidity can hard-block; uncertainty can trigger conservative ownership, explicit override or human escalation; optional outside-model/ML evidence can degrade gracefully; critical audit/gate machinery cannot always silently certify success.

### F12 — evaluation is first-class but test existence is not one confidence level

**Status:** strong source observation.

Some mechanisms have deterministic invariants and real-browser/PTY/HTTP E2Es; others have only structural floors. Verification claims must follow the actual test tier and oracle.

### F13 — persistent browser execution is a substantive evidence environment

**Status:** strong subsystem inference.

Browser state, tabs, refs, mode, restore and action side effects change what an observation means; evidence freshness must be constructed.

### F14 — browser authority is multi-dimensional capability state

**Status:** strong implementation observation.

Identity/token, scope, domain, tab policy, rate, expiry and listener surface jointly determine effective browser authority.

### F15 — browser isolation is contextual, not universal

**Status:** strong corrective finding.

Own-only pair-agent/tunnel clients receive strict tab isolation. Shared local skill clients intentionally may operate across unowned/other tabs.

### F16 — remote browser exposure is narrowed structurally before command policy

**Status:** strong structural observation + bounded behavioral support.

Tunnel traffic lands on a separate listener with only `/connect` and `/command`; root credentials are rejected there and a closed command allowlist precedes normal scoped-token checks. Live hostile ngrok exposure is not independently reproduced.

### F17 — high-risk browser escape hatches are separately scoped / deny-default where practical

**Status:** strong implementation + selected behavioral support.

Raw CDP uses an explicit allowlist; browser-wide control is separate; navigation/file effects are validated; selected CDP denials have real-Chromium E2E evidence.

### F18 — persistence excludes dangerous authority/content fields

**Status:** strong implementation + behavioral support.

Headless cross-restart persistence is opt-in. Cookies/URL/storage may persist; loaded HTML and tab ownership do not. Restore revalidates/filter/quarantines and has a real-Chromium round-trip test.

### F19 — security standing is itself an evidence/freshness problem

**Status:** strong source observation.

An unfed stale security-status surface was removed rather than allowed to report false-green “protected” state.

### F20 — browser auditability and operational visibility are separate

**Status:** strong implementation inference.

Persistent JSONL audit is best-effort forensic evidence; live activity is bounded/in-memory with gap detection. Neither is guaranteed complete history.

### F21 — `/investigate` separates diagnosis from intervention

**Status:** strong authored-contract observation.

A specific testable causal hypothesis is intended to be established before implementation. The causal ordering is policy/model compliance rather than a machine-readable “root-cause-confirmed” runtime state gate.

### F22 — uncertainty accumulation changes continuation authority

**Status:** strong authored-contract observation.

After three failed hypotheses the agent is instructed to stop and require an explicit choice among continued investigation, human escalation or instrumentation-and-wait.

### F23 — investigation scope lock is real but partial and host-specific

**Status:** strong implementation + test observation.

On Claude Code, Edit/Write hooks can hard-deny out-of-boundary files, malformed payloads and symlink escapes. Bash remains outside the guardrail. Common external hosts strip hooks; the OpenClaw adaptation omits the freeze stage.

### F24 — investigate freeze lifecycle is not automatically closed by the skill

**Status:** strong implementation observation.

The workflow writes `freeze-dir.txt`; `/unfreeze` removes it. `/investigate` does not guarantee automatic cleanup at completion, and state-root persistence varies by install/host context.

### F25 — investigation completion uses both mechanism and symptom evidence

**Status:** strong authored-contract observation.

The intended completion combines regression test, full suite and fresh reproduction of the original bug. `DONE_WITH_CONCERNS` allows incomplete verification to remain explicit.

### F26 — “root cause” is stronger language than the investigate contract can guarantee

**Status:** strong causal-depth qualification.

The workflow strongly supports hypothesis-driven debugging but does not require a separate analysis of why the system allowed/prevention/detection failed. A confirmed local mechanism can terminate the workflow even if deeper systemic causes remain.

### F27 — recurring failure is allowed to pressure analysis toward architecture

**Status:** strong authored-contract observation.

Repeated bugs in the same area, cascading fixes, three failed hypotheses and >5-file blast radius are explicit signals to question the abstraction/architecture rather than continue patching.

### F28 — investigation knowledge is designed to compound but remains fallible evidence

**Status:** strong implementation inference.

Local learnings preserve source/confidence/files, apply confidence decay and cross-project trust restrictions, and can reorder future investigation reasoning without becoming automatic truth.

### F29 — behavioral verification of investigate's causal methodology is a weak point

**Status:** direct coverage observation.

The skill coverage matrix assigns `/investigate` only the generic structural floor and no periodic E2E. Its freeze submechanism is much more strongly tested than the no-fix/3-strike/regression/fresh-verification behavior.

### F30 — promotional/relationship behavior remains analytically separate

**Status:** direct observation; R02 separation active.

Office-hours founder/YC/retention surfaces remain real product behavior but are not evidence for planning/debugging/delivery quality.

## Working cross-subsystem hypothesis

**Status:** strengthened working hypothesis, not whole-gstack conclusion.

The first four syntheses support the model that gstack is a **qualification-driven work system**:

```text
Planning/spec      qualifies intent before work admission
Review/ship        qualifies implementation before delivery
Browser/runtime    qualifies authority/effects/evidence at execution boundaries
Investigate        qualifies causal explanation before corrective mutation
```

Behavioral contracts, durable artifacts, actor authority, runtime capabilities, observed effects and evidence freshness are repeatedly connected by explicit continuation/transition rules.

This still must survive memory/context, multi-agent, guarded-action/security-review, production-feedback and eval-infrastructure research.

## Verification status

Current synthesis layers distinguish:

1. **intended policy** — skill/template prose;
2. **implemented composition/runtime contract** — resolver/helper/runtime code;
3. **structurally pinned contract** — deterministic invariant/generator/source/shell tests;
4. **behavioral evidence** — real-agent/PTY/browser/HTTP/LLM-judged E2E;
5. **independent verification** — not established for gstack as a whole.

Current limits include:

- no independent external replication;
- cross-model diversity is not automatically independent verification;
- several behavioral E2Es are scenario-bounded or approximate production orchestration;
- `/investigate` has no registered causal-workflow behavioral E2E beyond structural floor, despite stronger freeze tests;
- AI-assessed changed-path coverage is not instrumented coverage;
- browser runtime/security has no independent penetration validation;
- live hostile/public ngrok behavior was not reproduced by inspected tests;
- optional ML prompt-injection classification is fail-open and benchmark/oracle validity remains separate;
- audit and permission-hardening include best-effort semantics;
- deploy/canary/retro production loop remains open;
- four-ground and cross-ground synthesis remain premature.

## Known cautions

1. `docs/PROJECT_STRUCTURE.md` is a derived view and contains at least one stale/non-resolving path; actual pinned source/tree wins.
2. Long files marked `SUBSTANTIAL / CONTINUE` must be re-entered before stronger whole-file claims.
3. First-party tests/evals are evidence about expected/implemented behavior, not independent verification.
4. Upstream `main` is fast-moving; all current conclusions remain version-bound to the pinned commit.
5. “Gate,” “required,” “always-on,” “root cause,” “security” and “coverage” must be interpreted from actual control semantics, not labels.
6. Browser command READ/WRITE categories are not authoritative security capability classes.
7. Pair-agent own-only isolation must not be generalized to shared local clients.
8. Browser state continuity between calls is not default cross-daemon persistence.
9. Investigate freeze is not a filesystem sandbox and is not uniformly available across hosts.
10. The investigate text inconsistently says three failed **hypotheses** in the phase and three failed **fix attempts** in its closing rules; no machine-readable strike counter resolves this ambiguity.
11. Investigation “root cause” can be a confirmed proximate mechanism without a mandatory prevention/detection/systemic cause analysis.

## Current coverage gaps

Major unresolved clusters now are:

- **memory / learnings / context / GBrain lifecycle — NEXT**;
- multi-agent and cross-model dispatch beyond inspected planning/ship/browser paths;
- guarded-action and CSO security-review workflows beyond browser-native/freeze controls;
- host adapters / portability fidelity as a dedicated subsystem;
- deploy/canary/production/retro feedback loop;
- eval judges, routing, compliance, flake/compare/watch lifecycle;
- repository self-development / generation / update / release mechanisms;
- chronology/evolution stream from changelog and release diffs;
- independent/adversarial validation of selected security and causal-workflow claims.

## Next work

The immediate next native subsystem is **memory / learnings / context / GBrain**.

Rationale: investigation shows that verified causal conclusions are deliberately fed back into future reasoning. Planning also consumes prior decisions/context. The next system question is therefore not merely “where is memory stored?” but:

> how does gstack create, classify, retrieve, decay, trust, invalidate, scope and re-use informational state so that prior work can improve later work without silently turning stale/contaminated state into authority?

Research priorities:

1. reconstruct local `learnings.jsonl` creation/search/prune/staleness semantics;
2. inspect explicit context-save/context-restore checkpoints and what is or is not treated as current truth;
3. reconstruct GBrain integration, cache/TTL/stale-but-usable behavior, trust policy and host suppression;
4. distinguish user-stated, observed, inferred and cross-model sources;
5. inspect cross-project contamination controls and privacy boundaries;
6. trace where planning/review/investigate/retro consume and write memory;
7. inspect tests/E2Es around learning persistence, decay, staleness, bad-token/offline/fallback behavior;
8. determine whether memory is advisory context, an active control input, or both in different consumers;
9. write a bounded memory/context synthesis before moving to broader multi-agent or production loops.

Only after several more native subsystem syntheses should the study start the four-ground/cross-ground projection.
