# Hermes Agent — Açık sorular

2026-09-10 / plan v0.14. Q01–Q33 korunur; U02 ile Q34–Q37 eklenir. [V0.13 tam kayıt](https://github.com/batuhanozgun/agentic-os-search/blob/c163836d959e3ada2f31afd353bb364671b5fb32/research/studies/hermes-agent/OPEN-QUESTIONS.md), [SOURCE-LEDGER](SOURCE-LEDGER.md), [U02 defteri](evidence/2026-09-10-turn-lifecycle/SOURCES.md). Sorular üretimde doğrulanmış kusur listesi değildir.

| ID | Soru ve current disposition |
|---|---|
| Q01 | Review trigger/manual/refine/nudge/API — regular finalizer trigger ve gateway notification release source bağı eklendi; tüm çağırıcılar/gerçek zamanlama açık. |
| Q02 | Whitelist actual tüketimi — selected trace var; güçlü hüküm Q26 açık. |
| Q03 | Read/preview/approve/apply aynı revision mı? — U01B2; full binding açık. |
| Q04 | Pending persistence hatası/UI/restart — bounded bileşen kanıtı; actual UI açık. |
| Q05 | Proposer/approver/apply ownership — normal UI source; full record/actor/auth açık. |
| Q06 | Cancel/old-worker/shared-store — U02 generation/lease-release ve redirect acceptance source; fiziksel cancellation/global writer isolation değil. |
| Q07 | U02 SOURCE-PATH ADVANCE: normal compaction reload/build ve active-prompt→API-message bağı var. Cached/fresh-store tek başına freshness garantisi değil; actual approval-to-wire zaman ve bütün UI/transport paths OPEN. |
| Q08 | Digest/öğrenme kalitesi — gelecek-task fayda açık. |
| Q09 | Curator merge/rollback semantik koruma — hedef beyanı kalite oracle'ı değil. |
| Q10 | Session-search/raw/summary — persistence row/sidecar kaynakla açıldı; actual search/archived retrieval hâlâ açık. |
| Q11 | Terminal/backend/OS/adapter sınırı — in-process policy sandbox değil; alternate app-server gerçek state owner ayrı. |
| Q12 | U02 normal core modeli oluştu; targeted map tam recursive census değil. En yüksek sonraki açıklama boşluğu kanban/kalıcı task kabulü; F01–F12 varyantları açık. |
| Q13 | Curator boş aday literal skip — source adayı, consolidation default-off sınırı. |
| Q14 | Bundled/prune/dry-run prompt ve guard — actual bütün dispatch açık. |
| Q15 | Backup/report/cron hatasında kalan durum — ledger/sync/cron hâlâ köprü; goal/loop/heartbeat migration yeni source pointer. |
| Q16 | Nested operations/report/cron — açıklama köprüsü açık. |
| Q17 | Skill batch exception actual caller — actual round break/persistence source genişledi; full skill rollback entegrasyonu yok. |
| Q18 | Preview/JSON/live target/full diff — temsil ve revision bütünlüğü açık. |
| Q19 | Directory rollback/ledger/cache/ownership/sync — tüm yan etkiler açık. |
| Q20 | Memory special/general registry denetimi — source-backed dış katman; full worker açık. |
| Q21 | Error JSON telafi mi? — U02 pre-effect flush False ile post-effect persistence failure ayrı; rollback/exactly-once değil. |
| Q22 | U02 actual compression normal sırası invalidate/reload→build→byte-equal keep→commit/return. M4 V04 artificial sıra actual bug değil. In-place DB update failure/variant/last-wire runtime OPEN. |
| Q23 | Farklı approval mekanizmaları — A/SA/AP + normal caller source; U02 sync approval callback host bridge; full UI değil. |
| Q24 | Profile/home/config/cache/DB — U02 normal config signature/current-count/source binding; actual all profile/SQLite/lease lifecycle açık. |
| Q25 | Raw/archive/api_content/search/review — actual sidecar/row/API-copy kaynak bağı ilerledi; all modality/provider replay fidelity değil. |
| Q26 | Full review whitelist/worker — E01/E02 full-original verifier ve whole runtime NOT RUN. |
| Q27 | Writer hatası disk/live ayrışması — N02/N09 ve M4/V06 sınırı korunur; actual UI süre/dağılımı açık. |
| Q28 | content/new_text scanner eşdeğerliği — sentetik scanner; gerçek scanner/model sonucu açık. |
| Q29 | Valid-name/whitelist eşitliği — standard source ayrımı; full runtime açık. |
| Q30 | dispatched/handler/effect — actual round/callback/persist source; dış etki oracle'ı farklıdır. |
| Q31 | Middleware exception contract — MW bounded; U02 request/execution aşamaları kaynakta, her mandatory plugin/config doğru çalışıyor hükmü yok. |
| Q32 | Apply/cleanup/retry — N11 add idempotence; bütün replay/crash/full UI açık. |
| Q33 | Staging uygulanabilirliği — N12 invalid action; full UI validation açık. |
| Q34 | FIRST NEXT: Kanban task create/claim/dispatch/run/complete-or-block hangi terminal receipt ile kabul edilir? Stop helper tool-name kontrolü DB kabulü değildir. |
| Q35 | Task claim/run sahibi ile gateway turn lease/generation ve session ID ilişkisi nedir? Alias routing, claim loss ve geç sonuç nasıl bağlanır? Actual consumers açık. |
| Q36 | completed / persistence result / transformed response / delivery acknowledgement nasıl uzlaştırılır? U02 normal kod ayrımı gösterir; crash/full delivery koşusu yok. |
| Q37 | Goal/loop/heartbeat hangi kalıcı amacı birkaç tur boyunca sürdürür? Kanban'la eşdeğer mi? C13 migration pointer var, actual lifecycle henüz açılmadı. |

## Öncelik ve epistemik sınır

U02 general turn/context/session araştırması [synthesis/02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md) ve [CORE-COVERAGE](inventory/CORE-COVERAGE-2026-09-10.md) ile kapanmış bounded source slice'tır; bütün aile veya runtime kapanışı değildir. Yeni HERMES deneyi yok. Q07/Q22 normal caller bağlantısı source ile ilerledi; eski M4 testine actual compression/run sonucu mal edilmedi.

İlk sonraki kalıcı task/terminal acceptance Q34, Q35 ve gerekli SessionDB bağlarıdır; kanban stop helper tek başına yeterli değildir. Ardından Q37 diğer tur-üstü mekanizmalar; bütününün aynı görev modeli olduğu varsayılmayacak. Q26/Q29 için yeni tam kaynak/bağımlılık, source değişimi veya load-bearing reuse gerekir. A/SA/AP/M4 ve eski N/MW/C/V testleri bu tur yeniden koşulmadı, bağımsız doğrulama veya başarı toplamı yapılmaz.

Kaynak erişimi ve yayın continuity'si, kaynak iddiası/behavior/quality doğrulamasından ayrıdır. Kurulum/provider/credential/upstream/control/Foundation/adoption sınırı değişmedi.
