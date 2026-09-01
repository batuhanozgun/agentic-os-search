# Actors — Current Surfaces / Freshness Manifest

**Status:** canonical freshness/version binding for the bounded Actors handoff  
**Bound:** 2026-09-01  
**Branch:** `main`

## Purpose

This file prevents a direct search result, historical framing note or stale summary from being mistaken for the preferred current Actors conclusion.

For a decision-critical read:

1. start from the preferred current surfaces below;
2. if a listed path's current Git blob SHA differs from this manifest, treat the manifest as stale and re-evaluate the affected retrieval chain;
3. when any listed current surface changes materially, update this manifest after the change;
4. historical/audit files may remain useful but must not silently override current conclusion surfaces.

`CURRENT-SURFACES.md` does not hash itself; its Git history is the audit trail for changes to the manifest.

## Preferred current conclusion surfaces

| Layer / role | Path | Bound Git blob SHA |
|---|---|---|
| L0 shortest orientation | `KEY.md` | `7a7c38eda18a30664eec6fc0ad8bdf3484be5bee` |
| L1 topic router | `FINDINGS-MAP.md` | `20d83aac6a415ce6e84f35bf3a265c1d49945b84` |
| Vertical router | `INDEX.md` | `140bfc359aa8a0538789d9bfc769d22ef0821a3c` |
| Current vertical state | `STATE.md` | `693b3f1fee773fd1890b41d77e9a8662b1777cf9` |
| Vertical overview | `README.md` | `d89d862f223fffc65621d47b9f32cb96634ae253` |
| L2 consolidated synthesis | `synthesis/ACTORS-VERTICAL-SYNTHESIS.md` | `5ae5260cc5fc7ae8f5e7cc0171e3a1b887901224` |
| L3 identity/role/participation | `findings/IDENTITY-ROLE-PARTICIPATION.md` | `0b3e47ca2a9b0db2798b604e905629acc7b8263d` |
| L3 capability/authority/obligation | `findings/CAPABILITY-AUTHORITY-OBLIGATION.md` | `c1e2edfa445de1e31922db41e06dc0a0d16b1945` |
| L3 representation/delegation/attribution | `findings/REPRESENTATION-DELEGATION-ATTRIBUTION.md` | `84fe0768bf48c89ad751d987c23050daf230c36d` |
| L3 action/omission/decision | `findings/ACTION-OMISSION-DECISION.md` | `35ee0ca499f5642eed31799df157c4f69890f5a9` |
| L3 responsibility/accountability | `findings/RESPONSIBILITY-ACCOUNTABILITY.md` | `08b984083cd75bcb6ca4f4bcdd57e6e8d9f4deb0` |
| L3 shared/collective/institutional agency | `findings/COLLECTIVE-INSTITUTIONAL-AGENCY.md` | `d576b282ed3e20dbdbc1ff0b817b0725ccb38a4a` |
| L3 non-human/distributed agency | `findings/NONHUMAN-DISTRIBUTED-AGENCY.md` | `258b74669aa400db8169359a7f31d439eb8479a1` |
| Actors-local residuals | `OPEN-QUESTIONS.md` | `90eee421805f7b4259526d26e6ff883d7bf2fa47` |
| Cross-vertical deferrals | `DEFERRED-RELATIONS.md` | `06a7a1abb867fdc732e7cf6dca7b03ca2e55c966` |
| L4B source / inspected-view ledger | `evidence/SOURCE-LEDGER.md` | `75ed65c5e87851a868d163298427e4dde504a3ad` |

## Audit / completion surfaces

These are current audit evidence but are **not** the preferred statement of the Actors result.

| Role | Path | Bound Git blob SHA |
|---|---|---|
| Same-model adversarial completion check | `synthesis/COMPLETENESS-OMISSION-CHECK.md` | `1bf9e58d58be3cce18913803e185dd101cf85cf9` |
| Framing/research-history audit | `FRAME-EVOLUTION.md` | `ed5f51d8086c558ce00af7180bc82c2bbfdd2067` |
| Initial orientation / hypotheses | `ORIENTATION.md` | `64d1d8c8a520b39b3b7526ccc70ee1738e852ad5` |

Reading rule:
- `ORIENTATION.md` answers **what was initially hypothesized**, not what the research currently concludes.
- `FRAME-EVOLUTION.md` answers **how the framing changed**.
- `COMPLETENESS-OMISSION-CHECK.md` answers **how the result was adversarially challenged and why research stopped**; it is not independent verification.

## Parent routing surfaces bound at handoff

| Role | Path from `research/soul-foundations/` | Bound Git blob SHA |
|---|---|---|
| Parent state | `STATE.md` | `a7f0fe3616eb4d3076f167ee33ea06e8d22a5d7d` |
| Parent retrieval router | `INDEX.md` | `18dbe83ff6b7b27f551bd79c64d38d4c2eb1ea2e` |

If parent state or routing changes because the user evaluates Actors or authorizes a later phase, that does not by itself invalidate Actors substantive findings. It does mean this handoff binding is historically dated and should be refreshed if this file is still being used as the current routing manifest.

## Retrieval depth

`L0 KEY → L1 FINDINGS-MAP → L2 SYNTHESIS → L3 TOPIC FINDING → L4A COMPLETENESS/AUDIT or L4B SOURCE LEDGER → L5 PRIMARY/AUTHORITATIVE SOURCE`

## Update rule

A material edit to any preferred current conclusion surface must be followed by:

1. re-fetching the edited path from `main`;
2. replacing its bound blob SHA here;
3. checking `KEY.md`, `FINDINGS-MAP.md`, `INDEX.md` and `STATE.md` for routing/status drift;
4. if a load-bearing conclusion changed, checking the synthesis, relevant topic finding and source ledger together;
5. if the change affects bounded-completion status, re-running the completion judgment rather than leaving an old PASS in place.
