# EXP-001 — STATE

**Arşiv durumu:** PARTIAL — görünür diyalog ve yeniden kullanım metinleri `main` üzerinde; özgün eser dosyalarının GitHub aktarımı eksik.  
**Denemenin statüsü:** Kavramsal prova / sentetik demo / taslak mekanizma modeli. Bağımsız sistem doğrulaması veya mimari kabul değildir.  
**Yetki:** U018'deki arşivleme talebi, S018 planı ve U019 uygulama/devam onayı.  
**Kaynak kesimi:** U001–U019 ve S001–S018. Bu arşivleme çalıştırmasının son raporu bu özgün kesime dahil değildir.

## Repository'de tamamlanan bölüm

- `agent/` ve `research/` yanında `explorations/` kütüphanesi kuruldu; root README ve research/INDEX çapraz yönlendirmesi eklendi.
- 19 kullanıcı mesajı ve 18 substantive assistant cevabı, konuşmacı/sıra/kimlikleriyle aktarıldı. [Diyalog INDEX](sources/conversation/INDEX.md).
- 15 kaynak bağlantılı öğrenme kaydı, 13 evreli düşünce/düzeltme izi, 9 açık soru grubu, konu haritası ve araştırma kaynak yolları yayımlandı.
- Konsolidasyon, Atlas ve Atlas sonrası yaşayan plan tartışmasının ayrı kesimler olduğu kaydedildi. Eski eserler yeni görüşlerle yeniden yazılmadı.
- Eser envanteri, altı özgün dosyanın hash/size manifesti, aktarım sınırı ve sonraki devralma hareketi görünür.

## Kaynak sadakati sınırı

Bu, modele görünür konuşma metinlerinin assistant tarafından yapılmış kapsamlı aktarımıdır; platformun ham export'u veya bağımsız byte-perfect transcript doğrulaması değildir. Tarihsel citation/sandbox işaretleri korunur; yeni erişim garantisi sayılmaz. Bir aktarım yazım hatası kaynak ifadeye geri çevrildi ve [TRANSCRIPTION-NOTE](checks/TRANSCRIPTION-NOTE.md) içinde kaydedildi.

## Yerelde güvenceye alınmış, GitHub'da eksik bölüm

Altı özgün dosya: konsolidasyon Markdown/PDF, Atlas HTML/PDF/ZIP ve kullanıcının PNG çizimi. Bunlar byte-eşit kopyalandı; 35/51 PDF sayfaları dosyadan sayıldı. ZIP CRC kontrolü geçti; 26 üye güvenli göreli yollarla çıkarıldı. Toplam 32 payload'ın byte'ları yerel **EXP001_Artefakt_Tamamlama_Paketi.zip** içinde korunur.

**Bu 32 dosyanın GitHub'a aktarımı tamamlanmadı.** SOURCE-MANIFEST'te bu nedenle `github_payload: pending` kalır. Yalnız hash veya burada yazılı yol, remote dosyanın varlığı sayılmaz.

Tamamlama ZIP'i: 3.416.116 byte, SHA-256 `054983b46aaa6ac33b226445ce194c1125ff89e5a7a1e4bdbc11cb579783a5a2`.

## Doğrulama ve operasyonel sınır

GitHub metin yayımlama yolu bu tur yeniden keşfedildi ve kullanıldı; önceki turdaki salt-okuma sınırı geçerli kabul edilmedi. Yayımlanan tree/commit ve seçili kaynak içerikleri yeniden okundu. `917d981... → 55499db...` karşılaştırmasında 37 dosya değişikliği yalnız izinli alanlarda: root README, explorations ve research/INDEX'e dört satır ek. `AGENT.md`, `agent/**`, Foundation ve diğer studies değiştirilmedi. Denetim ayrıntısı [ARCHIVE-COVERAGE](checks/ARCHIVE-COVERAGE.md).

Büyük yerel payload'ları doğrudan dosya yolu ile alan bir connector eylemi bulunmadı; alternatif yerel ağ yolu host çözümlemesinde başarısız oldu. Büyük dosyalar bozuk veya eksik literal kopyaya dönüştürülmedi. Bu sınıra uygun, hash kontrollü tamamlama paketi hazırlandı.

## Sonraki yetkili hareket

**Yalnız eksik 32 özgün payload'ı, dosya aktarımı yapabilen Git/GitHub ortamından yayımla; remote readback/hash denetiminden sonra STATE/manifest/coverage kayıtlarını güncelle.** Giriş: [PAYLOAD-TRANSFER](checks/PAYLOAD-TRANSFER.md). Kullanıcıya verilen ZIP'in gerçek byte'ları gerekir; hash'ten veya konuşma özetinden eser yeniden oluşturulmaz.

Ham platform export'u elde edilirse aktarım sadakati ayrıca denetlenebilir; bu artık varmış gibi gösterilmez. Yaşayan plan araştırması, Atlas v0.2, SOUL veya Development OS implementasyonu bu devam işinin parçası değildir.
