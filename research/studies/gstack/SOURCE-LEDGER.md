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
| actual root contents/tree | GitHub contents + recursive tree API at pinned commit | INVENTORY | observed repository topology and path existence |

## Workflow / skill sources

| Source | Read status | Current role / note |
|---|---:|---|
| `office-hours/SKILL.md.tmpl` | SUBSTANTIAL / CONTINUE | discovery/design skill; hard no-implementation gate, context gathering, memory hooks, privacy-gated landscape search, premise challenge, mandatory alternatives, user approval gate, durable design handoff, builder profile signals |
| `plan-ceo-review/SKILL.md.tmpl` | PLANNED | product/CEO plan pressure test |
| `plan-eng-review/SKILL.md.tmpl` | PLANNED | engineering plan review |
| `plan-design-review/SKILL.md.tmpl` | PLANNED | design plan review |
| `plan-devex-review/SKILL.md.tmpl` | PLANNED | developer-experience plan review |
| `design-consultation/SKILL.md.tmpl` | PLANNED | design/product alternative research |
| `autoplan/SKILL.md.tmpl` | PLANNED | plan orchestration |
| `spec/SKILL.md.tmpl` | PLANNED | work specification / implementation handoff |
| `review/SKILL.md.tmpl` | PLANNED | code/implementation review |
| `investigate/SKILL.md.tmpl` | PLANNED | root-cause investigation |
| `qa/SKILL.md.tmpl` | PLANNED | QA workflow |
| `qa-only/SKILL.md.tmpl` | PLANNED | restricted QA path |
| `design-review/SKILL.md.tmpl` | PLANNED | implemented UI/design review |
| `devex-review/SKILL.md.tmpl` | PLANNED | implemented developer-experience review |
| `pair-agent/SKILL.md.tmpl` | PLANNED | multi-agent coordination |
| `cso/SKILL.md.tmpl` | PLANNED | security review/CSO role |
| `ship/SKILL.md.tmpl` | PLANNED | ship/release workflow |
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

| Source family | Status | Why needed |
|---|---:|---|
| skill generator / template expansion scripts | PLANNED | determine how ETHOS/preamble/sections become executable skill contracts |
| shared skill orchestration helpers | PLANNED | agent/subagent dispatch, handoff and shared behavior |
| shared Codex integration | PLANNED | cross-model topology and scope contracts |
| shared browser/reference-doc utilities | PLANNED | evidence/context formation across skills |
| `browse/src/**` core daemon/server/CLI | PLANNED | actual persistent execution environment |
| browser command modules | PLANNED | exact action/evidence capability surface |
| browser/runtime tests | PLANNED | enforcement and failure/recovery evidence |
| host adapter surfaces | PLANNED | portability and host-specific behavior |

## Eval / verification / compliance sources

| Source family | Status | Why needed |
|---|---:|---|
| `test/skill-llm-eval*.test.ts` | PLANNED | behavioral criteria and LLM-judged eval design |
| `test/skill-e2e-*.test.ts` | PLANNED | end-to-end workflow expectations |
| `test/skill-routing-e2e.test.ts` | PLANNED | skill invocation/routing behavior |
| `test/codex-e2e*.test.ts` | PLANNED | cross-model contract, including Sol scope |
| `test/gemini-e2e.test.ts` | PLANNED | host/model portability evidence |
| `test/llm-judge-recommendation.test.ts` | PLANNED | judge/oracle design |
| `test/carve-section-loading.test.ts` | PLANNED | section composition/loading behavior |
| audit/compliance tests | PLANNED | deterministic policy checks |
| eval list/compare/summary/flake/watch/select scripts | PLANNED | eval lifecycle and operational feedback |

## Evolution / chronology sources

| Source | Status | Note |
|---|---:|---|
| `CHANGELOG.md` (~1.1 MB at pinned revision) | PLANNED / PARTITIONED APPROACH | do not treat as a single linear read unit; partition chronologically/mechanistically and use recent release diffs to reconstruct evolution |
| pinned release commit diff | PLANNED | especially subagent-dispatch / ship behavior changes in v1.79.0.0 |

## Source-fidelity warnings

1. `docs/PROJECT_STRUCTURE.md` is a derived repository-authored view. At least one documented path (`skill/SKILL.md.tmpl`) did not resolve at the pinned revision when directly fetched; path/tree claims must be checked against actual contents.
2. Root `SKILL.md` or generated skill artifacts, where present, must not be substituted for source templates when repository instructions identify templates as canonical.
3. A skill template's declared gate is evidence of intended workflow policy; actual deterministic enforcement requires supporting code/test/runtime evidence if claimed.
4. First-party tests/evals increase evidence about expected/enforced behavior but are not independent external verification.
