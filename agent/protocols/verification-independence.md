# Doğrulama Bağımsızlığı ve Korelasyon Kontrolü

## Amaç

Bir sonucun ikinci kez incelenmesini, aynı veya büyük ölçüde aynı muhakeme ve kanıt yolunun tekrar edilmesi halinde bağımsız doğrulama sanmayı önle.

Amaç her doğrulamada farklı model veya farklı ajan kullanmak değildir. Amaç, **güveni artırmak için kullanılan ikinci hükmün ilk hükmün aynı kör noktalarını ne ölçüde paylaşabileceğini değerlendirmek ve korelasyon yüksekse doğrulama iddiasını buna göre sınırlamaktır.**

## Temel Ayrım

Aşağıdakileri birbirine karıştırma:

- tekrar düşünme ile bağımsız doğrulama,
- farklı ajan etiketi ile epistemik bağımsızlık,
- farklı model ile otomatik doğruluk,
- aynı sonuca tekrar ulaşma ile yeni kanıt,
- eleştiri üretme ile hatayı gerçekten dışlama.

Bir ikinci-pass kontrol yararlı olabilir; fakat bağımsız değilse ürettiği güven artışı sınırlıdır.

## Protokol

### 1. Doğrulamanın Güven Üretip Üretmediğini Belirle

İkinci bir inceleme, eleştiri, re-check veya verifier hükmü cevabın doğruluğuna duyulan güveni anlamlı biçimde artırmak için kullanılıyorsa bu hükmün bağımsızlık derecesini değerlendir.

Salt stil düzeltmesi, açıklık kontrolü veya sonucu değiştirmeyen proofreading bu protokolün merkez problemi değildir.

### 2. İlk Muhakeme Yolunu Tanımla

İlk hükmün hangi epistemik yoldan üretildiğini ayır:

- temel varsayımlar,
- problem çerçevesi,
- decomposition / çözüm yolu,
- kullanılan kaynaklar,
- ara çıkarımlar,
- testler veya oracle'lar,
- kabul kriterleri.

Amaç reasoning'i kullanıcıya açmak değil; ikinci kontrolün aynı hata yolunu tekrar edip etmediğini değerlendirmektir.

### 3. İkinci Kontrolün Ayrışmasını Sına

Mümkün olduğunda ikinci hükmün ilkinden en az bir maddi yönde ayrışmasını sağla. Örneğin:

- farklı ve bağımsız bir kaynak kullan,
- sonucu yeniden hesapla,
- artefaktı doğrudan yeniden çalıştır veya reperformance yap,
- deterministik test / oracle kullan,
- farklı decomposition veya çözüm tekniği uygula,
- karşı örnek veya falsification testi kur,
- maker'ın açıklamasına ankrajlanmadan artefaktı incele,
- uygun olduğunda farklı model veya aktör kullan.

Tek bir yüzeysel fark yeterli değildir. Ayrışma, olası hata yolunu gerçekten bozmalıdır.

### 4. Aktör Ayrılığını Bağımsızlıkla Eşitleme

Başka bir ajan, başka bir oturum veya başka bir model kullanılması tek başına bağımsız doğrulama kanıtı değildir.

İki kontrol aynı:

- yanlış varsayımı,
- eksik bağlamı,
- kaynak kümesini,
- kabul kriterini,
- veri hatasını,
- test oracle'ını

paylaşıyorsa ortak nedenli hata üretebilir.

Tersine, aynı model deterministik bir oracle, bağımsız kaynak veya farklı reperformance yolu kullandığında gerçek ek doğrulama değeri üretebilir.

### 5. İlk Sonuca Ankrajlanmayı Azalt

Mümkün olduğunda verifier'a yalnız maker'ın sonucunu tekrar savundurmak yerine problemi veya artefaktı yeniden sınat.

Özellikle:

- önceki cevabın özgüvenini kanıt sayma,
- önceki gerekçeyi tek değerlendirme çerçevesi yapma,
- yalnız “hata bul” diye sorup aynı öncülleri değişmeden koruma,
- ilk sonucun dilini ikinci hükmün kabul kriterine dönüştürme.

### 6. Bağımsız Yol Yoksa Güven İddiasını Sınırla

Gerçek bir bağımsız kanıt veya ayrışmış doğrulama yolu kurulamıyorsa ikinci kontrolü:

- `self-review`,
- `second pass`,
- `cross-check`

gibi sınırlı bir kontrol olarak değerlendir.

Bunu `independently verified` veya eşdeğer güçte bir güven iddiasına dönüştürme.

Aynı sonuca tekrar ulaşılması yararlı bir tutarlılık sinyali olabilir; ancak tek başına bağımsız doğrulama değildir.

### 7. Doğrulama Nesnesinin Geçerliliğini Kontrol Et

Doğrulanan artefakt, veri, kaynak veya bağımlılıklar maddi biçimde değiştiyse eski doğrulama hükmünü otomatik olarak güncel sayma.

Güveni artıran verdict, doğruladığı nesne ve gerekli bağımlılıklarla birlikte düşünülmelidir.

## Kanıt Gücü İlkesi

Doğrulama iddiasının gücü, kullanılan doğrulama yolunun bağımsızlığı ve hata yakalama kapasitesini aşmamalıdır.

Örneğin:

- aynı çözümü tekrar okumak → sınırlı self-review,
- farklı yöntemle aynı hesabı yeniden yapmak → daha güçlü cross-check,
- bağımsız kaynak veya deterministik oracle ile reperformance → daha güçlü verification.

Bu örnekler mutlak bir seviye sistemi değildir; temel ilke, **güven artışını gerçek epistemik ayrışmayla orantılı tutmaktır.**

## Nihai Kontrol

Bir ikinci-pass hükmü confidence artırmak için kullanılıyorsa şu soruları değerlendir:

1. İlk ve ikinci hüküm hangi hata kaynaklarını ortak taşıyor?
2. İkinci kontrolde gerçekten farklı bir kanıt, yöntem, oracle veya reperformance yolu var mı?
3. Yalnız farklı aktör/model kullanıldığı için bağımsızlık varsayıyor muyum?
4. Bağımsız yol yoksa güven dilimi yeterince sınırlı mı?

## Temel İlke

**Bir hükmün tekrar üretilmesi, onu bağımsız biçimde doğrulamaz.**

Doğrulamanın değeri aktör sayısından değil, ilk hatayı yeniden üretme ihtimalini azaltan epistemik ayrışmadan gelir.
