# Hermes Agent — Araştırma metaverisi

- **ID / type:** hermes-agent / external-target.
- **Nesne:** Nous Research Hermes Agent'ın ajan çalıştırma, kalıcı bilgi/iş, oturum, scheduler ve kullanıcı yüzeyleri.
- **Statü:** ACTIVE PARTIAL RESEARCH; U09 / plan v0.22. Current work/completion authority [STATE](STATE.md); U09 [yayın makbuzu](evidence/2026-09-12-cron-occurrence-admission/PUBLICATION.md). U08 yayını tamamlandı.
- **Tarih:** başlangıç 2026-09-07; son kayıt 2026-09-12.
- **Primary:** NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a; tree f54f5e9d2682bf11f164de7b34ee10ec121b6434; manifest 0.21.0. Current release/installed binary değil.

## Ana soru ve yöntem

HERMES ajanı ve işi nasıl başlatır, sürdürür, değiştirir, keser ve yeniden kabul eder? Hangi bilgi/hak/driver/sonuç kaydı gerçekten kullanılır? Önce native mekanizma ve sistem açıklaması, sonra dört-alan ve SOUL/Development OS aday değerlendirmesi. [METHOD](METHOD.md), [PLAN](RESEARCH-PLAN.md), [MAP](CURRENT-RESEARCH-MAP.md).

## U09'un eklediği ve kanıt sınırı

[24/U09](notes/24-CRON-OCCURRENCE-AND-FIRE-ADMISSION.md) → [RESEARCH/SOURCES](evidence/2026-09-12-cron-occurrence-admission/README.md). Outbound job+fire_at provisioning ile inbound job-only claim ayrıldı; gerçek generic store/runnable/fence/finish yardımcıları, hosted forwarder, API split/legacy admission ve due-scan/rearm okundu. Tamamlanma-sonrası dedup hakkındaki wire iddiasıyla kod arasındaki fark source-conditioned trace olarak açıklandı.

**U09 yeni execution içermez.** Test kaynakları mocked handler-order oracle'larıdır; gerçek NAS/store/late duplicate, crypto, full worker veya network sonucu ölçülmedi. Q47 kaynak olarak ilerledi; daha güçlü doğrulama açık. Sonraki geniş source Q49 run_job/script/no_agent/monitor/agent/context'tir.

## Yeniden kullanım rolleri

**Information:** planlanan zaman, taşınan payload, job özeti ve HTTP makbuzu arasında temsil/kimlik kaybı; geçmişi göstermek ile gerçek bağlamı kullanmak ayrımı. **Work:** job/occurrence/execution/tick/completion/delivery; active exclusion ile historical dedup farkı. **Actors:** token, holder, routing/generation, claim ve phase yetkisi. **Environment:** profile-local stores, process-local/durable locks, scheduler/gateway/adapter kabiliyeti. Bunlar many-to-many provisional retrieval hints'tir; Foundation taxonomy membership değildir.

**SOUL aday değeri:** kalıcı işi doğru kimlik, geçmiş, yetki ve tetikleyiciyle yeniden kurmanın somut dış örnekleri. **Development OS aday değeri:** exact receipt, stale-owner/occurrence sınırları, phase admission, cancellation/transport effect ayrımı, cross-layer doğrulama ve yanlış proxy testlerine karşı örnekler. Reuse rolleri reference/falsifier/mechanism learning/design pressure; dependency veya architecture benimsenmedi.

## Korunan birikim ve freshness

U04-A/B, U05, U06 L, U07 D ve U08 B source/deney kayıtları ayrı ve korunmuştur; sayı toplamı bağımsız tekrar veya ürün skoru değildir. Notes01–23/evidence/METHOD/synthesis01–03 değiştirilmedi; note24 yeni source amendment'tır. Eski raw hash/statü zinciri [exact v0.21 META](https://github.com/batuhanozgun/agentic-os-search/blob/c370cbc88823f7ee4d07aa6c97b75cf509129254/research/studies/hermes-agent/META.md) ve [SOURCE-LEDGER](SOURCE-LEDGER.md)'dadır.

Default search a84a2223f82c3d9906fd4a9d778a188774e7a08e üzerindeki daha yeni occurrence/manual sembollerini yalnız navigation olarak verdi. Current fix doğrulanmadı; adoption öncesi güncel kaynak/bağımlılık/çalışan ortam yeniden doğrulanmalıdır. Q40/Q42/Q48/Q50 ve Q07/Q22/Q26/Q29/Q38 eski sınırlar bu source birimiyle kapanmaz.

Revisit: scheduler/admission/occurrence, restart/retry, callback/receipt, profile/ownership, upstream change ve güçlü reliability/adoption ihtiyacı. [STATE](STATE.md) → [INDEX](INDEX.md) → ilgili evidence. Foundation/control/context/Codex/upstream/diğer studies mutation veya final CORE/dört-alan/adoption yoktur.
