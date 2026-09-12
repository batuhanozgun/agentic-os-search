# Hermes Agent — Araştırma planı

**v0.22 / 2026-09-12 — U09 occurrence/fire admission source study.** [STATE](STATE.md) yetki ve current work; [METHOD](METHOD.md) yöntem; [MAP](CURRENT-RESEARCH-MAP.md) derived büyük resim. [U09 publication](evidence/2026-09-12-cron-occurrence-admission/PUBLICATION.md). Primary c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a / manifest 0.21.0, current ürün hükmü değil.

## Revizyon gerekçesi ve yapılan

U08 bu tur önce yayımlandı/geri okundu; kullanıcı tarafından kabul edilen kapıdan sonra Q47 başlatıldı. [U08 makbuzu](evidence/2026-09-12-cron-drain-receipts/PUBLICATION.md), [eski exact v0.21 plan](https://github.com/batuhanozgun/agentic-os-search/blob/c370cbc88823f7ee4d07aa6c97b75cf509129254/research/studies/hermes-agent/RESEARCH-PLAN.md). U09 yeni source araştırmasıdır, eski deney veya yayın tekrarı değildir.

[24/U09](notes/24-CRON-OCCURRENCE-AND-FIRE-ADMISSION.md) → [RESEARCH/SOURCES](evidence/2026-09-12-cron-occurrence-admission/README.md). Provision iş+zaman anahtarı; dashboard→gateway job-only dönüş; split/legacy admission; gerçek load/_with_job/fence/runnable/claim; normal finish; due-scan/manual/rearm açıldı. Wire kontratındaki tamamlanma-sonrası dedup genellemesiyle kod arasındaki fark koşullu kaynak iziyle belirlendi.

**Yeni HERMES execution yok.** Gerçek late duplicate, NAS retry, store/process/clock/crypto ve tam worker sonucu gözlenmedi. Daha yeni default branch occurrence sembolleri pin yükseltmesi veya current fix doğrulaması değildir. Q47 bounded kaynak hedefi ilerledi, gerçek-runtime soruları açık.

## İlk yeni geniş source birimi — Q49

**Soru:** accepted scheduled snapshot, shared run_job içinde nasıl gerçek yürütme bağlamına dönüşüyor?

Başlangıç U07/U08 scheduler outer caller'dan run_job'a; script/no_agent/monitor/agent/preflight dalları. En az bir agent yolu ve ajan açmayan script yolu için iş/execution kimliği, profile ve cwd, model/provider seçimi, araç seti, session/history/context_from, sonuç ve persistence bağları izlenir. Source branch'i gerçekten kullanan caller aranır; constructor parametresi veya test fake'i runtime kabulü sayılmaz.

Çıkış ölçütü: bir scheduled işin hangi koşullarda model çağırdığı veya çağırmadığı, hangi bağlamla hangi worker'a geçtiği, başarısız ön kontrolün hangi kayıt/sonuca dönüştüğü ve açık kalan alt sınırların yeri açıklanabilir olmalı. Tam dış provider ekosistemi, bütün modeller veya bütün platform kombinasyonları araştırmanın otomatik kapsamı değildir. Full product/credential/model çağrısı yoktur. Kaynak/bağımlılıklar izin verirse yalnız gerekli, güvenli ve önceden ölçütlenmiş bounded diagnostic yapılır; test sayısı kotası yoktur.

## Ayrı doğrulama hattı

Q47: gerçek normal finish sonrasında late-callback claim, occurrence generation, re-arm/live claim, NAS arm replacement/retry ve HTTP receipt. [U09 NOT RUN](evidence/2026-09-12-cron-occurrence-admission/CHECKS-NOT-RUN.md). Q48/Q50: actual transport/queue/status/cancel/seeding/profile; [U08 NOT RUN](evidence/2026-09-12-cron-drain-receipts/CHECKS-NOT-RUN.md). Q40/Q42: actual SessionDB quiet-history ve startup preclaim/carrier/drain/agent kabulü.

Bütün bu hata uzayı bitmeden broad kaynak açıklaması durdurulmaz. İlgili full-source/bağımlılık erişimi, yeni karşı kanıt veya güçlü reliability/adoption yeniden kullanımı gerektiğinde ölçüm yeniden açılır. Q41/Q43/Q44/Q45 ve eski Q07/Q22/Q26/Q29/Q38 sınırları aynı statüde korunur.

## Büyük resim ve yetki

Önce native mekanizmalar→alt-sistemler→ilişkiler→çekirdek açıklama; daha sonra dört-alan/SOUL/Development OS aday değerlendirmesi. Provider/backend/delegation, tools/plugins, learning/ledger/sync/quality, diğer UI/install/eval aileleri haritada kalır. Üç mevcut sentez provisional'dır. Tek bir dalı sonsuz testle büyütmek veya büyük alanları varsayımla doldurup CORE üretmek uygun değildir.

Yalnız Hermes package + CATALOG Hermes satırı. U04–U08 evidence/notes, METHOD ve synthesis01–03 değişmez. Foundation/control/context/Codex/upstream/diğer studies/architecture/adoption veya izin ayarı değişmez. Scoped güncel main/nonforce/ref-content-diff doğrulaması yayın koşuludur; yayın testi davranış testi değildir.
