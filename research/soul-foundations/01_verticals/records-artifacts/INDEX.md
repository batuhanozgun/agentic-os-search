# Records / Persistent Information — INDEX

## Role

This file is the retrieval router for `records-artifacts/**`. It is not evidence and is not a source of architectural truth.

## Default reading order

1. `STATE.md` — current result and authorisation boundary.
2. `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` — latest bounded Records synthesis.
3. `synthesis/CHANGE-STATUS-TEMPORAL-COUNTERCHECK.md` — adverse test of the latest frame.
4. `synthesis/MINIMUM-ENVELOPE.md` — preservation-closure basis.
5. `synthesis/OBJECT-BOUNDARIES.md` — recordhood/object-boundary basis.
6. `FOUNDATIONAL-SYNTHESIS.md` — original broad foundation when earlier concepts/failure surfaces are needed.
7. relevant pass-specific ledger under `sources/`.
8. for exact/load-bearing claims, recover the primary source named by the ledger.

## Topic routing

| Topic / question | Read first | Then / source trace |
|---|---|---|
| Current Records state / authorised work | `STATE.md` | `OPEN-QUESTIONS.md` |
| Change / status / temporal semantics | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` | `sources/change-status-temporal-semantics.md` |
| Why generic `update` fails | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` sections 2–4 | pass source ledger |
| Revision vs migration vs derivation | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` C3–C5 | PROV/PREMIS/DataCite/JAV in source ledger |
| Supersession vs correction vs retraction/removal | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` C6–C9 | NISO CREC/JAV, ICMJE, Crossref, DataCite |
| Destruction / disposition record-side boundary | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` C11 | NARA in pass source ledger |
| Why one universal status enum fails | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` sections 5–6 | RiC/Crossref/NISO/PREMIS evidence |
| Effective/applicable vs system-known time | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` section 7 | Jensen/Snodgrass temporal sources |
| Current vs historical reconstruction | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` section 8 | pass source ledger |
| Counterexamples / architecture contamination check | `synthesis/CHANGE-STATUS-TEMPORAL-COUNTERCHECK.md` | pass source ledger |
| Change pass plan / return condition | `CHANGE-LIFECYCLE-PLAN.md` | `STATE.md` |
| Minimum preservation closure | `synthesis/MINIMUM-ENVELOPE.md` | `sources/minimum-envelope.md` |
| Minimum-closure adverse check | `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md` | `sources/minimum-envelope.md` |
| Recordhood / object boundaries | `synthesis/OBJECT-BOUNDARIES.md` | `sources/object-boundaries-recordhood.md` |
| `Artifact` current verdict | `synthesis/ARTIFACT-COUNTERCHECK.md` | `sources/artifact-counterframe.md` |
| Broad foundational distinctions | `FOUNDATIONAL-SYNTHESIS.md` | `SOURCES.md`, foundational source ledgers |
| Authenticity / reliability / integrity / correctness | `synthesis/CONCEPT-BOUNDARIES.md` | foundational/preservation ledgers |
| Failure modes | `synthesis/FAILURE-MODES.md` | relevant ledger |
| Next high-information Records questions | `OPEN-QUESTIONS.md` | latest relevant synthesis |
| Cross-vertical observations | `DEFERRED-RELATIONS.md` | later Work/Actors/synthesis only |

## Pass map

### Pass 1 — Foundational
- plan: `RESEARCH-PLAN.md`
- synthesis: `FOUNDATIONAL-SYNTHESIS.md`
- main ledger: `SOURCES.md`

### Pass 2 — Object boundaries
- plan: `OBJECT-BOUNDARIES-PLAN.md`
- synthesis: `synthesis/OBJECT-BOUNDARIES.md`
- artifact adverse check: `synthesis/ARTIFACT-COUNTERCHECK.md`
- ledgers: `sources/object-boundaries-recordhood.md`, `sources/artifact-counterframe.md`

### Pass 3 — Minimum preservation closure
- plan: `MINIMUM-ENVELOPE-PLAN.md`
- synthesis: `synthesis/MINIMUM-ENVELOPE.md`
- adverse check: `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md`
- ledger: `sources/minimum-envelope.md`

### Pass 4 — Change / status / temporal semantics
- plan: `CHANGE-LIFECYCLE-PLAN.md`
- synthesis: `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md`
- adverse check: `synthesis/CHANGE-STATUS-TEMPORAL-COUNTERCHECK.md`
- ledger: `sources/change-status-temporal-semantics.md`

## Epistemic status

- Plans define authorised question/scope/return condition; they are not evidence.
- Source ledgers are derived retrieval aids; they do not replace named primary sources.
- Syntheses are bounded research conclusions, not SOUL requirements or architecture decisions.
- Adversarial supplements are self-challenges, not independent verification.
- `OPEN-QUESTIONS.md` is a prioritised queue, not execution authority.
- `DEFERRED-RELATIONS.md` preserves cross-vertical observations without solving them from Records.

The package name `records-artifacts/` remains provisional/historical. Current evidence rejects unqualified `artifact` as a foundational Records super-category but has not yet established the best neutral umbrella category.