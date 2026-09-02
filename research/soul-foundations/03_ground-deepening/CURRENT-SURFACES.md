# Ground Deepening — CURRENT SURFACES

**Status:** canonical freshness binding for the current planning package  
**Date:** 2026-09-02  
**Branch:** `main`

## Purpose

Bind the current planning surfaces so a later fresh session does not mistake an intermediate plan or an unapproved substantive ground package for current authority.

Parent project authorization remains in `../STATE.md` and `../INDEX.md`.

## Bound surfaces

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Stable purpose | `README.md` | `ac086373147a2e0b80846dd276f4e8393ab2d692` |
| Planning state | `STATE.md` | `7cbcd782e6cfbd31b5bc1f843b8ac7c0cb3e5799` |
| Research plan | `PLAN.md` | `efde93494ad600af3f4c930691965bfeea444615` |
| Router | `INDEX.md` | `558a744a5f22885a9b9f77f2a6fc5edddadc127d` |

## Current rule

Preferred route:

`STATE → PLAN → INDEX → README as needed`

Current status is **PLAN READY / AWAITING USER EVALUATION**.

No substantive ground package under `grounds/` exists or is authorised yet.

## Update rule

If any bound surface changes materially:
1. re-fetch the path;
2. update its SHA here;
3. recheck parent `STATE.md` and `INDEX.md`;
4. do not let a plan update silently authorize substantive research.
