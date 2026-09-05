# gstack Study — Source Ledger

## Canonical target

Unless stated otherwise, sources refer to:

`garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`

Observed 2026-09-05.

## Status legend

- **FULL** — source read as a whole with enough visibility for current synthesis use.
- **SUBSTANTIAL / CONTINUE** — meaningful source coverage; re-enter before stronger whole-file claims.
- **INVENTORY** — topology/metadata inspected only.
- **PLANNED** — relevant source not yet substantively read.
- **ABSENT / NEGATIVE** — searched-for evidence/surface does not exist at the pinned revision or registered matrix.
- **BOUNDED NEGATIVE** — targeted search did not find the surface; not a universal proof of absence outside searched repository scope.

`FULL` is read coverage, not independent verification.

---

## Orientation / governing sources

| Source | Blob / evidence | Status | Role |
|---|---|---:|---|
| `AGENTS.md` | `7d802490e95cb7d6f19f9328d20223d6ce696ee9` | FULL | repo source-of-truth, generation, testing/security rules |
| `CLAUDE.md` | `115a5228277d6a5ecae31c3dc86b76802a739f62` | FULL | detailed repository/eval/release contract |
| `ETHOS.md` | pinned | FULL | behavioral philosophy |
| `DESIGN.md` | pinned | FULL | visual/design artifact policy |
| `ARCHITECTURE.md` | `374dd8774bd08657cb15987182596a7630bfae47` | FULL | runtime/browser/daemon/security architecture |
| `BROWSER.md` | pinned | SUBSTANTIAL / CONTINUE | browser operator/architecture view |
| `docs/PROJECT_STRUCTURE.md` | pinned | FULL | derived structure view; actual tree wins |
| `package.json` | pinned, v1.79.0 | FULL | runtime/test/eval commands and dependencies |
| root `SKILL.md.tmpl` | `402bd0d7b0f2bf02f6c9e4754e0e2a655f5f4057` | FULL | intent router |
| root tree/contents | pinned GitHub tree | INVENTORY | actual repository topology |

---

## Planning / specification / work-admission sources

| Source | Evidence | Status | Role |
|---|---|---:|---|
| `office-hours/SKILL.md.tmpl` | `ecd96fb4186115182a653f67e59c1dc7496ed326` | FULL | discovery, premise/alternative qualification |
| `office-hours/sections/manifest.json` | `fa6df52648ceca8ea427056d73000c8a7d6cd870` | FULL | section registry |
| `office-hours/sections/phase-2a-startup-diagnostic.md.tmpl` | `0e3a12274d5cbd2845130e529aec6f9118b7d479` | FULL | forcing/evidence questions |
| `office-hours/sections/phase-2b-builder-brainstorm.md.tmpl` | `e49d6cd80b61b8b12cfc6e3d372b8b8c0857134b` | FULL | builder/generative mode |
| `office-hours/sections/design-and-handoff.md.tmpl` | `5924dd706a141a77d96ea05aec998e6ddbaae5b9` | SUBSTANTIAL / CONTINUE | design lineage, approval, handoff, memory/promotion surfaces |
| `plan-ceo-review/SKILL.md.tmpl` | `1b1affe160d2919ee08e00f101784a97d210906a` | FULL | scope/ambition/authority |
| `plan-ceo-review/sections/manifest.json` | `5ef4425a943600708ff1d0fdb9352f2a97c07de9` | FULL | section registry |
| `plan-ceo-review/sections/review-sections.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | full-depth review findings/gates |
| `plan-eng-review/SKILL.md.tmpl` | `e066e2c5f5028ad3b8485fe8606967ac1188b47e` | FULL | target/scope authority |
| `plan-eng-review/sections/manifest.json` | `f76e8f95bf4b313cecc2797278440cfc8f0a90a5` | FULL | section registry |
| `plan-eng-review/sections/review-sections.md.tmpl` | pinned | FULL for synthesis use | architecture/test/perf review + optional worktree-parallelization planning |
| `autoplan/SKILL.md.tmpl` | `6a034e15e7647980d74dfa71bfe17c25875ed054` | SUBSTANTIAL / CONTINUE | delegated decisions and audit |
| `spec/SKILL.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | why/scope/code-evidence/spec spine |
| `spec/sections/gate-and-file.md.tmpl` | `f8923a834e9228d42b4e535ed8b97cb52e0e5a6d` | FULL | quality/redaction/sink/issue/archive/spawn controls |

---

## Review / QA / delivery qualification sources

| Source | Evidence | Status | Role |
|---|---|---:|---|
| `review/SKILL.md.tmpl` | `a1d6a172746bdc4905731fe4e96ffb6976a579e9` | FULL | diff review/Fix-First |
| `review/sections/manifest.json` | `26a94ca3a7ed431514d857d9b6bd758afa859e88` | FULL | section registry |
| `review/sections/plan-completion.md.tmpl` | `7a7ae47e4ae31f1e28991bf7b233fc665f2ad4a8` | FULL | standalone plan audit policy |
| `review/sections/plan-completion.md` | `38da1ae08b0d966004d522b74af3f48ffceadcf3` | FULL | generated audit implementation |
| `ship/SKILL.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | delivery orchestration |
| `ship/sections/manifest.json` | `e4394e5623f9421972c9be642f7d202760af866d` | FULL | ship section registry |
| `ship/sections/tests.md` | pinned | SUBSTANTIAL / CONTINUE | merged-code tests/failure ownership |
| `ship/sections/test-coverage.md` | pinned | SUBSTANTIAL / CONTINUE | semantic path coverage |
| `ship/sections/plan-completion.md` | `2c36cefe477d68768a5623090c9a90835427ae5f` | FULL | ship-time plan control |
| `ship/sections/review-army.md` | `bb1c3b82910ebaccf1beecfa10bf0771cc777601` | SUBSTANTIAL / CONTINUE | fresh specialists/red-team/fix loop |
| `ship/sections/adversarial.md` | `254331b9f615a09dc6e96deb952d622fe54bcd32` | FULL | Claude/Codex adversarial challenge |
| `ship/sections/pr-body.md` | pinned | SUBSTANTIAL / CONTINUE | PR/release evidence aggregation + spawned doc-sync handoff/recovery |
| `qa-only/SKILL.md.tmpl` | `75c4123cc5c406ffdd36c71a094335c137135b1e` | FULL | browser report-only evidence |
| `qa/SKILL.md.tmpl` | `d15a0c5d151ec6a8b15cd3a31dc96430ddb91909` | FULL | browser fix/verify loop |
| `scripts/resolvers/utility.ts` QA methodology | `911b01d8f7e5264a759cfa878c440e7f642eb7cb` | FULL for use | shared QA methodology |
| `scripts/resolvers/review.ts` dashboard | `04f2dee0091e768ad1a11feda9f3a824256bfb45` | FULL for use | review standing/freshness |

---

## Browser runtime / security / evidence sources

| Source | Evidence | Status | Role |
|---|---|---:|---|
| `browse/SKILL.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | browser contract/evidence caveats |
| `browse/src/server.ts` | pinned | SUBSTANTIAL / CONTINUE | daemon/listeners/auth/dispatch/security/audit |
| `browse/src/browser-manager.ts` | pinned | SUBSTANTIAL / CONTINUE | browser lifecycle/tab ownership |
| `browse/src/tab-session.ts` | `dccabf28f4263cb77d0a594369bb15f3e2c7ad73` | FULL | per-tab state/ref invalidation |
| `browse/src/token-registry.ts` | `89b0a990c31e26188275295e3d2d60f5908c5033` | FULL | scoped authority/revocation |
| `browse/src/cdp-allowlist.ts` | `752ce464c8e9e5d9f697c81a08444d0dd666b1e0` | FULL | deny-default CDP |
| `browse/src/cdp-bridge.ts` | `3d1fa3d8d002656f0e9528001df7b7c6e300b80b` | FULL | locks/timeouts/CDP lifecycle |
| `browse/src/url-validation.ts` | `c9e9c170ac36a6c744f47dee2b3bf15eb49e68f1` | FULL | URL/SSRF controls |
| `browse/src/path-security.ts` | `bc02ccde06c753dcd4b00e3fba49ad87267adb04` | FULL | filesystem path controls |
| `browse/src/session-persist.ts` | `3c6627bcbc0c24e76c519934b0a3a9ba3b87aca9` | FULL | opt-in persistence/restore |
| `browse/src/content-security.ts` | `a185764583f73aaa7b8d979d8ff5942bf63c25f7` | FULL | deterministic content defenses |
| `browse/src/security.ts` | `3da662a008e0785102f6572de468cc8dcb6bc136` | FULL | verdict combiner/dead-state context |
| `browse/src/security-classifier.ts` | `a89ddf694b165872263ed8a2f46e88faa5b3f52f` | FULL | optional fail-open ML defense |
| `browse/src/audit.ts` | `f93b47fb090c99c95dd3c83091a0b097330130df` | FULL | best-effort persistent audit |
| `browse/src/activity.ts` | `b15eb45a1d1c2bf5ae57f832418a0d7aa40a0f52` | FULL | bounded live activity/gaps |

---

## Investigation / causal-control sources

| Source | Evidence | Status | Role |
|---|---|---:|---|
| `investigate/SKILL.md.tmpl` | `c7cd9a99ad695f966ef2befaf18b1120eff89535` | FULL | causal workflow/3-strike/verification/learning |
| `freeze/SKILL.md.tmpl` | `e6804d91c23d1fd9804097a14adbc21a58745979` | FULL | Edit/Write boundary and non-sandbox caveat |
| `freeze/bin/check-freeze.sh` | `6c6e62e76395a4cb568a13f7578f4222ae0bb26d` | FULL | runtime freeze enforcement |
| `unfreeze/SKILL.md.tmpl` | `88e413fe5a49a45d46d8867b2d80ace30b3b45aa` | FULL | freeze cleanup |
| `bin/gstack-paths` | `5b66e3102ff5c55b76bf88b0a2cdc31ae6b83d56` | FULL | state-root resolution |
| OpenClaw investigate adaptation | pinned | FULL | causal phases without freeze |

---

## Memory / learnings / context / GBrain sources

| Source | Evidence | Status | Role / key finding |
|---|---|---:|---|
| `context-save/SKILL.md.tmpl` | `a3702bc95439cddd87841aba836708bf511ef55d` | FULL for synthesis use | explicit append-only context checkpoint |
| `context-restore/SKILL.md.tmpl` | `d2e78ca8976b96df3077bce57ab5396ad7e4afd2` | FULL for synthesis use | branch-aware restore/fallback; summary not source-revalidated |
| `learn/SKILL.md.tmpl` | `90d08d2298cccd0d5090f194a2cd76a5361b4323` | FULL for synthesis use | learning show/search/add/prune/export/stats |
| `scripts/resolvers/learnings.ts` | `aefc0fb864a3b19ee33b6253e1dbf7228ce2ba82` | FULL | learning schema/search/log prompt contract |
| `bin/gstack-learnings-log` | `3c47ebb80a4285028cf7c54549038553b81c5eb4` | FULL | validation/injection filter/trust mark/append |
| `bin/gstack-learnings-search` | `d7038e821881861f9661af2f34f3728bf1cabe23` | FULL | decay/latest-winner/query/cross-project trust |
| `scripts/brain-cache-spec.ts` | `eab2f9588776f7d3d9c734d9dcd2e1a52ba6879f` | FULL for synthesis use | canonical entity scope/TTL/budget/invalidation spec |
| `bin/gstack-brain-cache` | pinned | SUBSTANTIAL / CONTINUE | cache states/refresh/atomicity/stale fallback |
| `scripts/resolvers/gbrain.ts` | `6c6b66d640187363c0dc12326fe08adfb689c98d` | FULL for current use | **suppresses cache stderr, losing stale label** |
| `bin/gstack-gbrain-repo-policy` | pinned | FULL for current use | per-remote read-write/read-only/deny store; batch fail-closed |
| `lib/gbrain-repo-policy-client.ts` | `890282847a4241e4f79509360de5dc6a33de2505` | FULL | shared TS policy client |
| `bin/gstack-memory-ingest.ts` | pinned | SUBSTANTIAL / CONTINUE | transcript/artifact ingest policy filtering |

---

## Multi-agent / cross-model coordination sources

| Source | Evidence | Status | Role / key finding |
|---|---|---:|---|
| pinned v1.79 commit `0d1bd...` | commit message/diff | FULL for synthesis use | third stranded-parent recurrence; foreground fix/recovery/TODOs |
| `scripts/resolvers/constants.ts` | `4e94b986eff9a526eae24acead228e50dafb8bd8` | FULL for synthesis use | foreground dispatch + Codex availability semantics |
| `test/run-in-background-guidance.test.ts` | `bd0f1e42d95c0ac96ec40cda7a89112cd2c1f749` | FULL | cross-carrier structural pin/scanner |
| `ship/sections/pr-body.md` | pinned | FULL for multi-agent use | spawned docs child, JSON contract, timeout/cancel/reconcile |
| `document-release/SKILL.md` | pinned | SUBSTANTIAL / CONTINUE | spawned-session decision semantics |
| `test/skill-e2e-ship-docsync.test.ts` | pinned | FULL | actual dispatch/foreground behavioral pin |
| `test/skill-e2e-docsync-spawned.test.ts` | pinned | FULL | spawned child gate + JSON contract |
| `review/sections/review-army.md` | `f37fb5d738106c063bdcf784078535d714723bc5` | FULL for synthesis use | parallel specialist aggregation |
| `test/skill-e2e-review-army.test.ts` | pinned | SUBSTANTIAL / CONTINUE | checklist/output behavior; weak topology proof |
| `ship/sections/adversarial.md` | pinned | FULL for current use | same-family + Codex challenge |
| `codex/SKILL.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | outside-model workflow/nesting guard |
| `test/codex-under-codex-detection.test.ts` | `b2428244eaf6fab4be0ce86a914594987a643c70` | FULL | same-model nesting detection |
| Autoplan phase sections | pinned SHAs in synthesis | FULL for synthesis use | deliberately asymmetric Claude/Codex context |
| `test/skill-e2e-autoplan-dual-voice.test.ts` | `1efc6dfc68643fa2772770ea9b87187986612e99` | FULL | periodic actual dual-voice invocation/liveness |
| `cso/SKILL.md` | pinned | SUBSTANTIAL / CONTINUE | fresh verifier pattern |
| `test/skill-e2e-cso.test.ts` | `5f58a45d053b450d958c16696ec65fa8e393a60c` | FULL for current use | selected live verifier behavior |
| `design-shotgun/SKILL.md` | pinned | SUBSTANTIAL / CONTINUE | parallel generative fan-out |
| dedicated Design Shotgun E2E | targeted search | ABSENT / NEGATIVE | no dedicated production-topology E2E found |
| `pair-agent/SKILL.md.tmpl` | `2f66ec44b63ba24e6a0ba4023a042f66342edefc` | FULL for synthesis use | remote/local browser capability delegation |
| `plan-eng-review/sections/review-sections.md` | pinned | SUBSTANTIAL / CONTINUE | optional worktree parallelism |
| `hosts/define-host.ts` | `0ed190dd00606a69acb0aca990289781f79bbc79` | FULL | host tool rewrite model |
| `hosts/codex.ts` | `b46e9222495eada3da68debaae6dab6d9d57167c` | FULL | Codex host suppression / Agent mismatch context |
| pinned `TODOS.md` dispatch items | pinned | SUBSTANTIAL / CONTINUE | host dispatch defect + runtime foreground follow-up |

---

## Guarded-action / security-review sources

| Source | Evidence | Status | Role / key finding |
|---|---|---:|---|
| `careful/SKILL.md.tmpl` | `8fba18fb0bc699d68058bb569a55a2aa535ebb93` | FULL | Claude Bash PreToolUse safety contract; MEDIUM ask + narrow HIGH deny |
| `careful/bin/check-careful.sh` | `b6bebb9d3cc74758a292dd779361a7b5f49fff0b` | FULL for synthesis use | parser/obfuscation/safe-exception/destructive-pattern enforcement |
| `guard/SKILL.md.tmpl` | `d4c78be492ed24425a763008c975bd5e4569a5ee` | FULL | composition of careful Bash + freeze Edit/Write hooks |
| `freeze/bin/check-freeze.sh` | `6c6e62e76395a4cb568a13f7578f4222ae0bb26d` | FULL | path deny control reused by guard |
| `test/hook-scripts.test.ts` | pinned | FULL for careful synthesis use | realistic parser/bypass/HIGH deny/MEDIUM ask/safe-command regressions |
| `scripts/gen-skill-docs.ts` | `0be3ca9a126d0e3ad0f9cf76b641f15a728307c0` | FULL for safety-prose path | external-host hook extraction → Safety Advisory prose |
| `test/gen-skill-docs.test.ts` | `cc4a8eaaf982d86c0dd8d21965f689431f65168f` | SUBSTANTIAL / CONTINUE | external hook skills have safety prose and no hooks frontmatter |
| `scripts/one-way-doors.ts` | `61c0b24eaeec133afa399cd032d2106597bc4ff8` | FULL | typed-registry-first / keyword-fallback destructive decision classification |
| `hosts/claude/hooks/question-preference-hook.ts` | `3e488363f005659e65f271445e46d06741a97795` | FULL for current use | never-ask enforcement; one-way safety override; refuse-on-ambiguous |
| `test/plan-tune.test.ts` | `4eb9483ba2f808810f454b7011785afc704ff20f` | FULL for safety registry use | critical questions asserted one-way; registry consistency |
| `test/question-preference-hook.test.ts` | pinned | SUBSTANTIAL / CONTINUE | one-way overrides never-ask; destructive ad-hoc keyword net; ambiguity pass-through |
| `cso/SKILL.md` | `d16aef3278eede8f2b5377ed7d2798c8f5c11eff` | FULL for Phase 12-14 synthesis use | FP filters, active verification, confidence/status, source-quote gate, report/trend |
| `test/skill-e2e-cso.test.ts` | `5f58a45d053b450d958c16696ec65fa8e393a60c` | FULL | full/diff/infra live audit; diff path records real verifier child |
| `.gstack/security-reports` consumers | targeted repo search | BOUNDED NEGATIVE | found in CSO source/template/E2E; no separate live ship/deploy gate found in targeted search |

---

## Host adapters / portability-fidelity sources

| Source | Evidence | Status | Role / key finding |
|---|---|---:|---|
| `hosts/index.ts` | `cc1c213b532a5abb3bdf95a292a3a422c2faa1f8` | FULL | ten-host registry and host lookup/alias model |
| `scripts/host-config.ts` | `378a24e2fefc500e166c848580e60dba8a8e242a` | FULL | typed HostConfig + validators |
| `hosts/define-host.ts` | `0ed190dd00606a69acb0aca990289781f79bbc79` | FULL | common defaults, cross-model/GBrain suppression sets, tool rewrites |
| `hosts/claude.ts` | `5381953cae8040508a260e6e4b3eb39973c92934` | FULL | primary host semantics, hook-preserving frontmatter, full learnings |
| `hosts/codex.ts` | `b46e9222495eada3da68debaae6dab6d9d57167c` | FULL | gpt default, metadata, path rewrites, cross-model suppression, boundary instruction |
| `hosts/factory.ts` | `9161d7fafa0c02dd8721051a357d1bd76fc2f856` | FULL | sensitive metadata + generic tool-language rewrites |
| `hosts/kiro.ts` | `05d4b9ee512fe317299732d4573bce70cd27602f` | FULL | path adaptation |
| `hosts/opencode.ts` | `fcba39d91f0a7b14dd1b272a4c1e295a75fc2a07` | FULL | expanded runtime-root asset set |
| `hosts/slate.ts` | `99fa7197ab27f478f29d84d3a3d76f790b5331af` | FULL | registry/generation config despite non-first-class setup standing |
| `hosts/cursor.ts` | `e0d38db8a8c8bb2f05f9ca923c6fa3c715018d7e` | FULL | default host config; first-class setup arm exists separately |
| `hosts/openclaw.ts` | `6248e0587f083640b0b747ebff7eac90e90b258e` | FULL | sessions_spawn-style rewrites, cross-model/GBrain suppression, instruction tier |
| `hosts/hermes.ts` | `cf140fae79bd69114b966def75960b2bfc13f339` | FULL | terminal/patch/delegate_task rewrites; GBrain enabled; instruction tier |
| `hosts/gbrain.ts` | `32dfaa349ef5f67b9f5f642e2c979c63ee79e1ea` | FULL | brain-aware resolver retention, cross-model suppression |
| `scripts/models.ts` | `e7bdf3d2f4e32da7139e710ef50714572842160a` | FULL | explicit `host != model`; model family/overlay normalization |
| `scripts/resolvers/model-overlay.ts` | pinned | SUBSTANTIAL / CONTINUE | model-specific behavior patch generation |
| `scripts/gen-skill-docs.ts` | `0be3ca9a126d0e3ad0f9cf76b641f15a728307c0` | FULL for portability synthesis | host compilation, frontmatter transform, suppression, rewrites, external section inlining, safety prose |
| `docs/ADDING_A_HOST.md` | `d699816df9d63ee964a4d8184fb2b9528012526d` | FULL | intended declarative architecture; **overstates setup integration at pinned revision** |
| `scripts/host-config-export.ts` | `35a0b91927dc38c8b45f4b8cf614d89ab1ba98bb` | FULL | explicit statement that setup is NOT yet wired to registry and hand-rolls host lists |
| root `setup` | pinned | SUBSTANTIAL / CONTINUE | actual install/support tiers, host-specific runtime roots, sidecars, auto detection, model detection |
| `scripts/skill-check.ts` | `9182737ee19e83855a622a90d3cb6e00ac793b73` | FULL | generated-host path/freshness health, not runtime behavioral parity |
| `test/host-config.test.ts` | pinned | FULL for current use | config/index/export/golden structural validation |
| `test/gen-skill-docs.test.ts` | pinned | FULL for portability use | all-host render, YAML/path/frontmatter/suppression/model/static host checks |
| `test/fixtures/golden/codex-ship-SKILL.md` | pinned | SUBSTANTIAL / CONTINUE | Codex generated-view regression surface |
| `test/fixtures/golden/factory-ship-SKILL.md` | pinned | SUBSTANTIAL / CONTINUE | Factory generated-view regression surface |
| `test/helpers/codex-session-runner.ts` | pinned | SUBSTANTIAL / CONTINUE | real Codex CLI behavioral harness |
| `test/codex-e2e.test.ts` | pinned | SUBSTANTIAL / CONTINUE | real Codex workflow behavior |
| `test/codex-e2e-sol-scope.test.ts` | pinned | SUBSTANTIAL / CONTINUE | full generated Sol profile behavior / scope termination |
| pinned `TODOS.md` Codex periodic CI item | pinned | FULL for negative finding | CI image lacks Codex CLI; shards skip all and report green |
| pinned `TODOS.md` non-Claude dispatch audit | pinned | FULL for known gap | every subagent site still needs per-host native/inline/suppress decision |
| pinned `TODOS.md` setup host-function dedup | pinned | FULL for drift finding | near-verbatim runtime-root/link functions drift independently |
| Factory/Droid real-host E2E | targeted repo search | BOUNDED NEGATIVE | no dedicated real-host behavioral runner found; static generation evidence found |
| Kiro real-host E2E | targeted repo search | BOUNDED NEGATIVE | no dedicated real-host behavioral runner found; setup/static evidence found |
| OpenCode real-host E2E | targeted repo search | BOUNDED NEGATIVE | no dedicated real-host behavioral runner found; setup/static evidence found |
| Cursor real-host E2E | targeted repo search | BOUNDED NEGATIVE | no dedicated real-host behavioral runner found; setup/static evidence found |
| OpenClaw/Hermes full install/runtime parity | setup + targeted search | BOUNDED NEGATIVE / DIFFERENT CONTRACT | setup explicitly exposes methodology/instruction-tier path rather than same full install |

---

## Shared generation / composition sources

| Source | Evidence | Status | Role |
|---|---|---:|---|
| `scripts/gen-skill-docs.ts` | `0be3ca9a126d0e3ad0f9cf76b641f15a728307c0` | FULL for current use | template→resolver→host/model-specific output |
| `scripts/resolvers/index.ts` | `cee08c2015a6ac2ff8605b02ac07a49d284d3ce1` | FULL | resolver registry |
| `scripts/resolvers/sections.ts` | `c6425e19b93d20018057cf2fe6ae9eeb2f613a18` | FULL | carved section rendering |
| `scripts/resolvers/composition.ts` | `b8d3483d9bd961409025959eddcd8840dd5f98a8` | FULL | parent-child composition |

---

## Test / eval / verification sources

| Source | Status | What it actually supports |
|---|---:|---|
| `test/spec-template-invariants.test.ts` | FULL | spec structural pins |
| `test/ship-plan-completion-invariants.test.ts` | FULL | ship plan-gate structural pins |
| `test/skill-coverage-matrix.ts` | FULL | gate/periodic registry |
| `test/skill-coverage-floor.test.ts` | FULL | generic structural floor only |
| browser security/runtime tests recorded above | FULL/SUBSTANTIAL | real daemon/Chromium/auth/permission behaviors, not external pen test |
| investigate causal-workflow E2E | ABSENT / NEGATIVE | no direct registered behavioral E2E |
| context/learnings/brain-cache tests recorded above | FULL/SUBSTANTIAL | persistence/decay/trust/cache state machine |
| multi-agent tests recorded above | FULL/SUBSTANTIAL | topology strength varies by site |
| `test/hook-scripts.test.ts` | FULL for careful use | direct shell-hook outputs and safety regression cases |
| `test/plan-tune.test.ts` | FULL for safety use | one-way typed registry invariants |
| `test/question-preference-hook.test.ts` | SUBSTANTIAL / CONTINUE | deterministic AUQ preference/safety interposition |
| `test/gen-skill-docs.test.ts` | FULL for portability use | all-host generated-surface behavior; not actual-host equivalence |
| `test/host-config.test.ts` | FULL | declarative config validation and golden structural contract |
| `test/skill-e2e-cso.test.ts` | FULL for current use | selected real-agent security audit behavior and report persistence |
| Codex CLI E2Es | SUBSTANTIAL / CONTINUE | real Codex behavior locally/when runtime exists; periodic CI has known all-skip gap |
| Factory/Kiro/OpenCode/Cursor real-host E2E | BOUNDED NEGATIVE | no comparable dedicated runners found in targeted repository search |
| broader LLM judge/routing/compliance/flake lifecycle tests | PLANNED | dedicated later eval cluster |

---

## Durable subsystem syntheses

| Synthesis | Status | Boundary |
|---|---:|---|
| `syntheses/planning-specification-work-admission.md` | BOUNDED | discovery → planning → spec/work admission |
| `syntheses/review-qa-ship-delivery-qualification.md` | BOUNDED | implementation → review/QA/test/ship qualification |
| `syntheses/browser-runtime-security-evidence.md` | BOUNDED | browser execution → capability/security → evidence |
| `syntheses/investigation-root-cause-debug-control.md` | BOUNDED | failure → causal hypothesis → bounded fix → fresh verification/learning |
| `syntheses/memory-learnings-context-gbrain.md` | BOUNDED | prior state → qualification/trust/cache → current context/reuse |
| `syntheses/multi-agent-cross-model-coordination.md` | BOUNDED | dispatch/context/authority → child execution/result → liveness/continuation |
| `syntheses/guarded-action-security-review.md` | BOUNDED | preventive action interposition + one-way authority + security evidence standing |
| `syntheses/host-adapters-portability-fidelity.md` | BOUNDED | host/model compilation → install/runtime materialization → behavioral portability standing |

---

## Evolution / chronology

| Source | Status | Note |
|---|---:|---|
| `CHANGELOG.md` (~1.1 MB pinned) | PLANNED / PARTITIONED | use chronological/mechanistic partitions |
| pinned v1.79 release commit/diff | READ / SYNTHESIZED | stranded-subagent recurrence informs liveness/systemic cause |

---

## Protected source-fidelity warnings

1. Derived repository docs do not override actual pinned source/tree.
2. Generated `SKILL.md` does not replace `.tmpl`/resolver provenance.
3. Skill prose is intended workflow policy, not automatically executed behavior.
4. First-party tests/evals are not independent verification.
5. Same-family fresh-context and cross-model diversity are not automatically independent verification.
6. AI-assessed changed-path coverage is not instrumented coverage.
7. Pair-agent own-only tab isolation does not generalize to filesystem/worktree isolation.
8. Browser state continuity is not default cross-daemon persistence.
9. Investigate causal workflow is less behaviorally tested than freeze enforcement.
10. Context checkpoints are LLM-authored continuity views, not automatically current truth.
11. Local learnings are fallible sourced/decayed evidence.
12. GBrain `stale-fallback` qualification is lost when planning preflight suppresses stderr.
13. Review Army E2Es often inline specialist logic rather than real parallel dispatch.
14. Fresh context is not side-effect isolation; Step 18 child shares working tree.
15. v1.79 foreground guidance is not yet a universal runtime-enforced invariant.
16. Claude-host Agent semantics do not automatically port to other hosts.
17. `/careful` HIGH deny is explicitly best-effort/session-scoped, not a universal policy boundary.
18. `/guard` is careful+freeze composition, not a complete sandbox.
19. External-host careful/freeze/guard can degrade from PreToolUse enforcement to Safety Advisory prose.
20. CSO “read-only” is authored behavior, not an inspected source-write sandbox.
21. CSO confidence/status is an audit representation, not externally calibrated probability.
22. Historical `.gstack/security-reports` are not automatically current security truth or delivery gates.
23. One-way typed registry is the primary destructive-decision source; keyword prose classification is only defense-in-depth.
24. Host registry membership, generated-file freshness and actual runtime support are separate standings.
25. `docs/ADDING_A_HOST.md` is stale/aspirational where it says setup is already fully config-driven; `host-config-export.ts` + actual `setup` win.
26. Host and model are independent axes; do not infer model behavior from host identity alone.
27. External-host section inlining changes context/loading topology even where logical content is preserved.
28. A green Codex periodic shard can currently mean “all tests skipped”; job color is not proof that the intended runtime oracle executed.
29. Targeted absence of non-Codex external-host E2E runners is a bounded repository finding, not proof about external/private validation.
