# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-11 / plan v0.18.** Work authority [STATE](STATE.md). Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; current upstream/installed binary doğrulaması değildir. U05 yeni pinned source araştırmasıdır; **yeni HERMES execution veya independent replication yoktur**.

## Güncel kaynak girişi — U05

[20](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md) → **[U05-S01–S10](evidence/2026-09-11-session-lease-recovery/SOURCES.md)** → [RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md). S01 facade lease, S02 facade, S08 loops, S09 gateway goals FULL READ; S03 real DB compression/leases, S04 writer/meta, S05 quiet CLI, S06 prolog, S07 recovery/publication SELECTED; S10 transcript guard başı PARTIAL. 'FULL READ' local original-source byte/AST equality veya execution değildir.

Kaynak sonuçları: waited-only history reload; separate rotation recovery; quiet caller/prolog boundary; root-key lease; atomic transcript publication versus afterward state transfer; loop helper→real meta writer; restored in-flight gate ve heartbeat live watch. S10 continuation 429; actual DB resolve/projection/guard, startup/adapter receipt, heartbeat rebind, gerçek fault/process/OS/model-quality açık. Eski facade429 artık source engeli değildir. [NOT RUN kontrol tasarımı](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md) uygulanmış probe/SPEC değildir. Keşfedilen upstream test/startup yolları bu tur okunmuş/koşulmuş sayılmaz.

Default-branch search navigasyonu primary'den ayrıdır. Stored-response paging'de yanlış path/blob metadata'sı görülen temsil dışlandı; kritik compression kaynakları direct path/ref/range ile okundu. Yerel source download materyalizasyonu gerçekleşmedi. Ayrıntılı erişim ve exclusion kaydı U05 SOURCES'tadır.

## Tarihsel kaynakları koruyan giriş

[V0.17 exact ledger](https://github.com/batuhanozgun/agentic-os-search/blob/ac3cac0139dbfd6bd86773549c93172abcea4484/research/studies/hermes-agent/SOURCE-LEDGER.md) → [V0.16](https://github.com/batuhanozgun/agentic-os-search/blob/a0585203ca0a2bdd1cc8441aa152d7e4a72128cf/research/studies/hermes-agent/SOURCE-LEDGER.md) → [V0.15](https://github.com/batuhanozgun/agentic-os-search/blob/13e00420d27547998475ac3d1bcd0d4a492f2229/research/studies/hermes-agent/SOURCE-LEDGER.md), [SOURCE-LEDGER-THROUGH-V0.9](SOURCE-LEDGER-THROUGH-V0.9.md). Bütün eski evidence/notlar değişmeden korunur.

[U02 C01–C18/R01–R02](evidence/2026-09-10-turn-lifecycle/SOURCES.md) source-only genel tur modelidir; kaynak defteri U05'te tekrar okundu, bütün upstream consumer'ları yeni full read/run sayılmaz. [U03 S01–S04/K](evidence/2026-09-10-kanban-task/SOURCES.md), eski selected-source/SQLite koşusu ve publication recovery; original15 archive blob `5484ca39caf7ae5a8f6a31b68caeec0f9a44363d`. M4/V04 artificial sıra actual normal compression değildir; eski UI/A/SA/AP ortak kaynakları bağımsız doğrulama sayılmaz.

## U04-A — korunan 15-gruplu kayıt

[18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → [A S01–S11](evidence/2026-09-11-multi-turn-continuity/SOURCES.md) → [A RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md). SPEC blob `ee17ae74098f941b70e07bcf496d6d9be0206892`. Recorded run `2026-09-11T06:10:29.139368+00:00`; G01–G10 manual helper/synthetic callbacks, H01–H05 full heartbeat/reduced SQLite adapter. [9-file raw archive](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz) blob `89b1c87027f7e794133697ff07259474591affa4`, [manifest](evidence/2026-09-11-multi-turn-continuity/MANIFEST.json); raw RESULT SHA-256 `ae5b94ce2e4c540ef72074e4e37bd3f20fe60615c8e126781615b1e08ce7ebf3`.

[Summary](evidence/2026-09-11-multi-turn-continuity/RESULT-SUMMARY.json) exact raw yerine geçmez. A:S10 admission history substitution U05'te koşullarına ayrıldı; A:H05 stale manager sınırı değişmez. A'nın raw/probe'u bu tur yeniden çalıştırılmadı.

## U04-B — korunan 21-durumlu özgün teslim

[19](notes/19-U04-DELIVERY-RECONCILIATION.md) → [B kaynak](evidence/2026-09-11-multiturn/delivery/SOURCES.md) → [B RESEARCH](evidence/2026-09-11-multiturn/delivery/RESEARCH.md). Recorded run `2026-09-11T06:11:47.964054+00:00`; [SPEC](evidence/2026-09-11-multiturn/delivery/evidence/SPEC.md), [raw RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json), [probe](evidence/2026-09-11-multiturn/delivery/evidence/probe.py), [INPUTS](evidence/2026-09-11-multiturn/delivery/evidence/INPUTS.json). Raw SHA-256 `42929ea7388c9426bcdd08507ce953f14a5ff887296ac9143bbd7bd672d213a7`; probe `9fb2bef88e069d99233d978c02603cf15acc0aa7b38af0b5e8dc42a13b8e1a38`; SPEC `1253b10234b4dbe2cac3d11f1afdd8bb4547ba456609edbf4ae8e8aad65ba869`.

B:G01–G12 manual goal-loop/status/reduced SQLite; B:H01–H09 full heartbeat (`d3f440d9ed2035505b0bdfbe7d6d57dec926317f`, 11,016 bytes), controlled clock/MetaDB adapter. B:H08/H09 normal/child-save-fault migration actual SessionDB/compaction yürütmesi değildir. U05 real loop writer source bağı bunları yeni actual fault testine dönüştürmez. [Çapraz kayıt](evidence/2026-09-11-multiturn/RECONCILIATION.md) A/B kimliklerini ayrı tutar.

[33-file delivery manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json), native tree `d01c92f7414713300934be3bb4e3d40ac57631b3`, [original SHA manifest](evidence/2026-09-11-multiturn/delivery/MANIFEST.sha256) ve bütün 33 özgün dosya korunur. B candidate repo-updates current state değildir. Yayın hash/parse kontrolleri veya U05 okumaları A/B'yi independent replication/36 ürün testi yapmaz.

## Açık consumer sınırı

İlk sonraki U05-S10 actual selector/guard ve quiet next-history; ardından startup/adapter/in-flight recovery, gerekli migration DB/profile bağı. Q07/Q22 last wire, Q26/Q29 full worker, Q38 K/G selection fidelity, actual process/cancel, judge/gate effectiveness ve delivery açıktır. Merkezi üç sentez yeni bağımsız kanıt değildir; U05 not20 source amendment olarak onlarla birlikte okunur.
