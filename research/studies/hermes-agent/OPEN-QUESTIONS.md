# Hermes Agent — Açık sorular

**2026-09-10 / ACTIVE / plan v0.11.** Sorular üretimde doğrulanmış kusur listesi değildir. [Birikimli rota](SOURCE-LEDGER.md), [D caller](evidence/2026-09-08-context-transfer/SOURCES.md), [E/C/V](evidence/2026-09-08-worker-policy/SOURCES.md), [J/MW](evidence/2026-09-09-review-middleware/SOURCES.md), [M2/N](evidence/2026-09-09-memory-pending/SOURCES.md), [UI/A](evidence/2026-09-10-ui-profile/SOURCES.md), [ayrı M3-S/SA](evidence/2026-09-10-pending-caller/SOURCES.md). [V0.10 tam soru kaydı](https://github.com/batuhanozgun/agentic-os-search/blob/159936556f34e7e0e1dafcb54c087bef994cf5ba/research/studies/hermes-agent/OPEN-QUESTIONS.md) önceki ayrıntıları korur; Q01–Q33 ID'leri değişmedi.

| ID | Açık ayrım / mevcut ilerleme | Sonraki kaynak / karşı sınama |
|---|---|---|
| Q01 | Review trigger/manual refine/nudge/API aynı mı? | Prologue/cancel/run_review_fork kaynakları var; finalize/manual/alternate yollar açık. |
| Q02 | Whitelist actual çağrıda nerede tüketiliyor? | 06/09/10 tüketici/kurulum bağı; full runtime Q26. |
| Q03 | Read/preview/approve/write aynı hedef revizyonu mu? | U01B2 canlı diff; M3 gateway preview kesintisi ve ortak apply source bağı. Actual fuzzy/locking/revision-binding ve diğer UI'ler açık. |
| Q04 | Pending saklama hatasında kullanıcı ne görür? | Eski U01B kanıtı; actual UI/restart/disk hata dağılımı açık. M2 unlink hatası ayrı Q32. |
| Q05 | Proposer origin, insan onayı, apply ve ownership? | M3 normal CLI/gateway ingress/slash/shared apply kaynağı; command-family grant ile kayıt/alt-işlem yetkisi ayrıldı. Record origin insan kimliği değil; per-record ownership ve bütün auth/hook yolları açık. |
| Q06 | Cancellation sonrası eski worker/shared-store? | Kaynakta cancel/lock var; M2/N06 yalnız sıralı stale-store reload. M3 idle-only kuralı global çok-yazar kilidi değil. Actual stop/yarış açık. |
| Q07 | Sonraki session/rebuild bilgiyi ne zaman yükler? | İlk aktif iş: M3 CLI live/fresh ve gateway fresh apply → cached-agent reuse/store reload/stored prompt/prepared request. M3-S12/S13 source bağı var; `_restore_or_build_system_prompt` sonraki somut soru. |
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
| Q18 | Ortak preview bütün işlemleri temsil ediyor mu? | U01B/U01B2 + M3 gateway 3000-karakter kesintisi/sabit home ipucu; pending JSON immutable diff değildir. Full-diff okumasının apply ön şartı gösterilmedi; her UI/revizyon/profil için açık. |
| Q19 | Directory rollback vs ledger/cache/ownership/sync? | Gerçek yan etkiler ve yazar dışlama; sıralama global kilit değil. |
| Q20 | Özel memory/genel registry ortak denetim? | Ortak dış katman source-backed; full worker policy Q26 açık. |
| Q21 | Error JSON telafi de yapıyor mu? | M2/N02/N09 hata raporu disk/live restorasyonunu sağlamadı; M3 caller nesne ömrü source-backed. J07 error-origin/once farklı katman. Actual UI readback açık. |
| Q22 | Frozen memory ve aynı-ID context revizyonu? | Q07 ile aktif: approve ile approval/mode eviction farklı. M3-S12/S13 build/invalidate/cache source trace var; DB restore/compression/keep-prompt/request ölçümü açık. |
| Q23 | Command approval vs skill/memory pending? | M3 shared handler/mode setter ve ayrı approvals admin kontrolü kaynakta. UI/A ve ayrı SA policy koşuları bütün UI/admission execution değildir. |
| Q24 | Profile/home/DB/cache tutarlılığı? | M3 wrappers/transport damgası/context-home kaynakta; pairing source.profile ile supplied slash config farklı. SA06 profile-only/config duyarlılığı deployment açığı değil. Full route/auth resolver/config/cache/setup failure açık. |
| Q25 | Raw/archive/api_content/search/review görünümü? | Sidecar source-backed; tam temsil/compaction eşdeğerliği açık. |
| Q26 | Review whitelist'i worker'da korunuyor mu? | P/C/V + J source trace; 22 manuel-range AST, full E01/E02 verifier NOT RUN. Bütün runtime/telafi kontrolleri açık. |
| Q27 | Memory write failure live-store/disk ayrışması? | M2/N02/N09 bounded pre-commit hatası, hata/pending koruma, reload/retry; M3 live/fresh source bağı. Gerçek utils arızaları/UI etkisi/süresi açık. |
| Q28 | Batch content/new_text denetim eşdeğerliği? | M2/N07 sentetik scanner ön tarama farkı + load-time masking. Gerçek scanner/schema/transport/model sonucu açık; genel bypass değil. |
| Q29 | Gerçek review valid names dar izne eşit mi? | J03 parent toolset + J04 schema names + ayrı whitelist standard path'te eşitlenmiyor. Tüm later/runtime'lar açık; M2 notu bağımsız tekrar değil. |
| Q30 | Dispatched/handler/effect neyi gösteriyor? | C/V + MW06 ikinci next engellenirken ilk sonuç dönebilir. Gerçek etki oracle'ı ayrı gerekir. |
| Q31 | Middleware rolü ile hata sözleşmesi uyumlu mu? | MW02 erken own Exception devam; MW03 short-circuit/MW04 downstream/MW08 BaseException ayrı. Gerçek zorunlu eklenti/config açık. |
| Q32 | Successful apply, cleanup ve retry aynı mı? | N11 Approved 1 + pending 1, add idempotent. M3 shared UI source bağı; replace/remove/batch/crash/gerçek UI fault injection açık. |
| Q33 | Staging uygulanabilirliği doğruluyor mu? | N12 bilinmeyen action staged, apply ret/no-write/pending. Actual caller source bağı full UI validation/hatalı kayıt yönetimi değildir. |

## Disposition ve sıra

Normal CLI/gateway pending caller → home/supplied-store bağı kaynakla ilerledi. İlk aktif iş Q07/Q22 onaydan stored-prompt/prepared-request görünürlüğüdür. M3-S12/S13 üzerine `_restore_or_build_system_prompt`, compression/keep-prompt ve cached-agent yaşam döngüsü açılır. Yeni store'un eski DB prompt'unu restore edip etmediği peşinen kabul edilmez.

Komut ailesine yetki kayıt okuma iznine eşit değildir; transport admission, canonical slash policy, runtime profile ve kayıt sahipliği ayrı kalır. Q05/Q23/Q24'te full route/auth resolver, config'in hangi profile'dan geldiği, multi-session cache, hook rewrite sonrası yeniden-yetkilendirme, gerçek UI fault injection açıktır. SA06 ve SA08 deployment/adapter kusuru ilan edilmez; aynı normal handler'lar ilk kez bulunacakmış gibi başa alınmaz.

Q26/Q29 güçlü full-runtime iddiası kapanmadı. Tam E01/E02 byte-hash/verifier NOT RUN; manuel-range cross-check ikame değildir. Yeni tam-source/bağımlılık, source değişimi veya load-bearing reuse yeniden açar. Aynı selected fixture sayısı artırılmaz.

UI/A01–A08 ve ayrı M3-S/SA01–SA08 aynı modül fakat farklı kod/senaryo/koşu/negatif kontrol kayıtlarıdır; birbirine aktarılmaz. A'daki always-allow mutantı SA'ya mal edilmez; örtüşen source gözlemleri bağımsız kanıt sayılmaz. Gerçek gateway/profile/store/handler/provider çalıştırılmadı; UI09/M3-S10 test kaynakları NOT RUN. Bu yayın hiçbir yeni deney yapmadı. N06/N10/N11 ve J/MW/C/V/P sınırları korunur; sayılar ürün PASS toplamı değildir.

[13 yayın uzlaştırması](evidence/2026-09-10-pending-caller/PUBLICATION.md) 1599365'teki 12/UI çalışmasının korunmasını ve ZIP'teki ayrı kanıtın eklenmesini açıklar. Tarihsel NOT PUBLISHED/eski taslak/plan ifadeleri current engel sayılmaz.
