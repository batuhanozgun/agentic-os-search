# Hermes Agent — Araştırma planı

**Plan v0.8 — 2026-09-09.** Kanıta göre değişen external-target decomposition. Güncel iş/yetki otoritesi [STATE](STATE.md); kapanış ölçütü [METHOD](METHOD.md).

## 1. Yöntem ve kapsam

Kaynak keşfi → mekanizma sorusu → kaynak/caller/etki → karşı yol → not → kapsam/sıra revizyonu. Üst sentez notları yalnız kısaltmaz; açıklanmamış geçişlerde kaynağa döner. Önce HERMES-native model, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesi. Kurulum, upstream onarımı, hata listesi veya benimseme araştırmanın yerine geçmez.

Primary pin `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0. Moving-branch araması navigasyon; pinned kaynak yerine geçmez. W belgeleri unpinned; gerçek modül, seçili tanım, statik kaynak ve ürün yürütmesi ayrı.

## 2. Aşamalar

| Aşama | Güncel statü |
|---|---|
| A0 Kimlik/pin/sınır | Sabit pin ve çalışma yetkisi kurulu; current installed release doğrulanmadı. |
| A1 Topoloji | Root/apps/agent/tools/hermes_cli kısmi listeleri; recursive tam envanter yok. |
| B0 Öğrenme kesitleri | U01 review, U01-C curator, U01B/U01B2 skill/onay, U01-M memory; aile kapanmadı. |
| U01-DOC | Sekiz resmî unpinned belge; K01–K09 tarihsel tasarım. |
| U01-D / D2 | Caller/worker ve source-selected/tam-validator deneyleri kalıcı kayıtta. |
| U01-D3 | Gerçek review kurulum/ad-kümesi/round/Relay kaynak bağı; 22 tanım için manuel-range AST; exact middleware MW01–MW08. Tam büyük-orijinal verifier ve bütün runtime hâlâ açık. |
| C–F | Native alt-sistemler → ilişkiler → dört-alan/SOUL/DevOS → CORE/omission/freshness sentezleri henüz tamamlanmadı. |

## 3. Provisional kaynak aileleri — geniş kapsam korunur

| ID | Aile / soru | Mevcut ilerleme ve açık sınır |
|---|---|---|
| F01 | Başlama, araç döngüsü, retry, kesinti, sonlanma | Façade/prologue/worker'a gerçek tool-round eklendi; bütün yürütme ve alternatif runtime açık. |
| F02 | Prompt/context/schema/compression/cache | Schema parity ve valid names kaynakta bağlandı; cached/frozen/wire kaynakları var, reload/compression açık. |
| F03 | Session kimliği/lineage/arama/onarım | Persist-before-execute ve post-effect failure ayrımı; gerçek DB/search/restore yaşam döngüsü açık. |
| F04 | Bellek/beceri/sahiplik/onay/geri alma/paylaşım | Review/curator/skill batch/memory store/pending; actual UI/profile/store sonraki aktif iş, ledger/sync/kalite açık. |
| F05 | Provider/model/credential/profile/config | Review fork'un parent runtime/toolset bağı; gerçek resolver/credential kullanım testi yok. |
| F06 | Tool/skill/plugin/MCP keşfi ve yetki | Review valid names/whitelist ayrımı kaynakla güçlendi; exact middleware failure/once davranışı sınandı. Tam Q26 runtime açık. |
| F07 | Backend/native etki sınırı | Güvenlik kontratı/root; cooperative kontrol OS sandbox sayılmaz. |
| F08 | Delegation/process/cancellation/worktree/yazıcılar | Worker/callback/cancel kaynakları; full cancellation ve shared-store yarışları açık. |
| F09 | Gateway auth/session/teslim | Persistence/delivery kaynağı; actual gateway pending ve adapter farkları açık. |
| F10 | Cron/proaktif iş/kuyruk/tekrar-kayıp | Curator cron-reference/idle callsite; scheduler/restart açık. |
| F11 | CLI/TUI/desktop/web/API/ACP | Ortak approval command gerçek UI değildir; CLI/gateway caller ilk sırada. |
| F12 | Install/update/compat/test/eval/telemetri | Ayrı bounded probe kayıtları + MW01–MW08; upstream suite/release/CI/gelecek-task kalite yok. |

Family etiketi ürün modülü veya tamamlanma oranı değildir. Kaynağın bulunması aile kapanışı sayılmaz.

## 4. İlk sonraki yetkili birim ve sıra değişimi

**U01-M / actual pending caller:** Pinned CLI ve gateway'de `/memory` ve `/skills` onay akışını ortak D17/D15/skill apply'e kadar takip et. Onaylayan kimlik, aktif home/profil, live/fresh store ve başarı/pending silme sırası bir arada açıklanmalı. Command docstring'i veya web_server_memory dosya adı UI kanıtı sayılmamalı.

**Sonra M01/M02:** File/live/snapshot/request readback'i; normal yazım, write exception, sonraki reload; batch content/new_text normalizasyon ve denetim. Zararsız sentinel'lar, kontrollü geçici dosyalar; gerçek provider/credential yok.

**Sonraki bağlantılar:** review trigger/cancel/idle/shared-store; ledger/backup/restore/sync; sonraki skill/cache yükleme; U01-C curator nested operations/report/cron. U01B2 default_name staging/replay, preview/hedef sürümü, rollback/başka-yazar izolasyonu bu gerçek yollara bağlanır.

**Sıra gerekçesi:** V0.7 önce full-original fidelity ve gerçek review/worker bağını hedefliyordu; bu tur tam yerel E01/E02 materyalizasyonu kurulamadı. Daha dar range cross-check ve yeni gerçek kurulum/round/middleware kaynakları ilgili soruyu ilerletti. Artık aynı selected fixture'ları çoğaltmak yerine, v0.7 §4'ün izin verdiği biçimde Q26'nın ileri doğrulamasını açık tutup geniş öğrenme zincirine geçiliyor. Bu teknik kapanış değil, gerekçeli araştırma sırası değişimidir; yeni sistem veya mimari fazı değildir.

**U02:** Daha genel work/context/session yaşam döngüsü. **U03:** Provider/tool/plugin/backend/delegation yetki ve etki. **U04+:** Gateway/cron/UI/install/eval ve kalan varyantlar. Kaynak bağımlılığı farklı sıra gerektirirse kanıt ve gerekçe kaydedilir.

## 5. Açık ileri doğrulama — Q26/Q29

22 AST eşleşmesi, iki manuel transkripsiyonun bounded cross-check'idir. E01/E02 tam dosya Git hash + eski verify_excerpts.py kontrolü NOT RUN. Bu daha güçlü kontrol imkân oluştuğunda veya bulgu load-bearing reuse'a geçtiğinde yapılmalı.

Gerçek review/fork → actual valid names → tam ordinary executor/PluginManager/middleware/Relay → zararsız handler birlikte koşulmadı. Statik standart kurulumda parent toolset → schema-derived valid names ve ayrı review whitelist görüldü; tüm runtime/ek kontrol yokluğu kanıtlanmadı. Yeni materyalizasyon/bağımlılık erişimi, ilgili source değişimi veya adoption/tasarım/güvenlik kararı bu ileri işi yeniden açar. Sadece eski fixture'ı yeniden koşmak yetmez; provider/kurulum yetkisi genişletilemez.

## 6. K01–K09 güncel ayrımları

| Kontrol | V0.8 durumu |
|---|---|
| K01 özel/genel denetim | Ortak katman kaynakta; actual review/ad-kümesi/round bağlantısı yeni. Whole-runtime verdict yok. |
| K02 hata/telafi | Exact middleware MW01–MW08, callback/downstream/once ayrımı; disk/skill rollback entegrasyonu değil. |
| K03 context transfer | Eski P/C/V kanıtları + sınırlı range AST; tam worker/PluginManager integration açık. |
| K04 approval | Ortak command/memory replay kaynakları; actual UI/identity/profile/store aktif sırada. |
| K05 memory visibility | Store/snapshot/wire statik; M01 ve gerçek rebuild readback NOT RUN. |
| K06 lifecycle | Cancel/admission/round kaynakları; actual old-worker/finalization etkisi açık. |
| K07 replay | api_content/wire kaynakları; archive/search/review eşdeğerlik koşusu yok. |
| K08 compression failure | Belge sorusu sürüyor; yeni summarizer-failure deneyi yok. |
| K09 curator batch | Nested operations/report/cron hâlâ açık. |

Callback/handler/effect/persistence; declared policy/error handling; schema acceptance/authority ve UI preview/applied revision ayrı ölçülür. Test sayıları bir ürün PASS toplamı değildir.

## 7. Revizyon geçmişi

| Revizyon | Kanıt / değişim |
|---|---|
| v0.1 | Hermes-native araştırma, Gstack yöntem disiplini, geç projeksiyon. |
| v0.2 | Review/guard/provenance/approval; transcript/store/quality ayrımı. |
| v0.3 | Curator/usage/policy/report/cron; U01-C ayrı. |
| v0.4 | U01B yayını; tam H22 ve exception/preview/durability karşı örnekleri. |
| v0.5 | 429 sırasında U01-DOC, sekiz belge ve NOT RUN kontroller. |
| v0.6 | Tree/blob caller/memory kaynağı, üç-modüllü transport; actual worker/precheck önceliği. |
| v0.7 | U01-D2 selected gerçek tüketici/worker + tam validator C/V kanıtı yayımlandı; full fidelity ve actual review ilişkisi ilk sıraya alındı. |
| v0.8 | Review constructor→schema-derived valid names, gerçek tool-round ve Relay kaynakları; 22 tanımlık manuel-range cross-check; exact middleware 8 durum. Tam fidelity/runtime açık tutulup next active actual pending/profile/store'a geçirildi. |

[Önceki tam v0.7 plan](https://github.com/batuhanozgun/agentic-os-search/blob/9a95b2cf1f8a0460ac6128e1409bf54aa3191022/research/studies/hermes-agent/RESEARCH-PLAN.md) ve Git geçmişi tüm eski ayrıntıları korur. Bu revizyon eski deneyleri yeniden yürütülmüş veya genel ürün doğrulanmış yapmaz. Yeni [10 notu](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md) bu turun iddia/sınır otoritesine yönlendirir.
