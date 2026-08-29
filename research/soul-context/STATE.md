# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 5 — KEEL öz-anlatısını bugünkü mekanizmayla karşılaştırma  
**Son güncelleme:** 2026-08-29

## Ana hedef

Üç kaynak repoyu sistematik okuyarak SOUL Research projesinin gerçek araştırma niyetini yeniden kurmak; erken mimari çözüm üretmemek.

## Kaynak repoların rolleri

- `soul`: current explicit intent anchor.
- `os-architect`: tarihsel arıza, karar, yöntem, araştırma ve KEEL geliştirme bağlamı.
- `keel`: bugünkü somut ürün/mekanizma yüzeyi.

## Tamamlanan geçişler

### A — çalışma düzeni ve araştırma yöntemi

Tam okunan ana dosyalar: `eski-alanin-cokusu`, `sonsuza-kadar-kullanilabilirlik`, `arastirma-yontemi`, `hasim-turu-yontemi`, `dis-goz-yontemi`.

Doğrulanan ayrım:

- depo/temsil failure'ı,
- çalışma-döngüsü failure'ı,
- epistemik süreç failure'ı.

### B — KEEL problem ve kanıt modeli

Tam okunan ana dosyalar: `kurulus-ve-sertlestirme`, `genesis-v2-kanit-zinciri`, `urun-ariza-kokenleri`, `defo-cercevesi`, `dis-dogrulama`.

Doğrulanan ayrım:

- gözlenen arıza/saha olayı,
- ölçüm/tatbikat,
- tasarım hükmü,
- dış yakınsama.

KEEL güvenlik sınırı olarak değil savruk/onay-arayışlı ajan için işletim disiplini olarak çerçeveleniyor. Tarihsel olarak doğrulama/koruma mekanizmaları davranış anti-defolarından daha güçlü.

### C — önceki araştırma ve dış-göz kayıtları

Okundu:

- `arastirma-seansi-2026-08-kunye.md`
- `arastirma-seansi-2026-08-akil-yurutme.md`
- `arastirma-seansi-2026-08-ev-eslemesi.md`
- `arastirma-seansi-2026-08-sektorler.md`
- `arastirma-seansi-2026-08-sektorler-hukmu.md`
- `arastirma-seansi-2026-08-gstack.md`
- `disgoz-seansi-2026-08-kunye.md`
- `disgoz-seansi-2026-08-hedef-ve-bakis.md`
- `disgoz-seansi-2026-08-teshisler.md`
- `disgoz-seansi-2026-08-matris.md`
- `disgoz-seansi-2026-08-alternatifler.md`
- `disgoz-seansi-2026-08-fikir-carpismasi.md`

Önemli sınır: araştırma seansının altı kaleminden yalnız 1, 2 ve 6'nın repo ayağı koşulmuş. 3–5 için tamamlanmış ayrı koşu kaydı yok; araştırılmış sayılmayacak.

`akil-yurutme` ve `sektorler` dış literatürün damıtılmış ikinci-el görünümüdür. Şu aşamada geçmiş araştırmanın düşünce yönünü anlamak için kullanılır; SOUL için yük taşıyan dış-literatür iddiası gerektiğinde birincil kaynağa geri dönülecek.

## Şu ana kadarki yapısal problem haritası

1. **Depo/temsil:** bilgi şişiyor, kopyalanıyor, bulunamıyor veya farklı ömürler karışıyor.
2. **Çalışma yaşam döngüsü:** durum saklansa bile hareket, sorumluluk ve güncelleme yükümlülüğü taşınmayabiliyor.
3. **Epistemik süreç:** aynı kaynak/model/çerçeve sahte yakınsama; verifier körlüğü ve yalancı-yeşil sahte güven üretebiliyor.
4. **Amaç/çerçeve:** soru görev sanılıyor; öncül ve gerçek amaç icradan önce yeniden türetilmeyebiliyor. Oturumlar sonucu taşıyıp neden/amaç modelini kaybedebiliyor.
5. **Ders→mekanizma:** ders belge olarak kalıyor, ihtiyaç anına ulaşmıyor veya bir hatta uygulanıp kardeş hatta taşınmıyor.

## Tarihsel yön sinyalleri — henüz nedensel sonuç değil

- 2026-08-08 dış-göz seansında hedef: dünya standardı + alışılmışın dışında/vizyoner problem çözme; KEEL akıl+teknik birlikte değerlendirilmeli.
- Aynı seansın üst tezi: daha fazla altyapı eklemek yerine görünmez varsayımları sözleşme, fixture, iz ve kapsama ölçümüne dönüştürmek.
- 2026-08-10 araştırma seansı çerçeve körlüğü ve "soru ≠ görev" problemi etrafında açılmış.
- 2026-08-11 gstack kaydında sahibin yön beyanı: "araştırma evi kurulacak"; araştırmalar sonraki yeni geliştirme çalışmasına girdi olacak. Bu bir mühürlü karar değil.
- 2026-08-25 `soul` repo bootstrap'ı: SOUL first-principles general-purpose agentic architecture; `development/` ile `system/` ayrı; ilk iş paketi SOUL Development Operating System.

Bu kronoloji doğrudan devamlılık hipotezini güçlendiriyor fakat **SOUL Research = önceki KEEL planının aynen devamı** sonucu henüz verilmez.

## Çalışma hipotezleri — SONUÇ DEĞİL

H1. SOUL Research'ün temel niyeti yalnız yeni bir agent framework aramak değil; durumsuzluk, drift, öz-onaylama, bilgi ömrü, amaç kaybı ve doğrulama problemlerini daha genel bir agentic architecture seviyesinde first principles'tan yeniden ele almak olabilir.

H2. SOUL Development OS'nin problemi yalnız persistans değil; **amaç + iş yaşam döngüsü + güncelleme sorumluluğu + epistemik doğrulama + dersin ihtiyaç anına ulaşması** birlikte olabilir.

H3. KEEL'den SOUL'a aktarılabilir çekirdek, dosya/ritüel isimlerinden çok **failure → ölçüm → mekanizma → falsification → yaşam döngüsü** zinciri olabilir.

H4. Önceki araştırmalar "daha iyi düşün" öğüdünden çok sorgulamanın **üreteci + tetiği + kanıt zinciri** fikrine doğru ilerlemiş; SOUL bunun daha genel bir biçimini arıyor olabilir.

H5. 8–11 Ağustos dış-göz/araştırma çalışmaları ile 25 Ağustos SOUL bootstrap'ı arasında doğrudan tasarım devamlılığı olabilir; bunu mevcut KEEL mekanizması ve mümkünse aradaki karar/commit kayıtlarıyla doğrulamak gerekir.

## Şimdi — D geçişi

Amaç: geçmiş anlatıların bugünkü `keel` reposunda gerçekten ne kadar mekanik karşılığı olduğunu görmek.

Öncelikli yüzeyler:

1. kurulum/giriş + `GENESIS_DURUM` / yeniden başlama,
2. guard / protected paths / role boundary,
3. bekçi + kasıtlı bozma / test yüzeyi,
4. verifier / karne / kapanış,
5. insan-okur ↔ makine durum sözleşmeleri,
6. bağlam ve ders→ihtiyaç köprüsü.

D geçişinde önce `keel` dizin haritaları çıkarılacak, sonra yalnız yük taşıyan dosyalar seçilecek; bütün `tools/` ağacı körlemesine okunmayacak.

## Yeni oturumda devam

1. Canonical `AGENT.md` + routing protokollerini yükle.
2. `research/soul-context/README.md` oku.
3. Bu `STATE.md` dosyasını oku.
4. `research/soul-context/repos/keel/README.md` aç.
5. `keel` içinde D geçişi için dizin haritası + seçici mekanizma okumasıyla devam et.

## Henüz yapılmaması gerekenler

- SOUL mimarisi önermek.
- KEEL mekanizmalarını SOUL gereksinimi saymak.
- İkinci-el literatür özetlerini doğrulanmış dış kanıt saymak.
- "SOUL Research'ün amacı kesin olarak X" hükmü vermek.
