# Hermes Agent — Araştırma planı

**v0.21 / 2026-09-12 — U08 actual drainer/status source + native async-bridge diagnostic.** Current work [STATE](STATE.md), yöntem [METHOD](METHOD.md), derived overview [CURRENT-RESEARCH-MAP](CURRENT-RESEARCH-MAP.md). Yayın durumu [PUBLICATION](evidence/2026-09-12-cron-drain-receipts/PUBLICATION.md). U08 teknik araştırması U07/v0.20 tabanında yapıldı. Bu yayın checkpoint'inin tabanı `4c372138b7d652b1921e96ef9158b32b05c05fc8`; Foundation değişiklikleri korunur. [V0.20 exact plan](https://github.com/batuhanozgun/agentic-os-search/blob/188095b930ac77f8d2a5dd605191a09a369a57ce/research/studies/hermes-agent/RESEARCH-PLAN.md).

## Hedef ve elde olan

Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0. Önce HERMES-native açıklama, sonra alt-sistem ilişkileri/çekirdek model, daha sonra dört-alan ve SOUL/Development OS aday değerlendirmesi. Bütün araştırma ACTIVE PARTIAL. Üç merkezi provisional synthesis korunur; yeni map ve note23 dördüncü completed model değildir.

U07'nin Q48/Q46 first-next source hedefi yürütüldü: startup running gate→bağımsız housekeeping thread→profile/adapter scope→actual queue callback; hesaplama/delivery_error→job last status→latest execution join→cron CLI görünümü. Scope source seviyesidir, full-host/real transport değildir.

Actual live-send helper'daki timeout/cancel yorumu tam native async bridge ile sınandı. B01 normal receipt, B02 effect-before-cancel True, B03 timeout-to-error cancel False. Bu bridge'in iptal boolean'ı transport-effect makbuzu değil. Gerçek kanal duplicate ölçümü, enclosing scheduler/worker/CLI koşusu veya upstream düzeltme yok. [Note23](notes/23-CRON-DRAIN-RECEIPTS-AND-CANCELLATION.md), [RESEARCH](evidence/2026-09-12-cron-drain-receipts/RESEARCH.md), [SPEC/RESULT](evidence/2026-09-12-cron-drain-receipts/README.md).

## İlk yeni source birimi — Q47

**Soru:** job ID, planlanmış occurrence, external callback, fire claim ve gerçek execution ID hangi geçişlerde ayrılır? Aynı job'ın ikinci çalışmasıyla aynı occurrence'ın ikinci kez yürütülmesini ayırt eden gerçek anahtar/koşul nedir?

Başlangıç: U07 scheduler_provider.claim_fire/fire_due/fire_claimed, jobs.claim_job_for_fire/get_due_jobs/advance/rearm ve gerçek external callback consumer'ı. Normal scheduled fire, gecikmiş callback ve explicit manual/force yolunu karıştırma. Native callback kimliği/payload'ı/owner/next-run güncellemesini kaynakla takip et; job ID üzerinde sıraya alma ile occurrence idempotency'sini eşitleme. Due değerinin ilerletilmesi tek başına tam exactly-once kanıtı değildir.

Çıkış: normal bir occurrence ile late/duplicate callback yolunun hangi koşulda kabul veya reddedildiğini, hangi kaydın önce yazıldığını ve failure/defer sonucunu kaynaklarıyla açıklayabilmek. Gerekli kaynak/bağımlılık varsa güvenli bounded diagnostic olabilir; sırf test sayısını artırmak için önceki B/D/L fixture'ları çoğaltılmaz. U07 600s/120s karşılaştırması ordinary/config/force yolları bağlanmadan tüm ürün bug'ı diye sunulmaz.

## Sonraki geniş birim — Q49

Shared run_job içinde script/no_agent/monitor/agent/preflight ayrımı; scheduled iş kimliğinin model/provider, toolset, cwd/profile, session/history ve persistence'a çevrilmesi. Normal bir job ile ajan açmayan script yolu ayrı açıklanmalı. Provider/backend/delegation ailelerine çıkış buradan yeniden önceliklendirilir. Bütün dış plugin/model ekosistemini sınırsız araştırma kapsamına alma.

## Ayrı açık doğrulama hattı

Q48/Q50: actual enclosing live/standalone/relay transport receipt; worker queue timeout→late result→job/execution→CLI uzlaştırması; seeding ve profile/startup/shutdown. U08 source bridge açıklandı diye whole runtime kapanmaz. [CHECKS-NOT-RUN](evidence/2026-09-12-cron-drain-receipts/CHECKS-NOT-RUN.md) gerçek yapılmamış ölçümleri taşır.

Q40 actual SessionDB/quiet next-request, Q42 startup carrier/drain/actual admission, Q41 migration/profile, Q43 effects, Q44/Q45 semantic quality açık. Q07/Q22 wire/timing, Q26/Q29 full worker, Q38 selected-parent fidelity korunur. İlgili kaynak+bağımlılık erişimi, yeni karşı kanıt veya güçlü reliability/adoption reuse geldiğinde reopen. Bütün fault uzayının bitmesi broad source birimlerinin ön şartı değildir.

## Kapsam kontrolü ve kapanış

F01–F12 genel haritasındaki provider/profile/backend/delegation, tools/plugins, learning/ledger/sync/quality, UI/install/eval aileleri kaybolmaz. Bir dalın zengin test üretmesi onu araştırmanın ana amacı yapmaz. Yeni bounded birimden sonra büyük haritada hangi açıklama boşluğunun değiştiği değerlendirilir. Final CORE/dört-alan için büyük alanları varsayımla doldurma; dosya veya vaka sayısından yüzde tamamlama üretme.

## Yayın ve yetki

Kullanıcı önce U08 yayını ve geri okuması, ancak başarılı olursa kayıtlı araştırmaya devam sırasını onayladı. Bu checkpoint yalnız yayını kaydeder; Q47 henüz yeni araştırma sonucu değildir. Yalnız Hermes package + CATALOG Hermes satırı. Full product/model/provider/credential/izin ayarı/upstream/Foundation/control/context/Codex/diğer studies/architecture değişikliği yoktur. İlk teknik turdaki write-action yokluğu tarihsel PUBLICATION bölümünde korunur. Güncel yayın hükmü gerçek nonforce ref, scoped diff ve content readback üzerinden verilir. Eski U04–U07 yayınları ve raw deneyler yeniden yapılacak iş değildir.
