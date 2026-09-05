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
| `gstack` | external-target | active source-grounded external-repository study; gstack-native subsystem modeling in progress | implemented agentic software factory; workflow gates/artifact handoffs; persistent browser/runtime; cross-model/multi-agent coordination; eval/routing infrastructure; memory/learning; ship/deploy/production loops | Information: strong; Work: strong; Actors: strong; Environment: strong; relations/control: strong later-phase pressure-test potential | `gstack/META.md` |
| `multi-agent-patterns` | focused-topic | exploratory systems assessment complete for the triggering discussion | coordination/control patterns, generator–critic, orchestration, authority/verification design pressure | Actors: strong; Work: strong; relations/control: strong later-phase relevance | `multi-agent-patterns/META.md` |
| `hands-on-large-language-models` | external-target | durable external-repository research complete; production adoption not recommended/evaluated | executable LLM examples, representation/retrieval/fine-tuning/agent reference cases, version/environment failure cases | Information: strong; Environment: conditional; Actors: conditional | `hands-on-large-language-models/META.md` |
| `public-apis` | external-target | bounded general repository evaluation; discovery reuse candidate | external API/capability discovery; data/service landscape; build-vs-integrate exploration | Environment: strong; Information: conditional/strong when external data access matters; Work: conditional | `public-apis/META.md` |

## Selection guidance

### If current work concerns Information / representation

Likely candidates to inspect first, depending on the exact node/problem:

- `ai-knowledge-strategies`
- `context-memory-harness-engineering`
- `hands-on-large-language-models`
- `gstack` when durable design/spec/review/release artifacts, context selection, memory/learnings, evidence production, cross-stage handoffs or source-to-observation pipelines are material; study is still active, so read package state and revalidate load-bearing findings
- `anthropic-ai-native-sdlc-playbook` when artifact identity/derivation, context/configuration surfaces, policy freshness, exact-target binding or production-observation→representation transitions are material
- `public-apis` only when external information/data/capability access is materially in scope

Do not load all candidates by default; read META first and let the active Foundation method/authorization control depth.

### If current work concerns Environment / capability

Potential candidates:

- `public-apis`
- `context-memory-harness-engineering`
- `hands-on-large-language-models` for executable environment/version binding cases
- `gstack` for persistent browser/runtime capability, local/tunnel security boundaries, tooling/host portability, guarded actions and production/runtime evidence; active-study freshness and coverage limits apply
- `anthropic-ai-native-sdlc-playbook` for sandbox/permission/network/MCP/CI/production-state control examples and repo-state-vs-live-state falsifiers

### If current work concerns Actors / Work / coordination

Potential candidates:

- `multi-agent-patterns`
- `gstack` for explicit workflow roles, user approval gates, multi-agent/cross-model dispatch, review/QA/ship sequencing, durable handoffs and agent/runtime separation; active-study freshness and coverage limits apply
- `anthropic-ai-native-sdlc-playbook` for real operational producer/reviewer/human-gate patterns, transitive agent authority, tiered autonomy, artifact/gate dependencies and recurring maintenance work
- `context-memory-harness-engineering`
- selected agent material from `hands-on-large-language-models`

These are discovery hints, not conclusions about final Foundation structure.

### If later design / architecture work concerns agent-runtime governance

Potential candidates to inspect selectively:

- `gstack` — implemented workflow/runtime/eval/security/memory/ship mechanisms; use only after reading active package state and revalidating any changed target files
- `anthropic-ai-native-sdlc-playbook` — managed settings, Hooks, permissions, sandboxing, managed MCP, runtime telemetry, configuration evals, incident loops
- `context-memory-harness-engineering` — broader context/memory/harness boundaries
- `multi-agent-patterns` — coordination and verification topology

Current project authorization still controls whether such design/architecture work may begin.

## Maintenance

When a study is created, reclassified, materially updated, rejected, superseded or adopted as an input:

1. update its package `META.md` first;
2. refresh this catalog entry;
3. preserve package `STATE.md` authority where one exists.

When the library becomes large, prefer compact tags and retrieval hints here rather than copying findings from packages.
