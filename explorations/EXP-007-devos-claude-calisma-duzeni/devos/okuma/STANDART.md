# Çalışma standardı — her alt ajan için zorunlu

Bu dosyayı işe başlamadan önce baştan sona oku. Burada yazanlar, Batu'nun bu işi yapan herkesten beklediği standarttır. Ana oturum da aynı standarta tabidir. Kaynak: Batu'nun sözleri (`sources/conversation/U004`, `U014`, `U015`, `U017`, `U018`, `U020`; önceki Claude denemesindeki `OWNER.md` O-01, O-16, O-20, O-21).

## Batu'nun sözleri (birebir)
- "Doğru düzgün okumuyorsun, okuduklarından kendini yeninden kalibre etmiyorsun"
- "okuyacaksın, okuduklarını kullanacaksın. Adam gibi hazırlık yapıp bu işi yapacaksın"
- "basit, dandik, ucuz, yapı istemiyorum. ne gerekiyorsa yapan, bilmediği şeyi araştıran, kendini bilen, drift yaşamayana, mekanizma kullanan, bütünü gören ve bunun gibi binlerce özelliğ olan yapı istiyorum"
- "bir konuyu okuyor, onu örnek almakla onu daraltıp kullanmayı aynı şey sanıyor. [...] hep örnek aldığı yapının üstünde bir yapı kurmalı [...] ucuz işi genelde kapsamı daraltmak ile karıştırıyor LLM, siz öyle yapmayın." (O-16)
- "yeterli seviye ile standart seviye arasında fark var" (U004, araba benzetmesi)
- "bir dosyayı okuduğunda baştan sona oku; özet ya da arama sonucuyla 'okudum' deme." (O-01)
- "bana sorumluluk yükleme, kesinlikle yasak %100 sorumluluk sende olacak."

## Bundan çıkan kurallar
1. **Kapsamının tamamını oku.** Görev tanımındaki kaynakların hepsi okunur. Önce harita çıkar, sonra her dosyayı baştan sona oku. Büyük dosyayı parça parça, sonuna kadar oku. Göz gezdirme, "ilgisiz görünüyor" diye atlama. Atlanan her dosyanın gerekçesi notta yazılı olur ve gerekçe yalnız "içerik gerçekten konu dışı" olabilir. Gerekçeyi, dosyayı açıp gördükten sonra yaz.
2. **Kapsam sana büyük geliyorsa ayıklama, söyle.** Bağlamın dolacaksa ya da süre yetmeyecekse okumayı yarıda kesip özet yazma. Notunun başına "KAPSAM BÖLÜNMELİ" yaz; okuyamadığın dosyaları tam listeyle ver. Ana oturum ek ajan gönderir. Yarım okumayı tam okuma gibi sunmak en ağır hatadır.
3. **Yalnız META varsa asıl kaynağa git.** Bir study paketinde yalnız META ya da aday kaydı varsa, orada adı geçen asıl kaynağa git: upstream repo, belge, makale. Genel repoyu yalnız okunur sığ klonla (`GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 <url> <scratchpad-yolu>`; aynı repoya paralel klon açma; iş bitince sil) ya da WebFetch kullan. Mekanizmayı kaynağın kendisinden çıkar.
4. **Daraltma, yükselt.** Örnek aldığın yapının basitini çıkarma. Bir mekanizmanın bütün parçalarını, koşullarını ve sınırlarını yaz. "Şimdilik şu kadarı yeter" deme. Uyarlama gerekiyorsa, örneği aşan bir uyarlama öner.
5. **Kanıt ve dürüstlük.**
   - Her iddia kaynak yolu ya da URL'si ve gerekirse satır ya da alıntıyla desteklenir.
   - Etiket kullan: kaynak diyor / gözledim / çıkarım / bilinmiyor.
   - Test ya da koşu yapmadıysan "çalışıyor" deme; yalnız "kaynak çalıştığını söylüyor" de.
   - Kesik araç çıktısına bakıp "kaynakta yok" deme.
6. **Kendi yargını kur.** Kaynağın ya da ana oturumun öncülü yanlışsa kanıtla söyle. Bir iddia kaynakla çelişiyorsa açıkça yaz; bu, önceki notların iddiaları için de geçerlidir.
7. **Soru sorma, sorumluluğu yükleme.** Batu'ya soru yok. Bilmediğini kaynağa ve internete sor.
8. **Not boyutu okumayı sınırlamaz.** Gerekiyorsa not 90 KB'a kadar çıkabilir. Yoğun yaz, tekrar etme, ama içeriği kırpmak için okumayı kısma.
9. **Bitirmeden önce kontrol et.**
   - Kapsam listesinde "okunmadı" kalan her kalem için gerekçe var mı?
   - Her mekanizmada "nasıl işler" somut mu: dosya, format, tetik ve kod var mı?
   - DevOS için "al / uyarlayarak al / alma" kararı gerekçeli mi?
