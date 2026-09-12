# Hermes Agent — STATE

**U08 / plan v0.21 — CRON DRAIN RECEIPTS AND CANCELLATION.**
**Araştırma başlangıcı:** `188095b930ac77f8d2a5dd605191a09a369a57ce`; orada U07 / v0.20 yayımlıdır.
**Yayın tabanı:** `4c372138b7d652b1921e96ef9158b32b05c05fc8`; U07 tabanından sonraki iki Foundation commit’i korunur. HERMES/CATALOG/control değişmedi.
**Araştırma:** ACTIVE PARTIAL RESEARCH; bütün HERMES tamamlanmadı.
**Tarih:** 2026-09-12. Bu checkpoint özgün U08 tesliminin yayınıdır; yeni deney veya yeni teknik araştırma sonucu değildir. [U08 PUBLICATION](evidence/2026-09-12-cron-drain-receipts/PUBLICATION.md).
**Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release veya kurulu binary hükmü yok.

## Amaç, güncel yetki ve kapsam

Kullanıcı U08 yayını ve geri okumasını öncelemeyi; ancak yayın başarılı olursa kayıtlı Q47→Q49 araştırmasına devam etmeyi onayladı. Önceki teknik turun bulguları aşağıda korunur. Bu yayın checkpoint’inde yeni HERMES koşusu yapılmadı. Güncel main/AGENT/STATE, paket manifesti ve kaynak kayıtları geri kazanıldı; native write eylemleri bu denemede sunuldu. Neden değiştiği teşhis edilmez.

Kullanıcı araştırmanın planını değerlendirdikten sonra “devam et araştırmaya, operasyonel sınırına kadar çalış” dedi. U07/v0.20 STATE ve main yeniden repo üzerinden okundu; U07 yayını zaten tamamlanmıştı. Güncel AGENT blob'u değişmedi; aynı konuşmada tam okunmuş R01–R09 uygulandı. Bu yeni çalışma U08'dir, eski U07'yi tekrar göndermek veya eski deneyleri yeniden üretmek değildir.

Amaç HERMES'in kendi mekanizmalarını ve alt-sistem ilişkilerini açıklamak, daha sonra çekirdek model ve dört-alan/SOUL/Development OS aday değerlendirmesine ulaşmak. Yalnız `research/studies/hermes-agent/**` ve CATALOG'ın Hermes satırı değişebilir. Foundation, context/Codex, agent-control, diğer studies, upstream kodu, mimari/adoption, izin/ayar, credentials/model/provider veya full ürün kurulumu/çalıştırması kapsam dışıdır. Otomatik/background devam yoktur.

## U08'de gerçekten yapılan

[23 — Drainer, receipt ve cancellation](notes/23-CRON-DRAIN-RECEIPTS-AND-CANCELLATION.md) → [RESEARCH](evidence/2026-09-12-cron-drain-receipts/RESEARCH.md) → [SOURCES](evidence/2026-09-12-cron-drain-receipts/SOURCES.md) → [coverage](inventory/DELIVERY-RECEIPT-COVERAGE-2026-09-12.md). [CURRENT-RESEARCH-MAP](CURRENT-RESEARCH-MAP.md) sadece derived orientation'dır, ikinci work authority değildir.

**Source consumer zinciri:** successful running gateway startup → ayrı housekeeping thread → profile/adapter scope → scheduler.drain_delivery_queue → native queue callback → live/standalone sender. Queue dosyası yokken DB açılmaz. Job outcome→latest-execution join→cron CLI rows/warnings gerçek tüketicileri okundu. U07 pending+None deferral başarılı hesaplama koşulunda job last_status=ok ve CLI ok gösterimine kaynakla bağlandı; bu birleşik host/CLI yolu yeni bir runtime koşusu değildir. Kuyruk, execution ve last-job-summary ayrı durumlardır.

**Yeni ayırıcı soru:** live send timeout'undan sonra cancel boolean'ı “hiç başlamadı” veya “in-flight/teslim sayılabilir” olarak yorumlanabilir mi? Yalnız tam `agent/async_utils.py` modülü, Git blob `2bc558fad21eeec736c0283cb7df86304349f222`, 2.049 byte, full-byte eşleşmesiyle çalıştırıldı. Gerçek asyncio loop'u, ikinci thread ve fsync edilmiş yerel dosya etkisi; transport coroutine'i sentetik. [SPEC](evidence/2026-09-12-cron-drain-receipts/SPEC.md), [tam RESULT](evidence/2026-09-12-cron-drain-receipts/RESULT.json), [MANIFEST/raw](evidence/2026-09-12-cron-drain-receipts/MANIFEST.json).

B01 normal receipt/dosya; B02 dosya etkisi önce bağımsız okunmuşken cancel=True ve sonra etki hâlâ var; B03 timeout→terminal RuntimeError sonrası cancel=False ve etki dosyası yok. Böylece boolean'ın transport-phase oracle'ı olması çürütüldü. Actual enclosing _live_send_text, GatewayRunner, queue, network, SessionDB veya gerçek duplicate send çalıştırılmadı. Native fallback'in sonucu koşullu source inference; relay/no-fallback ve olası platform idempotency'si ayrıdır.

**Recorded run:** UTC `2026-09-11T21:12:38.167078+00:00` → `2026-09-11T21:12:38.171479+00:00`; Europe/Istanbul 12 Eylül. Python 3.13.5. Üç ordinary vaka expectation_met; N00 identity, N01/N02 fabricated observation-validator kontrolleri. Bunlar source mutant veya independent replication değildir. Thread join/loop close doğrulandı, audit listesi boş; probe stderr 0 byte. Ham source/spec/probe/result/log/effect/runtime/license bağları saklandı.

## Açık kalan ve yanlış genellenmeyecek olan

Q48 drainer/status **source hedefi ilerledi**, bütün transport/late-reconciliation doğrulaması kapanmadı. Q46 queue/compute/receipt alanları somut CLI tüketicisine bağlandı; tüm UI/yazarlar taranmadı. Q50 yeni cancellation/effect karşı örneği: actual network duplicate veya hata oranı iddiası değil. Seed/mirror caller'a varsayılan delivery geçebilir, actual DB seed etkisi NOT RUN.

Q40 actual SessionDB quiet next-request/wire, Q42 startup preclaim/carrier/drain/actual agent admission ertelenmiş doğrulamalardır. Bu tur gateway/run.py'nin başka aralıklarına erişilmiş olması Q42'nin eski exact aralığına veya bütün zincirine yeni doğrulama sağlamaz. Incidental cached-history selector gövdesi okundu, quiet yolu kapanmadı. Q41 migration/profile, Q43 full worker/arbitrary effects, Q44/Q45 semantic kalite ve Q07/Q22/Q26/Q29/Q38 eski sınırlar korunur. [CHECKS-NOT-RUN](evidence/2026-09-12-cron-drain-receipts/CHECKS-NOT-RUN.md) yeni yapılmamış ölçümleri açık taşır.

## Korunan tamamlanmış yayınlar

U04-A/18 ve U04-B/19 ayrı recorded source/deney paketleridir. B'nin 33 original dosyalı subtree'si `d01c92f7414713300934be3bb4e3d40ac57631b3`, [A/B reconciliation](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. A/B eş numaralı vakalar eş değildir; U06 L/U07 D/U08 B ile toplanıp ürün skoru üretilmez. B:H09, U07:D06 ve U08:B02 farklı nesne/deneylerdir.

U05/20, U06/21 ve U07/22 bütün evidence ve yayınları yerindedir. U07 içerik `56ffbfa608d6734ade1850198350726db0c5d05e`, yayın makbuzu `188095b930ac77f8d2a5dd605191a09a369a57ce`. **U07 yeniden yayın işi yoktur. U08’in güncel yayın hükmü PUBLICATION üst bölümündedir; eski unpublished ifadeler ilk teknik turu kaydeder.** U04–U07 raw/source/test kayıtları, notes01–22, METHOD ve merkezi synthesis01–03 değiştirilmez. Merkezi sentezler provisional; 20/21/22/23 ek notlar birlikte okunur, yeni final CORE/adoption yoktur.

## İlk operasyonel ve teknik devam

**Yayın kapısı:** U08 content/ref/diff geri okuması PUBLICATION makbuzunda doğrulanmadan Q47 başlamaz. Doğrulandıktan sonra eski sohbet ZIP'i gerekmez. Eski U07 first-next cümleleri tarihsel sıradır; güncel first-new-source aşağıdadır.

**İlk yeni source araştırması:** Q47 — scheduled occurrence/late callback/due/fire claim/rearm. Job ID, occurrence ve execution ID ayrımı; normal scheduled, gecikmiş ve explicit manual/force yolları. **Ardından Q49:** run_job içinde script/no_agent/monitor/agent/preflight ve actual context/history/provider bağlantısı. Bu kayıtlı sıranın ilerlemesidir; bütün Q48/Q50 fault uzayını bitirme ön şartı konmaz.

Q48/Q50 actual transport/status/seeding/profile deneyleri, gerekli full-source/bağımlılık ve güvenli imkân ya da güçlü reliability/adoption reuse gerektiğinde yeniden açılır. Provider/backend/delegation, learning/ledger/sync/quality, diğer UI/install/eval aileleri geniş haritada durur. Yayın işi yeni teknik deney diye sayılmaz; yeni teknik adım da mimari aşama yetkisi yaratmaz.

## Cold-start yolu

1. Güncel main AGENT ve tetiklenen protokoller → research root/studies catalog → current META/STATE/INDEX → METHOD/plan. U08 PUBLICATION üst bölümünü oku; ham manifestteki ilk teslim durumu güncel yayın hükmünün yerine geçmez.
2. Current publication authority: U07 ve U08 PUBLICATION üst bölümleri. Eski dosyalardaki historical unpublished açıklamalarını güncel engel sayma.
3. Gerçek yeni araştırma: note23 → U08 SOURCES/RESEARCH/coverage. Exact B koşusu için SPEC + tam RESULT + MANIFEST + arşivdeki source/probe/input/log/effect/runtime. Summary tam raw yerine geçmez.
4. Önceki source bağını gerektiği derinlikte 22/U07 → 21/U06 → 20/U05 üzerinden geri kazan. Eski canonical full cold-start yolundaki U04 ayrımı için19 + B README/RECONCILIATION/manifest; üst açıklama için synthesis03 + A SOURCES/RESEARCH/CONTINUITY-COVERAGE korunur. Aynı konuşmada tam okunanlar yeni independent evidence değildir.
5. Genişlik için CURRENT-RESEARCH-MAP ve F01–F12 coverage; exact eski iddia için kendi evidence raw/probe'u. Foundation araştırmasına veya upstream action'a geçilmez.

## Yayın kuralı

Güncel yayın, kullanıcının onayladığı önce yayın→doğrulama→araştırma sırasının ilk adımıdır. Native write bu denemede erişilebilir; yayın geçmişindeki aksi ifadeler ilk teknik turun capability kaydıdır. Ref force=false ilerletilir. Şu aşağıdaki tarihsel paragraflar güncel engel değildir.

### İlk teknik turdan korunmuş kayıt

Bu turn'de write/commit/ref eylemleri sunulmadığı sürece hiçbir repository mutation gerçekleşmiş değildir. Plugin installed/enabled olmak actual write capability değildir; sebep tahmin edilmez. İzin/credential/endpoint dolaşması yapılmaz. Güncel head değişmişse candidate eski ağacı force etmez; baseline SHA ve scoped dosya farkları yeniden değerlendirilir. Başarı ancak real nonforce ref + content/diff readback'tir; yerel hash/parse bunu ikame etmez.

## İlk teknik turun tarihsel head farkı

Kapanış readback'i main'i `a6c47ef3ff697c2d23c492dcf4ccfa32003040da` olarak gösterdi. Native compare, başlangıçtan bir commit ileri/geri farkı0 ve yalnız `research/soul-foundations/**` altında değişiklikler döndürdü. HERMES/CATALOG/control değişen yollar arasında değildi; yeni ref'ten HERMES STATE'in ilk16 satırı tekrar U07/v0.20 ve aynı blob'u verdi. Bu tur o Foundation değişiklikleri yapılmadı ve herhangi bir aktöre atfedilmedi. Yeni baseline dosya kimlikleri geçerli; eski root tree zorlanamaz. U08 hâlâ yayınlanmamıştır.
