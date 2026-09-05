# gstack Study — Source Ledger

## Canonical target

Unless stated otherwise, sources refer to:

`garrytan/gstack@0d1bd5616c0ef096bb7ccee336f63c60ee408618`

Observed 2026-09-05.

## Status legend

- **FULL** — source read as a whole with enough visibility for current use.
- **SUBSTANTIAL / CONTINUE** — meaningful portion read; re-enter before whole-source/load-bearing claims beyond current use.
- **INVENTORY** — topology/metadata inspected, not substantive source reading.
- **PLANNED** — relevant source not yet read in this study pass.

`FULL` is read coverage, not independent verification.

## Orientation / governing sources

| Source | Blob / evidence ref | Status | Current role |
|---|---|---:|---|
| `AGENTS.md` | `7d802490e95cb7d6f19f9328d20223d6ce696ee9` | FULL | repository development/source-of-truth/security/test contract |
| `CLAUDE.md` | `115a5228277d6a5ecae31c3dc86b76802a739f62` | FULL | detailed generation/eval/release/repository control |
| `ETHOS.md` | pinned source | FULL | cross-skill behavioral philosophy |
| `DESIGN.md` | pinned source | FULL | visual artifact policy |
| `ARCHITECTURE.md` | `374dd8774bd08657cb15987182596a7630bfae47` | FULL | runtime/browser/daemon/security architecture |
| `BROWSER.md` | pinned source | SUBSTANTIAL / CONTINUE | repository-authored browser view; implementation cross-check required |
| `docs/PROJECT_STRUCTURE.md` | pinned source | FULL | derived structure view; actual tree wins on conflicts |
| `package.json` | pinned source; v1.79.0 | FULL | dependencies, commands, tests/evals |
| root `SKILL.md.tmpl` | `402bd0d7b0f2bf02f6c9e4754e0e2a655f5f4057` | FULL | intent router/proactive routing |
| pinned root tree/contents | GitHub tree/contents | INVENTORY | observed repository topology |

## Planning / specification sources

| Source | Evidence ref | Status | Current role / limit |
|---|---|---:|---|
| `office-hours/SKILL.md.tmpl` | `ecd96fb4186115182a653f67e59c1dc7496ed326` | FULL | discovery, premise challenge, alternatives, approval/handoff |
| `office-hours/sections/manifest.json` | `fa6df52648ceca8ea427056d73000c8a7d6cd870` | FULL | section registry |
| `office-hours/sections/phase-2a-startup-diagnostic.md.tmpl` | `0e3a12274d5cbd2845130e529aec6f9118b7d479` | FULL | startup forcing questions/evidence discipline |
| `office-hours/sections/phase-2b-builder-brainstorm.md.tmpl` | `e49d6cd80b61b8b12cfc6e3d372b8b8c0857134b` | FULL | builder generative posture |
| `office-hours/sections/design-and-handoff.md.tmpl` | `5924dd706a141a77d96ea05aec998e6ddbaae5b9` | SUBSTANTIAL / CONTINUE | design lineage, dual-write, approval, memory/promotion/handoff |
| `plan-ceo-review/SKILL.md.tmpl` | `1b1affe160d2919ee08e00f101784a97d210906a` | FULL | scope/ambition and explicit authority |
| `plan-ceo-review/sections/manifest.json` | `5ef4425a943600708ff1d0fdb9352f2a97c07de9` | FULL | section registry |
| `plan-ceo-review/sections/review-sections.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | review sections/findings/gates/artifacts |
| `plan-eng-review/SKILL.md.tmpl` | `e066e2c5f5028ad3b8485fe8606967ac1188b47e` | FULL | first-action target/scope authority gate |
| `plan-eng-review/sections/manifest.json` | `f76e8f95bf4b313cecc2797278440cfc8f0a90a5` | FULL | section registry |
| `plan-eng-review/sections/review-sections.md.tmpl` | pinned | FULL for synthesis use | architecture/test/perf review, per-finding approval/tasks/failure modes |
| `autoplan/SKILL.md.tmpl` | `6a034e15e7647980d74dfa71bfe17c25875ed054` | SUBSTANTIAL / CONTINUE | delegated decisions, sequential review, final gate |
| `spec/SKILL.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | why/scope/code evidence/confirmation spine |
| `spec/sections/gate-and-file.md.tmpl` | `f8923a834e9228d42b4e535ed8b97cb52e0e5a6d` | FULL for synthesis use | quality/redaction/sink/issue/archive/spawn controls |
| design/devex planning skill surfaces | — | PLANNED | later design/DX cluster if needed |

## Review / QA / delivery sources

| Source | Evidence ref | Status | Current role / limit |
|---|---|---:|---|
| `review/SKILL.md.tmpl` | `a1d6a172746bdc4905731fe4e96ffb6976a579e9` | FULL for synthesis use | diff review, confidence, Fix-First |
| `review/sections/manifest.json` | `26a94ca3a7ed431514d857d9b6bd758afa859e88` | FULL | section registry |
| `review/sections/plan-completion.md.tmpl` | `7a7ae47e4ae31f1e28991bf7b233fc665f2ad4a8` | FULL | informational standalone plan-completion semantics |
| `review/sections/plan-completion.md` | `38da1ae08b0d966004d522b74af3f48ffceadcf3` | FULL | generated audit/verification modes |
| `ship/SKILL.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | release orchestration/readiness/base merge/sequencing |
| `ship/sections/manifest.json` | `e4394e5623f9421972c9be642f7d202760af866d` | FULL | ship section registry |
| `ship/sections/tests.md` | pinned | SUBSTANTIAL / CONTINUE | merged-code tests/failure ownership/evidence ledger |
| `ship/sections/test-coverage.md` | pinned | SUBSTANTIAL / CONTINUE | semantic changed-path coverage/thresholds/overrides |
| `ship/sections/plan-completion.md` | `2c36cefe477d68768a5623090c9a90835427ae5f` | FULL | ship-time plan gate / qa-only verification / scope drift |
| `ship/sections/review-army.md` | `bb1c3b82910ebaccf1beecfa10bf0771cc777601` | SUBSTANTIAL / CONTINUE | fresh review/specialists/red-team/fix loop |
| `ship/sections/adversarial.md` | `254331b9f615a09dc6e96deb952d622fe54bcd32` | FULL | Claude/Codex challenge and graceful degradation |
| `ship/sections/pr-body.md` | pinned | SUBSTANTIAL / CONTINUE | PR evidence aggregation/docs sync |
| `qa-only/SKILL.md.tmpl` | `75c4123cc5c406ffdd36c71a094335c137135b1e` | FULL for synthesis use | browser report-only evidence |
| `qa/SKILL.md.tmpl` | `d15a0c5d151ec6a8b15cd3a31dc96430ddb91909` | FULL for synthesis use | test→fix→verify browser loop |
| `scripts/resolvers/utility.ts` QA methodology | `911b01d8f7e5264a759cfa878c440e7f642eb7cb` | FULL for use | shared diff-aware browser QA |
| `scripts/resolvers/review.ts` review dashboard | `04f2dee0091e768ad1a11feda9f3a824256bfb45` | FULL for use | review standing/freshness/dashboard |
| land/deploy/canary/retro standalone skills | — | PLANNED | production lifecycle cluster |

## Browser runtime / security / evidence sources

| Source | Evidence ref | Status | Current role / limit |
|---|---|---:|---|
| `browse/SKILL.md.tmpl` | pinned | SUBSTANTIAL / CONTINUE | operator contract/evidence caveats/persistence/handoff |
| `browse/src/server.ts` | pinned | SUBSTANTIAL / CONTINUE | daemon, local/tunnel listeners, auth/dispatch/security/audit wiring |
| `browse/src/browser-manager.ts` | pinned | SUBSTANTIAL / CONTINUE | lifecycle, headed/headless, tab ownership/crash semantics |
| `browse/src/tab-session.ts` | `dccabf28f4263cb77d0a594369bb15f3e2c7ad73` | FULL | per-tab refs/snapshot/frame/load-html state |
| `browse/src/commands.ts` | pinned | SUBSTANTIAL / CONTINUE | command registry/page-content taxonomy; not security authority |
| `browse/src/token-registry.ts` | `89b0a990c31e26188275295e3d2d60f5908c5033` | FULL | scoped authority/re-pair reduction/revocation |
| `browse/src/snapshot.ts` | pinned | SUBSTANTIAL / CONTINUE | semantic ref/evidence/annotation ambiguity |
| `browse/src/cdp-allowlist.ts` | `752ce464c8e9e5d9f697c81a08444d0dd666b1e0` | FULL | deny-default CDP registry |
| `browse/src/cdp-bridge.ts` | `3d1fa3d8d002656f0e9528001df7b7c6e300b80b` | FULL | CDP dispatch/locks/timeouts/session lifecycle |
| `browse/src/url-validation.ts` | `c9e9c170ac36a6c744f47dee2b3bf15eb49e68f1` | FULL | scheme/file/metadata/SSRF/DNS checks |
| `browse/src/path-security.ts` | `bc02ccde06c753dcd4b00e3fba49ad87267adb04` | FULL | safe local/temp paths and symlink handling |
| `browse/src/file-permissions.ts` | pinned | SUBSTANTIAL / CONTINUE | platform hardening, best-effort semantics |
| `browse/src/session-persist.ts` | `3c6627bcbc0c24e76c519934b0a3a9ba3b87aca9` | FULL | opt-in persistence/excluded fields/restore filtering |
| `browse/src/content-security.ts` | `a185764583f73aaa7b8d979d8ff5942bf63c25f7` | FULL | datamark/hidden/ARIA/filter/envelope layers |
| `browse/src/security.ts` | `3da662a008e0785102f6572de468cc8dcb6bc136` | FULL | verdict combiner/canary/dead-state context |
| `browse/src/security-classifier.ts` | `a89ddf694b165872263ed8a2f46e88faa5b3f52f` | FULL | optional TestSavant L4 / fail-open |
| `browse/src/security-sidecar-client.ts` | `95e226070466df31b6e0db2ef7d93bf50b49b521` | FULL | sidecar timeout/circuit/degradation |
| `browse/src/audit.ts` | `f93b47fb090c99c95dd3c83091a0b097330130df` | FULL | persistent best-effort command audit |
| `browse/src/activity.ts` | `b15eb45a1d1c2bf5ae57f832418a0d7aa40a0f52` | FULL | bounded live activity/gap/privacy handling |

## Investigation / root-cause / debug-control sources

| Source | Evidence ref | Status | Current role / limit |
|---|---|---:|---|
| `investigate/SKILL.md.tmpl` | `c7cd9a99ad695f966ef2befaf18b1120eff89535` | FULL | causal workflow, 3-strike, scope lock, regression/fresh verification, learning handoff |
| generated `investigate/SKILL.md` | pinned | SUBSTANTIAL / CONTINUE | confirms rendered resolver/telemetry context; template remains behavior provenance |
| `freeze/SKILL.md.tmpl` | `e6804d91c23d1fd9804097a14adbc21a58745979` | FULL | Edit/Write boundary semantics and explicit non-sandbox caveat |
| `freeze/bin/check-freeze.sh` | `6c6e62e76395a4cb568a13f7578f4222ae0bb26d` | FULL | runtime deny/fail-closed/symlink enforcement |
| `unfreeze/SKILL.md.tmpl` | `88e413fe5a49a45d46d8867b2d80ace30b3b45aa` | FULL | explicit freeze state cleanup |
| `bin/gstack-paths` | `5b66e3102ff5c55b76bf88b0a2cdc31ae6b83d56` | FULL | state-root resolution/persistence context |
| `scripts/resolvers/learnings.ts` | `aefc0fb864a3b19ee33b6253e1dbf7228ce2ba82` | FULL | learning schema/search/log prompt contract |
| `bin/gstack-learnings-log` | `3c47ebb80a4285028cf7c54549038553b81c5eb4` | FULL | validation/trust mark/append/enqueue |
| `bin/gstack-learnings-search` | `d7038e821881861f9661af2f34f3728bf1cabe23` | FULL | confidence decay/dedup/query/cross-project trust gate |
| `scripts/resolvers/gbrain.ts` | `6c6b66d640187363c0dc12326fe08adfb689c98d` | FULL for investigation handoff | optional brain context/save; whole memory subsystem still open |
| `hosts/define-host.ts` | `0ed190dd00606a69acb0aca990289781f79bbc79` | FULL | common external-host frontmatter stripping / resolver defaults |
| `hosts/claude.ts` | `5381953cae8040508a260e6e4b3eb39973c92934` | FULL | Claude retains hooks/gbrain frontmatter and full learnings mode |
| `hosts/codex.ts` | `b46e9222495eada3da68debaae6dab6d9d57167c` | FULL | Codex allowlists name/description; hooks not retained |
| `openclaw/skills/gstack-openclaw-investigate/SKILL.md` | pinned | FULL | causal phases adapted; scope-lock/freeze absent; memory handoff differs |

## Shared generation / host sources

| Source | Evidence ref | Status | Current role / limit |
|---|---|---:|---|
| `scripts/gen-skill-docs.ts` | pinned | SUBSTANTIAL / CONTINUE | `.tmpl → resolver → generated`, host/model overlays, freshness |
| `scripts/resolvers/index.ts` | `cee08c2015a6ac2ff8605b02ac07a49d284d3ce1` | FULL | resolver registry |
| `scripts/resolvers/sections.ts` | `c6425e19b93d20018057cf2fe6ae9eeb2f613a18` | FULL | carved sections / Claude STOP+Read vs inline external host rendering |
| `scripts/resolvers/composition.ts` | `b8d3483d9bd961409025959eddcd8840dd5f98a8` | FULL | parent-child composition |
| broader host configs/adapters | partial | PLANNED / PARTIAL | dedicated portability cluster later |

## Test / eval / compliance sources

| Source | Evidence ref | Status | Current role / limit |
|---|---|---:|---|
| `test/spec-template-invariants.test.ts` | `40d2d22677cbd0a506c6395bc0e2b00b3a2149d2` | FULL | deterministic spec structural pins |
| `test/ship-plan-completion-invariants.test.ts` | `26c565b1b093262697832d3b161c479bbb5ce07b` | FULL | ship plan-gate pins |
| `test/skill-coverage-matrix.ts` | `7359afbce8144625e3b832d0fa9044fb753185a8` | FULL | per-skill gate/periodic registry; investigate only generic floor |
| `test/skill-coverage-floor.test.ts` | `4f75e370b09c01098fb711ca4332f1370e1e5a10` | FULL | structural compliance only; not behavioral proof |
| planning/office-hours/review/QA/ship E2Es | see earlier refs | FULL/SUBSTANTIAL | selected behavioral evidence; varying oracle/topology quality |
| `browse/test/dual-listener.test.ts` | pinned | SUBSTANTIAL / CONTINUE | exact-set tunnel structural pins |
| `browse/test/server-factory.test.ts` | pinned | SUBSTANTIAL / CONTINUE | server factory/auth/listener behavior |
| `browse/test/server-auth.test.ts` | pinned | SUBSTANTIAL / CONTINUE | auth/tab/chain/activity/tunnel regressions |
| `browse/test/pair-agent-e2e.test.ts` | pinned | SUBSTANTIAL / CONTINUE | real-daemon HTTP pair/connect; no live ngrok |
| `browse/test/tab-isolation.test.ts` | `698dd1ac8b0c750df4d03632925195e6458e1118` | FULL | own-only vs shared tab access |
| `browse/test/token-registry.test.ts` | pinned | SUBSTANTIAL / CONTINUE | token/scope/reduction behavior |
| `browse/test/cdp-allowlist.test.ts` | `8256e7a198e6e197ca2f70e60f9ff1abb109a661` | FULL | dangerous-method denial pins |
| `browse/test/cdp-e2e.test.ts` | `d5d2e26c1b8f08bf531dd4b4bed06b85d153458e` | FULL | real Chromium CDP allow/deny behavior |
| `browse/test/url-validation.test.ts` | `7f7fe5949318572935a55c46412a956d04d19994` | FULL | URL/SSRF/direct-fetch regressions |
| `browse/test/session-persist.test.ts` | `bf7bfa8bdec2633d160ff4122f33ede8869f283a` | FULL | real Chromium persistence round trip |
| `browse/test/content-security.test.ts` | pinned | SUBSTANTIAL / CONTINUE | deterministic content-security checks |
| `browse/test/server-security-surface.test.ts` | `cdfb76c96e982130048acc8fac511d8abb5b7bad` | FULL | false-green state removal/live L4 pin |
| `test/investigate-freeze-path.test.ts` | `7b9ef0cae733b872f188588f6d1fee3125e41fb8` | FULL | investigate hook/probe path resolution regression |
| `test/hook-scripts.test.ts` | `55817099a5380b6d7170a53adc9ae4e9351ec4e4` | SUBSTANTIAL / CONTINUE | freeze runtime allow/deny/fail-closed/symlink tests plus careful tests |
| investigate-specific causal behavioral E2E | — | **ABSENT IN REGISTERED MATRIX** | no direct registered proof of no-fix/3-strike/regression/fresh-verification behavior |
| broader LLM judge/routing/Codex/Gemini/eval lifecycle tests | — | PLANNED | later eval/portability cluster |

## Durable study syntheses

| Synthesis | Status | Boundary |
|---|---:|---|
| `syntheses/planning-specification-work-admission.md` | BOUNDED | discovery → planning → spec/work admission |
| `syntheses/review-qa-ship-delivery-qualification.md` | BOUNDED | implementation → review/QA/test/ship qualification |
| `syntheses/browser-runtime-security-evidence.md` | BOUNDED | browser execution → capability/security → evidence semantics |
| `syntheses/investigation-root-cause-debug-control.md` | BOUNDED | failure → causal hypothesis/falsification → bounded fix → fresh verification/learning |

## Evolution / chronology

| Source | Status | Note |
|---|---:|---|
| `CHANGELOG.md` (~1.1 MB at pinned revision) | PLANNED / PARTITIONED | use chronological/mechanistic partitions, not one linear unit |
| pinned v1.79 release commit diff | PLANNED | reconstruct recent dispatch/ship evolution later |

## Source-fidelity warnings

1. `docs/PROJECT_STRUCTURE.md` is a derived repository-authored view; actual pinned paths/source win.
2. Generated `SKILL.md` files must not replace `.tmpl`/resolver provenance where generation owns behavior.
3. Skill prose is intended workflow policy; structural tests do not prove model compliance.
4. First-party tests/evals are not independent verification.
5. Cross-model diversity is not automatically independent verification when framing/artifacts/oracles are shared.
6. Office-hours promotion/relationship behavior is separate from evidence about planning quality.
7. `/ship` evidence channels have different failure polarities; “gate” is not one semantics.
8. AI-assessed changed-path coverage is not instrumented coverage.
9. Documentation lifecycle diagrams do not establish a universal historical `Review → QA → Ship` state machine.
10. Pair-agent/tunnel own-only tab isolation must not be generalized to shared local browser clients.
11. Browser `READ_COMMANDS`/`WRITE_COMMANDS` are not authoritative security capability classes.
12. Browser state persistence between live-daemon calls is not default persistence across headless daemon restarts.
13. Browser security controls have heterogeneous hard-deny/best-effort/fail-open behavior.
14. Pair-agent HTTP E2E does not reproduce a live public ngrok tunnel.
15. `/investigate`'s causal methodology has no registered behavioral E2E at the pinned revision; generic structural floor is much weaker evidence than freeze runtime tests.
16. Investigate freeze is Edit/Write-hook enforcement, not a full mutation sandbox, and it is host-specific.
17. Investigate does not automatically clear its freeze state; `/unfreeze` owns explicit cleanup.
18. Investigate's “root cause” label does not guarantee prevention/detection/systemic causal depth.
19. Prior learnings are sourced/decayed/trust-scoped candidate context, not automatically authoritative truth.
