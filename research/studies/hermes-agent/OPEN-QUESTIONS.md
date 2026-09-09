# Hermes Agent — Açık sorular

**2026-09-09 / ACTIVE / plan v0.7.** Sorular üretimde doğrulanmış kusur listesi değildir. H/S/W geçmişi [SOURCE-LEDGER](SOURCE-LEDGER.md); D kaynakları [caller defteri](evidence/2026-09-08-context-transfer/SOURCES.md); E/C/V kayıtları [worker-policy defteri](evidence/2026-09-08-worker-policy/SOURCES.md). Önceki tam metin [v0.6 snapshot](https://github.com/batuhanozgun/agentic-os-search/blob/36f1b7e6ae07da5c1d9d57ff9633d48473c42537/research/studies/hermes-agent/OPEN-QUESTIONS.md) içinde korunur.

| ID | Açık ayrım / mevcut ilerleme | Sonraki kaynak / karşı sınama |
|---|---|---|
| Q01 | Review trigger/manual refine/nudge/API aynı mı? | Turn prologue nudge + facade cancel callsite görüldü; finalize/manual/alternate yollar açık. |
| Q02 | Whitelist actual çağrıda nerede tüketiliyor? | 06 source trace; 09 selected gerçek tüketici/worker ile ilerledi. Tam kurulum ve telafi edici callsite için Q26/Q29. |
| Q03 | Read/preview/approve/write hedef sürümü aynı mı? | H22/S01–S04 farkı ve U01B2 canlı diff kanıtı; actual fuzzy/locking/replay/UI binding açık. |
| Q04 | Pending saklama hatasında kullanıcı ne görür? | U01B D05 korunur; actual UI/restart/disk hata dağılımı açık. |
| Q05 | Proposer origin, insan onayı, apply ve ownership nasıl bağlanır? | D17/D15 payload tabanlı replay; actual UI/profile/skill ownership ve U01B2 default_name yeterliliği açık. |
| Q06 | Cancellation sonrası eski worker/shared store? | D12 cancel, D04 worker ve D16 lock/reload; actual stop/çok-caller eşzamanlılığı açık. U01B2 araya-giren yazı gerçek thread yarışı değildir. |
| Q07 | Sonraki oturum/rebuild yeni bilgiyi ne zaman yükler? | D16 live/frozen ve D13/D14 restore/wire; actual invalidation/reload readback'i açık. |
| Q08 | Aynı/farklı model digest'inde kayıp ve ders kalitesi? | H04 + eval/trajectory; eşdeğerlik/gelecek-task yarar doğrulanmadı. |
| Q09 | Curator merge/rollback semantik olarak ne korur? | H18/H19, ledger/backup/sync; absorbed_into yeterli oracle değil. |
| Q10 | Session-search özetleme/raw retrieval farkı? | Actual implementation/schema/test; D14 wire replay arama motorunun kanıtı değil. |
| Q11 | Terminal/OS/adapter/session izolasyon sınırları? | H13 → backend/gateway/UI; cooperative control sandbox sayılmaz. |
| Q12 | Büyük açıklanmamış bölgeler yeni mekanizma getiriyor mu? | F01–F12; recursive envanter ve apps/native/compat/eval açık. |
| Q13 | Boş curator aday kümesi skip literal farkı? | H18 statik aday; test kalanı/kontrollü karşı örnek; default-off ayrımı. |
| Q14 | Curator bundled/prune/dry-run prompt vs guard? | H16–H20/H05, actual curator dispatch; banner mekanik yasak değil. |
| Q15 | Backup/report/cron-reference hatasında ne kalır? | Gerçek ledger/backup/cron/restart; statik dal canlı olay değildir. |
| Q16 | Nested batch operations kısa curator raporuna ne taşır? | H18 + S01/S02 actual trace/report/cron; bu tur kapanmadı. |
| Q17 | Skill batch exception actual dış caller'da ne olur? | D04/D05/D22 wrapper statik; U01B/U01B2'nin dar exception kanıtı tam dispatch ile bağlanmadı. |
| Q18 | Ortak approval preview bütün işlemleri temsil ediyor mu? | U01B batch/rewrite ve U01B2 target-version bulguları; her UI için read/preview/apply ayrı. |
| Q19 | Dizin rollback'i ile ledger/cache/ownership/sync ilişkisi? | Gerçek yan etkiler ve başka-yazar kontrolü; sentetik event listesi gerçek audit/network değil. Sıralama global kilit sayılmaz. |
| Q20 | Özel memory ile genel registry ortak denetimi paylaşıyor mu? | D03/D04 ortak dış kontrolü gösterdi; local store kontrolsüz varsayımı desteklenmedi. Tam worker policy Q26 açık. |
| Q21 | Error JSON üretmek telafi de yapıyor mu? | D04/D05/D22 + S02; actual effect/readback/dependency closure açık. D2 hook/approval hataları rollback deneyinin yerine geçmez. |
| Q22 | Frozen memory ve aynı-ID context revizyonu? | D16 snapshot, D13/D14 cached/wire; compression reload ve gerçek istek gözlemi açık. |
| Q23 | Command approval olayları ile skill/memory pending aynı mı? | Observer/request/delivery/apply ayrı; D17 actual bütün UI değildir. Selected approve-directive sonucu pending UI'ye genellenmez. |
| Q24 | Profile/home, DB contention ve local cache tutarlılığı? | Deney profilleri sentetik; gerçek resolver/target/çok-process/store-lock kapsamı açık. |
| Q25 | Raw/archive/api_content/search/review hangi kanıtı korur? | D14 sidecar/substitution; bütün taşıma/compaction/search eşdeğerliği ve summary failure açık. |
| Q26 | Review thread whitelist'i worker precheck'inde var mı? | P transport + D2 C/V selected-function evidence. Parent'ta ret, worker'da liste yok; explicit binding ret getirdi. Tam E01/E02 seçki sadakati NOT RUN; ardından gerçek review/ara kontrol/worker erişilebilirliği ilk iş. |
| Q27 | Memory yazımı başarısızsa canlı store ile disk ayrışıyor mu? | 07/M01 assignment-before-write statik; file/live/snapshot/result ve sonraki reload readback'i NOT RUN. |
| Q28 | Batch content/new_text alias'ları aynı denetimi alıyor mu? | 07/M02 statik; zararsız sentinel/taklit scanner, sonra actual load-time sınırı ayrı. |
| Q29 | Gerçek review'un geçerli-ad kümesi dar yetki kümesine eşit mi? | E06 tam modül + sentetik holder V01–V05: ad/JSON reddi çalıştı; geniş kabul whitelist yerine geçmedi. Actual fork/valid-name üretimi ve compensating controls açık. |
| Q30 | Hangi yürütme işareti gerçekten etkiyi gösteriyor? | D2 C01/C05/C07 ve C12: dispatched callback kabulünü gösterirken handler sayısı sıfır veya yalnız bir olabilir. Tam caller gözleminde callback/policy/handler/effect/persistence ayrı oracle'larla izlenmeli. |

## Kanıt ve ilerleme sınırı

K01–K09 ilk olarak 05 notunda tasarlanmıştır. K03 transport alt sorusu önce üç-modüllü sentetik-policy probe ile, sonra D2'nin gerçek selected tüketici/worker ve tam name-validator köprüsüyle ilerledi. **Tam AIAgent/PluginManager/executor/profil ve bütün ara kontrollerin koşusu değildir.** K01/K02/K04/K05/K06/K07'de pinned kaynak kesitleri vardır; K08/K09 runtime sonucu yok. Plan v0.7 aşama ayrımlarını taşır.

D2'nin elle aktarılmış seçkileri tam kaynaklarla otomatik AST eşitliği kontrolünden henüz geçmedi. `verify_excerpts.py` bu yüzden ilk somut kontrol, fakat eşitlik bulunsa bile davranışın gerçek review'da erişilebilirliği ayrıca araştırılır. U01-D2 publication hash kontrolü bu AST veya davranış kontrolünün yerine geçmez.

Q26 ilk sıradadır ama çalışmayı tek bir güvenlik projesine dönüştürmez. Karşılayıcı kontrol veya farklı caller bulunursa çıkarım daraltılır. Q27/Q28 statik aday; üretim sıklığı/sızıntı/genel bellek güvensizliği iddiası yok. D21 provider dashboard helper'ı pending UI kapanışı değildir.

Bir soru ancak kaynak/ref/kanıt sınırıyla notta cevaplanır. Okuma hatası ürün yetersizliği değildir. H22 ve run_agent eski erişim/ilk-okuma işi değildir. U01-D2'nin 14/5 durumları kaydedildi; yeni oturum bunları kayıp veya yapılmamış saymamalı. Tüm U01 ve gelecek-kullanım kapanmadan genel self-improvement verified/absent hükmü verilmez.
