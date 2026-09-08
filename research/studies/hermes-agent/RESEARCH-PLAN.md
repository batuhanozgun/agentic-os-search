# Hermes Agent — Araştırma planı

**Plan v0.6 — 2026-09-08.** Kanıta göre değişen external-target decomposition. Güncel iş/yetki otoritesi [STATE](STATE.md); kapanış ölçütü [METHOD](METHOD.md).

## 1. Döngü ve kapsam

`kaynak keşfi → mekanizma sorusu → kaynak/caller/etki → karşı yol → not → kapsam revizyonu → sonraki birim`.

Üst sentez notları yalnız kısaltmaz; açıklanmamış geçişleri ve karşı örnekleri kaynağa dönerek arar. Önce HERMES-native model, ardından dört-alan ve SOUL/Development OS değerlendirmesi. Hata listesi, kurulum, upstream düzeltmesi veya benimseme bu araştırmanın yerine geçmez.

## 2. Aşamalar

| Aşama | Durum |
|---|---|
| A0 Kimlik/pin/sınır | c4a5de... immutable pin; 0.21.0 manifest. Son D kaynakları primary tree/blob'a bağlı; current HEAD değil. |
| A1 Topoloji | Root/apps geçmişine agent/tools/hermes_cli non-recursive listeleri eklendi. Recursive tam envanter yok. |
| B0 Öğrenme kesitleri | U01 review, U01-C curator, U01B skill/onay; eski iki-modül deneyi korunuyor. |
| U01-DOC | Sekiz unpinned resmî belge; 05/K01–K09 ilk tasarımları. |
| U01-D / U01-M | Ordinary caller/worker, ortak kontroller, memory/store/replay kaynakları; üç exact modüllü transport probe. Aile kapanmadı. |
| B1–Bn | Aşağıdaki F01–F12 kapsamı korunuyor. |
| C–F | Native alt-sistemler → ilişkiler → dört-alan/SOUL/DevOS → CORE/omission/freshness: henüz tamamlanmış sentez yok. |

## 3. Provisional kaynak aileleri

| ID | Aile / soru | Mevcut derinlik ve açık sınır |
|---|---|---|
| F01 | Başlama, araç döngüsü, retry, kesinti, sonlanma | Façade/ordinary loop/prologue/worker kaynak kesitleri; actual whole trace ve alternatif runtime açık. |
| F02 | Prompt, context, schema, compression/cache | Cached restore/build, api_content ve MemoryStore snapshot kaynakları; bütün reload/invalidation/compression açık. |
| F03 | Session kimliği, lineage, arama, kullanım/onarım | Turn/persist/replay kesiti; actual session-search ve tüm DB/restore yaşam döngüsü açık. |
| F04 | Bellek/beceri, sahiplik/onay/geri alma/paylaşım | Review/curator/skill batch + memory gate/store/pending kaynakları; gerçek UI, ledger/sync/reuse/kalite açık. |
| F05 | Provider/model/credential/profile/config bağlama | Review/curator seçimi ve ContextVar aktarımı incelendi; probe profili sentetik. Gerçek resolver/credential kullanılmadı. |
| F06 | Tool/skill/plugin/MCP keşfi ve çağrı yetkisi | Ortak middleware/pre-tool, özel/genel yollar ve thread-local whitelist adayı; gerçek policy tüketicisiyle worker probe sırada. |
| F07 | Backend/native katmanların etki sınırı | Güvenlik kontratı/root harita; kooperatif kontrol OS izolasyonu sayılmaz. |
| F08 | Delegation/process/cancellation/worktree/yazıcılar | Worker/callback transfer ve cancel callsite; actual stop, shared store ve genel delegasyon açık. |
| F09 | Gateway yetkilendirme/session/teslim | Kaynak bağlantı adayları ve persistence→tool.completed ayrımı; adapter eşdeğerliği kurulmadı. |
| F10 | Cron/proaktif iş/kuyruk/tekrar-kayıp | Curator cron referansı ve idle queue callsite; gerçek scheduler/restart açık. |
| F11 | CLI/TUI/desktop/web/API/ACP temsil/yetki | Ortak approval command; actual UI çağrıları açık. D21 dashboard helper pending caller değildir. |
| F12 | Install/update/compat/test/eval/telemetri | Önceki selected manifest/test; iki ayrı bounded probe. Upstream suite, release, CI ve gelecek-task kalite açık. |

Family etiketi ürün modülü veya okunmuş dosya sayısı değildir. Bir mekanizma çok aileye bağlanabilir; kaynak bulunması aile kapanışı değildir.

## 4. İlk sonraki birim ve ilerleme sırası

**U01-D devamı:** Actual ordinary executor + actual whitelist precheck + zararsız handler. Review thread'inde kurulan policy'nin worker'da gerçekten görüldüğünü veya başka callsite'ta telafi edildiğini sınamak. Üç-modüllü probe'un sentetik policy/profil/callback sınırı kaldırılmadan bütün runtime verdict'i verilmez. Source/fixture kimliği, actual handler'a ulaşma ve alternatif kontrol aynı gözlemde ayrılmalı.

**U01-M devamı:** Gerçek CLI/gateway pending çağırıcısı, onaylayan/profil/store bağlama. Sonra normal yazım, write exception, yeniden yükleme ve prompt rebuild için dosya/live/snapshot/istek readback'i. M01 (write-failure state ayrışması) ve M02 (batch alias kontrol kapsamı) statik adaydır; zararsız sentinel/denetçi ile önce ayırt edilir.

**Sonraki U01 kapanış bağlantıları:** Trigger/cancel/idle-store; ledger/backup/restore/sync; sonraki skill/cache yükleme; U01-C curator report/nested operations/cron. U01B/S01 ve S02 daha önce tam okunmuştur; yeniden 'ilk okuma' işi değildir.

**U02:** Çekirdek work/context/session yaşam döngüsünün genel sentezi, U01 için açılmış dar kesitlerin ötesinde. **U03:** Provider/tool/plugin/backend/delegation yetki ve etki. **U04+**: Gateway/cron/UI/install/eval ve kalan varyantlar.

U01 veya tek whitelist adayı bütün çalışmayı yutmamalı. İlgili mekanizma ve sınırları kaynakla savunulabilir olduğunda açık ileri doğrulamayı kaydedip diğer ailelere geç. Kaynak bağımlılığı sıra değiştirirse gözlemi ve gerekçeyi kaydet. Yeni dış araştırma nesnesi bu kapsamı sessizce genişletmez.

## 5. K01–K09 güncel statüsü

[05 §9](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) ilk tasarımın tarihsel kaydıdır; dokuz kontrolün tamamı çalıştırıldı denmez.

| Kontrol | V0.6 durumu |
|---|---|
| K01 özel/genel denetim | Ortak dış kontrol kaynakta görüldü; whitelist'in worker state'ine bağı ayrıca açık. Entegre test yok. |
| K02 error vs compensation | Dış wrapper/persistence statik incelendi; U01B exception'ı actual dispatch ile yeniden koşulmadı. |
| K03 context transfer | P01–P07, üç exact modül + sentetik marker/API/policy ile transport alt sorusunu sınadı. Actual executor/PluginManager/profil resolver henüz yok. |
| K04 approval | Ortak command + memory replay kaynakları; actual UI/identity/delivery ve skill ownership açık. |
| K05 memory visibility | Store/snapshot/restore/wire kaynakları; M01 ve actual rebuild readback'i NOT RUN. |
| K06 lifecycle | Cancel/admission/prologue/nudge callsite; tüm finalize/teardown/old-worker etkisi açık. |
| K07 replay | api_content/wire copy kaynakları; archive/search/review eşdeğerlik deneyi yok. |
| K08 compression failure | Belge sorusu sürüyor; yeni summarizer-failure deneyi yok. |
| K09 curator batch | Nested operations/report/cron bağlantısı açık; bu tur kapatılmadı. |

Diğer açık karşı-sınamalar: aynı/farklı model kanıt görünümü; read/preview/approve/write target revizyonu; pending saklama/silme; dosya dışı ledger/cache/sync etkileri; observer/enforcement/hata politikası; kullanım ile gelecek-task kalite. Statik dal, dar yürütme ve üretim sonucu ayrı tutulur.

## 6. Erişim ve freshness

V0.5 turunda iki path 429'u kod ilerlemesini engelledi. Son tur path erişimi yine başarısızken pinned Git tree/blob okumaları çalıştı. Current devam işi artık erişilemeyen run_agent dosyasını ilk kez almak değil, incelenmiş çağrı parçalarının entegrasyonunu sınamaktır. Okunmamış yeni bağımlılık erişilemiyorsa etkilenen iddia sınırlı kalır; kurulum/provider kullanımıyla yetki genişletilmez.

W belgeleri unpinned kalır; D kaynakları primary'ye bağlıdır. Sonraki current HEAD reuse kararında değişen bağımlılıklar yeniden kontrol edilir. Bu çalışma bir upstream güncellik/adoption kararı değildir.

## 7. Revizyon geçmişi

| Revizyon | Kanıt ve etkisi |
|---|---|
| v0.1 | Gstack yönteminden kaynak/sentez disiplini; Hermes-native araştırma, geç projeksiyon. |
| v0.2 | Review/guard/provenance/approval, transcript/store/quality ayrımı. |
| v0.3 | Curator/usage/policy/report/cron; U01-C ayrı birim. |
| v0.4 | U01B kaybının repo'ya aktarımı; H22 full, exception/preview/durability; önceki curation korundu. |
| v0.5 | 429 nedeniyle U01-DOC, sekiz belge ve NOT RUN K01–K09; caller hâlâ ilk kaynak işi. |
| v0.6 | Tree/blob erişimi; gerçek caller/memory kaynakları; üç-modül P01–P07. Ortak kontrol ile policy taşıma ayrıldı; ilk iş integrated harmless worker/precheck, sonra memory/UI/ledger/curator. |

[V0.5 tam plan](https://github.com/batuhanozgun/agentic-os-search/blob/a218acfc20e7ece488709e00a9762166ec970fba/research/studies/hermes-agent/RESEARCH-PLAN.md), [v0.3 öncesi yüzey](https://github.com/batuhanozgun/agentic-os-search/blob/000f691b9a94607c9a8219961b4618eda0f1014f/research/studies/hermes-agent/RESEARCH-PLAN.md). Geçmiş not/kanıtlar korunur; plan değişmesi eski deneyin yeniden yapıldığı veya yeni agent-control kuralı anlamına gelmez.
