# Domain State — CURRENT SURFACES

**Status:** canonical freshness binding for bounded Domain State immediate-child result  
**Date:** 2026-09-02  
**Branch:** `main`

## Entry surfaces

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Node state | `STATE.md` | `4e36927d905361a8808d95d9d45ef54bc29c6cfd` |
| Router | `INDEX.md` | `86d9a6ac7a7c44282566c7b480871e96a3c1a38d` |
| L0 key | `KEY.md` | `e51f022dceba988eb7d96246dc89b8f0f0c7a95c` |
| L1 findings map | `FINDINGS-MAP.md` | `e78bc58a65b0041e9af4d53ee0a4c9c12e9905e2` |
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

Findings tree: `d9d749dcc6d641abae5709ffd740aff5dbc16f83`

## Synthesis / audit / evidence

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Integrated synthesis | `synthesis/DOMAIN-STATE-SYNTHESIS.md` | `2fb261ec3a4522f8482421674d4c12e9c584eb9b` |
| Completion / omission audit | `synthesis/COMPLETENESS-OMISSION-CHECK.md` | `4564baf491b6f2b6a7465d26b19fc80ad1769348` |
| Source/view ledger | `evidence/SOURCE-LEDGER.md` | `65d300f926a5ec71194295a554fdc258d416ae01` |

Synthesis tree: `cae93528289779a262315f16141703d257407f57`  
Evidence tree: `16beb7a87b34025746993331c700b10c3761aea5`

## Current bounded result

```text
Domain State
    ├─ Domain Structure / Composition
    └─ Domain Condition / Status
```

`Domain State / Configuration` is refined to `Domain State`. Identity/Continuity, Constraints/Invariants, Granularity/State Sufficiency, actual-versus-represented State and related dimensions remain explicit cross-cutting/boundary questions rather than co-equal children at this level.

## Authorization rule

The node is closed for bounded immediate-child research and awaits user evaluation. `Domain Structure / Composition`, `Domain Condition / Status`, Domain Dynamics, Work Conditions and other grounds are inactive.

## Retrieval rule

`STATE → KEY/FINDINGS-MAP → DOMAIN-STATE-SYNTHESIS → focused finding → audit/source ledger → primary source`

## Update rule

After any material Domain State edit, re-fetch exact blobs, refresh this manifest, then refresh Domain Reality → Environment → stage manifests. Never let node closure or child discovery silently authorize next-node research.
