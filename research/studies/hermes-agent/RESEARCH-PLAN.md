# Hermes Agent — Araştırma planı

**v0.13 / 2026-09-10.** AP recovery checkpoint'inden sonra yeni M4 selector araştırması/koşusu ve ilk geçici alt-sistem sentezi. İş otoritesi [STATE](STATE.md), kapanış [METHOD](METHOD.md), sıra gerekçesi [SCOPE-REVIEW](inventory/SCOPE-REVIEW-2026-09-10.md). [v0.12 tam plan](https://github.com/batuhanozgun/agentic-os-search/blob/a14c8152a918a3379b4a0d6d67af9f7aece2f70e/research/studies/hermes-agent/RESEARCH-PLAN.md) korunur.

## 1. Araştırma hedefi ve yeni düzey

Önce HERMES-native mekanizmalar/ilişkiler, sonra Information/Work/Actors/Environment ve SOUL/Development OS. Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0. W belgeleri unpinned; current release veya kurulu ürün değerlendirmesi değil.

A0 pin/yöntem kurulu. A1 topoloji kısmi. B0 öğrenme/onay/bellek mekanizmaları derin fakat tam aile kapanışı yok. **C katmanında ilk provisional learning/change sentezi artık var**; bütün native alt sistemler veya genel ilişkiler tamamlanmadı. Dört-alan/CORE/quality açık. Plan sürümü, not ve test sayısı tamamlanma oranı değildir.

## 2. Bu turdaki fark

14/AP: eski altı senaryo ve 15 özgün dosyanın recovery'si; A/SA'dan ayrı, yeni deney değil. M4: beş archived full-module + altı selected definition ile V01–V08; fresh-store/old-stored-prompt, fresh build alternatifleri, delete/fault/reload/persist ayrımları. SPEC ve mutant/identity kontrolleri kaydedildi. Full parent byte fidelity, gerçek UI/SQLite/compression/request/builder/provider yok. **Q07/Q22 yalnız bounded olarak ilerledi; uçtan uca kapanmadı.**

[15](notes/15-MEMORY-PROMPT-RESTORE-BOUNDARIES.md) → [M4 kaynaklar](evidence/2026-09-10-prompt-restore/SOURCES.md). [Synthesis/01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md) bu sonucu eski kanıtla bağlar; açık kenarı görünür tutar.

## 3. İlk sonraki birim: genel çekirdek ve kapsam karşı okuması

Soru: öğrenme/değişim kesitinin dışındaki HERMES, bir işi kabul edip bağlam oluşturma, araç/model aşamalarına taşıma, durumu kalıcılaştırma ve devam/sonlanma işini hangi mekanizmalarla yürütür? Bu açıklama provisional modeli nerede değiştirir?

Önce pinned alt-tree/entrypoint haritası: agent ve genel session/state yüzeyleri; ardından tool/provider/backend/delegation, gateway/cron ve apps/install/eval. Dosya sayısı kota değildir; listelenmiş, okunmuş, kaynakla açıklanmış, koşulmuş ve sentezlenmiş ayrı işaretlenir. İlk envanter STRUCTURE yalnız kök düzeyini taşıyordu; onun yeterliliği varsayılmaz.

İlk davranış rotası M4-S03'te açılan `run_conversation`: build_turn_context'e verilen restore callback → returned state → iteration/request assembly/preflight/retry → tool/finalizer/persistence. Actual `turn_context`, `turn_request_assembly`, compression/keep-prompt ve gateway cache yollarına erişim sağlanınca eksik görünürlük bağı burada tamamlanır. Kod seçicisi final request sanılmaz; alternative app-server/transport yolu ordinary-loop ile eşdeğer kabul edilmez.

Beklenen çıktı: genel çekirdeğin provisional davranış haritası; önemli bağımlılık/kontrol/kalıcılık geçişleri; dışarıda bırakılan aileler ve gerekçeler; hangi yeni alt-sistemin en yüksek açıklama değerine sahip olduğuna dair kapsam kararı. Bir seçili yol bütün ürün closure'ı değildir. Salt yeni tree listesi de mekanizma sentezi sayılmaz.

## 4. Aile haritası ve ileri köprüler

| Aile | Mevcut durum / sonraki bağlantı |
|---|---|
| F01 başlama/loop/retry/interrupt | Selected source → **genel çekirdek ilk aktif genişleme**. |
| F02 prompt/context/schema/compression/cache | M4 stored-prompt seçimi bounded; gerçek request/caller OPEN ve genel çekirdekte yük taşıyor. |
| F03 session/lineage/search/repair | Persist/wire selected; genel session/restore/search modeli açık. |
| F04 memory/skill/approval/rollback/sync | Derin notlar + provisional learning/change; ledger/sync/skill reuse köprüleri açık. |
| F05 provider/credential/profile/config | Selected profile/transport; lifecycle/resolver genişliği açık. |
| F06 tool/skill/plugin/MCP/authority | Worker/middleware ve ayrı A/SA/AP; Q26 full runtime açık. |
| F07 backend/native | İlk topoloji; execution/effect sınırları geniş araştırma bekliyor. |
| F08 delegation/cancel/worktree/writers | Selected cancel/worker; bütün shared-writer/delegation lifecycle açık. |
| F09 gateway/auth/session/delivery | Normal pending yolu derin; genel teslim ve platform varyantları açık. |
| F10 cron/proaktif/queue/restart | Curator bağı; scheduler/report/persistence köprüsü açık. |
| F11 CLI/TUI/apps/API/ACP | CLI/gateway pending seçkileri; diğer surface semantics açık. |
| F12 install/update/compat/eval | Probes var; genel dağıtım/eval/quality açıklaması açık. |

Ledger/backup/restore/sync → skill/cache → curator nested batch/report/cron hâlâ açıklama köprüleri; geniş kapsam haritasına göre sıralanır. U01'in bütün residual'ları kapanmadan başka ailelere bakılamaz gibi bir kapı yoktur.

## 5. Yeniden açma ve durma

Q26/Q29, full originals/bağımlılık erişimi, source değişimi veya load-bearing adoption/security kararıyla yeniden açılır. E01/E02 legacy verifier NOT RUN; D3 manuel AST ikame değil. M4 full-parent identity ve actual caller/request gap'i de gerekli güçlü hüküm için ayrıca kapanır. Aynı V/N/A/SA/AP/C testlerini çoğaltmak yeni coverage değildir.

Erişim hatasında exact açık halka kaydedilir; kaynağın yokluğu veya kalıcı tool kaybı varsayılmaz. Provider/credential/kurulum/upstream/control/Foundation sınırı genişletilmez. Sentezde source, execution, inference ve open edge ayrı tutulur. Bitiş ölçütü METHOD; bu v0.13 bütün HERMES kapanışı değildir.
