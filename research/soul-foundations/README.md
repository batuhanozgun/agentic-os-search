# SOUL Foundations Research

## Purpose

This research package studies the foundational problem domains that may underlie SOUL before attempting a full SOUL architecture synthesis.

It is intentionally layered. Earlier research may change the structure, scope, or even the necessity of later research. The repository records the path actually supported by research; it does not pre-create future layers as if their necessity were already known.

## Current research hypothesis

The starting hypothesis was that three problem domains deserved independent vertical research:

1. **Records / Artifacts** — what persists, how information is represented, stored, organised, governed, changed, traced, and retrieved.
2. **Work** — what must be done, changed, investigated, verified, or completed, and how such work is represented and controlled.
3. **Actors** — what performs work or exercises authority, and how identity, capability, responsibility, delegation, and accountability are represented.

All three have now been independently researched to bounded sufficiency for the current foundation purpose.

The post-vertical discussion produced two additional working hypotheses:

- these three may be recurrent foundational system dimensions rather than mutually exclusive object classes or fixed SOUL modules;
- **Environment** may be a fourth foundational region concerning the conditions, resources, tools/capabilities, external systems and observable/changeable state within which Actors perform Work and Records obtain/use context.

Environment is a **candidate research region**, not an accepted fourth SOUL primitive or architecture component.

The same discussion also identified a possible cross-cutting **relation / control / coordination fabric** that may later be needed to explain how foundational dimensions form a coherent controlled working system. This is a working hypothesis for later study, not current architecture truth.

## Current status

Records, Work and Actors are sufficiently complete and user-evaluated for the current foundation purpose.

The three-vertical discussion has completed to a next-research checkpoint. The user has authorised an **independent Environment foundation research pass** designed to test rather than assume the fourth-leg hypothesis.

Current handoff:
- `ENVIRONMENT-RESEARCH-HANDOFF.md`

Earlier discussion-entry handoff:
- `DISCUSSION-HANDOFF.md`

Current state/router:
- `STATE.md`
- `INDEX.md`

Broad cross-vertical composition/relations research, SOUL architecture and implementation remain later steps requiring separate evaluation/authorization.

## Layering rule

- Layer 0 provides bounded context and problem reconstruction from prior repository research.
- Layer 1 independently researched Records, Work and Actors.
- Environment is now an authorised candidate foundation pass whose job is to test whether another first-order region exists; its result may confirm, split, rename or dissolve the current Environment framing.
- Later synthesis/composition layers remain undetermined until evidence and explicit user direction justify them.

A later synthesis may confirm, refine, add to, replace, or dissolve the current decomposition.

## Vertical isolation rule

Each completed Layer-1 vertical was researched independently. When research encountered a materially important relation to another vertical, it recorded that relation as a deferred question rather than allowing the vertical to drift into premature synthesis.

Isolation was methodological, not ontological: completion of independent research does not establish that the domains are truly independent in reality.

The Environment pass should preserve the same discipline. It may use the completed verticals to identify boundary questions, but it must not treat their cross-vertical hypotheses as axioms proving Environment's necessity.

## Epistemic rule

Research findings, taxonomies, models, cross-vertical inferences and working hypotheses produced here are evidence/research outputs. They do not automatically become SOUL architecture decisions.

Keep separate:

- established vertical findings;
- cross-vertical inferences;
- working hypotheses;
- open questions;
- candidate decisions;
- accepted architecture decisions.

## Research-work continuity rule

This research itself is conducted across fresh ChatGPT sessions in a ChatGPT Project with GitHub as the canonical persistent surface.

Conversation memory is not sufficient project state. A fresh session must be able to recover from repository state:

- the current research purpose;
- what is established versus hypothesised;
- current authorisation and next responsibility;
- relevant retrieval routes;
- unresolved questions and handoff context.

The current operating arrangement is described in `ENVIRONMENT-RESEARCH-HANDOFF.md` and current authority/state in `STATE.md`.

## Relationship to `research/soul-context/`

`research/soul-context/` remains the bounded context-reconstruction package for SOUL, Development OS and predecessor work. It is not duplicated here. Use its `INDEX.md` to recover SOUL / Development OS intent and the research–architecture boundary when those topics become relevant.