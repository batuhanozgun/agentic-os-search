# REVİZYON — eleştirilerin işlenmesi (P0.6)

**Önce oku:** `briefs/ORTAK-SENTEZ.md` ve `briefs/ENTEGRASYON.md`. Sonra üç eleştirinin tamamını oku:
- `reviews/E1-soz-cikti-ve-standart.md`
- `reviews/E2-butunsel-etkilesim.md`
- `reviews/E3-batu-ilkeleri-ve-uygulanabilirlik.md`

**Çıktı dosyaları** (her birini tek seferde yaz):
- `explorations/EXP-007-devos-claude-calisma-duzeni/phases/P0-calisma-duzeni/METHOD-v1.md`: tartışma sürümü;
- `explorations/EXP-007-devos-claude-calisma-duzeni/phases/P0-calisma-duzeni/reviews/DEGISIKLIK-KAYDI.md`: her bulgunun nasıl işlendiği.

## Okuma ve yazma düzeni
- Küme taslakları (`drafts/`) dondurulmuştur. Kart düzeyindeki her değişiklik METHOD-v1'e yazılır ve kart dizininde "değişti" diye işaretlenir.
- Bağlam ve maliyet disiplini: `briefs/ENTEGRASYON.md`, "Ana oturumdan notlar", madde 2.

## Ana oturumdan notlar (eleştiriler dönünce eklendi)

**1. Sayılar ve ortak kökler.** E1: 0 kritik · 7 önemli · 6 küçük. E2: 2 · 10 · 4. E3: 3 · 9 · 4. Toplam 5 kritik, 26 önemli ve 14 küçük, yani 45 bulgu. Bulgular örtüşüyor. Aynı kökü paylaşanları birlikte çöz ve DEGISIKLIK-KAYDI'nda birlikte göster:
- **Batu'nun denetçi işlevi:** E2-02 (sessizlik görünmez, tercih borcu birikir), E3-02 (Batu'nun neyi denetlediği tanımsız, kalan risk onun adına kabul edilmiş), E3-04 (sahte seçenek; onay teknik kapıya dönüşüyor).
- **Frenlerin sahibi:** E2-01 (frenler sürücünün elinde), E1-01 (frenler yalnız tavsiye, mekanik durdurma yok), E2-09 ve E3-12 (koordinatörün bütçesi yok).
- **Kendi beyanının şişmesi:** E1-03 ("karşılanmadı 0" yanlış), E1-04 (yazılmamış metinler §0'da söylenmiyor), E1-07 ve E3-03 (karar okuması 4.616 kelime, bütçe 1.500).
- **Yapan ile denetleyenin ayrılması:** E3-06, E1-05 (soğuk başlangıç testi koordinatörün kendi cevap anahtarıyla puanlanıyor).
- **AGENT.md önceliği:** E3-01. A-01 ile birlikte Batu'ya soru olur.

**2. Ana oturumun kendi payı (bilinsin).**
- §11–§14 ve Ek, yeniden okuma yapılmadan yazıldı. Bunu ana oturum istedi, çünkü birleştirme ajanının bağlamı 776 K'ya çıkmıştı. E3-03'ün §12 bulgusu bu kararın bedeli. Yazmaya başlamadan önce §12–§14'ü kaynaklarına karşı hedefli olarak doğrula.
- Ana oturum, taslağın "karşılanmadı 0" beyanını kontrol etmeden Batu'ya aktardı, sonra düzeltti. Bu, E1-03'ün canlı örneğidir; "beyan doğrulama değildir" kuralına örnek olarak girebilir.
- E3.md'deki "6,5 M" satırı, maliyet düzeltmesi STATE'e yazıldığı halde güncellenmedi. Bu bir yayılma kaçağıdır (W6 türü). T1'in "değişince kontrol et" sütunlu dosya görevleri tablosu tam bu kaçağı önlemek için var; kanıt olarak kullan.

**3. Batu'ya gidecek metin.**
- §0 bir sayfa ve sade Türkçe olur. Kod ve kısaltma kullanma; PS-1, SHA, MB-xx, hook gibi terimleri ya açıkla ya çıkar.
- Batu'nun karar için okuması gereken toplam metin ≤ 1.500 kelime olur. Say ve sayıyı METHOD'a yaz.
- Her soru şunları taşır: tek öneri, gerekçe, onay verilmezse ne olacağı. Sahte seçenek yok (E3-04). Batu'nun kararına bağlı olmayan teknik ayrıntı soru olarak gitmez.
- Kapsam beyanları sayıma dayanır: "X sözün Y'si somut, Z'si kısmen, W'si karşılanmadı." E1'in sayımını temel al, kendi sayımınla karşılaştır.
- Yazılmamış ve denenmemiş olan her şey §0'da açıkça söylenir.

**4. Maliyet (E3-12).** Bütün harita için kaba bir maliyet tahmini ve bir koordinatör bütçesi ekle. Ölçülmüş taban `STATE.md`, "Maliyet" bölümündedir:
- oturum toplamı ≈ 476 M işlenen token;
- eleştiri ajanı başına 5–10 M, küme ajanı başına 21–39 M, birleştirme 15 M.

E3 kendi hesabıyla P1–P6 için 1,2–2,3 milyar işlenen token buldu. Bu tahmini sına. Düşürme yollarını karşılaştır: hedefli okuma, tarama işlerinde daha küçük model, daha az ve daha küçük ajan.

**5. Ağırlık.** E1-06'ya göre birleştirme hiçbir kartı çıkarmadı; hook ve skill tavanları tasarımın kendi sayılarına eşit. Revizyonda çıkarılabilecek ya da birleştirilebilecek olanı da ara. Eklenen her şey için neyin çıktığını yaz.

**6. Senin okuma bütçen.** METHOD taslağı (218 KB) ile üç eleştiri (≈ 200 KB) zaten ≈ 420 KB eder. Taslaklardan yalnız bulguların işaret ettiği kartları aç; toplam okumayı ≈ 700 KB ile sınırla. Doğrulama okumalarını yazmaya başlamadan bitir. Çıktılar büyükse parçaları repo dışında, `/tmp/claude-0/-home-user-agentic-os-search/affc278a-ec70-529f-9e05-a727993399f1/scratchpad/revizyon/` altında hazırla.

## Görev
1. **Her bulgu için bir karar ver:** kabul / kısmen / ret.
   - Gerekçe zorunlu.
   - Ret de geçerli bir karardır, ama "yazar zaten öyle düşündü" gerekçe sayılmaz.
   - Kritik bulgular çözülmeden METHOD-v1 yazılmaz. Çözülemiyorsa açık soru olarak Batu'ya taşınır.
2. **Taslağı revize et** ve `METHOD-v1.md`'yi yaz. Yapı ENTEGRASYON.md'deki gibidir. Özet ve izlenebilirlik matrisi de güncellenir.
3. **DEGISIKLIK-KAYDI.md'yi yaz.** Her satır: bulgu kimliği, karar, gerekçe, METHOD-v1'de değişen yer.
4. **Ağırlığı yeniden kontrol et.** Eleştirilerin eklettiği her şey ağırlık bütçesine girer. "Her eleştiriye yeni bir tören" yaklaşımı kabul edilmez.

## Dönüş
Ana oturuma en fazla 250 kelime dön:
- dosya yolları;
- kaç bulgunun kabul, kısmen ya da ret edildiği;
- Batu'ya taşınan açık sorular;
- en büyük kalan risk.
