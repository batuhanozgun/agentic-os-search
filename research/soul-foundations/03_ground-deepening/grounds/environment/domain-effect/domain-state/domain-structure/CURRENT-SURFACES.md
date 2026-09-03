# Domain Structure — CURRENT SURFACES

**Status:** canonical freshness binding after bounded Structure closure and user acceptance  
**Date:** 2026-09-03  
**Branch:** `main`

## Entry surfaces

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Node state | `STATE.md` | `a69e73f90e2714ab8945529d309db99fedfda6be` |
| Router | `INDEX.md` | `4e6d11e895b459392c60f9346d6f7682b33d4603` |
| L0 key | `KEY.md` | `9815af79146027447a02b4e654b8797edc6bf424` |
| L1 findings map | `FINDINGS-MAP.md` | `3906538681a8a6ee28a7f5771860e6fe13f2a1fc` |
| Residual questions | `OPEN-QUESTIONS.md` | `a7a94666fac213c5fecc55086afaa14affd93d19` |
| Deferred relations | `DEFERRED-RELATIONS.md` | `248c52cc19f6145d15b6cab48dbdb6795a77d23f` |

## Focused findings

| Finding | Bound Git blob SHA |
|---|---|
| `findings/01-node-coherence-and-label.md` | `95404a30f99f5a3fd20d7c85cc91ae552ed879a0` |
| `findings/02-composition-membership-child.md` | `27842a0cc64b242c2ca4b5d2b00227b757c22a4e` |
| `findings/03-relational-organization-topology-child.md` | `7b2bab1e5e2e80865067393b91f8e739419143ce` |
| `findings/04-third-child-and-crosscut-audit.md` | `4ddcc6b5bc2ea7cbf055fb8907a71b2ff42e21e6` |
| `findings/05-cross-domain-holdouts.md` | `ddd812fe4810812585cca1c4aa1b7ecdaa4ba236` |
| `findings/06-boundary-and-anti-collapse.md` | `ad35d1c6d7bb99ec67f3b98ca0462a7cc66a8cc6` |

Findings tree: `038e39a0033ede87a34dd09b56cdb210f2fa7dc4`.

## Synthesis / audit / evidence

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Integrated synthesis | `synthesis/DOMAIN-STRUCTURE-SYNTHESIS.md` | `a222a028119edbd9c90b18a6449ba2929c526596` |
| Completion / omission audit | `synthesis/COMPLETENESS-OMISSION-CHECK.md` | `0105b90ccd7290c4398eb44c02b699df1483e27f` |
| Source / view ledger | `evidence/SOURCE-LEDGER.md` | `375b79264e9ce81297fd35630c9bae97c48e7234` |

Synthesis tree: `917e03cb418a4aed3cb42daa057ff0f6c421b700`  
Evidence tree: `778d3092c31159eeb1e856c82883695a9b8e7406`

## Exact pre-pass parent binding

This Structure pass was entered from the Domain State snapshot bound by:

- parent `../STATE.md`: `9c72eb836c164d574fe36deeff1dbc8b0127993f`
- parent `../CURRENT-SURFACES.md`: `c4f190f9d11dfa97ab94e2ed351f1c74b64e2b2c`
- parent `../KEY.md`: `1c7ea731c2629a132d06a43ef3d9f9d90825c02e`
- frozen plan `../DOMAIN-STRUCTURE-RESEARCH-PLAN.md`: `fc402ad7dd0259cec4a831586766e0c1a1cfdad4`

Those SHAs are historical pass-input bindings; parent current surfaces may now be refreshed to reflect this child result and evaluation state.

## Current bounded result

```text
Domain Structure
    ├─ Constituent Composition / Membership   ← discovered; inactive
    └─ Relational Organization / Topology     ← discovered; inactive
```

`Domain Structure / Composition` was refined to `Domain Structure`. The bounded result was user-evaluated and accepted on 2026-09-03. No discovered child is substantively active.

## Verification rule

The completion audit is same-model adversarial self-review, not independent verification. External sources discriminate/falsify rivals but do not independently validate this exact hierarchy. User acceptance does not alter that verification status.

## Authorization rule

No substantive work is currently authorized. The next logical step is `Domain Condition / Status` planning, which requires explicit user authorization.

Do not activate either Structure child, Domain Condition / Status, Information, Work, Actors, systematic relation/control composition, architecture, ontology/data-model work or implementation without later explicit authorization.

## Retrieval rule

For current Structure status/result:
`STATE → KEY → FINDINGS-MAP → synthesis → focused finding/audit/source ledger`.

For the historical input to the pass, use the pre-pass parent blobs above rather than current parent files after continuity refresh.
