# Current SOUL Development OS Bootstrap Bridge

**Status:** CURRENT OPERATIONAL CONTEXT / BOOTSTRAP BRIDGE  
**Date:** 2026-09-06  
**Epistemic status:** user-authorised current direction + directly observed repository/environment context + explicitly marked working hypotheses  
**Authority:** context/continuity only; **not Foundation truth, not SOUL architecture authority, not Development OS current-state authority, not agent-control**

## Why this file exists

SOUL Research has entered a new long-running phase in which research continues while a new SOUL Development OS is bootstrapped in parallel with Codex.

This transition was established in conversation and would be easy to lose across fresh ChatGPT sessions if it remained only in chat history. This file preserves the minimum current context needed to understand:

- why two new repositories were created;
- why the previous `batuhanozgun/soul` repository is not being continued as the active development surface;
- what role `agentic-os-search` now plays relative to development and production;
- what kind of Codex actor is being bootstrapped;
- why ChatGPT is temporarily helping bootstrap the Development OS;
- what must become true before that temporary bridge can end.

This file is deliberately **not** the canonical work state for `soul-development-os`. Once that repository has its own reliable canonical state/bootstrap surface, its current work must be recovered there rather than copied here.

---

# 1. Current repository topology

The current direction separates research, development and production into three repositories with distinct authority roles:

```text
batuhanozgun/agentic-os-search
    = SOUL Research
    = Foundation + candidate studies + research context

batuhanozgun/soul-development-os
    = the working system used to research/design/build/verify/evolve SOUL
    = intended future authority for current development state

batuhanozgun/soul-production
    = accepted SOUL product
    = intended future authority for accepted product state/behavior
```

The previous repository:

```text
batuhanozgun/soul
```

is intentionally left intact as **historical predecessor / prior-art / failure and verification evidence** rather than cleaned in place and reused as the new active surface.

## Authority rule

Do not create three authoritative copies of the same fact.

- Foundation/research finding authority remains in `agentic-os-search`.
- Current Development OS work/state should eventually live canonically in `soul-development-os`.
- Accepted product state/behavior should eventually live canonically in `soul-production`.
- The old `soul` repository is predecessor evidence, not a privileged default for the new design.

Cross-repository references should preserve provenance instead of copying source truth whenever practical.

---

# 2. Why a clean development reboot was chosen

The decision is **not** that every idea in the previous SOUL repository is obsolete.

Several predecessor principles remain strongly plausible and are reinforced by later research, including repository-authoritative continuity, bounded authority, producer/self-verification separation, explicit failure states, evidence-before-closure, missing-capability governance and observability.

The concern is at a different level:

> the previous Development OS and roadmap were produced before the current Foundation research and later candidate studies existed, so their decomposition, workflow, role model and architecture sequence may encode historical assumptions that should not receive inheritance privilege.

The chosen response is therefore a **semantic clean start without historical amnesia**:

```text
preserve old repository/history
        +
do not inherit its active structure by default
        +
allow old mechanisms to return only when current evidence/problem reasoning justifies them
```

The old SOUL/KEEL structures remain useful as prior art, regression/falsification material and failure-history evidence.

---

# 3. Research → Development → Production boundary

The intended information/decision direction is:

```text
SOUL Research
finding / evidence / falsifier / open question
        ↓
Development OS
problem framing / work selection / research if needed / candidate design
        ↓
challenge / verification / decision path
        ↓
accepted development decision
        ↓
SOUL Production
implemented accepted product state
        ↓
runtime / evaluation evidence
        └──────────→ research or development re-evaluation when relevant
```

Critical invariant:

```text
research finding
!= requirement
!= architecture decision
!= implementation commitment
```

Candidate studies and Foundation work can inform, falsify or pressure-test Development OS decisions, but they do not silently mutate development or production.

---

# 4. What kind of Codex actor is being bootstrapped

The target is **not a programmer that merely implements user instructions**.

The intended Development Actor should be able to:

- recover canonical purpose/state before material work;
- distinguish user goal from proposed method;
- challenge user framing and existing structures when evidence requires it;
- identify decision-critical assumptions and uncertainty;
- decide when additional repository/web research is required;
- use `agentic-os-search` as research input without treating it as architecture authority;
- compare alternatives rather than inherit the existing mechanism;
- distinguish capability, authority, Work admission and actual Environment state;
- keep research, design, implementation, verification and integration epistemically distinct when material;
- avoid producer self-certification;
- preserve exact evidence/provenance/freshness where load-bearing;
- choose or propose the correct next Work rather than automatically converting every finding into repair/build work;
- leave durable state that a fresh Codex session can recover without hidden human orchestration;
- challenge and improve the Development OS itself under governed conditions.

The goal is not for Codex to be identical to the ChatGPT research agent or to share one fixed prompt. The goal is **functional reasoning discipline** appropriate to development work.

---

# 5. Development OS is larger than Codex

Codex is expected to be an important Actor, but it is not identical to the Development OS.

The working framing is:

```text
Development OS
= Actors
+ Information
+ Work
+ Environment
+ the relations / qualification / authority-control / transition mechanisms that compose them
```

This framing is informed by current Foundation research, but it is not yet a Development OS architecture decision.

Examples of likely surfaces include:

- Codex and human owner as Actors with different authority/participation relations;
- repositories, external sources, evidence and current state as Information surfaces;
- research/design/build/verification/recovery as possible Work regions rather than one mandatory workflow;
- local/cloud runtime, GitHub, tools and internet access as Environment conditions;
- bindings, standing/qualification, control and realized-transition checks across them.

Do not prematurely convert these diagnostic regions into fixed modules or directories.

---

# 6. Temporary ChatGPT ↔ Codex bootstrap bridge

Until `soul-development-os` can sustain itself reliably, the current working arrangement is:

```text
ChatGPT / SOUL Research agent
    - continues Foundation / research work
    - temporarily helps design the Development OS bootstrap
    - prepares prompts/instructions for Codex when useful
    - reviews Codex-created repository state through GitHub
    - challenges premature or weak Development OS decisions

Human owner
    - can relay messages between ChatGPT and Codex during bootstrap
    - retains genuine vision/value/authority decisions
    - should not become the permanent hidden orchestrator

Codex Development Actor
    - explores/researches/designs/builds under the emerging Development OS
    - should progressively own its own canonical continuation/work selection
```

This bridge is intentionally temporary.

## Exit condition for the bridge

ChatGPT should return primarily to SOUL Research once a fresh Codex session can, from `soul-development-os` canonical state alone, reliably determine:

1. why the Development OS exists and the authorised end goal;
2. what is established, inferred, hypothesised, open or rejected;
3. current/next Work and how next Work is selected;
4. its own role, authority and non-authority;
5. when additional research is needed and where research authority lives;
6. when design/build/verification/acceptance must be separated;
7. how to validate completion without producer self-certification;
8. how to preserve evidence, uncertainty, exact state and continuity;
9. how to leave the repository so another fresh session can continue correctly;
10. how to challenge/reopen the Development OS itself without silently rewriting its own correctness rules.

A set of files existing is **not** sufficient to satisfy this exit condition.

---

# 7. Current Codex execution/environment exploration

## Codex Cloud

A Codex Cloud environment named:

`SOUL Development OS` / observed environment name `soul-development-os-cloud`

was created on 2026-09-06 for repository:

`batuhanozgun/soul-development-os`.

Observed configuration at creation time included:

- `universal` container image;
- automatic setup;
- container pre-cache enabled;
- agent internet access enabled with unrestricted domain access;
- no intentionally configured project secrets/environment variables at bootstrap time.

The Cloud environment remains available as an execution option.

**Freshness warning:** environment settings can change; load-bearing current claims must be re-read from Codex environment settings rather than trusted from this note.

## Current desktop/local bootstrap choice

The immediate bootstrap was then moved to the Codex desktop application because the user wanted to explicitly try **GPT-6 Astra Ultra**, while the Cloud task UI did not expose a visible model picker during setup.

A desktop project named:

`SOUL-Development-OS`

was created against a local folder intended to be the local checkout of `batuhanozgun/soul-development-os`.

At the time this note is written, a read-only capability preflight has been prepared but its results have **not yet been integrated here**. Therefore do not assume that:

- the local folder/remote binding is correct;
- cross-private-repository access works;
- web access works as intended;
- the runtime can read `agentic-os-search`;
- any Development OS files already exist.

Those are current preflight questions, not established facts.

## Model rule

The current use of Astra is an Environment/model choice for bootstrap experimentation, **not an architectural dependency**. Development OS should eventually treat model/runtime identity as a capability/environment variable rather than encode one model as permanent truth.

---

# 8. Current bootstrap sequence

The current intended bootstrap sequence is deliberately staged.

## Stage 0 — Environment capability preflight — CURRENT

Before writing any Development OS structure, Codex should read-only establish:

- actual repository/remote/branch/working-tree state;
- available local tools;
- public internet/research access;
- read-only access to `batuhanozgun/agentic-os-search`;
- read-only access to `batuhanozgun/soul-production`;
- observable model/runtime identity and limitations.

Epistemic output should distinguish `OBSERVED`, `INFERRED` and `UNKNOWN`.

No repository mutation or Development OS design should occur in this preflight.

## Stage 1 — Bootstrap problem research/design

After Environment facts are known, Codex should not be told to simply “create the Development OS.”

The next problem is to derive the **minimum sufficient bootstrap system** needed for a self-sustaining Development Actor, considering at least:

- agent-control / reasoning discipline;
- canonical project state;
- research ↔ development authority interface;
- Work selection and phase/authority boundaries;
- evidence/verification/continuity;
- GitHub as a control/coordination environment;
- fresh-session recovery;
- minimal complexity / anti-ceremony constraints.

Existing `agentic-os-search` agent-control and old SOUL/KEEL mechanisms are inputs/prior art, not templates to copy automatically.

## Stage 2 — Minimum bootstrap implementation

Only after the bootstrap design is sufficiently justified should a minimum canonical structure be implemented in `soul-development-os`.

Exact filenames, directory topology, role count, workflow shape and GitHub mechanisms are **not pre-decided** in this context file.

## Stage 3 — Fresh-session self-sustain test

Start a genuinely fresh Codex session and test the exit-condition capabilities in Section 6 without relying on chat history or the human as hidden coordinator.

Failures reopen the bootstrap design rather than being papered over by launch instructions.

## Stage 4 — Bridge retirement

When the self-sustain test is satisfactory, record that transition here, move current development authority fully to `soul-development-os`, and return the ChatGPT research agent primarily to research work.

---

# 9. Current next action

**As of 2026-09-06:** run the read-only Stage-0 Codex capability preflight in the desktop `SOUL-Development-OS` project.

The preflight must not mutate the repository or begin Development OS design. It should report:

1. current repository state;
2. local execution capabilities;
3. internet/research access;
4. cross-repository access to `agentic-os-search` and `soul-production`;
5. model/runtime visibility;
6. observed limitations;
7. bootstrap blockers.

After Codex reports, the result should be reviewed against actual GitHub state before Stage 1 begins.

---

# 10. Explicit non-decisions

The following have **not** been accepted merely because they were discussed:

- `AGENTS.md` + protocol-router is the final Development OS control architecture;
- the Research OS R01–R09 set should be copied unchanged;
- Core / Genesis / Runtime / Evolution is the new SOUL product architecture;
- GitHub Issues/Projects/Actions/PRs must all be used from day one;
- one fixed Research → Design → Build → Verify workflow is universal;
- Codex must permanently use Astra;
- Codex Cloud or local execution is the permanent runtime choice;
- the four Foundation grounds are literal software modules;
- old SOUL/KEEL mechanisms should be migrated unless re-justified.

These remain future research/design questions.

---

# 11. Update / retirement rule

Update this bridge only when the **cross-project operating context materially changes**, for example:

- repository authority/topology changes;
- bootstrap responsibility changes;
- Development OS becomes self-sustaining;
- the ChatGPT↔Codex relay arrangement changes;
- a current environment choice materially changes the bootstrap path;
- the research→development boundary changes.

Do **not** mirror routine Development OS current state here once `soul-development-os` has a reliable canonical state surface.

When the bootstrap bridge is retired, preserve this file as historical transition context and mark where future sessions should recover current Development OS state.

## Fresh-session test for this context file

A fresh SOUL Research session should be able to read:

`AGENT.md → research/INDEX.md → research/soul-context/INDEX.md → current/DEVELOPMENT-OS-BOOTSTRAP.md`

and understand the current cross-repository purpose and bootstrap responsibility without replaying the originating chat.
