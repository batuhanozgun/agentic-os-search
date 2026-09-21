# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-21 · **B6-T17-C5c / U12-A–B1 TRANSFER-COMPLETE / C5c-PARTIAL / C5-PARTIAL / PACKAGE-PARTIAL**.

Bu dosya Concepts okuma/aktarım durumudur. [TERMS.md](TERMS.md) kullanımları, [global STATE](../../STATE.md) programın current/next işini taşır. ECC source-study ACTIVE/PARTIAL; U12-C / plan 0.29'a kadar yayımlanmış ve U13-A/Q07d1 NOT STARTED. Concepts onun yeni araştırmasını başlatmaz. Bu checkpoint U12-B1 aktarımıdır; U12-B2/C ve C6 kapanışı değildir.

## 1. Kaynak kimliği ve korunmuş tam geçmiş

- Research repository: batuhanozgun/agentic-os-search.
- U12-B1 giriş main/snapshot: **25c2e6615990c4ad9a8acdd508ae5a6acab95b5d**; U12-A final kapanışıyla compare-identical.
- Kaynak paket: research/studies/ecc/.
- Korunan ECC package tree: **b6df4013a0f8275da82d6f27a2cd354201c5c70b**. Giriş ve yayın öncesi karşılaştırmalarında kaynak paket değişmedi; yeni whole-package census yapılmadı.
- Ayrı ECC research pin: **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a**.
- Kaynak araştırmanın host karşılaştırması: **anomalyco/opencode v1.4.3 / 877be7e8e04142cd8fbebcb5e6c4b9617bf28cce**. Nested lock etiketiyle seçilmiş kaynak sürümüdür; registry bytes, installed binary veya latest değildir.
- Ayrı indexed observation: **07756cee15788a54506031462794ad645719b028**. ECC pin'i veya current release yerine geçmez.
- Concepts METHOD v0.3-working, SCOPE S1 ve açık post-S1 delta hesabı korunur.

Önceki exact manifestler, yorum düzeltmeleri, evidence istisnaları ve yayın kayıtları aşağıdaki **tam değişmez dosyalarda** korunur; özetle veya yeni current-next ile değiştirilmez:

| Kapsam | Değişmez tam READING | Git blob |
|---|---|---|
| C1–C4 / U01–U09 | [753a4c6](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/studies/ecc/READING.md) | a027c7cb71f06de5355fcb4783f9a0a88d581c0c |
| C5a/U10, U11-A/E08 ve U11-B | [f0d9ae3](https://github.com/batuhanozgun/agentic-os-search/blob/f0d9ae31062459cf7b2cd982eaf484cbdfc336e8/concepts/studies/ecc/READING.md) | 0c740a10a604774ce8c1df4a967a419de69c6ca5 |
| U11-C/D exact manifestleri ve yayın ayrıntıları | [eb7754b](https://github.com/batuhanozgun/agentic-os-search/blob/eb7754b34953b57b9c1aeb92ef4885993ded7ca2/concepts/studies/ecc/READING.md) | 8b1ebc35fd4c5c2e20a9395f9f45f9599428b3a8 |
| U11-E manifesti, aktarım düzeltmeleri ve C5b kapanışı | [df7b81a](https://github.com/batuhanozgun/agentic-os-search/blob/df7b81a8f0bdb045d7307e63fdf306d0eaf9e843/concepts/studies/ecc/READING.md) | 08a3ea459fb34170d0ee356620b22f0f739526c9 |
| U12-A manifesti, EP kayıt ayrımları ve yayın kontrolü | [25c2e66](https://github.com/batuhanozgun/agentic-os-search/blob/25c2e6615990c4ad9a8acdd508ae5a6acab95b5d/concepts/studies/ecc/READING.md) | 5ac000dab5f3372d9617549f3702c43e193008d2 |

Son satır bu dosyanın girişteki tam sürümüdür; aynı konuşmada tam okunmuş içerik ve girişteki identical karşılaştırma korunur. Bu tur bütün geçmiş yeniden okunmuş sayılmaz. C6 **beş tam tarihsel READING ve current dosyayı**, ilgili TERMS ve actual source inventory ile birlikte devralır. Tarihsel next/PARTIAL ifadeleri bugünkü authority değildir. Önceki TERMS ve kaynak dosyaları değiştirilmedi.

Önceki inventory hesabı 60 root + 27 notes + 68 evidence + 4 inventory = 159 dosyadır. Bu sayı bu tur yeniden sayılmadı; semantik tamlık veya ilerleme yüzdesi değildir. Concepts/ECC directory discovery yanıtı kesildi; tam directory census veya yokluk kanıtı sayılmadı.

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
| C5b — U11-E | Transfer complete; C5b complete | TERMS-TEMPLATE-LAUNCH.md; TL01–TL74 |
| C5c — U12-A | Transfer complete; korunur | TERMS-EXECUTION-PROFILES.md; EP01–EP84 |
| C5c — U12-B1 | Bu tur transfer complete | TERMS-OPENCODE-CALLBACKS.md; OC01–OC92 |
| C5c — U12-B2 | Sıradaki exact next; gövdesi okunmadı | Note26 installation/loading/tool-result |
| C5c — U12-C | Bekliyor | Python/provider/tool-roundtrip ve E09 |
| C6 — package-wide reconciliation | Bekliyor | History/inventory/evidence, bütün TERMS ve source delta |

Bütün kullanım kimlikleri ECC- öneki taşır. C5a/b/c mevcut C5'in yürütme dilimleridir; yeni phase veya kapsam dışlama kararı değildir. **C5b complete korunur; C5c, C5 ve ECC Concepts paketi tamamlanmadı.** U12-B1'in source dosyalarındaki U12-B PARTIAL tarihsel checkpoint'i current source-study'ye geri taşınmaz: source-study Notes25–26'yı yayımlamıştır, Concepts ise B2'yi henüz aktarmadı.

## 3. U12-B1 gerçek okuma manifesti

Yollar research/studies/ecc/ tabanında, §1 giriş snapshot'ına bağlıdır. FULL bu research dosyasının tamamıdır; atfedilen upstream kaynakların bu tur okunması veya çalıştırılması değildir.

| Yol | Git blob | Gerçek okuma |
|---|---|---|
| notes/25-OPENCODE-CALLBACK-CONTRACTS-AND-GENERATED-ENTRY.md | 2d2bed97f3189db10e5ac6665086c69e3d0f6367 | FULL; 1–85 isteği EOF'a ulaştı |
| evidence/U12-B1-SOURCES.md | 377906978b712c37381ab91586cd6f1c99e292d3 | FULL; 1–95 isteği EOF'a ulaştı |
| ROUND-U12-B.md | ef7630af230b2117013d31f84df41feae87a8239 | FULL; 1–130 isteği EOF'a ulaştı |
| PUBLICATION-U12-B1.md | 744d87b284f3aa177bff67b76c12fb814ed0bd7b | FULL; 1–130 isteği EOF'a ulaştı |

Bu inquiry yeni deney içermez. Hook/build testleri araştırmada incelenmiş tanımlardır; Concepts'te yeni compiler, npm pack, host/model, fixture veya target execution yapılmadı. Araştırmanın versioned host incelemesi ve dated W-B1-DOC atfı yeni current product doğrulaması değildir. E08/E07 ve sonraki Python E09 bu plugin'in deneyine çevrilmedi.

**Preflight:** AGENT fresh tam okundu; aea3dd845e0f0bbcfb34465edb23782e99f95c80 değişmedi. R01, R02 ve R03 tam canonical içerikleri yeniden geri kazanıldı; R01 1–140/141–310, R03 1–165/166–400 ile EOF'a tamamlandı. R04–R09'un ve mandatory Concepts INDEX/STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE, local READING/TERMS ve ECC META/STATE/INDEX'in aynı konuşmadaki tam içerikleri korundu. Başlangıç main identical olduğundan değişmemiş dosyalar mekanik tekrarlanmadı. Control dosyaları kullanım korpusuna katılmadı.

## 4. Kaynak–kayıt ve yorum kontrolü

Yeni [TERMS-OPENCODE-CALLBACKS.md](TERMS-OPENCODE-CALLBACKS.md) **ECC-OC01–OC92** kayıtlarını N25 §1–8 ve ledger/round/receipt kapsamıyla bağlar. K/V/B/Y/T/H; ECC kod raporu, versioned host sözleşmesi, hedef beyanı, araştırmacı yorumu, incelenmiş test ve tarihli dokümanı ayırır. Türkçe metinler extractor paraphrase'idir. Kaynak tarafından bölüm-kayıt eşlemesi TERMS §9, ilişki/yorum izi §10'dadır.

Başlıca ayrımlar: plugin entry/catalog installation; root/nested/indexed/source/installed identity; callback invocation/consumed output; returned replacement/mutable supplied output; event name/event subscription; before output.args/after input.args; direct test oracle/host dispatcher; custom-tool return/lifecycle callback return; tracked map/complete per-session history; optional feature failure/global module startup; preparation path checks/transitive payload completeness.

Olumlu yollar da korundu: default plugin-only export, gerçek after-hook args ve tool return consumer, lazy optional-store import/guard/retry fırsatı ve missing/system-error ayrımı. Callback uyumsuzluğu total memory loss, permission bypass veya bütünüyle işlevsiz plugin hükmüne yükseltilmedi. Permission gözlemi ilgili trigger invocation kapsamındadır; host'un her permission call-site'ı araştırılmış sayılmaz.

İki önemli yorum sınırı ayrıca işlendi. Birincisi, B1'den B2'ye kalan source work yalnız daha güçlü canlı doğrulama eksiği diye sınıflandırılmadı; mevcut B2 çıktısı bir sonraki Concepts aktarımıdır. İkincisi, MR26'nın lazy/type-only import okumasından sonra terk ettiği static-import şüphesi OC75'te tarihsel araştırmacı değişimi olarak tutuldu; bu turun kendi keşfi/düzeltmesi diye sunulmadı. Önceki TERMS'i yeniden yazmayı gerektiren maddi çelişki saptanmadı.

Yeni dosyada iki TypeScript type ifadesine Markdown code-span eklendi; bu biçim korumasıdır, anlam veya kullanım-ID değişimi değildir. İlk/final bytes ve actual diff aşağıda ayrılır. Kullanıcı anlam seçimlerini okuma anında denetleyemediği için önemli dayanak ve yorum sınırları görünürdür; aynı sözcük ortak anlamı garanti etmez, kaynak/araştırmacı/extractor/kullanıcı onayı teknik doğruluk bakımından ayrı kalır.

## 5. Gerçek yayın, byte kontrolü ve eşzamanlı çalışma

- İlk TERMS commit: **4517b5431d2ee5070d6a4dd8cca50e14ae8564d0**. Local prepared file **31,292 bytes / 181 lines**, Git blob **98feb0302d61ce513850d16186a95570464c0ec5**; remote fetch aynı blob'u verdi.
- Markdown type-spelling düzeltmesi: **f9291e2041e24aabf00c804c56824aaf8b042631**. Prepared final **31,296 bytes**, Git blob **25abf0599f129c3c3d0af22d28fe145814fc3180**; update ve final fetch bu kimlikle eşleşti. Actual diff yalnız OC25 ve OC55'e code-span ekledi.
- Okuma karşılığı: initial 1–60; final 61–125 ve 126–205 üzerinden EOF; ilk aralıktaki OC25 değişimi actual diff ile ayrıca görüldü. Full final prepared content ve remote blob equality birlikte kontrol edildi; farklı revizyon aralıkları tek ham fetch gibi sunulmaz.
- Local mekanik kontrol **92 sıralı/unique kayıt, OC01–OC92 gap yok, duplicate yok**, her kullanım satırında üç kolon ve final newline gösterdi. Type ifadelerinin yerel Markdown yorumuna bakıldı. Bu kontroller target test veya bağımsız semantik doğrulama değildir.

Byte equality yalnız bu yeni TERMS'in hazırlanmış ve yayımlanmış içeriği içindir; source files'ın yerel raw download edildiği veya tüm repo hash/link suite'i çalıştığı iddia edilmez. Eski erişim hataları bu turun hatası değildir.

Giriş25c2e66→main karşılaştırması entry yazılarından önce **42 commit** gösterdi: bu turun iki yeni-TERMS commit'i ve bağımsız explorations değişimleri. EXP-004 paketi ile explorations INDEX/CATALOG değişimleri korunur; bu Concepts çalışmasına mal edilmez. Control, source ECC ve üç current Concepts entry dosyası o karşılaştırmada değişmemişti. Ref okuması **f9291e2041e24aabf00c804c56824aaf8b042631** verdi; eşzamanlı çalışmalar bu commit'in geçmişine dahil olduğundan eski köke force dönüş yapılmaz. Contents/SHA kontrollü devam yalnız yetkili Concepts entry'lerini değiştirir.

Bu READING/router/global STATE yazılarından sonra final ref/diff ve current-entry readback ayrıca yapılır. Bu metin kendi gelecekteki hash'ini veya henüz yapılmamış kontrolü uydurmaz. Fresh-session devralma kontrolü mevcut canonical yönlendirmelerin aynı-assistant kontrolüdür; bağımsız oturum deneyi değildir.

## 6. Exact next ve açık kapsam

**B6-T17-C5c / U12-B2:** research/studies/ecc/notes/26-OPENCODE-INSTALLATION-LOADING-AND-TOOL-RESULTS.md → evidence/U12-B2-SOURCES.md → ROUND-U12-B2.md → PUBLICATION-U12-B2.md. Gerekli bağlı evidence aynı kaynak kapsamıyla okunur. Bu tur Note26 gövdesi okunmadı; yol mevcut source INDEX'ten bilinir.

Amaç mevcut araştırmadaki root/nested/package identity, managed install/config rewriting, host loader, materialized imports ve tool-result kullanımlarını çıkarmaktır. Build, installation veya yeni host/model testi değildir. Ardından U12-C/Python ve mevcut E09 gelir.

C5c bitince C6, §1'deki **beş tam tarihsel READING ve current dosya**, bütün ECC TERMS, kalan master-history/inventory/evidence, source delta ve paket geneli source-to-record/ID/role hesabını yapar. B1 closure bu işi veya B2'yi yerine getirmez. Post-S1 additions agentmemory, claude-swap, cli-continues, ponytail B7 öncesi global kapsam hesabında kalır; ECC sonrası paket work-management-project-control'dür.

Q02b3 ve önceki güçlü runtime/authority/acceptance soruları Concepts tarafından çözülmedi veya otomatik deney borcu yapılmadı. E06 excluded; iki E05 geçmişi ve E04/E07/E08/E09 ayrı scope'larında korunur. B7/B8, Foundation/SOUL/Development OS mimarisi ve source-study U13-A bu checkpoint'in işi değildir.
