# Work Management / Project Control — Study Metadata

## Identity and status

- **Study ID:** `work-management-project-control`
- **Title:** Work Management / Project Control — Representation, Decomposition, Flow and Recovery
- **Study type:** `focused-topic`
- **Status:** **ACTIVE / INITIAL PROGRAM SETUP**. U00 framing and method setup are being established; repository targets are processed sequentially under package `STATE.md`.
- **Research object:** methodologies and implemented mechanisms for representing, decomposing, sequencing, assigning, progressing, blocking, reopening, replanning, verifying and recovering substantial work, independent of whether the actor is a human, an AI agent or a mixed team.
- **Research start:** 2026-09-17

## Primary question / purpose

How should a system represent and control large work when the path from intent to completion is not necessarily linear, fully known up front, or executed by one actor?

The study compares different work-management traditions and implemented systems rather than choosing a product. It asks how they model:

- work identity and decomposition;
- dependency and readiness;
- state and transition;
- ownership / claim / lease / role;
- uncertainty and progressive discovery;
- replanning, reopening, backtracking and compensation;
- scheduling, milestones, resources and constraints;
- verification / acceptance / definition of done;
- history, decisions, provenance and recovery;
- coordination across humans and agents;
- project / program / portfolio structure.

## Potential Foundation relevance — provisional retrieval hints

- **Work:** very strong candidate input for work identity, decomposition, readiness, state transitions, prerequisite/dependency structure, execution flow, verification and recovery.
- **Actors:** strong where assignment, claim, role, delegation, coordination, authority and human/agent participation affect work state.
- **Information:** strong/conditional where plans, issues, decisions, dependencies, schedules, evidence and current state must remain durable and recoverable.
- **Environment:** conditional/strong where calendars, capacity, resources, external systems, workflow engines or execution environments constrain what work is actually possible.
- **Relations / control:** very strong pressure surface for blocker/enabler edges, hierarchy versus DAG, state-machine transitions, admission/readiness, compensation/reopen, acceptance and portfolio composition.

These are discovery hints only. They do not assign Foundation taxonomy membership.

## Potential SOUL relevance

Possible future value includes:

- giving SOUL a broader vocabulary for reasoning about work than task lists alone;
- distinguishing decomposition from prerequisite discovery and readiness from priority;
- modelling unknown or not-yet-specifiable work without forcing premature tasks;
- choosing task/project/case/process/graph representations by work condition rather than one universal workflow;
- coordinating humans and agents over one durable work substrate;
- recovering current/next work after session, actor or environment changes;
- treating replanning, reversal and verification as first-class work transitions rather than exceptions.

No SOUL work architecture is authorised or implied by this study.

## Potential Development OS relevance

Possible future value includes:

- persistent multi-session work state;
- project / issue / decision / dependency representations;
- progressive planning and actionable-frontier computation;
- work admission, ownership, blockers, review and completion gates;
- large-project decomposition across sessions and agents;
- recovery / reopen / rollback / compensation patterns;
- schedule, milestone, resource and portfolio concepts where development work needs them;
- comparison of repository-native, issue-tracker, BPM/case-management and agent-native work systems.

No Development OS design or implementation decision is authorised or implied by this study.

## Reuse modes

- methodology reference;
- implemented mechanism catalogue;
- cross-system falsifier / counterexample;
- candidate work-state and control primitives;
- test/fixture source for large-work reasoning;
- design pressure for SOUL / Development OS when later authorised;
- negative-option evidence where a work model fails outside its native conditions.

## Likely revisit triggers

- Work Foundation deepening;
- Development OS work/project/task subsystem design;
- SOUL reasoning about large jobs or long-lived projects;
- agent task graphs, project trackers, workflow engines or case-management questions;
- dependency/frontier/replanning/recovery design;
- human-agent shared work-state design;
- portfolio/resource/schedule questions.

## Epistemic / authority boundary

This is candidate research, not Foundation authority and not an architecture decision. A repository's feature or terminology is evidence about that system, not proof that its ontology should be adopted. Product documentation and implementation are preferred over marketing claims; first-party benchmarks remain first-party until independently checked. Similar words across systems (task, issue, case, workflow, dependency, milestone, done) must not be assumed semantically equivalent.

Existing studies such as `recursive-prerequisite-discovery`, `mattpocock-skills`, `gstack`, `superpowers` and `multi-agent-patterns` are comparison inputs, not answers to be projected onto new targets.

## Freshness / revalidation

Each external repository is revalidated when its unit begins and pinned to a concrete observed ref/version before load-bearing source analysis. Fast-moving agent-native repositories require especially strict freshness checks. Stable project-management concepts may be reused conceptually, but exact product behavior, APIs, licensing and current features must be rechecked.

## Package entrypoints

1. `STATE.md` — authoritative current unit, completed work and next action
2. `METHOD.md` — comparison dimensions and evidence discipline
3. `PLAN.md` — unit sequence and change policy
4. `INDEX.md` — retrieval router

## Related studies

- `../recursive-prerequisite-discovery/`
- `../mattpocock-skills/`
- `../gstack/`
- `../superpowers/`
- `../multi-agent-patterns/`
- `../anthropic-ai-native-sdlc-playbook/`
- `../context-memory-harness-engineering/`
