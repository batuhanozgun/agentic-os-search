# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-21 · **B6-T17-C5c / U12-A–B2 TRANSFER-COMPLETE / U12-C-NEXT / C5c-PARTIAL / C5-PARTIAL / PACKAGE-PARTIAL**.

Bu dosya Concepts okuma/aktarım durumudur. [TERMS.md](TERMS.md) kullanımları, [global STATE](../../STATE.md) current/next işi taşır. Kaynak ECC araştırması ayrı ACTIVE/PARTIAL çalışmadır: bu tur sırasında U13-A/Q07d1 IN PROGRESS olarak etkinleştirildi; son tamamlanmış kaynak inquiry U12-C'dir. Bu source değişimi Concepts'i U13-A araştırmasına yönlendirmez. Yeni kaynak farkı §5/C6 hesabında tutulur.

## 1. Sabit aktarım kaynağı ve korunmuş tam geçmiş

- Research repository: batuhanozgun/agentic-os-search.
- B2 aktarım snapshot'ı / gözlenen giriş main: **2db53e57c4dba096a6a803433cfee9d7d99b2c90**.
- Önceki Concepts kapanışı: **5852459c9dc273f3b7aa2911978883424cd5aca7**. Buradan giriş main'e 47 commit vardı; değişen yollar explorations/EXP-004 ve explorations girişleriyle sınırlıydı. Bu bağımsız iş korunur; Concepts veya ECC aktarımına mal edilmez.
- ECC research pin: **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a**.
- Host comparator: **anomalyco/opencode v1.4.3 / 877be7e8e04142cd8fbebcb5e6c4b9617bf28cce**; nested lock etiketiyle ilişkilidir, registry/installed/latest kimliği değildir.
- Ayrı indexed observation: **07756cee15788a54506031462794ad645719b028**; repin değildir.
- METHOD v0.3-working ve SCOPE S1 korunur; post-S1 delta kapanmış değildir.

Önceki exact manifestler, yorum değişiklikleri ve yayın kayıtları aşağıdaki **tam değişmez READING sürümlerinde** korunur. Bunlar current-next veya kısa özet değildir:

| Kapsam | Tam READING sürümü | Git blob |
|---|---|---|
| C1–C4 / U01–U09 | [753a4c6](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/studies/ecc/READING.md) | a027c7cb71f06de5355fcb4783f9a0a88d581c0c |
| C5a/U10, U11-A/E08 ve U11-B | [f0d9ae3](https://github.com/batuhanozgun/agentic-os-search/blob/f0d9ae31062459cf7b2cd982eaf484cbdfc336e8/concepts/studies/ecc/READING.md) | 0c740a10a604774ce8c1df4a967a419de69c6ca5 |
| U11-C/D | [eb7754b](https://github.com/batuhanozgun/agentic-os-search/blob/eb7754b34953b57b9c1aeb92ef4885993ded7ca2/concepts/studies/ecc/READING.md) | 8b1ebc35fd4c5c2e20a9395f9f45f9599428b3a8 |
| U11-E ve C5b kapanışı | [df7b81a](https://github.com/batuhanozgun/agentic-os-search/blob/df7b81a8f0bdb045d7307e63fdf306d0eaf9e843/concepts/studies/ecc/READING.md) | 08a3ea459fb34170d0ee356620b22f0f739526c9 |
| U12-A | [25c2e66](https://github.com/batuhanozgun/agentic-os-search/blob/25c2e6615990c4ad9a8acdd508ae5a6acab95b5d/concepts/studies/ecc/READING.md) | 5ac000dab5f3372d9617549f3702c43e193008d2 |
| U12-B1, OC byte/ID kontrolü ve eşzamanlı EXP-004 yayını | [5852459](https://github.com/batuhanozgun/agentic-os-search/blob/5852459c9dc273f3b7aa2911978883424cd5aca7/concepts/studies/ecc/READING.md) | 0dbad408c96a73b827d26289b9d79f212dcb6248 |

Bu altı tam tarihsel kayıt ve current dosya C6'da birlikte devralınır. Bu tur altısının tamamı yeniden okunmuş sayılmaz; önceki konuşmada görülen tam/değişmemiş kayıtlar ve actual compare kullanıldı. Current yüzeyin kısaltılması kapsam/yorum geçmişini silmez. Önceki TERMS dosyaları değişmedi.

Önceki **b6df4013a0f8275da82d6f27a2cd354201c5c70b** package tree ve 60 root + 27 notes + 68 evidence + 4 inventory = 159 dosya hesabı tarihsel baseline'dır. U13-A eklenmesi sonrasında current whole-package envanteri gibi kullanılamaz. Yeni tree/yaprak census bu B2 aktarımının tamamlanmış işi değildir.

## 2. Güncel partition

| Bölüm | Concepts aktarımı | Kullanım dosyası / kimlikler |
|---|---|---|
| C1 / U01–U02 | Durable-complete; korunur | TERMS-SURFACES-INSTALLATION.md; S01–S56 |
| C2 / U03–U04 | Durable-complete; korunur | TERMS-WORK-EXECUTION-MEMORY.md; W01–W89 |
| C3 / U05–U06 | Durable-complete; korunur | TERMS-LEARNING-GOVERNANCE.md; L01–L104 |
| C4 / U07–U09 | Durable-complete; korunur | TERMS-REVIEW-RUNTIME-OPERATOR.md; R01–R176 |
| C5a / U10-A/B | Complete; korunur | TERMS-EVALUATION-REGISTRY.md E01–E50; TERMS-OFFLINE-CAPSULES.md O01–O69 |
| C5b / U11-A | Complete; korunur | TERMS-NATIVE-REVIEW.md; N01–N77 |
| C5b / U11-B | Complete; korunur | TERMS-SCHEDULED-WORK.md; SC01–SC61 |
| C5b / U11-C | Complete; korunur | TERMS-REMOTE-REQUESTS.md; RD01–RD70 |
| C5b / U11-D | Complete; korunur | TERMS-BACKLOG-COORDINATION.md; BC01–BC70 |
| C5b / U11-E | Complete; C5b complete | TERMS-TEMPLATE-LAUNCH.md; TL01–TL74 |
| C5c / U12-A | Complete; korunur | TERMS-EXECUTION-PROFILES.md; EP01–EP84 |
| C5c / U12-B1 | Complete; korunur | TERMS-OPENCODE-CALLBACKS.md; OC01–OC92 |
| C5c / U12-B2 | Bu tur transfer complete; U12-B combined transfer complete | TERMS-OPENCODE-INSTALLATION.md; OD01–OD91 |
| C5c / U12-C | NEXT; gövdeleri/ham kanıtı bu tur okunmadı | Note27, kaynak/tur/yayın ve mevcut E09 |
| C6 / paket geneli | Bekliyor; source delta açık | Altı tarihsel READING + current, bütün TERMS, history/inventory/evidence ve güncel değişimler |

Bütün kullanım kimlikleri ECC- öneki taşır. Sayılar kavram/bağımsız kanıt/ilerleme yüzdesi değildir. C5a/b/c mevcut C5'in yürütme dilimleridir. U12-B aktarımı source-family kapanışıdır; C5c/C5/C6/ECC paket kapanışı değildir.

## 3. U12-B2 gerçek okuma manifesti

Yollar research/studies/ecc/ tabanına göre, §1 snapshot'ına bağlıdır. FULL yalnız bu research dosyalarının okunmasıdır; atfedilen upstream source/test dosyalarının bu tur yeniden okunması değildir.

| Yol | Git blob | Gerçek okuma |
|---|---|---|
| notes/26-OPENCODE-INSTALLATION-LOADING-AND-TOOL-RESULTS.md | 46576b4c8c7df5c2b2eefbe2288b00c493e67bb5 | FULL; 1–70 + 71–160 isteğiyle EOF |
| evidence/U12-B2-SOURCES.md | 39b5e39d01d8b0dcaad4fb5d1930f668031ef416 | FULL; 1–55 + 56–150 isteğiyle EOF |
| ROUND-U12-B2.md | ded88f931216d522b8a77f15c84bfe2379607b2a | FULL; 1–130 isteğiyle EOF |
| PUBLICATION-U12-B2.md | c1979d0faf434bfdcbf781368868e651e1fa7fde | FULL; 1–130 isteğiyle EOF |

N26'nın mevcut CONSENT locator düzeltmesini içeren sürümü okundu; initial fde59999 sürümü yeni tam kaynak diye sayılmadı. B1/B2'nin sekiz direct tool/barrel kapsamı özgün araştırmanın kapsamıdır; yeni upstream code/build/test/install/npm pack veya model deneyi yapılmadı. Aynı note/ledger/round/receipt dört bağımsız evidence değildir. U12-C'nin E09'u bu unit'e aktarılmadı veya yeniden koşulmadı.

**Preflight ve bağlam:** AGENT fresh tam okundu ve aea3dd845e0f0bbcfb34465edb23782e99f95c80 ile eşleşti. R04/R05/R07/R08/R09 tam canonical içerikleri yeniden alındı; R04 ve R09 kesilen sonları örtüşen aralıklarla tamamlandı. Bu konuşmada görünen tam R01/R02/R03/R06 sürümleri korundu; giriş karşılaştırmasında agent-control değişikliği yoktu. Concepts INDEX yeniden FULL okundu (b7e19deb909462a42f6f48508f1cfc1afd987000). CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE, current STATE/READING/TERMS ve source META/INDEX'in görünen tam/değişmemiş konuşma okumaları devralındı. Tarihsel preflight'lar yeni-oturum başarısı kanıtı sayılmadı; control materyali kullanım korpusuna katılmadı.

Source STATE, eşzamanlı değişiklik görülünce ayrıca FULL geri kazanıldı: **564461b06eaf34f5b27c0349a32e1cc1b7ef0f7d**, U13-A IN PROGRESS; gözlenen ref **d7e7a0caf051cd9e70193a5ae62383333a3cb7f2**. Bu source-context okumasıdır; U13-A içerik çıkarımı veya source research devamı değildir.

## 4. Kaynak-kayıt kontrolü ve yorum izi

Yeni [TERMS-OPENCODE-INSTALLATION.md](TERMS-OPENCODE-INSTALLATION.md), **ECC-OD01–OD91**. Her kullanım kaynak bölümü/locator ve K/V/B/Y/T rolüyle bağlıdır. N26 §1–8'den kayda coverage eşlemesi §9'da, ilişki ve yorum izi §10'dadır.

Başlıca ayrımlar: package contents/selected entry; compiled payload/source-plugin route; copy digest/host-sonrası dependency değişikliği; declined consent/classifier coverage; file-origin identity/export identity; path confinement/canonical-legacy role; başarılı write/surviving payload; manifest inventory/command recommendation/report comparison/Git query/bounded scan; default-zero/measured-zero; command error/clean status.

B1 OC82–OC92'nin kaynak sorumlulukları actual caller/materializer/loader ile bağlandı. OC11'in registration düzeyindeki dependency-analyzer işareti implementation anlamıyla ayrıntılandı; OC10 iki-tool map'i bütün sekiz-tool kataloğuyla eşitlenmedi. Callback return/mutable-output bulgusu veya optional-store sınırı geriye dönük değiştirilmedi. Default disjoint roots, classified-hook removal, explicit-conflict refusal, precheck/path/hash ve yararlı gerçek Git/scan yolları olumlu karşılıklar olarak korundu.

Taslakta materialization filtresi/.npmignore ve success:true/öneri metni ayrı adreslendi: OD17/OD90, OD65/OD91. Bu ilk remote yayından önceki aktarım açıklığıdır; yayımlanmış eski kaydın düzeltilmesi veya yeni ürün bulgusu değildir. Önceki TERMS dosyalarını değiştirmeyi gerektiren maddi çelişki saptanmadı. MR27'nin cleanup tüketicisiyle değişen araştırmacı açıklaması tarihsel statüsüyle taşındı.

Same-root cleanup, retained plugin ve duplicate-origin örnekleri koşullu source sonuçlarıdır; migration, canlı consent bypass veya double-run deneyi yapılmadı. Q02b3 ve Q03c açık kalır. Kullanıcı okuma anındaki anlam seçimlerini denetleyemediğinden önemli dayanak/yorum izlenebilir tutuldu; ortak sözcük ortak anlamı garanti etmez, kaynak/araştırmacı/extractor/kullanıcı onayı teknik doğruluk bakımından ayrı kalır.

## 5. Yayın, correspondence ve eşzamanlı source delta

Yeni TERMS commit: **b5b4afa2e9b7ed7c76914f7fdf31991644bbeb3d**. Hazırlanmış local final içerik **32,293 UTF-8 bytes / 183 satır**, Git blob **c100cb12c73676c5d4f9946785b153d80eb48f07**; remote fetch aynı blob'u verdi. Local mekanik kontrol 91 sıralı/unique ID, OD01–OD91 gapsiz, duplicate yok, her kullanım satırında üç kolon ve final newline gösterdi. Bu yalnız yeni TERMS byte/şekil kontrolüdür; bütün-repo link/ID suite'i veya semantik bağımsızlık değildir.

Remote tam içerik 1–65, 66–130 ve 120–210/EOF ile okundu. 66–130 görünümü son kısımda kesildi; 120–EOF örtüşmesi eksiği kapattı. Tam görülen final içerik ve eşleşen blob birlikte kullanıldı. B2 kaynak dosyalarının local raw checkout olarak indirildiği iddia edilmez; yerel metin/hash idaresi ECC deneyi değildir.

**Yeni source delta:** 2db53e57→d7e7a0ca aralığında bağımsız ECC çalışması **ROUND-U13-A.md ekledi ve research/studies/ecc/STATE.md'yi değiştirdi**. Dört B2 kaynağı değişmedi; bunların pin'li aktarımı geçerliliğini korur. Source STATE artık U13-A IN PROGRESS der. Yeni ROUND'un gövdesi bu tur okunmadı/çıkarılmadı. Source META/INDEX'teki eski NOT STARTED yönlendirmeleri source STATE'i geçersiz kılmaz ve bu Concepts işiyle kaynak dosyaları düzeltilmez.

C6, bu iki yolu ve sonradan gelecek source değişikliklerini tam güncel manifestle yeniden karşılaştırmalı; U13-A'yı örtük dışlayarak 159 dosyalık baseline'dan package closure vermemelidir. Bu açık delta sorumluluğudur; Concepts U13-A teknik araştırmasını başlatmaz. B7'nin agentmemory/claude-swap/cli-continues/ponytail post-S1 hesabı da korunur.

Bu READING, TERMS router ve global STATE yazılarının final compare/current-ref/readback kontrolü kapanışta yapılır. Kendi gelecekteki hash veya henüz yapılmamış kontrol uydurulmaz. Eski tarafların tarihsel kayıtları immutable snapshot'larda kalır. Aynı-assistant source-to-record ve publication kontrolü, bağımsız araştırma veya ürün doğrulaması değildir.

## 6. Exact next

**B6-T17-C5c / U12-C:** research/studies/ecc/notes/27-PYTHON-PROVIDER-SELECTION-AND-TOOL-ROUNDTRIPS.md → evidence/U12-C-SOURCES.md → ROUND-U12-C.md → PUBLICATION-U12-C.md → evidence/u12-c-python-flow-probe/README.md ve PRECHECK.md → mevcut E09.zip.b64 kapsamı.

Amaç mevcut selection/provider/tool round-trip kullanımlarını ve E09'un kayıtlı kanıt sınıfını çıkarmaktır. E09 recovery gerekirse mevcut corrected taşıyıcı kullanılır; source STATE'in belirttiği **02441842546271f10050f0f5d4257235b972f113** blob'u tarihsel bozuk yüklemeyle karıştırılmaz. Bu tur Note27 veya raw E09 okunmadı/çözülmedi; byte kimliği bilmek içerik okuması değildir. Yeni provider/model çağrısı veya deney koşusu yoktur.

C5c sonrası C6: altı tarihsel READING + current, bütün ECC TERMS, kalan history/inventory/evidence ve §5 güncel source delta. ECC sonrası sıra work-management-project-control; B7 geçmeden B8 ortak referans başlamaz. Foundation/SOUL/Development OS mimarisi ve kaynak U13-A araştırması bu aktarımın işi değildir.
