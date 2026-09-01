# Records / Persistent Information — Vertical Research

## Purpose

Research the persistent-information / Records problem domain independently before using it inside a broader SOUL architecture model.

The concern is broader than a database or file format: what information-bearing things persist, what makes them identifiable/interpretable, what context must survive, how they change, how they are organised/retrieved, how requirements vary by use/risk/horizon, and when persistence should end or custody should change.

The directory name `records-artifacts/` is retained for continuity. Current research does not treat unqualified `artifact` as a foundational super-category.

## Current status

**SUFFICIENTLY COMPLETE FOR THE CURRENT FOUNDATION PURPOSE.**

The vertical should not keep expanding by default. Reopen only if later Work/Actors/architecture research produces a material Records counterexample or new first-order gap.

## Read first

1. `STATE.md` — current status, remaining boundaries and reopen condition.
2. `synthesis/RECORDS-VERTICAL-SYNTHESIS.md` — consolidated bounded result.
3. `INDEX.md` — topic/pass/source routing.
4. `OPEN-QUESTIONS.md` — bounded residual questions and classification.
5. Exact pass syntheses/source ledgers only when deeper evidence recovery is needed.

## Research map

### Pass 1 — Foundational
- `RESEARCH-PLAN.md`
- `FOUNDATIONAL-SYNTHESIS.md`
- `SOURCES.md`

### Pass 2 — Object boundaries / recordhood / artifact
- `OBJECT-BOUNDARIES-PLAN.md`
- `synthesis/OBJECT-BOUNDARIES.md`
- `synthesis/ARTIFACT-COUNTERCHECK.md`

### Pass 3 — Minimum preservation closure
- `MINIMUM-ENVELOPE-PLAN.md`
- `synthesis/MINIMUM-ENVELOPE.md`
- `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md`

### Pass 4 — Change / status / temporal semantics
- `CHANGE-LIFECYCLE-PLAN.md`
- `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md`
- `synthesis/CHANGE-STATUS-TEMPORAL-COUNTERCHECK.md`

### Pass 5 — Organisation / derived views / retrieval
- `ORGANISATION-RETRIEVAL-PLAN.md`
- `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md`
- `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md`

### Pass 6 — Requirement profile / recurrent appraisal
- `REQUIREMENT-PROFILE-PLAN.md`
- `synthesis/REQUIREMENT-PROFILE-DERIVATION.md`
- `synthesis/REQUIREMENT-PROFILE-COUNTERCHECK.md`

### Pass 7 — Mechanism pattern landscape
- `MECHANISM-PATTERNS-PLAN.md`
- `synthesis/MECHANISM-PATTERN-LANDSCAPE.md`
- `synthesis/MECHANISM-PATTERN-COUNTERCHECK.md`

### Pass 8 — Retention / appraisal / disposition
- `RETENTION-DISPOSITION-PLAN.md`
- `synthesis/RETENTION-DISPOSITION-SEMANTICS.md`
- `synthesis/RETENTION-DISPOSITION-COUNTERCHECK.md`

### Completeness / omission review
- `VERTICAL-COMPLETENESS-PLAN.md`
- `synthesis/VERTICAL-COMPLETENESS-COUNTERCHECK.md`
- `synthesis/RECORDS-VERTICAL-SYNTHESIS.md`

Pass-specific source ledgers live under `sources/`.

## Consolidated working principles

- `record` is not every stored/persistent thing;
- resource identity ≠ version identity ≠ representation/copy identity;
- recordhood is contextual/functional as well as representational;
- preservation minimum is purpose/profile relative and logically distributed, not one universal metadata bundle;
- change/currentness/history cannot be reduced to one `update`, status or timestamp;
- organisation may preserve context, description/knowledge or access and these functions may diverge;
- retrieval sufficiency depends on the claim/question, corpus coverage, standing/as-of scope and freshness/recall;
- requirement necessity, assurance depth, satisfaction location and verification are separate decisions;
- mechanisms are partial satisfiers of Records requirements, not automatic complete solutions;
- correct persistence includes appraisal/retention/disposition as well as preservation;
- destruction/removal/transfer and residual history are distinct semantic outcomes;
- authenticity/integrity/history preservation does not establish factual truth.

## Vertical isolation

Records research exposes relations to Work, Actors, authority and evidence but does not solve them.

See `DEFERRED-RELATIONS.md`.

No database, graph/vector store, Git/event-sourcing model, search engine, deletion mechanism, Actor model, Work model, Development System design or SOUL architecture has been selected.

## Epistemic rule

Research findings are not SOUL architecture decisions. Source ledgers and syntheses are derived research views; exact/load-bearing claims remain recoverable to primary sources.

`Sufficiently complete` means enough foundation to stop expanding this vertical by default — not final truth, universal ontology or independent verification.