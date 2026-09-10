# Hermes Agent — Araştırma planı

**Plan v0.11 — 2026-09-10.** Mevcut v0.10 UI/A çalışması korunarak ayrı M3-S/SA pending-caller teslimi yayımlandı; bu revizyon yeni deney değildir. İş/yetki [STATE](STATE.md); yöntem ve kapanış [METHOD](METHOD.md). [Önceki tam v0.10 plan](https://github.com/batuhanozgun/agentic-os-search/blob/159936556f34e7e0e1dafcb54c087bef994cf5ba/research/studies/hermes-agent/RESEARCH-PLAN.md) korunur.

## 1. Amaç, pin ve döngü

Kaynak keşfi → mekanizma sorusu → caller/uygulama/etki → karşı yol → not → kapsam/sıra revizyonu. Önce HERMES-native model; sonra Information/Work/Actors/Environment ve SOUL/Development OS. Kurulum, hata avı, upstream onarımı veya adoption araştırmanın yerine geçmez.

Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0. Moving-branch search sadece navigasyon; current release doğrulaması değil. W belgeleri unpinned kalır. Kaynak okuma, selected definition, tam module execution ve product runtime ayrı statülerdir.

## 2. Birikimli aşamalar

A0 pin/sınır kurulu. A1 topoloji kısmi; recursive tam envanter yok. B0 öğrenme kesitleri review/curator/skill onayı/caller/memory boyunca ilerledi; tam aile kapanışı yok. U01-DOC sekiz belge/K kontrolleri; D/D2/D3 ve M2 eski statüleriyle korunur.

U01-M3 **UI/A:** CLI live/fresh ile gateway fresh store; normal ingress/slash/busy-idle/adapter-profile/shared apply source zinciri; config-mode vs payload-apply/cache ayrımı; UI08 tam modülle sekiz policy diagnostic ve iki ayrı negative control. Full UI/profile/worker/provider run yok.

U01-M3 **M3-S/SA ek teslimi:** aynı pin'e bağlı ayrı source defteri/araştırma, SA01–SA08 ve kendi pre-import source reddi. UI/A koşusuna birleştirilmez. M3-S12/S13 prompt/invalidation/cache kaynaklarını ilk görünürlük işine bağlar; gerçek request ölçümü değildir. Yayın sırasında her iki eski koşu ve tüm eski deneyler tekrar edilmedi.

C–F native alt-sistemler → ilişkiler → dört-alan/SOUL/DevOS → CORE/omission/freshness sentezleri henüz tamamlanmadı.

## 3. Provisional kaynak aileleri

| ID | Aile | Güncel ilerleme / açık sınır |
|---|---|---|
| F01 | Başlama, araç döngüsü, retry, kesinti, sonlanma | Facade/round/worker ve inbound busy/idle kaynakları; tüm runtime alternatifleri açık. |
| F02 | Prompt/context/schema/compression/cache | Frozen/live/wire ve approve vs mode eviction; M3-S12/S13 build/invalidate/cache bağı. Onaydan prepared request'e geçiş ilk aktif iş. |
| F03 | Session/lineage/arama/onarım | Persist-before-execute ve session sıra kontrolleri; gerçek DB/search/restore yaşam döngüsü açık. |
| F04 | Bellek/beceri/sahiplik/onay/geri alma/paylaşım | M2 beş-modül ve gerçek CLI/gateway supplied-store source bağı; ledger/sync/kalite, full UI hata yolları açık. |
| F05 | Provider/credential/profile/config | Adapter scope/transport damgası/home önceliği ve SA supplied-config duyarlılığı; full resolver/config lifecycle/credential koşusu yok. |
| F06 | Tool/skill/plugin/MCP keşfi ve yetki | Review/worker/middleware ve ayrı A/SA slash-policy kanıtları; full Q26 runtime açık. |
| F07 | Backend/native etki sınırı | Cooperative/context-local kontroller OS sandbox değildir; bütün backend araştırması açık. |
| F08 | Delegation/cancellation/worktree/yazarlar | Worker/cancel/busy kaynakları; aynı profile'ın çok-yazar izolasyonu açık. |
| F09 | Gateway auth/session/teslim | Normal ingress/profile wrappers/pending source trace; tüm platform/admission varyantları doğrulanmadı. |
| F10 | Cron/proaktif iş/kuyruk/tekrar-kayıp | Curator/idle referansları; scheduler/restart/report açık. |
| F11 | CLI/TUI/desktop/web/API/ACP temsil/yetki | Actual CLI/gateway memory/skills çağrıları/diff kesintisi; diğer UI ve live bütünlük açık. |
| F12 | Install/update/compat/test/eval/telemetri | Ayrı eski probes, UI/A ve M3-S/SA. UI09/M3-S10 kaynak testleri NOT RUN; product suite/kalite/current release yok. |

Family etiketi tamamlama oranı değildir; bir mekanizma birden fazla aileye bağlıdır.

## 4. İlk sonraki yetkili birim — U01-M görünürlük

Soru: `/memory approve <id>` sonrası yeni disk verisi, mevcut CLI ajanında ve gateway cached-agent reuse yolunda ne zaman model için hazırlanmış isteğe girer?

Kaynak rotası: 12/UI caller ve 13/M3-S12/S13 → `agent/conversation_loop.py::_restore_or_build_system_prompt` → store/frozen snapshot (07/11) → invalidation/rebuild/compression/keep-prompt → cached-agent reuse/eviction → prepared request. Gerekli dosyalar primary pin'den sembol/caller takibiyle açılır; unpinned açıklama gerçek kod yerine geçmez.

Ayrı olaylar: payload apply; pending cleanup; mode config write; cache eviction; store reload; frozen snapshot refresh; DB'den stored prompt restore; prompt rebuild; prepared request. Birinin başarısı diğerini kanıtlamaz. Cached/resident agent yokluğu varsayılmaz; getter yardımcıları kaynakta vardır.

Rakip açıklamalar: next turn reload edebilir; cached agent farklı invalidation şartıyla yenilenebilir; yeni store eski DB system prompt'unu restore edebilir; CLI live/fresh apply nesne ömrü farklı olabilir; başka profile farklı home'a yönlenebilir. Bunlar peşinen kabul edilmez. Önce source bağı, sonra mümkünse zararsız offline readback; provider/model/credential veya kurulum yetkisi genişletilmez. Normal yazım/silme/hata/restore karşı senaryolarını ayır.

Gerekli prepared-request bağı kurulamazsa tam açık halka ve hüküm kaydedilir. Aynı A/SA/N/C/V fixture'larını çoğaltmak full-path kanıtı değildir. Actual normal UI caller'ların ilk keşfi tamamlanmış kaynak işi olarak korunur; yeniden başa dönülmez.

## 5. İleri onay sınırları ve genel devam

Q05/Q23/Q24 normal source yolu ilerledi; bütün auth/profile/UI kapandı denmez. İleri sınırlar: actual transport authorization/profile resolver; command hook rewrite sonrası gate; multi-session config/cache scope; record/actor/revision bağlama; full UI cleanup hata enjeksiyonu ve diff/profile gösterimi. SA06 supplied-config duyarlılığı deployment açığı, SA08 boş chat_type normal adapter kusuru değildir.

Sonra ledger/backup/restore/sync → skill/cache reuse → U01-C nested batch/report/cron ve trigger/cancel/shared-store. U01B2 default_name/replay/preview ve rollback/diğer-yazar soruları gerçek yollara bağlanır. U02 genel work/context/session, U03 provider/tool/plugin/backend/delegation, U04+ gateway/cron/UI/install/eval genişliği korunur. Tek whitelist/alias/policy adayı bütün araştırmayı tüketmez.

## 6. Ertelenmiş Q26/Q29

Full E01/E02 originals + legacy verify_excerpts.py NOT RUN. D3'ün 22 manuel-range AST eşleşmesi full identity/fidelity değildir. Actual review/fork/valid names/executor/PluginManager/middleware/Relay/handler ortak koşusu açık. Yeni materyalizasyon/bağımlılık erişimi, source değişimi veya load-bearing reuse yeniden açar. Başlangıçtaki run_agent.py erişim engeli tarihsel; eski 429'a dönüp yeniden başlanmaz.

## 7. K01–K09

K01 source/selected ortak denetim, whole-runtime yok. K02 MW+M2 hata/telafi ayrı; full skill rollback/UI yok. K03 P/C/V ve sınırlı AST; full worker açık. K04 actual CLI/gateway source zinciri ve ayrı A/SA policy kanıtı, full interface execution değil. K05 M2 disk/live/frozen + M3 caller/prompt source bağı; actual stored-prompt/prepared-request readback ilk aktif iş. K06 lifecycle kaynakları kısmi/full cancellation yok. K07 sidecar/wire statik; tam temsil eşdeğerliği yok. K08 compression failure ve K09 curator report/batch açık.

## 8. Revizyon ve yayın

V0.1–v0.9 exact tarihçe önceki plan/Git geçmişindedir. V0.10 normal UI/profile caller ve UI/A kanıtını ekleyip prompt/request'e geçti. **V0.11**, ZIP'teki ayrı M3-S/SA teslimini v0.10 korunarak kaydeder; aynı devam yönüne stored-prompt restore somut rotasını ekler. Araştırma veya bütün runtime/security/quality kapanışı değildir; yayın sırasında deney tekrarı yoktur.

[12/UI](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md) değişmez. [13/M3-S-SA](notes/13-PENDING-CALLER-EVIDENCE-RECONCILIATION.md), [PUBLICATION](evidence/2026-09-10-pending-caller/PUBLICATION.md) ve [TRANSFER-CHECK](evidence/2026-09-10-pending-caller/TRANSFER-CHECK.json) yeni teslimi ayırır. Özgün 12 taslağı/NOT PUBLISHED/NOT APPLIED delivery altında tarihsel tutulur. Eski notes/evidence ve exact v0.9 source arşivi korunur. Katalog yalnız HERMES satırında değişir; control/Foundation/context/Codex/diğer study'lere dokunulmaz. Main ve content readback yayın doğrulamasıdır.
