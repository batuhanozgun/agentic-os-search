# Hermes Agent — Açık sorular

**2026-09-09 / ACTIVE / plan v0.8.** Sorular üretimde doğrulanmış kusur listesi değildir. [Birikimli defter](SOURCE-LEDGER.md), [D caller](evidence/2026-09-08-context-transfer/SOURCES.md), [E/C/V](evidence/2026-09-08-worker-policy/SOURCES.md), [J/MW](evidence/2026-09-09-review-middleware/SOURCES.md). Önceki ayrıntılı soru metni [v0.7 snapshot](https://github.com/batuhanozgun/agentic-os-search/blob/9a95b2cf1f8a0460ac6128e1409bf54aa3191022/research/studies/hermes-agent/OPEN-QUESTIONS.md) içindedir.

| ID | Açık ayrım / mevcut ilerleme | Sonraki kaynak / karşı sınama |
|---|---|---|
| Q01 | Review trigger/manual refine/nudge/API aynı mı? | Prologue/cancel/run_review_fork kaynakları var; finalize/manual/alternate yollar açık. |
| Q02 | Whitelist actual çağrıda nerede tüketiliyor? | 06/09/10 tüketici/kurulum bağı; full runtime Q26. |
| Q03 | Read/preview/approve/write aynı hedef revizyonu mu? | U01B2 canlı diff; actual fuzzy/locking/replay/UI binding. |
| Q04 | Pending saklama hatasında kullanıcı ne görür? | Eski U01B kanıtı; actual UI/restart/disk hata dağılımı açık. |
| Q05 | Proposer origin, insan onayı, apply ve ownership? | Actual CLI/gateway kimliği, home/profil ve live/fresh store ilk aktif kaynak işi; ortak D17/D15 yetmez. |
| Q06 | Cancellation sonrası eski worker/shared-store? | Kaynakta cancel/lock var; actual stop/çok-caller eşzamanlılığı açık. |
| Q07 | Sonraki session/rebuild bilgiyi ne zaman yükler? | D16 frozen/live ve D13/D14; actual invalidation/reload readback açık. |
| Q08 | Aynı/farklı model digest kaybı ve ders kalitesi? | H04 + eval/trajectory; gelecek-task yarar doğrulanmadı. |
| Q09 | Curator merge/rollback semantik olarak ne korur? | H18/H19, ledger/sync; absorbed_into tek oracle değil. |
| Q10 | Session-search summary/raw farkı? | Actual arama implementasyonu ve testleri; wire replay kaynakları yeterli değil. |
| Q11 | Terminal/OS/adapter/session izolasyonu? | Backend/gateway/UI; cooperative policy sandbox sayılmaz. |
| Q12 | Açılmamış alanlar yeni mekanizma getiriyor mu? | F01–F12, recursive envanter/apps/native/compat/eval. |
| Q13 | Boş curator aday kümesi skip literal farkı? | H18 static aday; test kalanı ve default-off sınırı. |
| Q14 | Curator bundled/prune/dry-run prompt vs guard? | Actual curator dispatch; banner mekanik yasak değil. |
| Q15 | Backup/report/cron-reference hatasında ne kalır? | Ledger/backup/cron/restart; gerçek koşu açık. |
| Q16 | Nested batch operations curator raporuna ne taşır? | H18/S01/S02 actual report/cron bağı açık. |
| Q17 | Skill batch exception actual caller'da ne olur? | J07 callback/downstream ayrımı şimdi bounded koşuldu; gerçek skill disk rollback ile entegrasyon hâlâ yok. |
| Q18 | Ortak preview bütün işlemleri temsil ediyor mu? | U01B/U01B2; her UI için read/preview/apply ayrı. |
| Q19 | Directory rollback vs ledger/cache/ownership/sync? | Gerçek yan etkiler ve yazar dışlama; sıralama global kilit değil. |
| Q20 | Özel memory/genel registry ortak denetim? | Ortak dış katman source-backed; full worker policy Q26 açık. |
| Q21 | Error JSON telafi de yapıyor mu? | J07 error-origin/once davranışı disk telafisinin yerine geçmez. Actual mutator/dispatch/readback açık. |
| Q22 | Frozen memory ve aynı-ID context revizyonu? | Compression/reload ve gerçek istek görünümü açık. |
| Q23 | Command approval vs skill/memory pending? | Request/observer/delivery/apply ayrı; actual UI bağlantısı sırada. |
| Q24 | Profile/home/DB/cache tutarlılığı? | Gerçek profile resolver/store ve caller bağlama; deney registry/profilleri sentetik. |
| Q25 | Raw/archive/api_content/search/review görünümü? | Sidecar source-backed; tam temsil/compaction eşdeğerliği açık. |
| Q26 | Review whitelist'i worker'da korunuyor mu? | Eski P/C/V + J03/J04/J05 source trace. 22 manuel-range AST eşleşti; full E01/E02 verifier NOT RUN. Bütün runtime/telafi kontrolleri açık, kaynak-bağımlı ileri doğrulama olarak tutulur. |
| Q27 | Memory write failure live-store/disk ayrışması? | 07/M01 statik; file/live/snapshot/result/reload readback NOT RUN. |
| Q28 | Batch content/new_text denetim eşdeğerliği? | 07/M02 statik; zararsız sentinel/taklit scanner sonra actual load-time sınırı. |
| Q29 | Gerçek review valid names dar izne eşit mi? | J03 parent toolset aktarımı + J04 schema-derived names + ayrı whitelist, standart kurulumda eşitlenmiyor. Tüm later mutations/runtime'lar için hüküm yok. |
| Q30 | Dispatched/handler/effect işaretleri neyi gösteriyor? | Eski C/V + MW06: ikinci next engellenebilir ama dışarı ilk sonuç dönebilir. Gerçek etki oracle'ı ayrı olmalı. |
| Q31 | Middleware rolü ile hata sözleşmesi uyumlu mu? | Exact J07 MW02 erken kendi Exception'ında devam; MW03 short-circuit, MW04 downstream error, MW08 BaseException ayrı. Gerçek zorunlu policy eklentileri ve konfigürasyon henüz değerlendirilmedi. |

## Disposition ve sıra

Q26/Q29 güçlü full-runtime iddiası kapanmadı. Constructor'ın dar ad-kümesiyle otomatik telafi ettiği açıklaması incelenen standart source yolunda desteklenmiyor; fakat gerçek bütün AIAgent/PluginManager/Relay/executor koşusu yok. Tam E01/E02 byte-hash/verifier NOT RUN; manuel-range cross-check bunu ikame etmez. İki transkripsiyonun ortak hata riski vardır.

V0.7'nin sınırlı ilerleme seçeneği kullanılarak ilk aktif iş Q05/Q23/Q24 actual pending CLI/gateway/profile/store'a geçti. Q26 yeni tam-source/bağımlılık erişimi, ilgili source değişimi veya load-bearing reuse olduğunda yeniden açılır. Aynı eski selected fixture'ların tekrar sayısı yükseltilmez. Bu sıra değişimi bir güvenlik ya da bütün U01 kapanışı değildir.

J07 sekiz tanılayıcı durumunda fake registry/callback/handler vardır; tüm Hermes güvenliği/kalitesi ölçülmedi. 22 AST karşılaştırması yürütme senaryosu değildir. K01–K09'un tamamı koşulmuş sayılmaz; M01/M02 ve compression/curator deneyleri NOT RUN. Sayılar ürün PASS toplamı yapılmaz; bütün eski not/kanıtlar korunur.
