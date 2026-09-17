# Superpowers — Source Ledger and Progressive Topology

Observation date: 2026-09-17. This ledger records **observed coverage**, not promised future coverage. All upstream file references below are bound to `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` unless explicitly stated otherwise. U01-B extends the original ledger without resetting first-round full reads or experiment results.

## Snapshot binding

- Repository: https://github.com/obra/superpowers
- `refs/heads/main` resolved in the first round through connected GitHub to `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`.
- Git commit metadata: timestamp `2026-08-12T16:53:21Z`; root tree `21219529a4e224bcb27baf8816b039c8bf7c6673`.
- The commit message was truncated in the tool view. Only its metadata is used; its long change narrative is not treated as fully read evidence.
- `.codex-plugin/plugin.json` declares version `6.3.0`. U01-B additionally read matching version declarations in root package, Gemini, Cursor, Kimi and Hermes manifests. No installed-version/release-channel equivalence is claimed.
- U01-B continued at the existing pin. No new upstream HEAD/release freshness verdict was produced.

## Upstream source register — first round, retained

Base for paths: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/

| ID | Source | Git identity | Coverage and role |
|---|---|---|---|
| S00 | Git ref and commit metadata | commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` | Metadata observed; long commit message PARTIAL, not detailed-behavior evidence. |
| S01 | `README.md` | `09a91c6d03cfa3d874c5c33b6f8cc3d0b2d89645` | FULL earlier in this conversation; rebound through pinned root tree. Product orientation/author claims, not efficacy. |
| S02 | Root tree | tree `21219529a4e224bcb27baf8816b039c8bf7c6673` | FULL non-recursive tree; first JSON copy complete with truncated:false despite truncated repeated wrapper copy. Not full repository content. |
| S03 | Skills tree | tree `9483dd00b0bda60c6ea631d88900f0436630d064` | FULL non-recursive listing; 14 skill directories. Presence is not full skill reading. |
| S04 | `skills/using-superpowers/SKILL.md` | `7ab2eb678f649c8befb94512359ee0b6e9a9a9a4` | FULL; selection, subagent exception, user precedence, platform-reference routes. |
| S05 | `hooks/hooks.json` | `67975137aafc8a097bdd1c2b51fea3989b8ad6c0` | FULL; declared SessionStart matcher/wrapper. No actual host startup observed. |
| S06 | `hooks/session-start` | `93a6bc2c6b7269c704378cb6a61fce6aea7ff631` | FULL; exact local copy executed in U01-A synthetic fixtures. No rerun in U01-B. |
| S07 | `.codex-plugin/plugin.json` | `123793e54ffbd933e9a3e6f99e133e8087a08828` | FULL; skills path, empty hooks object/version. Manifest observation, not live Codex. |
| S08 | `docs/porting-to-a-new-harness.md` | `4ae9603defaf0d9ff052189a33fe515dd2a4ee2e` | NOW FULL across this conversation: initial 1–310, then U01-B 311–460, 461–610, 611–800, 801–EOF. Prior PARTIAL status superseded only for this file. |
| S09 | `tests/hooks/test-session-start.sh` | `c1508290e9813de1a7d20b24d3ca3c8927fbc11c` | FULL SOURCE ONLY; registration/output/warning checks. Upstream suite not run. |
| S10 | `skills/brainstorming/SKILL.md` | `b56a3b5ed6ea0d6216501e0e401ecb00a1b4675f` | FULL in initial requests 1–150 and 151–EOF. Three-path routing/approval/spec/companion reference. Planning/worktree/companion dependencies still open. |

An initial public web view was used only for orientation, not as substitute for pinned sources. U01-B public web opens failed; the connected GitHub reads below succeeded and supply the evidence. No unavailable web result is cited as confirmation.

## Upstream source register — U01-B additions

All 17 file bodies below were **FULLY READ through GitHub at the same pin**. Only S12 was executed locally; other executable files/test files remain source observations.

| ID | Source | Blob SHA | Role / execution boundary |
|---|---|---|---|
| S11 | `hooks/run-hook.cmd` | `ceec3a732d6251abb3c65ba860b7cc5d1f21dfb8` | Polyglot wrapper; Windows Bash search/no-Bash success path, Unix dispatch. Not run. |
| S12 | `.opencode/plugins/superpowers.js` | `423e5ed513261485c657ba166b0372a5293639c7` | Config registration, first-user transform, generic-marker dedup, module cache. Exact-byte local callback execution E03/E04. |
| S13 | `.pi/extensions/superpowers.ts` | `a978e80ee0bbffe649ace8826bf6e8b69beea421` | Discovery, lifecycle flag, message insertion/dedup, inline mapping/cache. Not run. |
| S14 | `package.json` | `3a84ce88c91344a7931d3f1d156d2ade317d6577` | ESM/OpenCode entry; Pi extension and skill resource declarations. |
| S15 | `gemini-extension.json` | `ccb77ae2169968e60f49914f97aa1a25ffe98e18` | Declared extension context file. |
| S16 | `GEMINI.md` | `0dd2f585ecb2ee37c558c8233d72489bb2135856` | Two relative includes. Real host expansion not observed. |
| S17 | `skills/using-superpowers/references/gemini-tools.md` | `b01b65238a50981aeed22ae52ee20f8b55d16b42` | Target's tool/agent/template instructions, not verified current Gemini API. |
| S18 | `skills/using-superpowers/references/codex-tools.md` | `e4488fb224bb0fa0a33e9ac7dc961174e9f0c150` | Target's version-sensitive delegation/context/worktree instructions; actual current Codex contracts not revalidated. |
| S19 | `skills/using-superpowers/references/pi-tools.md` | `0c1f21713a45255ece4144fd2fee353e4ed4f90e` | Optional subagent/task-tool fallbacks. Not an identical copy of all S13 inline mapping. |
| S20 | `.hermes-plugin/__init__.py` | `3b41644bb2890fbd3b642b63ed6625da0077e935` | Two layout resolution, bootstrap build, skill registration, first-turn hook. Not run. |
| S21 | `.hermes-plugin/plugin.yaml` | `3a0ecfb21e6061c1560b8477f1e2f2b4e6cd1f58` | Declares pre_llm_call hook capability. |
| S22 | `skills/using-superpowers/references/hermes-tools.md` | `0f1fa57bc1b495462e75c6ce11e798245a34987e` | Skill names/path fallbacks/delegation mapping; namespace seam with S20 preserved. |
| S23 | `.kimi-plugin/plugin.json` | `dcb9a7a9bee9ee8acfc73d535060569de0cdc8e6` | sessionStart.skill, skills path, inline interaction/task/role mapping. Host not run. |
| S24 | `hooks/hooks-cursor.json` | `84e6d33874ab5926035e35bc13dccf21244bb079` | Lowercase event, relative command; no explicit compaction entry in this file. |
| S25 | `.cursor-plugin/plugin.json` | `bb2bdbcd1ab620883d1a4865ae03f021064ff13c` | Skills/hooks declarations. |
| S26 | `tests/opencode/test-bootstrap-caching.mjs` | `32149aed33037d7bcda36dc875546d390b501c78` | FULL SOURCE ONLY; present/missing cache assertions, mapping strings, generic-marker counting. Not run. |
| S27 | `tests/pi/test-pi-extension.mjs` | `d7af9cb2ae125341eaab1e53bea8d2a2d7448dda` | FULL SOURCE ONLY; fake-event actual-extension tests and table-text check. Not run. |

Additional FULL non-recursive navigation trees:

- `.hermes-plugin`: `24ce40750b8c305dac592ed04462861d102a2fb2` — two files, both read.
- `tests`: `3b4b2210556b6c3f668aca2c6c34dffb114c7293` — test-family presence only.
- `tests/opencode`: `60f3f9394823bc86c768e3b9974e49fa18968f9d` — seven entries; only S26's content read.

## Progressive native source topology

This is not a complete recursive inventory or final subsystem taxonomy.

| Family | Observed role | Current coverage limit |
|---|---|---|
| Shared skills | 14 native skill directories | Only using-superpowers and brainstorming SKILL bodies fully read so far. |
| Host integration | Shell, native-description, manifest-sessionStart, includes, in-process callback paths | Selected material families covered in U01-B matrix. Not every supported host/version or distribution path. Devin and remaining installations deferred to U07. |
| Bootstrap/hooks | Selected shell registration/output/wrapper plus Cursor config | S06 local U01-A probes retained; wrapper source-only; event consumption not established. |
| In-process entry | OpenCode, Pi, Hermes | All three adapter bodies fully read; only OpenCode module callbacks locally exercised. No actual host run. |
| Supporting runtime/distribution | scripts, assets, root package, host dotdirs | Root package full; runtime/helper/packaging internals mostly open. Guide-to-Antigravity path mismatch is U07 residual. |
| Tests/evaluation/history | tests, .github, pre-commit/version manifests, release history | Three test bodies fully read across rounds, none of those upstream suites run. Two separate study-written local experiments exist. CI/effectiveness open. |
| Contributor/orientation | README, CLAUDE, AGENTS, LICENSE and auxiliary files | README full; remaining contributor/license bodies not yet investigated. Root AGENTS symlink noted only. |
| Documentation | Porting and other docs/history | Porting guide now full. Other documentation not recursively inventoried. |

Skill catalogue retained: brainstorming; dispatching-parallel-agents; executing-plans; finishing-a-development-branch; receiving-code-review; requesting-code-review; subagent-driven-development; systematic-debugging; test-driven-development; using-git-worktrees; using-superpowers; verification-before-completion; writing-plans; writing-skills.

## Method and project-context inputs

- `gstack/METHOD.md`, FULL initial round, blob `dc003b3f74115667a05787a847eadb10876784c8`: source-first synthesis precedent, not imported architecture.
- `gstack/META.md`, FULL initial round, blob `f2ad498742f026aa84578e82ec7fd0cf6843da65`: historical scope/no-adoption boundary; no current runtime comparison.
- Initial `research/INDEX.md`, `studies/INDEX.md`, `studies/PACKAGE-CONTRACT.md`, `studies/CATALOG.md`: full placement/continuity recovery.
- U01-B re-read package STATE, META, METHOD, PLAN, SOURCE-LEDGER and U01 note fully, then current library CATALOG before updating its row. Unrelated ECC/DeepSeek entries present in current catalog must be preserved.
- Agent-control files are not part of the substantive research corpus.

## Local experiment evidence

### E01/E02 — retained U01-A, not rerun here

- Runner: [evidence/U01-hook-probes.py](evidence/U01-hook-probes.py).
- Output: [evidence/U01-hook-probes-results.json](evidence/U01-hook-probes-results.json).
- S06 exact blob `93a6bc2c6b7269c704378cb6a61fce6aea7ff631`, 2,274 bytes, verified before first-round execution.
- Linux, Python 3.13.5, GNU Bash 5.2.37. Temporary synthetic filesystem; no host, credentials, installation or external APIs.
- Four transport cases passed; two study-defined bootstrap-health challenges failed; one wrong-event negative control rejected correctly. Interpretation remains in the original U01 note.

### E03/E04 — actual U01-B execution

- Runner: [evidence/U01B-opencode-probes.mjs](evidence/U01B-opencode-probes.mjs).
- Output: [evidence/U01B-opencode-probes-results.json](evidence/U01B-opencode-probes-results.json).
- S12 exact module blob `423e5ed513261485c657ba166b0372a5293639c7`, 5,464 bytes, transferred through connector output and hash-verified before execution.
- Linux x64, Node v22.16.0; built-in modules only, temporary ESM package/skill fixtures; exported factory and callbacks manually invoked. No install, network, real host/model or upstream suite.
- Eight mechanism checks passed; two study-defined semantic-health challenges failed (marker collision and empty-body already-loaded claim); one marker-only oracle control passed.
- Separate V1/V2 and missing/repaired controls distinguish file revision, cached module and fresh module identity. A new ES module is not claimed equivalent to a real host's new session.
- Local runner Git blob: `6a99be598bac4d60943c816857124c907882c089`; local output Git blob: `fae46fb808c5814fc7039f874f7d9aae5e5b34f3`. Compare published blobs during readback; identities establish transfer fidelity, not interpretive independence.
- All experiments are source-informed exploratory probes; mechanism PASS is not product qualification. Full interpretation and criteria are in [U01-B note](notes/U01B-host-delivery-and-continuity.md).

## Acquisition and negative-evidence limits

The first-round archive attempt failed at DNS resolution. A U01-B raw-source connectivity attempt likewise failed DNS; public web views were unavailable. Connected GitHub source reads and writes worked. No full clone/archive was obtained; locally transferred scripts/modules do not imply full repository availability.

No real Claude/Codex/Cursor/Gemini/Kimi/Hermes/Pi/OpenCode session, Windows wrapper, model/credentialed call, upstream test suite or CI verdict was produced. No production incident, general reliability ranking, development-quality benchmark or host namespace/API qualification is claimed.

Absence from this progressive map is not repository-wide absence. A source-level unit can close with explicit host/effectiveness boundaries; the whole study cannot close while load-bearing work/verification/lifecycle families remain uninvestigated.
