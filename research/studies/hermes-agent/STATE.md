# Hermes Agent — STATE

**2026-09-12 / U11 / plan v0.24 — RUNTIME, BACKEND AND CONTROL OWNERSHIP.**
**Statü:** ACTIVE PARTIAL RESEARCH; bütün HERMES tamamlanmadı. Q53'ün A/B bounded kaynak açıklaması ilerledi; gerçek runtime doğrulaması kapanmadı.
**Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release/kurulu binary değil.
**Güncel yayın authority:** [U11 PUBLICATION](evidence/2026-09-12-runtime-backend/PUBLICATION.md). Bu STATE'te birimin anlatılması, tek başına main/ref/content doğrulaması değildir.

## Amaç, yetki ve incremental kapılar

Kullanıcı önce anlamlı başlangıç kaydı→main geri okuma→küçük araştırma dilimi→yayın/geri okuma düzenini onayladı; “Tamam devam et lütfen” talebiyle uygulandı. Başlangıç main `595d9ebb24302e271b9f84cc86d0debbd74dc790` içindeki Foundation ve ayrı roadmap çalışması korundu. U10 zaten yayımlanmıştı; eski ZIP veya deneyler yeniden yapılmadı.

Q53 başlangıç STATE/PLAN kaydı `d3a4baeeb7afd97d38588c674c4842f01e87c6f0` olarak gerçek main/ref ve değişen metinlerden geri okundu. Sonra A araştırıldı. A, `e562de82ab4ea33872e55d501c8b59f26b441fa8` olarak main'e yazıldı; araştırma/kaynak tam metinleri ve güncel STATE bölümü geri okunduktan sonra B'ye geçildi. B'nin content/ref/scope makbuzu PUBLICATION'dadır. Native write işlemlerinin önceki turlarda neden değiştiğine dair teşhis yoktur.

Amaç önce HERMES-native mekanizmalar ve sistem ilişkileri; sonra çekirdek açıklama ve ayrı dört-alan/SOUL/Development OS aday değerlendirmesi. Yalnız `research/studies/hermes-agent/**` ve CATALOG Hermes satırı değişebilir. Foundation, context/Codex, agent-control, diğer studies, upstream kod, mimari/adoption, izin/ayarlar değişmez. Full ürün, model/provider/credential/NAS ve harici backend çalıştırması yok; otomatik/background devam yok.

**Yayın düzeni sürer:** anlamlı kaynak/kanıt/sınır/sonraki soru dilimi main'e kaydedilip doğrulanmadan ikinci büyük dilim biriktirilmez. Yazma kesilirse mevcut dilimin yayınını çöz. Küçük metin yayını binary kanıt veya gelecekteki bütün yazmaların garantisi değildir.

## U11 — gerçekten yapılan

[Note26](notes/26-RUNTIME-BACKEND-AND-CONTROL-OWNERSHIP.md) → [A: seçim/dispatch](evidence/2026-09-12-runtime-backend/RESEARCH.md) + [B: sahiplik](evidence/2026-09-12-runtime-backend/BACKEND-OWNERSHIP.md). [A kaynakları](evidence/2026-09-12-runtime-backend/SOURCES.md) ve [B kaynakları](evidence/2026-09-12-runtime-backend/BACKEND-SOURCES.md), S01–S16'nın gerçek full/selected kapsamını taşır.

Requested provider/model → lazy runtime resolver → init/client → ortak turn admission/context → ordinary loop veya whole-turn native Codex dalı bağlandı. `codex_responses` model transportu ile `codex_app_server` bütün-tur devri aynı değildir. Ortak facade içinde kabul korunurken model, history, tools, compaction, fallback ve cancel/cleanup sahipliği değişebilir.

Native factory/RPC yolu cwd ve güncel input'u taşır; HERMES'in ayrı model/system/history/tool alanlarını aynı RPC alanlarıyla iletmez. Native config veya input'taki başka bağlamın telafisi mümkündür; gerçek native modelin farklı olduğu gözlenmedi. Native thread'in authoritative geçmişi ile tamamlanmış olaylardan türetilen seçici HERMES aynası ayrıldı. Compaction native taraftadır; checkpoint-required birleşimi native girişte reddedilir.

Ordinary tool/executor/parent-agent bağı ile curated stateless Hermes MCP yüzeyi ayrıldı. Ordinary fallback etkin route/client/pool/compressor/prompt alanlarını yeniden bağlar; native error/retire/dönüş önerisi başka bir toparlama yoludur. Interrupt isteği, native terminal bildirimi, hard close ve fiziksel etkinin durması eşitlenmedi. Native deadline'da final text kabulü ile turn/completed ve projection flush ile agent_persisted/completed farklı makbuz sınırları olarak açıldı.

**Yeni behavioral execution: YOK.** SDK/model/native subprocess/network/SessionDB veya upstream test suite çalıştırılmadı. Kaynak control-flow çıkarımları actual data loss, wrong-model, duplicate veya ürün güvenilirliği hükmü değildir. RESULT/başarı sayısı üretilmedi. [NOT RUN](evidence/2026-09-12-runtime-backend/CHECKS-NOT-RUN.md) yapılmamış ayırıcı kontrolleri taşır.

## İlk sonraki geniş kaynak işi

**Q54 — ordinary tool/delegation kabulü → parent/child yetki ve bağlamı → sonuç dönüşü → cancel/cleanup sorumluluğu.** Başlangıç `run_agent.py::_execute_tool_calls/_dispatch_delegate_task`, gerçek tool executor/policy ve `tools/delegate_tool.py` çağıran zinciridir. En az ordinary parent-bound iş ile native stateless MCP yüzeyinin sınırı karşılaştırılır; bütün Codex plugin ekosistemi otomatik kapsam değildir.

Q53 bounded source açıklaması ilerledi; Q55 native model/system/history/restart binding ve Q56 terminal/persistence/control makbuzları residual doğrulamalardır. Primary restore, fallback geçiş ortası ve bütün profile/config varyantları tam kapanmadı. Full source/bağımlılık, yeni karşı kanıt veya güçlü reliability reuse gerektiğinde ilgili ölçümler yeniden açılır. Learning/skill-ledger/sync/quality ve diğer UI/install/update/eval aileleri kapsamdan düşmez.

Bu bir sonraki kaynak araştırmasıdır; mimari, canlı ürün veya araç yetkisi değiştirme aşamasına geçiş değildir. Geniş kaynak araştırmasının sürmesi, bütün fault matrisinin bitmesine bağlanmaz. Sonraki büyük dilim yalnız current yayın makbuzu doğrulandıktan sonra başlar.

## Korunan tamamlanmış araştırma ve açık sınırlar

U10 Q49 cron execution/context araştırması, native selector C01–C06 ve provisional synthesis04 kendi kayıtlarında korunur: [note25](notes/25-CRON-EXECUTION-AND-CONTEXT.md), [RESEARCH](evidence/2026-09-12-cron-execution-context/RESEARCH.md), [SOURCES](evidence/2026-09-12-cron-execution-context/SOURCES.md), [PUBLICATION](evidence/2026-09-12-cron-execution-context/PUBLICATION.md). İçerik d1b045a66b7a07d62d135c025bf5a1d4ab741022; makbuz b658913dd8148dd9a4850414159f13513904f137. U10 bekleyen yayın değildir.

U04-A/18 ile ayrı U04-B/19 aynı numaralarda aynı vakalar değildir. B'nin 33 original dosyalı subtree'si d01c92f7414713300934be3bb4e3d40ac57631b3 ve [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. U05–U09 ve daha eski kaynak/ham koşu/yayınlar, notes01–25, METHOD ve synthesis01–04 değiştirilmez. A'nın bu tur yayımlanan RESEARCH/SOURCES metni de B sırasında yeniden yazılmaz. Dört provisional sentez dört Foundation alanının tamamlandığı anlamına gelmez; note26 yeni final CORE değildir.

Q40 actual DB/quiet history, Q42 startup admission, Q47 late callback/NAS/clock, Q48/Q50 transport/status/cancel, Q41/Q43/Q44/Q45 ve Q07/Q22/Q26/Q29/Q38 fidelity/quality; U10 Q49 full run_job, Q51 context→request/quality ve Q52 detection→handling açık kalır. Eski G/H/L/D/B/C vaka sayıları birleştirilmez; U11 kaynak okuması onları yeniden test etmedi.

## Cold-start ve retrieval

1. Current main AGENT/tetiklenen protokoller → research root/studies catalog → META/STATE/INDEX → METHOD/PLAN. U11 PUBLICATION üstü güncel ref/content hükmüdür. Başlangıç ve A checkpoint'leri tamamlanmış kapılardır; tarihsel prepared ifadeleri güncel engel sayma.
2. Note26 + A RESEARCH/SOURCES + B BACKEND-OWNERSHIP/BACKEND-SOURCES + NOT RUN tam okunur. U11'de runtime RESULT veya test arşivi yoktur. Tam dosya okuması, full dependency closure veya execution değildir.
3. Synthesis02 ordinary-loop ve synthesis04 scheduled-work ile birlikte karşı oku. U10 note25 + SOURCES/RESEARCH/NOT RUN yolu korunur; exact C iddiası için SPEC + tam RESULT + MANIFEST + raw source/probe/input/output/log/attempt-00 gerekir.
4. U04 zorunlu ayrımı: note19 + B README/RECONCILIATION/manifest; synthesis03 + A SOURCES/RESEARCH/CONTINUITY-COVERAGE. Genel turn/memory için synthesis01/02 ve U05/U06/U07 kanıt rotaları gerekli derinlikte izlenir. Aynı-conversation full reads yeni bağımsız kanıt değildir.
5. [Exact U10 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/b658913dd8148dd9a4850414159f13513904f137/research/studies/hermes-agent/STATE.md), [başlangıç STATE](https://github.com/batuhanozgun/agentic-os-search/blob/d3a4baeeb7afd97d38588c674c4842f01e87c6f0/research/studies/hermes-agent/STATE.md), [A STATE](https://github.com/batuhanozgun/agentic-os-search/blob/e562de82ab4ea33872e55d501c8b59f26b441fa8/research/studies/hermes-agent/STATE.md) tarihsel kimlik ve yetki ayrımlarını korur. MAP/catalog derived yüzeylerdir, raw kanıtın veya bu STATE'in yerine geçmez.
