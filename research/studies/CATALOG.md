# Candidate Studies — Catalog

## Role

Compact derived discovery index for `research/studies/**`.

This catalog is **not** the source of truth for a study's detailed findings or current work state. Use it to find plausible packages, then read the package-local `META.md` and, when present, `STATE.md` / `INDEX.md`.

Foundation relevance below is a retrieval hint only. It does not assign a study to the Foundation taxonomy.

## Catalog

| Study | Type | Current status | Strongest current reuse signals | Foundation relevance hints | Start |
|---|---|---|---|---|---|
| `ai-knowledge-strategies` | focused-topic | bounded research complete; related follow-up linked | RAG, Knowledge Graph, Fine-Tuning, CAG, Long Context decision boundaries; knowledge/context mechanism selection; falsifiers and failure modes | Information: strong; Environment/Work/Actors: conditional cross-boundary relevance | `ai-knowledge-strategies/META.md` |
| `anthropic-ai-native-sdlc-playbook` | external-target | bounded external-target research complete; architecture/adoption not authorised | agent-native software operating model; committed artifact chain; configuration evals; advisory→deterministic control stack; environment-tiered autonomy; transitive agent authority; production feedback/evolution loops | Work: strong; Actors: strong; Information: strong; Environment: strong/conditional; relations/control: strong later-phase relevance | `anthropic-ai-native-sdlc-playbook/META.md` |
| `context-memory-harness-engineering` | focused-topic | bounded research complete; user evaluation pending in package state | context formation, memory lifecycle, harness/runtime/control, relationship to AI knowledge mechanisms | Information: strong; Environment: strong/conditional; Work & Actors: conditional | `context-memory-harness-engineering/META.md` |
| `gstack` | external-target | bounded research complete; pinned v1.79 corpus revalidated through v1.80 current-main snapshot; no adoption authorised | implemented agentic software factory; artifact-mediated qualification; work admission/review/QA/ship/deploy; persistent browser/runtime; authority vs capability; cross-model/multi-agent coordination; eval/routing; memory/learning; install/update/self-development; qualification-loss counterexamples | Information: strong; Work: strong; Actors: strong; Environment: strong; Binding/Standing/Control/Transition: strong later-phase pressure-test relevance | `gstack/META.md` |
| `hermes-agent` | external-target | active partial research; pinned 0.21.0; plan v0.8. Review-construction/name-set/round/Relay source trace; 22-definition manual-range AST cross-check; exact middleware eight-case evidence, separate from older U01B/transport/U01B2/C/V records. No whole-product validation or adoption | schema-derived valid names vs review authority; worker-local policy; middleware own/downstream failure and single-use effects; persistence timing; memory/approval/rollback boundaries. Next active: actual pending CLI/gateway/profile/store; full-original fidelity and Q26 whole-runtime integration remain open with revisit triggers | Information: strong candidate; Work/Actors/Environment and relations/control: provisional cross-boundary relevance, not a completed projection | `hermes-agent/META.md` |
| `multi-agent-patterns` | focused-topic | exploratory systems assessment complete for the triggering discussion | coordination/control patterns, generator–critic, orchestration, authority/verification design pressure | Actors: strong; Work: strong; relations/control: strong later-phase relevance | `multi-agent-patterns/META.md` |
| `hands-on-large-language-models` | external-target | durable external-repository research complete; production adoption not recommended/evaluated | executable LLM examples, representation/retrieval/fine-tuning/agent reference cases, version/environment failure cases | Information: strong; Environment: conditional; Actors: conditional | `hands-on-large-language-models/META.md` |
| `public-apis` | external-target | bounded general repository evaluation; discovery reuse candidate | external API/capability discovery; data/service landscape; build-vs-integrate exploration | Environment: strong; Information: conditional/strong when external data access matters; Work: conditional | `public-apis/META.md` |
| `recursive-prerequisite-discovery` | focused-topic | bounded source-informed assessment; 25 local mechanical tests re-run; no live-agent efficacy/integration validation; original-source recovery limitation explicit | prerequisite vs decomposition; conditional methods and AND/OR; agent-relative actionable frontier; unfinished inquiry/return-to continuity; proposal vs accepted state; prototype vs reasoning validity | Work/Information: strong candidate; Actors/Environment and Binding/Standing/Control/Transition: cross-boundary relevance; not Foundation adoption | `recursive-prerequisite-discovery/META.md` |

## Selection guidance

### If current work concerns Information / representation

Likely candidates to inspect first, depending on the exact node/problem:

- `ai-knowledge-strategies`
- `context-memory-harness-engineering`
- `hands-on-large-language-models`
- `gstack` when durable design/spec/review/release artifacts, context selection, memory/learnings, evidence formation, qualification/freshness, cross-stage handoffs or source→observation→standing pipelines are material; start at `gstack/META.md` / `CORE.md` and revalidate upstream again if current behavior beyond its recorded v1.80 checkpoint matters
- `anthropic-ai-native-sdlc-playbook` when artifact identity/derivation, context/configuration surfaces, policy freshness, exact-target binding or production-observation→representation transitions are material
- `public-apis` only when external information/data/capability access is materially in scope

Do not load all candidates by default; read META first and let the active Foundation method/authorization control depth.

### If current work concerns Environment / capability

Potential candidates:

- `public-apis`
- `context-memory-harness-engineering`
- `hands-on-large-language-models` for executable environment/version binding cases
- `gstack` for persistent browser/runtime capability, host/model/materialization distinctions, tool/install state, guarded actions, CI/runtime validity and production evidence; the study is closed but current upstream must be revalidated beyond its recorded checkpoint when load-bearing
- `anthropic-ai-native-sdlc-playbook` for sandbox/permission/network/MCP/CI/production-state control examples and repo-state-vs-live-state falsifiers

### If current work concerns Actors / Work / coordination

Potential candidates:

- `multi-agent-patterns`
- `gstack` for user approval gates, authority vs effect power, delegation, multi-agent/cross-model dispatch, work admission, review/QA/ship/deploy sequencing, durable handoffs, liveness and recovery
- `anthropic-ai-native-sdlc-playbook` for real operational producer/reviewer/human-gate patterns, transitive agent authority, tiered autonomy, artifact/gate dependencies and recurring maintenance work
- `context-memory-harness-engineering`
- selected agent material from `hands-on-large-language-models`
- `recursive-prerequisite-discovery` for discovery-driven work, agent-level prerequisite reasoning, actionable-frontier selection and unfinished-inquiry continuity; the proposed storage architecture is not automatically adopted and mechanical tests do not verify agent reasoning

These are discovery hints, not conclusions about final Foundation structure.

### If current work concerns relation / standing / control / transition composition

Potential candidates:

- `gstack` — implemented pressure cases for exact binding/provenance, composite readiness/qualification, enforcement-point vs protected-effect scope, realized effect/readback, partial propagation, rollback/restoration and qualification loss at handoff seams
- `anthropic-ai-native-sdlc-playbook` — policy/configuration/authority/effect and production-feedback control cases
- `multi-agent-patterns` — coordination/authority/verification topology

Candidate-study relevance never changes the active Foundation authorization or acceptance state.

### If later design / architecture work concerns agent-runtime governance

Potential candidates to inspect selectively:

- `gstack` — implemented workflow/runtime/eval/security/memory/install/ship mechanisms; read `META.md`, `CORE.md`, relevant synthesis and freshness revalidation before load-bearing reuse
- `anthropic-ai-native-sdlc-playbook` — managed settings, Hooks, permissions, sandboxing, managed MCP, runtime telemetry, configuration evals, incident loops
- `context-memory-harness-engineering` — broader context/memory/harness boundaries
- `multi-agent-patterns` — coordination and verification topology

Current project authorization still controls whether such design/architecture work may begin.

## Maintenance

When a study is created, reclassified, materially updated, rejected, superseded or adopted as an input:

1. update its package `META.md` first;
2. refresh this catalog entry;
3. preserve package `STATE.md` authority if it exists.

When the library becomes large, prefer compact tags and retrieval hints here rather than copying findings from packages.
