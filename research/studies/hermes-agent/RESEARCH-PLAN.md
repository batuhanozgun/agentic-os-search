# Hermes Agent — Araştırma planı

**Plan v0.9 — 2026-09-09.** U01-M2 tesliminin mevcut v0.8 üzerine kaydı; yeni deney veya tam ürün doğrulaması değildir. Güncel iş/yetki otoritesi [STATE](STATE.md); kapanış ölçütü [METHOD](METHOD.md).

## 1. Yöntem ve kapsam

Kaynak keşfi → mekanizma sorusu → kaynak/caller/etki → karşı yol → not → kapsam/sıra revizyonu. Üst sentez notları yalnız kısaltmaz; açıklanmamış geçişlerde kaynağa döner. Önce HERMES-native model, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesi. Kurulum, upstream onarımı, hata listesi veya benimseme araştırmanın yerine geçmez.

Primary pin `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0. Moving-branch araması navigasyon; pinned kaynak yerine geçmez. W belgeleri unpinned; gerçek modül, seçili tanım, statik kaynak ve ürün yürütmesi ayrı.

## 2. Aşamalar

| Aşama | Güncel statü |
|---|---|
| A0 Kimlik/pin/sınır | Sabit pin ve çalışma yetkisi kurulu; current installed release doğrulanmadı. |
| A1 Topoloji | Root/apps/agent/tools/hermes_cli kısmi listeleri; recursive tam envanter yok. |
| B0 Öğrenme kesitleri | U01 review, U01-C curator, U01B/U01B2 skill/onay, U01-M/M2 memory; aile kapanmadı. |
| U01-DOC | Sekiz resmî unpinned belge; K01–K09 tarihsel tasarım. |
| U01-D / D2 | Caller/worker ve source-selected/tam-validator deneyleri kalıcı kayıtta. |
| U01-D3 | Gerçek review kurulum/ad-kümesi/round/Relay kaynak bağı; 22 tanım için manuel-range AST; exact middleware MW01–MW08. Tam büyük-orijinal verifier ve bütün runtime hâlâ açık. |
| U01-M2 | Beş tam modül + sentetik çevre ile eski N01–N12 koşusu yayımlandı. File/live/snapshot, alias ve shared pending replay/cleanup ayrıldı; actual UI/profile/request kapanmadı. |
| C–F | Native alt-sistemler → ilişkiler → dört-alan/SOUL/DevOS → CORE/omission/freshness sentezleri henüz tamamlanmadı. |

## 3. Provisional kaynak aileleri — geniş kapsam korunur

| ID | Aile / soru | Mevcut ilerleme ve açık sınır |
|---|---|---|
| F01 | Başlama, araç döngüsü, retry, kesinti, sonlanma | Façade/prologue/worker'a gerçek tool-round eklendi; bütün yürütme ve alternatif runtime açık. |
| F02 | Prompt/context/schema/compression/cache | Schema parity ve valid names kaynakta; M2 disk/live/frozen/reload bounded readback. Gerçek prompt/request/compression açık. |
| F03 | Session kimliği/lineage/arama/onarım | Persist-before-execute ve post-effect failure ayrımı; gerçek DB/search/restore yaşam döngüsü açık. |
| F04 | Bellek/beceri/sahiplik/onay/geri alma/paylaşım | Review/curator/skill batch/store; M2 shared pending replay ve failure/cleanup yürütüldü. Actual UI/profile/store sonraki aktif iş; ledger/sync/kalite açık. |
| F05 | Provider/model/credential/profile/config | Review fork parent runtime/toolset bağı; M2 supplied-store flag kontrolü gerçek config-refresh/profil testi değil. |
| F06 | Tool/skill/plugin/MCP keşfi ve yetki | Review valid names/whitelist kaynak bağı; exact middleware failure/once. Tam Q26 runtime açık; M2 alias/sentinel actual scanner hükmü değil. |
| F07 | Backend/native etki sınırı | Güvenlik kontratı/root; cooperative kontrol OS sandbox sayılmaz. |
| F08 | Delegation/process/cancellation/worktree/yazıcılar | Worker/callback/cancel kaynakları; M2 stale store sıralı reload, full cancellation/eşzamanlılık güvencesi değil. |
| F09 | Gateway auth/session/teslim | Persistence/delivery kaynağı; actual gateway pending ve adapter farkları açık. |
| F10 | Cron/proaktif iş/kuyruk/tekrar-kayıp | Curator cron-reference/idle callsite; scheduler/restart açık. |
| F11 | CLI/TUI/desktop/web/API/ACP | Ortak approval command'ın M2 yürütmesi gerçek UI değildir; CLI/gateway caller ilk sırada. |
| F12 | Install/update/compat/test/eval/telemetri | Ayrı bounded probe kayıtları, MW01–MW08 ve N01–N12; upstream suite/release/CI/gelecek-task kalite yok. |

Family etiketi ürün modülü veya tamamlanma oranı değildir. Kaynağın bulunması aile kapanışı sayılmaz.

## 4. İlk sonraki yetkili birim ve mevcut kanıt

**U01-M / actual pending caller:** Pinned CLI ve gateway'de `/memory` ve `/skills` onay akışını ortak D17/M2-S03, D15/M2-S02 ve skill apply'e kadar takip et. İlk navigasyon adayları `hermes_cli/cli_commands_mixin.py` ve `gateway/slash_commands.py`; ilgili callsite'ları primary pin'de aç. Onaylayan kimlik, aktif home/profil, live/fresh store ve başarı/pending silme sırası bir arada açıklanmalı. Command docstring'i, dosya adı veya ortak command fixture'ı UI kanıtı değildir.

**Yapılmış M01/M02'yi tekrar ilk iş sayma:** M2/N02 ve N09, kontrollü pre-commit hata sonrası disk/live/snapshot ve reload/retry ayrımını; N07 sentetik scanner ile alias ön-tarama ve load-time masking ayrımını çalıştırdı. N01/N04/N06 normal/silme/stale-store görünümünü; N08–N12 staged/apply/failure/cleanup koşullarını ekledi. Gerçek scanner, UI config-refresh, bütün replay türleri veya API-wire doğrulanmış değil. Aynı 12 fixture'ı çoğaltmak gerçek caller bağlantısını kapatmaz.

**Ardından:** File/live/frozen snapshot → AIAgent prompt rebuild/compression/reload → gerçek isteğin hazırlanması. Kaydedilmiş hata ve silme senaryolarını bu bağlamdaki readback'e taşı; yalnız add happy-path ile yetinme. Provider/credential kullanımı veya kurulum yetkisi genişletilmez.

**Sonraki bağlantılar:** review trigger/cancel/idle/shared-store; ledger/backup/restore/sync; sonraki skill/cache yükleme; U01-C curator nested operations/report/cron. U01B2 default_name staging/replay, preview/hedef sürümü, rollback/başka-yazar izolasyonu bu gerçek yollara bağlanır.

**Sıra gerekçesi:** V0.8, tam yerel E01/E02 materyalizasyonu kurulamadığı için daha dar range cross-check ve gerçek kurulum/round/middleware kaynaklarıyla Q26'yı ilerletip güçlü hükmü açık bırakmıştı. V0.9 bu bilinçli sırayı korur ve aynı eski research tabanından gelen ayrı M2 dilimini kayda alır. M2'nin bağımsız çalışma diliminde önden yaptığı store testleri artık görünürdür; D3 ilerlemesi geri alınmaz. Bu teknik bütünlük kapanışı değil, kanıt/yayın uzlaştırmasıdır.

**U02:** Daha genel work/context/session yaşam döngüsü. **U03:** Provider/tool/plugin/backend/delegation yetki ve etki. **U04+:** Gateway/cron/UI/install/eval ve kalan varyantlar. Kaynak bağımlılığı farklı sıra gerektirirse kanıt ve gerekçe kaydedilir. Tek whitelist veya alias adayı bütün araştırmayı tüketmemeli.

## 5. Açık ileri doğrulama — Q26/Q29

22 AST eşleşmesi, iki manuel transkripsiyonun bounded cross-check'idir. E01/E02 tam dosya Git hash + eski verify_excerpts.py kontrolü NOT RUN. Bu daha güçlü kontrol imkân oluştuğunda veya bulgu load-bearing reuse'a geçtiğinde yapılmalı.

Gerçek review/fork → actual valid names → tam ordinary executor/PluginManager/middleware/Relay → zararsız handler birlikte koşulmadı. Statik standart kurulumda parent toolset → schema-derived valid names ve ayrı review whitelist görüldü; tüm runtime/ek kontrol yokluğu kanıtlanmadı. Yeni materyalizasyon/bağımlılık erişimi, ilgili source değişimi veya adoption/tasarım/güvenlik kararı bu ileri işi yeniden açar. Sadece eski fixture'ı yeniden koşmak yetmez; provider/kurulum yetkisi genişletilemez. M2'nin beş tam bellek modülü eksik worker bağımlılıklarını tamamlamaz.

## 6. K01–K09 güncel ayrımları

| Kontrol | V0.9 durumu |
|---|---|
| K01 özel/genel denetim | Ortak katman kaynakta; actual review/ad-kümesi/round bağlantısı. Whole-runtime verdict yok. |
| K02 hata/telafi | Exact middleware MW01–MW08 callback/downstream/once; M2 pre-commit write-error disk/live farkı ayrı. Skill rollback tam dispatch entegrasyonu yok. |
| K03 context transfer | Eski P/C/V + sınırlı range AST; tam worker/PluginManager integration açık. |
| K04 approval | Shared command/replay M2 N08–N12 ile yürütüldü; proposal/apply origin ve cleanup ayrıldı. Actual UI/identity/profile/store aktif sırada. |
| K05 memory visibility | M2 normal/failure/remove/reload disk/live/frozen readback; gerçek prompt rebuild/API request görünümü hâlâ NOT RUN. Alias sentetik scanner + load-time karşı-kontrol actual scanner deneyi değil. |
| K06 lifecycle | Cancel/admission/round kaynakları; actual old-worker/finalization etkisi açık. |
| K07 replay | api_content/wire kaynakları; M2 pending replay bu ayrı arşiv/search/review eşdeğerlik sorusunu kapatmaz. |
| K08 compression failure | Belge sorusu sürüyor; yeni summarizer-failure deneyi yok. |
| K09 curator batch | Nested operations/report/cron hâlâ açık. |

Callback/handler/effect/persistence; declared policy/error handling; schema acceptance/authority ve UI preview/applied revision ayrı ölçülür. Test sayıları ürün PASS toplamı değildir. N06 sıralı fixture, N10 supplied-store flag, N11 add idempotence tüm eşzamanlılık/config/tekrar davranışlarının garantisi değildir.

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
| v0.9 | ZIP'teki ayrı U01-M2 beş tam modül/N01–N12 kaydı v0.8 korunarak yayımlandı; M01/M02 artık bounded yürütme. Actual UI/profile/request ve Q26 ileri sınırları açık. Bu revizyonda deney tekrarlanmadı. |

[Önceki tam v0.8 plan](https://github.com/batuhanozgun/agentic-os-search/blob/c0ef2374a34cbb30f5f58a28333f89254931b00f/research/studies/hermes-agent/RESEARCH-PLAN.md), [v0.7](https://github.com/batuhanozgun/agentic-os-search/blob/9a95b2cf1f8a0460ac6128e1409bf54aa3191022/research/studies/hermes-agent/RESEARCH-PLAN.md) ve Git geçmişi eski ayrıntıları korur. [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md) ile [11](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md) ayrı kanıtlara yönlendirir. Özgün teslimlerdeki NOT PUBLISHED ve eski plan ifadeleri [M2 yayın kaydıyla](evidence/2026-09-09-memory-pending/PUBLICATION.md) tarihsel bağlama alınır.
