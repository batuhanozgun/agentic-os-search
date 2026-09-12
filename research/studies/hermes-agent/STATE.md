# Hermes Agent — STATE

**U09 / plan v0.22 — CRON OCCURRENCE AND FIRE ADMISSION.**
**Statü:** ACTIVE PARTIAL RESEARCH; bütün HERMES tamamlanmadı.
**2026-09-12.** U08 yayını tamamlandı ve doğrulandı; ardından Q47 source birimi yürütüldü. U09'un gerçek ref/content yayın hükmü [PUBLICATION](evidence/2026-09-12-cron-occurrence-admission/PUBLICATION.md)'dadır.
**Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release/kurulu binary değil.
**U09 tabanı:** `c370cbc88823f7ee4d07aa6c97b75cf509129254`.

## Amaç, yetki ve ilk kapının gerçek kapanışı

Kullanıcı önce U08'in yayımlanmasını, geri okunmasını, ancak başarıdan sonra kayıtlı araştırmanın sürdürülmesini onayladı. Bu tur native write eylemleri sunuldu; neden değiştikleri teşhis edilmedi. U08 içerik `e30f6ee6a027ec247fd3dff6cb28f9a3d7ade1ca`, yayın makbuzu `c370cbc88823f7ee4d07aa6c97b75cf509129254`. Gerçek main, scoped diff ve içerik geri okuması doğrulandıktan sonra Q47 başlatıldı. U08 artık bekleyen ZIP değildir; önceki unpublished/capability metinleri tarihsel kayıtlardır. [U08 makbuzu](evidence/2026-09-12-cron-drain-receipts/PUBLICATION.md).

U08 yayını, başlangıç main `4c372138b7d652b1921e96ef9158b32b05c05fc8` içindeki iki Foundation commit'ini korudu. Onlar bu tur oluşturulmadı ve herhangi bir aktöre atfedilmedi. U08 kaynak/deneyleri yeniden koşulmadı. U09 yeni kaynak araştırmasıdır; U08 yayın doğrulaması yeni teknik test gibi sayılmaz.

Amaç önce HERMES-native mekanizma ve sistem açıklaması, sonra ilişkiler/çekirdek model ve daha sonraki dört-alan/SOUL/Development OS aday değerlendirmesidir. Yalnız `research/studies/hermes-agent/**` ve CATALOG Hermes satırı değişebilir. Foundation, context/Codex, agent-control, diğer studies, upstream kodu, mimari/adoption, izin/ayar, credentials/provider/model ve full ürün kurulum/çalıştırması kapsam dışı. Otomatik/background çalışma yoktur.

## U09 — gerçekten yapılan

[24 — Occurrence ve kabul](notes/24-CRON-OCCURRENCE-AND-FIRE-ADMISSION.md) → [RESEARCH](evidence/2026-09-12-cron-occurrence-admission/RESEARCH.md) → [SOURCES](evidence/2026-09-12-cron-occurrence-admission/SOURCES.md). [MAP](CURRENT-RESEARCH-MAP.md) derived orientation, [PLAN](RESEARCH-PLAN.md) sıra, [INDEX](INDEX.md) retrieval içindir; current work authority bu dosyadır.

Kaynak zinciri: Chronos job+fire_at provision/dedup key → hosted dashboard profile/forward → API adapter token/admission → provider claim/execution snapshot → jobs active-owner/runnable/fence → normal finish/claim clear → next-run/re-arm. Built-in due-scan ve explicit manual/force yolları ayrıldı. Gerçek _with_job/load/runnable/fence yardımcıları incelenerek kabuldeki zaman koşulunun varsayılmadığı kontrol edildi.

**Yük taşıyan bulgu:** dışarı gönderilen job+zaman anahtarı, dönüşte yalnız job ID'ye daralıyor. Claim, live-owner ve iş durumunu kontrol ediyor; next_run_at <= now veya expected occurrence karşılaştırması bu actual claim yolunda yok. Normal bitiş claim'i temizleyip recurring işi runnable bırakınca geçerli eski tetiklemenin yeni claim alabilmesi koşullu source iziyle açıklanıyor. Wire belgesindeki tamamlanma-sonrası ret genellemesi bu kodla desteklenmiyor. Bu gözlenmiş üretim duplicate veya gerçek ikinci worker/araç etkisi değildir. Dış NAS'ın stale relay/dedup davranışı, canlı claim/terminal/pause retleri ve sonraki worker kontrolleri ayrı sınırdır.

HTTP 202 split provider'da claim dönüşünü bekler; legacy tek-aşama yolunda aynı işaret background fire_due devri olabilir. 200 duplicate, None'a dönüşen farklı ret nedenlerini kapsayabilir. Dashboard 200 gateway_stopped operator-stop nedeniyle retry'ı keser; çalışma/teslim başarısı değildir. Rearm_oneshot aynı job ID'sinde yeni zaman/bütçe kurar, canlı claim üzerine yazmayı reddeder. Built-in due-scan zaman kapısı direct external claim'e otomatik taşınmaz.

**Yeni execution: YOK.** U09 source-only'dir; gerçek API/store/NAS/token/OS/model, upstream test suite veya eski diagnostic'ler çalıştırılmadı. Test kaynakları mocked provider'larla handler sırasını sınar; gerçek occurrence persistence kanıtı gibi kullanılmadı. Büyük parent full-byte/bağımlılık kurulamadığından kopya/fake kabul mekanizmasıyla sahte runtime kapanışı yapılmadı. [CHECKS-NOT-RUN](evidence/2026-09-12-cron-occurrence-admission/CHECKS-NOT-RUN.md). Source-only birim için RESULT veya ham koşu arşivi uydurulmadı.

## Açık doğrulamalar ve güncellik

Q47 SOURCE ADVANCED, gerçek late-callback/store/process/NAS/clock/fault ve re-arm yarışları NOT RUN. Q49 source araştırması henüz yapılmadı. Q40 actual SessionDB/quiet next-request, Q42 startup admission ve Q48/Q50 actual transport/status/cancel/seeding doğrulamaları açık/ertelenmiştir. Q41 migration/profile, Q43 full-worker/effects, Q44/Q45 semantic quality, Q07/Q22 wire, Q26/Q29 full worker ve Q38 manual selected-parent fidelity korunur. Erteleme kapanış değildir.

Default search daha yeni `a84a2223f82c3d9906fd4a9d778a188774e7a08e` üzerinde occurrence/manual/test pointer'ları verdi. Bunlar navigation/freshness uyarısıdır; current fix revalidation veya pin yükseltmesi yapılmadı. Raw download/urllib DNS sınırı büyük parent materyalizasyonunu engelledi; pinned connector range okumaları ise çalıştı. Source erişimi, runtime ve publication birbirine karıştırılmaz.

## Korunan araştırma ve yayınlar

Notes01–23, bütün U04–U08 ve daha eski evidence, METHOD, merkezi synthesis01–03 değişmedi. U04-A/18 ve ayrı U04-B/19 eş numaralarda aynı deney değildir; B'nin 33 original dosyalı subtree'si `d01c92f7414713300934be3bb4e3d40ac57631b3` ve [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. U05/20, U06/21, U07/22 ve U08/23 bitmiş yayınlardır, yeniden yapılacak işler değildir. Eski G/H/L/D/B sayıları bağımsız replication veya ürün skoru olarak toplanmaz.

Üç merkezi synthesis provisional'dır; 20–24 ek notlarla birlikte okunur. Yeni final CORE, dördüncü completed model, Foundation taxonomy veya benimsenmiş architecture yoktur. Önceki current state'in tam metni ve raw kimlikleri [v0.21 exact STATE](https://github.com/batuhanozgun/agentic-os-search/blob/c370cbc88823f7ee4d07aa6c97b75cf509129254/research/studies/hermes-agent/STATE.md)'ten geri kazanılabilir.

## İlk sonraki iş

**Q49 — kabul edilmiş scheduled snapshot shared run_job'da hangi betik/no_agent/monitor/agent yoluna, hangi profile/model/tools/cwd/session/history'ye dönüşüyor?** Normal agent ve ajan açmayan script yolu ayrı kaynak zincirleri olarak izlenir. Q47'nin gerçek-runtime borcunu bitirmek bu yeni geniş açıklamanın ön koşulu değildir; tam kaynak/bağımlılık veya güçlü reliability/adoption ihtiyacı doğunca ayrı doğrulama hattı yeniden açılır.

Provider/backend/delegation, learning/skill-ledger/sync/quality, diğer UI/install/eval aileleri geniş haritada korunur. Araştırma sadece cron hataları aramaya indirgenmez. Current turn yetkisi yayın sonrası kayıtlı araştırmayı sürdürmektir; yeni mimari veya canlı ürün çalışma aşamasına geçiş yetkisi değildir.

## Cold-start ve kanıt yolu

1. Güncel main AGENT ve tetiklenen protokoller → research root/studies catalog → META/STATE/INDEX → METHOD/plan. Aynı konuşmada tam okunmuş kontrol sürümleri değişmediyse geçerlidir; yeni oturum canonical bootstrap yapar.
2. U08 ve U09 PUBLICATION üst bölümleriyle gerçek yayın durumunu ayır. Eski unpublished metinler güncel engel değildir. U09 note24 + SOURCES/RESEARCH/NOT RUN tam okunur; source T0–T4 bir runtime sonucu değildir.
3. U08 note23/SOURCES/RESEARCH/coverage, U07 note22/SOURCES/RESEARCH/coverage, U06 note21 ve U05 note20 ilgili kaynak/coverage yolları korunur; eski first-next cümleleri tarihsel sıralarıyla okunur.
4. U04 ayrımı için note19 + B README/RECONCILIATION/manifest; üst açıklama için synthesis03 + U04-A SOURCES/RESEARCH/CONTINUITY-COVERAGE zorunlu eski yol korunur. Gerektiğinde synthesis01/02 ile genel modeli geri kazan.
5. Exact eski execution iddiası için ilgili SPEC + tam RESULT + MANIFEST + source/probe/raw arşiv; U08'in B, U07'nin D, U06'nın L ve A/B kimlikleri karıştırılmaz. U09'da execution yoktur. Derived MAP/catalog raw kanıtın yerine geçmez.

Yayın güncel main tabanında scoped commit, nonforce ref ve gerçek main/diff/content geri okumasıyla kapanır. Sonuç U09 PUBLICATION'dadır. Kaynak incelemesinin kaydı, canlı davranış güvencesi değildir.
