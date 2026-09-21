# EXP-004 — Arşiv onarımı çalışma planı

**Durum: REOPENED / SOURCE-FIDELITY-REPAIR-IN-PROGRESS.** Önceki CLOSED yalnız teknik yayını kapatmış, kaynak sadakatini gereğinden güçlü sunmuştur. [Onarım kaydı](checks/REPAIR-20260921.md).

## Yetki ve durma sınırı

U016, yeni kavramsal testten önce repository eksiklerini onarma yönüdür. Bu tur yeni stress testi, SOUL mimarisi veya Development OS uygulaması yapılmaz.

## İş sırası

1. İlk yoğunlaştırılmış S001–S013 ve eski manifesti açık tarihsel görünüm konumunda koru.
2. Görünür özgün S001–S013 yanıtlarını kısaltmadan aktar.
3. Yayın cevabı S014, U015/S015 T08 devamı ve U016 açıklamasını kaynak sırasına ekle.
4. Kaynak metin, türetilmiş eser, kullanıcı örneği ve mimari kabul ayrımını koruyan güncel STATE/INDEX/manifest/okuma yollarını düzelt.
5. Paket içi bağlantıları, mesaj kapsamını, kaynak sonlarını ve korunan tarihsel kimlikleri kontrol et.
6. Yalnız yetkili değişiklikleri main'e yayımla; yayın kimliği ve karşılaştırmayla kapsamı geri doğrula.

## Kapanış ölçütü

Özgün görünür gövdeler kaynak yollarında bulunur; eski yoğunlaştırmalar kaynak diye yönlendirilmez; kapsam ve manifest gerçek dosyalarla eşleşir; yeni kullanıcı açıklamaları karar gibi kabul edilmez; main yayını ve kontrol sınırları kayıtlı olur. Henüz bu ölçüt karşılandı denmez.
