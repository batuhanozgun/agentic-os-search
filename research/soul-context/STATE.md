# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 1 — giriş kapıları ve okuma haritası  
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

- kök ağaç haritası görüldü.
- `NEREDE_NE_VAR.md` tam okundu — SHA `049d892677edef0480d7ccf6f37b02b1a363b6de`.
- `PANO.md` tam okundu — SHA `28a9be2ab5b2cecfa4fb86691bf46d7a0f3ba2c9`.
- `CLAUDE.md` tam okundu — SHA `2eb682f06d75295facfc58681eb6b9d0123d1342`.
- `bilgi/INDEKS.md` tam okundu — SHA `19b78442ce12f378dd5ab55dc9829e3505c5760b`.
- `bilgi/keel/INDEKS.md` tam okundu — SHA `881c2be41c5924c7648fa56d111a26facec8e01b`.
- `bilgi/calisma-duzeni/INDEKS.md` tam okundu — SHA `1f5cef294d760bac2c86776f876c757568b8bc5a`.
- Explicit çapa: bu çalışma alanının işi KEEL'i geliştirmek ve bitirmek.
- İlk sinyal: bilgi mimarisi özellikle uzun ömür, tek-ev, indeks, çıkış/ömür kuralı, mekanik bekçi, kanıt dili ve chat hafızasına güvenmeme problemleri etrafında evrilmiş.
- `bilgi/keel/INDEKS.md`, kuruluş, otonomi, doğrulama, dış-göz, araştırma seansları ve sahip karar alanı gibi SOUL Research için yüksek bilgi değerli kümeler gösteriyor.
- `bilgi/calisma-duzeni/INDEKS.md`, araştırma yöntemi, hasım turu, deney, dış-göz, sürdürülebilirlik ve eski alanın çöküşü gibi meta-yöntem kaynaklarını gösteriyor.

## Çalışma hipotezleri — SONUÇ DEĞİL

H1. SOUL Research yalnız "yeni bir agent framework araştırması" değildir; önceki çalışma alanlarında ortaya çıkan **durumsuzluk, drift, öz-onaylama, motivasyon çakışması, bilgi ömrü ve doğrulama** problemlerini daha genel bir agentic architecture bağlamında yeniden ele alma hazırlığı olabilir.

H2. KEEL, önemli deney ve mekanizma kanıtı taşısa da yazılım-projesi işletim disiplinidir; SOUL'un genel amaçlı mimarisine doğrudan kopyalanamaz. Ürün-özel mekanizma ile genellenebilir prensip ayrılmalıdır.

H3. `soul` README'sindeki `development/` / `system/` ayrımı, önce sistemin kendisini değil **onu güvenilir biçimde üretecek geliştirme işletim sistemini** kurma ihtiyacının bilinçli sonucu olabilir. Bu gerekçenin kaynağı os-architect ve KEEL geçmişinden doğrulanmalıdır.

## En yüksek bilgi değerli sonraki okuma

### A. Çalışma düzeninin neden evrildiğini anla

1. `os-architect/bilgi/calisma-duzeni/eski-alanin-cokusu.md`
2. `os-architect/bilgi/calisma-duzeni/sonsuza-kadar-kullanilabilirlik.md`
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

## Okuma sırası için karar

Bir sonraki turda **A → B → C → D** sırası izlenecek. Gerekçe: önce çalışma alanının neden bu hale geldiğini anlamadan ürün mekanizmasını okumak, mevcut çözümü problem tanımının kendisi sanma riski yaratır.

## Yeni oturumda devam

1. Canonical `AGENT.md` + routing protokollerini yükle.
2. `research/soul-context/README.md` oku.
3. Bu `STATE.md` dosyasını oku.
4. `repos/os-architect/README.md` dosyasını aç.
5. A grubunun ilk dosyasından devam et.

## Henüz yapılmaması gerekenler

- SOUL için mimari önermek.
- KEEL mekanizmalarını SOUL gereksinimi olarak kabul etmek.
- "SOUL Research'ün amacı kesin olarak X" hükmü vermek.
- Üç repoyu dosya sayısı üzerinden körlemesine tüketmek.
