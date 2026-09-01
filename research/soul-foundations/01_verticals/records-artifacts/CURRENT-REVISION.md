# Records — Current Revision Binding

**Document role:** CURRENT_REVISION_MANIFEST  
**Revision:** `records-foundation-2026-09-01-r2`  
**Purpose:** bind the preferred current reading surfaces to exact repository blobs so derived views cannot silently drift apart.

## Revision rule

This revision is current only while the listed current-surface blobs match these SHA values.

If a current substantive/routing surface changes materially:

1. update all affected derived surfaces;
2. re-run the bounded cold-read/currentness check;
3. create/update the revision binding with the new exact blobs;
4. change the revision identifier when the meaning/routing contract materially changes.

Historical/audit/source files are not required to share this revision identifier; their role is classified in `DOCUMENT-STATUS.md`.

## Status / routing surfaces

| File | Blob SHA |
|---|---|
| `README.md` | `15bedacb37bdc2eda5971cf542a6a387d5ab67a9` |
| `STATE.md` | `e18d1178a4e0096a067b29033b8948645e31b3c1` |
| `INDEX.md` | `8df2cb201a35e8cea4e3f51ef0a8777bb802e40c` |
| `DOCUMENT-STATUS.md` | `8d090bf1d82cb3ed67a1ce4f8671f954f6ec9bd3` |
| `synthesis/README.md` | `8588c4a5ed2b6f06b7f18eb1c88e9cf443eed9a3` |
| `synthesis/current/README.md` | `0f54413a9282d026beb2f6d55afb25286d7807fd` |
| `sources/README.md` | `e3e79da6a8b68b137c80647aee3aa87fdffdae69` |

## L0 / L1 / L2

| Layer | File | Blob SHA |
|---|---|---|
| L0 | `KEY.md` | `9050bf3ea76e0b983a1c93f3bafa0c55f15625d6` |
| L1 | `FINDINGS-MAP.md` | `4e020b465fe97dff745ed8c10d3afac55d141124` |
| L2 | `synthesis/RECORDS-VERTICAL-SYNTHESIS.md` | `76fb18f2538aceeccf353a807a777cd1e91c9d3a` |

## L3 — current topic syntheses

| Topic | File | Blob SHA |
|---|---|---|
| object / identity | `synthesis/current/OBJECT-IDENTITY.md` | `f33f10d9d2b1d411d7d8a3e46fc2090a7ab99557` |
| preservation closure | `synthesis/current/PRESERVATION-CLOSURE.md` | `8b9625c55246549e35693eff1a774c3b3627a3f0` |
| change / time / standing | `synthesis/current/CHANGE-TIME-STANDING.md` | `986b82de6758257b0d8154dad12070dd297cc659` |
| organisation / retrieval | `synthesis/current/ORGANISATION-RETRIEVAL.md` | `ba8928f5dc871ff8fa09e43faa749070985a7c3f` |
| requirement derivation | `synthesis/current/REQUIREMENT-DERIVATION.md` | `06d75011549cf6de505ef14700e3e8335b113f87` |
| mechanism landscape | `synthesis/current/MECHANISM-LANDSCAPE.md` | `a19d616c2b9210b38f629b88e9f0bdb5be4eda8e` |
| retention / disposition | `synthesis/current/RETENTION-DISPOSITION.md` | `758b761be4243eb181b51d842d573e4ec1c475f0` |
| failure surfaces | `synthesis/current/FAILURE-SURFACES.md` | `73c9f99bfb052b87eb8b576ad8ec4a121248ff74` |
| completeness | `synthesis/current/COMPLETENESS.md` | `dae72c4783fc48f045cf465bbb3f513ce3e15a4b` |

## Bounded residual / deferred records

| File | Blob SHA |
|---|---|
| `OPEN-QUESTIONS.md` | `2634cc4639a8798f8d4f60f73aca76e5621a693d` |
| `DEFERRED-RELATIONS.md` | `caea5a5502e7ade5e1c6bc35dfecdd86e2d7cce5` |

## Interpretation

The SHA binding establishes **which derived view/version is current in this repository revision**. It does not make the view primary evidence or independently verified truth.

If a listed SHA no longer matches the current path, treat this manifest as stale until repaired; do not silently infer that the newer file is part of this revision.