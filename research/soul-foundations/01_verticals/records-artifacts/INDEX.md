# Records / Persistent Information — INDEX

## Role

Retrieval router for `records-artifacts/**`. This file is not evidence or architectural truth.

## Status gate

`STATE.md` is not part of the content-depth ladder. Read it first whenever current status, scope, remaining uncertainty, or reopen conditions matter.

## Layered reading order

### L0 — Key

`KEY.md`

Use for the shortest accurate orientation: domain purpose, strongest results, rejected shortcuts, and limits.

### L1 — Findings map

`FINDINGS-MAP.md`

Use to identify which problem area matters and which deeper document should be loaded next.

### L2 — Integrated vertical synthesis

`synthesis/RECORDS-VERTICAL-SYNTHESIS.md`

Use when the question spans several Records dimensions or the consolidated vertical model is needed.

### L3 — Topic synthesis

Read the relevant focused synthesis listed in the topic-routing table below.

### L4 — Challenge and evidence recovery

1. Read the companion adversarial counter-check when the focused synthesis needs to be challenged.
2. Read the relevant source ledger under `sources/` when claim provenance, source scope, or competing evidence matters.

### L5 — Primary source

For exact/load-bearing claims, recover the primary source URL named in the source ledger and read the primary source itself.

## Layer rule

Higher layers are deliberately lossy derived views. They are useful for routing and bounded understanding, but they do not gain authority merely by being easier to read.

Descend when:

- an omitted caveat could change a decision;
- a claim is load-bearing;
- two summaries appear inconsistent;
- exact terminology/source scope matters;
- a counterexample or falsifier must be checked.

Do not descend merely to increase source count when the higher layer already answers the bounded question safely.

## Topic routing

| Topic | Deeper read first | Challenge / evidence recovery |
|---|---|---|
| Overall Records result | `synthesis/RECORDS-VERTICAL-SYNTHESIS.md` | `synthesis/VERTICAL-COMPLETENESS-COUNTERCHECK.md`, relevant source ledgers |
| Why the vertical stopped | `synthesis/VERTICAL-COMPLETENESS-COUNTERCHECK.md` | `sources/vertical-completeness-omission-review.md`, `VERTICAL-COMPLETENESS-PLAN.md` |
| What is a record / object boundaries | `synthesis/OBJECT-BOUNDARIES.md` | `synthesis/ARTIFACT-COUNTERCHECK.md`, `sources/object-boundaries-recordhood.md`, `sources/term-boundaries.md` |
| `Artifact` verdict | `synthesis/ARTIFACT-COUNTERCHECK.md` | `sources/artifact-counterframe.md`, `sources/term-boundaries.md` |
| What must persist / preservation closure | `synthesis/MINIMUM-ENVELOPE.md` | `synthesis/MINIMUM-ENVELOPE-COUNTERCHECK.md`, `sources/minimum-envelope.md` |
| Change / status / time | `synthesis/CHANGE-STATUS-TEMPORAL-SEMANTICS.md` | `synthesis/CHANGE-STATUS-TEMPORAL-COUNTERCHECK.md`, `sources/change-status-temporal-semantics.md` |
| Organisation / derived views / retrieval | `synthesis/ORGANISATION-RETRIEVAL-SEMANTICS.md` | `synthesis/ORGANISATION-RETRIEVAL-COUNTERCHECK.md`, `sources/organisation-retrieval-semantics.md` |
| Requirement/profile derivation | `synthesis/REQUIREMENT-PROFILE-DERIVATION.md` | `synthesis/REQUIREMENT-PROFILE-COUNTERCHECK.md`, `sources/requirement-profile-derivation.md` |
| Storage/history/search mechanism patterns | `synthesis/MECHANISM-PATTERN-LANDSCAPE.md` | `synthesis/MECHANISM-PATTERN-COUNTERCHECK.md`, `sources/mechanism-pattern-landscape.md` |
| Retention / appraisal / disposition | `synthesis/RETENTION-DISPOSITION-SEMANTICS.md` | `synthesis/RETENTION-DISPOSITION-COUNTERCHECK.md`, `sources/retention-disposition.md` |
| Failure modes | `synthesis/FAILURE-MODES.md` | relevant topic synthesis and source ledger |
| Remaining unresolved issues | `OPEN-QUESTIONS.md` | `STATE.md`, relevant topic synthesis |
| Deliberately deferred relations | `DEFERRED-RELATIONS.md` | relevant Records synthesis only; do not resolve adjacent domains here |

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

- `KEY.md` and `FINDINGS-MAP.md` are access surfaces, not new evidence or competing canonical syntheses.
- The consolidated synthesis is **sufficient for current foundation purpose**, not final ontology.
- `OPEN-QUESTIONS.md` records bounded residual uncertainty and reopen triggers; it is not an automatic execution queue.
- The package name `records-artifacts/` remains historical/provisional.