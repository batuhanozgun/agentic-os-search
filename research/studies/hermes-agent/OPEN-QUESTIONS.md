# Hermes Agent — Açık sorular

**2026-09-07 / active, plan v0.4.** Keşif/continuation kaydı; bütün satırlar doğrulanmış üretim kusuru değildir. H-ID'leri [SOURCE-LEDGER](SOURCE-LEDGER.md), S-ID'leri [U01B defteri](evidence/2026-09-07-u01b/SOURCES.md) üzerinden açılır.

| ID | Açık ayrım / mevcut ilerleme | Sonraki kaynak / karşı sınama |
|---|---|---|
| Q01 | Review ne zaman tetiklenir; manual refine/nudge/API yolları aynı mı? | run_agent forwarding → turn_facade/loop ve çağıranlar. |
| Q02 | Whitelist bütün ilgili gerçek dispatch yollarında mı? | plugins, invoke-tool/worker/context; H09 mock assertion'ı yeterli değil. |
| Q03 | Read/preview/approve/write arasında hedef değişirse ne olur? | H22/S01 tam; S04 preview ile mutator işlemi farklı. Gerçek caller, fuzzy matching, locking ve sürüm bağlama açık. |
| Q04 | Pending saklama hatasında kullanıcı ne görür? | U01B D05'te kimlik döndü, normal pending kaydı bulunamadı, temp kaldı. Gerçek UI/caller, restart/recovery ve disk dağılımı açık; tüm ürün arızası denmez. |
| Q05 | Öneren origin, insan onayı ve sonraki ownership nasıl bağlanır? | S01/S04/S05 dar replay yolu okundu; record origin'i payload dışında. UI/caller context ve memory apply açık. |
| Q06 | Paylaşılan store/cancellation sonrası eski worker yazıları? | H04/H12 → store kilitleri, context-copy ve lifecycle/test. |
| Q07 | Sonraki oturum değişikliği ne zaman yükler? | prompt-builder, MemoryStore, skill discovery/view/cache; frozen vs live görünüm. |
| Q08 | Farklı-model digest'in düşürdüğü kanıt ders kalitesini nasıl etkiler? | H04 + varsa eval/trajectory/dataset; eşdeğerlik varsayılmayacak. |
| Q09 | Curator merge/rollback semantik olarak ne korur? | 03 notu §§6–7; H18/H19 → ledger/backup/sync ve S01/S02 bağlantısı. absorbed_into yeterli oracle değil. |
| Q10 | README session-search özetleme vs raw-message rehberi? | Actual session-search implementation/schema/test ve gerekirse tarih. |
| Q11 | Terminal sandbox/whole-process/adapter/session sınırları? | H13 → backend/plugin/gateway/UI; politika compliance'ı açık. |
| Q12 | Büyük açıklanmamış bölgeler yeni mekanizma getiriyor mu? | apps/web/native/cron/provider/compat/eval envanteri; F01–F12 değişebilir. |
| Q13 | Boş aday kümesi curator skip koşulu? | H18 metin uyuşmazlığı statik; test kalanı ve kontrollü karşı örnek. Varsayılan-off yoluyla karıştırma. |
| Q14 | Curator prompt bundled/prune/dry-run ile gerçek guard uyumu? | H16–H20/H05 → S01/S02 gerçek caller ve origin. Banner mekanik yasak değildir. |
| Q15 | Backup/report/cron-reference hatasında hangi durum kalır? | H18/H19 → gerçek ledger/backup/cron/restart. Kaynak dalı canlı olay değil. |
| Q16 | Batch operations ve kısa tool arguments curator raporuna ne taşır? | H22/S01 schema + S02 → H18 args/report yorumları ve gerçek trace/ledger. |
| Q17 | Fırlatılan mutator istisnası gerçek caller'da nasıl ele alınır? | U01B B04 exact batch + sentetik OSError'da ilk değişiklik kaldı, snapshot temizlendi. Gerçek invoke/exception wrapper ve readback açık. |
| Q18 | Ortak onay önizlemi tüm işlemleri temsil ediyor mu? | D02 batch etiketi, D03 rewrite/no-textual-change bileşen gözlemleri. CLI/gateway/desktop kullanımı, alternatif diff ve kullanıcıya etkisi ayrı incelenecek. |
| Q19 | Dizin geri alınırken diğer etkiler? | S01 _record_success + S02; gerçek ledger/cache/ownership/sync/timer-profile. Sentetik olay listesi gerçek network veya audit sonucu değil. |

Q03–Q05 kısmen aydınlandı; bütün caller/ürün kapsamında kapatılmadı. H22'nin eski eksik orta aralığı U01B tam okumasıyla recover edildi; sıradaki görev artık o aralığı ilk kez okumak değil gerçek zincire bağlamak.

Bir soru kaynağı/ref'i/kanıt statüsüyle notta cevaplanır; tablo rotadır. Kaynak erişimi eksiği ürün yetersizliği sayılmaz. Deney gerektiren genelleme statik kodla kapanmaz. Kapsam dışına çıkarılacak soru varsa gerekçe korunur. U01 ve bağlantılı bakım/gelecek-kullanım tamamlanmadan genel self-improvement verified/absent hükmü yoktur.
