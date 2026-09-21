# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-21 · **B6-T17-C5c / U12-C-TRANSFER-COMPLETE / C5c-COMPLETE / C5-U10–U12-COMPLETE / PACKAGE-PARTIAL / C6-NEXT**.

Bu dosya Concepts okuma/aktarım durumudur. [TERMS.md](TERMS.md) kullanım girişini, [global STATE](../../STATE.md) programın amaç/yetki/current-next işini taşır. C5 kapanışı başlangıçta tanımlanmış U10–U12 kaynak-ailelerinin aktarımıdır; bütün ECC dosyalarının veya sonradan eklenen U13 kapsamının kapanışı değildir. Kaynak araştırmanın kendi devam işi Concepts'in teknik araştırma yetkisine dönüşmez.

## 1. Sabit kaynak ve korunmuş tam geçmiş

Bu turun aktarım snapshot'ı **c0fd473bd3d39ff69371261c1de93afe0af8ad9c**, repository **batuhanozgun/agentic-os-search**. Ayrı ECC research pin'i **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a**. U12-C'nin SDK karşılaştırması **OpenAI v1.30.0 / e2214ce7243c027c4e04e39b5a11986d5e361e37**; indexed934195f ayrı keşif sürümüdür. Önceki OpenCode v1.4.3/877be7e ve indexed07756cee bağlamları kendi kayıtlarında korunur. Research snapshot, upstream pin, dependency etiketi ve installed environment aynı kimlik değildir.

Aşağıdakiler önceki **tam değişmez READING dosyalarıdır**, kısa özet veya current-next değildir. Eski exact manifestler, kaynak/yorum ayrımları, düzeltmeler, evidence istisnaları ve yayın kayıtları korunur:

| Kapsam | Tam READING sürümü | Git blob |
|---|---|---|
| C1–C4 / U01–U09 | [753a4c6](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/studies/ecc/READING.md) | a027c7cb71f06de5355fcb4783f9a0a88d581c0c |
| C5a/U10, U11-A/E08 ve U11-B | [f0d9ae3](https://github.com/batuhanozgun/agentic-os-search/blob/f0d9ae31062459cf7b2cd982eaf484cbdfc336e8/concepts/studies/ecc/READING.md) | 0c740a10a604774ce8c1df4a967a419de69c6ca5 |
| U11-C/D | [eb7754b](https://github.com/batuhanozgun/agentic-os-search/blob/eb7754b34953b57b9c1aeb92ef4885993ded7ca2/concepts/studies/ecc/READING.md) | 8b1ebc35fd4c5c2e20a9395f9f45f9599428b3a8 |
| U11-E ve C5b kapanışı | [df7b81a](https://github.com/batuhanozgun/agentic-os-search/blob/df7b81a8f0bdb045d7307e63fdf306d0eaf9e843/concepts/studies/ecc/READING.md) | 08a3ea459fb34170d0ee356620b22f0f739526c9 |
| U12-A | [25c2e66](https://github.com/batuhanozgun/agentic-os-search/blob/25c2e6615990c4ad9a8acdd508ae5a6acab95b5d/concepts/studies/ecc/READING.md) | 5ac000dab5f3372d9617549f3702c43e193008d2 |
| U12-B1 ve eşzamanlı EXP-004 yayını | [5852459](https://github.com/batuhanozgun/agentic-os-search/blob/5852459c9dc273f3b7aa2911978883424cd5aca7/concepts/studies/ecc/READING.md) | 0dbad408c96a73b827d26289b9d79f212dcb6248 |
| U12-B2, OD kontrolü ve U13-A activation delta'sı | [592b11b](https://github.com/batuhanozgun/agentic-os-search/blob/592b11bd726fd39e84e53098507cf5b1a60d92e3/concepts/studies/ecc/READING.md) | 70b7aca07ae7d189937efe4530cf6b326e4f1a8b |

**C6 yedi tam tarihsel kayıt + current dosyayı birlikte devralır.** Bu turun bütün tarihi yeniden okuduğu iddia edilmez. En son B2 kaydı bu tur da 1–65/66–150 üzerinden EOF'a tam geri okundu; aynı blob'du. Önceki kullanım dosyaları yerinde kalır. Tarihsel PARTIAL/next ifadeleri kendi checkpoint'lerine aittir.

Önceki package tree **b6df4013a0f8275da82d6f27a2cd354201c5c70b** ve 60 root + 27 notes + 68 evidence + 4 inventory = 159 dosya hesabı artık yalnız baseline'dır. U13-A/B eklenmeleri varken current census değildir. Bu tur bütün ECC yaprakları yeniden sayılmadı; §6 bu işi açık taşır. METHOD v0.3-working ve SCOPE S1 korunur; post-S1 kapsam hesabı kapanmadı.

## 2. Güncel aktarım ve devam

| Dilim | Durum | Kalıcı kullanım grupları |
|---|---|---|
| C1–C4 / U01–U09 | Durable-complete; korunur | S01–S56, W01–W89, L01–L104, R01–R176 |
| C5a / U10-A/B | Complete; korunur | E01–E50, O01–O69 |
| C5b / U11-A–E | Complete; korunur | N01–N77, SC01–SC61, RD01–RD70, BC01–BC70, TL01–TL74 |
| C5c / U12-A/B1/B2 | Complete; korunur | EP01–EP84, OC01–OC92, OD01–OD91 |
| C5c / U12-C | Bu tur transfer complete | TERMS-PYTHON-PROVIDERS-AND-TOOLS.md; PY01–PY108 |
| C6 / paket geneli | Exact next; kapanmadı | Güncel census, yedi tarihsel READING + current, bütün TERMS, kalan history/inventory/evidence ve U13 dahil delta |

Kimlikler ECC- öneki taşır; dosya girişleri TERMS.md'dedir. Sayılar bağımsız kavram/kanıt veya ilerleme yüzdesi değildir. C5a/b/c ayrı yeni phase değil, mevcut C5'in yürütme dilimleridir. C5c ve C5'in U10–U12 aktarımı complete; **ECC Concepts paketi PARTIAL**, B7/B8 NOT STARTED.

## 3. Bu turdaki yön tazeleme ve actual source manifest

Kullanıcının isteğiyle README, Concepts INDEX/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE canonical içerikleri tam geri kazanıldı. METHOD 1–95 görünümündeki kesinti 75–145 ve 125–190/EOF ile; SCOPE kesintisi 105–210/EOF ile tamamlandı. PLAN 1–60/61–160 üzerinden tam okundu. Güncel STATE, bu READING ve TERMS de yazı öncesi tam geri okundu. Amaç değişmedi: kendi bağlamında kullanım çıkarımı; genel tanım, ürün testi veya mimari yok. Eski hazırlık/pilot ifadeleri current work yapılmadı.

AGENT fresh full, blob **aea3dd845e0f0bbcfb34465edb23782e99f95c80**. R01–R09 LOAD; R06 full canonical yeniden alındı, blob **91a07c45e6956ba51b89dc81d45b25e30a2afc38**. Diğer protokollerin aynı konuşmada görünen tam/değişmemiş sürümleri korundu. Başlangıç karşılaştırmasında agent-control değişmedi; kontrol materyali araştırma korpusuna katılmadı. Bu yeni-oturum efficacy testi değildir.

Yollar aşağıda **research/studies/ecc/** tabanına ve §1 snapshot'ına bağlıdır. FULL yalnız bu research metninin veya belirtilmiş taşıyıcının okunmasıdır; atfedilen bütün upstream body'lerin yeniden okunması değildir.

| Yol | Git blob | Gerçek okuma |
|---|---|---|
| notes/27-PYTHON-PROVIDER-SELECTION-AND-TOOL-ROUNDTRIPS.md | 325d4234370b2019974969b6517c883b2bf3fad4 | FULL; 1–65 + 66–160/EOF |
| evidence/U12-C-SOURCES.md | 900f277fead1d75a581f4e034da59a103cb88dc1 | FULL; 1–75 isteği EOF'a ulaştı |
| ROUND-U12-C.md | 6c36398267263e5335efe10885dbec1c5a1e0965 | FULL |
| PUBLICATION-U12-C.md | 72ad93a2c1ed9757ea5ec493c70a1623ea7d94d4 | FULL |
| evidence/u12-c-python-flow-probe/README.md | e4e5feb757c062f0899f099c439e4b9a3c20bb46 | FULL |
| evidence/u12-c-python-flow-probe/PRECHECK.md | e77ffb78644e74a8db4a884ae1a53164aa19e552 | FULL |
| evidence/u12-c-python-flow-probe/E09.zip.b64 | 02441842546271f10050f0f5d4257235b972f113 | İlk display kesildi; response resource içindeki tam 8801-byte içerik geri kazanılıp Git blob eşliğiyle doğrulandı, decode edildi |

E09 dizininin üç repository girdisi tam listelendi: README, PRECHECK ve encoded bundle. Altı metin + bir carrier, içindeki beş üyenin ayrıca hesabıyla okunmuştur. LC'nin 20 Python body ve üç upstream test hesabı önceki araştırmanındır; bu tur onları tekrar koşmuş/okumuş saymayız. Dated API/SDK/service atıfları current ürün doğrulaması değildir.

## 4. E09 read-only recovery ve kanıtın sınırı

E09 **2026-09-20T00:34:55.313830+00:00 tarihli tek run, sekiz controlled case** olarak korunur. Bu tur probe veya target source import edilmedi/çalıştırılmadı. Normal package/SDK/provider initialization eski deneyde bilinçli dışlanmıştı. ZIP upstream source snapshots içermez.

| Kurtarılan üye | Bytes | SHA256 / gerçek okuma |
|---|---:|---|
| probe.py | 10305 | 0808157f0756bf039f0bfcd7d783dbcbdf13b4017ccd780e74a6b0c6f9cd0744; FULL 1–130 + 131–197 |
| results.json | 16373 | d7900dddbca2e682644b3693a22e8b9a447d494509f8fe94f8217451934be285; FULL 1–190 + 191–415 + 416–615 |
| MANIFEST.json | 848 | 0a2fa8a339ccad479442c7bc9f1a02906ae5be79553a31ee42bd8894d80b94ba; FULL |
| stderr.txt | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; boş içerik doğrulandı |
| exit-code.txt | 2 | 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa; 0 ve newline |

Decoded ZIP **6598 bytes**, SHA256 **f70acdf4df1fd04e1c446f2813d704f3bff5428945e9684acf4fff620e31e08b**. Beklenen beş üye, CRC, manifestteki üye hashleri, source pin, run_count=1, sekiz vaka ve kayıtlı aggregate/check tutarlılığı kontrol edildi. Bunlar arşiv/temsil kontrolleridir; E09 yeniden-performansı veya yeni bağımsız doğrulama değildir.

Bir download yardımcısı URL-view önkoşulu nedeniyle, bir urllib denemesi DNS nedeniyle byte sağlamadı; bağlı response recovery kullanıldı. Tek satırlı base64 görünümünün kesilmesi tam içerik diye sayılmadı. Signed download URL veya erişim token'ı çalışma kayıtlarına konmadı. Yerelde doğru taşıyıcı Git blob'u tutmadan decode sonucu kanıt yapılmadı.

Kaynak PRECHECK, betik ve sonuç birlikte ele alındı. Olumlu normal round-trip, unknown-name refusal ve Python invocation error karşılıkları korundu. Case6'daki iki loop çağrısı tek run içindedir. Case8 iki alanı sınayan local shape checker'dır; SDK/API rejection değildir. Case7 diagnostic text/id'yi korur, yalnız structural is_error history'de kaybolur. E06 excluded ve iki E05 geçmişi dahil önceki deneyler kendi kapsamlarında kalır.

## 5. Kaynak–kayıt kontrolü, yorum izi ve publication

Yeni [TERMS-PYTHON-PROVIDERS-AND-TOOLS.md](TERMS-PYTHON-PROVIDERS-AND-TOOLS.md), **ECC-PY01–PY108**. §12 N27 bölüm-kayıt ve E09 vaka-kayıt hesabını, §13 ilişki/yorum izini taşır. K/V/H/B/T/E/Y; kod raporu, versioned sözleşme, dated belge, mesaj/beyan, upstream test, kayıtlı deney ve açıklamayı ayırır. Yeni Türkçe metinler extractor paraphrase'idir.

Başlıca ayrımlar: saved provider/model pair ile consumed selection; optional helper ile actual caller; ortak input alanı ile effective provider option; tool definition/response conversion ile whole-history conversion; registry membership ile request-specific authority; declared schema/strict etiketi ile Python invocation; iteration limit ile effect-free stop; error text ile structural error state; fresh retry ile recoverable attempt; declared dependency range ile constructor compatibility.

Ham kaydın anlam katkısı PY66 strict:true, PY83 accepted scripted result ve PY80 no_internal_retry isimlerinde görünürdür. Bunlar sırasıyla executor schema enforcement, bağımsız iş kabulü veya bütün SDK'larda retry yokluğu diye okunmadı. İlk yayın öncesinde normalization/refusal PY19/PY106, ModelInfo/list_models PY31/PY107 ve global/CN PY47/PY108 ayrı adreslendi. Önceki TERMS'i değiştirmeyi gerektiren maddi çelişki saptanmadı; yeni ayrımlar eski araştırmayı yeniden yazmadı.

Yeni TERMS commit **1ff40ee8ee957ab0a4926dd2f649e651f859c257**, blob **65a50600cd696d63566ef4b8dc07c58c3d55839d**. Hazırlanmış içerik **37679 UTF-8 bytes / 228 satır** ve remote blob eşleşti. 108 sıralı/unique ID, gap/duplicate yok ve üç-kolon kullanım satırları kontrol edildi. Remote FULL readback **1–55 / 56–105 / 106–155 / 156–200 / 201–260 üzerinden EOF**. Bu yeni dosya için byte/şekil ve source-to-record kontrolüdür; bütün-repo link suite'i veya bağımsız semantik doğrulama değildir.

Bu READING/router/global STATE güncellemelerinden sonra final main/ref/diff ve entry readback ayrıca yapılır. Kendi gelecekteki hash veya yapılmamış kontrol uydurulmaz. Current-parent SHA-aware writes eşzamanlı işi korur; branch, force update, kaynak araştırma mutation'ı veya kullanıcı upload/merge görevi yoktur.

## 6. Kaynak delta'sı ve exact next — ECC C6

Önceki Concepts kapanışı **592b11b → c0fd473** altı commit farkı yalnız ECC kaynak girişleri, U13-A receipt/round/state ve catalogue kapsamındaydı; Concepts/control değişmedi. Source STATE/META/INDEX c0fd473'te FULL okundu: bloblar sırasıyla **961dda6d1f72f889ab67f5c2b8113d2724c1f592**, **8e74c18c353870fb99fd6c911e7e3c7558b85fe7**, **929d8a505674828f27617f1ebc5a842db2c5df00**. U13-A artık COMPLETE/PUBLISHED idi.

Tur içinde separate source research U13-B'yi de açtı. İlk c0fd473→main karşılaştırması PLAN/STATE değişikliği ve **ROUND-U13-B.md, evidence/U13-B-SOURCES.md, notes/29-SUPPLY-CHAIN-SCAN-COVERAGE-AND-ADVISORY-FRESHNESS.md** eklerini gösterdi. Source STATE **3eac1c12fab41e17f41a93088d5f135542010f01** ref'inde FULL okundu, blob **81ee321e41d746118a7b94ae196995b28c72ead3**: U13-B IN PROGRESS, son completed U13-A. Bu as-of context kaydıdır; yeni note29 gövdesi Concepts'te okunmuş veya source inquiry burada yürütülmüş değildir. U12-C'nin yedi fixed kaynağı değişmedi.

**Sıradaki iş C6'nın actual package manifest ve reconciliation başlangıcıdır:**
1. Fresh source STATE/META/INDEX ve current ECC tree/yaprak envanterini al; baseline ile added/changed/deleted/moved delta'yı çıkar.
2. §1'deki yedi tam READING, current dosya, router'ın korunan tam ilişki geçmişi ve bütün ECC TERMS'i birlikte devral; görünmeyen eski full scope'u tahmin etme.
3. Kalan root/master-history/inventory/evidence dosyalarının hesabını kapat; U13-A ve o sırada mevcut U13-B/sonraki kaynak materyalini sırf eski C1–C5 planında yok diye dışlama. Gereken mevcut-source kullanım aktarımını uygun Concepts kaydına yap; yeni ECC teknik araştırması başlatma.
4. Kullanım/atıf/rol/ID/ilişki ve maddi değişiklik etkisini paket genelinde kontrol et. Ancak actual scope karşılandıktan sonra version-qualified ECC Concepts package closure ver.

C6 bu tur başlatılmadı; delta discovery ve next-work kaydı C6'nın tamamlandığı anlamına gelmez. ECC sonrası sıra **work-management-project-control**. Post-S1 agentmemory/claude-swap/cli-continues/ponytail kapsamı B7 öncesi global hesaba girer. B7 bitmeden B8 ortak referans başlamaz.

Q02c2 ve diğer kaynak araştırma residual'ları otomatik Concepts deney borcu değildir. Batu okuma anındaki anlam seçimlerini denetleyemediğinden önemli dayanak/yorum/belirsizlik/değişim izlenebilir kalır; aynı sözcük ortak anlamı garanti etmez ve kullanıcı onayı teknik oracle olmaz.
