# Records / Artifacts — Vertical Research

## Purpose

Research the persistent-information / records problem domain independently before using it inside a broader SOUL architecture model.

The concern is broader than a database or file format: what information-bearing things persist across time, what makes them identifiable and trustworthy, how they are represented and stored, how they change, how they are organised and related, and how they can be found and recovered later.

The directory name `records-artifacts/` is retained for continuity. Current research no longer assumes that unqualified `artifact` is a valid foundational super-category.

## Current status

Two bounded internal passes have reached their explicit user-return conditions on 2026-09-01:

1. **Foundational Records pass** — established the broad problem structure and rejected a storage-first framing.
2. **Object-boundaries pass** — compared recordhood models; tested resource/record/representation/copy/version/derivation/aggregation boundaries; tested `artifact`; and mapped identity/change cases.

The Records vertical itself remains open.

## Current canonical reading order

1. `STATE.md` — current vertical state, findings and authorisation boundary.
2. `INDEX.md` — topic/claim retrieval routing.
3. `synthesis/OBJECT-BOUNDARIES.md` — current main bounded synthesis for recordhood/object boundaries.
4. `synthesis/ARTIFACT-COUNTERCHECK.md` — adverse-evidence refinement of the artifact verdict.
5. `OPEN-QUESTIONS.md` — current prioritised internal Records queue.
6. `FOUNDATIONAL-SYNTHESIS.md` — broader foundational synthesis when earlier problem structure is needed.
7. Source ledgers and primary sources as routed by `INDEX.md`.

Pass plans:
- `RESEARCH-PLAN.md` — foundational-pass method/return condition.
- `OBJECT-BOUNDARIES-PLAN.md` — object-boundaries method/return condition.

Cross-vertical observations:
- `DEFERRED-RELATIONS.md`.

## Current bounded working model

The evidence is strong enough to keep these concepts separate during further research, without treating them as final SOUL primitives:

- higher-level persistent information resource/content identity;
- record role/status;
- representation / instantiation;
- copy / instance;
- version / revision;
- semantic derivation / derived information object;
- aggregation / set.

The current recordhood synthesis is hybrid rather than storage-based:

> A plausible record must be a persistent/recoverable information representation, but recordhood also depends on documentary relation to activity/occurrence/context and on a continuing recordkeeping/reference/evidence/accountability/information function.

This is a research synthesis, not a universal legal definition.

## `Artifact` boundary

The object-boundaries pass does **not** support unqualified `artifact` as the super-category for this vertical.

Reason:
- archival usage can mean a physical/man-made object or material-value object;
- software/systems usage often means a work product;
- assessment usage can mean supporting evidence;
- forensic usage can mean an unintended process by-product/distortion.

An adversarial counter-check also found coherent qualified artifact ontologies, including `technical artifact` and `information artifact` / information-content ontology traditions.

Therefore the bounded verdict is:

- discard **unqualified** `artifact` as a foundational Records primitive;
- retain qualified artifact concepts as legitimate candidates when their ontology is explicit;
- do not rename this package until the neutral broader persistent-information category above/around `record` is better resolved.

## Anti-collapse rules now supported

- `record` ≠ every stored/persistent thing;
- resource/content identity ≠ representation/instantiation identity;
- copy identity ≠ record status;
- broader resource identity ≠ version/revision identity;
- representation ≠ semantic derivation;
- current/authoritative status ≠ historical existence/identity;
- authenticity/integrity ≠ factual correctness;
- aggregation/order/relations can carry meaning not recoverable from isolated item payloads;
- a new file does not automatically mean a new record, and the same bits do not guarantee the same record status.

## Current highest-information question

Before comparing storage, organisation, retrieval, database, graph, vector, Git, or other mechanisms, the current best next question is:

> **What is the minimum persistent information / record envelope required to preserve identity, interpretation, context, provenance, temporal/status semantics, integrity, relationships, and retrievability across time — and which properties vary by information-resource class or retention horizon?**

This is `next logical work`, not automatic execution authority.

## Vertical isolation

This research may discover that records depend on work, actors, authority, or other concepts. Such relations are captured in `DEFERRED-RELATIONS.md` when material, but the active research does not turn into Work, Actors, orchestration, Development System, or SOUL architecture research.

Isolation is methodological only. It does not assume records are ontologically independent.

## Scope evolution

The terms `records-artifacts` remain historical/provisional labels. If later evidence supports `records`, `persistent-information`, `information-resource`, or another frame, repository structure may be changed explicitly rather than forcing findings into the initial name.

## Epistemic rule

Research findings are not SOUL architecture decisions. Source ledgers, indexes, and syntheses are derived research views; load-bearing exact claims must remain recoverable to primary sources.