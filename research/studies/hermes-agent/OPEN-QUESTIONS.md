# Hermes Agent — Açık sorular

2026-09-10 / plan v0.12. Q01–Q33 kimlikleri korunur. [v0.11 ayrıntılı tablo](https://github.com/batuhanozgun/agentic-os-search/blob/634ab66f195130d551d58dfc062639e0feec23fa/research/studies/hermes-agent/OPEN-QUESTIONS.md) kaynak/koşu ayrıntılarının tam önceki kaydıdır. AP yayını hiçbir teknik soruyu full-runtime düzeyinde kapatmaz. Bu bir kusur listesi değildir.

| ID | Soru ve current disposition |
|---|---|
| Q01 | Review trigger/manual/refine/nudge/API varyantları — kaynaklar kısmi. |
| Q02 | Whitelist actual tüketimi — selected trace var; Q26 strong claim açık. |
| Q03 | Read/preview/approve/apply hedef revizyonu — U01B2 canlı diff; full binding açık. |
| Q04 | Pending persistence hatası ve kullanıcıya sonuç — bileşen kanıtı var, UI/restart açık. |
| Q05 | Proposer/approver/apply ownership — normal UI source bağlı; bütün record/actor/auth yolları açık. |
| Q06 | Cancel/old-worker/shared-store — N06 sıralı reload; gerçek yarış ve stop sonrası etkiler açık. |
| **Q07** | **İlk aktif:** approval sonrası store/frozen/stored-cached prompt/prepared request. |
| Q08 | Review digest ile ders kalitesi — gerçek gelecek-task fayda açık. |
| Q09 | Curator merge/rollback semantik koruma — hedef beyanı kalite oracle'ı değil. |
| Q10 | Session search summary/raw — temel arama/temsil yolları açık. |
| Q11 | Terminal/backend/OS/adapter izolasyonu — in-process policy sandbox değil. |
| Q12 | Açılmamış aileler modeli değiştirir mi? — ara sentez sonrası geniş topoloji kontrolü. |
| Q13 | Curator boş aday literal skip — kaynak adayı, consolidation default-off sınırı. |
| Q14 | Bundled/prune/dry-run prompt ve guard — actual bütün dispatch açık. |
| Q15 | Backup/report/cron hatasında kalan durum — açıklama köprüsü olarak sırada. |
| Q16 | Nested operations/report/cron ilişkisi — açıklama köprüsü olarak sırada. |
| Q17 | Skill batch exception gerçek caller — bounded MW ve shared UI trace; full disk rollback birleşimi yok. |
| Q18 | Preview temsil kapsamı — canlı target, kesilen chat diff, pending JSON ve full diff ayrı. |
| Q19 | Directory rollback ile ledger/cache/ownership/sync — yan etkilerin bütünlüğü açık. |
| Q20 | Special memory/general registry denetimi — source-backed dış katman; full worker açık. |
| Q21 | Error JSON ve telafi — N/MW ayrımları var; gerçek UI readback açık. |
| **Q22** | **Q07 ile aktif:** invalidation, DB restore, compression/keep-prompt ve aynı session tazeliği. |
| Q23 | Farklı approval mekanizmaları — A/SA/AP policy ve actual normal caller trace; full UI koşusu değil. |
| Q24 | Profile/home/config/cache/DB — wrappers ve supplied-config sınırlı; full lifecycle açık. |
| Q25 | Raw/archive/api_content/search/review temsilleri — bütün eşdeğerlik açık. |
| Q26 | Full review whitelist/worker — E01/E02 full-original verifier ve full runtime NOT RUN. |
| Q27 | Memory write failure disk/live ayrışması — N02/N09 bounded; gerçek caller etkisi/süresi açık. |
| Q28 | content/new_text scanner eşdeğerliği — sentetik scanner farkı; gerçek scanner/model sonucu açık. |
| Q29 | Review valid-name vs whitelist — standard source ayrımı; full runtime açık. |
| Q30 | dispatched/handler/effect işaretleri — C/V/MW ayrı; gerçek effect oracle gerekli. |
| Q31 | Middleware exception contract — bounded MW; gerçek zorunlu plugin/config açık. |
| Q32 | Apply/cleanup/retry — N11 add idempotence; diğer replay/çökme/full UI açık. |
| Q33 | Staging uygulanabilirlik — N12 staged invalid action; full UI validation açık. |

## Öncelik ilkesi

[Kapsam değerlendirmesi](inventory/SCOPE-REVIEW-2026-09-10.md) açık soruları açıklama köprüsü, daha güçlü hüküm için ileri doğrulama ve keşfedilmemiş kapsam olarak ayırır. Her OPEN madde bir sonraki araştırmanın ön koşulu değildir.

AP teslimi artık [14](notes/14-AP-DELIVERY-RECONCILIATION.md) ve özgün arşivle ayrılır. A/SA/AP aynı modül fakat farklı kod/senaryo; bağımsız kanıt veya toplu PASS değil. AP06 eksik principal/policy, AP03 literal/canonical ayrımı; SA06/SA08 deployment kusuru sayılmaz. A'nın semantic mutantı diğerlerine atfedilmez.

İlk teknik birim Q07/Q22. Ardından geçici öğrenme/değişim sentezi, geniş topoloji kontrolü ve ledger/skill-cache/curator köprüleri. Q26/Q29 yeni tam kaynak/bağımlılık, source değişimi veya load-bearing reuse ile yeniden açılır; aynı selected fixture'ları çoğaltmak full-runtime kanıtı değildir. Mevcut kullanıcı yetkisi kurulum/provider/credential/upstream değişikliğine uzanmaz.
