# Records / Persistent Information — INDEX

## Role

This file is the retrieval router for `records-artifacts/**`. It is not evidence and is not a source of architectural truth.

## Default reading order

1. `STATE.md` — current result and authorisation boundary.
2. `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` — latest bounded Records synthesis.
3. `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md` — adverse test of the latest frame.
4. `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` — change/standing/time basis.
5. `synthesis/MINIMUM-ENVELOPE.md` — preservation-closure basis.
6. `synthesis/OBJECT-BOUNDARIES.md` — recordhood/object-boundary basis.
7. `FOUNDATIONAL-SYNTHESIS.md` — original broad foundation when earlier concepts/failure surfaces are needed.
8. relevant pass-specific ledger under `sources/`.
9. for exact/load-bearing claims, recover the primary source named by the ledger.

## Topic routing

| Topic / question | Read first | Then / source trace |
|---|---|---|
| Current Records state / authorised work | `STATE.md` | `OPEN-QUESTIONS.md` |
| Organisation / derived views / retrieval semantics | `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` | `sources/organisation-retrieval-semantics.md` |
| Organisation roles: context vs knowledge vs access | `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` sections 2–3 | RiC/SAA/SKOS in pass ledger |
| Source / derived / recordkeeping designation relationships | `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` sections 4–5 | OAIS/NARA/PROV in pass ledger |
| Retrieval modes / sufficiency | `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` sections 6–8 | IR/Memento/FAIR in pass ledger |
| Stale view / freshness / propagation | `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` sections 9–10 | RFC 9111/PostgreSQL/Elasticsearch in pass ledger |
| Retrieval hit/miss and absence limits | `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` section 8 | IR/Memento + countercheck C5 |
| Organisation/retrieval adverse constraints | `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md` | pass source ledger |
| Organisation/retrieval plan / return condition | `ORGANISATION-RETRIEVAL-PLAN.md` | `STATE.md` |
| Change / status / temporal semantics | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` | `sources/change-status-temporal-semantics.md` |
| Minimum preservation closure | `synthesis/MINIMUM-ENVELOPE.md` | `sources/minimum-envelope.md` |
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

### Pass 5 — Organisation / derived views / retrieval semantics
- plan: `ORGANISATION-RETRIEVAL-PLAN.md`
- synthesis: `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md`
- adverse check: `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md`
- ledger: `sources/organisation-retrieval-semantics.md`

## Epistemic status

- Plans define authorised question/scope/return condition; they are not evidence.
- Source ledgers are derived retrieval aids; they do not replace named primary sources.
- Syntheses are bounded research conclusions, not SOUL requirements or architecture decisions.
- Adversarial supplements are self-challenges, not independent verification.
- `OPEN-QUESTIONS.md` is a prioritised queue, not execution authority.
- `DEFERRED-RELATIONS.md` preserves cross-vertical observations without solving them from Records.

The package name `records-artifacts/` remains provisional/historical. Current evidence rejects unqualified `artifact` as a foundational Records super-category but has not yet established the best neutral umbrella category.