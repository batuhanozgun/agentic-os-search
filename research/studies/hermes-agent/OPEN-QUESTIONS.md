# Hermes Agent — Açık sorular

**2026-09-08 / active, plan v0.5.** Keşif/continuation kaydı; bütün satırlar doğrulanmış üretim kusuru değildir. H-ID'leri [SOURCE-LEDGER](SOURCE-LEDGER.md), S-ID'leri [U01B defteri](evidence/2026-09-07-u01b/SOURCES.md) üzerinden açılır.

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

## U01-DOC ile ayrıntılanan sorular — kapatılmış kod bulgusu değil

[05 notu](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) ve [W01–W08 defteri](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md), yukarıdaki soruların kontrat tarafını genişletir. Primary caller isteği iki kez 429 verdiği için Q01/Q02/Q05/Q17'nin yeni pinned kod kapanışı yoktur. Aşağıdaki alt sorular mevcut aileleri ikame etmez.

| ID | Yeni ayırıcı soru | Bağlantı / sonraki kontrol |
|---|---|---|
| Q20 | Agent-local memory/todo/session_search/delegate ile genel registry yolları aynı denetimi hangi callsite'ta alır? | Q02; W01–W03; K01/K03. Belge şemasından bypass sonucu çıkmaz. |
| Q21 | Error-to-JSON wrapper yalnız sonucu mu dönüştürür, önceki etkiyi de telafi eder mi? | Q17/Q19; W01 ve U01B B04; K02 gerçek caller + readback. |
| Q22 | Frozen memory hangi rebuild'de yeniden görünür; aynı session ID bağlam revizyonunu gizler mi? | Q07/Q01; W04/W05/W08; K05/K06. Belge kapsam farkı runtime bug değildir. |
| Q23 | Command approval gözlem olayları ile skill/memory pending onayı aynı kontrol/teslim/karar zincirini paylaşır mı? | Q04/Q05/Q18; W03; K04. Observer, onay veren merci değildir. |
| Q24 | Profile/home bölümlemesi, DB contention yönetimi ve agent-local cache/memory tutarlılığı hangi kapsamda birleşir? | Q06/Q11; W06/W07; K03/K05. Namespace, sandbox ve tüm-depo eşzamanlılığı ayrı. |
| Q25 | Raw/arşiv/API-content/search/review görünümleri hangi kritik bilgiyi korur; summary failure hangi isteği değiştirir? | Q08/Q10; W07/W08; K07/K08. Belgedeki failure uyarısı yürütülmüş deney değildir. |

K09, Q16'nın mevcut curator batch sorusunu sınayacak; yeni kod sonucu yok. K01–K09'un tamamı **PLANNED / NOT RUN**. Güncel resmî belge ortak commit'i bilinmediğinden bu sorular primary kaynakla karşılaştırılmadan implementation veya ürün güvenliği hükmü verilmez.
