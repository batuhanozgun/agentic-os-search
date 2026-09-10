# EXP-001 — Yaşayan aktarım planı

**Güncel durum otoritesi:** [STATE.md](STATE.md). Bu plan toplam işi ve alt görevlerin durumunu görünür tutar. `Bitti` sözcüğü yerel kopyayı, remote yayını ve kaynak sadakatini tek hükme indirmez.

## 1. Kaynakları güvenceye al

| Alt iş | Durum | Not |
|---|---|---|
| 1.1 Altı özgün dosyayı bul, byte-eşit koru, hash'le | YEREL TAMAM | SOURCE-MANIFEST altı özgün kimliği taşır. |
| 1.2 ZIP'i güvenle aç, üyeleri karşılaştır | YEREL TAMAM | CRC sağlam; 26 üye, orijinal ad/göreli yol korunuyor. |
| 1.3 U001–U019 görünür kullanıcı metinlerini aktar | MAIN ÜZERİNDE | 19 mesaj; ham platform export'u değil. |
| 1.4 S001–S018 substantive cevapları aktar | MAIN ÜZERİNDE | 18 ayrı dosya; tarihsel yanlışlar sonradan sessizce düzeltilmedi. |
| 1.5 Kaynak kesimi ve normalizasyonu açıkla | MAIN ÜZERİNDE | Aktarım hatası düzeltme notu; araç/private içerik dışarıda. |
| 1.6 Özgün 32 payload'ı remote'a yayımla | **BEKLİYOR** | Dosya aktarım yoluna bağlı; gerçek byte'lar tamamlama ZIP'inde. |

## 2. Düşünce gelişimini işle — MAIN ÜZERİNDE

2.1 LEARNINGS: 15 kaynak bağlantılı kazanım ve sınırı.  
2.2 EVOLUTION: 13 çerçeve/değişim evresi; özellikle kullanıcı düzeltmeleri.  
2.3 Konsolidasyon, Atlas ve sonraki yaşayan plan tartışmasının ayrı kesimleri.  
2.4 OPEN-QUESTIONS: 9 açık konu; araştırma/uygulama yetkisine çevrilmedi.

## 3. Yeniden çağırma yolları — MAIN ÜZERİNDE

3.1 Root README → explorations INDEX/CATALOG → EXP-001 INDEX/STATE.  
3.2 Research root'unda ayrı denemeler kütüphanesine kısa cross-link.  
3.3 TOPIC-MAP: roman, mimar, kulübe, alet çantası, D-02, C bitmeden başlama ve başka dala not gibi hatırlama ipuçları.  
3.4 RESEARCH-REFERENCES: tarihsel snapshot/blob ve güncel kaynak yolları.  
3.5 Sonraki EXP'ler için `builds_on/revises/contrasts_with` ilişkileri; tekrar bağımsız kanıt değildir.

## 4. Doğrulama — KAPSAMA GÖRE AYRI

| Kontrol | Durum |
|---|---|
| 37 görünür kaynak mesajının sıra/kimlik kapsamı | Yayımlanan kaynak dizini ve tree üzerinden denetlendi. |
| Önemli düğümlerin remote içerik okuması | Kullanıcı metinleri, demo D-02, mesleki standart düzeltmesi ve retrieval girişleri seçici okundu. |
| Kaynak metninin ham platform export'una byte diff'i | YAPILMADI / export yok. |
| Yerel altı orijinalin hash, PDF sayımı ve ZIP CRC'si | TAMAM. |
| Tamamlama helper'ının dar kopyalama kontrolleri | 9 yerel kontrol geçti; remote yayın değildir. |
| Remote özgün eserlerin byte/hash readback'i | **YAPILMADI / payload eksik.** |
| İzinli path sınırı | GitHub compare ile yalnız README, explorations ve research/INDEX eki görüldü. |
| Bütün historical dış URL'lerin ve sandbox linklerinin canlılığı | İddia edilmiyor; tarihsel adresler ve güncel yönlendirme ayrıldı. |
| Her link fragment'inin tarayıcıda bağımsız testi | YAPILMADI; kimlikli mesaj bağlantıları ve önemli okuma yolları seçici incelendi. |

## Bir sonraki somut iş

[PAYLOAD-TRANSFER](checks/PAYLOAD-TRANSFER.md) yolunu izle. Kullanıcının tamamlama ZIP'ini al; sadece manifestteki 32 payload'ı mevcut repository'ye doğrula/kopyala/yayımla; sonra remote içerik kimliklerini doğrula ve metadata'yı gerçek sonuca göre güncelle. Farklı mevcut dosyayı veya unrelated kullanıcı değişikliğini ezme.

Bu adım tamamlanmadan genel arşiv durumunu COMPLETE yapma. Yeni kapsam veya yeni araştırma açma. Aktarım başka turda devam ederse konuşmayı tekrar özetlemek yerine bu exact kaldığı yerden sürdür.
