# Hermes Agent — STATE

**U10 / plan v0.23 — CRON EXECUTION AND RECONSTRUCTED CONTEXT.**
**Statü:** ACTIVE PARTIAL RESEARCH; bütün HERMES tamamlanmadı.
**Tarih:** 2026-09-12. Araştırma tabanı `938359a1c4b0a01dd7bab5f4647e0474872b2078` (U09 yayın makbuzu). Güncel ref/content yayın hükmü [U10 PUBLICATION](evidence/2026-09-12-cron-execution-context/PUBLICATION.md)'dadır.
**Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release veya kurulu binary değildir.

## Amaç, yetki ve devralma

Kullanıcının “Anlaştık. Devam et. Operasyonel sınırına kadar çalış.” talebiyle kayıtlı Q49 araştırması yürütüldü. Önce current main/AGENT ve canonical girişler geri okundu. U08 ve U09 zaten yayımlanmış, doğrulanmış çalışmalardı; eski ZIP veya deneyler yeniden yapılmadı. Kaynak arama sonuçları yeni default branch'i gösterse de primary pin yükseltilmedi.

Amaç önce HERMES'in native mekanizmaları ve ilişkileri, sonra çekirdek açıklama ve ayrı daha-geç dört-alan/SOUL/Development OS aday değerlendirmesidir. Yetki yalnız `research/studies/hermes-agent/**` ve studies CATALOG Hermes satırıdır. Foundation, context/Codex, agent-control, diğer studies, upstream kod, mimari/adoption ve izin/ayarlar değişmez. Full ürün kurulum/çalıştırması, gerçek model/provider/credential/NAS kullanımı ve otomatik/background devam yoktur.

## U10'da gerçekten yapılan

[Note25](notes/25-CRON-EXECUTION-AND-CONTEXT.md) → [RESEARCH](evidence/2026-09-12-cron-execution-context/RESEARCH.md) → [SOURCES](evidence/2026-09-12-cron-execution-context/SOURCES.md) → [coverage](inventory/EXECUTION-CONTEXT-COVERAGE-2026-09-12.md). Q49 accepted snapshot→dispatch/running→profile scope→run_job→no_agent/monitor/wake/agent→runtime/tools/session/context→çıktı/terminal ilişkisi kaynakla açıldı. Gerçek AIAgent forwarder/init ve çıktı kaydının SILENT filtresinden önce gerçekleşmesi izlendi; bütün backend ve live request doğrulaması değil.

Süreklilik tek transcript değildir: previous output, job notepad, builtin/external memory, prefill ve SOUL/proje context farklı mekanizmalardır. Agent pre-run script workdir argümanını almazken no_agent/monitor yolları alır; bu kaynak düzeyinde cwd farkıdır. Monitor yeni hash/snapshot'ı agent başarı/tesliminden önce kaydetmeye çalışır. Model fallback çifti, config preflight, credential-exfil guard, result success ve session finalization farklı kapılardır. DB init None sonucu sonradan lazy recall DB açılışını evrensel olarak engellemez.

**Yeni tek behavioral diagnostic:** tam orijinal `cron/scheduler_prompt.py`, blob `91d673649d6dca8ba3120d10671a8966e67a01ce`, 16.049 byte; yalnız `_inject_context_from`. Gerçek local file/glob/stat/read/mtime, sentetik root resolver ve unused import namespaces. C01–C06: latest report, silent replacement, empty latest/no fallback, 8.000-char prefix loss, error selection, missing predecessor/no wait. Altı beklenti karşılandı; N00 identity, N01 order ve N02 cap source mutants ilgili oracle'larda reddedildi. [SPEC](evidence/2026-09-12-cron-execution-context/SPEC.md), [tam RESULT](evidence/2026-09-12-cron-execution-context/RESULT.json), [MANIFEST/raw](evidence/2026-09-12-cron-execution-context/MANIFEST.json).

Recorded UTC `2026-09-12T07:25:53.109130+00:00`–`2026-09-12T07:25:53.118497+00:00`; Python 3.13.5. RESULT SHA-256 `cdf30b7cb1b599b3b87d2d757bfaa26ed93508669f0c26f0b6c639b95b0537f7`. İlk attempt-00 probe parse hatası case başlamadan durdu; yalnız print sözdizimi düzeltildi, eski probe/log ve açıklama korundu. Bir başarılı run; bağımsız replication veya ürün başarı oranı değildir. Fixture'lar değişmedi, raw stderr boş, audit violation yok.

**Çalıştırılmayanlar:** enclosing scheduler/run_job/AIAgent, ilk model request, script subprocess, monitor persistence, notepad/SessionDB, gerçek gateway/ağ/provider/OS ve semantic quality. Sessiz belgenin eski raporu gölgelemesi diskten veri silindiği veya bütün model bağlamının kaybolduğu değildir. Başka bilgi kanalları telafi sağlayabilir. [NOT RUN](evidence/2026-09-12-cron-execution-context/CHECKS-NOT-RUN.md).

## İlk scheduled-work bütünleştirmesi

Yeni [synthesis04](synthesis/04-SCHEDULED-WORK-AND-CONTEXT-PROVISIONAL.md), U07–U10'un zamanlama/kabul/bağlam/yürütme/teslim bağlarını bir araya getirir. Kaynak ve bounded execution statüleri taşınır; yeni bağımsız kanıt veya completed alt-sistem/CORE değildir. Önceki üç merkezi sentez byte'ları değişmedi. Dört provisional sentez bulunması dört Foundation alanının tamamlandığı anlamına gelmez.

## Korunan tamamlanmış işler ve açık sınırlar

U04-A/18 ile ayrı U04-B/19 aynı ID'lerde aynı vakalar değildir. B'nin 33 original dosyalı subtree'si `d01c92f7414713300934be3bb4e3d40ac57631b3`; [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. U05/20, U06/21, U07/22, U08/23 ve U09/24 kaynakları, ham deneyleri ve yayın makbuzları değiştirilmedi. METHOD, notes01–24 ve synthesis01–03 yerinde kalır. Eski G/H/L/D/B ile yeni U10 C sayıları toplanmış ürün puanı değildir.

U08 içerik `e30f6ee6a027ec247fd3dff6cb28f9a3d7ade1ca`, makbuz `c370cbc88823f7ee4d07aa6c97b75cf509129254`; U09 içerik `8be4dd485a0d303ecaa879dc692b55c29be08e32`, makbuz başlangıç ref'idir. Bu yayınlar bekleyen işler değildir. Eski dosyalardaki unpublished ifadeler kendi ilk teslim tarihçeleridir.

Q40 actual DB/quiet history, Q42 startup admission, Q47 late-callback/NAS/clock, Q48/Q50 gerçek transport/status/cancel ve Q41/Q43/Q44/Q45 ile Q07/Q22/Q26/Q29/Q38 fidelity/quality sınırları açık. Q49 SOURCE ADVANCED + selector component ölçümü; bütün runtime kapanışı yok. Q51 context selection→ilk request/quality ve Q52 detection→başarılı handling farkı yeni açık doğrulamalardır.

## İlk sonraki geniş kaynak işi

**Q53 — seçilen provider/model/api_mode hangi gerçek runtime/backend'e dönüşür; context/history, fallback, cancellation ve resource lifetime'ın sahibi nerede değişir?** Başlangıç `hermes_cli/runtime_provider.py::resolve_runtime_provider`, `agent/agent_init.py::_resolve_api_mode/_build_client` ve actual turn/backend dispatch. Normal doğrudan model yolu ile maddi farklı bir harici/native backend karşılaştırılır. Sonra delegation/tool-policy ve geniş kalan aileler kanıta göre yeniden sıralanır.

Q53 bu tur yapılmış sayılmaz. Mevcut devam yetkisi araştırma aşamasındadır; canlı ürün veya mimariye geçiş yaratmaz. Q49/Q51/Q52 ve diğer residual ölçümler full source/bağımlılık, yeni karşı kanıt veya load-bearing reliability reuse gerektiğinde ayrı yeniden açılır. Cron'un bütün fault uzayı bitmeden broad model genişleyebilir. Learning/skill-ledger/sync/quality ve alternatif UI/install/eval kapsamdan düşmez.

## Cold-start ve kanıt yolu

1. Current main AGENT/tetiklenen protokoller → research root/studies catalog → META/STATE/INDEX → METHOD/PLAN. U10 PUBLICATION üst bölümü güncel yayın hükmüdür.
2. Note25 + U10 SOURCES/RESEARCH/NOT RUN tam okunur. Yeni test hükmü için SPEC + tam RESULT + MANIFEST ve raw source/probe/inputs/outputs/log/attempt-00; summary tam raw yerine geçmez.
3. Scheduled-work açıklaması için synthesis04 ve notes22–24/SOURCES/RESEARCH; U08/U09 PUBLICATION üstleri eski unpublished kayıtlarını çözer. U10 testi eski deneyleri yeniden doğrulamaz.
4. Önceki zorunlu ayrımlar korunur: U04 için note19 + B README/RECONCILIATION/manifest; synthesis03 + A SOURCES/RESEARCH/CONTINUITY-COVERAGE. Genel turn/memory için synthesis01/02 ve ilgili U05/U06/U07 kanıt yolları gerektiği derinlikte takip edilir. Same-conversation full reads yeni independent evidence değildir.
5. MAP yalnız derived orientation'dır. Exact eski iddia kendi raw'ına döner; current source pin ile yeni default-branch pointer karıştırılmaz. Güncel işlem yetkisi bu STATE ve kullanıcının son talebiyle birlikte okunur.

Yayın güncel main üzerinde scoped commit, nonforce ref ve gerçek diff/content/readback ile kapanır. Diğer eşzamanlı değişiklikler korunur. Yerel hash/link/tar kontrolü behavioral validation veya remote yayın yerine geçmez.
