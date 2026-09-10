# Hermes Agent — Açık sorular

**2026-09-10 / ACTIVE / plan v0.10.** Sorular üretimde doğrulanmış kusur listesi değildir. [Birikimli rota](SOURCE-LEDGER.md), [D caller](evidence/2026-09-08-context-transfer/SOURCES.md), [E/C/V](evidence/2026-09-08-worker-policy/SOURCES.md), [J/MW](evidence/2026-09-09-review-middleware/SOURCES.md), [M2/N](evidence/2026-09-09-memory-pending/SOURCES.md), [UI/A](evidence/2026-09-10-ui-profile/SOURCES.md). [V0.9 tam soru kaydı](https://github.com/batuhanozgun/agentic-os-search/blob/91af4415c22e05b80484b935383ceeb04a3c5b7b/research/studies/hermes-agent/OPEN-QUESTIONS.md) önceki ayrıntıları ve sıralamayı korur.

| ID | Açık ayrım / mevcut ilerleme | Sonraki kaynak / karşı sınama |
|---|---|---|
| Q01 | Review trigger/manual refine/nudge/API aynı mı? | Prologue/cancel/run_review_fork kaynakları var; finalize/manual/alternate yollar açık. |
| Q02 | Whitelist actual çağrıda nerede tüketiliyor? | 06/09/10 tüketici/kurulum bağı; full runtime Q26. |
| Q03 | Read/preview/approve/write aynı hedef revizyonu mu? | U01B2 canlı diff; M3 gateway preview kesintisi ve ortak apply source bağı. Actual fuzzy/locking/revision-binding ve diğer UI'ler açık. |
| Q04 | Pending saklama hatasında kullanıcı ne görür? | Eski U01B kanıtı; actual UI/restart/disk hata dağılımı açık. M2 unlink hatası ayrı Q32. |
| Q05 | Proposer origin, insan onayı, apply ve ownership? | M3 normal CLI/gateway ingress/slash/shared apply kaynağı; command-family grant ile kayıt/alt-işlem yetkisi ayrıldı. Record origin insan kimliği değil; per-record ownership ve bütün auth/hook yolları açık. |
| Q06 | Cancellation sonrası eski worker/shared-store? | Kaynakta cancel/lock var; M2/N06 yalnız sıralı stale-store reload. M3 idle-only kuralı global çok-yazar kilidi değil. Actual stop/yarış açık. |
| Q07 | Sonraki session/rebuild bilgiyi ne zaman yükler? | **İlk aktif iş:** M3 gerçek CLI live/fresh ve gateway fresh apply seçimi → cached-agent reuse/store reload/prompt/prepared request. M2 frozen readback'i actual request değildir. |
| Q08 | Aynı/farklı model digest kaybı ve ders kalitesi? | H04 + eval/trajectory; gelecek-task yarar doğrulanmadı. |
| Q09 | Curator merge/rollback semantik olarak ne korur? | H18/H19, ledger/sync; absorbed_into tek oracle değil. |
| Q10 | Session-search summary/raw farkı? | Actual arama implementasyonu ve testleri; wire replay kaynakları yeterli değil. |
| Q11 | Terminal/OS/adapter/session izolasyonu? | Backend/gateway/UI; cooperative policy ve context-local profile scope OS sandbox sayılmaz. |
| Q12 | Açılmamış alanlar yeni mekanizma getiriyor mu? | F01–F12, recursive envanter/apps/native/compat/eval. |
| Q13 | Boş curator aday kümesi skip literal farkı? | H18 static aday; test kalanı ve default-off sınırı. |
| Q14 | Curator bundled/prune/dry-run prompt vs guard? | Actual curator dispatch; banner mekanik yasak değil. |
| Q15 | Backup/report/cron-reference hatasında ne kalır? | Ledger/backup/cron/restart; gerçek koşu açık. |
| Q16 | Nested batch operations curator raporuna ne taşır? | H18/S01/S02 actual report/cron bağı açık. |
| Q17 | Skill batch exception actual caller'da ne olur? | J07 callback/downstream bounded koşuldu; M3 shared UI apply source bağı var. Gerçek skill disk rollback ile tam entegrasyon hâlâ yok. |
| Q18 | Ortak preview bütün işlemleri temsil ediyor mu? | U01B/U01B2 + M3 gateway 3000-karakter kesintisi/sabit home ipucu; full-diff okunmasının apply ön şartı olduğu gösterilmedi. Her UI/revizyon/profil için temsil doğruluğu açık. |
| Q19 | Directory rollback vs ledger/cache/ownership/sync? | Gerçek yan etkiler ve yazar dışlama; sıralama global kilit değil. |
| Q20 | Özel memory/genel registry ortak denetim? | Ortak dış katman source-backed; full worker policy Q26 açık. |
| Q21 | Error JSON telafi de yapıyor mu? | M2/N02/N09 hata raporu disk/live restorasyonunu sağlamadı; M3 caller nesne ömrü source-backed. J07 error-origin/once farklı katman. Actual UI readback açık. |
| Q22 | Frozen memory ve aynı-ID context revizyonu? | **Q07 ile aktif:** payload approve ile approval/mode cache eviction farklı. Gerçek compression/turn-prologue/reload/prompt/request görünümü bağlanacak. |
| Q23 | Command approval vs skill/memory pending? | M3 gerçek memory/skills shared handler, mode setter ve ayrı approvals admin kontrolü kaynakta. Merkez canonical-name policy sekiz bounded senaryoda çalıştı; bütün UI/admission execution değil. |
| Q24 | Profile/home/DB/cache tutarlılığı? | M3 primary/secondary wrapper, admitting-transport damgası ve context-home önceliği source-backed. Tam route/auth resolver, multi-session config/cache, setup failure ve gerçek kullanıcı bağlama açık. |
| Q25 | Raw/archive/api_content/search/review görünümü? | Sidecar source-backed; tam temsil/compaction eşdeğerliği açık. |
| Q26 | Review whitelist'i worker'da korunuyor mu? | Eski P/C/V + J03/J04/J05 source trace. 22 manuel-range AST eşleşti; full E01/E02 verifier NOT RUN. Bütün runtime/telafi kontrolleri açık, kaynak-bağımlı ileri doğrulama. |
| Q27 | Memory write failure live-store/disk ayrışması? | M2/N02/N09 bounded pre-commit writer hatası, hata/pending koruma ve reload/retry. M3 CLI live-store/gateway fresh-store kaynak bağı etkisini ayrıştırır; gerçek utils arızaları/UI etkisi/süresi açık. |
| Q28 | Batch content/new_text denetim eşdeğerliği? | M2/N07 sentetik sentinel scanner ile ön tarama farkı + load-time masking. Gerçek scanner/schema/transport/model-visible sonuç açık; genel bypass hükmü değil. |
| Q29 | Gerçek review valid names dar izne eşit mi? | J03 parent toolset + J04 schema-derived names + ayrı whitelist, standart kurulumda eşitlenmiyor. Tüm later mutations/runtime'lar için hüküm yok. M2 statik notu bağımsız tekrar değil. |
| Q30 | Dispatched/handler/effect işaretleri neyi gösteriyor? | Eski C/V + MW06: ikinci next engellenebilir ama dışarı ilk sonuç dönebilir. Gerçek etki oracle'ı ayrı olmalı. |
| Q31 | Middleware rolü ile hata sözleşmesi uyumlu mu? | Exact J07 MW02 erken kendi Exception'ında devam; MW03 short-circuit, MW04 downstream error, MW08 BaseException ayrı. Gerçek zorunlu policy eklentileri/konfigürasyon açık. |
| Q32 | Successful apply, pending temizleme ve retry aynı mı? | M2/N11 unlink hatasında Approved 1 + pending 1; ikinci add idempotent. M3 actual UI shared-handler bağı gösterildi; replace/remove/batch/crash ve gerçek UI hata enjeksiyonu açık. |
| Q33 | Staging uygulanabilirliği doğruluyor mu? | M2/N12 bilinmeyen action staged, apply'de ret/no-write/pending korundu. M3 ortak gerçek caller bağlantısı var; full UI hatalı kayıt yönetimi/doğrulama açık. |

## Disposition ve sıra

V0.9'un ilk aktif sorusu olan normal CLI/gateway pending caller → profile/home/supplied-store bağı, U01-M3'te kaynakla ilerledi. **İlk aktif iş Q07/Q22 onaydan prompt/prepared-request görünürlüğüne geçti.** Komut adı için yetki verilmesi yalnız pending okuma izni değildir; transport admission, canonical slash policy, runtime profile ve kayıt sahipliği ayrı kalır. Bütün kullanıcılar yetkisizdir/yetkilidir veya bütün profile yolları eşdeğerdir hükmü yoktur.

Q05/Q23/Q24'ün ileri kaynak/çalışma sınırları: tam profile route/transport authorization, gerçek konfigürasyonun hangi profile'dan geldiği, multi-session cache scope, optional command hook rewrite sonrası yeniden-yetkilendirme, gerçek UI fault injection. Bunlar doğrulanmış güvenlik olayı değil; 12 notundaki açık yollar ve reuse tetikleyicileridir. Aynı normal handler'ları ilk kez bulunacakmış gibi tekrar başa alma.

Q26/Q29 güçlü full-runtime iddiası kapanmadı. Tam E01/E02 byte-hash/verifier NOT RUN; manuel-range cross-check bunu ikame etmez. Yeni tam-source/bağımlılık erişimi, ilgili source değişimi veya load-bearing reuse olduğunda yeniden açılır. Aynı eski selected fixture'ların tekrar sayısı yükseltilmez.

M3/A01–A08 sadece tam slash-policy modülü ve synthetic config/source/platform nesneleridir; gerçek gateway/profile/store/handler/provider çalıştırılmadı. UI09 test kaynağı okundu, koşulmadı. Eski J07/M2/C/V/P ve diğer deneyler bu tur tekrarlanmadı. N06 sıralı stale-store, N10 supplied-store flag, N11 duplicate-add kapsamlarında kalır. K01–K09'un tamamı koşulmuş değildir; bütün eski not/kanıtlar korunur ve sayılar ürün PASS toplamı yapılmaz.
