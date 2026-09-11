# Hermes Agent — Araştırma planı

**v0.16 / 2026-09-11 — U04 multi-turn continuation.** Current authority [STATE](STATE.md), method/closure [METHOD](METHOD.md). [V0.15 exact plan](https://github.com/batuhanozgun/agentic-os-search/blob/13e00420d27547998475ac3d1bcd0d4a492f2229/research/studies/hermes-agent/RESEARCH-PLAN.md), [U02 broad map](inventory/CORE-COVERAGE-2026-09-10.md), [U04 update](inventory/CONTINUITY-COVERAGE-2026-09-11.md).

## 1. Hedef ve mevcut aşama

Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest0.21.0; current release değil. Önce native mekanizmalar/sistem ilişkileri, sonra dört-alan ve SOUL/Development OS. Üç provisional sentez vardır: learning/change, turn/context/session, persistent work/continuation. Genel sistem kapsamı hâlâ kısmi; byte/test/file/version sayısından yüzde veya ürün kalitesi çıkarılmaz.

## 2. U04 ve önceki plana etkisi

[18/U04](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md): actual Kanban quiet CLI/callback/helper, session GoalManager, loop cadence/stop ve heartbeat state/driver kaynakları açıldı. G01–G10 selected-function ve H01–H05 verified-full-heartbeat diagnostics yeni koşudur; U03/K recovery veya eski suite tekrar sayılmadı.

Önceki 'aynı işi birkaç turda nasıl sürdürür?' sorusu native yolları ayıracak ölçüde ilerledi: shared judge ≠ shared state/wait/gate/budget; helper stop ≠ durable block receipt; persisted setting ≠ registered driver; same-session ≠ verified history. S10 actual facade, quiet caller history'sinin admission tarafından yeniden seçilebilmesini göstererek erken history-loss hükmüne karşı sınır koydu. Alttaki consumer okunamadı (429).

[Üçüncü sentez](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md) bu partial source ve executable ayrımları taşır. U04 bounded çıktısı hazırdır; whole SessionDB/driver/production veya semantic judge verification kapanmadı.

## 3. İlk sonraki birim — saklanan devam gerçekten nasıl yeniden çalışır?

Soru: **Bir continuation hangi actual session lease ve history ile kabul edilir; rotation/restart sonrasında goal/loop/heartbeat kaydı ile onu ateşleyecek driver/queue nasıl birlikte recover edilir?**

Başlangıç `agent/turn_facade.py::run_conversation` → `agent/turn_facade_lease.py::admit_durable_turn_lease` ve onun gerçek SessionDB/history consumer'ları. İlgili source pin'de açılmalı; default-branch search yalnız navigasyon. Sonra ihtiyaç kadar `goal:/loop:/heartbeat:` meta save/rotation, driver registration ve awaiting-response recovery bağlanır. Bütün SessionDB dosyalarını körlemesine okumak yerine bu geçişi taşıyan caller/transaction'ları takip et.

Çıktı/durma ölçütü: normal bir yeniden girişte history seçimi ve çalışma hakkı; bir interruption veya rotation/restart yolunda kalıcı devam kaydı, live manager, route/driver ve in-flight tick arasındaki kabul/red/telafi açıklanabilmeli. Worker run fence, session turn lease ve provider çağrı izni eşdeğer sayılmamalı. Offline test yapılırsa gerçek consumer+DB sınırına yönelmeli; model/provider/ürün kurulumuna sessiz genişleme yok.

429 tekrar deneme bahanesiyle araştırmayı sonsuz erişim döngüsüne sokma. Erişim tekrar kontrol edilir; okunamayan kenar source-blocked olarak korunur, mevcut bağımsız kaynakla cevaplanabilen kenar seçilebilir. Aynı G/H senaryolarını tekrar üretmek yeni driver coverage değildir.

## 4. Kapsam dengesi ve yeniden açma

U03/K ve U04/G manuel seçkilerin full-parent fidelity borcu ayrı; full S05 hash eşleşmesi bunları kapatmaz. Q26/Q29 full-worker, Q07/Q22 wire/timing, task process cancellation/artifact/delivery, actual model quality açık kalır. Session receipt/migration, pending tick recovery ve actual ownership admission yeni Q40–Q44'tür.

F01–F12 genişliğinden vazgeçilmedi: provider/backend/delegation, actual scheduler/cron/queue, alternatif UI, install/update/eval ve memory/skill ledger/sync/quality sırada yeniden değerlendirilecek. Kalıcı işi yalnız cron altında veya bütün otomasyonu Kanban altında sabitleme. Yeni model açıklama lensidir, ontology değil.

## 5. Yetki ve kapanış

User yeni araştırmaya devamı onayladı; scope HERMES study + catalog HERMES row. Eski evidence/not/syntheses korunur. Agent-control/Foundation/context/Codex/upstream/adoption değişikliği yok. U04 exact raw/source/probe/log archive ve immutable pre-run SPEC, readable source/research/summary ve retrieval state birlikte yayımlanır. Son main parent korunur, scoped diff karşılaştırılır, ref non-force ilerler, içerik geri okunur. Yeni source research, new experiment, synthesis ve publication ayrı raporlanır.
