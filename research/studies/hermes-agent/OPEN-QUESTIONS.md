# Hermes Agent — Açık sorular

**2026-09-11 / plan v0.16.** Q01–Q39 korunur; Q40–Q44 yeni U04 sınırlarıdır. [V0.15 exact](https://github.com/batuhanozgun/agentic-os-search/blob/13e00420d27547998475ac3d1bcd0d4a492f2229/research/studies/hermes-agent/OPEN-QUESTIONS.md) → [v0.14 Q01–Q37](https://github.com/batuhanozgun/agentic-os-search/blob/25b06521083e2a4ddf7b0dbeb9454804796963b6/research/studies/hermes-agent/OPEN-QUESTIONS.md). Bunlar ürün kusur listesi veya üretim olayı iddiası değildir.

| ID | Current disposition |
|---|---|
| Q12 | U02/U03/U04 + üç provisional sentez; whole native CORE ve geniş F01–F12 açık. |
| Q34 | Task/claim/run/complete/block/review kaynağı + K; şimdi actual quiet goal caller bağlandı. Full dispatcher/OS ve semantic task-quality acceptance açık. |
| Q35 | Expected run ID actual CLI callback'e bağlı; helper status boundary'de superseded durur. G06 judge sırasında değişimde bir callback daha gösterir, gerçek dış etki değil; lower admission/lease açık. |
| Q36 | Task commit/caller/result/delivery ayrımı sürer. G04 helper block outcome gerçek block receipt'i değildir; actual wrapper sonucunu/exit-code'u ayrı tüketir. |
| Q37 | PARTIAL SOURCE + EXECUTION ADVANCE: Kanban goal-mode, session goal, loop, heartbeat ayrı native lifecycle'lar olarak karşılaştırıldı; wait/gate/budget/stop/driver farkları açıklandı. Bütün driver/rotation/restart veya quality hükmü yok. |
| Q38 | Eski K full-parent byte/AST hâlâ NOT VERIFIED. U04 G seçkisi de manual; yalnız S05 tam heartbeat upstream Git kimliği eşleşti. |
| Q39 | Normal worker expected ID aktarır; invalid/missing environment ve low-level operator None yolları tüm caller'larda kapanmadı. |
| Q40 | FIRST NEXT: S10 facade `admit_durable_turn_lease` hangi koşulda history'yi yeniler/değiştirir? Quiet caller listesi, SessionDB transcript ve current session/turn lease nasıl birleşir? turn_facade_lease source429; neither verified-history nor history-loss verdict. |
| Q41 | Goal/loop/heartbeat child-copy/parent-clear migration, save receipt ve actual SessionDB transaction/recovery ile nasıl korunur? H04 yalnız save sınırı; gerçek migration loss gösterilmedi. |
| Q42 | Persisted loop awaiting_response ve heartbeat watch/route, restart/rotation ardından hangi driver admission ile recover edilir? H05 local stale managers ≠ actual gateway duplicate event. |
| Q43 | Run status check → judge → next run callback aralığında ownership loss'u gerçek admission/cancel/worker fence nasıl keser? G05/G06 helper kapsamı; real worker/OS test yok. |
| Q44 | Goal gate oracle/revision binding ve judge evidence scope ne kadar yeterli? Source prefix-limited last response, optional gates ve HEAD+porcelain fingerprint görülür; semantic quality veya unchanged-dirty-content etkisi yürütülmedi. |

Diğer eski Q01–Q33 disposition'ları sessizce kapanmaz. Q07/Q22 normal compaction→API-message source-backed ama final wire/timing/variant açık; Q26/Q29 full-original/full-worker NOT RUN. Review/skill/ledger/sync/scanner/quality ve önceki approval/batch/rollback sınırları korunur.

## Yöntem ve sonraki sıra

[U04 SPEC](evidence/2026-09-11-multi-turn-continuity/SPEC.md) koşudan önce sabitlendi. 15 grup ve 3 negatif kontrol yeni fakat sınırlı kanıt; eski suite rerun veya independent replication değil. Ham gözlem [archive](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz), gezinme [summary](evidence/2026-09-11-multi-turn-continuity/RESULT-SUMMARY.json). Aynı G/H testlerini çoğaltmak Q40–Q43 consumer/driver boşluğunu kapatmaz.

İlk çalışma Q40, gerekli Q41/Q42 bağı; ardından Q43 ve diğer broad families açıklama değerine göre. Q44 güçlü verification/adoption kullanımında yeniden açılır; whole research'ü yalnız judge/gate ayrıntısına kilitlemez. Source erişimi engelliyse açık kayıt ve yeterli bağımsız kenar, seri retry/kısıt dolaşma değil. Yetki STATE'te sınırlıdır.
