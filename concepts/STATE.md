# Concepts — Güncel çalışma durumu

2026-09-20 · **B6-T17-C5c / U12-A tamamlandı; sıradaki iş ECC U12-B1**.

Bu dosya global amaç, yetki ve current/next work yüzeyidir. Ayrıntılı ECC okuma hesabı [READING](studies/ecc/READING.md), kullanım kayıtları [TERMS](studies/ecc/TERMS.md) içindedir. Kaynak araştırmanın kendi STATE'i Concepts'in sonraki işini belirlemez.

## 1. Amaç ve güncel aşama

**B6-SERIAL-EXTRACTION-ACTIVE / ECC-C1–C4-DURABLE-COMPLETE / ECC-C5a-U10-DURABLE-COMPLETE / ECC-C5b-U11-A–E-DURABLE-COMPLETE / ECC-U12-A-DURABLE-COMPLETE / ECC-C5c-PARTIAL / ECC-C5-PARTIAL / ECC-PACKAGE-PARTIAL / METHOD-v0.3-WORKING / B7-B8-NOT-STARTED.**

Önce research/studies araştırmalarını kendi bağlamlarında tam okuyarak kullanımları ve ilişkileri çıkarmak; bütün ilgili çıkarımlar ve kapsam/delta kontrolü tamamlandıktan sonra ayrı ortak değerlendirme yapmak. Genel sözlük araştırması, yeni ürün testi, Foundation doğrusu veya SOUL/Development OS mimarisi bu ilk aşamanın yerine geçmez.

Giriş: AGENT ve gereken protokoller → [INDEX](INDEX.md)'in STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE tam okuma yolu → etkin paketin READING/TERMS → gereken kaynak derinliği. Aynı konuşmada tam ve değişmemiş içerik mekanik tekrar edilmez; gerekli gerçek içerik görünür değilse canonical kaynaktan geri kazanılır. Tarihsel reset/pilot/current-next ifadeleri yeni çalışma talimatı değildir.

## 2. Program ve paket durumu

| İş | Durum |
|---|---|
| Pilotlar, B2/B4 ve B5-SCOPE-S1 | Tamamlandı; yöntem v0.3-working korunur |
| CMH, Superpowers, AI Knowledge Strategies | Concepts durable-complete; korunur |
| Multi-Agent Patterns, Anthropic AI-Native SDLC, gstack | Concepts durable-complete; korunur |
| Hermes Concepts | H1–H5 durable-complete / package-complete; korunur |
| Hermes source-study | ACTIVE PARTIAL; Q60 NOT RESEARCHED; Concepts bunu araştırmaz |
| ECC Concepts C1–C4 | U01–U09 durable-complete; korunur |
| ECC C5a | U10-A/U10-B transfer complete; korunur |
| ECC C5b | U11-A–E transfer complete; korunur |
| ECC C5c / U12-A | Execution-profile/harness-consumer aktarımı bu tur tamamlandı |
| ECC C5c / U12-B1–B2 | Sırada; ilk exact next U12-B1/Note25 |
| ECC C5c / U12-C | Python/provider/tool-roundtrip ve mevcut E09 aktarımı bekliyor |
| ECC C6 | Paket geneli reconciliation/final closure bekliyor |
| ECC source-study | ACTIVE/PARTIAL; U12-C / plan 0.29'a kadar published; U13-A/Q07d1 NOT STARTED |
| Post-S1 additions | agentmemory, claude-swap, cli-continues, ponytail B7 öncesi kapsam hesabına alınacak |
| B7/B8 | Başlamadı |

C5a/b/c mevcut C5'in yürütme dilimleridir; yeni phase veya kaynak dışlama kararı değildir. **U12-A kapanışı, C5c/C5 veya ECC paketinin bütün dosyalarının reconciliation'ı değildir.** U12-B1/B2/C ve C6 açıktır. Paket/ID sayıları ilerleme yüzdesi değildir; S1 sonrası eklemeler hesaba katılmadan kaynak evreni tamamlandı denmez.

## 3. Bu turun gerçek sonucu — U12-A

Giriş main **df7b81a8f0bdb045d7307e63fdf306d0eaf9e843**, U11-E final kapanışıyla compare-identical bulundu. AGENT fresh tam okundu ve aynı aea3dd845e0f0bbcfb34465edb23782e99f95c80 kimliğindeydi. R01–R09'un, mandatory Concepts dosyalarının, current READING/TERMS ve ECC META/STATE/INDEX'in bu konuşmadaki tam değişmemiş canonical içerikleri korundu. Bu yeni-oturum deneyi veya bütün geçmişi tekrar okuma değildir.

**Dört araştırma dosyası tam okundu:** Note24, U12-A-SOURCES, ROUND-U12-A ve PUBLICATION-U12-A. Exact ref/blob/aralık hesabı yerel READING §3'tedir. Atfedilen upstream Rust/host/process/test kaynakları bu tur yeniden okunmuş veya çalıştırılmış sayılmaz. Host dokümanı açıklamaları araştırmanın 2026-09-19 tarihli atıflarıdır, yeni güncel ürün doğrulaması değildir. Source-only inquiry yeni deney/E09 gibi gösterilmedi.

Yeni çıktı: [TERMS-EXECUTION-PROFILES.md](studies/ecc/TERMS-EXECUTION-PROFILES.md), **ECC-EP01–EP84**. Seksen dört adreslenebilir kullanım kaydıdır; bağımsız kavram veya kanıt sayısı değildir. N24 §1–8 ve ledger kaynak/consumer/test/sözleşme kapsamı K/Y/T/H rolleriyle kayıtlara bağlandı.

Başlıca ayrımlar:
- Ortak profile representation, portable enforcement değildir; native argv, task text ve ayrı ECC denetimleri farklı consumer yollarıdır.
- Tarihli Claude allowed-tools preapproval, exclusive tools availability değildir; deny/mode kontrollerinin varlığı da korunur.
- Configured runner aynı known key'i kullansa bile built-in komut tarifinin yerini alır; yalnız executable ekleme/değiştirme değildir.
- Native token flag yokluğu token alanının tüketilmediği anlamına gelmez: gerçek TUI/CLI→metric import→ECC enforcer vardır. Aynı enforcer global USD ve profile token kontrol eder, profile.max_budget_usd'yi kontrol etmez.
- Recorded-usage denetimi provider ön-harcama izni değildir; çağrı, metrik güncelliği, seçilmiş state ve gerçek termination sınırları açıktır.
- get_session_profile agent=None, effective harness'ın session'da ayrı saklanmasıyla birlikte okunur; kendiliğinden seçim kaybı değildir.
- Malformed stored deny JSON'un boş vektöre dönüşmesi, bilerek boş yazılmış listeyle aynı köken değildir; normal writer geçerli JSON üretir.
- Shared environment label ile runtime'ın explicit session_id'si farklı kimlik yollarıdır; marker discovery plugin activation değildir.

**Extractor düzeltmesi:** İlk EP29 iki host izin yüzeyini; EP33 program/base_args alanlarını tek adreste taşıyordu. EP29 OpenCode/EP84 Gemini ve EP33 program/EP83 base_args olarak ayrıldı. İlk sürüm, kaynak ve etki kontrolü TERMS §11'de korunur. Diğer yeni kullanım açıklamaları, önceki TERMS ve source-study değiştirilmedi.

Olumlu native mapping, metinsel intent aktarımı, configured extension, profil serialization, program refusal ve gerçek bütçe consumer'ları korundu. Koşullu malformed-list/custom-flag/environment örnekleri canlı exploit veya ölçülmüş başarısızlık sayılmadı. Q02a2 ve önceki güçlü doğrulama soruları açık kalır. U12-B1/B2/C gövdeleri bu tur okunmadı.

## 4. Exact next — C5c / U12-B1

**research/studies/ecc/notes/25-OPENCODE-CALLBACK-CONTRACTS-AND-GENERATED-ENTRY.md** → evidence/U12-B1-SOURCES.md → ROUND-U12-B.md → PUBLICATION-U12-B1.md; bağlı evidence gerçek kapsamıyla devralınır.

Amaç mevcut araştırmadaki generated entry, callback/event/output, useful tool path ve source/host sözleşmesi kullanımlarını çıkarmaktır. Ardından Note26/U12-B2 installation/loading/tool-result aktarımı gelir. Rust OpenCode argv tarifi EP16 bu ayrı plugin ailesini tamamlamaz. Build, host installation, yeni model/test veya ECC source-study U13-A araştırması bu yetkinin parçası değildir. Exact yollar önceki tam source INDEX'ten gelir; yolu bilmek gövde okuması değildir.

Sonra U12-C/Python ve mevcut E09 kanıtı. C5c bitince C6, READING'nin **dört tam tarihsel manifesti ve current kaydı**, bütün ECC TERMS, kalan history/inventory/evidence ve source delta üzerinden paket-geneli coverage/role/ID kontrolünü yapar. C6 yalnız current özetle kapanmaz. ECC sonrası paket SCOPE sırasına göre work-management-project-control'dür. B7 tamamlanmadan B8 ortak referans başlamaz. U10, U11-A–E ve U12-A sırf yeni tur diye yeniden yapılmaz.

## 5. İki risk ve yetki

Batu okuma anındaki anlam seçimlerini denetleyemediğinden önemli dayanak, yorum, belirsizlik ve değişiklik görünür olmalıdır. Ortak sözcükler ortak anlamı garanti etmez; kaynak kullanımı, araştırmacı yorumu, extractor açıklaması ve kullanıcı onayı teknik doğruluk yerine geçmez. Kullanıcı teknik oracle değildir. Bu turun somut karşılığı representation/enforcement, preapproval/availability, per-profile/global budget ve ayrı host/runner alanlarının adreslenmesidir.

Kaynakta tanımlanmayan anlam dış genel bilgiyle doldurulmaz; açık kaynak ayrımı da belirsizlik bahanesiyle atlanmaz. Q02a2 ve önceki güçlü runtime/authority/acceptance soruları çözülmüş veya otomatik yeni Concepts deney borcu sayılmaz. E06 NOT VERIFIED/EXCLUDED; iki E05 geçmişi ve E04/E07/E08/E09 kendi kapsamlarında korunur.

Yazma yetkisi yalnız ilgili Concepts kullanım dosyası, yerel READING/TERMS ve global STATE bakımındandır. Agent-control, Foundation, source studies, CATALOG, diğer Concepts paketleri, explorations ve publications değiştirilemez. Yeni endpoint, dış request, provider/model, installation, test/fixture, DB/runtime, release veya upstream mutation bu tur yapılmadı.

## 6. Korunmuş tarih ve yayın kontrolü

U11-E/C5b kapanışı, önceki global kayıtlar ve bütün daha eski checkpoint yolları [df7b81a STATE'in tam sürümünde](https://github.com/batuhanozgun/agentic-os-search/blob/df7b81a8f0bdb045d7307e63fdf306d0eaf9e843/concepts/STATE.md) korunur; blob **2c84ee354051e7a9f0662ca7c1d8af93b0956bf6**. O sürüm eb7754b, f0d9ae3 ve 753a4c6 tam STATE kayıtlarını da bağlar. Tarihsel current-next ifadeleri geçmiş checkpoint'lerdir; eski kullanım dosyaları ve düzeltmeleri yerinde kalır.

Global STATE okuma günlüğünün ikinci kopyası değildir. Yerel READING de U11-E ayrıntısını df7b81a tam sürümüne bağladı; önceki üç tam manifest bağlantısı korundu. Kapsam/tarih düşürülmedi; C6 dört tam tarihsel READING'yi ve current kaydı devralır.

U12-A gerçek checkpoints:
- Yeni TERMS: **f1dc83651f57fcdaff1074cd0339717624d58fdb**, ilk blob **a9004bb9370d57a25aff3a6aff7d01a805ee71dd**; 1–68/69–124/125–EOF tam readback.
- Adresleme düzeltmesi: **ee91f06721ac5774d596a22bf62556fe3fad0ea7**, blob **480a8decc41d1f11dea5d83b4d46124b46086b32**; tam actual diff alanı okundu. Yalnız EP29/EP33, mapping/açıklama, correction izi/yeni EP83–EP84 ve sayım değişti.
- Yerel READING: **9476be45fd979535c027533f2a05ff5ef334953a**, blob **5ac000dab5f3372d9617549f3702c43e193008d2**.
- TERMS router: **af2b505ed43d753b721387326b4eb5fca64c7072**, blob **886f4012f1545923b5bff4dafb220cccc1c7c1a8**.

Entry yazıları öncesi df7b81a→main karşılaştırması iki commit/yalnız yeni TERMS dosyasını gösterdi. Final current-ref/diff ve güncellenmiş girişlerin readback'i bu STATE yazımından sonra yapılır. Bu chronological uyarı ayrı next-work üretmez; dosya kendi gelecekteki hash'ini uydurmaz. Otomatik tüm-repo ID/link suite'i, bağımsız aktör incelemesi veya local full-byte/hash-match iddiası yoktur. Aynı-assistant source-to-record/readback kontrolü bilimsel ya da ürün düzeyi bağımsız doğrulama değildir.
