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

## Other workflow / lifecycle sources

| Source | Read status | Current role / note |
|---|---:|---|
| `review/SKILL.md.tmpl` | PLANNED | code/implementation review |
| `investigate/SKILL.md.tmpl` | PLANNED | root-cause investigation |
| `qa/SKILL.md.tmpl` | PLANNED | QA workflow |
| `qa-only/SKILL.md.tmpl` | PLANNED | restricted QA path |
| `design-review/SKILL.md.tmpl` | PLANNED | implemented UI/design review |
| `devex-review/SKILL.md.tmpl` | PLANNED | implemented developer-experience review |
| `pair-agent/SKILL.md.tmpl` | PLANNED | multi-agent coordination |
| `cso/SKILL.md.tmpl` | PLANNED | security review/CSO role |
| `ship/SKILL.md.tmpl` | PLANNED | ship/release workflow; next dependency for planning-chain closure |
| `land-and-deploy/SKILL.md.tmpl` | PLANNED | merge/deploy workflow |
| `canary/SKILL.md.tmpl` | PLANNED | production/canary feedback |
| `document-release/SKILL.md.tmpl` | PLANNED | release documentation/artifact chain |
| `retro/SKILL.md.tmpl` | PLANNED | retrospective / learning loop |
| `learn/SKILL.md.tmpl` | PLANNED | durable learning capture |
| `setup-gbrain/SKILL.md.tmpl` | PLANNED | GBrain setup/context memory |
| `sync-gbrain/SKILL.md.tmpl` | PLANNED | GBrain synchronization |
| `codex/SKILL.md.tmpl` | PLANNED | cross-model second opinion/review |
| `benchmark/SKILL.md.tmpl` | PLANNED | model/agent comparison |
| `browse/SKILL.md.tmpl` | PLANNED | browser skill contract |
| guard/freeze/careful/unfreeze skill surfaces | PLANNED | guarded-action / scope-control mechanisms; exact paths to verify from tree |

## Shared / generator / runtime sources

| Source | Evidence ref | Status | Why needed / current result |
|---|---|---:|---|
| `scripts/gen-skill-docs.ts` | pinned source | SUBSTANTIAL / CONTINUE | confirms `.tmpl → resolver → generated .md`, host/model overlays, dry-run freshness, output isolation |
| `scripts/resolvers/index.ts` | `cee08c2015a6ac2ff8605b02ac07a49d284d3ce1` | FULL | central resolver registry across review, memory, tasks, sections, redaction, composition |
| `scripts/resolvers/sections.ts` | `c6425e19b93d20018057cf2fe6ae9eeb2f613a18` | FULL | Claude STOP+Read carve vs non-Claude inline rendering; passive manifest semantics |
| `scripts/resolvers/composition.ts` | `b8d3483d9bd961409025959eddcd8840dd5f98a8` | FULL | parent-child skill invocation and parent-owned section skip contract |
| `scripts/resolvers/review.ts` | pinned source | SUBSTANTIAL / CONTINUE | dashboard/report/staleness and cross-model shared review machinery; next pass should finish relevant consumers |
| shared Codex integration | partial through planning/resolver sources | SUBSTANTIAL / CONTINUE | cross-model topology and scope contracts; independence not established |
| shared browser/reference-doc utilities | — | PLANNED | evidence/context formation across skills |
| `browse/src/**` core daemon/server/CLI | — | PLANNED | actual persistent execution environment |
| browser command modules | — | PLANNED | exact action/evidence capability surface |
| browser/runtime tests | — | PLANNED | enforcement and failure/recovery evidence |
| host adapter surfaces | — | PLANNED | portability and host-specific behavior |

## Eval / verification / compliance sources

| Source | Evidence ref | Status | Current role / limit |
|---|---|---:|---|
| `test/spec-template-invariants.test.ts` | `40d2d22677cbd0a506c6395bc0e2b00b3a2149d2` | FULL | deterministic structural pins for spec phase/safety/admission contracts; not behavioral proof by itself |
| `test/skill-coverage-matrix.ts` | `7359afbce8144625e3b832d0fa9044fb753185a8` | FULL | gate vs periodic coverage model; every skill has at least a CI-blocking floor |
| `test/skill-e2e-plan-eng-plan-mode.test.ts` | `85eec6cc401bf79275aae0e34e11373a72e7c71b` | FULL | periodic real-PTY behavior for STOP-before-write and plan-mode scope-gate bypass |
| `test/skill-e2e-autoplan-dual-voice.test.ts` | `1efc6dfc68643fa2772770ea9b87187986612e99` | FULL | periodic/non-gating dual-voice dispatch/graceful-degrade evidence; partial-pipeline only |
| `test/skill-e2e-office-hours.test.ts` | `c3ad6c57b80ce6a78510f1e0d226b39900e9df49` | FULL | LLM-judged posture behavior for startup forcing and builder wildness; oracle-dependent |
| `test/skill-validation.test.ts` | pinned source | SUBSTANTIAL / CONTINUE | generated-skill/router/command invariants; pins autoplan scope-gate skip-list |
| `test/skill-llm-eval*.test.ts` | — | PLANNED | broader behavioral criteria and LLM-judged eval design |
| `test/skill-routing-e2e.test.ts` | — | PLANNED | skill invocation/routing behavior |
| `test/codex-e2e*.test.ts` | — | PLANNED | cross-model contract, including Sol scope |
| `test/gemini-e2e.test.ts` | — | PLANNED | host/model portability evidence |
| `test/llm-judge-recommendation.test.ts` | — | PLANNED | judge/oracle design |
| `test/carve-section-loading.test.ts` | — | PLANNED | runtime section-loading behavior |
| audit/compliance tests | partial via spec invariants | SUBSTANTIAL / CONTINUE | deterministic policy checks require broader pass |
| eval list/compare/summary/flake/watch/select scripts | — | PLANNED | eval lifecycle and operational feedback |

## Durable study syntheses

| Synthesis | Status | Boundary |
|---|---:|---|
| `syntheses/planning-specification-work-admission.md` | BOUNDED | gstack-native discovery → planning review → spec/work-admission model; not whole-system closure |

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
5. Cross-model diversity is not automatically verification independence when models share the same plan, framing, orchestration, or first-party oracle.
6. `office-hours` mixes work-design mechanics with YC/founder relationship and promotion behavior. Treat the latter as a separate incentive/retention mechanism; do not use it as evidence for planning quality.
