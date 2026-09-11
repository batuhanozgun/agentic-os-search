# Hermes Agent — Açık sorular

**2026-09-11 / plan v0.20.** Q01–Q46 kimlikleri korunur; Q47–Q49 U07 cron consumer sorularıdır. Yayın checkpoint'i bu açık soruları veya deney sonuçlarını kapatmaz. [V0.18 exact](https://github.com/batuhanozgun/agentic-os-search/blob/0a475b5d7c50f47689c72cd31f954f5b2303ced6/research/studies/hermes-agent/OPEN-QUESTIONS.md) önceki disposition ve v0.17/v0.16 zincirini taşır. [STATE](STATE.md), [SOURCE-LEDGER](SOURCE-LEDGER.md), [U06](evidence/2026-09-11-resume-admission/RESEARCH.md).

| ID | Current disposition |
|---|---|
| Q12 | U02–U07 native açıklamaları + üç merkezi provisional synthesis; 20/21/22 source amendments. U07 first F10 kesiti, whole cron/CORE/F01–F12/dört-alan kapanışı değil. |
| Q34 | U03 task/claim/terminal ve U04/U05 quiet caller. Actual full dispatcher/OS/task-quality acceptance açık; U06 gateway registry bunların testi değil. |
| Q35 | Expected run ile terminal/superseded ayrımı korunur; A:G06/B:G10 callback timing. Session lease başka bir nesne; physical cancellation veya run ownership otomatik doğrulanmaz. |
| Q36 | Kanban block callback sonucu/durable receipt/exit-code/notification reconciliation açık. Yeni gateway redelivery Q46 ile related, aynı transaction veya aynı soru değildir. |
| Q37 | Kanban goal, session goal/loop/heartbeat farklı driver/state/acceptance mekanizmaları. U06 actual startup/command/post-turn bağlantısını genişletti; whole runtime/quality tamam değil. |
| Q38 | U03 K ve U04 manual Kanban selected-parent fidelity NOT VERIFIED. U06 tam registry module hash/execution yalnız yeni S11'dir; eski borcu kapatmaz. |
| Q39 | Missing/invalid run-ID ve None yolu bütün caller'larda nasıl ayrılır? Açık; U06 genel gateway route bilgisi cevap değildir. |
| Q40 | SOURCE ADVANCED: actual resolve/projection/guard ve gateway load/live-history→agent caller okundu. U05 quiet no-wait/no-rotation history gap'i bounded source inference olarak sürer. **Actual SessionDB + quiet next-request/wire NOT RUN**; yeni selector okuması çağrılmayan immediate reload'u var yapmaz. Eski messages429 current blocker değil. |
| Q41 | U05 transcript atomic publish vs afterward manager save/clear ayrımı korunur. U06 write-adoption/context ayrımı ve local lease alias/refusal açıldı. L03 gerçek DB rotation değil; actual migration fault/same-profile/receipt/heartbeat rebind açık. B:H09 reduced adapter değişmez. |
| Q42 | DEFERRED, NOT CLOSED: startup wrapper tek görülen carrier task'ını bekler; alt gateway/run.py 3150–3325 isteği U07'de 429. Actual preclaim/drain/agent admission, tick-turn kimliği ve full process restart yapılmadı. Plan erteleme kuralıyla broad cron'a geçildi; queue diagnostic bu host sorusunu kapatmaz. |
| Q43 | Actual transcript guard holder mismatch'i reddeder; aynı henüz-reclaimed-olmayan holder'ı expiry sonrası txn içinde yenileyebilir. Agent flush holder geçirir; holder/reject flag olmadan bütün writers bu gate'te değildir. L01–L07 yalnız process-local registry. Real task-run/worker/OS/external-effect fencing açık. |
| Q44 | Goal gate oracle/revision ve prefix-limited judge scope. Gerçek gate effectiveness, dirty-content fingerprint ve model kalitesi yürütülmedi. |
| Q45 | Loop marker/until/count/budget ayrı stop nedenleri; post-turn bağının görülmesi kullanıcı kabulünü veya model completion'ını doğrulamaz. Actual UX/semantic validation açık. |
| Q46 | SOURCE/COMPONENT ADVANCED: gateway redelivery ile cron execution audit ve deliveries queue ayrı store/kimliktir. U07 queue D01 pending+None ve D03/D06 unknown/no retry; terminal tombstone/failure boundaries. Actual gateway delivery ledger ile aynı implementasyon değildir. Cron upper classifier ve downstream UI/receipt integration açık. |
| Q47 | NEW / SOURCE-BOUNDED: scheduled occurrence/late callback/due/claim/rearm nasıl bağlanıyor? Finite one-shot preclaim, recurring preadvance, 600s external backstop vs 120s grace okundu; full callback occurrence identity ve timing NOT RUN. |
| Q48 | FIRST NEXT: actual gateway drainer/profile/transport ve queued/delivered/finished status tüketicileri. Full queue D01 gerçek None+pending; non-local valid-target üst delivered sınıflaması koşullu source inference. Enclosing scheduler/monitoring/real user delivery çalıştırılmadı. |
| Q49 | NEW: shared run_job script/no_agent/agent/preflight/provider ve session/history bağı. Outer caller/read bazı seams görüldü; inner payload/work quality/native backend ve tool effects açık. |

Q01–Q11 ve Q13–Q33'ün eski disposition'ları korunur. Q07/Q22 ordinary compaction→API-message source bağı, final wire/timing/variants açık; Q26/Q29 full-original/full-worker NOT RUN. Skill-ledger/sync/scanner/learning quality ve önceki approval/rollback sınırları devam eder.

## Kanıt ve öncelik

[U06 SPEC](evidence/2026-09-11-resume-admission/SPEC.md)/[RESULT](evidence/2026-09-11-resume-admission/RESULT.json)/[MANIFEST](evidence/2026-09-11-resume-admission/MANIFEST.json): yedi native process-local senaryo ve üç dar negative-control. Bu actual DB/host validation değildir. U05 CHECKS-NOT-RUN eski geniş deney planıdır, yeni L sonuçları onu tamamlamaz.

U04-A/B [uzlaştırması](evidence/2026-09-11-multiturn/RECONCILIATION.md) case/source kimliklerini korur; exact eski hüküm için ilgili raw/probe okunur. A/B/L sayıları toplanmaz, publication kontrolleri davranış deneyi sayılmaz.

U07'nin [SPEC](evidence/2026-09-11-cron-scheduling-delivery/SPEC.md)/[RESULT](evidence/2026-09-11-cron-scheduling-delivery/RESULT.json)/[MANIFEST](evidence/2026-09-11-cron-scheduling-delivery/MANIFEST.json) altı ordinary ve üç negative-control kaydını taşır; tek başarılı behavioral run ve saklanmış pre-case attempt-00 vardır. Source queue full byte; actual SessionDB/full-host/OS/network/model yok. D01 sıfır callback alanı setup açıklaması, diğer recording sayıları actual callback ölçümüdür. Eski sayılara eklenen ürün skoru yok.

U07 yayın makbuzu [PUBLICATION](evidence/2026-09-11-cron-scheduling-delivery/PUBLICATION.md) üzerinden okunur. İlk teknik devam Q48 drainer/receipt; ardından Q47 occurrence/rearm ve Q49 run_job/context. Q40/Q42 explicit deferred; eski source429'ların hepsi tek güncel engel sanılmaz. Current yetki STATE'te, architecture/adoption yok.
