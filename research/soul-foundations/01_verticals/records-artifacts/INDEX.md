# Records / Persistent Information — INDEX

## Role

This file is the retrieval router for `records-artifacts/**`. It is not evidence and is not a source of architectural truth.

## Default reading order

1. `STATE.md` — current result and authorisation boundary.
2. `synthesis/MINIMUM-ENVELOPE.md` — latest bounded Records synthesis.
3. `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md` — adverse/omission test of the latest frame.
4. `synthesis/OBJECT-BOUNDARIES.md` — recordhood/object-boundary basis when needed.
5. `FOUNDATIONAL-SYNTHESIS.md` — original broad foundation when earlier concepts/failure surfaces are needed.
6. relevant pass-specific ledger under `sources/`.
7. for exact/load-bearing claims, recover the primary source named by the ledger.

## Topic routing

| Topic / question | Read first | Then / source trace |
|---|---|---|
| Current Records state / authorised work | `STATE.md` | `OPEN-QUESTIONS.md` |
| Why `minimum envelope` changed frame | `synthesis/MINIMUM-ENVELOPE.md` sections 1–3 | `sources/minimum-envelope.md` |
| What must remain knowable/recoverable? | `synthesis/MINIMUM-ENVELOPE.md` sections 4–8 | `sources/minimum-envelope.md` |
| Identity + exact metadata/resource binding | `synthesis/MINIMUM-ENVELOPE.md` O1 | `sources/minimum-envelope.md` — OAIS/PREMIS/NARA/NAA/DataCite/FAIR |
| Interpretability / representation information | `synthesis/MINIMUM-ENVELOPE.md` O2 | `sources/minimum-envelope.md` — OAIS/PREMIS/NARA |
| Provenance / context / origin history | `synthesis/MINIMUM-ENVELOPE.md` O3 | `sources/minimum-envelope.md` — ISO 23081/OAIS/PROV/RiC/NARA/NAA |
| Temporal / version / currentness closure | `synthesis/MINIMUM-ENVELOPE.md` O4 | `OPEN-QUESTIONS.md` Q1; prior provenance/time ledger |
| Integrity / fixity / authenticity minimum | `synthesis/MINIMUM-ENVELOPE.md` O5 | `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md` C4; source ledger |
| Relations / aggregation / derivation closure | `synthesis/MINIMUM-ENVELOPE.md` O6 | `synthesis/OBJECT-BOUNDARIES.md`; RiC/NARA/PREMIS/FAIR in source ledger |
| Rights / access / use constraints | `synthesis/MINIMUM-ENVELOPE.md` O7 | `sources/minimum-envelope.md` — OAIS/NARA/NAA/FAIR |
| Discovery / retrieval-path closure | `synthesis/MINIMUM-ENVELOPE.md` O8 | `OPEN-QUESTIONS.md` Q8–Q9 |
| Preservation Objectives / significant properties | `synthesis/MINIMUM-ENVELOPE.md` M1–M2 | `sources/minimum-envelope.md` — OAIS/PREMIS |
| Intrinsic vs external/inherited metadata | `synthesis/MINIMUM-ENVELOPE.md` section 6 | `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md` C5 |
| How minimum changes by horizon / resource class | `synthesis/MINIMUM-ENVELOPE.md` sections 9–10 | `sources/minimum-envelope.md` — especially NAA/OAIS/NARA |
| Counterexamples to the closure model | `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md` | `sources/minimum-envelope.md` |
| Minimum-envelope pass method / return condition | `MINIMUM-ENVELOPE-PLAN.md` | `STATE.md`, main synthesis section 16 |
| Recordhood: what makes something a record? | `synthesis/OBJECT-BOUNDARIES.md` | `sources/object-boundaries-recordhood.md`, `FOUNDATIONAL-SYNTHESIS.md` |
| Resource / record / representation / copy / version / derivation / aggregation boundaries | `synthesis/OBJECT-BOUNDARIES.md` | `sources/object-boundaries-recordhood.md` |
| `Artifact` current verdict | `synthesis/ARTIFACT-COUNTERCHECK.md` | `sources/artifact-counterframe.md`, object-boundaries synthesis |
| Broad foundational record/data/state/event/evidence distinctions | `FOUNDATIONAL-SYNTHESIS.md` | `SOURCES.md`, foundational source ledgers |
| Authenticity / reliability / integrity / correctness distinctions | `synthesis/CONCEPT-BOUNDARIES.md` | foundational/preservation source ledgers |
| Failure modes | `synthesis/FAILURE-MODES.md` | relevant ledger |
| Next high-information Records questions | `OPEN-QUESTIONS.md` | relevant synthesis/source ledger |
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

## Epistemic status

- Plans define authorised question/scope/return condition; they are not evidence.
- Source ledgers are derived retrieval aids; they do not replace the named primary sources.
- Syntheses are bounded research conclusions, not SOUL requirements or architecture decisions.
- `OPEN-QUESTIONS.md` is a prioritised queue, not execution authority.
- `DEFERRED-RELATIONS.md` preserves cross-vertical observations without solving them from Records.

The package name `records-artifacts/` remains provisional/historical. Current evidence rejects unqualified `artifact` as a foundational Records super-category but has not yet established the best neutral umbrella category.