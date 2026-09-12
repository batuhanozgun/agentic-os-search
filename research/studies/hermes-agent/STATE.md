# Hermes Agent — STATE

**2026-09-12 / U11-A, Q53 incremental source araştırması.** Son bütünü yayımlanmış önceki birim U10 / plan v0.23; yeni Q53'ün yalnız A kaynak dilimi hazırlanmıştır. Gerçek yayın commit/ref geri okuması yapılmadan bu başlık publication proof sayılmaz. [A araştırması](evidence/2026-09-12-runtime-backend/RESEARCH.md) / [kaynaklar](evidence/2026-09-12-runtime-backend/SOURCES.md).

**Statü:** ACTIVE PARTIAL RESEARCH; bütün HERMES ve Q53 tamamlanmadı. Primary `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release/kurulu binary değil. [PLAN](RESEARCH-PLAN.md), [METHOD](METHOD.md), [INDEX](INDEX.md), [META](META.md). U10 ağırlıklı derived girişler tam U11 checkpoint'inde güncellenecek; o sırada current work için bu STATE üst bölümü otoritedir.

## Güncel yetki ve tamamlanan ilk kapı

Kullanıcı küçük, repo ile eşzamanlı araştırma dilimlerini ve “Tamam devam et lütfen” ile uygulamayı onayladı. Başlangıç kaydı `d3a4baeeb7afd97d38588c674c4842f01e87c6f0` olarak main/ref ve STATE/PLAN değişen içerikleri üzerinden geri okundu. Yalnız iki HERMES dosyası değişti. Sonra Q53-A kaynak araştırmasına geçildi. Başlangıç tabanı `595d9ebb24302e271b9f84cc86d0debbd74dc790` içindeki Foundation ve ayrı roadmap çalışması korunur.

Amaç önce HERMES-native mekanizmalar ve sistem ilişkileri; sonra çekirdek model ve ayrı dört-alan/SOUL/Development OS değerlendirmesi. Yalnız `research/studies/hermes-agent/**` ve CATALOG Hermes satırı. Foundation, context/Codex, agent-control, diğer studies, upstream kod, mimari/adoption ve izin/ayarlar değişmez. Full ürün/model/provider/credential/NAS ve harici backend çalıştırması yok; otomatik/background devam yok.

**Yayın düzeni:** A main'e kaydedilip ref/content/scope geri okunmadan B büyütülmez. Yazma kesilirse yalnız mevcut dilimin yayınını çöz; ikinci büyük araştırma biriktirme. Küçük metin yazısı binary kanıt veya sonraki write kabiliyetinin garantisi değildir.

## U11-A — ne gerçekten ilerledi?

Requested model/provider → lazy runtime resolver → api_mode/endpoint/credential-source → AIAgent routing/client/init → ortak turn admission/context → ordinary loop veya Codex whole-turn devri kaynakla bağlandı. Aynı model/provider/client nesnesi actual execution sahibiyle eşit değildir.

Pool-path app-server opt-in helper'ı ve explicit/singleton OAuth return yolları ayrı görüldü; tüm user paths için aynı opt-in sonucu varsayılmadı. Normal loop'taki request/preflight/tool/finalizer hattı ile codex_app_server erken dönüşü ayrıldı. Native dalın kendi kontrol ve cleanup'ı henüz açılmadığından “bütün korumalar atlanıyor” sonucu çıkarılmadı. Dış facade admission/lease/finally yolu iki dalı da sarar.

**Yeni execution: YOK.** A selected source gözlemi ve source-linked inference'dır; gerçek SDK, credential, model, process, SessionDB veya hata senaryosu koşulmadı. Bütün resolver alt ağacı ve bütün phase helper'ları okunmadı. Kaynak kapsamları SOURCES'tadır. Aktarımı doğrulamak yeni davranış deneyi değildir.

## İlk sonraki iş

**A'nın yayın/geri okumasından sonra Q53-B:** `agent/codex_runtime.py` ve native session/client/projector; doğrudan model transportu ile history/compaction, tools, fallback, interruption ve cleanup sahipliğini karşılaştır. Normal kontrolün native karşılığı bulunmadan absence iddiası üretme. B bu checkpoint'te yapılmış değildir. Tam dependency ve güvenli önceden ölçütlenmiş diagnostic imkânı yoksa source-only sınırını koru.

Q53 sonrası delegation/tool-policy ve kalan geniş ailelerin sırası kanıta göre değerlendirilir. Learning/skill-ledger/sync/quality ve UI/install/eval kapsamdan düşmez. Araştırma salt cron/transport hata aramaya indirgenmez.

## Korunan U10 ve önceki araştırma

U10 Q49 accepted-snapshot→script/no_agent/monitor/agent→profile/runtime/context→persistence source araştırması ve yalnız `_inject_context_from` native selector diagnostic'idir. U10'un [note25](notes/25-CRON-EXECUTION-AND-CONTEXT.md), [RESEARCH](evidence/2026-09-12-cron-execution-context/RESEARCH.md), [SOURCES](evidence/2026-09-12-cron-execution-context/SOURCES.md), [NOT RUN](evidence/2026-09-12-cron-execution-context/CHECKS-NOT-RUN.md), [PUBLICATION](evidence/2026-09-12-cron-execution-context/PUBLICATION.md) değişmez. Content d1b045a66b7a07d62d135c025bf5a1d4ab741022; makbuz b658913dd8148dd9a4850414159f13513904f137. Bekleyen U10 ZIP'i yoktur.

U04-A/18 ile ayrı U04-B/19 aynı numaralarda aynı vakalar değildir; B'nin 33 original dosyalı subtree'si d01c92f7414713300934be3bb4e3d40ac57631b3 ve [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. U05–U09 ve önceki kanıt/yayınlar, notes01–25, METHOD ve synthesis01–04 değiştirilmez. Test grupları birleştirilmiş ürün skoru değildir. Dört provisional sentez dört Foundation alanının tamamlandığı anlamına gelmez.

Q40 actual DB/quiet history, Q42 startup admission, Q47 late-callback/NAS/clock, Q48/Q50 transport/status/cancel; Q41/Q43/Q44/Q45, Q07/Q22/Q26/Q29/Q38 eski fidelity/quality; U10 Q49 full-host, Q51 context→request/quality ve Q52 detection→handling açık kalır. Q53-A onları kapatmaz.

## Cold-start ve retrieval

1. Current main AGENT/tetiklenen protokoller → research root/studies catalog → META/STATE/INDEX → METHOD/PLAN. Current Q53 için bu STATE üstü ve A RESEARCH/SOURCES tam okunur; A'nın main publication/ref'i doğrulanır.
2. U10 note25 + SOURCES/RESEARCH/NOT RUN tam yolu korunur. Exact C test hükmü için SPEC + tam RESULT + MANIFEST + raw source/probe/inputs/outputs/log/attempt-00. A'da yeni runtime sonucu yoktur.
3. Synthesis02 ordinary-loop, synthesis04 scheduled-work; notes22–24/SOURCES/RESEARCH ve U08/U09 PUBLICATION üstleri. Eski unpublished ifadeler tarihçedir.
4. U04 mandatory ayrımı: note19 + B README/RECONCILIATION/manifest; synthesis03 + A SOURCES/RESEARCH/CONTINUITY-COVERAGE. Genel turn/memory için synthesis01/02 ve önceki U05/U06 kanıt yolları gerekli derinlikte korunur.
5. Bütün U10 historical state ve ham kimlik ayrıntıları [exact U10 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/b658913dd8148dd9a4850414159f13513904f137/research/studies/hermes-agent/STATE.md); incremental başlangıç tam kaydı [exact başlangıç STATE](https://github.com/batuhanozgun/agentic-os-search/blob/d3a4baeeb7afd97d38588c674c4842f01e87c6f0/research/studies/hermes-agent/STATE.md). Bu daha kısa current router eski kanıtları silmez veya epistemik statülerini yükseltmez.
