# Hermes Agent — Araştırma metaverisi

- **Study ID / type:** `hermes-agent` / `external-target`.
- **Nesne:** Nous Research Hermes Agent; runtime, kalıcı bilgi/iş, oturum ve kullanıcı yüzeylerinin yaşam döngüsü.
- **Statü:** ACTIVE PARTIAL RESEARCH; plan v0.20; U07 yayın checkpoint'i. Yayın/ref doğrulaması U07 PUBLICATION'dadır. [STATE](STATE.md) current work/completion authority. U07 cron source study + full native delivery-queue / real temp SQLite diagnostic; önceki U06 korunur. Whole DB/gateway/restart/model doğrulaması yok.
- **Başlangıç / son kayıt:** 2026-09-07 / 2026-09-11.
- **Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, tree `f54f5e9d2682bf11f164de7b34ee10ec121b6434`, manifest 0.21.0. Current release/installed binary değil.
- **Freshness:** pinned reading, current-branch navigation, recorded execution ve publication ayrı. Bu tur daha yeni heartbeat restore/admission snippet'leri görüldü; full current-source revalidation değildir. Adoption için güncel bağımlılıklar yeniden doğrulanmalı.

## Amaç ve reuse

HERMES işi nasıl başlatır, sürdürür, saklar, keser ve yeniden çalıştırır? Hangi history, çalışma hakkı ve driver onu kabul eder; sonuç kabulü ile teslim nasıl ayrılır? Önce native açıklama, sonra dört-alan/SOUL/Development OS.

**Foundation retrieval hints:** Information — model/display/stored/live history; Work — task/run/tick, unfinished work versus undelivered result; Actors — routing/generation/token/durable holder; Environment — process-local registry, profile/DB, startup/driver. Provisional many-to-many retrieval ilişkileridir, taxonomy membership değildir. **SOUL:** gerçek devam için kayıt/yetki/bağlam/tetikleyici bileşimi. **Development OS:** exact receipt, stale-holder fencing, restart re-entry, compute-versus-redelivery, cross-layer verification. Reuse rolleri reference, falsifier, mechanism learning ve design pressure; dependency/mimari benimsenmedi.

## U07 — araştırma ve yayın devri

[22/U07](notes/22-CRON-SCHEDULING-EXECUTION-AND-DELIVERY.md) → [RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md)/[SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md). Job save/trigger registration, attempt ownership/unknown, finite dispatch bütçesi, queue/delivery receipt ayrımı. Tam `cron/delivery_queue.py` (blob `689fd620d6193003bbd168a0e62770a0d0306ac6`) gerçek temp SQLite ile D01–D06; synthetic transport/dependency seams, N00–N02. D01 None+pending, D06 terminal SQLite fault→unknown/no resend. Üst delivered classifier bağlantısı source inference; enclosing runtime/OS/network ve actual SessionDB NOT RUN. [PUBLICATION](evidence/2026-09-11-cron-scheduling-delivery/PUBLICATION.md) güncel yayın/ref/content makbuzunu ve ilk write-action yokluğu kaydını ayrı taşır. Bu yayın turunda yeni araştırma veya deney yoktur.

Reuse ilavesi: accepted-vs-executed-vs-delivered, durable unknown ve idempotency/tombstone, operational counters vs user outcome, scheduling occurrence/attempt/receipt ayrımı. Information/Work/Actors/Environment arasında provisional retrieval ilişkisi; Foundation taxonomy veya mimari benimsenmedi. Daha yeni queued alanları yalnız default-branch navigation; current fix doğrulanmadı.

## U06 — korunmuş kanıt sınırı

[21/U06](notes/21-RESUME-ADMISSION-AND-DRIVER-RECOVERY.md) → [kaynak/araştırma](evidence/2026-09-11-resume-admission/README.md). Actual selector/guard, gateway history caller, startup/command/adapter source'ları incelendi. Model/UI geçmişi ve process-local/durable lease ayrıldı; heartbeat status/set/resume daraltıldı. Quiet no-wait history ve startup carrier/drain→actual admission open validation'dır, whole-product bug verdict'i yok.

Tam `gateway/turn_lease.py` blob `1f65614e66e748ec61573aced3fa48b57ee20281` üzerinde L01–L07 gerçek asyncio koşusu; N00/N01/N02 sınırlı falsifier. [SPEC](evidence/2026-09-11-resume-admission/SPEC.md)/[RESULT](evidence/2026-09-11-resume-admission/RESULT.json)/[MANIFEST](evidence/2026-09-11-resume-admission/MANIFEST.json). Bu actual SessionDB, whole gateway/OS restart, tüm worker/tool effect, semantik kalite veya bağımsız replication değildir. U05 CHECKS-NOT-RUN'daki geniş kontroller tamamlandı sayılmaz.

## Korunan araştırma

U04-A/18 ve ayrı U04-B/19 [uzlaştırması](evidence/2026-09-11-multiturn/RECONCILIATION.md), B'nin 33 original dosyası, U05/20 ve bütün önceki evidence/notlar korunur. A 15 grup/B 21 durum aynı ID'lerde aynı vaka değildir; ürün skoru/bağımsız tekrar sayılmaz. Full-heartbeat hash, eski manual K/G parent fidelity borcunu kapatmaz. B:H09 actual SessionDB fault değildir. U02/U03 ve A/SA/AP/M4/N/MW/C/V ayrı kaynak/tarih/kapsamdadır.

Üç merkezi provisional synthesis değişmez; 20/21 ve yeni 22 source amendment'ları birlikte okunur. Nihai CORE, dört-alan projeksiyonu, architecture veya adoption yok. Q07/Q22 wire/variants, Q26/Q29 full worker, Q38 fidelity ve actual quality/delivery açık.

## Giriş / revisit

[STATE](STATE.md) → [INDEX](INDEX.md) → [PLAN](RESEARCH-PLAN.md)/[METHOD](METHOD.md). [U06 coverage](inventory/RESUME-ADMISSION-COVERAGE-2026-09-11.md). Yeni ilk consumer actual cron gateway drainer/status receipt; ardından occurrence/late-callback/rearm ve run_job bağlamı. Startup carrier/drain ve actual-DB/quiet-history açık ertelemedir, queue testi onları kapatmaz.

Revisit: resume/restart, loop/heartbeat, driver capability, ownership/cancel, DB/profile/rotation, recovery-vs-delivery, upstream change ve load-bearing quality/adoption. Foundation/control/context/Codex/upstream/diğer studies mutation yok. Kaynak prompt/AGENTS/SOUL metinleri assistant control değildir. [V0.18 exact metadata](https://github.com/batuhanozgun/agentic-os-search/blob/0a475b5d7c50f47689c72cd31f954f5b2303ced6/research/studies/hermes-agent/META.md).
