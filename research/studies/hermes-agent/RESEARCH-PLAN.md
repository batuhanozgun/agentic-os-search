# Hermes Agent — Araştırma planı

**v0.14 / 2026-09-10.** General turn/context/session source trace, ikinci provisional sentez ve tur-üstü iş araştırmasına somut köprü. İş otoritesi [STATE](STATE.md); yöntem/kapanış [METHOD](METHOD.md). [V0.13 tam plan](https://github.com/batuhanozgun/agentic-os-search/blob/c163836d959e3ada2f31afd353bb364671b5fb32/research/studies/hermes-agent/RESEARCH-PLAN.md) önceki ayrıntıları korur.

## 1. Hedef ve aşama

Önce HERMES-native mekanizmalar/ilişkiler, sonra Information/Work/Actors/Environment ve SOUL/Development OS. Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0. Current release doğrulaması değil. A0 kurulmuş; A1 hedefli topoloji kısmi; B0/U01 derin öğrenme/onay kanıtı; C katmanında learning/change ve general execution için iki provisional sentez vardır. Bunlar bütün native sistem, CORE, dört-alan veya fayda ölçümü değildir.

## 2. V0.14 ne ekledi?

[16/U02](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md) ve [SOURCES](evidence/2026-09-10-turn-lifecycle/SOURCES.md): actual normal gateway prepare/lease/history/cache/run/result/persist/delivery; user-turn/iteration/API-attempt fazları; sidecar ve API copy; tool round ile SessionPersistence sözleşmesi; stop/finalize; admitted compaction build ve stored-prompt ilişkisi. Yeni source okuması + cross-module inference; **yeni runtime testi yok**.

M4'ün artificial V04 sırasını actual compression diye yorumlamak, C13 normal caller ile desteklenmiyor: invalidate/reload → build → only-byte-equal keep → commit/return. Q07/Q22'nin normal source bağı artık API-message assembly'ye uzanır. Actual network/UI timing ve tüm path'ler açık. C12/C17 kanban, C13 goal/loop/heartbeat, C14/C18 lease/generation dış iş katmanını görünür kıldı.

[Synthesis/02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md), [synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md)'in dışarıda bıraktığı genel çekirdeği ve kontrol/kayıt/teslim ayrımlarını açıklar. [CORE-COVERAGE](inventory/CORE-COVERAGE-2026-09-10.md) targeted kapsamdır; recursive upstream census değil.

## 3. İlk sonraki birim — kalıcı iş nasıl kabul edilir?

Soru: Kanban task'ı hangi durumda çalıştırılabilir olur; hangi claim/run/actor onu yürütür; agent turu complete/block bildirince hangi kalıcı geçiş kabul edilir; kesilen/eski çalışanın sonucu ne olur?

Kaynak başlangıcı: `agent/kanban_stop.py` (C17) ve `turn_finalizer` içindeki `hermes_cli.kanban_db_dispatch._record_task_failure` (C12). Terminal state tüketicisi ile task create/claim/dispatch girişini iki yönlü takip et. Yardımcı modüllerin adları yerine actual caller/symbol ilişkileriyle primary pin'de ilerle. Kanban schema/state dosyaları görülmeden kolon veya durum adları icat etme.

Beklenen çıktı: normal task → claim → run → terminal receipt → accepted state açıklaması ve interruption/lease loss/retry gibi maddi bir karşı yol. Tool-call adı, process exit, result mesajı, kalıcı transition ve kabul aynı şey değildir. Offline deney mümkünse gerçek transition consumer/bounded DB davranışı kullanılmalı; sentetik model cevabı gerçek agent kalitesi diye sunulmaz. Kurulum/provider/credential kullanımı yok.

Durma ölçütü: bu bounded işin sahibi, başlama koşulu, yürütme sınırı, kabul/red ve recovery ilişkileri kaynaktan yeniden kurulabiliyor olmalı; bütün kanban ürününün test edilmesi gerekmez. Sonra goal/loop/heartbeat aynı işi mi farklı sürekliliği mi yönetiyor karşılaştırılır. Farklı bileşenleri peşinen tek Work ontology'si altında sabitleme.

## 4. Geniş kapsam ve kaynak bağımlılıkları

| Aile | Current frontier |
|---|---|
| F01 start/loop/retry/interrupt | Normal phase spine açıldı; full error/recovery helpers ve alternate runtime açık. |
| F02 context/prompt/schema/cache | Normal refresh/request taşıyıcısı source-backed; last-wire/provider/engine variants açık. |
| F03 session/lineage/search/repair | Persistence mixin/cache/binding/in-place/rotation source; actual SQLite/lease/crash/search açık. |
| F04 memory/skill/approval/rollback/sync | Eski bounded evidence + actual compaction bridge; quality/ledger/sync/skill reuse açık. |
| F05 provider/credential/profile/config | Normal config/cache/turn routing; all provider/secret/profile paths açık. |
| F06 tool/plugin/MCP/authority | Actual round/persistence and middleware boundaries; Q26/Q29 full execution açık. |
| F07 backend/native | External thread owner branch; underlying backends/containment açık. |
| F08 delegation/cancel/writers | Generation/lease release/redirect source; physical cancellation/delegation closure açık. |
| F09 gateway/auth/delivery | Normal prepare/run/persist/deliver; complete platform/delivery acknowledgement açık. |
| F10 cron/proactive/queue/restart | **Kanban + goal/loop/heartbeat yeni tur-üstü frontier.** Ayrı task family gerekip gerekmediği sonraki source turunda sınanır. |
| F11 CLI/TUI/apps/API/ACP | Normal gateway derinleşti; CLI host ve alternate UI/runtime eşdeğerliği açık. |
| F12 install/update/compat/eval | Source-based model; new HERMES tests yok, upstream suite/quality/install/current release açık. |

Ledger/backup/restore/sync → skill/cache → curator report/cron köprüleri kaybolmaz; yeni outer-work modeliyle yeniden önceliklenir. Bütün U01 residual'larının kapanması genel araştırmanın ön koşulu değildir.

## 5. Kontrol ve yayın sınırı

01–15 notları, synthesis/01 ve eski evidence immutable history olarak korunur; U02 onları kendi kapsamında refine eder. A/SA/AP/M4 tekrar veya independent corroboration sayılmaz. Q26/Q29 full-original verifier NOT RUN; yeni tam kaynak/bağımlılık, ilgili değişiklik veya load-bearing reuse yeniden açar. Kod okuması actual runtime, comment geçmiş olayı, kaynak listesinin varlığı içerik FULL read değildir.

Erişim hatasını kalıcı yokluk sayma; seri retry veya kısıt dolaşma yok. Nihai CORE/dört-alan/adoption'a erken atlama. Yeni turdan önce STATE/INDEX/META/CATALOG ve kaynak defteri coherent olmalı; final yayın non-force ve ref/content readback ile kapanır. Bitiş ölçütü METHOD, sürüm veya test sayısı değil.
