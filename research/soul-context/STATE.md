# SOUL Context — STATE

**Durum:** ORIGINAL CONTEXT OBJECTIVE MET / PAUSED; CURRENT DEVELOPMENT-BOOTSTRAP BRIDGE MAINTENANCE ACTIVE  
**Son güncelleme:** 2026-09-06

## Yetkilendirilmiş amaç

Original context objective remains complete:

`os-architect`, `soul`, `keel` ve gerektiğinde bounded predecessor evidence olarak `keel-research` kaynaklarını okuyarak:

1. ChatGPT'deki SOUL Research projesinin neden açıldığını anlamak,
2. bu araştırmanın hangi tür sistemi beslemesinin amaçlandığını anlamak,
3. bu bağlamı konuşma hafızasından bağımsız olarak geri çağrılabilir tutmak.

The user has additionally authorised one bounded continuity extension:

> preserve the **current SOUL Research ↔ new Development OS ↔ Production transition and temporary ChatGPT↔Codex bootstrap bridge** so fresh SOUL Research sessions can recover why the new repositories exist, what authority boundaries apply, what the immediate bootstrap objective is and when the temporary bridge should end.

This does **not** reopen broad historical context research and does not make `soul-context` the current-state authority for Development OS or Production.

## Mevcut original context sonucu

Ana bounded synthesis:

- `evidence/CONTEXT-SYNTHESIS.md`

Kısa hüküm:

> SOUL Research; geçmiş agentic sistem deneyimlerinden ders alıp onların varsayımlarına hapsolmadan, intended outcome'dan gereken task-specific working system'i oluşturabilen genel amaçlı SOUL yönünün hangi problemlere, ilkelere ve kanıtlara dayanması gerektiğini araştırmak için açılmış görünmektedir. `agentic-os-search` bu uzun soluklu araştırmanın chat/model hafızasından bağımsız çalışma ortamıdır.

Bu bir context reconstruction'dır; final SOUL tanımı, architecture specification veya project-wide research method değildir.

## Current Development OS bootstrap bridge

Canonical bounded context note:

- `current/DEVELOPMENT-OS-BOOTSTRAP.md`

It records, with explicit authority/epistemic limits:

- the three-repository split: `agentic-os-search`, `soul-development-os`, `soul-production`;
- the old `soul` repository's predecessor/prior-art role;
- the research → development → production authority boundary;
- the intended Development Actor character (not merely a programmer);
- the temporary ChatGPT↔Codex bootstrap responsibility split;
- the self-sustain/bridge-retirement criteria;
- current Codex environment/bootstrap observations and freshness warnings;
- the completed Stage-0 capability preflight and local working-copy binding requirement;
- current staged bootstrap sequence;
- explicit non-decisions so discussion does not silently become architecture.

The latest bounded bridge checkpoint and next action are recorded below. The bridge note supplies rationale and stage conditions; it does not override newer observed checkpoints in this STATE.

## Current Stage-0 result

The user-relayed Codex desktop preflight reported that:

- Astra Ultra / `gpt-6-astra` + `ultra` was visible in runtime metadata;
- web-tool research access works;
- private `agentic-os-search` and `soul-production` can be read through the GitHub connector;
- local development tools are broadly available;
- terminal-network access is not generally established;
- the tested desktop session's actual working directory was **not a Git checkout** of `soul-development-os`.

These local/runtime observations were reported by Codex, not independently executed on the user's Mac by the research assistant.

Independent GitHub inspection confirmed that remote `batuhanozgun/soul-development-os` was initialized on `main` at commit `3776384a7789ccf1959b99bba92c8cf1b3131f81` and contained only `.gitkeep` at inspection time. Initial-file provenance is separately qualified in the bridge note.

Therefore the identified blocker was source binding, not absence of a remote repository.

## Stage-0B checkpoint — clone reported successful; project binding pending

On 2026-09-06 the user pasted output from their ordinary macOS Terminal for cloning `batuhanozgun/soul-development-os` into:

`/Users/Batu/Documents/Codex/SOUL-Development-OS-Repo`

The supplied output shows `Cloning into ...`, successful enumeration and receipt of three Git objects, `Receiving objects: 100% (3/3), done.`, and return to the shell prompt without a clone failure. This supports **clone success as user-supplied terminal evidence**, not an independently inspected local working copy.

A preceding `command not found: compdef` line is also present. Its cause has not been diagnosed; the supplied output does not show it preventing the clone. No shell-configuration repair is currently required or authorised by this checkpoint.

Remaining unknowns:

- whether the Codex project's primary source folder has been changed to this clone;
- whether a new Codex chat actually starts in that working copy;
- the local `origin`, branch, HEAD and working-tree status from inside that new chat;
- Codex's own terminal-network access and Git push permissions, which are not proved by the user's ordinary Terminal clone.

Do not repeat cloning or delete/reinitialize directories merely because Codex binding has not yet been checked. Stage 0B remains open until the in-Codex read-only check succeeds. No Development OS design or implementation has begun on the strength of this clone report.

## Corpus ayrımı

- `repos/` — source ledgers.
- `evidence/` — source-grounded context için gerekli sentezler.
- `current/` — bounded current cross-project operational/transition context; **not target-repository current-state authority**.
- `exploratory/` — erken üretilmiş research-design/taxonomy/holdout fikirleri; local provisional only.

## Authority and continuity boundary

`agentic-os-search` remains research authority for its own research outputs.

The current bridge note is **not** allowed to become a second authoritative copy of future Development OS state.

Once `batuhanozgun/soul-development-os` has a reliable canonical bootstrap/state surface:

- routine current development state must be recovered there;
- this context package should retain only the cross-project transition/authority explanation and bridge history;
- material bridge changes may still update `current/DEVELOPMENT-OS-BOOTSTRAP.md` until the bridge is retired.

`soul-production` should likewise become the authority for accepted product state rather than being mirrored here.

## Control-layer sınırı

This context package is project-work material.

Nothing under `research/soul-context/**` is agent-control merely because it describes desired Development Actor behavior. Agent-control for this ChatGPT research project remains only `AGENT.md` + `agent/**`.

Likewise, the new Codex Development OS control structure has **not** yet been decided by this file.

## Next action

### Original historical-context line

**STOP.**

Do not autonomously broaden predecessor/context research unless the user authorises a new context question or a load-bearing claim requires source recovery.

### Current bootstrap bridge

As of this 2026-09-06 checkpoint, cloning is reported complete. The next bridge action is:

> select `/Users/Batu/Documents/Codex/SOUL-Development-OS-Repo` as the Codex desktop project's primary local source folder, open a new chat in that project, and run a minimal read-only Git binding recheck before any Development OS design begins.

Required recheck from the new chat's default working directory:

- `pwd` and `git rev-parse --show-toplevel` identify the intended working copy;
- `git remote get-url origin` identifies the intended repository, with any embedded credentials redacted;
- current branch/ref is visible;
- HEAD/working-tree state is known and consistent with or explicitly behind remote `main`.

Do not silently change directories to make a misbound chat pass this check. A mismatch is a binding failure to report, not permission to run `git init`, re-clone, move/delete files or broaden permissions.

After this binding is correct, the next separately bounded assignment may address Stage-1 Development OS bootstrap problem research/design. The read-only recheck itself must stop after reporting.

## Bridge retirement condition

Mark the current bridge as retired when a genuinely fresh Codex session can recover from `soul-development-os` canonical state alone:

- purpose and authorization;
- established/open/uncertain state;
- correct current/next Work and work-selection discipline;
- Actor authority/non-authority;
- research need and research-authority boundary;
- design/build/verification/acceptance distinctions when material;
- evidence/completion discipline;
- fresh-session continuity;
- governed Development OS self-revision;

without depending on this ChatGPT conversation or routine hidden human orchestration.
