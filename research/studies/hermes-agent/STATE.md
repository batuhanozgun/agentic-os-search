# Hermes Agent — STATE

**2026-09-13 / U13 / plan v0.26 — COMPLETION TO PARENT RE-ENTRY.**
**Statü:** ACTIVE PARTIAL RESEARCH. Q57 CLI/TUI source oku ilerledi; bounded manual-selection diagnostic yapıldı. Bütün HERMES, full runtime ve kalite kapanmadı.
**Primary:** NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a / manifest0.21.0; current release/kurulu binary değil.
**Güncel publication authority:** [U13 PUBLICATION](evidence/2026-09-13-delegation-reentry/PUBLICATION.md). STATE başlığı tek başına ref/content kanıtı değildir. [PLAN](RESEARCH-PLAN.md), [METHOD](METHOD.md), [INDEX](INDEX.md), [META](META.md).

## Amaç, yetki ve gerçekleşen incremental kapılar

Kullanıcının “Anlaştık. Devam et. Operasyonel sınırına kadar çalış.” yetkisiyle kayıtlı Q57 sürdürüldü. Amaç önce HERMES-native mekanizma/ilişkiler; sonra CORE ve ayrı daha-geç dört-alan/SOUL/Development OS aday değerlendirmesi. Implementation/adoption veya canlı kurulum yetkisi yoktur.

Başlangıç main **74c5e3d1dcd260a1841c64dda5fb1d182f7bb299**. Q57 opening PLAN **899422ceba05f7b6a577b35baf6a985c317b7cf7** actual main/ref, tam plan ve tek-path compare ile doğrulandı. A kaynak/SPEC **2ef205a9bf13d166c15a630e4320dd73eb190fb2** nonforce main'e bağlandı; araştırma/kaynak/SPEC/STATE tam geri okunduktan sonra B başladı. B diagnostic/raw **1372287c9b0806c1d0103cc1c9351bcf4dd69b08** yayımlandı; actual main ve beş metin geri okundu, arşivin main'e bağlı blob kimliği local/create_blob kimliğiyle eşleşti. Sonra kapsam değerlendirmesi yapıldı. Final routing/receipt sonucu PUBLICATION'dadır.

Yalnız HERMES paketi ve CATALOG HERMES satırı değişebilir. Foundation, context/Codex, AGENT/agent-control, diğer studies, upstream, architecture/adoption ve izin/credential ayarları değişmez. Full ürün/model/provider/NAS/native backend/servis başlatma yok; background devam yoktur. Bir anlamlı dilim main/ref/content doğrulanmadan ikinci büyük dilim biriktirilmez. Yayın engelinde mevcut dilim çözülür.

## U13'te gerçekten yapılan

[Note28](notes/28-DELEGATION-COMPLETION-AND-PARENT-REENTRY.md) → [A](evidence/2026-09-13-delegation-reentry/RESEARCH.md)/[SOURCES](evidence/2026-09-13-delegation-reentry/SOURCES.md) → [B](evidence/2026-09-13-delegation-reentry/DIAGNOSTIC.md)/[SPEC](evidence/2026-09-13-delegation-reentry/SPEC.md)/[MANIFEST ve raw](evidence/2026-09-13-delegation-reentry/MANIFEST.json).

U12 producer→ProcessRegistry startup restore→ownership/format→CLI queue ack ve TUI local-running/claim/submit ack→actual parent history/run_conversation bağlandı. Event ownership, turn-slot, thread schedule, facade lease ve model completion ayrı. CLI ack'i volatile input kabulüne, TUI ack'i no-exception submit dönüşüne bağlanabilir. Alt False'un üst ack'e aktarılmaması kaynakla gösterildi; bütün product'a genellenmedi.

**Gerçek B koşusu:** manuel sekiz işlev seçkisi, sekiz D durumu ve iki duyarlılık değişikliği, bir invocation. D02/D03/D04/D07 schedule olmadan ack-request; D05 claimNone sonrası running residue; D06 exception release; D08 boş-token ayrımı. SPEC koşudan önce main'deydi. Hash bağlı 11-member raw arşiv, kaynak/input/probe/tam RESULT/logları korur. **Tam parent byte/AST sadakati doğrulanmadı.** Thread target/model ve SQL/SessionDB çalışmadı; gerçek gateway/OS/credential/network/suite yok. Expected trace eşleşmesi product PASS değil. [NOT RUN](evidence/2026-09-13-delegation-reentry/CHECKS-NOT-RUN.md).

Aynı pinned heartbeat yolu False'u kontrol edip fire'ı geri alır; source karşı örnek, bu tur heartbeat run'ı değildir. Restore/interim, task-context vs formatter ve UI/model görünümü ayrımları korunur. B gerçek durable delivery/data-loss/kalite gözlemi değildir.

## Kapsam değerlendirmesi ve ilk sonraki geniş soru — Q58

[Kapsam değerlendirmesi](inventory/SCOPE-REVIEW-2026-09-13-U13.md): yürütme/devam/zaman/runtime/delegation/consumer omurgası genişledi. F04 learning çekirdeği derin ama ledger/sync/curator/quality açık; F12 kurulum/güncelleme/etkinleştirme yaşamı ise henüz benzer native açıklamaya sahip değil. Q57'nin tüm fault matrisini bitirmeyi genişlemenin ön koşulu yapmak reddedildi.

**Q58 — Kaynak/dağıtım paketi ve bağımlılıklar nasıl kurulu komut, home/profile/config ve etkin runtime'a dönüşür; update bu kimlikleri ve kullanıcı durumunu nasıl korur/değiştirir?** İlk route pinned root tree f54f5e9d2682bf11f164de7b34ee10ec121b6434 → README/manifest/entrypoint → gerçek installer/updater. `scripts/`, `apps/bootstrap-installer/` alternatifleri progressive discovery ile açılır; guessed path kullanılmaz.

En az normal install/activation ve bir materially farklı update/refusal/interruption/desktop yolu source düzeyinde karşılaştırılmalı. Repository ref, downloaded/installed artefact, config ve active process eşitlenmez. **Q58 henüz araştırılmadı; yalnız sonraki soru belirlendi.** Bu, kullanıcıya yazılım kurma/güncelleme eylemi değildir. İlk anlamlı Q58 diliminden sonra learning/skill-ledger/sync ve eval/quality adayları tekrar tartılır. Dört provisional synthesis korunur, CORE/dört-alan aşamasına geçilmez.

## Korunan önceki çalışmalar ve residual'lar

METHOD, notes01–27, U04–U12 bütün evidence/yayınlar, synthesis01–04 ve U13 A/SPEC/B özgün evidence değişmez; yeni publication/metadata makbuzları ayrı yazılır. U04-A/18 ile U04-B/19 aynı numarada aynı vakalar değildir; B33 original subtree **d01c92f7414713300934be3bb4e3d40ac57631b3** ve [uzlaştırma](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. U08–U12 eski ZIP'leri bekleyen işler değildir.

Q57 full-parent fidelity, actual DB ack/claim expiry, CLI queue/restart, TUI late release/first request, messaging adapter/API ve bilgi sadakati açıktır. Q54 actual policy/child/context/cancel, Q55 native binding/history, Q56 terminal/persistence; Q40/Q42 DB/quiet/startup, Q47 timing/store, Q48/Q50 transport/cancel, U10 Q49 full run_job/Q51 request-quality/Q52 detection-handling ve eski Q07/Q22/Q26/Q29/Q38 quality/fidelity/whole-worker borçları kapanmaz. Erteleme kapanış değil; güçlü reuse veya karşı kanıt ilgili ölçümü tekrar açar.

## Cold-start ve retrieval

1. Current AGENT/tetiklenen protokoller→research root/catalog→META/STATE/INDEX→METHOD/PLAN; U13 PUBLICATION üstü güncel yayın hükmü. Opening/A/B historical prepared ifadelerini yeniden yapılacak iş sayma.
2. Note28+A RESEARCH/SOURCES+B DIAGNOSTIC+SPEC+MANIFEST+NOT RUN ve SCOPE-REVIEW-2026-09-13-U13 tam okunur. Exact D/N hükmünde raw source/INPUTS/probe/tam RESULT/loglar okunur; derived summary yetmez.
3. U12 note27/A-B/source/NOT RUN; U11 note26/A-B/source/NOT RUN; synthesis02 ordinary-loop, synthesis03 continuation ve synthesis04 scheduled-work birlikte okunur. U10 note25/SOURCES/RESEARCH/NOT RUN; exact C iddiasında SPEC+RESULT+MANIFEST/raw. Aynı-conversation değişmeyen tam okumalar reuse olabilir, yeni bağımsız kanıt değildir.
4. U04 zorunlu ayrımı note19+B README/RECONCILIATION/manifest, synthesis03+A SOURCES/RESEARCH/CONTINUITY-COVERAGE ile korunur. Genel learning için synthesis01 ve not rotaları; exact kaynak için ilgili ledger. [Exact U12 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/74c5e3d1dcd260a1841c64dda5fb1d182f7bb299/research/studies/hermes-agent/STATE.md) önceki U11/U10 ayrıntılı rotaları korur. MAP/catalog derived'dır.
