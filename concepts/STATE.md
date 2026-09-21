# Concepts — Güncel çalışma durumu

2026-09-21 · **B6-T17-C5c / U12-B1 tamamlandı; sıradaki iş ECC U12-B2**.

Bu dosya global amaç, yetki ve current/next work yüzeyidir. ECC okuma hesabı [READING](studies/ecc/READING.md), kullanım kayıtları [TERMS](studies/ecc/TERMS.md) içindedir. Kaynak araştırmanın kendi STATE'i Concepts'in sonraki işini belirlemez.

## 1. Amaç ve güncel aşama

**B6-SERIAL-EXTRACTION-ACTIVE / ECC-C1–C4-DURABLE-COMPLETE / ECC-C5a-U10-DURABLE-COMPLETE / ECC-C5b-U11-A–E-DURABLE-COMPLETE / ECC-U12-A–B1-DURABLE-COMPLETE / ECC-C5c-PARTIAL / ECC-C5-PARTIAL / ECC-PACKAGE-PARTIAL / METHOD-v0.3-WORKING / B7-B8-NOT-STARTED.**

Önce research/studies araştırmalarını kendi bağlamlarında tam okuyarak kullanımları ve ilişkileri çıkarmak; bütün ilgili çıkarımlar ve kapsam/delta hesabı tamamlandıktan sonra ayrı ortak değerlendirme yapmak. Genel sözlük, yeni ürün testi, Foundation doğrusu veya SOUL/Development OS mimari kararı bu aşamanın yerine geçmez.

Giriş: AGENT ve gereken protokoller → [INDEX](INDEX.md)'in STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE tam okuma yolu → etkin paketin READING/TERMS → gereken kaynak derinliği. Aynı konuşmada tam/değişmemiş içerik mekanik tekrarlanmaz; gerekli gerçek içerik görünür değilse canonical kaynaktan geri kazanılır. Tarihsel reset/pilot/next-work ifadeleri current authority değildir.

## 2. Program ve paket durumu

| İş | Durum |
|---|---|
| Pilotlar, B2/B4 ve B5-SCOPE-S1 | Tamamlandı; yöntem v0.3-working korunur |
| CMH, Superpowers, AI Knowledge Strategies | Concepts durable-complete; korunur |
| Multi-Agent Patterns, Anthropic AI-Native SDLC, gstack | Concepts durable-complete; korunur |
| Hermes Concepts | H1–H5 durable-complete / package-complete; korunur |
| Hermes source-study | ACTIVE PARTIAL; Q60 NOT RESEARCHED; Concepts bunu araştırmaz |
| ECC C1–C4 | U01–U09 durable-complete; korunur |
| ECC C5a | U10-A/U10-B transfer complete; korunur |
| ECC C5b | U11-A–E transfer complete; korunur |
| ECC C5c / U12-A | Execution-profile/harness-consumer aktarımı complete; korunur |
| ECC C5c / U12-B1 | Generated entry/callback/tool-consumer aktarımı bu tur tamamlandı |
| ECC C5c / U12-B2 | Sıradaki exact next; Note26 gövdesi okunmadı |
| ECC C5c / U12-C | Python/provider/tool-roundtrip ve mevcut E09 aktarımı bekliyor |
| ECC C6 | Paket geneli reconciliation/final closure bekliyor |
| ECC source-study | ACTIVE/PARTIAL; U12-C / plan 0.29'a kadar published; U13-A/Q07d1 NOT STARTED |
| Post-S1 additions | agentmemory, claude-swap, cli-continues, ponytail B7 öncesi kapsam hesabına alınacak |
| B7/B8 | Başlamadı |

C5a/b/c mevcut C5'in yürütme dilimleridir; yeni phase veya kaynak dışlama kararı değildir. U12-B1 kapanışı C5c/C5 veya paket-geneli C6 değildir. Paket/ID sayıları ilerleme yüzdesi sayılmaz; post-S1 kapsam tamamlanmış kabul edilmez.

## 3. Bu turun sonucu — U12-B1

Giriş main **25c2e6615990c4ad9a8acdd508ae5a6acab95b5d**, U12-A final kapanışıyla compare-identical bulundu. AGENT fresh tam okundu, kimliği değişmedi. R01/R02/R03 tam canonical içerikle yeniden geri kazanıldı; R04–R09 ve mandatory Concepts/current ECC girişlerinin aynı konuşmadaki tam, değişmemiş içerikleri korundu. Source-study U13-A başlatılmadı.

**Dört research dosyası tam okundu:** Note25, U12-B1-SOURCES, ROUND-U12-B ve PUBLICATION-U12-B1. Exact ref/blob/gerçek aralıklar yerel READING §3'tedir. Atfedilen upstream ECC/host kaynakları, dokümanlar veya testler yeniden okunmuş/çalıştırılmış sayılmaz. Kaynak araştırmanın OpenCode v1.4.3/877be7e karşılaştırması nested lock etiketiyle ilişkilidir; latest, registry bytes veya kurulu host değildir.

Yeni çıktı: [TERMS-OPENCODE-CALLBACKS.md](studies/ecc/TERMS-OPENCODE-CALLBACKS.md), **ECC-OC01–OC92**. Bunlar 92 adreslenebilir bağlamlı kullanım kaydıdır; bağımsız kavram/deney veya ortak kabul edilmiş tanım değildir. N25 §1–8 ve ledger/round/receipt kaynak rolleri, kullanım ve ilişki kayıtlarına bağlandı.

Önemli anlam sınırları:
- Callback'in çağrılıp değer döndürmesi, host'un o değeri tüketmesi değildir. Versioned trigger supplied output'u kullanır, replacement dönüşü değil.
- Tool execute dönüşü farklı consumer üzerinden gerçekten kullanılır; callback uyumsuzluğu bütün plugin'e genellenmez.
- Event türüyle aynı adlı fonksiyon, host bus'a abonelik değildir. Before output.args ile after input.args farklı sözleşmelerdir.
- Testin doğrudan çağırdığı fonksiyon ve asserted return nesnesi, gerçek host trigger/event yolunu sınamış sayılmaz.
- changed-files, yakalanmış module-local map'i raporlar; map boşluğu complete per-session/Git yokluk hükmü değildir.
- Lazy optional-store davranışı gerçek bir dayanıklılık mekanizmasıdır; tek özelliğin eksikliği global startup failure sayılmaz. Retry fırsatı gerçek loader-cache onarımı değildir.
- Root/nested dependency beyanları, indexed revision ve host karşılaştırması tek kurulum yapılmaz. Üç path/type precheck'i transitive payload veya callback uyumunu kanıtlamaz.

**Yorum ve değişim izi:** B1'in tarihsel U12-B PARTIAL ifadesi current source-study'ye geri taşınmadı. Bugün mevcut B2 araştırma çıktısının Concepts aktarımı bekliyor; B1'deki eksik source work yalnız canlı test açığı diye dışlanmadı. MR26'nın terk ettiği static-import şüphesi OC75'te tarihsel araştırmacı değişimi olarak tutuldu, bu turun kendi keşfi diye sunulmadı. Önceki kullanım dosyalarını değiştirmeyi gerektiren maddi çelişki saptanmadı. Yeni OC25/OC55 type ifadelerine yalnız Markdown code-span eklenmesi anlam/ID düzeltmesi değildir.

Olumlu plugin-only export, after-hook/tool return, optional-store ve preparation-error ayrımları korundu. Total context loss, permission bypass, observed incident veya all-host failure iddiası üretilmedi. Q02b3 ve önceki güçlü doğrulama soruları açık kalır. U12-B2/C gövdeleri bu tur okunmadı.

## 4. Exact next — C5c / U12-B2

**research/studies/ecc/notes/26-OPENCODE-INSTALLATION-LOADING-AND-TOOL-RESULTS.md** → evidence/U12-B2-SOURCES.md → ROUND-U12-B2.md → PUBLICATION-U12-B2.md; bağlı evidence gerçek source scope'uyla devralınır.

Amaç mevcut araştırmadaki root/nested/package identity, managed installation/config rewriting, loader resolution, materialized imports ve tool-result kullanımlarını çıkarmaktır. Yeni build, installation, host/model testi veya ECC source-study araştırması değildir. Note25'in B1/B2 ayrımı korunur; B2 eski bir kaynaktaki future next diye yapılmamış source research sanılmaz.

Ardından U12-C/Python ve mevcut E09. C5c bitince C6, yerel READING'nin **beş tam tarihsel manifesti ve current kaydı**, bütün ECC TERMS, kalan history/inventory/evidence ve source delta üzerinden paket-geneli coverage/role/ID hesabını yapar. C6 yalnız current özetle kapanmaz. ECC sonrası paket SCOPE sırasına göre work-management-project-control'dür. B7 tamamlanmadan B8 ortak referans başlamaz. Tamamlanmış aktarım birimleri sırf yeni tur diye yeniden yapılmaz.

## 5. İki risk ve yetki

Batu okuma anındaki anlam seçimlerini denetleyemediğinden önemli dayanak, yorum, belirsizlik ve değişiklik görünür olmalıdır. Ortak sözcük ortak anlamı garanti etmez; kaynak kullanımı, araştırmacı yorumu, extractor açıklaması ve kullanıcı onayı teknik doğruluk bakımından ayrı kalır. Bu turun somut karşılığı callback return/consumer output, event-name/subscription, tracked-map/session-history ve B1 historical/B2 current ayrımlarıdır.

Kaynakta tanımlanmayan anlam dış genel bilgiyle doldurulmaz; açık kaynak ayrımı belirsizlik bahanesiyle atlanmaz. Q02b3 ve önceki runtime/authority/acceptance soruları çözülmüş veya otomatik yeni Concepts deney borcu sayılmaz. E06 NOT VERIFIED/EXCLUDED; iki E05 geçmişi ve E04/E07/E08/E09 ayrı kapsamlarında korunur.

Yazma yetkisi ilgili Concepts kullanım dosyası, yerel READING/TERMS ve global STATE ile sınırlıdır. Agent-control, Foundation, source studies, CATALOG, diğer Concepts paketleri, explorations ve publications değiştirilmez. Yeni endpoint/request, provider/model, installation, target test/fixture, DB/runtime, release veya upstream mutation yapılmadı. Yerel Markdown/ID/hash kontrolleri yalnız yayın idaresidir.

## 6. Korunmuş tarih, eşzamanlı çalışma ve yayın

U12-A'nın ayrıntılı sonucu ve önceki checkpoint zinciri [25c2e66 STATE'in tam sürümünde](https://github.com/batuhanozgun/agentic-os-search/blob/25c2e6615990c4ad9a8acdd508ae5a6acab95b5d/concepts/STATE.md) korunur; blob **8e8a5f3fdaca40e0875150e6dfff332f1b746dcf**. O sürüm df7b81a, eb7754b, f0d9ae3 ve 753a4c6 tam geçmiş yollarını korur. Yerel READING önceki dört manifest bağlantısını tutup U12-A için beşinci tam snapshot bağlantısını ekledi. Eski TERMS veya maddi düzeltme izleri değiştirilmedi.

Bu turun actual checkpoints:
- Yeni OC TERMS: **4517b5431d2ee5070d6a4dd8cca50e14ae8564d0**, blob **98feb0302d61ce513850d16186a95570464c0ec5**.
- Type-spelling biçim düzeltmesi: **f9291e2041e24aabf00c804c56824aaf8b042631**, blob **25abf0599f129c3c3d0af22d28fe145814fc3180**.
- Yerel READING: **c37b49de19a1c301d3f010a68b4055ff9b1e03ad**, blob **0dbad408c96a73b827d26289b9d79f212dcb6248**.
- TERMS router: **7b4fa4cb47ff18e6314ec914cb4c6400e48489fa**, blob **c4f11c6b2e076b25b8f2e1d021e9ac9a8e652ccd**.

Yeni TERMS'in hazırlanmış ilk/final byte kimlikleri remote blob'larla eşleşti; local kontrol 92 unique/sıralı ID, gap/duplicate yok ve üç-kolon yapısını gösterdi. Initial/final content aralıkları ile yalnız iki code-span ekleyen actual diff karşılaştırıldı. Bu yeni dosya için byte correspondence vardır; bütün repo automated link/ID suite'i veya bağımsız semantik/host doğrulaması yoktur.

Entry yazılarından önceki 25c2e66→main aralığı **42 commit** içeriyordu: bu turun iki TERMS commit'i yanında bağımsız **EXP-004 ve explorations INDEX/CATALOG** değişimleri vardı. Bunlar korunmuştur ve bu Concepts çalışmasına mal edilmez. Source ECC, agent-control ve current Concepts entry'leri o karşılaştırmada değişmemişti. Ref **f9291e2** olarak okundu; onun mevcut geçmişi üzerinde contents/SHA kontrollü yazıldı, eski köke force dönüş yapılmadı. Toplam interval yalnız Concepts diye raporlanmaz.

Bu STATE yazısından sonra final ref/diff ve current-entry readback kontrolü yapılır. Dosya kendi gelecekteki hash'ini veya henüz yapılmamış kontrolü uydurmaz; bu chronological uyarı ayrı repair işi değildir. Aynı-assistant publication/source-to-record kontrolü bağımsız araştırma doğrulaması değildir.
