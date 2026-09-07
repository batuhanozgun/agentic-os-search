# Hermes Agent — Araştırma planı

**Plan v0.3 — 2026-09-07.** Aktif dış hedef araştırması; değişebilir decomposition. Güncel iş otoritesi [STATE](STATE.md).

## 1. Döngü

`kaynak keşfi → sınırlandırılmış mekanizma sorusu → alt kaynakları tam okuma → karşı yol/test → not → kapsam revizyonu → sonraki birim`.

Üst sentez, alt notların yalnız kısaltılması değildir; aralarındaki açıklanmamış geçişleri arar ve gerekirse kaynağa geri açılır. Bir öğrenme modülünden bütün ürün hakkında erken sonuca gidilmez.

## 2. Aşama ve ilk durum

| Aşama | Durum / teslim |
|---|---|
| A0 Kimlik, pin, mevcut proje sınırı | Kaydedildi; upstream 0.21.0 manifesti ve immutable commit tanımlı. d8a077... ek okuma ref'i aynı ilgili blob'larla uzlaştırıldı; primary pin değişmedi. |
| A1 Kaynak topolojisi | Kök ve apps listeleri tamam; recursive alt envanter ve execution-path haritası sürüyor. |
| B0 İlk mekanizma sondajları | U01 review/koruma/onay/test kesiti + U01-C curator/usage/rapor kesiti kaydedildi. Uçtan uca öğrenme ailesi kapanmadı. |
| B1–Bn Mekanizma genişletme | Aşağıdaki aileler provisional; kanıt geldikçe bölünebilir. |
| C Native alt-sistem sentezleri | Başlatılmadı. |
| D İlişkiler ve karşı-yol incelemesi | Genel sentez başlatılmadı; yerel sorular notlardan birikiyor. |
| E Dört-alan projeksiyonu ve SOUL/DevOS değerlendirmesi | Native modelden sonra; henüz yok. |
| F Çekirdek sentez, omission/distortion, freshness kapanışı | Henüz yok; METHOD ölçütleri uygulanacak. |

## 3. Provisional kaynak aileleri

Bu liste on iki kesin modül iddiası değildir. Bir satır birden fazla mekanizma içerir, bir mekanizma birden fazla satıra bağlanabilir.

| ID | Soru / doğal kaynak ailesi | Başlangıç rotası | Mevcut derinlik |
|---|---|---|---|
| F01 | Konuşma/iş nasıl başlar, araç döngüsü, retry, kesinti ve sonlanma nasıl yönetilir? | `run_agent.py`, `agent/conversation_loop.py`, `agent/turn_*.py` | Harita/doküman; implementation closure yok. |
| F02 | Prompt, context dosyası, araç tanımı, compression ve cache hangi bilgiyi taşır/kaybeder? | `agent/prompt_builder.py`, context-engine/compressor, prompt-caching, system-prompt yolları | Mimari/geliştirici rehberleri + review fork'a ait kod; genel context lifecycle açık. |
| F03 | Oturum kimliği, lineage, arama, kullanım kaydı ve onarım hangi durumu korur? | `hermes_state.py`, `hermes_state_*.py`, `gateway/session.py`, session-search tool | Doküman; README–rehber çelişkisi açık. Skill kullanım kaydı session-storage'ın yerine geçmez. |
| F04 | Bellek/beceri nasıl oluşur, değişir, sahiplenilir, onaylanır, geri alınır ve paylaşılır? | memory/skills, `agent/background_review.py`, curator, skill ledger/sync | İki kısmi not. Curator/skill_usage tam; mutator seçili; caller/replay/reuse/ledger/sync kapanmadı. |
| F05 | Provider, model, credential, profile ve config seçimi çalışmayı nasıl bağlar? | `hermes_cli/runtime_provider.py`, auth/config/profile, `providers/` | Manifest ve review/curator runtime seçimi; genel çözümleme okunmadı. |
| F06 | Araç/skill/plugin/MCP keşfi ile gerçek çağrı yetkisi nasıl ayrılır? | `model_tools.py`, `toolsets.py`, registry, plugin/pre-tool gates | Review whitelist/guard ve seçili test; skill_manage registry/schema kesiti. Gerçek single-op/batch/dispatch closure açık. |
| F07 | Ortam/backends/native katmanlar hangi etkiyi gerçekten sınırlar? | `tools/environments/`, terminal/file/code/MCP, `native/`, Docker/OpenShell bağlantıları | Güvenlik kontratı ve root envanter; izolasyon doğrulanmadı. |
| F08 | Delegation, process, cancellation, worktree ve eşzamanlı yazıcılar nasıl yönetilir? | `tools/delegate_tool.py`, process registry, review worker, profile context | Review/curator fork dar yolları; genel delegasyon ve etkili izolasyon henüz yok. |
| F09 | Gateway mesajı nasıl yetkilendirilir, oturuma bağlanır ve sonuç teslim edilir? | `gateway/run*.py`, platform registry, `plugins/platforms/`, delivery/pairing | Mimari/güvenlik belgeleri; adapter eşdeğerliği kabul edilmedi. |
| F10 | Cron/proaktif işler, kuyruk ve tekrarlar hangi durumda çalışır veya kaybolur? | `cron/`, `agent/review_idle_queue.py`, scheduler/delivery state | Curator'ın cron-reference koruma/rewrite çağrıları ve seçili testler; gerçek scheduler/restart açık. |
| F11 | CLI/TUI/desktop/web/API/ACP aynı iş ve onay anlamını koruyor mu? | `apps/`, `web/`, `ui-tui/`, `tui_gateway/`, `acp_adapter/`, CLI | Apps listesi, package workspaces ve ortak onay komutları; yüzeyler ayrı korunuyor. |
| F12 | Kurulum/güncelleme/compat, test/eval/telemetri ve trajectory üretimi değişimi nasıl yönetir? | pyproject/locks, `.github/`, scripts, `evals/`, batch/trajectory, compat manifest | Manifest/testler + skill telemetry/reporting/backup callsite; release/CI/quality eval/runtime henüz yok. |

Başlangıç rotalarından henüz getirilmeyen yollar keşif hedefidir. İlk kök haritasından veya belgelerin verdiği isimlerden türemiş olmaları dosyanın içeriğini doğrulamaz.

## 4. Sıradaki çalışma birimleri

**U01 — deneyimden kalıcı belleğe/beceriye geçiş.** İlk not [02-BACKGROUND-LEARNING](notes/02-BACKGROUND-LEARNING.md). Devam: trigger/caller → gerçek dispatch → memory/skill mutator → pending replay → ledger/geri alma → sonraki session/skill load. Her aşamadaki kritik karar/yan etki için test veya açık boşluk.

**U01-C — oluşmuş beceri kütüphanesinin bakımı.** [03-SKILL-CURATION](notes/03-SKILL-CURATION.md) otomatik yaşam döngüsü, yönetim politikası, opt-in LLM consolidation, rapor ve cron bağlantısını ayırdı. Bu, U01'in yerine geçen yeni ana araştırma değil, kaynakta ortaya çıkan bağlantılı birimdir. İlk sonraki okuma H22 `tools/skill_manager_tool.py` 201–800; ardından batch/dispatch/apply. Prompt/guard farkı ve schema/report ilişkisi bu yoldan sınanacak. Son istekte 429 geldiği için eksik aralık açık kaydedildi; test veya çalışma başarısızlığı sanılmayacak.

**U02 — çekirdek iş ve bağlam yaşam döngüsü.** F01/F02/F03 bağlantısı; farklı girişlerin ortak çekirdeğe ne taşıdığı. U01'i anlamak için gereken alt yol şimdi açılabilir; bütün çekirdek sentezi ayrı teslimdir.

**U03 — genişleyen yetki ve etki sınırı.** F05/F06/F07/F08; callback/whitelist, namespace, OS sınırı ve credential/external effect aynı güvence değildir. README'deki 'isolated subagents' ifadesi bütün bu alanlar için sonuç sayılmayacak.

**U04 ve devamı — haritadaki kalan aileler ve varyantlar.** Gateway/cron/UI/install/eval bölgeleri U01'e ilginçlik nedeniyle tabi kılınmaz. Kaynak ağında ortaya çıkan bağımlılığa göre sıra değiştirilir; hedef dışı ecosystem araştırması ayrı gerekçe ister.

## 5. Önceden seçilen karşı sorular

- Başka model daha bağımsız review mü sağlıyor, yoksa farklı ve eksik transcript ile farklı bir işi mi yapıyor?
- Read-before-write kaydı exact içeriğe mi, path'e mi bağlı; okuma/approve/yazma arasında hedef değişirse ne olur?
- Varsayılan izin ve config hatası aynı sonucu mu üretir; verilen onay ile gerçekten kalıcı pending record eşleşir mi?
- Yeni kullanıcı mesajı review'u keserken eski worker ve paylaşılan store ne olur?
- Session/profile ayırımı caller yetkisi veya dosya/process izolasyonuyla karıştırılıyor mu?
- Zamanlanmış işin üretildiği, yürütüldüğü, teslim edildiği ve sonraki oturumda kullanıldığı durumlar ayrı mı?
- Bir beceri güncellemesini 'başarılı öğrenme' sayan bağımsız sonuç ölçütü var mı; bulunmazsa arama kapsamı bunu söylemeye yeterli mi?
- Curator'ın raporu gerçek içeriği korumayı mı, isim/araç beyanlarını mı doğruluyor? Raporlama arızası cron referansını da etkiliyor mu?
- Otomatik arşivleme ile background skill_manage aynı ownership/dry-run/approval sözleşmesini mi uygular?
- Çekirdek modelin dışında bırakılan desktop/web/native/compat bölgesi aslında birinci-derece mekanizma taşıyor mu?

Bunlar doğrulanmış arıza listesi değil, araştırmanın kendi doğrulama yüzeyidir.

## 6. Revizyon geçmişi

| Revizyon | Kaynakla ortaya çıkan değişiklik | Plan etkisi |
|---|---|---|
| v0.1 | Gstack'in semantic-pyramid yöntemi ve HERMES root/architecture | Sabit ref, doğal mekanizma birimi, geç aşama Foundation projeksiyonu. Gstack'in 11 ailesi kopyalanmadı. |
| v0.2 | H04 review fork; H05 origin/ownership; H07/H08 approval; H09/H10 testlerin gerçek kapsamı; H13 security; T01 apps | 'Öğrenme' tek kutu olmaktan çıkarıldı. Transcript izolasyonu, kalıcı store, sahiplik, onay, kalite ve paylaşım ayrı sorular oldu. UI/native/terminal-whole-process ayrımları kapsamda bağımsız tutuldu. |
| v0.3 | H16–H20 curator/docs/usage/test karşı okuması; H05 yeniden okuma; H22 seçili mutator/schema; kaynak-ref uzlaştırması | Beceri üretimi ve kütüphane bakımı ayrı birimler olarak bağlandı. Policy≠authorship, usage≠quality, archive≠complete rollback ve report→cron etkisi ortaya çıktı. U01-C erken açıldı; dispatcher/batch/apply boşluğu sıradaki somut kaynağa dönüştü. Primary pin ve diğer çalışma hatları korunur. |

Sonraki değişiklik bu tablodan önce bulguya dayanmalıdır; plan sırf eski biçimi korumak için dondurulmaz. Curator prompt'undaki nicelik baskısı araştırmamızın kapanış ölçütüne aktarılmaz.
