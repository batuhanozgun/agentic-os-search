# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 3 — KEEL'in problem ve kanıt modeli  
**Son güncelleme:** 2026-08-29

## Ana hedef

Üç kaynak repoyu sistematik okuyarak SOUL Research projesinin gerçek araştırma niyetini yeniden kurmak; erken mimari çözüm üretmemek.

## Şu ana kadar doğrulananlar

### `soul`

- `README.md` tam okundu — SHA `9dbded3017e62a968ead024cf1d544d1d37a2be2`.
- Repo geçmişinde bağlı GitHub görünümünde tek commit bulundu: `7b2a9a4` — `bootstrap: initialize SOUL repository` (2026-08-25).
- Commit yalnız `README.md` oluşturuyor.
- Explicit çapa: SOUL, intended outcome'u kontrollü ve doğrulanabilir çalışan sisteme dönüştüren genel amaçlı agentic architecture olarak first principles'tan yeniden kuruluyor.
- Explicit ayrım: `development/` = SOUL'u tasarlayan/gözden geçiren/doğrulayan/geliştiren operating system; `system/` = tekrar kullanılabilir ürün.
- İlk iş paketi product architecture değil, SOUL Development Operating System.

### `keel`

- kök ağaç haritası görüldü.
- `README.md` tam okundu — SHA `a221d174f7422a32dbd369e8516d8b7aa31b3a92`.
- `GENESIS.md` tam okundu — SHA `a04b80607915644ea56524d2fa87c6177f34949d`.
- `00_genesis/DEFO_MODELI.md` tam okundu — SHA `e9bddf5e04e13d90dbb6014eb432fba18357f6ac`.
- İlk sinyal: KEEL, durumsuz ajanlarla yazılım projesi kurup yürütmek için işletim disiplini; kanonik durum, roller, kutular, insan mühürleri ve mekanik doğrulama yüzeyleri merkezde.
- DEFO modeli, sistem tasarımının LLM/ajan eğilimlerini yok saymak yerine bunların gözlemlenebilir izlerini ve mekanik karşılıklarını üretmesi gerektiğini savunuyor.

### `os-architect`

Giriş ve indeksler tam okundu:

- `NEREDE_NE_VAR.md` — `049d8926`.
- `PANO.md` — `28a9be2a`.
- `CLAUDE.md` — `2eb682f0`.
- `bilgi/INDEKS.md` — `19b78442`.
- `bilgi/keel/INDEKS.md` — `881c2be4`.
- `bilgi/calisma-duzeni/INDEKS.md` — `1f5cef29`.

A grubu — çalışma düzeni ve araştırma yöntemi — TAMAMLANDI:

- `bilgi/calisma-duzeni/eski-alanin-cokusu.md` — `5fd38faa`.
- `bilgi/calisma-duzeni/sonsuza-kadar-kullanilabilirlik.md` — `4750e45d`.
- `bilgi/calisma-duzeni/arastirma-yontemi.md` — `a6601f3f`.
- `bilgi/calisma-duzeni/hasim-turu-yontemi.md` — `751fafea`.
- `bilgi/calisma-duzeni/dis-goz-yontemi.md` — `fcc54218`.

Doğrulanan maddi bulgular:

- Eski alanın ölçülen çöküşünde aşırı büyük canonical dosyalar, tavansız ham araştırma, arama güvensizliği yüzünden kopya/drift ve farklı ömürlü içeriğin aynı yerde tutulması öne çıkıyor.
- Yalnız dosya yapısını düzeltmek yeterli görülmemiş; aynı davranış yeni yapılarda tekrar edebiliyor.
- Uzun ömürlü kullanılabilirlik üç ayrı disiplini gerektiriyor: veri/kütüphane disiplini, danışmanın çalışma disiplini ve ürün geliştirme disiplini.
- Statik hijyen tek başına yeterli olmamış: sistemin hareketi, güncelleme sorumluluğu ve yaşam döngüsü de taşınmadığında çalışma alanı "depo" oluyor fakat "tezgâh" olmuyor.
- Araştırma süreci kendi epistemik failure mode'larına karşı tasarlanmış: echo/self-citation, aynı kaynağı çoğaltma, dış aracın sentezini dış kanıt sayma, ölçülmemiş tasarım ve doğrulanmamış dış iddia özellikle kontrol ediliyor.
- Çok reviewer veya çok ajan tek başına bağımsızlık değil. Okuyan göz ile koşan göz farklı hata sınıfları buluyor; yalancı-yeşil avı ve kasıtlı bozma, doğrulamanın gerçekten kırmızı verebildiğini sınamak için kullanılıyor.
- Dış göz yararlı olabilir ve yeni gerçek bulgular üretmiş; ancak dış rapor hakikat olarak alınmıyor, repo/makine üzerinde yeniden doğrulanıyor. Doğru bulgu + yanlış teşhis mümkün kabul ediliyor.

## Çalışma hipotezleri — SONUÇ DEĞİL

H1. SOUL Research yalnız "yeni bir agent framework araştırması" değildir; önceki çalışma alanlarında ortaya çıkan **durumsuzluk, drift, öz-onaylama, motivasyon çakışması, bilgi ömrü ve doğrulama** problemlerini daha genel bir agentic architecture bağlamında yeniden ele alma hazırlığı olabilir.

H2. KEEL, önemli deney ve mekanizma kanıtı taşısa da yazılım-projesi işletim disiplinidir; SOUL'un genel amaçlı mimarisine doğrudan kopyalanamaz. Ürün-özel mekanizma ile genellenebilir prensip ayrılmalıdır.

H3. `soul` README'sindeki `development/` / `system/` ayrımı, önce sistemi değil **onu güvenilir biçimde üretecek ve uzun süre geliştirecek çalışma sistemini** kurma ihtiyacının bilinçli sonucu olabilir. A grubu bu hipotezi güçlendiriyor, ancak doğrudan nedensel bağ henüz kanıtlanmış değil.

H4. SOUL Development OS'nin çözmesi gereken problem yalnız bilgi persistansı olmayabilir; **işin yaşam döngüsünü, güncelleme sorumluluğunu, doğrulamayı ve drift kontrolünü oturumlar arasında taşıma** problemi daha temel olabilir.

H5. SOUL Research'ün kendi araştırma düzeni de araştırma nesnesinden bağımsız bir güven problemi taşıyor olabilir: aynı model/aynı kaynak/aynı çerçeveden gelen çoklu sentez sahte yakınsama üretebilir. Bu nedenle ilerideki dış araştırmada kaynak bağımsızlığı ve falsification yüzeyi açıkça izlenmeli.

## Plan kontrolü

A grubu tamamlandı. A → B → C → D planı korunuyor.

Metodoloji geçişi planı değiştirmedi; aksine B ve C gruplarındaki kanıtların nasıl okunacağını belirginleştirdi: öz-anlatı, ölçüm, uygulama ve dış doğrulama epistemik olarak ayrı tutulacak.

## En yüksek bilgi değerli sonraki okuma

### B. KEEL'in hangi problem modelinden doğduğunu anla — ŞİMDİ

1. `os-architect/bilgi/keel/kurulus-ve-sertlestirme.md`
2. `os-architect/bilgi/keel/genesis-v2-kanit-zinciri.md`
3. `os-architect/bilgi/keel/urun-ariza-kokenleri.md`
4. `os-architect/bilgi/keel/defo-cercevesi.md`
5. `os-architect/bilgi/keel/dis-dogrulama.md`

### C. Daha önce yapılmış dış araştırmanın çerçevesini oku

1. `os-architect/bilgi/keel/arastirma-seansi-2026-08-kunye.md`
2. ardından yalnız künyenin işaret ettiği altı araştırma dosyası
3. `os-architect/bilgi/keel/disgoz-seansi-2026-08-kunye.md`
4. ardından gerekli dış-göz kayıtları

### D. KEEL'in öz-anlatısını mekanikle karşılaştır

OS Architect'teki problem/kanıt modeli okunduktan sonra KEEL'de ilgili `tools/guard`, `tools/bekci`, fixture ve sözleşme dosyalarına seçici in.

## Yeni oturumda devam

1. Canonical `AGENT.md` + routing protokollerini yükle.
2. `research/soul-context/README.md` oku.
3. Bu `STATE.md` dosyasını oku.
4. `research/soul-context/repos/os-architect/README.md` aç.
5. B grubunda tamamlanmamış ilk dosyadan devam et; şu anda başlangıç noktası `os-architect/bilgi/keel/kurulus-ve-sertlestirme.md`.

## Henüz yapılmaması gerekenler

- SOUL için mimari önermek.
- KEEL mekanizmalarını SOUL gereksinimi olarak kabul etmek.
- "SOUL Research'ün amacı kesin olarak X" hükmü vermek.
- Üç repoyu dosya sayısı üzerinden körlemesine tüketmek.
