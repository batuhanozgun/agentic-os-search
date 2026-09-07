# Hermes Agent — Araştırma planı

**Plan v0.2 — 2026-09-07.** Aktif dış hedef araştırması; değişebilir decomposition. Güncel iş otoritesi [STATE](STATE.md).

## 1. Döngü

`kaynak keşfi → sınırlandırılmış mekanizma sorusu → alt kaynakları tam okuma → karşı yol/test → not → kapsam revizyonu → sonraki birim`.

Üst sentez, alt notların yalnız kısaltılması değildir; aralarındaki açıklanmamış geçişleri arar ve gerekirse kaynağa geri açılır. Bir öğrenme modülünden bütün ürün hakkında erken sonuca gidilmez.

## 2. Aşama ve ilk durum

| Aşama | Durum / teslim |
|---|---|
| A0 Kimlik, pin, mevcut proje sınırı | Kaydedildi; upstream 0.21.0 manifesti ve immutable commit tanımlı. |
| A1 Kaynak topolojisi | Kök ve apps listeleri tamam; recursive alt envanter ve execution-path haritası sürüyor. |
| B0 İlk mekanizma sondajı | U01'in review/koruma/onay/test bölümü okundu; uçtan uca aile henüz kapanmadı. |
| B1–Bn Mekanizma genişletme | Aşağıdaki aileler provisional; kanıt geldikçe bölünebilir. |
| C Native alt-sistem sentezleri | Başlatılmadı. |
| D İlişkiler ve karşı-yol incelemesi | Başlatılmadı; soruları ilk notlardan birikiyor. |
| E Dört-alan projeksiyonu ve SOUL/DevOS değerlendirmesi | Native modelden sonra; henüz yok. |
| F Çekirdek sentez, omission/distortion, freshness kapanışı | Henüz yok; METHOD ölçütleri uygulanacak. |

## 3. Provisional kaynak aileleri

Bu liste on iki kesin modül iddiası değildir. Bir satır birden fazla mekanizma içerir, bir mekanizma birden fazla satıra bağlanabilir.

| ID | Soru / doğal kaynak ailesi | Başlangıç rotası | Mevcut derinlik |
|---|---|---|---|
| F01 | Konuşma/iş nasıl başlar, araç döngüsü, retry, kesinti ve sonlanma nasıl yönetilir? | `run_agent.py`, `agent/conversation_loop.py`, `agent/turn_*.py` | Harita/doküman; implementation closure yok. |
| F02 | Prompt, context dosyası, araç tanımı, compression ve cache hangi bilgiyi taşır/kaybeder? | `agent/prompt_builder.py`, context-engine/compressor, prompt-caching, system-prompt yolları | Mimari rehber + review fork'a ait kod. |
| F03 | Oturum kimliği, lineage, arama, kullanım kaydı ve onarım hangi durumu korur? | `hermes_state.py`, `hermes_state_*.py`, `gateway/session.py`, session-search tool | Doküman; README–rehber çelişkisi açık. |
| F04 | Bellek/beceri nasıl oluşur, değişir, sahiplenilir, onaylanır, geri alınır ve paylaşılır? | memory/skills, `agent/background_review.py`, curator, skill ledger/sync | İlk kısmi mekanizma notu; caller/replay/reuse ve curator/sync açık. |
| F05 | Provider, model, credential, profile ve config seçimi çalışmayı nasıl bağlar? | `hermes_cli/runtime_provider.py`, auth/config/profile, `providers/` | Manifest ve review runtime seçimi; genel çözümleme okunmadı. |
| F06 | Araç/skill/plugin/MCP keşfi ile gerçek çağrı yetkisi nasıl ayrılır? | `model_tools.py`, `toolsets.py`, registry, plugin/pre-tool gates | Review whitelist kurulumu + seçili test; genel dispatch henüz yok. |
| F07 | Ortam/backends/native katmanlar hangi etkiyi gerçekten sınırlar? | `tools/environments/`, terminal/file/code/MCP, `native/`, Docker/OpenShell bağlantıları | Güvenlik kontratı ve root envanter; izolasyon doğrulanmadı. |
| F08 | Delegation, process, cancellation, worktree ve eşzamanlı yazıcılar nasıl yönetilir? | `tools/delegate_tool.py`, process registry, review worker, profile context | Review worker dar yolu; genel delegasyon henüz yok. |
| F09 | Gateway mesajı nasıl yetkilendirilir, oturuma bağlanır ve sonuç teslim edilir? | `gateway/run*.py`, platform registry, `plugins/platforms/`, delivery/pairing | Mimari/güvenlik belgeleri; adapter eşdeğerliği kabul edilmedi. |
| F10 | Cron/proaktif işler, kuyruk ve tekrarlar hangi durumda çalışır veya kaybolur? | `cron/`, `agent/review_idle_queue.py`, scheduler/delivery state | Doküman; trigger/liveness/restart incelemesi açık. |
| F11 | CLI/TUI/desktop/web/API/ACP aynı iş ve onay anlamını koruyor mu? | `apps/`, `web/`, `ui-tui/`, `tui_gateway/`, `acp_adapter/`, CLI | Apps listesi + ortak onay komutları; yüzeyler ayrı korunuyor. |
| F12 | Kurulum/güncelleme/compat, test/eval/telemetri ve trajectory üretimi değişimi nasıl yönetir? | pyproject/locks, `.github/`, scripts, `evals/`, batch/trajectory, compat manifest | Seçili manifest ve test kaynakları; release/CI/runtime henüz yok. |

Başlangıç rotalarından henüz getirilmeyen yollar keşif hedefidir. İlk kök haritasından veya belgelerin verdiği isimlerden türemiş olmaları dosyanın içeriğini doğrulamaz.

## 4. Sıradaki çalışma birimleri

**U01 — deneyimden kalıcı belleğe/beceriye geçiş.** İlk not [02-BACKGROUND-LEARNING](notes/02-BACKGROUND-LEARNING.md). Devam: trigger/caller → gerçek dispatch → memory/skill mutator → pending replay → ledger/geri alma → sonraki session/skill load. Her aşamadaki kritik karar/yan etki için test veya açık boşluk.

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
- Çekirdek modelin dışında bırakılan desktop/web/native/compat bölgesi aslında birinci-derece mekanizma taşıyor mu?

Bunlar doğrulanmış arıza listesi değil, araştırmanın kendi doğrulama yüzeyidir.

## 6. Revizyon geçmişi

| Revizyon | Kaynakla ortaya çıkan değişiklik | Plan etkisi |
|---|---|---|
| v0.1 | Gstack'in semantic-pyramid yöntemi ve HERMES root/architecture | Sabit ref, doğal mekanizma birimi, geç aşama Foundation projeksiyonu. Gstack'in 11 ailesi kopyalanmadı. |
| v0.2 | H04 review fork; H05 origin/ownership; H07/H08 approval; H09/H10 testlerin gerçek kapsamı; H13 security; T01 apps | 'Öğrenme' tek kutu olmaktan çıkarıldı. Transcript izolasyonu, kalıcı store, sahiplik, onay, kalite ve paylaşım ayrı sorular oldu. UI/native/terminal-whole-process ayrımları kapsamda bağımsız tutuldu. |

Sonraki değişiklik bu tablodan önce bulguya dayanmalıdır; plan sırf eski biçimi korumak için dondurulmaz.
