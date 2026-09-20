# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-20 · **B6-T17-C5c / U12-A TRANSFER-COMPLETE / C5c-PARTIAL / C5-PARTIAL / PACKAGE-PARTIAL**.

Bu dosya Concepts okuma ve devam durumudur. [TERMS.md](TERMS.md) kullanımları, [global STATE](../../STATE.md) programın current/next işini taşır. ECC source-study ACTIVE/PARTIAL; U12-C / plan 0.29'a kadar yayımlanmış ve U13-A/Q07d1 NOT STARTED. Concepts onun yeni araştırmasını başlatmaz. Bu checkpoint U12-A kullanım aktarımıdır; U12-B1/B2/C ve C6 kapanışı değildir.

## 1. Kaynak kimliği ve korunmuş tam geçmiş

- Research repository: batuhanozgun/agentic-os-search.
- U12-A giriş main/snapshot: **df7b81a8f0bdb045d7307e63fdf306d0eaf9e843**; önceki U11-E final kapanışıyla compare-identical.
- Kaynak paket: research/studies/ecc/.
- Korunan ECC package tree: **b6df4013a0f8275da82d6f27a2cd354201c5c70b**. Girişte intervening repository değişikliği yoktu; yeni whole-package census yapılmadı.
- Ayrı upstream research pin: **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a**. Research snapshot'ı, upstream pin ve installed runtime farklı nesnelerdir.
- Concepts METHOD v0.3-working, SCOPE S1 ve açık post-S1 delta hesabı korunur.

Önceki exact manifestler, yorum düzeltmeleri, evidence istisnaları ve yayın kayıtları aşağıdaki **tam değişmez dosyalarda** korunur. Bunlar yalnız özet veya yeni current-next değildir:

| Kapsam | Değişmez tam READING | Git blob |
|---|---|---|
| C1–C4 / U01–U09 | [753a4c6](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/studies/ecc/READING.md) | a027c7cb71f06de5355fcb4783f9a0a88d581c0c |
| C5a/U10, U11-A/E08 ve U11-B | [f0d9ae3](https://github.com/batuhanozgun/agentic-os-search/blob/f0d9ae31062459cf7b2cd982eaf484cbdfc336e8/concepts/studies/ecc/READING.md) | 0c740a10a604774ce8c1df4a967a419de69c6ca5 |
| U11-C ve U11-D exact manifestleri, source-to-record ve yayın ayrıntıları | [eb7754b](https://github.com/batuhanozgun/agentic-os-search/blob/eb7754b34953b57b9c1aeb92ef4885993ded7ca2/concepts/studies/ecc/READING.md) | 8b1ebc35fd4c5c2e20a9395f9f45f9599428b3a8 |
| U11-E exact manifesti, ilk aktarım/düzeltmeler ve C5b kapanışı | [df7b81a](https://github.com/batuhanozgun/agentic-os-search/blob/df7b81a8f0bdb045d7307e63fdf306d0eaf9e843/concepts/studies/ecc/READING.md) | 08a3ea459fb34170d0ee356620b22f0f739526c9 |

Df7b81a içeriği önceki turda tam geri okunmuştu; yeni giriş identical ve bu dosya güncellemesi aynı blob'a SHA kontrollüdür. Bu tur bütün tarih yeniden okunmuş sayılmaz. C6, bu dört tam tarihsel kaydı ve current dosyayı birlikte devralır; scope/role/ID hesabını yalnız current tablodan kapatmaz. U11-E'nin TL38/TL74, TL50/TL73 ve TL72 düzeltmeleri kendi TERMS §10'unda da korunur. Önceki TERMS ve kaynak dosyaları bu tur değiştirilmedi.

Önceki inventory hesabı 60 root + 27 notes + 68 evidence + 4 inventory = 159 dosyadır. Bu sayı bu tur yeniden sayılmadı; semantik tamlık veya ilerleme yüzdesi değildir.

## 2. Güncel partition

| Bölüm | Concepts durumu | Kullanım dosyası / kimlikler |
|---|---|---|
| C1 — U01–U02 | Durable-complete; korunur | TERMS-SURFACES-INSTALLATION.md; S01–S56 |
| C2 — U03–U04 | Durable-complete; korunur | TERMS-WORK-EXECUTION-MEMORY.md; W01–W89 |
| C3 — U05–U06 | Durable-complete; korunur | TERMS-LEARNING-GOVERNANCE.md; L01–L104 |
| C4 — U07–U09 | Durable-complete; korunur | TERMS-REVIEW-RUNTIME-OPERATOR.md; R01–R176 |
| C5a — U10-A/U10-B | Transfer complete; korunur | TERMS-EVALUATION-REGISTRY.md E01–E50; TERMS-OFFLINE-CAPSULES.md O01–O69 |
| C5b — U11-A | Transfer complete; korunur | TERMS-NATIVE-REVIEW.md; N01–N77 |
| C5b — U11-B | Transfer complete; korunur | TERMS-SCHEDULED-WORK.md; SC01–SC61 |
| C5b — U11-C | Transfer complete; korunur | TERMS-REMOTE-REQUESTS.md; RD01–RD70 |
| C5b — U11-D | Transfer complete; korunur | TERMS-BACKLOG-COORDINATION.md; BC01–BC70 |
| C5b — U11-E | Transfer complete; korunur; C5b complete | TERMS-TEMPLATE-LAUNCH.md; TL01–TL74 |
| C5c — U12-A | Bu tur transfer complete | TERMS-EXECUTION-PROFILES.md; EP01–EP84 |
| C5c — U12-B1/B2 | Sırada; ilk Note25 | Generated OpenCode entry ve installation/loading/tool-result |
| C5c — U12-C | Bekliyor | Python/provider/tool-roundtrip ve E09 |
| C6 — package-wide reconciliation | Bekliyor | History/inventory/evidence, bütün TERMS ve source delta |

Bütün kimlikler ECC- öneki taşır. C5a/b/c mevcut C5'in yürütme dilimleridir; yeni phase veya kapsam dışlama kararı değildir. **C5b complete korunur; C5c, C5, ECC Concepts paketi ve ECC source-study tamamlanmadı.** Bu tur U12-B1/B2/C gövde okuması başlamadı.

## 3. U12-A gerçek okuma manifesti

Aşağıdaki yollar research/studies/ecc/ tabanında, §1 giriş snapshot'ına bağlıdır. FULL bu araştırma dosyasının tamamıdır; içinde atfedilen upstream kaynakların bu tur okunması/çalıştırılması değildir.

| Yol | Git blob | Gerçek okuma |
|---|---|---|
| notes/24-EXECUTION-PROFILES-AND-HARNESS-CONSUMERS.md | 2d228fca57f5fcdc8bbbce955fcde4a4a03b42f9 | FULL; 1–65 ve 66–140 isteğiyle EOF |
| evidence/U12-A-SOURCES.md | befcad04dfc6f00d2210b0f9c67a43239b6925ce | FULL; 1–70 isteğiyle EOF |
| ROUND-U12-A.md | baca22dc3226d07f42e7a50bd4a4dd15e7669ee2 | FULL; 1–110 isteğiyle EOF |
| PUBLICATION-U12-A.md | 0d53d1a221414ee75ee8405c44870fbb71f93abf | FULL; 1–115 isteğiyle EOF |

U12-A source-only inquiry'dir. Dated host/process sözleşmeleri araştırmanın **2026-09-19** tarihli atıflarıdır; güncel installed binary/API/host behavior doğrulaması değildir. Upstream command tests araştırmada incelenmiş fakat koşulmamıştır; bu Concepts turunda test gövdeleri ayrıca yeniden okunmadı. Ayrı raw run veya E09 burada varmış gibi üretilmedi. E08/E07 ve sonraki Python E09 profile/host deneyine dönüştürülmedi.

**Preflight:** AGENT fresh tam okundu ve aynı aea3dd845e0f0bbcfb34465edb23782e99f95c80 kimliğindeydi. R01–R09'un, Concepts INDEX/STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE, yerel READING/TERMS ve ECC META/STATE/INDEX'in aynı konuşmadaki tam canonical içerikleri korundu. Giriş compare-identical olduğundan değişmemiş dosyalar mekanik tekrar edilmedi. Bu yeni oturum deneyi veya önceki okumaların bağımsız doğrulaması değildir. Control materyali kullanım korpusuna katılmadı.

## 4. Kaynak–kayıt kontrolü ve yorum izi

Yeni [TERMS-EXECUTION-PROFILES.md](TERMS-EXECUTION-PROFILES.md) **ECC-EP01–EP84** kullanımını N24 §1–8 ve LA kaynak/consumer/test/dış sözleşme kapsamıyla bağlar. K/Y/T/H rolleri code-report, eski araştırmacı yorumu, inspected test ve dated external contract'ı ayırır. Türkçe açıklamalar extractor paraphrase'idir. Kaynak tarafından bölüm-kayıt eşlemesi TERMS §10, ilişki ve düzeltme izi §11'dedir.

Başlıca ayrımlar: resolved profile/stored session harness/execution identity; native argument/task text/host enforcement; allowed-tools preapproval/tools availability; configured recipe replacement/additive customization; native flag presence/actual support; per-profile tokens/global USD/per-profile USD; sampled recorded-usage check/pre-spend admission; malformed decoded-empty/explicit-empty; shared environment label/explicit runtime session_id; marker discovery/active capability.

Olumlu mekanizmalar korundu: scalar/list/prompt composition, effective harness'ın session'da saklanması, worker'ın stored profile okuması, native mapping, unsupported intent'in text'te korunması, configured extension, normal JSON serialization, program refusal ve gerçek TUI/CLI bütçe caller'ları. Native token flag yokluğu alanın tüketilmediği sonucu yapılmadı; gerçek ECC enforcer da her profilin dolar tavanını uyguluyormuş gibi gösterilmedi.

**İlk aktarımın düzeltmesi:** EP29 iki ayrı host izin yüzeyini, EP33 program/base_args girdilerini tek kullanım adresinde taşıyordu. N24 §3–4/LA üzerinden EP29 OpenCode, EP84 Gemini; EP33 program, EP83 base_args olarak ayrıldı. Kaynak eşlemesi ve sıkıştırılmış açıklama düzeltildi. EP16/EP17/EP30–EP36/EP74/EP81 etki kontrolü yapıldı; diğer açıklamalar değişmedi. İlk yayın f1dc836 ve gerekçe TERMS §11'de korunur. Bu bir extractor adresleme düzeltmesidir; yeni host bulgusu değildir.

Önceki TL35 selection/persistence işareti yeni EP kayıtlarına bağlanır, fakat Q02a2 enforcement açık kalır. TL37'nin Stale'i kapasitede sayması, EP58'in stop hedeflerinden dışlamasıyla aynı nüfus değildir. RD reuse'a yeni profil uygulaması eklenmiş sayılmaz; R88 effectful observer ve R95/R96 stop/cleanup kapsamı korunur. Önceki kullanım dosyalarını yeniden yazmayı gerektiren maddi çelişki saptanmadı.

İki riskin somut karşılığı: Batu okuma anındaki anlam seçimlerini denetleyemediği için dayanak/yorum/düzeltme izlenebilir olmalı; aynı sözcük ortak anlam veya teknik doğruluk sağlamaz. Kaynak kullanımı, araştırmacı/extractor yorumu ve kullanıcı onayı birbirinin doğrulaması değildir.

## 5. Gerçek yayın ve kontrol kapsamı

- İlk TERMS commit: **f1dc83651f57fcdaff1074cd0339717624d58fdb**, blob **a9004bb9370d57a25aff3a6aff7d01a805ee71dd**.
- İlk içerik tam readback: **1–68 / 69–124 / 125–220 üzerinden EOF**.
- Adresleme düzeltmesi: **ee91f06721ac5774d596a22bf62556fe3fad0ea7**, blob **480a8decc41d1f11dea5d83b4d46124b46086b32**.
- Düzeltmenin tam actual diff alanı okundu: EP29/EP33, kaynak mapping, açıklama, correction izi/EP83/EP84 ve 82→84 sayımı. Araç yanıtının daha sonraki yinelenen patch/metadata bölümü kesildi; tamamı görülen ilk diff alanı kesilmedi. Başka kullanım satırı değişmedi.
- Df7b81a→main entry yazıları öncesi karşılaştırması **iki commit ve yalnız yeni TERMS dosyasını** gösterdi. Önceki kaynak/control/entry dosyalarında intervening değişiklik bulunmadı.

Bu READING/router/global STATE güncellemelerinin final main/ref/diff/readback kontrolü kapanışta yapılır; metin kendi gelecekteki hash'ini veya henüz yapılmamış kontrolü uydurmaz. Aynı-assistant source-to-record/diff/readback kontrolü yayın/temsil tutarlılığıdır; bağımsız host veya kavram doğrulaması değildir. Otomatik tüm-repo ID/link suite'i, local full-byte/hash equality, yeni target/code/test execution veya bağımsız aktör kontrolü yapılmadı. Bu tur raw download denenmedi; tarihsel erişim hataları güncel hata sayılmadı.

## 6. Exact next ve açık kapsam

**B6-T17-C5c / ilk U12-B1:** research/studies/ecc/notes/25-OPENCODE-CALLBACK-CONTRACTS-AND-GENERATED-ENTRY.md → evidence/U12-B1-SOURCES.md → ROUND-U12-B.md → PUBLICATION-U12-B1.md. Ardından **U12-B2:** notes/26-OPENCODE-INSTALLATION-LOADING-AND-TOOL-RESULTS.md ve U12-B2 source/round/publication kayıtları. Yol/ayrım önceki tam source INDEX'ten gelir; bu tur bu gövdeler okunmadı.

Amaç generated entry, callback/event/output, package/install/load ve tool-result kullanımlarını mevcut araştırmadan çıkarmaktır; build, installation veya canlı OpenCode testi başlatmak değildir. Rust OpenCode argv tarifi EP16 bu ayrı plugin ailesini kapatmaz. Sonra U12-C/Python ve E09'un mevcut kanıtı gelir.

C5c tamamlanınca C6, §1'deki **dört tam tarihsel READING ve current dosya**, kalan master-history/inventory/evidence, bütün ECC TERMS, source delta ve paket geneli source-to-record/ID/role tutarlılığını kapsar. C5b veya U12-A kapanışı C6 yerine geçmez. Post-S1 additions agentmemory, claude-swap, cli-continues, ponytail B7 öncesi global kapsam hesabında kalır; ECC sonrası paket work-management-project-control'dür.

Q02a2 ve önceki güçlü runtime/authority/acceptance soruları Concepts tarafından çözülmedi ve otomatik yeni deney borcu değildir. E06 excluded; iki E05 geçmişi ve E04/E07/E08/E09 kendi scope'larında korunur. B7/B8, Foundation/SOUL/Development OS mimarisi ve source-study U13-A bu checkpoint'in işi değildir.
