# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 2 — çalışma düzeninin kök nedenleri  
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
- Def o modeli, sistem tasarımının LLM/ajan eğilimlerini yok saymak yerine bunların gözlemlenebilir izlerini ve mekanik karşılıklarını üretmesi gerektiğini savunuyor.

### `os-architect`

Giriş ve indeksler:

- `NEREDE_NE_VAR.md` — `049d8926` — full.
- `PANO.md` — `28a9be2a` — full.
- `CLAUDE.md` — `2eb682f0` — full.
- `bilgi/INDEKS.md` — `19b78442` — full.
- `bilgi/keel/INDEKS.md` — `881c2be4` — full.
- `bilgi/calisma-duzeni/INDEKS.md` — `1f5cef29` — full.

Kök-neden geçişi:

- `bilgi/calisma-duzeni/eski-alanin-cokusu.md` — `5fd38faa` — full.
- `bilgi/calisma-duzeni/sonsuza-kadar-kullanilabilirlik.md` — `4750e45d` — full.

Doğrulanan maddi bulgular:

- Eski alanın ölçülen çöküşünde aşırı büyük canonical dosyalar, tavansız ham araştırma, arama güvensizliği yüzünden kopya/drift ve farklı ömürlü içeriğin aynı yerde tutulması öne çıkıyor.
- Yalnız dosya yapısını düzeltmek yeterli görülmemiş; aynı davranış yeni yapılarda tekrar edebiliyor.
- Uzun ömürlü kullanılabilirlik üç ayrı disiplini gerektiriyor: veri/kütüphane disiplini, danışmanın çalışma disiplini ve ürün geliştirme disiplini.
- Ortam, danışman ve ürünün rolleri/evleri karıştırılmıyor.
- Statik hijyen tek başına yeterli olmamış: sistemin hareketi, güncelleme sorumluluğu ve yaşam döngüsü de taşınmadığında çalışma alanı "depo" oluyor fakat "tezgâh" olmuyor.

## Çalışma hipotezleri — SONUÇ DEĞİL

H1. SOUL Research yalnız "yeni bir agent framework araştırması" değildir; önceki çalışma alanlarında ortaya çıkan **durumsuzluk, drift, öz-onaylama, motivasyon çakışması, bilgi ömrü ve doğrulama** problemlerini daha genel bir agentic architecture bağlamında yeniden ele alma hazırlığı olabilir.

H2. KEEL, önemli deney ve mekanizma kanıtı taşısa da yazılım-projesi işletim disiplinidir; SOUL'un genel amaçlı mimarisine doğrudan kopyalanamaz. Ürün-özel mekanizma ile genellenebilir prensip ayrılmalıdır.

H3. `soul` README'sindeki `development/` / `system/` ayrımı, önce sistemi değil **onu güvenilir biçimde üretecek ve uzun süre geliştirecek çalışma sistemini** kurma ihtiyacının bilinçli sonucu olabilir. İlk iki kök-neden dosyası bu hipotezi güçlendiriyor, ancak henüz doğrudan nedensel bağ kanıtlanmış değil.

H4. SOUL Development OS'nin çözmesi gereken problem yalnız bilgi persistansı olmayabilir; **işin yaşam döngüsünü, güncelleme sorumluluğunu, doğrulamayı ve drift kontrolünü oturumlar arasında taşıma** problemi daha temel olabilir.

## Plan kontrolü

İlk iki A-grubu dosyası mevcut sırayı değiştirmedi. A → B → C → D planı korunuyor.

Gerekçe: mevcut çözüm (KEEL) önce okunursa ürün mekanizmasının problem tanımını peşinen belirlemesi riski var. Önce çalışma düzeninin gerçek failure mode'ları ve araştırma yöntemi anlaşılmalı.

## En yüksek bilgi değerli sonraki okuma

### A. Çalışma düzeninin neden evrildiğini anla — DEVAM

Tamamlandı:

1. `os-architect/bilgi/calisma-duzeni/eski-alanin-cokusu.md`
2. `os-architect/bilgi/calisma-duzeni/sonsuza-kadar-kullanilabilirlik.md`

Sıradaki:

3. `os-architect/bilgi/calisma-duzeni/arastirma-yontemi.md`
4. `os-architect/bilgi/calisma-duzeni/hasim-turu-yontemi.md`
5. `os-architect/bilgi/calisma-duzeni/dis-goz-yontemi.md`

### B. KEEL'in hangi problem modelinden doğduğunu anla

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
5. `os-architect/bilgi/calisma-duzeni/arastirma-yontemi.md` ile devam et.

## Henüz yapılmaması gerekenler

- SOUL için mimari önermek.
- KEEL mekanizmalarını SOUL gereksinimi olarak kabul etmek.
- "SOUL Research'ün amacı kesin olarak X" hükmü vermek.
- Üç repoyu dosya sayısı üzerinden körlemesine tüketmek.
