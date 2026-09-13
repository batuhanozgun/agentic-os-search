# Hermes Agent — Araştırma planı

**v0.25 / 2026-09-13 — U12 yayımlı; Q57 başlangıç checkpoint'i.** [STATE](STATE.md) current work/yetki, [METHOD](METHOD.md) yöntem, [MAP](CURRENT-RESEARCH-MAP.md) büyük resim, [PUBLICATION](evidence/2026-09-13-tool-delegation/PUBLICATION.md) tamamlanmış U12 yayını. Primary c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a / manifest0.21.0; current ürün hükmü değil.

## Q57 başlangıç — 2026-09-13

Kullanıcının “Anlaştık. Devam et. Operasyonel sınırına kadar çalış.” yetkisiyle kayıtlı Q57 devralındı. Gerçek main **74c5e3d1dcd260a1841c64dda5fb1d182f7bb299**; U12 yayın makbuzundan sonra ilerlememiştir. Güncel AGENT tekrar getirildi; değişmeyen R01–R09 ve U12 current/source metinlerinin aynı-conversation tam okumaları uygulanır. Research root, METHOD ve synthesis02/04 yeniden geri kazanıldı. U12-A/B ile eski U04-A/B yayınları yeniden yapılacak iş değildir.

Bu başlangıç kaydı yeni teknik bulgu/deney değildir. Actual main/ref ve plan geri okunmadan kapsamlı yeni kaynak dilimi başlamaz. İlk dilim: shared completion producer→gerçek host drain→ownership/claim→parent continuation/admission→ack. Normal olay ile restored/expired/interim event ayrımı korunur. CLI ve gateway/API yolları aynı varsayılmaz. Kaynaklar tek anlamlı consumer zincirinde bağlanabiliyorsa yapay dosya kotasına bölünmez. İlk anlamlı dilim main'e kaydedilip geri okunduktan sonra coverage/map üzerinden geniş kalan ailelerin önceliği değerlendirilir; yayınsız ikinci büyük dilim biriktirilmez.

## Yapılan ve revizyon gerekçesi

Kayıtlı Q54, iki kaynak diliminde ilerledi. Başlangıç planı 0fd4b597002eb478cd1ed913a588ba44fe70edb3 main/ref/tam metin/scope ile doğrulandı. A; schema/visibility/admission → pre-effect kayıt → son argüman policy → executor/gerçek read_file handler → result kaydıdır. A ef51c3f4b1d4d94038a428fa9bac1a21dfda778f main'e yazılıp tam geri okunduktan sonra B açıldı. Araya giren diğer harness çalışması korundu.

B; config/depth/budget/runtime ile child kurulması, parent-context vs native stateless MCP, task/workspace/DB sahipliği, sync/detached group/unit/slot, live control, summary/schema/status, timeout/deferred close ve async completion ledger'ıdır. [Note27](notes/27-TOOL-ADMISSION-AND-DELEGATION.md) A/B'yi tek erişim yüzeyinde birleştirir. Yeni HERMES behavioral execution yapılmadı; source read kapsamları kendi iki defterindedir.

Q54 kaynak çıkışı kısmen yerine getirildi: bir ordinary araç ve gerçek delegation child/return zinciri açıklanabilir. Sync tool-result parent'a döner; detached sonuç DB/queue/claim helper'larına bağlandı. **Actual host drain→parent turn kabulü aynı derinlikte açılmadı.** Bu yük taşıyan boşluk Q57 olarak ayrıldı. Bu ayırım Q54 tamamlanmış ürün doğrulaması veya yeni hata matrisi bitirme yükümlülüğü değildir.

Önemli yeni native ayrımlar: fresh child conversation vs shared environment; inherited restriction vs role-granted delegation; per-child budget vs whole-tree cost; grouping vs execution dependency; child completed/summary vs semantic task acceptance; steering queued vs consumed; stalled terminal vs physical stop; durable completion vs parent use. Synthesis01–04 ve U11/U10 kaynakları korunur; yeni amendment final CORE değildir.

## İlk sonraki dar kaynak birimi — Q57

**Soru:** Kayıtlı async-delegation sonucu, doğru güncel parent'ın hangi turuna hangi kabul ve acknowledgement koşullarıyla girer?

Başlangıç `tools/async_delegation.py::_push_completion_event`, `claim_event_delivery`, `complete_event_delivery`, `restore_undelivered_completions` gerçek çağırıcılarıdır. Completion queue tüketicisi, routing/session ownership, explicit user boundary, claim acquisition/release/ack ve actual agent admission/context sırası takip edilir. En az bir normal host yolu ve materially farklı restored/expired/interim child-failure yolu karşı okunur. Helper ismi veya queue.put dönüşü kabul makbuzu yapılmaz; CLI/gateway/API bütünü aynı sayılmaz.

İlk anlamlı consumer dilimi: producer→drain→ownership/claim→host continuation çağrısı; ardından gerekli olduğunda yeni agent admission/history ve ack sınırı. Source tek doğal birim halinde bağlanabiliyorsa yapay bölünmez. Source erişimi yetmezse tam okunmayan halka açık kaydedilir. Live ürün/model/credential/OS veya gerçek dış servis deneyi başlatılmaz.

**Bu dilimden sonra kapsam dengesi yeniden değerlendirilir.** Kalan learning/skill-ledger/sync/quality, alternatif UI/install/update/eval aileleri coverage/map üzerinden tartılır. Bütün teslim, concurrency ve failure kombinasyonlarını tüketmek geniş modelin ön koşulu yapılmaz. Q57'nin seçilme nedeni ilginç bir hata değil, child sonucunun parent tarafından tüketildiği eksik ilişkinin native açıklama değeridir.

## Ayrı residual doğrulama hattı

Q54: actual registry/scope/policy, rewritten path vs batch reservation, DB proposal/result failure, child ilk request/runtime/budget, role-granted yetki, workspace/DB handle izolasyonu, correction schema turu, summary/spill tüketimi, sync/detached fallback ve cancellation/worker lifetime. [U12 NOT RUN](evidence/2026-09-13-tool-delegation/CHECKS-NOT-RUN.md). Source gözlemleri data-loss/race/başarı oranı değildir.

Q53 fallback geçiş ortası/primary restore; Q55 native model/system/history/restart; Q56 native terminal/persistence/control. U10 Q49 full accepted→run_job→script/agent/request, Q51 selector→request/quality, Q52 detection→handling. Q40/Q42 actual DB/quiet/startup; Q47 callback/NAS/clock; Q48/Q50 transport/status/cancel; Q41/Q43/Q44/Q45/Q07/Q22/Q26/Q29/Q38 eski sınırları korur. Full source/bağımlılık, yeni karşı kanıt veya load-bearing reliability reuse gerektiğinde ilgili ölçüm yeniden açılır; erteleme kapanış değildir.

## Incremental kayıt ve kapsam

Yeni büyük dilimden önce actual main/STATE ve current yayın makbuzu kontrol edilir. Her anlamlı dilim bulgu+kaynak+sınır+sonraki soru ile kalıcılaştırılır; ref/content/scope geri okumasından önce yayımlandı denmez. Yayın engelinde mevcut dilimin devri çözülür, yeni araştırma biriktirilmez. Bu çalışma düzeni agent-control değişikliği değildir.

Yalnız Hermes package + CATALOG Hermes satırı. METHOD, notes01–27, U04–U12 evidence/yayınlar ve synthesis01–04 değişmez. Foundation/control/context/Codex/upstream/diğer studies/architecture/adoption/izin ayarları değişmez. [Exact U12 plan](https://github.com/batuhanozgun/agentic-os-search/blob/74c5e3d1dcd260a1841c64dda5fb1d182f7bb299/research/studies/hermes-agent/RESEARCH-PLAN.md) → [Q54 başlangıç planı](https://github.com/batuhanozgun/agentic-os-search/blob/0fd4b597002eb478cd1ed913a588ba44fe70edb3/research/studies/hermes-agent/RESEARCH-PLAN.md) geçmiş sırayı korur. Araştırma yöntemi kaynak→mekanizma→alt-sistem→ilişki→CORE→ayrı daha-geç dört-alan değerlendirmesidir; dosya/test adedi ilerleme yüzdesi değildir.
