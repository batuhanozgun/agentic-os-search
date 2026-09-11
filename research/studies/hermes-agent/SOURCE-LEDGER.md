# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-11 / plan v0.17.** Work authority [STATE](STATE.md). Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; current upstream/installed binary doğrulaması değildir. V0.17 publication reconciliation; yeni upstream okuması veya behavioral run yoktur.

## Tarihsel kaynakları koruyan giriş

[V0.16 exact ledger](https://github.com/batuhanozgun/agentic-os-search/blob/a0585203ca0a2bdd1cc8441aa152d7e4a72128cf/research/studies/hermes-agent/SOURCE-LEDGER.md) → [V0.15 exact](https://github.com/batuhanozgun/agentic-os-search/blob/13e00420d27547998475ac3d1bcd0d4a492f2229/research/studies/hermes-agent/SOURCE-LEDGER.md) → [V0.14](https://github.com/batuhanozgun/agentic-os-search/blob/25b06521083e2a4ddf7b0dbeb9454804796963b6/research/studies/hermes-agent/SOURCE-LEDGER.md), [SOURCE-LEDGER-THROUGH-V0.9](SOURCE-LEDGER-THROUGH-V0.9.md). Tüm eski evidence/notlar değişmeden korunur.

[U02 C01–C18/R01–R02](evidence/2026-09-10-turn-lifecycle/SOURCES.md) source-only genel tur modelidir. [U03 S01–S04/K](evidence/2026-09-10-kanban-task/SOURCES.md), eski selected-source/SQLite koşusu ve publication recovery; original15 archive blob `5484ca39caf7ae5a8f6a31b68caeec0f9a44363d`. M4/V04 artificial sıra actual normal compression değildir; eski UI/A/SA/AP ortak kaynakları bağımsız doğrulama sayılmaz.

## U04-A — önceden yayımlanmış kayıt

[18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → **[A S01–S11](evidence/2026-09-11-multi-turn-continuity/SOURCES.md)** → [A RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md). S01 goals full-readable; S02 quiet CLI, S03 drivers, S04 loops, S06 gateway seçili; S05 full-original heartbeat; S07 test source NOT RUN; S08 prolog/S09 loop-head seçili; S10 facade FULL READ; S11 MIT byte-matched. Bunlar A kaynak kaydıdır, bu transfer turunda yeniden okunmuş upstream sayılmaz.

SPEC blob `ee17ae74098f941b70e07bcf496d6d9be0206892`. Recorded run `2026-09-11T06:10:29.139368+00:00`; G01–G10 manual helper/synthetic callbacks, H01–H05 full heartbeat/reduced SQLite adapter. [9-file raw archive](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz) blob `89b1c87027f7e794133697ff07259474591affa4`, [manifest](evidence/2026-09-11-multi-turn-continuity/MANIFEST.json); raw RESULT SHA-256 `ae5b94ce2e4c540ef72074e4e37bd3f20fe60615c8e126781615b1e08ce7ebf3`. [Summary](evidence/2026-09-11-multi-turn-continuity/RESULT-SUMMARY.json) ayrıntıların yerine geçmez. A:S10 admission history substitution ve A:H05 stale manager sınırı B tarafından silinmez.

## U04-B — özgün 21-durumlu teslim, şimdi native kayıt

[19](notes/19-U04-DELIVERY-RECONCILIATION.md) → **[B kaynak defteri](evidence/2026-09-11-multiturn/delivery/SOURCES.md)** → [B RESEARCH](evidence/2026-09-11-multiturn/delivery/RESEARCH.md). B:S01–S08 kendi full/selected/reused kapsamlarını korur. Eski candidate repo-updates current state değildir.

Recorded run `2026-09-11T06:11:47.964054+00:00`; [SPEC](evidence/2026-09-11-multiturn/delivery/evidence/SPEC.md), [raw RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json), [probe](evidence/2026-09-11-multiturn/delivery/evidence/probe.py), [INPUTS](evidence/2026-09-11-multiturn/delivery/evidence/INPUTS.json). Raw SHA-256 `42929ea7388c9426bcdd08507ce953f14a5ff887296ac9143bbd7bd672d213a7`; probe `9fb2bef88e069d99233d978c02603cf15acc0aa7b38af0b5e8dc42a13b8e1a38`; SPEC `1253b10234b4dbe2cac3d11f1afdd8bb4547ba456609edbf4ae8e8aad65ba869`.

B:G01–G12 manual goal-loop + manual goal_run_status/real reduced SQLite records; task writes/get_task/judge/model fixture. B:H01–H09 full heartbeat (`d3f440d9ed2035505b0bdfbe7d6d57dec926317f`, 11,016 bytes), controlled clock/MetaDB adapter. B:H08/H09 normal/child-save-fault migration kayıtları actual SessionDB/compaction yürütmesi değildir. A:G06 ile B:G10, A:H04 ile B:H07 ve diğer numaralar birbirine eşit kabul edilmez; [çapraz kayıt](evidence/2026-09-11-multiturn/RECONCILIATION.md).

[33-file delivery manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json) native tree `d01c92f7414713300934be3bb4e3d40ac57631b3` ve tüm byte/Git kimliklerini bağlar; [original SHA manifest](evidence/2026-09-11-multiturn/delivery/MANIFEST.sha256) değişmez. Transferde hash/parse ve kayıtlı input ilişkileri kontrol edildi, probelar yeniden koşulmadı. A/B iki independent replication veya 36 ürün testi değildir.

## Açık consumer sınırı

A:S10 facade history'yi admission'dan değiştirebilir; actual `turn_facade_lease.py` önceki source429 nedeniyle açık. İlk çalışma bu consumer'dan SessionDB/history'ye, sonra gerekli manager migration/driver/in-flight recovery'ye gider. B:H09 adaptörü gerçek DB'nin yerine tekrar kullanılamaz. Q07/Q22 last wire, Q26/Q29 full worker, Q38 K/G selection fidelity, actual process/cancel, judge/gate effectiveness, profile/driver ve delivery açıktır. Merkezi üç sentez yeni bağımsız kanıt değildir; bu yayın önceki kanıtı korur.
