# Work — Current Revision Binding

**Document role:** CURRENT_REVISION_MANIFEST  
**Revision:** `work-foundation-2026-09-01-r1`  
**Purpose:** bind the preferred current Work reading surfaces to exact repository blobs so progressive derived views cannot silently drift apart.

## Revision rule

This revision is current only while the listed current-surface blobs match these SHA values.

If a preferred current substantive/routing surface changes materially:

1. update all affected derived/routing surfaces;
2. re-run a bounded cold-read/currentness check from L0 downward;
3. update this exact-blob binding;
4. change the revision identifier when the meaning or retrieval contract materially changes.

Historical orientation is not required to share the current revision identifier; its role is classified in `DOCUMENT-STATUS.md`.

## Status / routing surfaces

| File | Blob SHA |
|---|---|
| `README.md` | `b1077da2146ca1104e6ccd4cb85f046fd6823cec` |
| `STATE.md` | `4bee6d5a362f12189df77948ef247bbb86eddcf2` |
| `INDEX.md` | `10a2a50509bca725c137b0348217754144b48447` |
| `DOCUMENT-STATUS.md` | `6818f6909d3c5f1e0e4a7f88f0fc3bbc3a6ba275` |

## L0 / L1 / L2

| Layer | File | Blob SHA |
|---|---|---|
| L0 | `KEY.md` | `89b26785d4828605bc61ac1f6a5d16c45abddef2` |
| L1 | `FINDINGS-MAP.md` | `624e53ad4f6dc3cc6806898bf95f023d616b0999` |
| L2 | `synthesis/WORK-VERTICAL-SYNTHESIS.md` | `58fb887139fa84adf6eb522569c593e320b51684` |

## L3 — current topic findings

| Topic | File | Blob SHA |
|---|---|---|
| frames / units / purpose-action-method / boundedness | `findings/WORK-FRAMES-AND-UNITS.md` | `592fccfb1633c37425890a883f52cf8606258f45` |
| intake / selection / commitment / priority | `findings/INTAKE-SELECTION-COMMITMENT-AND-PRIORITY.md` | `0201c31111716b1dac2ccfb8782b1fcea0822f38` |
| situatedness / coordination / concurrency / flow | `findings/COORDINATION-FLOW-AND-SITUATEDNESS.md` | `7ae84b61d980068d8522a33bbecb59c3ac7b5ff0` |
| state / effort-time / closure / recovery | `findings/CONTROL-STATE-CLOSURE-AND-RECOVERY.md` | `8dd706301c5b4bc1bd7d6d02a7df5512e14a7e49` |

## L4 — challenge and evidence trace

| Layer | File | Blob SHA |
|---|---|---|
| L4A adversarial/completeness audit | `synthesis/COMPLETENESS-OMISSION-CHECK.md` | `b335f54caa93955c8073099babc9c331d5ebd43d` |
| L4B evidence trace | `evidence/SOURCE-LEDGER.md` | `7970f0c1e97b1544a2c1c568eb865358134bd551` |

L5 consists of the primary/authoritative sources named by the source ledger and is not blob-bound inside this repository.

## Bounded residual / deferred relation surfaces

| File | Blob SHA |
|---|---|
| `OPEN-QUESTIONS.md` | `1e14f4907c6c2c9c9b9ca17b3ae33797d907dd7a` |
| `DEFERRED-RELATIONS.md` | `28b6d8583a6425871f9503733a06a55bf4a5ceca` |

## Historical research-path surface

`orientation/RESEARCH-ORIENTATION.md` is deliberately **HISTORICAL**. It is retained to reconstruct the weak starting hypothesis and alternative-frame challenge, not bound as a preferred current conclusion.

## Interpretation

The SHA binding establishes **which derived view/version is current in this Work retrieval revision**. It does not make any derived view primary evidence or independently verified truth.

If a listed SHA no longer matches the current path, treat this manifest as stale until repaired; do not silently infer that the newer file is part of this revision.