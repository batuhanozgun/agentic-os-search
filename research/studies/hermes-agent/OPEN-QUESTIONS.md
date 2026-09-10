# Hermes Agent — Açık sorular

2026-09-10 / plan v0.13. Q01–Q33 kimlikleri korunur. [v0.12 tam kayıt](https://github.com/batuhanozgun/agentic-os-search/blob/a14c8152a918a3379b4a0d6d67af9f7aece2f70e/research/studies/hermes-agent/OPEN-QUESTIONS.md) ve [kaynak rotası](SOURCE-LEDGER.md) önceki ayrıntılara döndürür. Bu bir üretim kusur listesi değildir.

| ID | Soru ve current disposition |
|---|---|
| Q01 | Review trigger/manual/refine/nudge/API — kaynaklar kısmi; genel lifecycle'da bağlanır. |
| Q02 | Whitelist actual tüketimi — selected trace var; güçlü hüküm Q26 açık. |
| Q03 | Read/preview/approve/apply aynı revision mı? — U01B2; full binding açık. |
| Q04 | Pending persistence hatası/UI/restart — bounded bileşen kanıtı, actual UI açık. |
| Q05 | Proposer/approver/apply ownership — normal UI source; full record/actor/auth açık. |
| Q06 | Cancel/old-worker/shared-store — sıralı N06 gerçek yarış değil. |
| **Q07** | **M4 ile bounded ilerleme:** fresh store + compatible stored prompt eski metni seçebilir; no-history/null/runtime mismatch rebuild. Gerçek CLI/gateway cache ve son request hâlâ OPEN. |
| Q08 | Digest/öğrenme kalitesi — gelecek-task fayda açık. |
| Q09 | Curator merge/rollback semantik koruma — target beyanı kalite oracle'ı değil. |
| Q10 | Session-search/raw/summary — genel session modelinde önemli açık alan. |
| Q11 | Terminal/backend/OS/adapter sınırı — in-process policy sandbox değil. |
| **Q12** | **İlk aktif kapsam sorusu:** genel turn/context/session ve geniş alt-tree/entrypoint karşı okuması provisional modeli nerede değiştirir? |
| Q13 | Curator boş aday literal skip — source adayı, consolidation default-off sınırı. |
| Q14 | Bundled/prune/dry-run prompt ve guard — actual bütün dispatch açık. |
| Q15 | Backup/report/cron hatasında kalan durum — genel kapsamla bağlanacak açıklama köprüsü. |
| Q16 | Nested operations/report/cron — açıklama köprüsü açık. |
| Q17 | Skill batch exception actual caller — MW/shared UI trace; full disk rollback birleşimi yok. |
| Q18 | Preview/JSON/live target/full diff — temsil ve revision bütünlüğü açık. |
| Q19 | Directory rollback/ledger/cache/ownership/sync — bütün yan etkiler açık. |
| Q20 | Memory special/general registry denetimi — source-backed dış katman; full worker açık. |
| Q21 | Error JSON telafi mi? — M2/MW/M4 durum ayrımları; actual UI readback açık. |
| **Q22** | **M4 source/selected execution:** invalidate reload/clear yapar, tek başına stored DB değiştirmez. V04 harness sırası actual compression değil. Keep-prompt/actual caller/final request OPEN. |
| Q23 | Farklı approval mekanizmaları — A/SA/AP + normal caller trace; full UI değil. |
| Q24 | Profile/home/config/cache/DB — selected wrappers ve fake DB M4; gerçek lifecycle/SQLite açık. |
| Q25 | Raw/archive/api_content/search/review temsilleri — tam eşdeğerlik açık. |
| Q26 | Full review whitelist/worker — E01/E02 full-original verifier ve whole runtime NOT RUN. |
| Q27 | Writer hatası disk/live ayrışması — N02/N09; M4/V06 selector bileşiminde reload toparlanması. Actual UI süre ve failure dağılımı açık. |
| Q28 | content/new_text scanner eşdeğerliği — sentetik scanner; gerçek scanner/model sonucu açık. |
| Q29 | Valid-name/whitelist eşitliği — standard source ayrımı; full runtime açık. |
| Q30 | dispatched/handler/effect — C/V/MW farklı; actual effect oracle gerekir. |
| Q31 | Middleware exception contract — bounded MW; gerçek zorunlu plugin/config açık. |
| Q32 | Apply/cleanup/retry — N11 add idempotence; bütün replay/çökme/full UI açık. |
| Q33 | Staging uygulanabilirliği — N12 staged invalid action; full UI validation açık. |

## Öncelik ve güçlü hüküm sınırı

[Synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md) ilk provisional üst katman; geniş HERMES sistemi değildir. [Kapsam değerlendirmesi](inventory/SCOPE-REVIEW-2026-09-10.md) gereğince genel loop/context/session ve topoloji karşı okuması şimdi aktiftir. Q07/Q22'nin gerçek request bağı burada korunur; çözülmüş gibi görünmez, fakat bütün diğer aileleri durdurmaz.

M4/V01–V08 aynı-investigator/synthetic çevreli selected-source deneyidir. Full parent identity, full prompt builder, actual DB/UI/compression/provider koşusu yok. Fresh build yollarının varlığı da eski stored prompt yolunun varlığı kadar kaydedilir; sürekli bayatlık veya compression arızası hükmü verilmez. Bozuk-source/local-selection ve comparator mutantları sınırlı yanlışları ayırır, full coverage ispatı değildir.

A/SA/AP geçmiş suite'leri tekrarlanmadı; AP original15 arşivlenmiş durumda. Ortak kaynak ve fixture independent corroboration değildir. Q26/Q29 için yeni kaynak/bağımlılık, değişiklik veya load-bearing reuse yeniden açar. Kurulum/provider/credential/upstream/architecture yetkisi genişlemez.
