# EXP-003 — Arşivleme çalışma planı

Bu dosya arşiv işini izler; yeni memory araştırma planı değildir. Durum [STATE](STATE.md), gerçekleşmiş yayın [PUBLICATION](checks/PUBLICATION.md).

| Aşama | Çıktı | Durum |
|---|---|---|
| P0 — Giriş ve kapsam | Kütüphane sözleşmesi, EXP kimliği, önceki denemelerle seçici devir; kaynak kesimi | Tamamlandı. EXP-003 başlangıç main'de yoktu. |
| P1 — Kaynak güvenceye alma | U001–U011, S001–S010; 11 kaynak dosyası | Çalışma dalında kaynak ref'i `3e3169305a545eb87694a269bc6318576a3ddb39`. |
| P2 — Açıklayıcı işleme | Konsolidasyon, kazanım, evrim, terimler, açık sorular, nitelendirmeler | Payload hazır. |
| P3 — Retrieval ve devir | Konu haritası, 95 mesajlık toplu okuma, predecessor ve araştırma yolları | Payload hazır; eski kaynaklar değiştirilmedi. |
| P4 — Yayın ve denetim | Kapsam karşılaştırması, main yayını, source kimlikleri ve kritik içerik geri okuması | Bekliyor; tamamlanmış sayılmaz. |

## Değişiklik sınırı

Yalnız `explorations/EXP-003-ek-hafiza-ve-arastirma-temelli-guvenilirlik/**` ve `explorations/INDEX.md`, `explorations/CATALOG.md`. Önceki EXP'lerin kaynaklarını veya araştırma statülerini değiştirme işi yoktur. Başka oturumların main değişiklikleri korunur; force push veya branch temizliği bu işin parçası değildir.

## Dönüş koşulu

Arşiv ve nitelendirmeler yayımlanıp gerekli geri okuma tamamlandığında kullanıcıya dönülür. Kaynakta geçen OpenViking→ai-memory önerisi ayrı research grant değildir. Plan tamamlandıktan sonra yeni tasarım/uygulamaya kendiliğinden geçilmez.
