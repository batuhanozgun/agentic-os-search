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
| `plan-eng-review/sections/review-sections.md.tmpl` | pinned | FULL for synthesis use | architecture/test/perf review |
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
| `ship/sections/pr-body.md` | pinned | SUBSTANTIAL / CONTINUE | PR/release evidence aggregation |
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
| `browse/src/commands.ts` | pinned | SUBSTANTIAL / CONTINUE | command registry; historical read/write taxonomy |
| `browse/src/token-registry.ts` | `89b0a990c31e26188275295e3d2d60f5908c5033` | FULL | scoped authority/revocation |
| `browse/src/snapshot.ts` | pinned | SUBSTANTIAL / CONTINUE | semantic refs/evidence ambiguity |
| `browse/src/cdp-allowlist.ts` | `752ce464c8e9e5d9f697c81a08444d0dd666b1e0` | FULL | deny-default CDP |
| `browse/src/cdp-bridge.ts` | `3d1fa3d8d002656f0e9528001df7b7c6e300b80b` | FULL | locks/timeouts/CDP lifecycle |
| `browse/src/url-validation.ts` | `c9e9c170ac36a6c744f47dee2b3bf15eb49e68f1` | FULL | URL/SSRF controls |
| `browse/src/path-security.ts` | `bc02ccde06c753dcd4b00e3fba49ad87267adb04` | FULL | filesystem path controls |
| `browse/src/file-permissions.ts` | pinned | SUBSTANTIAL / CONTINUE | platform permission hardening |
| `browse/src/session-persist.ts` | `3c6627bcbc0c24e76c519934b0a3a9ba3b87aca9` | FULL | opt-in persistence/restore |
| `browse/src/content-security.ts` | `a185764583f73aaa7b8d979d8ff5942bf63c25f7` | FULL | deterministic content defenses |
| `browse/src/security.ts` | `3da662a008e0785102f6572de468cc8dcb6bc136` | FULL | verdict combiner/dead-state context |
| `browse/src/security-classifier.ts` | `a89ddf694b165872263ed8a2f46e88faa5b3f52f` | FULL | optional fail-open ML defense |
| `browse/src/security-sidecar-client.ts` | `95e226070466df31b6e0db2ef7d93bf50b49b521` | FULL | sidecar timeout/circuit behavior |
| `browse/src/audit.ts` | `f93b47fb090c99c95dd3c83091a0b097330130df` | FULL | best-effort persistent audit |
| `browse/src/activity.ts` | `b15eb45a1d1c2bf5ae57f832418a0d7aa40a0f52` | FULL | bounded live activity/gaps |

---

## Investigation / causal-control sources

| Source | Evidence | Status | Role |
|---|---|---:|---|
| `investigate/SKILL.md.tmpl` | `c7cd9a99ad695f966ef2befaf18b1120eff89535` | FULL | causal workflow/3-strike/verification/learning |
| generated `investigate/SKILL.md` | pinned | SUBSTANTIAL / CONTINUE | rendered context |
| `freeze/SKILL.md.tmpl` | `e6804d91c23d1fd9804097a14adbc21a58745979` | FULL | Edit/Write boundary and non-sandbox caveat |
| `freeze/bin/check-freeze.sh` | `6c6e62e76395a4cb568a13f7578f4222ae0bb26d` | FULL | runtime freeze enforcement |
| `unfreeze/SKILL.md.tmpl` | `88e413fe5a49a45d46d8867b2d80ace30b3b45aa` | FULL | freeze cleanup |
| `bin/gstack-paths` | `5b66e3102ff5c55b76bf88b0a2cdc31ae6b83d56` | FULL | state-root resolution |
| `hosts/define-host.ts` | `0ed190dd00606a69acb0aca990289781f79bbc79` | FULL | external-host frontmatter defaults |
| `hosts/claude.ts` | `5381953cae8040508a260e6e4b3eb39973c92934` | FULL | Claude hook/GBrain behavior |
| `hosts/codex.ts` | `b46e9222495eada3da68debaae6dab6d9d57167c` | FULL | Codex hook suppression |
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
| `bin/gstack-brain-cache` | pinned | SUBSTANTIAL / CONTINUE | cache states/refresh/atomicity/stale fallback; CLI prints non-warm state to stderr |
| `scripts/resolvers/gbrain.ts` | `6c6b66d640187363c0dc12326fe08adfb689c98d` | FULL for current use | skill-specific brain preflight/refresh/writeback; **suppresses cache stderr, losing stale label** |
| `setup-gbrain/SKILL.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | storage/trust/repo-policy consent setup |
| `sync-gbrain/SKILL.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | code/memory/brain sync and failure polarity |
| `bin/gstack-gbrain-repo-policy` | pinned | FULL for current use | normalized per-remote read-write/read-only/deny store; batch fail-closed |
| `lib/gbrain-repo-policy-client.ts` | `890282847a4241e4f79509360de5dc6a33de2505` | FULL | shared TS policy client; caller owns failure polarity |
| `bin/gstack-memory-ingest.ts` | pinned | SUBSTANTIAL / CONTINUE | transcript/artifact ingest; policy filter before write; accounting/state controls |

---

## Shared generation / composition / host sources

| Source | Evidence | Status | Role |
|---|---|---:|---|
| `scripts/gen-skill-docs.ts` | pinned | SUBSTANTIAL / CONTINUE | template→resolver→generated/host overlays |
| `scripts/resolvers/index.ts` | `cee08c2015a6ac2ff8605b02ac07a49d284d3ce1` | FULL | resolver registry |
| `scripts/resolvers/sections.ts` | `c6425e19b93d20018057cf2fe6ae9eeb2f613a18` | FULL | carved section rendering |
| `scripts/resolvers/composition.ts` | `b8d3483d9bd961409025959eddcd8840dd5f98a8` | FULL | parent-child composition |
| broader host adapter set | partial | PLANNED / PARTIAL | dedicated portability cluster later |

---

## Test / eval / verification sources

| Source | Evidence | Status | What it actually supports |
|---|---|---:|---|
| `test/spec-template-invariants.test.ts` | `40d2d22677cbd0a506c6395bc0e2b00b3a2149d2` | FULL | spec structural pins |
| `test/ship-plan-completion-invariants.test.ts` | `26c565b1b093262697832d3b161c479bbb5ce07b` | FULL | ship plan-gate structural pins |
| `test/skill-coverage-matrix.ts` | `7359afbce8144625e3b832d0fa9044fb753185a8` | FULL | per-skill gate/periodic registry |
| `test/skill-coverage-floor.test.ts` | `4f75e370b09c01098fb711ca4332f1370e1e5a10` | FULL | generic structural floor only |
| planning/review/QA/ship live E2Es | recorded in prior study pass | FULL/SUBSTANTIAL | selected agent behavior, oracle/topology varies |
| `browse/test/dual-listener.test.ts` | pinned | SUBSTANTIAL / CONTINUE | exact tunnel structural surface |
| `browse/test/server-factory.test.ts` | pinned | SUBSTANTIAL / CONTINUE | factory/auth/listener behavior |
| `browse/test/server-auth.test.ts` | pinned | SUBSTANTIAL / CONTINUE | auth/tab/chain/activity/tunnel regressions |
| `browse/test/pair-agent-e2e.test.ts` | pinned | SUBSTANTIAL / CONTINUE | real-daemon HTTP pairing, no live ngrok |
| `browse/test/tab-isolation.test.ts` | `698dd1ac8b0c750df4d03632925195e6458e1118` | FULL | own-only vs shared tab policy |
| `browse/test/cdp-allowlist.test.ts` | `8256e7a198e6e197ca2f70e60f9ff1abb109a661` | FULL | dangerous CDP denial pins |
| `browse/test/cdp-e2e.test.ts` | `d5d2e26c1b8f08bf531dd4b4bed06b85d153458e` | FULL | real Chromium CDP behavior |
| `browse/test/url-validation.test.ts` | `7f7fe5949318572935a55c46412a956d04d19994` | FULL | URL/SSRF/direct-fetch regressions |
| `browse/test/session-persist.test.ts` | `bf7bfa8bdec2633d160ff4122f33ede8869f283a` | FULL | real Chromium persistence roundtrip |
| `browse/test/server-security-surface.test.ts` | `cdfb76c96e982130048acc8fac511d8abb5b7bad` | FULL | false-green security-status removal |
| `test/investigate-freeze-path.test.ts` | `7b9ef0cae733b872f188588f6d1fee3125e41fb8` | FULL | investigate hook-path regression |
| `test/hook-scripts.test.ts` | `55817099a5380b6d7170a53adc9ae4e9351ec4e4` | SUBSTANTIAL / CONTINUE | freeze/careful shell behavior |
| investigate causal-workflow E2E | matrix | ABSENT / NEGATIVE | no registered direct behavioral E2E |
| `test/context-save-hardening.test.ts` | pinned | SUBSTANTIAL / CONTINUE | save sanitization/collision + restore branch/order/cap shell logic |
| `test/skill-e2e-context-skills.test.ts` | pinned | SUBSTANTIAL / CONTINUE | real skill save→restore/list/branch behavior |
| `test/learnings.test.ts` | `e43fe7c04969f287ebab171baced4a9944601119` | SUBSTANTIAL / CONTINUE | real logger/search append, decay, latest-winner, injection checks |
| `test/gstack-learnings-search.test.ts` | `ffa0227aed5afe0d2f4656f18b49cc2d8b344a45` | FULL | cross-project trusted-only + query behavior |
| `test/learnings-injection.test.ts` | `f5b5191f4eca3c3cc53be1b5872a647dbbb2e35b` | PLANNED / REFERENCED | dedicated learning-injection suite exists; current synthesis already has logger regression evidence |
| `test/skill-e2e-learnings.test.ts` | `8672ef3c2a2ab1fe2caaa0bd76c7098df747168e` | FULL | real-agent basic `/learn` retrieval |
| `test/brain-cache-spec.test.ts` | pinned | FULL for current use | entity/scope/TTL/budget/trust constants |
| `test/brain-cache-roundtrip.test.ts` | pinned | FULL for current use | warm/missing/stale-fallback/meta/endpoint state machine |
| separate stale-but-usable test file referenced by comments | search | ABSENT / NEGATIVE | current source comments stale; behavior covered in roundtrip suite |
| `test/brain-preflight.test.ts` | pinned | FULL | planning-only preflight/subsets/writeback/invalidation wiring |
| `test/skill-preflight-budget.test.ts` | pinned | FULL | resolver instruction budgets + autoplan aggregate |
| `test/autoplan-preflight-budget.test.ts` referenced in spec comment | fetch 404 | ABSENT / NEGATIVE | stale comment; equivalent current assertions exist elsewhere |
| `test/salience-allowlist.test.ts` | pinned | FULL | privacy-prefix allowlist behavior |
| `test/gbrain-repo-policy-client.test.ts` | pinned | FULL | real Bash/TS policy, corrupt batch fail-closed, normalization parity |
| broader LLM judge/routing/Codex/Gemini/eval lifecycle tests | — | PLANNED | later eval/portability cluster |

---

## Durable subsystem syntheses

| Synthesis | Status | Boundary |
|---|---:|---|
| `syntheses/planning-specification-work-admission.md` | BOUNDED | discovery → planning → spec/work admission |
| `syntheses/review-qa-ship-delivery-qualification.md` | BOUNDED | implementation → review/QA/test/ship qualification |
| `syntheses/browser-runtime-security-evidence.md` | BOUNDED | browser execution → capability/security → evidence |
| `syntheses/investigation-root-cause-debug-control.md` | BOUNDED | failure → causal hypothesis → bounded fix → fresh verification/learning |
| `syntheses/memory-learnings-context-gbrain.md` | BOUNDED | prior state → qualification/trust/cache → current context/reuse |

---

## Evolution / chronology

| Source | Status | Note |
|---|---:|---|
| `CHANGELOG.md` (~1.1 MB pinned) | PLANNED / PARTITIONED | use chronological/mechanistic partitions |
| pinned v1.79 release commit/diff | NEXT-CLUSTER RELEVANT | subagent dispatch/stranded-run behavior relevant to multi-agent synthesis |

---

## Protected source-fidelity warnings

1. Derived repository docs do not override actual pinned source/tree.
2. Generated `SKILL.md` does not replace `.tmpl`/resolver provenance.
3. Skill prose is intended workflow policy, not automatically executed behavior.
4. First-party tests/evals are not independent verification.
5. Cross-model diversity is not automatically independent verification.
6. Office-hours promotion/relationship behavior is separate from planning-quality evidence.
7. Ship evidence channels have heterogeneous failure polarity; “gate” is not one semantics.
8. AI-assessed changed-path coverage is not instrumented coverage.
9. Pair-agent own-only tab isolation does not generalize to shared local clients.
10. Browser command historical READ/WRITE sets are not security capability authority.
11. Browser state continuity between calls is not default headless cross-daemon persistence.
12. Live public ngrok behavior was not reproduced by inspected E2E.
13. Investigate causal workflow has no registered direct behavioral E2E; freeze is better tested.
14. Investigate freeze is Edit/Write-specific, host-specific and not automatically cleared by investigate.
15. Investigate `root cause` does not guarantee systemic prevention/detection depth.
16. Context checkpoints are LLM-authored continuity representations and are not automatically source-revalidated on restore.
17. Local learnings are sourced/decayed candidate evidence, not automatic truth.
18. GBrain cache qualification can be lost in representation: `stale-fallback` is printed on stderr but planning preflight suppresses stderr and injects content only.
19. A stale brain-cache spec comment points to a non-existent autoplan budget test; actual current tests win.
20. Repo trust policy is an actual ingest control; unattended unreadable policy state fails closed before transcript writes.
