# Transition / Effect / Feedback — CURRENT SURFACES

**Status:** canonical freshness binding after accepted Actual Causal Contribution bounded leaf checkpoint  
**Date:** 2026-09-06  
**Branch:** `main`

## Current parent / routing surfaces

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Parent state | `STATE.md` | `2b8558a31b41162369c29498d76ed0830c919ed5` |
| Parent router | `INDEX.md` | `c5e30c8fb491a6420cbf9a89694b691df0d9ca58` |
| Parent plan | `PLAN.md` | `b8a94e61fad5a98df5c2a8ed7cf7656b6d019362` |
| Parent L0 key | `KEY.md` | `4c497dd0fb66756f67fd65b5a2d153c81c3352de` |
| Parent findings map | `FINDINGS-MAP.md` | `c4c2ce07e104874fc5c977869907c967a0751a7a` |
| Parent synthesis | `synthesis/TRANSITION-EFFECT-FEEDBACK-SYNTHESIS.md` | `104d182c83f51a75035269d8aeb4f2fe319c8085` |
| Parent residuals | `OPEN-QUESTIONS.md` | `d1b9c00cf18a684981553ec8ea5d2a1cff209b91` |

## Current child surfaces

| Child | Status | Current manifest |
|---|---|---|
| Cross-Ground Transition / Propagation | accepted bounded leaf | `transition-propagation/CURRENT-SURFACES.md` @ `bf27c8c5b630995af0f83f11702f6f1e9b3eb26d` |
| Cross-Ground Causal Effect / Contribution | accepted bounded parent | `causal-effect-contribution/CURRENT-SURFACES.md` @ `2fd621e67e6cdc66940591279437fd7c9aca4b54` |
| Cross-Ground Feedback / Adaptation | inactive | not created/active |

## Causal frontier

```text
Cross-Ground Causal Effect / Contribution        ← ACCEPTED PARENT
├─ Actual Causal Contribution / Episode Causation       ← ACCEPTED BOUNDED LEAF
└─ Contrastive / Interventional Causal Effect            ← recommended next / inactive
```

Actual child manifest:

`causal-effect-contribution/actual-causal-contribution/CURRENT-SURFACES.md` @ `fbc0a842a4e4f1b95443470a1f0d3050c6a547b4`

## Current bounded result

```text
Transition / Effect / Feedback                         ← ACCEPTED PARENT
├─ Cross-Ground Transition / Propagation               ← ACCEPTED BOUNDED LEAF
├─ Cross-Ground Causal Effect / Contribution           ← ACCEPTED BOUNDED PARENT
│  ├─ Actual Causal Contribution / Episode Causation       ← ACCEPTED BOUNDED LEAF
│  └─ Contrastive / Interventional Causal Effect            ← recommended next / inactive
└─ Cross-Ground Feedback / Adaptation                  ← inactive

substantive Transition-parent child                    ← NONE
```

## Verification note

Exact SHA binding establishes repository-view identity/freshness only.

Transition T7, Propagation P7, Causal E7 and Actual A7 are same-model adversarial reviews. No independent second-researcher/model replication validates the exact current decomposition.
