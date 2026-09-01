# Records / Persistent Information — INDEX

## Role

Retrieval router for `records-artifacts/**`. This file is not evidence or architectural truth.

## Default reading order

1. `STATE.md` — status, boundary, reopen condition.
2. `synthesis/RECORDS-VERTICAL-SYNTHESIS.md` — consolidated bounded result.
3. `OPEN-QUESTIONS.md` — remaining issues classified by type.
4. Relevant pass synthesis/counter-check.
5. Relevant pass source ledger under `sources/`.
6. For exact/load-bearing claims, recover the primary source named by the ledger.

## Topic routing

| Topic | Read first | Then |
|---|---|---|
| Overall Records result | `synthesis/RECORDS-VERTICAL-SYNTHESIS.md` | `STATE.md` |
| Why the vertical stopped | `synthesis/VERTICAL-COMPLETENESS-COUNTERCHECK.md` | `VERTICAL-COMPLETENESS-PLAN.md`, completeness source ledger |
| What is a record / object boundaries | `synthesis/OBJECT-BOUNDARIES.md` | `FOUNDATIONAL-SYNTHESIS.md`, object source ledger |
| `Artifact` verdict | `synthesis/ARTIFACT-COUNTERCHECK.md` | artifact source ledger |
| What must persist / preservation closure | `synthesis/MINIMUM-ENVELOPE.md` | counter-check + minimum-envelope ledger |
| Change / status / time | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` | counter-check + pass ledger |
| Organisation / derived views / retrieval | `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` | counter-check + pass ledger |
| Requirement/profile derivation | `synthesis/REQUIREMENT-PROFILE-DERIVATION.md` | counter-check + `sources/requirement-profile-derivation.md` |
| Storage/history/search mechanism patterns | `synthesis/MECHANISM-PATTERN-LANDSCAPE.md` | counter-check + `sources/mechanism-pattern-landscape.md` |
| Retention / appraisal / disposition | `synthesis/RETENTION-DISPOSITION-SEMANTICS.md` | counter-check + `sources/retention-disposition.md` |
| Failure modes | `synthesis/FAILURE-MODES.md` | relevant pass synthesis/source ledger |
| Remaining unresolved issues | `OPEN-QUESTIONS.md` | `STATE.md` |
| Work / Actors relations deliberately deferred | `DEFERRED-RELATIONS.md` | later independent verticals/synthesis |

## Pass map

1. Foundational — `RESEARCH-PLAN.md` → `FOUNDATIONAL-SYNTHESIS.md`
2. Object boundaries — `OBJECT-BOUNDARIES-PLAN.md` → `synthesis/OBJECT-BOUNDARIES.md`
3. Minimum preservation closure — `MINIMUM-ENVELOPE-PLAN.md` → `synthesis/MINIMUM-ENVELOPE.md`
4. Change/status/time — `CHANGE-LIFECYCLE-PLAN.md` → `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md`
5. Organisation/retrieval — `ORGANISATION-RETRIEVAL-PLAN.md` → `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md`
6. Requirement profile — `REQUIREMENT-PROFILE-PLAN.md` → `synthesis/REQUIREMENT-PROFILE-DERIVATION.md`
7. Mechanism patterns — `MECHANISM-PATTERNS-PLAN.md` → `synthesis/MECHANISM-PATTERN-LANDSCAPE.md`
8. Retention/disposition — `RETENTION-DISPOSITION-PLAN.md` → `synthesis/RETENTION-DISPOSITION-SEMANTICS.md`
9. Completeness review — `VERTICAL-COMPLETENESS-PLAN.md` → `synthesis/VERTICAL-COMPLETENESS-COUNTERCHECK.md` → `synthesis/RECORDS-VERTICAL-SYNTHESIS.md`

Each later pass has a companion adversarial counter-check where applicable. Source ledgers remain derived retrieval aids, not substitutes for primary sources.

## Epistemic status

- The consolidated synthesis is **sufficient for current foundation purpose**, not final ontology.
- `OPEN-QUESTIONS.md` no longer functions as an automatic internal execution queue; it records bounded residual uncertainty and reopen triggers.
- The package name `records-artifacts/` remains historical/provisional.