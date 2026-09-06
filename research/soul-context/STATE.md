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
- the completed Stage-0 capability preflight and current local working-copy blocker;
- current staged bootstrap sequence and immediate next action;
- explicit non-decisions so discussion does not silently become architecture.

## Current Stage-0 result

Codex desktop preflight established that:

- Astra Ultra / `gpt-6-astra` + `ultra` was visible in runtime metadata;
- web-tool research access works;
- private `agentic-os-search` and `soul-production` can be read through the GitHub connector;
- local development tools are broadly available;
- terminal-network access is not generally established;
- the desktop project's actual working directory is **not a Git checkout** of `soul-development-os`.

Independent GitHub inspection confirmed that remote `batuhanozgun/soul-development-os` is initialized on `main` at commit `3776384a7789ccf1959b99bba92c8cf1b3131f81` and contains only `.gitkeep`.

Therefore the current blocker is source binding, not absence of a remote repository.

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

As of 2026-09-06, the current next bridge action is:

> bind the Codex desktop `SOUL-Development-OS` project to an **actual local Git checkout** of `batuhanozgun/soul-development-os`, then run a minimal read-only Git binding recheck before any Development OS design begins.

Required recheck:

- `git rev-parse --show-toplevel` succeeds;
- `git remote -v` identifies the intended repository;
- current branch/ref is visible;
- HEAD/working-tree state is known and consistent with or explicitly behind remote `main`.

After this binding is correct, Stage-1 Development OS bootstrap problem research/design may begin.

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
