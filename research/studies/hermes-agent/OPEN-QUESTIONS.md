# Hermes Agent — Açık sorular

**2026-09-09 / ACTIVE / plan v0.9.** Sorular üretimde doğrulanmış kusur listesi değildir. [Birikimli defter](SOURCE-LEDGER.md), [D caller](evidence/2026-09-08-context-transfer/SOURCES.md), [E/C/V](evidence/2026-09-08-worker-policy/SOURCES.md), [J/MW](evidence/2026-09-09-review-middleware/SOURCES.md), [M2/N](evidence/2026-09-09-memory-pending/SOURCES.md). Önceki ayrıntılı soru metni [v0.8 snapshot](https://github.com/batuhanozgun/agentic-os-search/blob/c0ef2374a34cbb30f5f58a28333f89254931b00f/research/studies/hermes-agent/OPEN-QUESTIONS.md) ve Git geçmişindedir.

| ID | Açık ayrım / mevcut ilerleme | Sonraki kaynak / karşı sınama |
|---|---|---|
| Q01 | Review trigger/manual refine/nudge/API aynı mı? | Prologue/cancel/run_review_fork kaynakları var; finalize/manual/alternate yollar açık. |
| Q02 | Whitelist actual çağrıda nerede tüketiliyor? | 06/09/10 tüketici/kurulum bağı; full runtime Q26. |
| Q03 | Read/preview/approve/write aynı hedef revizyonu mu? | U01B2 canlı diff; actual fuzzy/locking/replay/UI binding. |
| Q04 | Pending saklama hatasında kullanıcı ne görür? | Eski U01B kanıtı; actual UI/restart/disk hata dağılımı açık. M2 unlink hatası ayrı Q32. |
| Q05 | Proposer origin, insan onayı, apply ve ownership? | M2/N08 record origin ile supplied caller origin ayrıldı; gerçek CLI/gateway kimliği, home/profil ve live/fresh store ilk aktif iş. |
| Q06 | Cancellation sonrası eski worker/shared-store? | Kaynakta cancel/lock var; M2/N06 yalnız sıralı stale-store reload. Actual stop/çok-caller yarış açık. |
| Q07 | Sonraki session/rebuild bilgiyi ne zaman yükler? | M2 normal/silme/reload disk-live-frozen ayrımını yürüttü; actual AIAgent invalidation/rebuild/request hâlâ açık. |
| Q08 | Aynı/farklı model digest kaybı ve ders kalitesi? | H04 + eval/trajectory; gelecek-task yarar doğrulanmadı. |
| Q09 | Curator merge/rollback semantik olarak ne korur? | H18/H19, ledger/sync; absorbed_into tek oracle değil. |
| Q10 | Session-search summary/raw farkı? | Actual arama implementasyonu ve testleri; wire replay kaynakları yeterli değil. |
| Q11 | Terminal/OS/adapter/session izolasyonu? | Backend/gateway/UI; cooperative policy sandbox sayılmaz. |
| Q12 | Açılmamış alanlar yeni mekanizma getiriyor mu? | F01–F12, recursive envanter/apps/native/compat/eval. |
| Q13 | Boş curator aday kümesi skip literal farkı? | H18 static aday; test kalanı ve default-off sınırı. |
| Q14 | Curator bundled/prune/dry-run prompt vs guard? | Actual curator dispatch; banner mekanik yasak değil. |
| Q15 | Backup/report/cron-reference hatasında ne kalır? | Ledger/backup/cron/restart; gerçek koşu açık. |
| Q16 | Nested batch operations curator raporuna ne taşır? | H18/S01/S02 actual report/cron bağı açık. |
| Q17 | Skill batch exception actual caller'da ne olur? | J07 callback/downstream bounded koşuldu; gerçek skill disk rollback ile entegrasyon hâlâ yok. |
| Q18 | Ortak preview bütün işlemleri temsil ediyor mu? | U01B/U01B2; her UI için read/preview/apply ayrı. |
| Q19 | Directory rollback vs ledger/cache/ownership/sync? | Gerçek yan etkiler ve yazar dışlama; sıralama global kilit değil. |
| Q20 | Özel memory/genel registry ortak denetim? | Ortak dış katman source-backed; full worker policy Q26 açık. |
| Q21 | Error JSON telafi de yapıyor mu? | M2/N02/N09 hata raporu disk/live restorasyonunu sağlamadı; J07 error-origin/once farklı katman. Actual caller readback açık. |
| Q22 | Frozen memory ve aynı-ID context revizyonu? | M2 store snapshot'ı explicit reload'a kadar eski; gerçek compression/prompt/request görünümü açık. |
| Q23 | Command approval vs skill/memory pending? | M2 shared pending command yürütüldü, request/observer/delivery/UI auth zinciri değil. Actual UI bağlantısı sırada. |
| Q24 | Profile/home/DB/cache tutarlılığı? | M2 supplied-store disabled-target ret var; gerçek config refresh/resolver/home/caller bağlama yok. |
| Q25 | Raw/archive/api_content/search/review görünümü? | Sidecar source-backed; tam temsil/compaction eşdeğerliği açık. |
| Q26 | Review whitelist'i worker'da korunuyor mu? | Eski P/C/V + J03/J04/J05 source trace. 22 manuel-range AST eşleşti; full E01/E02 verifier NOT RUN. Bütün runtime/telafi kontrolleri açık, kaynak-bağımlı ileri doğrulama. |
| Q27 | Memory write failure live-store/disk ayrışması? | M2/N02/N09 ile bounded yürütme: pre-commit writer hatası disk eski/live yeni/snapshot eski, hata raporu ve pending korunması, reload/retry toparlanması. Gerçek utils arızaları/UI etkisi/süresi hâlâ açık. |
| Q28 | Batch content/new_text denetim eşdeğerliği? | M2/N07 sentetik sentinel scanner ile ön tarama farkı + load-time masking gözlendi. Gerçek scanner/schema/transport/model-visible sonuç açık; genel bypass hükmü değil. |
| Q29 | Gerçek review valid names dar izne eşit mi? | J03 parent toolset + J04 schema-derived names + ayrı whitelist, standart kurulumda eşitlenmiyor. Tüm later mutations/runtime'lar için hüküm yok. M2 statik notu bağımsız tekrar değil. |
| Q30 | Dispatched/handler/effect işaretleri neyi gösteriyor? | Eski C/V + MW06: ikinci next engellenebilir ama dışarı ilk sonuç dönebilir. Gerçek etki oracle'ı ayrı olmalı. |
| Q31 | Middleware rolü ile hata sözleşmesi uyumlu mu? | Exact J07 MW02 erken kendi Exception'ında devam; MW03 short-circuit, MW04 downstream error, MW08 BaseException ayrı. Gerçek zorunlu policy eklentileri/konfigürasyon açık. |
| Q32 | Successful apply, pending temizleme ve retry aynı mı? | M2/N11 unlink hatasında Approved 1 + pending 1; ikinci add idempotent. Replace/remove/batch, çökme, actual UI feedback ve farklı caller'larda tekrar güvencesi açık. |
| Q33 | Staging uygulanabilirliği doğruluyor mu? | M2/N12 bilinmeyen action listesi staged, apply'de ret/no-write/pending korundu. Actual UI'nin doğrulama/temsil ve hatalı kayıt yönetimi açık. |

## Disposition ve sıra

Q26/Q29 güçlü full-runtime iddiası kapanmadı. Constructor'ın dar ad-kümesiyle otomatik telafi ettiği açıklaması incelenen standart source yolunda desteklenmiyor; fakat gerçek bütün AIAgent/PluginManager/Relay/executor koşusu yok. Tam E01/E02 byte-hash/verifier NOT RUN; manuel-range cross-check bunu ikame etmez. İki transkripsiyonun ortak hata riski vardır.

V0.8'in ilk aktif işi Q05/Q23/Q24 actual pending CLI/gateway/profile/store olarak korunur. Q27/Q28 artık salt statik değildir; M2 bounded koşusu kayda alındı. Gerçek UI ve prompt/request etkisi hâlâ açıktır; aynı 12 fixture yeniden ilk iş yapılmaz. Q32/Q33, actual caller araştırmasına hata/cleanup senaryoları sağlar.

Q26 yeni tam-source/bağımlılık erişimi, ilgili source değişimi veya load-bearing reuse olduğunda yeniden açılır. Aynı eski selected fixture'ların tekrar sayısı yükseltilmez. Bu sıra bir güvenlik veya bütün U01 kapanışı değildir.

J07 fake registry/callback/handler; M2 fake home/config/registry/callback/scanner/writer yardımcısı kullanır. N06 sıralı stale-store örneği, N10 supplied-store flag, N11 duplicate-add örneğidir. Bunlar tüm locking/config/replay güvencesi değildir. 22 AST karşılaştırması yürütme senaryosu sayılmaz. K01–K09'un tamamı koşulmuş değildir; gerçek rebuild/compression/curator deneyleri hâlâ açık. Bu yayın hiçbir deneyi tekrarlamadı; sayılar ürün PASS toplamı yapılmaz ve bütün eski not/kanıtlar korunur.
