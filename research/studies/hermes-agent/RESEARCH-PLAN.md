# Hermes Agent — Araştırma planı

**Plan v0.5 — 2026-09-08.** Aktif dış hedef araştırması; kanıta göre değişebilir decomposition. Güncel iş otoritesi [STATE](STATE.md).

## 1. Döngü ve kapsam

`kaynak keşfi → mekanizma sorusu → alt kaynakları tam okuma → karşı yol/test → not → kapsam revizyonu → sonraki birim`.

Üst sentez yalnız alt notların kısaltılması değildir; açıklanmamış geçişleri arar ve kaynağa geri döner. HERMES'i kendi davranış ailelerinden anlamak, ardından dört-alan ve SOUL/Development OS değerlendirmesi üretmek amaçtır. Hata listesi, kurulum, upstream onarımı veya benimseme bu araştırmanın yerine geçmez.

## 2. Aşamalar

| Aşama | Durum |
|---|---|
| A0 Kimlik, pin, proje sınırı | c4a5de... immutable pin / 0.21.0 manifest; d8a077... ve üç dosyalık 7874ef... gözlemleri kapsamlarıyla ayrıldı. |
| A1 Kaynak topolojisi | Kök/apps listeleri var; recursive alt envanter ve giriş yolları haritası sürüyor. |
| B0 Mekanizma sondajları | U01 review, U01-C curator ve U01B onay/mutasyon kesitleri; iki exact modül üzerinde 10 sentetik tanılayıcı gözlem. Aile kapanmadı. |
| U01-DOC Ek kontrat incelemesi | Sekiz resmî web belge yüzeyinde seçili bölümler incelendi. Pin ile eşleştirilmedi; kod okuması veya yeni deney değildir. [05 notu](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md). |
| B1–Bn Genişletme | F01–F12 aşağıda; sabit modül sayısı iddiası değil. |
| C Native alt-sistem sentezleri | Henüz yok. |
| D İlişkiler ve karşı-yol incelemesi | Yerel aday bağlantılar var; genel sentez yok. |
| E Dört-alan / SOUL / DevOS | Native model yeterli olduktan sonra; henüz yok. |
| F Çekirdek / omission-distortion / freshness | Henüz yok; METHOD bitiş ölçütleri geçerli. |

## 3. Provisional kaynak aileleri — korunan geniş kapsam

| ID | Soru / aile | Başlangıç rotası | Mevcut derinlik |
|---|---|---|---|
| F01 | Başlama, araç döngüsü, retry, kesinti, sonlanma | run_agent.py; agent/conversation_loop.py; turn_*.py | Harita/kontrat; gerçek caller/dispatch kapanışı sırada. |
| F02 | Prompt, context dosyası, schema, compression/cache | prompt_builder; context-engine/compressor; prompt-caching | Rehberler + review fork; değişiklik sonrası invalidation callsite. Genel yaşam döngüsü açık. |
| F03 | Session kimliği, lineage, arama, kullanım/onarım | hermes_state*.py; gateway/session.py; session-search | Doküman; README–rehber farkı açık. Skill usage ayrı kayıt. |
| F04 | Bellek/beceri oluşturma, sahiplik, onay, geri alma/paylaşım | memory/skills; background_review; curator; ledger/sync | U01/U01-C/U01B; mutator/batch/approval kaynakları tam. Caller, memory, ledger/sync/reuse/kalite kapanmadı. |
| F05 | Provider/model/credential/profile/config bağlama | runtime_provider; auth/config/profile; providers | Manifest + review/curator seçimi; genel resolver açık. |
| F06 | Tool/skill/plugin/MCP keşfi ve gerçek çağrı yetkisi | model_tools.py; toolsets; registry; plugin pre-tool gates | Whitelist/guard, skill schema/registry/batch/apply; gerçek invoke ve bağlam aktarımı açık. |
| F07 | Backend/native katmanların sınırlandırdığı etki | tools/environments; terminal/file/code/MCP; native; Docker/OpenShell | Güvenlik kontratı/root harita; izolasyon doğrulanmadı. |
| F08 | Delegation/process/cancellation/worktree/yazıcılar | delegate_tool; process registry; fork/profile context | Review/curator dar yolları; genel delegasyon/eşzamanlılık açık. |
| F09 | Gateway yetkilendirme, session, teslim | gateway/run*; registry/platforms; delivery/pairing | Mimari/güvenlik kontratı; adapter eşdeğerliği varsayılmadı. |
| F10 | Cron/proaktif iş, kuyruk, tekrar/kayıp | cron; review_idle_queue; scheduler/delivery | Curator cron-reference callsite; gerçek scheduler/restart açık. |
| F11 | CLI/TUI/desktop/web/API/ACP temsil/yetki eşdeğerliği | apps/web/ui-tui/tui_gateway/acp_adapter; CLI | Ortak approval preview/komut kesiti + bileşen karşı örnekleri; her UI'ye genellenmedi. |
| F12 | Install/update/compat, test/eval/telemetri/trajectory | pyproject/locks; .github; scripts/evals; batch/trajectory | Seçili manifest, test kaynağı, curation kayıtları ve dar bileşen deneyi. Release/CI/gelecek-task quality açık. |

Başlangıç rotası dosyanın okunduğunu göstermez. Bir mekanizma birden çok aileye bağlanır; family etiketleri ürün modülleri değildir.

## 4. Birimler ve sıradaki iş

**U01:** Deneyimden kalıcı belleğe/beceriye geçiş. [02 notu](notes/02-BACKGROUND-LEARNING.md). Trigger/caller, dispatch, memory-store, replay, ledger ve sonraki kullanım açık.

**U01-C (kimliği korunur):** Oluşmuş beceri kütüphanesinin bakımı. [03 notu](notes/03-SKILL-CURATION.md). Policy/authorship, deterministic maintenance/LLM consolidation, report/cron ve recovery ayrımları. Önceki tur H22 orta aralığına 429 nedeniyle erişemedi; U01B bu dosyanın tam okumasını sonradan kalıcı kayda getirdi. Eski eksik aralık current sonraki iş değildir.

**U01B:** Onay, mutasyon ve geri alma. [04 notu](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [S01–S06](evidence/2026-09-07-u01b/SOURCES.md). Üç ayrı soru: onaylanan nesne/temsil; hata/istisna/restore yolları; dosya dışındaki iz/cache/sync etkileri. Bileşen kanıtı aile veya ürün kapanışı sayılmaz.

**İlk sonraki kaynak işi:** Gerçek review/foreground/curator caller → invoke/dispatch → exception handling → pending apply bağını izle. Origin/profile/authority aktarımı ve U01-C raporunun batch operations yorumunu aç. S01/S02 tam okuma mevcut; kaynakları gerekince iddiaya bağlı tekrar aç, eski state yüzünden gereksiz yeni-ilk-okuma yapma. Ardından memory mutator, cancellation/store, ledger/backup/restore/sync ve sonraki skill/cache-load.

**U02:** Çekirdek iş/bağlam yaşam döngüsü (F01/F02/F03); U01'in ihtiyaç duyduğu dar alt yollar şimdi açılabilir, genel çekirdek sentezi ayrıdır.

**U03:** Genişleyen yetki ve etki (F05/F06/F07/F08); callback/whitelist, namespace, OS sınırı ve credentials tek güvence değildir.

**U04 ve devamı:** Gateway/cron/UI/install/eval ve kalan varyantlar. U01 ayrıntıları bütün sistemi yutmamalı; kaynak bağımlılığına göre sıra değişebilir. Sistem dışı yeni araştırma nesnesi ayrı gerekçe/yetki ister.

## 4A. Bu turun erişim sınırı ve ek kontrat katmanı

2026-09-08'de primary pin'deki `run_agent.py` 1–190 isteği iki kez 429 / `too-many-processes` ile içerik getirmedi. Bu giriş dosyası veya caller zinciri okunmuş sayılmadı. [Erişim/okuma kaydı](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) gerçek gözlemi taşır; bu bir kalıcı erişim yokluğu veya ürün kusuru değildir.

Bu nedenle aynı araştırma nesnesinin resmî belgeleriyle **U01-DOC** ek birimi yapıldı. W01–W08; registry/special-tool dispatch, observer/enforcement ayrımı, profile namespace, memory görünürlüğü, session temsilleri ve compression sınırları için kontrat ve rakip açıklama sağladı. Web belgelerinin ortak commit'i bilinmiyor. Primary pin değişmedi; belgeler U01B'nin gerçek caller karşılığını doğrulamadı.

[05 notunun §9'undaki K01–K09](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) gelecek kaynak/deney çalışmasının ayırıcı kontrolleridir: special/genel dispatch kapsamı; exception temsili ve telafi; context aktarımı; onay talebi/teslim/karar/etki; disk/store/prompt görünürlüğü; turn/teardown; kaynak/arşiv/replay görünümü; özet hatası; curator batch raporu. **Dokuzu da PLANNED / NOT RUN.** Yeni HERMES koşusu veya bağımsız test yoktur.

Sonraki çalışma ilk olarak §4'teki gerçek caller zincirine döner. Belgelerdeki semboller yalnız navigation ipucudur; kodun current/pinned konumu doğrulanmalıdır. Yeni bir kaynak revizyonu kullanılacaksa primary ile ilgili bağımlılık farkları ayrılmadan mevcut deneyle birleştirilmez. Okuma yeniden mümkün olmadığında kod-aile kapanışı verilmez; erişim durumu açık tutulur. F01–F12 kapsamı ve önce native model, sonra projeksiyon sırası değişmez.

## 5. Karşı sınama yüzeyi

- Aynı/farklı model review'unda kanıt görünümü eşdeğer mi?
- Read/preview/approve/write aynı hedef sürümünü mü bağlar; fuzzy patch ve rewrite varyantları neyi değiştirir?
- Normal hata, fırlatılan istisna, restore hatası ve pending disk hatası gerçek caller'da nasıl temsil edilir?
- Dosya geri alınırken ledger/cache/sahiplik/sync hangi durumu korur?
- Origin/profil etiketi ile öneren/onaylayan/uygulayanın yetkisi nasıl ayrılır?
- Cancellation sonrası eski worker ve paylaşılan store nasıl düzenlenir?
- İşin oluşturulması/yürütülmesi/teslimi/sonraki kullanım aynı kayıt mı?
- Curator raporu isim/beyan mı yoksa içerik koruması mı ölçer; batch schema/report ve cron referansı ilişkisi nedir?
- Usage/update sayısı yerine sonraki görevde kalite artışı hangi kanıtla kurulabilir?
- Dışarıda kalan UI/native/compat ailesi yeni birinci-derece mekanizma getiriyor mu?

Bunların hepsi doğrulanmış kusur değildir. Bileşen gözlemi, statik çıkarım ve ürün düzeyinde açık soru ayrı tutulur.

## 6. Revizyon geçmişi

| Revizyon | Kaynak / değişim | Etki |
|---|---|---|
| v0.1 | Gstack yöntem + HERMES root/architecture | Sabit ref, doğal mekanizma birimi, geç Foundation projeksiyonu; Gstack aileleri kopyalanmadı. |
| v0.2 | H04–H10/H13, apps | Öğrenme; transcript/store/ownership/approval/quality/share ayrımlarına açıldı. |
| v0.3 | H16–H20/H05/H22, ref uzlaştırması | U01-C curator; policy≠authorship, usage≠quality, archive≠complete rollback, report→cron ilişkisi. |
| v0.4 | Sohbet U01B paketinin kaynak/deney kaydı ve güncel v0.3 ile birleştirilmesi | H22 tam okuması recover edildi; approval representation, exception rollback ve pending durability karşı örnekleri taşındı. Caller/context ilk sıraya alındı. U01-C'nin kimliği ve F01–F12 kapsamı korundu; eski yerel v0.3 önerisi current'ın üstüne yazılmadı. |
| v0.5 | 2026-09-08 upstream caller isteğinde iki 429; W01–W08 resmî belge kontratları | Ek U01-DOC katmanı ve dokuz çalıştırılmamış ayırıcı kontrol; gerçek caller ilk sırada kaldı. H/S kanıtının kapsamı, primary pin ve geniş aileler korunur; yeni kod okuması/deney iddiası yok. |

V0.3 ayrıntıları Git geçmişinde `000f691b9a94607c9a8219961b4618eda0f1014f` ref'indeki bu dosyadan recover edilebilir. Bu kayıtların birleştirilmesi yeni deney, bağımsız doğrulama veya çalışma yöntemi için agent-control değişikliği değildir.
