# Hermes Agent — Araştırma planı

**v0.23 / 2026-09-12 — U10 yayımlı; Q53 başlangıç checkpoint'i etkin.** [STATE](STATE.md) authority; [METHOD](METHOD.md) yöntem; [MAP](CURRENT-RESEARCH-MAP.md) derived büyük resim; [U10 PUBLICATION](evidence/2026-09-12-cron-execution-context/PUBLICATION.md) tamamlanmış yayın. Primary c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a / manifest 0.21.0.

## Onaylanan incremental kayıt düzeni

Kullanıcı “Tamam devam et lütfen” diyerek önce anlamlı başlangıç kaydı→main geri okuma→küçük araştırma dilimi→yayın/geri okuma sırasını onayladı. Başlangıç ref'i 595d9ebb24302e271b9f84cc86d0debbd74dc790. Bu checkpoint teknik bulgu veya yeni deney değildir; çalışma sırası kaydıdır. U10 kanıtları ve açık sorular değişmez.

Q53 iki anlamlı dilimle ilerletilir: (A) provider/model/api_mode çözümleme→istemci→gerçek dispatch ayrımı; (B) doğrudan model yolu ile maddi farklı backend'in history/tools/fallback/cancel/cleanup sahipliği karşılaştırması. A yayımlanıp geri okunmadan B büyütülmez. Tam olmayan bir A kaydı completed Q53 diye etiketlenmez. Kaynak zinciri daha uygun bir bölünme gerektirirse gerekçe kaydedilir. Yazma kesilirse yeni büyük dilim değil, mevcut dilimin yayın devri çözülür.

## Gerçek ilerleme ve revizyon gerekçesi

Kayıtlı Q49, normal agent ile no_agent/script yolları ve monitor/wake gate'leri üzerinden kaynakla ilerledi. Model/preflight/tools/profile/cwd/session/history/persistence consumer'ları açıldı. Yalnız tam native scheduler_prompt.py'nin previous-output selector'ı altı bounded local-file vaka ile çalıştırıldı; model/DB/host koşusu yok. [Note25](notes/25-CRON-EXECUTION-AND-CONTEXT.md) → [RESEARCH/SOURCES](evidence/2026-09-12-cron-execution-context/README.md).

U07–U10 artık yalnız ayrı notlar değildir: [synthesis04](synthesis/04-SCHEDULED-WORK-AND-CONTEXT-PROVISIONAL.md) scheduled-work zincirini ve açık kenarları ilk geçici modelde birleştirir. Eski synthesis01–03 korunur. Yeni 04 final/complete CORE değildir. Bu, source→mekanizma→ara-sentez→karşı-okuma yönteminin devamıdır; araştırma konusu veya mimari aşama değişikliği değildir.

U10'un en güçlü yeni ayrımları: fresh agent ile çok-kanallı persistent context; newest output ile useful/confirmed response; detection checkpoint ile successful handling; input workdir ile actual subprocess cwd; operational success ile semantic completion. Bunların bütün failure varyantlarını tüketmek yerine, ortaya çıkan provider/runtime sahipliği boşluğu geniş açıklama değeri nedeniyle öne alınır.

## İlk yeni geniş source birimi — Q53

**Soru:** declared provider/model/api_mode, hangi actual runtime/backend tarafından yürütülür; fallback/context/cancellation/resource sahipliği nerede değişir?

Başlangıç `hermes_cli/runtime_provider.py::resolve_runtime_provider` → `agent/agent_init.py::_resolve_api_mode/_build_client` → turn/backend dispatch. En az normal doğrudan model yolu ve maddi farklı bir harici/native backend okunmalı. Declared/model-config, effective runtime, gerçek request/backend kabulü ve kalıcı oturum görünümü ayrı tutulmalı. Önceki U02 iç-turn sentezi bu iki yola karşı okunmalı; aynı constructor sınıfı aynı history owner demek değildir.

Çıkış: hangi aktörün model isteğini, araç yürütmesini, history/compaction'ı, stop/cancel'i ve kapanışı yönettiği; fallback'in hangi alanları değiştirip hangilerini koruduğu kaynakla açıklanabilsin. Exact alt sınırlar kayıtlı kalsın. Bütün provider kataloğu, her eklenti veya her platform kombinasyonu bu birimin kapsamı değil. Full product/model/credential/NAS çağrısı yok; yalnız gerekliyse tam source ve önceden sabit oracle ile güvenli diagnostic.

## Ayrı residual validation hattı

Q49 full accepted→run_job→agent/script/first-request; Q51 gerçek producer→selector→request/quality; Q52 monitor checkpoint→failed downstream→next unchanged tick ve storage races. [U10 NOT RUN](evidence/2026-09-12-cron-execution-context/CHECKS-NOT-RUN.md). Cwd, late DB/teardown, config/preflight/permission ve semantic completion burada residual'dır.

Q47 late-callback/NAS/store/clock, Q48/Q50 actual transport/status/cancellation/seeding, Q40/Q42 actual SessionDB quiet-history/startup kabulü ve eski Q41/Q43/Q44/Q45/Q07/Q22/Q26/Q29/Q38 aynı statüde açık. Bir alanın tam dependency erişimi, yeni karşı kanıt veya güçlü reliability/adoption kullanım ihtiyacı doğduğunda ilgili ölçüm yeniden açılır. Erteleme kapanış değildir; bütün fault matrix broad araştırmanın ön koşulu yapılmaz.

## Geniş kapsam, sonraki sıralama ve yetki

Q53 sonrası kanıta göre delegation/concurrency ve tool/plugin policy bağları yeniden önceliklendirilir. Learning/skill-ledger/sync/quality, alternatif UI/install/update/eval aileleri kapsam haritasında tutulur. Önce native alt-sistemler ve ilişkiler, sonra çekirdek açıklama, daha sonra ayrı dört-alan/SOUL/Development OS değerlendirmesi. Aşama ve başarı ölçütü dosya/test sayısı değildir.

Yalnız Hermes package + CATALOG Hermes satırı; U04–U10 evidence/notes, METHOD ve synthesis01–04 değişmez. Foundation/control/context/Codex/upstream/diğer studies/architecture/adoption veya izin ayarı değişmez. Güncel main/nonforce/ref-content-diff readback yayın koşuludur. [Önceki exact v0.23 plan](https://github.com/batuhanozgun/agentic-os-search/blob/b658913dd8148dd9a4850414159f13513904f137/research/studies/hermes-agent/RESEARCH-PLAN.md) korunur.
