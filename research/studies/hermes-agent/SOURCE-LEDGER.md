# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-11 / plan v0.16.** Work authority [STATE](STATE.md). Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; current upstream/installed binary doğrulaması değildir.

## Tarihsel kaynakları koruyan giriş

[V0.15 exact ledger](https://github.com/batuhanozgun/agentic-os-search/blob/13e00420d27547998475ac3d1bcd0d4a492f2229/research/studies/hermes-agent/SOURCE-LEDGER.md) → [V0.14 ledger](https://github.com/batuhanozgun/agentic-os-search/blob/25b06521083e2a4ddf7b0dbeb9454804796963b6/research/studies/hermes-agent/SOURCE-LEDGER.md), [SOURCE-LEDGER-THROUGH-V0.9](SOURCE-LEDGER-THROUGH-V0.9.md). Bütün eski evidence ve notlar yerindedir.

[U02 C01–C18/R01–R02](evidence/2026-09-10-turn-lifecycle/SOURCES.md) source-only genel tur modelidir. [U03 S01–S04/K](evidence/2026-09-10-kanban-task/SOURCES.md) eski selected-source/SQLite koşusu ve publication recovery; original15 archive blob `5484ca39caf7ae5a8f6a31b68caeec0f9a44363d`. U04 bunları rerun etmedi. M4/V04 artificial sırası normal actual compression diye kullanılmaz; A/SA/AP örtüşen koşular independent değildir.

## U04 — Yeni multi-turn source ve G/H koşusu

[18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → **[S01–S11 SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md)** → [RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md). S01 goals full-readable source; S02 quiet CLI selected; S03 CLI loop drivers selected; S04 loops selected; S05 full-original heartbeat verified/executed; S06 gateway drivers selected; S07 tests source-inspected NOT RUN; S08 prolog selected; S09 loop head/U02 reused; S10 facade FULL READ; S11 MIT byte-matched.

Pre-run SPEC blob `ee17ae74098f941b70e07bcf496d6d9be0206892`. Recorded execution `2026-09-11T06:10:29.139368+00:00`. G01–G10 manual run_kanban_goal_loop selection with synthetic callbacks, no parent byte/AST proof. H01–H05 whole heartbeat blob `d3f440d9ed2035505b0bdfbe7d6d57dec926317f` (11,016 bytes) with real temporary SQLite fixture accessor/synthetic clock. Neither is whole Hermes/worker/model/driver execution.

[Exact archive](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz), blob `89b1c87027f7e794133697ff07259474591affa4`, 9 regular files. [Manifest](evidence/2026-09-11-multi-turn-continuity/MANIFEST.json) all hashes; raw RESULT SHA256 `ae5b94ce2e4c540ef72074e4e37bd3f20fe60615c8e126781615b1e08ce7ebf3`; [summary](evidence/2026-09-11-multi-turn-continuity/RESULT-SUMMARY.json) omits detailed traces. Mutation controls target superseded/finalize and full-source integrity, not total coverage or independent replication.

## Açık source/consumer sınırları

Actual `turn_facade_lease.py` and extra loops range returned429; no invented content/serial retries. S10 can substitute admission history, so quiet caller read is not sufficient for a history-loss assertion. Actual SessionDB/lease/history, migration/driver/in-flight recovery, real process/cancel, provider/judge/gate effectiveness and delivery remain open. Q07/Q22 last wire; Q26/Q29 full worker; Q38 old K source fidelity remain unchanged. Synthesis is explanation, not another evidence source.
