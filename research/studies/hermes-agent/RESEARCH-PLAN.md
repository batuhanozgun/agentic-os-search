# Hermes Agent — Araştırma planı

**Plan v0.10 — 2026-09-10.** U01-M3 gerçek UI/profile caller source trace ve bounded slash-policy kanıtı. İş/yetki otoritesi [STATE](STATE.md); yöntem ve kapanış [METHOD](METHOD.md). Önceki [tam v0.9 plan](https://github.com/batuhanozgun/agentic-os-search/blob/91af4415c22e05b80484b935383ceeb04a3c5b7b/research/studies/hermes-agent/RESEARCH-PLAN.md) korunur.

## 1. Amaç, pin ve döngü

Kaynak keşfi → mekanizma sorusu → caller/uygulama/etki → karşı yol → not → kapsam/sıra revizyonu. Önce HERMES-native model; sonra Information/Work/Actors/Environment ve SOUL/Development OS. Kurulum, hata avı, upstream onarımı veya adoption araştırmanın yerine geçmez.

Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0. Moving-branch search sadece navigasyon; current release doğrulaması değil. W belgeleri unpinned kalır. Kaynak okuma, selected definition, tam module execution ve product runtime ayrı statülerdir.

## 2. Birikimli aşamalar

A0 pin/sınır kurulu. A1 topoloji kısmi; recursive tam envanter yok. B0 öğrenme kesitleri review/curator/skill onayı/caller/memory boyunca ilerledi; tam aile kapanışı yok. U01-DOC sekiz belge/K kontrolleri; D/D2/D3 ve M2 eski statüleriyle korunur.

**Yeni U01-M3:** CLI live/fresh ile gateway fresh store; normal ingress/slash/busy-idle/adapter-profile/shared apply source zinciri; config-mode vs payload-apply/cache ayrımı; UI08 tam modülle sekiz policy diagnostic ve iki ayrı negative control. Full UI/profile/worker/provider run yok.

C–F native alt-sistemler → ilişkiler → dört-alan/SOUL/DevOS → CORE/omission/freshness sentezleri henüz tamamlanmadı.

## 3. Provisional kaynak aileleri

| ID | Aile | Güncel ilerleme / açık sınır |
|---|---|---|
| F01 | Başlama, araç döngüsü, retry, kesinti, sonlanma | Facade/round/worker ve inbound busy/idle kaynakları; tüm runtime alternatifleri açık. |
| F02 | Prompt/context/schema/compression/cache | Önceki frozen/live/wire; yeni approve vs mode eviction ayrımı. **Onaydan prepared request'e geçiş ilk aktif iş.** |
| F03 | Session/lineage/arama/onarım | Persist-before-execute ve session sıra kontrolleri; gerçek DB/search/restore yaşam döngüsü açık. |
| F04 | Bellek/beceri/sahiplik/onay/geri alma/paylaşım | M2 beş-modül kanıtı ve gerçek CLI/gateway supplied-store source bağı. Ledger/sync/kalite, full UI hata yolları açık. |
| F05 | Provider/credential/profile/config | Adapter profile scope/transport-authority damgası ve home önceliği kaynakta. Gerçek credentials/full resolver yok. |
| F06 | Tool/skill/plugin/MCP keşfi ve yetki | Review/worker/middleware eski kanıtı; yeni canonical slash-name policy. Full Q26 runtime açık. |
| F07 | Backend/native etki sınırı | Cooperative/context-local kontroller OS sandbox değildir; bütün backend araştırması açık. |
| F08 | Delegation/cancellation/worktree/yazarlar | Worker/cancel ve busy-session kaynakları; aynı profile'ın çok-yazar bütün izolasyonu açık. |
| F09 | Gateway auth/session/teslim | Normal ingress, primary/secondary profile wrapper, idle pending source trace. Tüm platform/admission varyantları doğrulanmadı. |
| F10 | Cron/proaktif iş/kuyruk/tekrar-kayıp | Curator/idle referansları; scheduler/restart ve report bağı açık. |
| F11 | CLI/TUI/desktop/web/API/ACP temsil/yetki | Gerçek CLI/gateway memory/skills çağrıları, diff kesintisi; diğer UI ve live bütünlük açık. |
| F12 | Install/update/compat/test/eval/telemetri | Ayrı eski probes + UI08 A01–A08. UI09 kaynak testi NOT RUN; product suite/kalite/current release yok. |

Family etiketi tamamlama oranı değildir; bir mekanizma birden fazla aileye bağlıdır.

## 4. İlk sonraki yetkili birim — U01-M görünürlük

Soru: `/memory approve <id>` sonrası yeni disk verisi, mevcut CLI ajanında ve gateway cached-agent reuse yolunda ne zaman model için hazırlanmış isteğe girer?

İlk kaynak rotası: 12/UI01/UI02 → memory store load/frozen snapshot (07/11) → turn prologue/system prompt invalidation → gateway cached agent reuse → prepared request assembly. Gerekli dosyalar pinned source üzerinden sembol/caller takibiyle bulunur; unpinned web açıklaması asıl kod yerine geçmez.

Ayrı olaylar: payload apply; pending cleanup; mode config write; cache eviction; store reload; frozen snapshot refresh; prompt rebuild; prepared request. Birinin başarılı olması diğerinin gerçekleştiğini kanıtlamaz. Mevcut cached/resident agent'ın yokluğu varsayılmaz; getter yardımcıları kaynakta var.

Karşı açıklamalar: next turn her seferinde reload ediyor olabilir; cached agent farklı invalidation şartıyla yenilenebilir; CLI current store ile gateway fresh apply nesnesinin ömrü farklı olabilir; başka profile aynı home'a yönlenmiyor olabilir. Önce bu ayrımları kaynakla aç. Sonra güvenli offline readback mümkünse provider çağırmadan sınanır; gerçek ve synthetic bağımlılıklar ayrı tutulur.

Durma/devam: gerekli hazırlanan-request bağı kurulamazsa tam hangi halka ve hükmün açık kaldığı yazılır; kurulum/provider yetkisi genişletilmez. Aynı eski A/N/C/V fixture'larını çoğaltmak full-path kanıtı yerine geçmez.

## 5. İleri onay sınırları ve genel devam

Q05/Q23/Q24 normal source yolu ilerledi; bütün auth/profile/UI kapandı denmez. Gerekince: actual transport authorization/profile resolver; command hook rewrite sonrası gate; multi-session config/cache scope; per-record actor/version bağlama; full UI cleanup hata enjeksiyonu ve diff/profile gösterimi.

Sonra ledger/backup/restore/sync → skill/cache reuse → U01-C nested batch/report/cron ve trigger/cancel/shared-store. U01B2 default_name/replay/preview ve rollback/diğer-yazar soruları gerçek yollara bağlanır. U02 genel work/context/session, U03 provider/tool/plugin/backend/delegation, U04+ gateway/cron/UI/install/eval genişliği korunur.

## 6. Ertelenmiş Q26/Q29

Full E01/E02 originals + legacy verify_excerpts.py NOT RUN. D3'ün 22 manuel-range AST eşleşmesi full identity/fidelity değildir. Actual review/fork/valid names/executor/PluginManager/middleware/Relay/handler ortak koşusu açık. Yeni materyalizasyon/bağımlılık erişimi, source değişimi veya bulgunun load-bearing reuse'a geçmesi yeniden açar. Başlangıçtaki `run_agent.py` erişim engeli kapanmıştı; eski 429'a dönüp tekrar başlama.

## 7. K01–K09

K01 ortak denetim: source/selected kanıt, whole-runtime yok. K02 hata/telafi: MW + M2 ayrı; full skill rollback/UI yok. K03 aktarım: P/C/V ve sınırlı AST; full worker hâlâ açık. **K04 approval: artık actual CLI/gateway source zinciri + bounded UI08 policy; full interface execution değil.** **K05 memory visibility: M2 disk/live/frozen ve M3 caller ömrü; actual prompt/request readback ilk aktif iş.** K06 lifecycle: kaynaklar kısmi; full cancellation yok. K07 replay: sidecar/wire statik; bütün temsil eşdeğerliği yok. K08 compression failure ve K09 curator report/batch açık.

## 8. Revizyon ve yayın

V0.1–v0.9 exact tarihçe önceki plan/Git geçmişindedir. V0.10 değişimi: v0.9'da ilk sıradaki normal UI/profile/shared-store source bağı incelendi; politika granülerliği actual küçük modülle sınandı. Sonraki halka artık onaydan prompt/request'e görünürlüktür. Bu mekanizmanın bütün runtime/security/quality kapanışı değildir.

Yeni [12](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md) ve [UI evidence](evidence/2026-09-10-ui-profile/README.md). Eski not/kanıtlar değişmez. Kaynak defteri progressive retrieval olarak eski v0.9 içeriğinin exact kopyası ve yeni UI defterini birlikte yönlendirir. Katalog yalnız HERMES satırında güncellenir; control/Foundation/context/Codex/başka study dosyalarına dokunulmaz. Yayın ref ve content readback ile ayrıca doğrulanır.
