# DEVOS-001 — kaynak kapsamı ve okuma girişleri

**Kaynak tabanı:** `batuhanozgun/agentic-os-search@dc76496e2ea87a08b60f88ea8ec2731c6a4b5cbb`.
**Rol:** kapsam ve soru→kayıt yönlendirmesi; içerik özeti veya tek başına tam-okuma kanıtı değil. İş otoritesi [WORK](../WORK.md), yöntem [METHOD](../METHOD.md).

## Gerçek ilerleme

İlk Research kümesi: [F08-FOUNDATION-FRAME](F08-FOUNDATION-FRAME.md). Foundation kök STATE/INDEX ve 08 paketinin 13/13 dosyası doğrudan tam okundu; kaynak-bağlı 20 katkı kaydı ve bütünsel model çıkarıldı. Bu yalnız tanımlı kümenin kapsamıdır; bütün Foundation veya bütün repo tamamlanmadı. Karşı aktör okuması bekleniyor.

Kök, research, Foundation ve studies doğrudan Git ağaçları alındı. Aşağıdaki alt-ağaç kayıtları tüm yaprak dosyaların açıldığı anlamına gelmez. Claude'a bütün path/blob manifestini üretme görevi R-004 ile verildi; alındısı yok. Manifest veya eşdeğer ağaç dolaşımı tamamlanana kadar bütün-repo dosya sayısı/okuma yüzdesi ilan edilmez.

Durumlar: ENVANTERDE; TAM_OKUNDU; KISMİ (aralık); KAYITLANDI; KARŞI_OKUNDU; ENGEL; EŞDEĞER_KOPYA (özgün bağlantısıyla); KONTROL. Tarihsel olmak okumama gerekçesi değildir; tarihsel karar etkin yetki de değildir.

## Kökün tamamı

| Kaynak | Git nesnesi | Birincil sorumlu / durum |
|---|---|---|
| README.md | blob 3f9a9e4ef7418968ab15ce80bb2190016f6cba27 | Research; kaynak tabanındaki yönlendirme okundu |
| AGENT.md | blob aea3dd845e0f0bbcfb34465edb23782e99f95c80 | Kontrol; araştırma sonucu değil |
| agent/ | tree bd184e1b2a9598dbdd65aca8adb9767b81dea965 | Kontrol; araştırma sonucu değil |
| research/ | tree 5edfd1746d2e2c5a53590909550bf713e4754ced | Aşağıda açılır; gövdeler tamamlanmadı |
| concepts/ | tree b9579b6dc8282ee7d9f88f3c726f59e607fbf1a4 | Claude; okuma/çıkarım açık |
| explorations/ | tree 039979d678adca886e24034b81848f18ed13d6d3 | Research; yeni bütünsel çıkarım açık |
| publications/ | tree 643adf03268a1dba84296ae46a17dd6450246cf0 | Research; açık |
| development-os/ | tree 523e23c368913cd8847a1565dba986a94f346219 | Research; başlangıca kadarki drift/çalışma kaydı. Yeni çıktılar öz-okuma kuyruğu değil |

## Research kapsamı

| Kaynak | Git nesnesi | Durum |
|---|---|---|
| research/INDEX.md | blob 167d8df1f3d29544065388ff915a6c24518772e6 | Yeni geçişte açık |
| research/soul-context/ | tree 70aee5302300c2ca2c3fe003b3ecaf9909b23c46 | Research; tarihsel denemeler ve amaç bağlamı, açık |
| research/soul-foundations/ | tree 0f9513f91bba76f1e52c955ddcb6270908c11939 | Research; F08 ilk kümesi kayıtlandı, kalanlar açık |
| research/studies/ | tree 7710f53876711e168e463843aa039296b64404f7 | Claude birincil; Research karşı okuma/kayıt tüketimi |

Foundation'ın bütün doğrudan üyeleri ve durumları:

| Küme | Durum |
|---|---|
| Kök STATE.md, INDEX.md | F08 kaynak defterinde tam okundu |
| 08_foundation-sufficiency-reuse-review/ | 13/13 dosya tam okundu ve F08'e çıkarıldı; karşı okuma bekliyor |
| README.md, RESEARCH-USE-ALIGNMENT.md | Sıradaki girişler |
| 00_context/ | Sıradaki tam paket; alt dosya envanteri ve okuma açık |
| 01_verticals/ | Bütün dikeyler açık |
| 02_adequacy/ | Açık |
| 03_ground-deepening/ | Bütün zemin/alt araştırmalar açık |
| 04_top-level-adequacy-rerun/ | Açık |
| 05_relation-control-composition/ | Bütün bileşim/alt araştırmalar açık |
| 06_integration-frontier-review/ | Açık |
| 07_selection-dynamics-integration-review/ | Açık |
| history/, REPAIR-AUDIT.md, REPAIR-PUBLICATION.md | Tarihçe/onarım kapsamı açık |

Sonraki sıra: kalan Foundation kök amaç/uyum girişleri → 00_context → 01_verticals/02 → 03 → 04–07/composition → history/repair uzlaştırması. 08'in üst sonucu alt kaynakların yerine geçmez. Büyük kümeler dosya manifestleriyle alt birimlere ayrılır; hiçbir kalan dosya görünmez olmaz.

## Studies'in bütün doğrudan paketleri

Başlangıç durumları **OKUMA/ÇIKARIM AÇIK**. Mevcut ağaç üyeleridir; bekleyen paket ile tamamlanmış araştırma ayrımı paket içinden öğrenilir. İlk örnek gstack; liste yalnız gstack/Hermes/ECC değildir.

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

Kök CATALOG.md, INDEX.md ve PACKAGE-CONTRACT.md kapsamda. RPD ve iş yönetimi ortak planlama bağlamına ayrıca okunur. Claude'un eski 2.204/~%81 beyanı bu yeni çıkarımın tamamlanma sayısı değildir.

## Soru→katkı kaydı rotaları

| Toplu değerlendirmede geri aranacak ihtiyaç | İlk kayıt / derinleşme sınırı |
|---|---|
| İşi üreten sistem, planlama, atama ve koordinasyon | F08-01/02/03; 00_context/Work/Actors özgün ayrıntıları açık |
| Gerçek ortam ve bileşik iş hazırlığı | F08-04/06/07; Environment/RPD ayrıntıları açık |
| Bilgi, anlam, yeterlik, erişim ve kanıt | F08-05/08/09; Information alt araştırmaları açık |
| Amaç, yetki ve birden fazla katılımcı | F08-03/10/16; Actors/composition ayrıntıları açık |
| Oturum devamı, gerekçe, geri bildirim ve öğrenme | F08-11/12/20; Records/Revision/Feedback ayrıntıları açık |
| Açık uçlu iş, alternatif giriş/temsil biçimleri | F08-13/14/15; Work ve studies uygulamaları açık |
| Araştırmadan gerekçeli yapı kararına geçiş | F08-17/18/19; bütün P1/P2 işi tamamlanmadı |

Bu kimliklerin hepsi [F08](F08-FOUNDATION-FRAME.md)'dedir; yalnız üst-küme kaynak çıkarımıdır. Claude kayıtları beklenen adres: hedef `coordination/devos-001/reading/`; alım teyitsiz. Başkasının kaydını okumak onun kaynaklarını tam okuma sayılmaz.

## Kapsam kapanışı

Bütün başlangıç dosyaları manifestle uzlaştırılmadan; tam okumalar/kayıtlar tamamlanmadan ve maddi atlamalar değerlendirilmeden P2/P3 başlamaz. Kaynak main ilerlerse yeni/farklı blob'lar ayrı delta kuyruğuna girer; sabit kaynak snapshot'ı ile güncel owner yetkisi ayrı tutulur. Denemenin yeni çıktı dosyaları paydasını kendi kendine büyütmez.
