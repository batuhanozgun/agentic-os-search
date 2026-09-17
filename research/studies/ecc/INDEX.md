# ECC — INDEX

Current work ve yetki için önce [STATE](STATE.md). Bu index keşif yoludur; çalışma durumunun ikinci otoritesi değildir.

| Gereksinim | Giriş |
|---|---|
| ECC'yi neden araştırıyoruz; neyi varsaymıyoruz? | [00-WHY-THIS-RESEARCH](00-WHY-THIS-RESEARCH.md) |
| Nesne, sürüm, aday değer ve kullanım sınırları | [META](META.md) |
| Nasıl araştırılacak; kanıt ve sentez nasıl korunacak? | [METHOD](METHOD.md) |
| Aşamalar, çıkış ölçütleri, ilk devam birimi | [PLAN](PLAN.md) |
| Açık sorular, rakip açıklamalar ve ayırt edici kanıt | [QUESTIONS](QUESTIONS.md) |
| Gerçekte hangi kaynak ne derinlikte okundu? | [SOURCE-LEDGER](SOURCE-LEDGER.md) |
| Turlar arasında bulgu/iş değişimi ve devam izi | [RESEARCH-LOG](RESEARCH-LOG.md) |
| Yöntem neye göre değişti; işe yaradığı gösterildi mi? | [METHOD-REVIEW](METHOD-REVIEW.md) |

## Progressive retrieval

`library CATALOG → META → STATE → aktif soru/plan → ilgili mekanizma notu → pinned kaynak`

Cold-start için tam okunacak küçük giriş dosyaları STATE'te sayılıdır. Büyüyen log, ledger ve notların tamamı her tur yeniden okunmaz. Buna karşılık soru/kanıt sınırı bir özette korunamıyorsa ilgili kaynak tam veya gereken exact aralıkla geri açılır.

## Future artifacts are not existing results

U01 gerekirse `inventory/STRUCTURE.md` ve dosya/kaynak manifestini üretir. Sonraki birimler ihtiyaç oldukça `notes/`, `syntheses/`, `evidence/` ve `revalidation/` yollarını oluşturur. CORE, proje-facing assessment ve yöntem vaka sentezi yalnız içerikleri hazır olduğunda eklenir. Şimdiden boş sonuç dosyaları veya sahte tamamlanma yüzdeleri yoktur.

Yayın tamamlandığında `PUBLICATION.md` commit/dosya kapsamı ve geri-okuma kontrollerini kaydeder. Dosya varlığı gerçek host davranışının veya bağımsız fresh-session başarısının kanıtı değildir.

## Authority separation

STATE current work; META sınıflandırma/reuse; PLAN tasarlanan işler; QUESTIONS soru statüsü; SOURCE-LEDGER kaynak kapsamı; RESEARCH-LOG tarihsel tur kayıtları; METHOD-REVIEW yöntem kararları ve etkileri. Bir alanın gerçeği değiştiğinde onun sahibi güncellenir, diğer dosyalardaki türetilmiş yönlendirmeler tutarlılık açısından kontrol edilir.
