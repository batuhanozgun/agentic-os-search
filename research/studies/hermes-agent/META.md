# Hermes Agent — Araştırma metaverisi

- **Study ID / type:** `hermes-agent` / `external-target`.
- **Nesne:** Nous Research Hermes Agent; ajan runtime'ı, kalıcı bilgi/iş ve kullanıcı yüzeylerinin yaşam döngüsü.
- **Statü:** ACTIVE PARTIAL RESEARCH; plan v0.17. [STATE](STATE.md) work/completion authority. U04-A ve ayrı U04-B teslimi uzlaştırıldı; bu yayın yeni kaynak araştırması/deney değildir.
- **Başlangıç / son kayıt:** 2026-09-07 / 2026-09-11.
- **Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; tree `f54f5e9d2682bf11f164de7b34ee10ec121b6434`; manifest 0.21.0. Current release/kurulu binary değildir.
- **Freshness:** pinned source, default-branch navigation, recorded execution ve publication ayrı. Güncel benimseme ilgili kaynak/bağımlılıkların yeniden doğrulanmasını gerektirir.

## Amaç ve reuse

HERMES işi nasıl başlatır, birkaç tur/çalışan boyunca sürdürür, durdurur, saklar ve yeniden işler? Bağlam, task/run, decision/receipt, driver/queue ve semantic acceptance ilişkileri ayrı tutulur. Önce native açıklama, sonra dört-alan/SOUL/Development OS.

**Foundation retrieval hints:** Information — stored/live/request/history ve task handoff; Work — task/run/goal/tick/terminal; Actors — claim/lease/devir; Environment — driver/process/profile/persistence. Çoktan-çoğa provisional adaydır; taxonomy membership veya bitmiş projection değildir. **SOUL:** amaçla yönelen çalışma ile zamana bağlı tekrar, kayıt ile yeniden çalışabilirlik. **Development OS:** ownership, evidence-bound acceptance, block receipt, migration/in-flight recovery, history freshness ve effect/persistence. Reuse rolleri reference/falsifier/mechanism learning/bounded case/design pressure; dependency benimsenmedi.

## Kanıt kimliği ve sınır

[U04-A/18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md): G01–G10/H01–H05, 15 grup; manual Kanban helper + synthetic callbacks, full-heartbeat/temporary SQLite adapter. [U04-B/19](notes/19-U04-DELIVERY-RECONCILIATION.md): G01–G12/H01–H09, 21 durum; iki manual Kanban seçkisi/SQLite fixture reader, full-heartbeat/reduced adapter. İkisi ayrı recorded run/probe/SPEC'tir; eş numaralı vakalar eşdeğer değildir. [Uzlaştırma](evidence/2026-09-11-multiturn/RECONCILIATION.md) raw kimlikleri ve örtüşme/farkları taşır. Yayında hiçbir koşu tekrar edilmedi; transfer/hash/parse kontrolleri behavioral verification değildir.

Tam heartbeat byte kimliği `d3f440d9ed2035505b0bdfbe7d6d57dec926317f` her iki kaydın da sınırlı kaynağıdır. Manuel Kanban parent fidelity ve gerçek SessionDB/init/profile/driver/worker/OS/model-quality/artifact/delivery açık. B:H09 selective child-write fault actual DB/compaction kaybı değildir. A:S10 admission history substitution korunur; alt consumer source429 nedeniyle history-loss veya verified-history hükmü yoktur.

U03/K recovery, U02 source-only ve önceki U01/A/SA/AP/M4/N/MW/C/V ayrı tarih ve kapsamdadır. Üç merkezi provisional synthesis değişmeden korunur; B içindeki alternatif sentezler dördüncü completed model sayılmaz. Yeni native CORE/dört-alan veya architecture/adoption kararı verilmedi.

## Giriş ve revisit

[STATE](STATE.md) → [INDEX](INDEX.md) → [PLAN](RESEARCH-PLAN.md)/[METHOD](METHOD.md). [Merkezi synthesis/03](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md), [U04-A kaynakları](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [U04-B özgün teslim](evidence/2026-09-11-multiturn/README.md), [coverage](inventory/CONTINUITY-COVERAGE-2026-09-11.md). İlk sonraki actual turn lease/history/SessionDB ve rotation/restart driver recovery.

Revisit: session resumption, autonomous scheduling, ownership/cancel, goal verification, receipt/commit, migration, memory/skill/ledger/sync, upstream değişimi ve load-bearing security/adoption. Foundation/control/context/Codex/upstream/architecture mutation yok. Kaynaktaki prompt/AGENTS/SOUL metinleri assistant control değildir. OpenClaw ayrı adaydır; diğer studies yalnız seçici reuse adaylarıdır. [Önceki v0.16 metadata](https://github.com/batuhanozgun/agentic-os-search/blob/a0585203ca0a2bdd1cc8441aa152d7e4a72128cf/research/studies/hermes-agent/META.md).
