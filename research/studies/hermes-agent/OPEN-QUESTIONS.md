# Hermes Agent — Açık sorular

**2026-09-08 / ACTIVE / plan v0.6.** Sorular üretimde doğrulanmış kusur listesi değildir. H/S/W geçmişi [SOURCE-LEDGER](SOURCE-LEDGER.md); D kaynakları [yeni defter](evidence/2026-09-08-context-transfer/SOURCES.md). Önceki soru metinleri [v0.5 snapshot](https://github.com/batuhanozgun/agentic-os-search/blob/a218acfc20e7ece488709e00a9762166ec970fba/research/studies/hermes-agent/OPEN-QUESTIONS.md) içinde korunur.

| ID | Açık ayrım / mevcut ilerleme | Sonraki kaynak / karşı sınama |
|---|---|---|
| Q01 | Review trigger/manual refine/nudge/API aynı mı? | Turn prologue nudge + facade cancel callsite görüldü; finalize/manual/alternate yollar açık. |
| Q02 | Whitelist actual çağrıda nerede tüketiliyor? | 06'da source trace ve Q26; H09 mock yeterli değil. |
| Q03 | Read/preview/approve/write hedef sürümü aynı mı? | H22/S01 ve S04 ayrımı korunur; fuzzy/locking/replay/UI target binding açık. |
| Q04 | Pending saklama hatasında kullanıcı ne görür? | U01B D05 korunur; actual UI/restart/disk hata dağılımı açık. |
| Q05 | Proposer origin, insan onayı, apply ve ownership nasıl bağlanır? | D17/D15 payload tabanlı memory replay görüldü; actual UI/profile ve skill ownership açık. |
| Q06 | Cancellation sonrası eski worker/shared store? | D12 cancel, D04 worker ve D16 lock/reload var; actual stop/çok-caller eşzamanlılığı açık. |
| Q07 | Sonraki oturum/rebuild yeni bilgiyi ne zaman yükler? | D16 live/frozen ayrımı ve D13/D14 restore/wire; gerçek invalidation/reload readback'i açık. |
| Q08 | Aynı/farklı model digest'inde kayıp ve ders kalitesi? | H04 + eval/trajectory; eşdeğerlik/gelecek-task yarar doğrulanmadı. |
| Q09 | Curator merge/rollback semantik olarak ne korur? | H18/H19, ledger/backup/sync; absorbed_into yeterli oracle değil. |
| Q10 | Session-search özetleme/raw retrieval farkı? | Actual implementation/schema/test; D14 wire replay arama motorunun kanıtı değil. |
| Q11 | Terminal/OS/adapter/session izolasyon sınırları? | H13 → backend/gateway/UI; cooperative control sandbox sayılmaz. |
| Q12 | Büyük açıklanmamış bölgeler yeni mekanizma getiriyor mu? | F01–F12; recursive envanter ve apps/native/compat/eval açık. |
| Q13 | Boş curator aday kümesi skip literal farkı? | H18 statik aday; test kalanı/kontrollü karşı örnek; default-off ayrımı. |
| Q14 | Curator bundled/prune/dry-run prompt vs guard? | H16–H20/H05, actual curator dispatch; banner mekanik yasak değil. |
| Q15 | Backup/report/cron-reference hatasında ne kalır? | Gerçek ledger/backup/cron/restart; statik dal canlı olay değildir. |
| Q16 | Nested batch operations kısa curator raporuna ne taşır? | H18 + S01/S02 actual trace/report/cron; bu tur kapanmadı. |
| Q17 | Skill batch exception actual dış caller'da ne olur? | D04/D05/D22 wrapper statik incelendi; U01B B04 entegre yeniden koşulmadı. |
| Q18 | Ortak approval preview bütün işlemleri temsil ediyor mu? | U01B batch/rewrite counterexamples; her UI için read/preview/apply ayrı. |
| Q19 | Dizin rollback'i ile ledger/cache/ownership/sync ilişkisi? | S01/S02 + gerçek yan etki yolları; sentetik event listesi gerçek audit/network değil. |
| Q20 | Özel memory ile genel registry ortak denetimi paylaşıyor mu? | D03/D04 ortak dış kontrolü gösterdi; local store yolu kontrolsüz varsayımı desteklenmedi. Worker policy Q26 hâlâ açık. |
| Q21 | Error JSON üretmek telafi de yapıyor mu? | D04/D05/D22 + S02; actual effect/readback ve bağımlılık kapanışı açık. |
| Q22 | Frozen memory ve aynı-ID context revizyonu? | D16 snapshot, D13/D14 cached/wire; compression reload ve gerçek istek gözlemi açık. |
| Q23 | Command approval olayları ile skill/memory pending aynı mı? | Observer/request/delivery/apply ayrı; D17 common command actual bütün UI değildir. |
| Q24 | Profile/home, DB contention ve local cache tutarlılığı? | Probe profili sentetik; gerçek resolver/target/çok-process ve store-lock kapsamı açık. |
| Q25 | Raw/archive/api_content/search/review hangi kanıtı korur? | D14 sidecar/substitution source-backed; bütün taşıma/compaction/search eşdeğerliği ve summary failure açık. |
| Q26 | Review thread whitelist'i worker precheck'inde var mı? | 06 control-context süreksizliği adayı. P01–P07 transport evidence; actual executor + actual whitelist + zararsız handler sırada. |
| Q27 | Memory dosya yazımı başarısızsa canlı store ile disk ayrışıyor mu? | 07/M01: assignment-before-write statik; file/live/snapshot/result ve sonraki reload için NOT RUN readback. |
| Q28 | Batch content/new_text alias'ları aynı denetimi alıyor mu? | 07/M02 statik kapsam farkı; zararsız sentinel/taklit scanner, sonra actual load-time sınırı ayrı. |

## Kanıt ve ilerleme sınırı

K01–K09 ilk olarak 05 notunda tasarlanmıştır. K03'ün transport alt sorusu yeni üç-modüllü probe ile kısmen sınandı; bu, actual PluginManager/executor/profile deneyi veya dokuz kontrolün tamamı değildir. K01/K02/K04/K05/K06/K07'de yeni statik kaynak vardır; K08/K09 runtime sonucu yok. Current statü RESEARCH-PLAN v0.6'da ayrılır.

Q26 ilk sıradadır ama genel araştırmayı tek bir güvenlik yan dalına dönüştürmez. Karşılayıcı kontrol veya farklı caller bulunursa mevcut çıkarım daraltılır. Q27/Q28 henüz kaynak adayıdır; üretim sıklığı, sızıntı veya bütün bellek güvenliğinin başarısızlığı iddia edilmez. D21 provider dashboard helper'ı pending UI kapanışı sayılmaz.

Bir soru ancak kaynak/ref/kanıt sınırıyla notta cevaplanır. Okuma hatası ürün yetersizliği değildir. H22'nin eski orta aralık eksikliği kapanmıştır; yeni run_agent/tree/blob erişimi de bu tur ilerlemiştir. Yeni oturum tarihsel 429'u gerekçe gösterip aynı ilk dosyada başa dönmemeli. U01, bağlantılı bakım ve gelecek-kullanım kapanmadan genel self-improvement verified/absent hükmü verilmez.
