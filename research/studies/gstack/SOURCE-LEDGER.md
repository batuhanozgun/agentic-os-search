# gstack Study — Source Ledger

## Canonical target

Unless a row states otherwise, source paths refer to:

`garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`

Observed 2026-09-05.

## Status legend

- **FULL** — source was read as a whole at the study snapshot with enough visibility for current use.
- **SUBSTANTIAL / CONTINUE** — meaningful portion read, but long/composed source requires more reading before whole-source claims.
- **INVENTORY** — path/tree/metadata inspected, not substantive file content.
- **PLANNED** — known relevant source not yet read in this study pass.

`FULL` means read coverage, not independent verification.

## Orientation / governing sources

| Source | Blob / evidence ref | Read status | Current role |
|---|---|---:|---|
| `AGENTS.md` | actual pinned tree reports blob `7d802490e95cb7d6f19f9328d20223d6ce696ee9`; earlier content fetch exposed governing instructions | FULL | repository behavior/development contract; generation, testing, security, source-of-truth rules |
| `CLAUDE.md` | actual pinned tree reports blob `115a5228277d6a5ecae31c3dc86b76802a739f62` | FULL | detailed repo-control, skill-generation, test/eval/release contract |
| `ETHOS.md` | content fetch during study | FULL | cross-skill behavioral philosophy/policy source |
| `DESIGN.md` | content fetch during study | FULL | visual artifact design policy |
| `ARCHITECTURE.md` | blob `374dd8774bd08657cb15987182596a7630bfae47` | FULL | browser/runtime architecture, daemon lifecycle, listener/security model |
| `BROWSER.md` | pinned content/search during browser pass | SUBSTANTIAL / CONTINUE | repository-authored browser operator/security/runtime view; implementation cross-check required |
| `docs/PROJECT_STRUCTURE.md` | pinned content fetch | FULL | repository-authored structural view; requires actual-tree cross-check |
| `package.json` | pinned content fetch; package v1.79.0 | FULL | build/runtime dependencies; test/eval/gate commands; executable surfaces |
| `SKILL.md.tmpl` | blob `402bd0d7b0f2bf02f6c9e4754e0e2a655f5f4057` | FULL | root intent router; proactive opt-out; direct specialist routing |
| actual root contents/tree | GitHub contents + recursive tree API at pinned commit | INVENTORY | observed repository topology and path existence |

## Planning / specification workflow sources

| Source | Evidence ref | Read status | Current role / note |
|---|---|---:|---|
| `office-hours/SKILL.md.tmpl` | `ecd96fb4186115182a653f67e59c1dc7496ed326` | FULL | discovery/design parent contract; no-implementation gate, premise challenge, alternatives, approval, handoff |
| `office-hours/sections/manifest.json` | `fa6df52648ceca8ea427056d73000c8a7d6cd870` | FULL | passive carve registry |
| `office-hours/sections/phase-2a-startup-diagnostic.md.tmpl` | `0e3a12274d5cbd2845130e529aec6f9118b7d479` | FULL | startup forcing questions, demand/status-quo/specificity evidence discipline |
| `office-hours/sections/phase-2b-builder-brainstorm.md.tmpl` | `e49d6cd80b61b8b12cfc6e3d372b8b8c0857134b` | FULL | builder-mode generative/delight posture |
| `office-hours/sections/design-and-handoff.md.tmpl` | `5924dd706a141a77d96ea05aec998e6ddbaae5b9` | SUBSTANTIAL / CONTINUE | design lineage, dual-write, sink scan, approval, memory/profile, YC/resource relationship layer, downstream handoff; long tail should be re-opened for any later claim beyond current bounded synthesis |
| `plan-ceo-review/SKILL.md.tmpl` | `1b1affe160d2919ee08e00f101784a97d210906a` | FULL | scope/ambition modes, explicit scope authority, pre-review system audit, artifacts |
| `plan-ceo-review/sections/manifest.json` | `5ef4425a943600708ff1d0fdb9352f2a97c07de9` | FULL | review-section carve registry |
| `plan-ceo-review/sections/review-sections.md.tmpl` | pinned path; blob to re-confirm before load-bearing reuse | SUBSTANTIAL / CONTINUE | 11-section full-depth review, per-finding gates, registries, logs, chaining |
| `plan-eng-review/SKILL.md.tmpl` | `e066e2c5f5028ad3b8485fe8606967ac1188b47e` | FULL | first-action scope/target authority gate; architecture/test/perf review |
| `plan-eng-review/sections/manifest.json` | `f76e8f95bf4b313cecc2797278440cfc8f0a90a5` | FULL | eng-review carve registry |
| `plan-eng-review/sections/review-sections.md.tmpl` | pinned path; blob to re-confirm before load-bearing reuse | FULL for current subsystem use | four review sections, per-finding approval, tasks/failure modes/parallel lanes/review logs |
| `autoplan/SKILL.md.tmpl` | `6a034e15e7647980d74dfa71bfe17c25875ed054` | SUBSTANTIAL / CONTINUE | delegated-decision mode, sequential review chain, one final gate, decision audit trail |
| `spec/SKILL.md.tmpl` | pinned path; blob to re-confirm before load-bearing reuse | SUBSTANTIAL / CONTINUE | why/scope/code-evidence/draft confirmation spine; executable-spec admission criteria |
| `spec/sections/gate-and-file.md.tmpl` | `f8923a834e9228d42b4e535ed8b97cb52e0e5a6d` | FULL for current subsystem use | quality/redaction/sink gates; issue/archive; worktree/SHA/spawn controls |
| `plan-design-review/SKILL.md.tmpl` | — | PLANNED | design plan review |
| `plan-devex-review/SKILL.md.tmpl` | — | PLANNED | developer-experience plan review |
| `design-consultation/SKILL.md.tmpl` | — | PLANNED | design/product alternative research |

## Review / QA / delivery qualification sources

| Source | Evidence ref | Read status | Current role / note |
|---|---|---:|---|
| `review/SKILL.md.tmpl` | `a1d6a172746bdc4905731fe4e96ffb6976a579e9` | FULL for current subsystem use | diff review, confidence calibration, Fix-First, claim verification, result persistence |
| `review/sections/manifest.json` | `26a94ca3a7ed431514d857d9b6bd758afa859e88` | FULL | review carve registry |
| `review/sections/plan-completion.md.tmpl` | `7a7ae47e4ae31f1e28991bf7b233fc665f2ad4a8` | FULL for current subsystem use | informational plan-completion semantics for standalone review |
| `review/sections/plan-completion.md` | `38da1ae08b0d966004d522b74af3f48ffceadcf3` | FULL | generated plan audit, verification modes, gap classification, learning path |
| `ship/SKILL.md.tmpl` | pinned source; exact blob to re-confirm before byte-level reuse | SUBSTANTIAL / CONTINUE | release orchestration, readiness preflight, base merge, tests/review/release sequencing |
| `ship/sections/manifest.json` | `e4394e5623f9421972c9be642f7d202760af866d` | FULL | ship carve registry |
| `ship/sections/tests.md` | pinned generated source | SUBSTANTIAL / CONTINUE | framework bootstrap, merged-code tests, failure ownership triage, evidence ledger |
| `ship/sections/test-coverage.md` | pinned generated source | SUBSTANTIAL / CONTINUE | fresh-context semantic path coverage, generated tests, thresholds/overrides, test-plan artifact |
| `ship/sections/plan-completion.md` | `2c36cefe477d68768a5623090c9a90835427ae5f` | FULL for current subsystem use | plan item audit as release gate, per-item unverifiable confirmation, qa-only plan verification, scope drift |
| `ship/sections/review-army.md` | `bb1c3b82910ebaccf1beecfa10bf0771cc777601` | SUBSTANTIAL / CONTINUE | fresh pre-landing review, specialists, red team, dedup, Fix-First, test+review closure loop |
| `ship/sections/adversarial.md` | `254331b9f615a09dc6e96deb952d622fe54bcd32` | FULL for current subsystem use | always-attempted Claude/Codex adversarial topology, degradation and non-blocking failure semantics |
| `ship/sections/pr-body.md` | pinned generated source | SUBSTANTIAL / CONTINUE | fresh-context docs sync, PR evidence aggregation, idempotent body/title handling |
| `qa-only/SKILL.md.tmpl` | `75c4123cc5c406ffdd36c71a094335c137135b1e` | FULL for current subsystem use | browser-only report mode, no source fix, durable QA evidence |
| `qa/SKILL.md.tmpl` | `d15a0c5d151ec6a8b15cd3a31dc96430ddb91909` | FULL for current subsystem use | browser test→fix→verify loop, atomic commits, regression tests, self-regulation |
| `scripts/resolvers/utility.ts` (`generateQAMethodology`) | `911b01d8f7e5264a759cfa878c440e7f642eb7cb` | FULL for QA-methodology use | shared diff-aware/full/quick/regression browser QA, screenshots/repro/health scoring |
| `scripts/resolvers/review.ts` (`generateReviewDashboard`) | `04f2dee0091e768ad1a11feda9f3a824256bfb45` | FULL for dashboard/staleness use | current Eng Review semantics, content-first freshness, plan-vs-diff standing, dashboard consumers |
| `land-and-deploy/SKILL.md.tmpl` | — | PLANNED | post-PR landing/deployment |
| `canary/SKILL.md.tmpl` | — | PLANNED | production observation / canary feedback |
| `document-release/SKILL.md.tmpl` | partial via `/ship` dispatch contract only | PLANNED / REFERENCED | documentation synchronization is observed as a ship subagent dependency; standalone workflow not yet reconstructed |
| `retro/SKILL.md.tmpl` | — | PLANNED | retrospective / feedback learning loop |

## Other workflow / lifecycle sources

| Source | Read status | Current role / note |
|---|---:|---|
| `investigate/SKILL.md.tmpl` | `c7cd9a99ad695f966ef2befaf18b1120eff89535` | FULL / NEXT SYNTHESIS | root-cause investigation phases, hypothesis testing, scope lock, regression/fresh verification, learning handoff |
| `design-review/SKILL.md.tmpl` | PLANNED | implemented UI/design review |
| `devex-review/SKILL.md.tmpl` | PLANNED | implemented developer-experience review |
| `pair-agent/SKILL.md.tmpl` | PLANNED | multi-agent coordination beyond browser-side pairing ceremony |
| `cso/SKILL.md.tmpl` | PLANNED | security review/CSO role |
| `learn/SKILL.md.tmpl` | PLANNED | durable learning capture |
| `setup-gbrain/SKILL.md.tmpl` | PLANNED | GBrain setup/context memory |
| `sync-gbrain/SKILL.md.tmpl` | PLANNED | GBrain synchronization |
| `codex/SKILL.md.tmpl` | PLANNED | cross-model second opinion/review beyond the inspected ship integration |
| `benchmark/SKILL.md.tmpl` | PLANNED | model/agent comparison |
| guard/freeze/careful/unfreeze skill surfaces | PLANNED / REFERENCED | guarded-action / scope-control mechanisms; investigate already references freeze runtime |

## Shared / generator / browser runtime sources

| Source | Evidence ref | Status | Why needed / current result |
|---|---|---:|---|
| `scripts/gen-skill-docs.ts` | pinned source | SUBSTANTIAL / CONTINUE | confirms `.tmpl → resolver → generated .md`, host/model overlays, dry-run freshness, output isolation |
| `scripts/resolvers/index.ts` | `cee08c2015a6ac2ff8605b02ac07a49d284d3ce1` | FULL | central resolver registry across review, memory, tasks, sections, redaction, composition |
| `scripts/resolvers/sections.ts` | `c6425e19b93d20018057cf2fe6ae9eeb2f613a18` | FULL | Claude STOP+Read carve vs non-Claude inline rendering; passive manifest semantics |
| `scripts/resolvers/composition.ts` | `b8d3483d9bd961409025959eddcd8840dd5f98a8` | FULL | parent-child skill invocation and parent-owned section skip contract |
| shared Codex integration | partial through planning/review/ship sources | SUBSTANTIAL / CONTINUE | cross-model challenge topology and graceful degradation; independence not established |
| `browse/SKILL.md.tmpl` | pinned fetch | SUBSTANTIAL / CONTINUE | operator/runtime contract; persistence, QA patterns, evidence caveats, handoff, file/local-render guidance |
| `browse/src/server.ts` | pinned fetch/search | SUBSTANTIAL / CONTINUE | long-lived daemon, factory/auth, local/tunnel listeners, dispatch, tab gate, persistence/security/audit integration |
| `browse/src/browser-manager.ts` | pinned fetch/search | SUBSTANTIAL / CONTINUE | browser/context lifecycle, headed/headless modes, persistent profile, tab ownership, crash/disconnect semantics |
| `browse/src/tab-session.ts` | `dccabf28f4263cb77d0a594369bb15f3e2c7ad73` | FULL | per-tab refs/snapshot/frame/load-html state and invalidation |
| `browse/src/commands.ts` | pinned fetch | SUBSTANTIAL / CONTINUE | shared command registry and page-content classification; historical read/write labels are not security authority |
| `browse/src/token-registry.ts` | `89b0a990c31e26188275295e3d2d60f5908c5033` | FULL | root/scoped tokens, scope/domain/rate/expiry/tab policy, reduction/revocation semantics |
| `browse/src/snapshot.ts` | pinned fetch | SUBSTANTIAL / CONTINUE | ARIA snapshot/ref model, cursor-interactive refs, annotation ambiguity/degradation |
| `browse/src/cdp-allowlist.ts` | `752ce464c8e9e5d9f697c81a08444d0dd666b1e0` | FULL | deny-default CDP method registry with scope/output/justification |
| `browse/src/cdp-bridge.ts` | `3d1fa3d8d002656f0e9528001df7b7c6e300b80b` | FULL | allowlist dispatch, tab/global locks, timeout, CDP-session lifecycle |
| `browse/src/url-validation.ts` | `c9e9c170ac36a6c744f47dee2b3bf15eb49e68f1` | FULL | schemes, file URLs, metadata/SSRF/DNS-rebinding checks; local QA allowances |
| `browse/src/path-security.ts` | `bc02ccde06c753dcd4b00e3fba49ad87267adb04` | FULL | local output/read paths, symlink handling, temp-only remote serving |
| `browse/src/file-permissions.ts` | pinned fetch | SUBSTANTIAL / CONTINUE | POSIX/Windows owner-only hardening, shared/symlink directory protection, best-effort semantics |
| `browse/src/session-persist.ts` | `3c6627bcbc0c24e76c519934b0a3a9ba3b87aca9` | FULL | opt-in headless persistence, excluded authority/content fields, restore filtering/quarantine |
| `browse/src/content-security.ts` | `a185764583f73aaa7b8d979d8ff5942bf63c25f7` | FULL | datamarking, hidden/ARIA handling, content filters, untrusted envelopes, URL blocklist |
| `browse/src/security.ts` | `3da662a008e0785102f6572de468cc8dcb6bc136` | FULL | ML-signal verdict combiner/canary utilities and dead-state removal context |
| `browse/src/security-classifier.ts` | `a89ddf694b165872263ed8a2f46e88faa5b3f52f` | FULL | TestSavantAI L4 classifier, model staging, explicit fail-open behavior |
| `browse/src/security-sidecar-client.ts` | `95e226070466df31b6e0db2ef7d93bf50b49b521` | FULL | lazy sidecar, timeout/request cap, respawn/circuit breaker, degradation semantics |
| `browse/src/audit.ts` | `f93b47fb090c99c95dd3c83091a0b097330130df` | FULL | persistent best-effort JSONL command forensic trail |
| `browse/src/activity.ts` | `b15eb45a1d1c2bf5ae57f832418a0d7aa40a0f52` | FULL | bounded real-time activity feed, privacy filtering, gap detection |
| host adapter surfaces | — | PLANNED | portability and host-specific behavior beyond current browser implementation |

## Eval / verification / compliance sources

| Source | Evidence ref | Status | Current role / limit |
|---|---|---:|---|
| `test/spec-template-invariants.test.ts` | `40d2d22677cbd0a506c6395bc0e2b00b3a2149d2` | FULL | deterministic structural pins for spec phase/safety/admission contracts; not behavioral proof by itself |
| `test/ship-plan-completion-invariants.test.ts` | `26c565b1b093262697832d3b161c479bbb5ce07b` | FULL | deterministic ship plan-gate pins: concrete paths, validators, per-item confirmation, no silent fail-open |
| `test/skill-coverage-matrix.ts` | `7359afbce8144625e3b832d0fa9044fb753185a8` | FULL | gate vs periodic coverage model; every skill has at least a CI-blocking floor |
| `test/skill-e2e-plan-eng-plan-mode.test.ts` | `85eec6cc401bf79275aae0e34e11373a72e7c71b` | FULL | periodic real-PTY behavior for STOP-before-write and plan-mode scope-gate bypass |
| `test/skill-e2e-autoplan-dual-voice.test.ts` | `1efc6dfc68643fa2772770ea9b87187986612e99` | FULL | periodic/non-gating dual-voice dispatch/graceful-degrade evidence; partial-pipeline only |
| `test/skill-e2e-office-hours.test.ts` | `c3ad6c57b80ce6a78510f1e0d226b39900e9df49` | FULL | LLM-judged posture behavior for startup forcing and builder wildness; oracle-dependent |
| `test/skill-e2e-review.test.ts` | `75b9accd3939e35877c4245bc3a33d9e2977eff0` | FULL | selected planted defect detection for SQL/value/design review behavior |
| `test/skill-e2e-review-army.test.ts` | pinned source | SUBSTANTIAL / CONTINUE | migration/performance/delivery/score scenarios; some tests apply specialist checklist inline rather than reproduce production Agent topology |
| `test/skill-e2e-qa-workflow.test.ts` | pinned source | SUBSTANTIAL / CONTINUE | real browser QA behavior; qa-only no-edit/clean-tree guardrail; qa fix-loop edit + commit evidence; broader file continues |
| `test/skill-e2e-ship-idempotency.test.ts` | `29ef83827d66b150d4114a3e7efa8124975a4dfc` | FULL | periodic real-PTY proof for release version/changelog idempotency only; not a whole-ship gate E2E |
| `test/skill-validation.test.ts` | pinned source | SUBSTANTIAL / CONTINUE | generated-skill/router/command invariants; pins selected composition contracts |
| `browse/test/dual-listener.test.ts` | pinned fetch | SUBSTANTIAL / CONTINUE | exact-set tunnel path/command structural pins; explicitly distinct from behavioral tunnel E2E |
| `browse/test/server-factory.test.ts` | pinned fetch | SUBSTANTIAL / CONTINUE | factory/auth/listener behavior and embedded-server contract |
| `browse/test/server-auth.test.ts` | pinned fetch | SUBSTANTIAL / CONTINUE | auth/CORS/token/tab/chain/activity/tunnel structural security regressions |
| `browse/test/pair-agent-e2e.test.ts` | pinned fetch | SUBSTANTIAL / CONTINUE | real-daemon HTTP pair/connect/scoped-token behavior; explicitly no live ngrok |
| `browse/test/tab-isolation.test.ts` | `698dd1ac8b0c750df4d03632925195e6458e1118` | FULL | own-only versus shared tab-access logic, ownership release |
| `browse/test/token-registry.test.ts` | pinned fetch | SUBSTANTIAL / CONTINUE | scope/token/reduction/reserved-identity behavior |
| `browse/test/cdp-allowlist.test.ts` | `8256e7a198e6e197ca2f70e60f9ff1abb109a661` | FULL | explicit dangerous-method denial and allowlist metadata pins |
| `browse/test/cdp-e2e.test.ts` | `d5d2e26c1b8f08bf531dd4b4bed06b85d153458e` | FULL | real Chromium CDP allow/deny/output behavior |
| `browse/test/url-validation.test.ts` | `7f7fe5949318572935a55c46412a956d04d19994` | FULL | scheme/metadata/file-path and direct-fetch SSRF regression tests |
| `browse/test/session-persist.test.ts` | `bf7bfa8bdec2633d160ff4122f33ede8869f283a` | FULL | serialization/restore controls plus real-Chromium persistence round trip |
| `browse/test/content-security.test.ts` | pinned fetch | SUBSTANTIAL / CONTINUE | envelope/datamark/filter/hidden-content and centralized wrapping checks |
| `browse/test/server-security-surface.test.ts` | `cdfb76c96e982130048acc8fac511d8abb5b7bad` | FULL | removes unfed false-green security state while pinning live L4 path |
| `test/skill-llm-eval*.test.ts` | — | PLANNED | broader behavioral criteria and LLM-judged eval design |
| `test/skill-routing-e2e.test.ts` | — | PLANNED | skill invocation/routing behavior |
| `test/codex-e2e*.test.ts` | — | PLANNED | cross-model contract, including Sol scope |
| `test/gemini-e2e.test.ts` | — | PLANNED | host/model portability evidence |
| `test/llm-judge-recommendation.test.ts` | — | PLANNED | judge/oracle design |
| `test/carve-section-loading.test.ts` | — | PLANNED | runtime section-loading behavior |
| audit/compliance tests | partial via spec + ship + browser security invariants | SUBSTANTIAL / CONTINUE | deterministic policy checks require broader pass |
| eval list/compare/summary/flake/watch/select scripts | — | PLANNED | eval lifecycle and operational feedback |

## Durable study syntheses

| Synthesis | Status | Boundary |
|---|---:|---|
| `syntheses/planning-specification-work-admission.md` | BOUNDED | gstack-native discovery → planning review → spec/work-admission model; not whole-system closure |
| `syntheses/review-qa-ship-delivery-qualification.md` | BOUNDED | implementation → review/QA/test/plan reconciliation → ship-time delivery qualification; not production/deploy closure |
| `syntheses/browser-runtime-security-evidence.md` | BOUNDED | persistent browser execution → capability/isolation/security controls → browser evidence/audit semantics; not independent security certification |

## Evolution / chronology sources

| Source | Status | Note |
|---|---:|---|
| `CHANGELOG.md` (~1.1 MB at pinned revision) | PLANNED / PARTITIONED APPROACH | do not treat as a single linear read unit; partition chronologically/mechanistically and use recent release diffs to reconstruct evolution |
| pinned release commit diff | PLANNED | especially subagent-dispatch / ship behavior changes in v1.79.0.0 |

## Source-fidelity warnings

1. `docs/PROJECT_STRUCTURE.md` is a derived repository-authored view. At least one documented path (`skill/SKILL.md.tmpl`) did not resolve at the pinned revision when directly fetched; path/tree claims must be checked against actual contents.
2. Root/generated `SKILL.md` artifacts must not be substituted for source templates/resolvers when repository instructions identify generated output.
3. A skill template's declared STOP/gate is evidence of intended workflow policy; deterministic template tests strengthen structural confidence but model-level compliance still requires behavioral evidence.
4. First-party tests/evals increase evidence about expected/enforced behavior but are not independent external verification.
5. Cross-model diversity is not automatically verification independence when models share the same plan, diff, framing, orchestration, or first-party oracle.
6. `office-hours` mixes work-design mechanics with YC/founder relationship and promotion behavior. Treat the latter as a separate incentive/retention mechanism; do not use it as evidence for planning quality.
7. `/ship` uses heterogeneous evidence with different failure polarities. “Gate” does not always mean non-overridable blocker, and “always-on” adversarial review does not mean every outside-model pass successfully ran.
8. AI-assessed changed-path coverage is not the same measurement as instrumented line/branch coverage; preserve that distinction.
9. The README/docs lifecycle is a normative system view. Actual `/ship` can skip standalone QA when no executable plan verification is available, so do not infer a universal `Review → QA → Ship` state machine from documentation alone.
10. Pair-agent/tunnel tab ownership is strict under `own-only`, but shared local browser-skill clients intentionally bypass tab ownership as a security boundary; do not generalize isolation across both modes.
11. `browse/src/commands.ts` historical `READ_COMMANDS`/`WRITE_COMMANDS` sets are not the authoritative security capability classification; `token-registry.ts` explicitly reclassifies dangerous side effects.
12. Browser persistence between live-daemon calls is not equivalent to persistence across headless daemon restart; cross-restart persistence is opt-in.
13. Browser security controls have heterogeneous failure polarity: selected CDP/tunnel/URL/path controls hard-deny, while ML classification, audit writes and some file-permission hardening are graceful/best-effort.
14. The inspected pair-agent E2E does not create a live ngrok tunnel; do not upgrade local HTTP ceremony evidence into a claim of hostile public-tunnel validation.
