# Superpowers — Source Ledger and Initial Topology

Observation date: 2026-09-17. This ledger records **observed coverage**, not promised future coverage. All upstream file references below are bound to `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` unless explicitly stated otherwise.

## Snapshot binding

- Repository: https://github.com/obra/superpowers
- `refs/heads/main` resolved through the connected GitHub API to `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`.
- Git commit metadata: timestamp `2026-08-12T16:53:21Z`; root tree `21219529a4e224bcb27baf8816b039c8bf7c6673`.
- The commit message was truncated in the tool view. Only its metadata is used here; its long change narrative is not treated as fully read evidence.
- `.codex-plugin/plugin.json` declares version `6.3.0`. No claim is made about installed versions or every release channel.

## Upstream source register

Base for file links: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/

| ID | Source | Identity | Coverage and role |
|---|---|---|---|
| S00 | Git ref and commit metadata | commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` | Metadata observed; long commit message PARTIAL, not evidence for detailed behavior. |
| S01 | [README.md](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/README.md) | blob `09a91c6d03cfa3d874c5c33b6f8cc3d0b2d89645` | FULL earlier in this conversation; identity rebound through the pinned root tree. Product orientation and author claims, not efficacy proof. |
| S02 | [Root tree](https://api.github.com/repos/obra/superpowers/git/trees/21219529a4e224bcb27baf8816b039c8bf7c6673) | tree `21219529a4e224bcb27baf8816b039c8bf7c6673` | FULL non-recursive tree; first JSON copy complete with `truncated:false`, although the wrapper's repeated copy was truncated. Not full repository content. |
| S03 | [Skills tree](https://api.github.com/repos/obra/superpowers/git/trees/9483dd00b0bda60c6ea631d88900f0436630d064) | tree `9483dd00b0bda60c6ea631d88900f0436630d064` | FULL non-recursive listing; 14 skill directories. Directory presence is not full skill reading. |
| S04 | [skills/using-superpowers/SKILL.md](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/using-superpowers/SKILL.md) | blob `7ab2eb678f649c8befb94512359ee0b6e9a9a9a4` | FULL; skill selection, subagent exception, user-instruction precedence and platform-reference routes. |
| S05 | [hooks/hooks.json](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/hooks/hooks.json) | blob `67975137aafc8a097bdd1c2b51fea3989b8ad6c0` | FULL; declared SessionStart matcher and shell wrapper registration. No actual host startup observed. |
| S06 | [hooks/session-start](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/hooks/session-start) | blob `93a6bc2c6b7269c704378cb6a61fce6aea7ff631` | FULL; exact byte-verified local copy executed with synthetic fixtures. JSON delivery, environment routing and failure signal. |
| S07 | [.codex-plugin/plugin.json](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/.codex-plugin/plugin.json) | blob `123793e54ffbd933e9a3e6f99e133e8087a08828` | FULL; `skills: ./skills/`, `hooks: {}` and version declaration. Manifest observation, not live Codex execution. |
| S08 | [docs/porting-to-a-new-harness.md](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/docs/porting-to-a-new-harness.md) | blob `4ae9603defaf0d9ff052189a33fe515dd2a4ee2e` | PARTIAL: lines 1–310 read in two contiguous requests. Integration model, capability/acceptance criteria, shapes and native-discovery clarification. Remainder MUST be recovered before closing U01. |
| S09 | [tests/hooks/test-session-start.sh](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/tests/hooks/test-session-start.sh) | blob `c1508290e9813de1a7d20b24d3ca3c8927fbc11c` | FULL SOURCE READ ONLY. Registration, JSON shape, nonempty context and obsolete-warning checks. The upstream suite was not run. |
| S10 | [skills/brainstorming/SKILL.md](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/brainstorming/SKILL.md) | blob `b56a3b5ed6ea0d6216501e0e401ecb00a1b4675f` | FULL in contiguous requests 1–150 and 151–EOF. Three-path request routing, approval, spec/self-review and optional companion reference. Supporting companion/plan/worktree files remain unread. |

A public web view was also opened for current orientation. It is not substituted for these pinned GitHub sources; irrelevant web search results were discarded.

## Initial native source topology

This is an orientation map, **not a complete recursive inventory or final subsystem taxonomy**.

| Family | Observed root entries / role | Coverage limit |
|---|---|---|
| Shared skills | `skills/` | 14 directory entries catalogued; only using-superpowers and brainstorming SKILL bodies read fully this round. |
| Host integration surfaces | `.agents`, `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `.devin-plugin`, `.hermes-plugin`, `.kimi-plugin`, `.opencode`, `.pi`, `gemini-extension.json`, `GEMINI.md` | Presence observed; only the Codex manifest and selected shell-hook sources inspected in depth. Presence does not establish support quality. |
| Bootstrap/hooks | `hooks/` | Selected configuration and script read; wrapper and remaining configurations pending. |
| Supporting runtime/distribution | `scripts/`, `assets/`, `package.json` | Root presence only. Contents and runtime effects not yet characterised. |
| Tests and development history | `tests/`, `.github/`, `.pre-commit-config.yaml`, `.version-bump.json`, `RELEASE-NOTES.md` | One hook test file read; other tests, CI and release-history semantics pending. |
| Orientation/contributor surfaces | `README.md`, `CLAUDE.md`, `AGENTS.md`, `LICENSE`, `CODE_OF_CONDUCT.md` and auxiliary root files | README full; remaining bodies not yet read. Root tree records AGENTS.md as a symlink blob; no behavior is inferred from its name. |
| Documentation | `docs/` | Porting guide partial; other documents and historical design plans not yet inventoried recursively. |

### Skill catalogue

`brainstorming`; `dispatching-parallel-agents`; `executing-plans`; `finishing-a-development-branch`; `receiving-code-review`; `requesting-code-review`; `subagent-driven-development`; `systematic-debugging`; `test-driven-development`; `using-git-worktrees`; `using-superpowers`; `verification-before-completion`; `writing-plans`; `writing-skills`.

This catalogue supports navigation only. It does not mean every skill or its dependencies has been investigated.

## Method and project-context inputs

- `gstack/METHOD.md`, full, blob `dc003b3f74115667a05787a847eadb10876784c8`: source-first semantic synthesis precedent.
- `gstack/META.md`, full, blob `f2ad498742f026aa84578e82ec7fd0cf6843da65`: scope, historical snapshot and no-adoption boundary. Not used to make current gstack runtime claims.
- Current `research/INDEX.md`, `studies/INDEX.md`, `studies/PACKAGE-CONTRACT.md`, `studies/CATALOG.md`: full recovery for placement and continuity. They are project-work context, not evidence about Superpowers.
- Agent-control files are deliberately not part of the substantive research corpus.

## Local experiment evidence

- E01 runner: [evidence/U01-hook-probes.py](evidence/U01-hook-probes.py).
- E02 actual output: [evidence/U01-hook-probes-results.json](evidence/U01-hook-probes-results.json).
- Source transfer: exact S06 content obtained through GitHub, materialised locally and verified against Git blob SHA `93a6bc2c6b7269c704378cb6a61fce6aea7ff631` before execution; 2,274 bytes.
- Environment: Linux, Python 3.13.5, GNU Bash 5.2.37. Temporary synthetic plugin filesystem; no live host, credentials, installation or external API calls.
- Scope: four output/escaping cases passed; two study-defined bootstrap-health challenges failed; one wrong-event negative control was correctly rejected. See the U01 note for interpretation.
- These are source-informed exploratory probes, not independent model evaluation or a preregistered efficacy study.

## Acquisition and negative-evidence limits

A full archive download through the local container was attempted but failed at DNS resolution. No full clone or archive was obtained. Connected GitHub source reads remained available; the exact single-script transfer above does not imply a complete local repository.

Absence from this initial map does not establish repository-wide absence. Missing/empty synthetic bootstrap results do not establish that a correctly installed host encounters that condition in production. No production incident, complete integration qualification, runtime comparison, upstream CI verdict or development-quality benchmark is claimed.
