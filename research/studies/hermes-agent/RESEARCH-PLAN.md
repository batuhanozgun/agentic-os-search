# Hermes Agent — Araştırma planı

**Plan v0.7 — 2026-09-09.** U01-D2 tesliminin kaydı ve kalan entegrasyon sorusunun ayrıştırılması. Güncel iş/yetki otoritesi [STATE](STATE.md); kapanış ölçütü [METHOD](METHOD.md). Bu revizyon yeni deney, upstream güncellemesi veya araştırma tamamlanması değildir.

## 1. Döngü ve kapsam

`kaynak keşfi → mekanizma sorusu → kaynak/caller/etki → karşı yol → not → kapsam revizyonu → sonraki birim`.

Üst sentez notları yalnız kısaltmaz; açıklanmamış geçişleri ve karşı örnekleri kaynağa dönerek arar. Önce HERMES-native model, ardından dört-alan ve SOUL/Development OS değerlendirmesi. Hata listesi, kurulum, upstream düzeltmesi veya benimseme bu araştırmanın yerine geçmez.

## 2. Aşamalar

| Aşama | Durum |
|---|---|
| A0 Kimlik/pin/sınır | c4a5de... immutable pin; 0.21.0 manifest. D/E kaynakları primary'ye bağlı; current HEAD veya kurulu release doğrulaması değil. |
| A1 Topoloji | Root/apps/agent/tools/hermes_cli non-recursive listeleri; recursive tam envanter yok. |
| B0 Öğrenme kesitleri | U01 review, U01-C curator, U01B skill/onay; ayrı U01B2 onay/rollback kanıtı da korunuyor. |
| U01-DOC | Sekiz unpinned resmî belge; 05/K01–K09 ilk tasarımları. |
| U01-D / U01-M | Ordinary caller/worker, ortak kontroller, memory/store/replay kaynakları; önceki üç-modüllü transport probe. |
| U01-D2 | 09 notu: seçili gerçek executor/whitelist tanımlarıyla 14 durum; ayrı tam name-validator köprüsüyle 5 durum. Büyük modüller manuel seçki; tam review/ithal bağımlılık entegrasyonu açık. 2026-09-09'da eski kanıt yayımlandı, yeniden koşulmadı. |
| B1–Bn | Aşağıdaki F01–F12 kapsamı korunuyor. |
| C–F | Native alt-sistemler → ilişkiler → dört-alan/SOUL/DevOS → CORE/omission/freshness: henüz tamamlanmış sentez yok. |

## 3. Provisional kaynak aileleri

| ID | Aile / soru | Mevcut derinlik ve açık sınır |
|---|---|---|
| F01 | Başlama, araç döngüsü, retry, kesinti, sonlanma | Façade/ordinary loop/prologue/worker kaynak kesitleri; seçili sequential işlevler yürütüldü. Actual whole trace ve alternatif runtime açık. |
| F02 | Prompt, context, schema, compression/cache | Cached restore/build, api_content ve MemoryStore snapshot kaynakları; bütün reload/invalidation/compression açık. |
| F03 | Session kimliği, lineage, arama, kullanım/onarım | Turn/persist/replay kesiti; actual session-search ve tüm DB/restore yaşam döngüsü açık. |
| F04 | Bellek/beceri, sahiplik/onay/geri alma/paylaşım | Review/curator/skill batch + memory gate/store/pending kaynakları; U01B2 payload/preview/rollback kanıtı. Actual UI, ledger/sync/reuse/kalite açık. |
| F05 | Provider/model/credential/profile/config bağlama | Review/curator seçimi ve ContextVar aktarımı incelendi; deney profili sentetik. Gerçek resolver/credential kullanılmadı. |
| F06 | Tool/skill/plugin/MCP keşfi ve çağrı yetkisi | Ortak kontrol ve thread-local whitelist kaynakları; U01-D2 selected tüketici/worker ve tam ad doğrulayıcı deneyi. Gerçek review ad-kümesi/ara kontrol/worker bağlama kapanışı açık. |
| F07 | Backend/native katmanların etki sınırı | Güvenlik kontratı/root harita; kooperatif kontrol OS izolasyonu sayılmaz. |
| F08 | Delegation/process/cancellation/worktree/yazıcılar | Worker/callback transfer ve cancel callsite; actual stop, shared store ve genel delegasyon açık. |
| F09 | Gateway yetkilendirme/session/teslim | Kaynak bağlantı adayları ve persistence→tool.completed ayrımı; adapter eşdeğerliği kurulmadı. |
| F10 | Cron/proaktif iş/kuyruk/tekrar-kayıp | Curator cron referansı ve idle queue callsite; gerçek scheduler/restart açık. |
| F11 | CLI/TUI/desktop/web/API/ACP temsil/yetki | Ortak approval command; actual UI çağrıları açık. D21 dashboard helper pending caller değildir. |
| F12 | Install/update/compat/test/eval/telemetri | Önceki selected manifest/test; ayrı U01B/transport/U01B2/U01-D2 kanıtları. Ürün PASS toplamı yok. Upstream suite, release, CI ve gelecek-task kalite açık. |

Family etiketi ürün modülü veya okunmuş dosya sayısı değildir. Bir mekanizma çok aileye bağlanabilir; kaynak bulunması aile kapanışı değildir.

## 4. İlk sonraki birim — yapılmış olanı tekrar etmeden

**D2-FIDELITY / ilk somut kontrol:** [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md) ve [E defteri](evidence/2026-09-08-worker-policy/SOURCES.md) üzerinden `agent/tool_executor.py@799199c10f9930da77c01da2324373614b27cb78` ile `hermes_cli/plugins.py@da8d7e2c68b2346e6ecc15567d755d96085ef767` tam pinned içeriklerini yerelde elde et. `verify_excerpts.py` için bu tam orijinalleri sağla; orijinal blob kimliğini ve seçili tanım AST eşitliğini ayır. Script hazır, bu kontrol **NOT RUN**. Fark varsa özgün kanıtı değiştirme; farkı ve etkilediği iddiayı yeni kayıtla göster. Eşitlik gerçek çalışma bağlamını tek başına doğrulamaz.

**D2-REACHABILITY / ana ayırıcı soru:** Gerçek review/fork kurulumu, geçerli-ad kümesinin oluşumu, ordinary dispatcher, tam middleware/PluginManager ve worker-local policy bağını birlikte izle. Zararsız handler'a gerçekten ulaşıldığını veya başka kontrolün çağrıyı engellediğini ölç. `dispatched` alanını tek effect oracle'ı yapma; callback kabulü, policy kararı, handler girişi ve sonuç ayrı kaydedilsin.

Rival açıklamalar: gerçek valid-name kümesi zaten dar olabilir; worker girişinde ayrı policy kurulumu olabilir; başka middleware çağrıyı önce engelleyebilir; alternatif runtime farklı yol kullanabilir; manuel excerpt'te fark olabilir. Bunları dışlamadan genel bypass hükmü verme. Tam modül ithali, fixture ve kaynak kimlikleri açık olsun; izin sınırını kurulum/provider/credential kullanımıyla büyütme.

**Sınırlı durma/devam koşulu:** İlgili dependency closure elde edilemez veya yetki dışına çıkıyorsa eksik dosya/bağ ve etkilediği hüküm kaydedilir. Bu durumda tam entegrasyon doğrulanmış sayılmaz. Aynı C/V fixture'ını yeniden çoğaltarak ilerleme üretilmez. Mevcut mekanizma ve sınırları kaynakla savunulabilir olduğunda ileri entegrasyon sorusunu açık tutup aşağıdaki yetkili araştırma sırasına geçilebilir; gerekçe STATE/planda korunur.

## 5. Sonraki sıra ve aileler arası geçiş

**U01-M:** Actual CLI/gateway pending çağırıcısı, onaylayan/profil/store bağlama. Ardından normal yazım, write exception, yeniden yükleme ve prompt rebuild için dosya/live/snapshot/gerçek istek ayrımı. M01 (write-failure state ayrışması) ve M02 (batch alias kontrol kapsamı) statik adaydır; zararsız sentinel/denetçiyle ayırıcı kontrol henüz yapılmadı.

**U01 kapanış bağlantıları:** Trigger/cancel/idle-store; ledger/backup/restore/sync; sonraki skill/cache yükleme; U01-C curator report/nested operations/cron. U01B2'nin default_name üretim–staging–replay ve rollback sırasında diğer yazarları dışlama soruları actual caller'a bağlanır. S01/S02 ve `run_agent.py` erişimi eski ilk-okuma işi değildir.

**U02:** Çekirdek work/context/session yaşam döngüsünün genel sentezi, U01 için açılmış dar kesitlerin ötesinde. **U03:** Provider/tool/plugin/backend/delegation yetki ve etki. **U04+:** Gateway/cron/UI/install/eval ve kalan varyantlar.

U01 veya tek whitelist adayı bütün çalışmayı yutmamalı. Kaynak bağımlılığı sıra değiştirirse gözlem ve gerekçe kaydedilir. Yeni dış araştırma nesnesi veya Foundation/architecture aşaması bu kapsamı sessizce genişletmez. Araştırmanın doğal sonraki aşaması benimseme yetkisi değildir.

## 6. K01–K09 güncel statüsü

[05 §9](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) ilk tasarımın tarihsel kaydıdır; dokuz kontrolün tamamı çalıştırıldı denmez.

| Kontrol | V0.7 durumu |
|---|---|
| K01 özel/genel denetim | Ortak dış kontrol kaynakta; selected gerçek policy tüketicisi deneyi U01-D2'de. Tam ordinary/özel/genel bütün çağrı entegrasyonu yok. |
| K02 error vs compensation | Dış wrapper/persistence statik; U01B/U01B2 exception kanıtı actual tam dispatch ile yeniden koşulmadı. D2 lifecycle/approval hatası ayrı sorudur, rollback testi değildir. |
| K03 context transfer | Önce P01–P07 sentetik policy; sonra C01–C14 selected gerçek tüketici/worker ve V01–V05 ad doğrulama köprüsü. Tam orijinal modül/gerçek review kurulumu hâlâ açık. |
| K04 approval | Ortak command + memory replay kaynakları; D2 selected approve-directive exception kontrolü pending UI/kimlik/skill ownership doğrulaması değildir. |
| K05 memory visibility | Store/snapshot/restore/wire kaynakları; M01 ve actual rebuild readback'i NOT RUN. |
| K06 lifecycle | Cancel/admission/prologue/nudge callsite; tüm finalize/teardown/old-worker etkisi açık. |
| K07 replay | api_content/wire copy kaynakları; archive/search/review eşdeğerlik deneyi yok. |
| K08 compression failure | Belge sorusu sürüyor; summarizer-failure deneyi yok. |
| K09 curator batch | Nested operations/report/cron bağlantısı açık. |

Diğer açık ayrımlar: aynı/farklı model kanıt görünümü; read/preview/approve/write hedef sürümü; pending saklama/silme; ledger/cache/sync etkileri; observer/enforcement/hata politikası; kullanım ile gelecek-task kalite. D2'nin kimlik olumsuz kontrolü, excerpt eşitliğini veya davranışın tüm bağlamlarını doğrulamaz.

## 7. Erişim, publication ve freshness

Eski path 429'ları, sonradan okunan kaynakları hâlâ erişilemez yapmaz. Tool discovery ile gerçek çağrı sonucu ayrılır; yazılamama veya izin nedeni tahmin edilmez. 2026-09-09'da Git veri yazma yolu çalıştı ve özgün evidence subtree kimliği geri okundu. Önceki teslimdeki NOT PUBLISHED/NOT APPLIED ifadeleri [PUBLICATION](evidence/2026-09-08-worker-policy/PUBLICATION.md) ile tarihsel bağlama alınır. Bu yayın yeni teknik deney değildir.

Primary pin değişmedi. W belgeleri unpinned kalır; D/E kaynakları primary'ye bağlıdır. Manuel büyük-modül seçkileri tam dosya kimliğiyle karıştırılmaz. Current HEAD'e bağlı ilerideki kullanım kararında değişen bağımlılıklar ayrıca doğrulanır; bu yayın upstream güncellik/adoption kararı değildir.

## 8. Revizyon geçmişi

| Revizyon | Kanıt ve etkisi |
|---|---|
| v0.1 | Gstack yönteminden kaynak/sentez disiplini; Hermes-native araştırma, geç projeksiyon. |
| v0.2 | Review/guard/provenance/approval, transcript/store/quality ayrımı. |
| v0.3 | Curator/usage/policy/report/cron; U01-C ayrı birim. |
| v0.4 | U01B repo aktarımı; H22 full, exception/preview/durability; curation korundu. |
| v0.5 | 429 nedeniyle U01-DOC, sekiz belge ve NOT RUN K01–K09; caller ilk sıradaydı. |
| v0.6 | Tree/blob erişimi; caller/memory kaynakları; üç-modül P01–P07. Ortak kontrol ile policy taşıma ayrıldı. Sonraki U01B2 yayını bu sırayı değiştirmedi. |
| v0.7 | 2026-09-08 U01-D2 selected-function/name-validator/kimlik kanıtı 2026-09-09'da yayımlandı. Tam AST sadakati ve gerçek review/worker erişilebilirliği ayrı artık işler oldu; tam entegrasyon kapanmadı. U01-M ve F01–F12 sırası korundu. |

[V0.6 tam plan](https://github.com/batuhanozgun/agentic-os-search/blob/36f1b7e6ae07da5c1d9d57ff9633d48473c42537/research/studies/hermes-agent/RESEARCH-PLAN.md), [v0.5](https://github.com/batuhanozgun/agentic-os-search/blob/a218acfc20e7ece488709e00a9762166ec970fba/research/studies/hermes-agent/RESEARCH-PLAN.md), [v0.3 öncesi](https://github.com/batuhanozgun/agentic-os-search/blob/000f691b9a94607c9a8219961b4618eda0f1014f/research/studies/hermes-agent/RESEARCH-PLAN.md). Plan revizyonu eski koşuların tekrarlandığı veya yeni agent-control kuralı anlamına gelmez.
