# Superpowers — Study Metadata

## Identity and authority

- **Study ID:** `superpowers`
- **Title:** Superpowers — Portable Agent Skills and Software-Development Methodology
- **Study type:** `external-target`
- **Status:** ACTIVE / PARTIAL; initial orientation and bounded bootstrap investigation. [STATE.md](STATE.md) owns current work and completion state.
- **Research object:** `obra/superpowers`, including its skill contracts, integration code, supporting tools, artifacts, tests and evaluation dependencies.
- **Canonical target:** https://github.com/obra/superpowers
- **Observed branch:** `main`
- **Pinned commit:** `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`
- **Root tree:** `21219529a4e224bcb27baf8816b039c8bf7c6673`
- **Version context:** `.codex-plugin/plugin.json` declares `6.3.0`; this is a manifest observation, not a release-availability or installed-version claim.
- **Observation date:** 2026-09-17
- **Commit timestamp:** 2026-08-12T16:53:21Z, from Git commit metadata.

## Why this research exists

On 2026-09-17 the user authorised a detailed study under `research/studies/`, with an explicit methodology analogous to the gstack investigation. The objective is to understand the external system through its own mechanisms, then preserve reusable findings, limitations and comparison questions for later SOUL / Development OS work.

The object is not a catalogue of alternative reading sources like `build-your-own-x`. It is a specific implementation of agent-facing development procedures and the machinery that exposes those procedures to different hosts. This framing remains subject to source challenge; it is not a verdict that the implementation is effective or should be adopted.

## Primary question

How does Superpowers turn a development request into skill selection, bounded work, human decisions, implementation, review, verification and delivery; which parts are procedural instructions, which are executable mechanisms, and which depend on the host or model actually behaving as expected?

The study must distinguish:

`installed → discoverable → delivered to context → selected → followed → effective`.

These are different claims, not interchangeable success states.

## Potential relevance — provisional retrieval hints

| Area | Possible reuse; not an adopted design |
|---|---|
| Information | Skill descriptions versus full bodies; context delivery; specifications/plans/review evidence; source and artifact freshness. |
| Work | Request classification, stage transitions, approval, task decomposition, completion and return-to-work paths. |
| Actors | User/controller/implementer/reviewer responsibilities; delegation context; instructions versus authority and capabilities. |
| Environment | Host-specific loading/tool mappings; worktrees; shell/runtime availability; installation and optional visual tooling. |
| SOUL | Candidate mechanisms and counterexamples for choosing and maintaining work procedures without confusing an instruction with an enforced constraint. |
| Development OS | A concrete comparison case for agentic SDLC, multi-agent review, TDD/debugging, workflow portability and skill development/evaluation. |

These are many-to-many relevance hints. They do not assign Foundation nodes, establish ontology, select dependencies or authorize architecture changes.

## Reuse modes and revisit triggers

Potential modes: source-grounded mechanism reference; implementation-learning; design pressure; counterexample/falsifier; evaluation/test-case seed; rejected-option evidence if later findings warrant it.

Revisit when a question concerns procedural agent control, skill discovery, development handoffs, review independence, verification validity, environment-dependent workflow execution, or skill evolution. Read the package's current STATE and the relevant source evidence, not only this metadata.

## Epistemic and authorization boundary

This is candidate research, not Foundation truth or SOUL / Development OS architecture. Studying upstream instructions does not activate them as our agent-control rules. No installation, upstream modification, live model campaign or adoption has been authorised by this study request.

The first round includes source inspection and narrowly scoped local probes of one byte-verified hook script in synthetic temporary fixtures. It does not demonstrate real host startup, model skill selection, obedience, development quality, Windows behavior, or end-to-end reliability. Research completion and product qualification remain different judgments.

## Freshness

Claims are bound to the pinned commit unless explicitly identified otherwise. Before current operational reuse, compare upstream HEAD and relevant host versions, then re-read changed load-bearing sources. Do not silently mix a future README, release note or integration with this corpus. External evaluation repositories, if later needed, require their own version pin and evidence boundary.

## Entrypoints

- [STATE.md](STATE.md) — authority, current work, cold-start and next action.
- [INDEX.md](INDEX.md) — retrieval router.
- [METHOD.md](METHOD.md) — source-first synthesis and verification method.
- [PLAN.md](PLAN.md) — provisional investigation units and completion criteria.
- [SOURCE-LEDGER.md](SOURCE-LEDGER.md) — inspected sources, topology and coverage limits.
- [notes/U01-entry-routing-and-bootstrap.md](notes/U01-entry-routing-and-bootstrap.md) — first bounded findings and local probe interpretation.

## Related studies

[gstack](../gstack/META.md) supplies the research-method precedent: semantic synthesis with source backreferences, not a ready-made Superpowers architecture. Its METHOD and META were read for this round; no current gstack behavior comparison was performed.

Hermes Agent, the AI-native SDLC playbook and context/memory/harness studies are possible later comparators. They were not substantively revalidated in this round. Selective recovery is required before using their findings as evidence.
