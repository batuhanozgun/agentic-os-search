# Hermes Agent — STATE

**Durum:** ACTIVE PARTIAL RESEARCH / U04 MULTI-TURN CONTINUATION AND THIRD PROVISIONAL SYNTHESIS  
**Son kayıt:** 2026-09-11.  
**Primary:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current-release doğrulaması değil.  
**Plan:** [v0.16](RESEARCH-PLAN.md). **Bütün HERMES araştırması tamamlandı mı? HAYIR.**

## Güncel amaç ve yetki

Önce HERMES-native mekanizma/sistem açıklaması, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesi. Kullanıcı v0.15 sonrası çok turlu Kanban goal-mode ve goal/loop/heartbeat araştırma planını uygun bulup operasyonel sınıra kadar devamı yetkilendirdi. **U04 yeni kaynak araştırması ve yeni sınırlı deneydir; önceki U03 yayın kurtarmasının tekrar raporu değildir.**

Yalnız `research/studies/hermes-agent/**` ve CATALOG'daki HERMES satırı değişebilir. Bütün ürünü kurma/çalıştırma, model/provider/gerçek credential, upstream mutation, Codex işi, Foundation/control/context/architecture/adoption yetkisi yoktur. Sentetik çevre ile güvenli sınırlı offline deneyler bu araştırma kapsamında kalır. Codex başka repo kullanır; main hareketleri ona atfedilmez. Yanıtlar arasında otomatik/background iş veya uygulama/izin değişikliği yapılmaz. OpenClaw ayrı adaydır.

## Bu tur ne ilerledi?

[18/U04](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → [RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md), [SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [SPEC](evidence/2026-09-11-multi-turn-continuity/SPEC.md).

Actual quiet CLI → Kanban goal helper → expected-run status/block callbacks bağlandı. Judge DONE doğrudan task commit değil, finalize nudge üretir. Terminal worker/review handoff ve superseded ayrı durma nedenleridir. Helper outcome, block callback receipt'i ve process exit-code farklıdır.

Session GoalManager kontrat/gate/wait/parse-transport counters taşır; Kanban helper bunlarla eşdeğer değildir. Loop'un cadence/tick/marker/until/times kabulü ve heartbeat'in idle recurring istemi ayrı state/driver kullanır. Gateway persisted-loop scan ile memory-only heartbeat watch ayrımı kaynakta görüldü. Settings persistence, live state, driver registration, queued turn ve prepared context eşitlenmedi.

**Yeni yürütme:** G01–G10 manuel tam-function Kanban seçkisi + sentetik callbacks; H01–H05 Git kimliği eşleşen TAM heartbeat.py + gerçek geçici SQLite adapter + sentetik saat. 15 grup ve üç sınırlı negatif kontrol beklentilerle eşleşti. Raw koşu `2026-09-11T06:10:29.139368+00:00`. G04 block receipt ayrımı, G06 judge sırasında ownership-loss callback penceresi, H04 live/durable fire ayrışması, H05 iki stale manager'ın atomic claim olmaması gözlendi. Gerçek worker/driver/race/delivery veya ürün güvenlik hükmü değildir.

[Tam arşiv](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz) dokuz dosya taşır; [MANIFEST](evidence/2026-09-11-multi-turn-continuity/MANIFEST.json) exact kimliklerdir. [RESULT-SUMMARY](evidence/2026-09-11-multi-turn-continuity/RESULT-SUMMARY.json) yalnız gezinme görünümü; exact gözlem/probe için arşiv açılır. Spec önceden Git blob olarak sabitlendi. Source/fixture/negative-control sınırları arşivde korunur; aynı modelin deneyi bağımsız replication sayılmaz.

[Üçüncü geçici sentez](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md), U02 iç tur ile U03 kalıcı görev ve U04 devam yollarını bağlar. [Yeni kapsam kontrolü](inventory/CONTINUITY-COVERAGE-2026-09-11.md) geniş F01–F12'yi ve açık consumer'ları korur. Bu nihai HERMES CORE/dört-alan/adoption değildir.

## Açık kalan kritik bağlantı

S02 quiet callback'i history'yi yeniden verir; S08 onu kopyalar. Ancak S10 `agent/turn_facade.py`, `admit_durable_turn_lease` sonucundaki history ile girdiyi değiştirebilir. **Bu nedenle ne same-session → kayıpsız bağlam, ne doğrudan history-loss bug hükmü verildi.** Actual `agent/turn_facade_lease.py` 429 aldı; bu consumer okunamadı. Ek loops aralığı da 429 aldı; var olan okumaların yerine yeni erişim uydurulmadı.

Bir ayarın kaydı ile tekrar ateşlenecek driver, durable awaiting_response ve migration/rebind kabulü açık. Goal/loop/heartbeat best-effort save/migration source yolları universal atomic transfer garantisi değildir. H04 yalnız full heartbeat save sınırını çalıştırdı; actual SessionDB veya rotation failure testi değil.

## Korunan önceki kanıt

01–17 notları, syntheses/01–02 ve eski evidence değişmeden korunur. [V0.15 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/13e00420d27547998475ac3d1bcd0d4a492f2229/research/studies/hermes-agent/STATE.md) U03/K recovery ayrıntısını taşır. U03 original15 kapanışı tamamdır; eski 'yayımlanmadı/ilerleme yok' ifadeleri tarihsel düzeltilmiş kayıtlardır.

Q07/Q22 normal compaction→API-message source bağı durur; actual wire/timing/all variants açık. Q26/Q29 full-original/full-worker NOT RUN; U03 K full-parent fidelity Q38 açık. U04'te yalnız S05 full-byte kimlik eşleşmesi, eski E/K/goal seçkilerini doğrulamış sayılmaz. A/SA/AP/N/M4/K ve upstream suite'ler yeniden çalıştırılmadı. Gerçek model/goal judge/gate efficacy, profiles, process cancellation, artifact/notification ve gelecek-task kalite açık.

## İlk sonraki yetkili araştırma birimi

**Session-bound devamın actual SessionDB/turn lease/history ve rotation/restart driver'ına bağlanması.** S10'un `admit_durable_turn_lease` çağrısından başla; ilgili current source erişimini yeniden kontrol et, gerekli SessionDB/history refresh/append/restore consumer'ına in. Bir continuation kuyruğa girdiğinde hangi geçmişle hangi session'da yürütüldüğünü, session rotasyonunda devam kaydı/route/manager'ın nasıl yeniden bağlandığını ve in-flight loop/heartbeat durumunun recovery sınırını aç.

Normal yol + bir interruption/rotation/restart karşı yolu yeterli bounded çıkış hedefidir; full product testi gerekmez. Yeni deneyi aynı G/H fakes'i çoğaltmak yerine gerçek consumer/DB geçişine yönelt; source identity ve fixture sınırlarını koru. Erişim kapalıysa repeated retry veya kısıt dolaşma yok; desteklenebilen bağımsız kenarı araştır veya açık boundary ile dur. Claim-loss actual admission, whole-driver dedupe ve semantic quality birbirinin yerine geçmesin.

Daha sonra task cancellation/delegation, scheduler/cron/delivery, provider/backend, skill ledger/sync/quality ve diğer UI/install/eval kapsamı yeni modele göre yeniden seçilir. Tüm eski security residual'larını kapatmak diğer ailelerin araştırılmasının ön koşulu değildir; güçlü reuse/security/adoption hükmü için ilgili borç yeniden açılır.

## Cold start ve yayın

Bootstrap → research root/studies catalog → META/STATE/INDEX → METHOD/plan v0.16 → **synthesis/03 + 18/U04 RESEARCH/SOURCES/SPEC/RESULT-SUMMARY/PUBLICATION + CONTINUITY-COVERAGE**. Exact G/H iddiası için committed archive/manifest. İç tur için synthesis/02/U02, task transaction için17/U03/K. Sohbet ZIP'ine ihtiyaç yoktur.

İlk head13e0042 iken yayın hazırlığında e335438'e ilerleme görüldü; compare yalnız Foundation değişiklikleri gösterdi ve güncel tree taban alındı. Son yayın non-force ref ve current content readback ile doğrulanır. Blob/tree/commit oluşması tek başına main yayını değildir. Dosya/test/plan sayısı tamamlanma yüzdesi değildir.
