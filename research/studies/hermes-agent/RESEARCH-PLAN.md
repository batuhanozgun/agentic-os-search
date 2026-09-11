# Hermes Agent — Araştırma planı

**v0.20 / 2026-09-11 — U07 cron scheduling/execution/delivery.** [STATE](STATE.md) güncel durum/yetkiyi, [PUBLICATION](evidence/2026-09-11-cron-scheduling-delivery/PUBLICATION.md) yayın makbuzunu taşır. [V0.19 exact plan](https://github.com/batuhanozgun/agentic-os-search/blob/d928ee14b16a277c010a966816fc2c4097944aab/research/studies/hermes-agent/RESEARCH-PLAN.md) U06 tarihçesidir. Bu yayın checkpoint'inde önceki U07 araştırması kaydedilir; yeni teknik koşu yapılmaz.

## Hedef ve revizyon gerekçesi

Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0. Önce HERMES-native mekanizma/sistem açıklaması, sonra dört-alan/SOUL/Development OS. Bütün çalışma partial; üç merkezi synthesis korunur, note22 dördüncü completed model değildir.

U06 sonrası kullanıcı araştırmaya devam yetkisi verdi. İlk Q42 startup wrapper yeniden okundu, alt gateway/run.py 3150–3325 isteği 429 aldı. Full-host/actual-DB challenge kurulamadı; Q42 ve Q40 validation borcu açık tutuldu. V0.19'un açık erteleme kuralıyla F10 cron/scheduler→run→delivery araştırması başlatıldı. Böylece native broad model ilerledi, eski dar borç başka testle sahte kapanmadı.

## Yapılan U07 — yeniden yapılacak iş değil

[22](notes/22-CRON-SCHEDULING-EXECUTION-AND-DELIVERY.md), [RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md), [SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md), [coverage](inventory/CRON-COVERAGE-2026-09-11.md). Job/register, provider trigger/common run, recurring preadvance, finite one-shot dispatch counter, profile/jobs/fire fence, execution ledger/ownership/unknown, external-worker handoff ve output/delivery status zinciri kaynakla incelendi. Büyük modüller selected; actual run_job/context ve full store lifecycle kapanmadı.

Tam orijinal delivery_queue.py (blob `689fd620d6193003bbd168a0e62770a0d0306ac6`) gerçek temp SQLite ile D01–D06; N00–N02 dar identity/mutation kontrolleri. Native queue None/pending ile source-only üst delivered-classification bağlantısı ayrı etiketlendi. D06 gerçek SQLite trigger fault, actual SessionDB veya gateway/network/restart değildir. Attempt-00 pre-case metadata hatası korunur. Eski U04/U06 koşuları tekrar edilmedi.

## Bir sonraki bounded consumer hedefi

**Q48/Q46:** actual gateway `drain_delivery_queue` caller/launch/profile/transport ve job/execution/delivery status'unun gerçek tüketicisi. En az bir normal ve bir deferred/uncertain akışta exact execution ID, enqueue/claim, callback, terminal row, job outcome ve user-facing receipt ayrılmalı. None=no-error dönüşünü delivered diye varsayan veya testin kendi fake'iyle ürettiği acceptance kullanan harness yeterli değildir.

**Q47:** scheduled occurrence, late external callback, fresh fire claim ve next_run rearm ilişkisi. Same job ID dedup, same scheduled occurrence idempotency değildir. 10min backstop / 120s one-shot grace kesiti bir koşullu source sınırıdır; ordinary fire ve config varyantlarıyla birlikte okunmalı.

**Q49:** shared run_job içindeki script/no_agent/agent/preflight ve sonraki bağlam/persistence: scheduled task kimliği actual session/task/history'ye nasıl çevrilir? Provider/backend/delegation'e bağlanan yeni geniş açıklama boşluğu budur.

Önce mevcut özgün U07 teslimi recover edilir; publication gerekiyorsa testler yeniden koşulmaz. Aynı queue fault listesini veya U06 küçük registry'yi büyütmek gerçek caller açığını kapatmaz. Olası yeni koşu için tam source/bağımlılık sınırı, önceden sabit oracle ve gerçek receipt kaydı gerekir; model/provider/credential veya full product install yok.

## Erteleme ve geniş kapsam

Q40 actual SessionDB/quiet next-request, Q42 startup carrier/drain/actual admission, Q41 migration/profile, Q43 effects ve Q44/Q45 semantic kalite açık. Yeni altı queue vakası bunların yerine geçmez. Q07/Q22 wire/timing/variants, Q26/Q29 full worker ve Q38 selected-parent fidelity kapanmaz.

F01–F12 haritası korunur: provider/profile/backend/delegation, diğer UI/install/eval, memory/skill-ledger/sync/quality aileleri kaybolmaz. Source erişimi veya actual-host test sınırı broad araştırmayı sonsuza dek bloke etmez; ertelemenin adı ve yeniden açma koşulu STATE'te açık olur. Nihai CORE veya mimari/adoption aşamasına sıçranmaz.

## Yayın ve yetki

Yalnız Hermes study ve CATALOG HERMES row. U04-A/B, U05/U06 evidence/notlar, synthesis01–03 ve METHOD değişmez. İlk U07 teknik turunda write araçları sunulmadı; bu yeni gönderme isteğinde sunulan native write araçlarıyla scoped/nonforce yayın ve main/content/diff readback yapılır. Güncel makbuz PUBLICATION'dadır; ilk engel tarihsel olarak korunur. Bu yayın isteği yukarıdaki yeni teknik hedefleri otomatik yetkilendirmez. Mevcut snapshot tabanı `d928ee14b16a277c010a966816fc2c4097944aab`; head değişirse yeniden karşılaştırılır, force yapılmaz. Background çalışma veya izin ayarı değişikliği yoktur.
