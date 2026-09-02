# Ground Deepening — CURRENT SURFACES

**Status:** canonical freshness binding for the user-accepted ground-deepening program  
**Date:** 2026-09-02  
**Branch:** `main`

## Purpose

Bind the current program surfaces so a later fresh session does not mistake an intermediate plan, pre-acceptance state, or an unapproved substantive ground package for current authority.

Parent project authorization remains in `../STATE.md` and `../INDEX.md`.

## Bound surfaces

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Stable purpose | `README.md` | `ac086373147a2e0b80846dd276f4e8393ab2d692` |
| Program state / one-active-ground rule | `STATE.md` | `1abd8016a2aab793cf038946307219c87fb69cc7` |
| User-accepted research plan | `PLAN.md` | `dfe00d2ca4d43758c476f640332751c3af013725` |
| Router | `INDEX.md` | `83d1648a42ae5ff542e45d3106a1a28a0753a8a8` |

## Current rule

Preferred route:

`STATE → PLAN → INDEX → README as needed`

Current status is **PLAN USER-ACCEPTED; NO SUBSTANTIVE GROUND PASS ACTIVE**.

At most one ground may be active at a time. No package under `grounds/` exists or is authorised yet.

## Update rule

If any bound surface changes materially:
1. re-fetch the path;
2. update its SHA here;
3. recheck parent `STATE.md` and `INDEX.md`;
4. do not let a plan/program update silently authorize substantive research or a second simultaneous ground.
