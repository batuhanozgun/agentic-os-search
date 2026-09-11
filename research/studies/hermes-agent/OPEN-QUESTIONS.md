# Hermes Agent — Açık sorular

**2026-09-11 / plan v0.17.** Mevcut Q01–Q44 kimlikleri korunur; B'nin eski aday Q45'i loop stop semantiği olarak kayda alınır. [V0.16 exact](https://github.com/batuhanozgun/agentic-os-search/blob/a0585203ca0a2bdd1cc8441aa152d7e4a72128cf/research/studies/hermes-agent/OPEN-QUESTIONS.md) → [V0.15](https://github.com/batuhanozgun/agentic-os-search/blob/13e00420d27547998475ac3d1bcd0d4a492f2229/research/studies/hermes-agent/OPEN-QUESTIONS.md) → [V0.14](https://github.com/batuhanozgun/agentic-os-search/blob/25b06521083e2a4ddf7b0dbeb9454804796963b6/research/studies/hermes-agent/OPEN-QUESTIONS.md). Eski sorular sessizce kapatılmaz. [STATE](STATE.md), [SOURCE-LEDGER](SOURCE-LEDGER.md).

U04-A = önceden yayımlanmış 15 grup; U04-B = ayrı 21-durumlu teslim. A/B ayrımı eski UI/A serisinden farklıdır. Bu tur yeni deney yapılmadı. B-draft Q40–Q44 numaraları canonical numaraların yerine uygulanmadı; [eşleme](evidence/2026-09-11-multiturn/RECONCILIATION.md).

| ID | Current disposition |
|---|---|
| Q12 | U02/U03/U04 açıklamaları + üç merkezi provisional sentez; B ayrıca korunmuş delivery'dir, dördüncü model değildir. Whole CORE/genel F01–F12 açık. |
| Q34 | Task/claim/complete/block/review kaynağı ve K; actual quiet goal caller A/B kaynak kayıtlarında. Full dispatcher/OS ve semantic task-quality acceptance açık. |
| Q35 | Expected run ID actual CLI callback'e bağlı. B:G02/G03 manual run-status/SQLite-fixture okuyucusunu terminal/superseded durumlarına bağlar; A:G06/B:G10 geçiş sırasında ek callback sınırı gösterir. Physical cancellation değil. |
| Q36 | Commit/caller/outcome/delivery ayrı. A:G04 budget block callback'i; B:G08/G09 judge BLOCKED dalı. Başarısız block sonucu gerçek dispatcher tarafından nasıl recover edilir? Actual receipt/exit-code/notification consumer açık. |
| Q37 | Kanban goal-mode, session goal, loop, heartbeat native state/trigger/wait/gate/budget/driver farkları açıklanmış bounded kesit. B yayını yeni koşu değildir; bütün driver/rotation/restart/quality kapanışı yok. |
| Q38 | K ve U04 Kanban seçkilerinin full-parent byte/AST sadakati NOT VERIFIED. A/B yalnız heartbeat full-original kimliğini eşler; bütün runtime'a yayılmaz. |
| Q39 | Normal worker ID aktarımı ile invalid/missing environment/operator None yolu bütün caller'larda nasıl ayrılır? Açık. |
| Q40 | FIRST NEXT: A:S10 facade `admit_durable_turn_lease` hangi koşulda history'yi yeniler/değiştirir? Quiet caller listesi, SessionDB transcript, session/turn lease nasıl birleşir? Önceki source429 yeniden kontrol edilir; ne verified-history ne history-loss verdict'i var. |
| Q41 | Goal/loop/heartbeat child-copy/parent-clear, save receipt ve actual SessionDB transaction/recovery nasıl korunur? B:H08/H09 normal/migration selective-write-fault kayıtları artık erişilebilir; helper True/child yok/parent cleared azaltılmış adaptör sınırıdır. Gerçek DB/compaction migration loss gösterilmedi. |
| Q42 | Persisted loop awaiting_response, heartbeat watch/route restart/rotation sonrası hangi driver admission ile recover edilir? A:H05 local stale managers gerçek duplicate gateway event değildir; B:H05/H06 abandon senaryolarıyla karıştırılmaz. |
| Q43 | Status check → judge → next run aralığında ownership loss'u actual admission/cancel/worker fence nasıl keser? A:G05/G06 ve B:G03/G10 sınırlı yardımcı/reader kanıtı, gerçek process/OS testi yok. |
| Q44 | Goal gate oracle/revision binding ve judge evidence scope yeterliliği? Prefix-limited response ve HEAD+porcelain fingerprint source gözlemi; unchanged-dirty-content/gate effectiveness/model quality yürütülmedi. |
| Q45 | B-draft'tan korunan açık soru: `/loop` marker/until/requested-count sonlanması, durum mesajı ve kullanıcı kabul koşulu nasıl eşleştirilir? Kaynakta ayrı nedenler var; actual model/UX semantik doğrulaması yok. |

Q01–Q11 ve Q13–Q33'ün önceki disposition'ları değişmez. Q07/Q22 ordinary compaction→API-message source bağı var, final wire/timing/variants açık. Q26/Q29 full-original/full-worker NOT RUN. Review/skill/ledger/sync/scanner/quality ve eski approval/batch/rollback sınırları korunur.

## Kanıt ve sıra

[A SPEC/raw archive](evidence/2026-09-11-multi-turn-continuity/SPEC.md) ve [B SPEC/raw RESULT](evidence/2026-09-11-multiturn/delivery/evidence/SPEC.md) ayrı özgün girdilerdir; B tam [RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json) doğrudan erişilir. Yük taşıyan exact claim için ilgili tam raw/probe okunur; browsing summary yetmez. Hash/parse transfer kontrolü source equivalence, yeni execution veya independent replication değildir.

İlk teknik araştırma Q40 ve gerekli Q41/Q42 bağlantısıdır; B migration bulgusu A'nın facade/history girişini atlatmaz. Q43 ve broad families açıklama değerine göre, Q44 güçlü verification/adoption reuse'ta yeniden açılır. Q45 planı sınırsız yeni yan dala dönüştürmez. Yetki STATE'tedir; bu yayın yeni teknik çalışmayı başlatmadı.
