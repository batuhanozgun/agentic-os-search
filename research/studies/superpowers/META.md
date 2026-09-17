# Superpowers — Study Metadata

## Identity and authority

- **Study ID:** `superpowers`
- **Title:** Superpowers — Portable Agent Skills and Software-Development Methodology
- **Study type:** `external-target`
- **Status:** ACTIVE / PARTIAL; U01 selected-host delivery and U02 approval/plan/workspace source models bounded-complete; U03 next. [STATE.md](STATE.md) owns work and completion state.
- **Research object:** `obra/superpowers`, including skill contracts, integration code, supporting tools, artifacts, tests and evaluation dependencies.
- **Canonical target:** https://github.com/obra/superpowers
- **Observed branch:** `main`
- **Pinned commit:** `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`
- **Root tree:** `21219529a4e224bcb27baf8816b039c8bf7c6673`
- **Version context:** inspected manifests declare `6.3.0`; not an installed-version or release-channel claim.
- **Observation date:** 2026-09-17
- **Commit timestamp:** 2026-08-12T16:53:21Z from Git commit metadata.

## Why this research exists

On 2026-09-17 the user authorised detailed research under studies with an explicit methodology analogous to gstack, reviewed successive rounds as suitable and requested continuation. The objective is to understand the system through its own mechanisms and preserve findings, limitations and comparison questions for later SOUL / Development OS work. Prior approval of a research round does not establish future findings or product efficacy.

Unlike a reading-source catalogue, this object implements agent-facing procedures and machinery exposing them to hosts. That framing is not an adoption verdict. Upstream instruction files remain research objects, not active agent-control.

## Primary question

How does Superpowers turn a development request into skill selection, bounded work, human decisions, implementation, review, verification and delivery; which parts are instructions, which executable, and which depend on host/model behavior?

Keep installed, discoverable, delivered, selected, followed and effective distinct. Also distinguish procedure revision/module/session/message lifetime from work identity: spec, plan path, plan revision, selected workspace, task brief and completion/review standing.

## Current bounded result

U01 explains selected shell-hook, native-description, declared-context/session-start and OpenCode/Pi/Hermes delivery arrangements. It records differing re-entry, caching/failure policies and role/task behavior in mappings. It is not full supported-host qualification.

U02 explains phase-conditioned authority, spec/plan/interface contracts, host-owned workspace selection, SDD ledger recovery and task extraction. It distinguishes an approved intent from an immutable artifact authorization, a saved plan from one available to an executor, and a plan path from its current revision. The controller remains responsible for transferring global constraints and resolving rulings; helper output is not equivalent to a fully qualified task.

Three bounded local experiments exist:

- U01-A exact shell script: four transport observations, two failed missing/empty health criteria, one negative control.
- U01-B exact OpenCode module: eight mechanism observations, two failed semantic-health criteria and one negative control; marker/content and stale/null cache lifetime distinctions retained.
- U02 exact workspace/task-brief helpers plus one documented ignore-check command: thirteen cases; eleven expected mechanism/representation/identity observations and two failed health criteria. Same-basename plan paths shared/overwrote a task brief; an OR predicate accepted an unignored selected directory based on another ignored directory. Same-path revisions retained a synthetic completion marker; an uncommitted plan did not appear in a new HEAD worktree. These are not observed production incidents or model behaviors.

## Potential relevance — provisional retrieval hints

| Area | Possible reuse; not an adopted design |
|---|---|
| Information | Description/full body, marker/content, cached revision, spec/plan/brief transformations, omitted global constraints and artifact materialization. |
| Work | Request classification, phase/route authority, controller rulings, task granularity, ledger resumption and revision-sensitive completion. |
| Actors | Human/controller/child/reviewer responsibilities, mapping-driven fallbacks, role/context separation and load-bearing requirement transfer. |
| Environment | Host-conditioned events, module/session lifetime, Git worktree ownership, in-place fallbacks, ignored scratch and selected-path checks. |
| SOUL | Concrete comparison cases for procedure applicability, accepted work identity, bounded actor authority, actual effect and recoverable decisions. |
| Development OS | Candidate SDLC mechanisms for spec→plan→task transfer, independent review units, workspace handoff, progress retention, testing and skill evolution. |

These are many-to-many retrieval hints, not Foundation membership, ontology, selected dependencies or architecture authority.

## Reuse modes and revisit triggers

Potential modes: mechanism reference, implementation-learning, design pressure, falsifier/counterexample, evaluation/test-case seed, negative-option evidence if later findings warrant it.

Revisit for skill discovery/delivery, cache invalidation, procedure integrity, host-specific fallback, context loss, approval/plan revision, worktree transfer, reviewer packets, decision retention or skill evolution. Start at STATE and the relevant note/source, not this metadata alone.

U01 residuals Q09–Q12 preserve host/module lifetime, marker validity, Hermes aliases and distribution seams. U02 Q13–Q17 preserve scope/ruling authority, revision rebinding, controller information transfer, ignored-evidence retention and exact-target checks.

## Epistemic and authorization boundary

Candidate research is not Foundation truth or SOUL / Development OS architecture. No installation in a user's environment, upstream modification/reporting, credentialed live-model campaign or adoption is authorised here.

Local helper/callback observations do not demonstrate host startup, model selection/obedience, development quality, real approval handling, Windows behavior or end-to-end reliability. First-party test files inspected by this study were not run. Host API/namespace/version claims in upstream references remain target claims. A descriptive probe PASS can reproduce a limitation, not certify safety.

There is an actual SDD recovery mechanism; its existence is now source-established. It must not be confused with complete preservation of every task revision, ruling or acceptance condition. No blanket absence or universal failure claim is justified.

## Freshness

Claims remain pinned. U01-B/U02 did not repin or produce a fresh current-HEAD verdict. Before operational reuse, compare upstream and relevant host versions, then reopen changed sources. A new host session need not reload a module/cache; a plan at the same path need not be the same revision. External evaluation repositories need separate identity/coverage records.

## Entrypoints

- [STATE.md](STATE.md) — authority, work, cold-start and next action.
- [INDEX.md](INDEX.md) — retrieval router.
- [METHOD.md](METHOD.md) — source-first synthesis/verification method v0.1, unchanged.
- [PLAN.md](PLAN.md) — v0.3 units, sequencing and method/plan reflection.
- [SOURCE-LEDGER.md](SOURCE-LEDGER.md) — identities, full/partial reads, execution boundaries.
- [U01-A](notes/U01-entry-routing-and-bootstrap.md) — first findings and shell probes.
- [U01-B](notes/U01B-host-delivery-and-continuity.md) — host delivery/cache/continuity.
- [U02](notes/U02-approval-plan-workspace-handoff.md) — approval/plan/workspace map, F13–F19, local evidence and residuals.

## Related studies

[gstack](../gstack/META.md) supplied the method precedent, not a ready-made Superpowers architecture. Its METHOD/META were read initially; no current-runtime comparison was performed.

Hermes Agent, AI-native SDLC, context/memory/harness and other catalogued studies remain potential later comparators. Reading an integration adapter or noting provisional relevance does not continue/revalidate those studies. Selective canonical recovery precedes cross-study conclusions.
