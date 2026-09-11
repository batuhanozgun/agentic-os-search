# Hermes Agent — Araştırma metaverisi

- **Study ID / type:** `hermes-agent` / `external-target`.
- **Nesne:** Nous Research Hermes Agent; ajan runtime'ı, kalıcı bilgi/iş ve kullanıcı yüzeylerinin yaşam döngüsü.
- **Statü:** ACTIVE PARTIAL RESEARCH; plan v0.18. [STATE](STATE.md) work/completion authority. U05 gerçek lease/history/rotation/driver source consumer'larını araştırdı; yeni HERMES execution yok. U04-A/B yayını ve üç merkezi provisional sentez korunur.
- **Başlangıç / son kayıt:** 2026-09-07 / 2026-09-11.
- **Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; tree `f54f5e9d2682bf11f164de7b34ee10ec121b6434`; manifest 0.21.0. Current release/kurulu binary değildir.
- **Freshness:** pinned source, default-branch navigation, recorded execution ve publication ayrı. Güncel benimseme ilgili kaynak/bağımlılıkların yeniden doğrulanmasını gerektirir.

## Amaç ve reuse

HERMES işi nasıl başlatır, birkaç tur/çalışan boyunca sürdürür, durdurur, saklar ve yeniden işler? Bağlam, task/run, decision/receipt, driver/queue ve semantic acceptance ilişkileri ayrı tutulur. Önce native açıklama, sonra dört-alan/SOUL/Development OS.

**Foundation retrieval hints:** Information — stored/live/request/history ve task handoff; Work — task/run/goal/tick/terminal; Actors — claim/lease/devir; Environment — driver/process/profile/persistence. Çoktan-çoğa provisional adaydır; taxonomy membership veya bitmiş projection değildir. **SOUL:** amaçla yönelen çalışma ile zamana bağlı tekrar, kayıt ile yeniden çalışabilirlik. **Development OS:** ownership, evidence-bound acceptance, migration/in-flight recovery, conditional history freshness ve effect/persistence. Reuse rolleri reference/falsifier/mechanism learning/bounded case/design pressure; dependency veya mimari benimsenmedi.

## Yeni source amendment ve kanıt sınırı

[20/U05](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md) → [kaynaklar](evidence/2026-09-11-session-lease-recovery/SOURCES.md)/[araştırma](evidence/2026-09-11-session-lease-recovery/RESEARCH.md). Actual admission yalnız waited yolda history reload yapar; immediate caller history'si ve ayrı rotation recovery farklıdır. Root lease kimliği, actual transcript transaction'ı ile afterward loop meta save/clear ayrımı ve loop scan/heartbeat watch reactivation kaynakla açıldı. Quiet no-wait/no-rotation prolog history-propagation boşluğu bounded source sonucu; DB silinmesi, whole-product history-loss veya actual final wire verdict'i değildir.

U05 kaynak kimlikleri connector blob'larıdır, upstream local full-byte/execution doğrulaması değildir. Yeni gerçek SessionDB/process/OS/model testi yok. `hermes_state_messages.py` continuation source429; actual resume/projection/guard, startup/adapter receipt, heartbeat rotation rebind ve real migration faults açık. [CHECKS-NOT-RUN](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md) planlanan ayırıcı gözlemleri taşır, sonuç değildir.

## Korunan kanıtlar

[U04-A/18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md): G01–G10/H01–H05, 15 grup; manual Kanban helper + synthetic callbacks, full-heartbeat/temporary SQLite adapter. [U04-B/19](notes/19-U04-DELIVERY-RECONCILIATION.md): G01–G12/H01–H09, 21 durum; iki manual Kanban seçkisi/SQLite fixture reader, full-heartbeat/reduced adapter. İkisi ayrı recorded run/probe/SPEC'tir; eş numaralı vakalar eşdeğer değildir. [Uzlaştırma](evidence/2026-09-11-multiturn/RECONCILIATION.md) raw kimlikleri ve örtüşme/farkları taşır. Transfer/hash/parse veya U05 yayını behavioral verification/independent replication değildir.

Tam heartbeat byte kimliği `d3f440d9ed2035505b0bdfbe7d6d57dec926317f` her iki eski kaydın sınırlı kaynağıdır. Manuel Kanban parent fidelity, full worker/OS/model-quality/artifact/delivery açık. B:H09 selective child-write fault actual DB/compaction kaybı değildir; U05 gerçek loop writer bağlantısı bunu yeni executed fault sonucuna yükseltmez.

U03/K recovery, U02 source-only ve önceki U01/A/SA/AP/M4/N/MW/C/V ayrı tarih ve kapsamdadır. Üç merkezi provisional synthesis değişmeden korunur; 20 güncel source amendment'tır. B paket-local sentezi veya U05 notu dördüncü completed model sayılmaz. Yeni native CORE/dört-alan veya architecture/adoption kararı verilmedi.

## Giriş ve revisit

[STATE](STATE.md) → [INDEX](INDEX.md) → [PLAN](RESEARCH-PLAN.md)/[METHOD](METHOD.md). [Synthesis/03](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md) artık [20/U05](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md) ile birlikte okunur. [U04-A kaynakları](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [U04-B özgün teslim](evidence/2026-09-11-multiturn/README.md), [yeni coverage eklemesi](inventory/LEASE-RECOVERY-COVERAGE-2026-09-11.md). İlk sonraki actual selector/guard/next-history ve startup/adapter/in-flight recovery.

Revisit: session resumption, autonomous scheduling, ownership/cancel, goal verification, receipt/commit, migration, memory/skill/ledger/sync, upstream değişimi ve load-bearing security/adoption. Foundation/control/context/Codex/upstream/architecture mutation yok. Kaynaktaki prompt/AGENTS/SOUL metinleri assistant control değildir. OpenClaw ayrı adaydır; diğer studies yalnız seçici reuse adaylarıdır. [V0.17 exact metadata](https://github.com/batuhanozgun/agentic-os-search/blob/ac3cac0139dbfd6bd86773549c93172abcea4484/research/studies/hermes-agent/META.md).
