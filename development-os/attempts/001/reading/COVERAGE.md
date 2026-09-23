# DEVOS-001 — kaynak kapsamı ve okuma girişleri

**Kaynak tabanı:** `batuhanozgun/agentic-os-search@dc76496e2ea87a08b60f88ea8ec2731c6a4b5cbb`.
**Rol:** bütün kapsamı görünür tutan okuma haritası; içerik özeti veya tam-okuma kanıtı değil. İş otoritesi [WORK](../WORK.md), kayıt yöntemi [METHOD](../METHOD.md).

## Kapsam hesabı

Bu başlangıçta kök, research, Foundation ve studies doğrudan Git ağaçları alındı. Kök bütün alanları kapsıyor. Aşağıdaki alt-ağaç kayıtları henüz tüm yaprak dosyaların açıldığı veya okunduğu anlamına gelmez. Claude'a bütün path/blob manifestini üretme görevi R-004 ile verildi; alındısı yok. Bu manifest gelene veya eşdeğer ağaç dolaşımı bitene kadar tam dosya sayısı/okuma yüzdesi ilan edilmez.

Dosya durumları ayrı: ENVANTERDE, TAM_OKUNDU, KISMİ (aralık), KAYITLANDI, KARŞI_OKUNDU, ENGEL, EŞDEĞER_KOPYA (özgün bağlantısıyla), KONTROL. Tarihsel olmak okumama gerekçesi değil; tarihsel karar etkin yetki değildir.

## Kökün tamamı

| Kaynak | Git nesnesi | Birincil sorumlu / durum |
|---|---|---|
| README.md | blob 3f9a9e4ef7418968ab15ce80bb2190016f6cba27 | Research; yönlendirme okundu |
| AGENT.md | blob aea3dd845e0f0bbcfb34465edb23782e99f95c80 | Kontrol; araştırma sonucu değil |
| agent/ | tree bd184e1b2a9598dbdd65aca8adb9767b81dea965 | Kontrol; araştırma sonucu değil |
| research/ | tree 5edfd1746d2e2c5a53590909550bf713e4754ced | Aşağıda açılır; gövdeler tamamlanmadı |
| concepts/ | tree b9579b6dc8282ee7d9f88f3c726f59e607fbf1a4 | Claude; okuma/çıkarım açık |
| explorations/ | tree 039979d678adca886e24034b81848f18ed13d6d3 | Research; yeni bütünsel çıkarım açık |
| publications/ | tree 643adf03268a1dba84296ae46a17dd6450246cf0 | Research; açık |
| development-os/ | tree 523e23c368913cd8847a1565dba986a94f346219 | Research; bu başlangıca kadarki drift/çalışma kaydı. Yeni çıktılar öz-okuma kuyruğu değil |

## Research kapsamı

| Kaynak | Git nesnesi | Durum |
|---|---|---|
| research/INDEX.md | blob 167d8df1f3d29544065388ff915a6c24518772e6 | Genel yönlendirme; yeni geçişte açık |
| research/soul-context/ | tree 70aee5302300c2ca2c3fe003b3ecaf9909b23c46 | Research; tarihsel denemeler ve amaç bağlamı, açık |
| research/soul-foundations/ | tree 0f9513f91bba76f1e52c955ddcb6270908c11939 | Research; ilk okuma ailesi |
| research/studies/ | tree 7710f53876711e168e463843aa039296b64404f7 | Claude birincil; Research karşı okuma/kayıt tüketimi |

Foundation'ın bütün doğrudan üyeleri: `00_context/`, `01_verticals/`, `02_adequacy/`, `03_ground-deepening/`, `04_top-level-adequacy-rerun/`, `05_relation-control-composition/`, `06_integration-frontier-review/`, `07_selection-dynamics-integration-review/`, `08_foundation-sufficiency-reuse-review/`, `history/`; `INDEX.md`, `README.md`, `REPAIR-AUDIT.md`, `REPAIR-PUBLICATION.md`, `RESEARCH-USE-ALIGNMENT.md`, `STATE.md`. Hiçbiri sadece adı görüldü diye tamamlanmış sayılmaz.

Başlangıç sırası: Foundation current STATE/INDEX → 08 genel sonuç/yeniden kullanım ve kapsam → 00_context → 01_verticals ve 02_adequacy → 03_ground-deepening → 04–07/composition → history/repair/alignment uzlaştırması. 08'i önce okumak alt kaynakların yerine geçmez. Alt ağaçlar kendi dosya manifestleriyle açılır; bölünürse kalanlar açık tutulur.

## Studies'in bütün doğrudan paketleri

Her satırın başlangıç durumu **OKUMA/ÇIKARIM AÇIK**. Bunlar yalnız mevcut ağaç üyeleridir; bekleyen paket ile tamamlanmış araştırma ayrımı paket içinden öğrenilir. İlk öncelikli örnek gstack; liste yalnız ona/Hermes/ECC'ye indirgenmez.

| Paket | Paket | Paket |
|---|---|---|
| agent-memory-providers | agentic-ai-systems-roadmap | agentmemory |
| ai-knowledge-strategies | ai-memory | anthropic-ai-native-sdlc-playbook |
| beads | claude-swap | cli-continues |
| context-memory-harness-engineering | context-mode | deepseek-harness |
| ecc | erpnext | flowable |
| gastown | gstack | hands-on-large-language-models |
| harness-engineering-and-evolution | hermes-agent | i-have-adhd |
| leantime | llm-wiki | mattpocock-skills |
| multi-agent-patterns | openproject | openspec |
| openviking | ponytail | public-apis |
| recursive-prerequisite-discovery | spec-kit | superpowers |
| the-carbon-layer | work-management-project-control | — |

Studies kök dosyaları `CATALOG.md`, `INDEX.md`, `PACKAGE-CONTRACT.md` da kapsamdadır. RPD ve iş yönetimi kayıtları ortak planlama bağlamına ayrıca okunur. Claude'un eski 2.204/~%81 beyanı bu yeni çıkarımın tamamlanma sayısı değildir.

## Kayıt ve soru→kaynak rotaları

Henüz bu yeniden yönlendirmeye ait substantive katkı kaydı yayımlanmadı. İlk Research kaydı Foundation genel çerçevesi/08 kümesinden üretilecek. Sonra bu bölüm kayıt kimliği, kapsanan exact dosyalar, dört zemin/ilişki bakımından katkı, karşı okuma ve kalan kapsamla güncellenir. Her kaydın ayrıntılı source/read defteri kendi gövdesindedir.

Claude kayıtları beklenen adres: hedef `coordination/devos-001/reading/`; yayın/alım teyitsiz. Diğer aktör kaydına bağlantı verilmesi onun kaynağının bu aktör tarafından tam okunduğu anlamına gelmez.

## Kapsam kapanışı

Bütün başlangıç dosyaları manifestle uzlaştırılmadan; tam okumalar/kayıtlar tamamlanmadan ve maddi atlamalar değerlendirilmeden P2/P3 başlamaz. Kaynak main ilerlerse yeni/farklı blob'lar delta kuyruğuna girer; sabit snapshot ile güncel owner yetkisi ayrı tutulur. Bu alanın yeni çıktıları tamlık paydasını kendi kendine büyütmez.
