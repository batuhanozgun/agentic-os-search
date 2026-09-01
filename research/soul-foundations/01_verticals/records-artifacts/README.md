# Records / Persistent Information — Vertical Research

## Purpose

Research the persistent-information / records problem domain independently before using it inside a broader SOUL architecture model.

The concern is broader than a database or file format: what information-bearing things persist across time, what makes them identifiable and trustworthy, how they are represented, how their meaning/context survives, how they change, how they are organised/related, and how they can be found and reconstructed later.

The directory name `records-artifacts/` is retained for continuity. Current research no longer assumes that unqualified `artifact` is a valid foundational super-category.

## Current status

Three bounded internal passes have reached explicit user-return conditions on 2026-09-01:

1. **Foundational Records pass** — established the broad problem structure and rejected a storage-first framing.
2. **Object-boundaries pass** — compared recordhood models; separated resource/record/representation/copy/version/derivation/aggregation; tested `artifact`; and mapped identity/change cases.
3. **Minimum preservation-closure pass** — tested what information must survive with/around persistent resources and rejected one universal object-local metadata bundle.

The Records vertical itself remains open.

## Current canonical reading order

1. `STATE.md` — current vertical state, bounded findings and authorisation boundary.
2. `INDEX.md` — topic/claim retrieval routing.
3. `synthesis/MINIMUM-ENVELOPE.md` — latest bounded synthesis: minimum preservation closure.
4. `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md` — adverse/omission check for that frame.
5. `synthesis/OBJECT-BOUNDARIES.md` — prior recordhood/object-boundaries synthesis.
6. `synthesis/ARTIFACT-COUNTERCHECK.md` — artifact adverse-evidence refinement.
7. `OPEN-QUESTIONS.md` — current prioritised internal Records queue.
8. `FOUNDATIONAL-SYNTHESIS.md` — original broader foundational synthesis when earlier problem structure is needed.
9. Pass-specific source ledgers and their primary sources as routed by `INDEX.md`.

Pass plans:
- `RESEARCH-PLAN.md` — foundational pass;
- `OBJECT-BOUNDARIES-PLAN.md` — object-boundaries pass;
- `MINIMUM-ENVELOPE-PLAN.md` — minimum preservation-closure pass.

Source note:
- `SOURCES.md` is the consolidated **foundational-pass** ledger;
- later passes maintain explicit pass-specific ledgers under `sources/` so later evidence does not silently rewrite the earlier corpus.

Cross-vertical observations:
- `DEFERRED-RELATIONS.md`.

---

# Current bounded working model

## Object boundaries

The evidence is strong enough to keep these concepts separate during further research, without treating them as final SOUL primitives:

- higher-level persistent information resource/content identity;
- record role/status;
- representation / instantiation;
- copy / instance;
- version / revision;
- semantic derivation / derived information object;
- aggregation / set.

Recordhood remains hybrid rather than storage-based: persistence/recoverability is necessary to the current working model, while documentary relation to activity/occurrence/context and continuing recordkeeping/reference/evidence/accountability/information function contribute record status/meaning.

## `Artifact` boundary

Unqualified `artifact` is not retained as the super-category for this vertical because its meanings across archival, software, assessment and forensic domains are materially different.

Qualified artifact concepts remain legitimate where their ontology is explicit (`information artifact`, `technical artifact`, etc.). The package is not renamed yet because the neutral broader category around `record` remains unresolved.

---

# Latest result — minimum preservation closure

The third pass materially changed the question from:

> `Which metadata fields must every persistent object contain?`

into:

> `What must remain reliably knowable/recoverable for the intended future use, and where may that information safely live?`

The current working research frame is:

> **Minimum preservation closure** = the smallest set of information, relationships, interpretive dependencies, controls and reliable bindings — intrinsic or externally/inheritedly available — required for a specified future use of a specified resource class at a specified horizon/risk level.

This is a local research term, not a standard or architecture component.

## Variables that change the closure

- intended future use / protected capability;
- resource class/structure;
- retention horizon / environmental change;
- risk, security, legal and business obligations;
- expected transformations;
- future target knowledge base/community.

## Recurring obligation families

- referential identity + exact binding;
- interpretability / representation information;
- origin / provenance / contextual history;
- temporal/version/status information when change matters;
- integrity/continuity evidence proportional to horizon/risk;
- relationship/aggregation/derivation information when dependencies exist;
- rights/access/use constraints when applicable;
- discovery/retrieval path at system level.

Long-term/transformation work adds two important meta-obligations:

- explicit preservation/use objective + target knowledge base;
- significant/transformational properties that must survive change.

These are **obligation families, not fields**.

## Placement result

Required knowledge need not be physically embedded in every object. It may be external, inherited, relational, system-level, or reconstructable if:

- exact binding is preserved;
- dependencies remain resolvable and version-correct;
- historical scope/membership remains reconstructable;
- representation/context dependencies remain interpretable;
- receiving environments can materialise or resolve what they need during transfer.

Therefore the envelope boundary is **logical rather than necessarily physical**.

---

# Anti-collapse rules now supported

- `record` ≠ every stored/persistent thing;
- resource identity ≠ version identity ≠ representation/copy identity;
- representation ≠ semantic derivation;
- current/authoritative status ≠ historical existence;
- authenticity/integrity ≠ factual correctness;
- preservation obligation ≠ metadata field;
- `repository needs to know X` ≠ `X must be duplicated inside every object`;
- persistent identifier ≠ guaranteed future availability/resolution;
- fixity ≠ provenance/truth/current validity;
- preserved resource ≠ retrievable/discoverable resource;
- longer retention horizon ≠ the only reason metadata/control depth can increase.

---

# Current highest-information question

The first three passes now provide enough ground to move from `what is the persistent thing?` and `what must remain knowable?` to the major unresolved dynamic problem:

> **How should persistent information change through time — creation, revision, supersession, correction, retraction/invalidation, derivation, migration and disposition — so that current status/truth, historical truth, identity and provenance remain simultaneously reconstructable?**

This is `next logical work`, not automatic execution authority.

See `OPEN-QUESTIONS.md` for competing next candidates and residual uncertainties.

## Vertical isolation

Records research may expose relations to Work, Actors, authority or evidence. Material relations are captured in `DEFERRED-RELATIONS.md` but are not solved from this vertical.

No storage topology, database, vector system, Git model, agent memory architecture, Work model, Actor model, Development System design or SOUL architecture has been selected by these passes.

## Scope evolution

The package name remains historical/provisional. If later evidence supports `records`, `persistent-information`, `information-resource`, or another frame, repository structure may be changed explicitly rather than forcing the research into the initial label.

## Epistemic rule

Research findings are not SOUL architecture decisions. Plans, source ledgers, indexes and syntheses are derived research views; load-bearing exact claims must remain recoverable to primary sources.