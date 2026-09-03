# Domain State — CURRENT SURFACES

**Status:** canonical freshness binding after Domain Structure selection/planning; substantive Structure research not active  
**Date:** 2026-09-03  
**Branch:** `main`

## Entry surfaces

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Node state | `STATE.md` | `9c72eb836c164d574fe36deeff1dbc8b0127993f` |
| Router | `INDEX.md` | `887019991d82bc7bb1f44504575fa01dbc93ed7b` |
| L0 key | `KEY.md` | `1c7ea731c2629a132d06a43ef3d9f9d90825c02e` |
| Selected next-node plan | `DOMAIN-STRUCTURE-RESEARCH-PLAN.md` | `fc402ad7dd0259cec4a831586766e0c1a1cfdad4` |
| L1 findings map | `FINDINGS-MAP.md` | `29d01710810399ce81b79051b1fb0840da13acf4` |
| Executed Domain State research plan | `../DOMAIN-STATE-RESEARCH-PLAN.md` | `8f5cabdd360fee61cd31a230018591673c348f24` |
| Residual questions | `OPEN-QUESTIONS.md` | `554a54fb344348b1bfb32502cd165f754c14235f` |
| Deferred relations | `DEFERRED-RELATIONS.md` | `6b331ef678a46fb9aaeb20a0d9cab68073d4143e` |

## Focused findings

| Finding | Bound Git blob SHA |
|---|---|
| `findings/01-evidence-inventory-and-starting-falsifiers.md` | `bc64abf902c7aa6853e8cacae60897e672a04386` |
| `findings/02-node-coherence-and-rename.md` | `6b765454a53bfb19f5d805e37f520b275b3d0b7d` |
| `findings/03-structure-composition-child.md` | `6d0c29848b86b3d31ecdf65b02a241d96ca911ad` |
| `findings/04-condition-status-child.md` | `faddd2e642d92f980d92792c75d25c8e85826b27` |
| `findings/05-identity-constraints-granularity-crosscut.md` | `22bbfeaab395ff4b14d013de66ccd48a7334e75e` |
| `findings/06-actual-vs-represented-state-boundary.md` | `196c6499091fe26117f51df873434f876e3b7dd5` |
| `findings/07-cross-domain-holdouts.md` | `5f074cbb4cd62c6ea7a52eec4c176d571c8f6dca` |
| `findings/08-rival-decomposition-and-child-result.md` | `19c2c214cd52414f190d4ce90eb80eff8b4ae1aa` |
| `findings/09-domain-state-problem-map.md` | `26c347258cd6320dcfeeeddd93be485dea439c4c` |

Findings tree: `d9d749dcc6d641abae5709ffd740aff5dbc16f83`.

## Synthesis / audit / evidence

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Integrated synthesis | `synthesis/DOMAIN-STATE-SYNTHESIS.md` | `2fb261ec3a4522f8482421674d4c12e9c584eb9b` |
| Completion / omission audit | `synthesis/COMPLETENESS-OMISSION-CHECK.md` | `4564baf491b6f2b6a7465d26b19fc80ad1769348` |
| Preserved source/view ledger with exact pre-pass parent snapshot | `evidence/SOURCE-LEDGER.md` | `352c75725f8e19fc751cc60ba07cd37a0891e2b6` |

Synthesis tree: `cae93528289779a262315f16141703d257407f57`  
Evidence tree: `d30a87b120945f2d1746b66c4f1c4c9ae954d4bd`

The source ledger preserves the historical Domain State pass input separately from later sequencing changes.

## Current bounded result / selected sequence

```text
Domain State
    ├─ Domain Structure / Composition   ← selected/planned next; research not active
    └─ Domain Condition / Status        ← discovered; intended after Structure evaluation
```

Agreed continuation:

```text
Structure research → user evaluation
→ Condition research → user evaluation
→ Environment completion review
→ then decide whether Information should begin
```

The Condition plan is intentionally deferred until after Structure research/evaluation so that it can use the then-current canonical state rather than premature assumptions.

## Authorization rule

Current authorized work is **Domain Structure selection/planning only**. Planning is complete. No substantive node is active.

A later explicit transition is required before Structure research begins.

## Retrieval rule

For current sequencing/authorization:
`STATE → DOMAIN-STRUCTURE-RESEARCH-PLAN → KEY`

For established Domain State evidence:
`KEY/FINDINGS-MAP → DOMAIN-STATE-SYNTHESIS → focused finding → audit/source ledger → primary source`

## Update rule

If Structure research is activated, first bind the exact pre-pass Domain State snapshot and create/update the Structure research package/state as required by the hierarchical method. Then refresh Domain Reality → Environment → stage/root surfaces bottom-up.