# EXP-003 — STATE

**Durum:** PAYLOAD PREPARED / çalışma dalı; main yayını ve son geri okuma bekliyor.  
**Kaynak tarih:** 18 Eylül 2026; tekil mesaj saatleri üretilmedi.  
**Kaynak kesimi:** U001–U011 ve S001–S010: 21 mesaj, 11 kaynak dosyası.  
**Kaynak payload ref'i:** `3e3169305a545eb87694a269bc6318576a3ddb39`; uzak kaynak dosyaları 125.688 byte.  
**Başlangıç main:** `7d312c9e6dd26ec8393b5f4d94e99950775b16bf`.  
**Çalışma dalı:** `archive/exp-003-memory-20260918`.

## Amaç ve yetki

U011, konuşmayı baştan okuyup EXP-003 olarak kayıt altına alma yönüdür. Başlangıçtaki geçici terimler, kullanıcının kendi bilgisini sorgulama niyeti, işlem–mekanizma düzeltmesi, dosya–içerik ayrımı, seçici erişim, Foundation kullanımı, Karpathy/studies değerlendirmesi ve uzun vadeli sağlamlık hedefi korunur.

Yetki arşivlemedir. 'Daha sağlam yapıyı kurduk' U011'de gelecekte ulaşılmak istenen cümledir; henüz yapı, benchmark veya üstünlük yoktur. Foundation, studies, concepts, agent-control, eski EXP kaynakları ve Development OS/SOUL uygulaması değiştirilmez.

## Tamamlanan içerik

21 görünür kaynak mesaj [diyalog dizini](sources/conversation/INDEX.md) ile sıra ve konuşmacı korunarak aktarıldı. U011 sonrası yayın konuşması kaynak kesimine karıştırılmadı. Platform export'u veya bağımsız byte-perfect transcript değildir.

Konsolidasyon; kaynak bağlı kazanım/evrim/terim/açık soru kayıtları; nitelendirmeler; konu haritası; EXP-001/002 ile seçici kaynak devri ve 95 mesajlık toplu okuma yolu hazırlandı. 100→180 ve 240–345 puanları karşılaştırmalı kazanım tahmini olarak geri çekildi. Karpathy tam kaynak/pin ve studies okuma kapsamı açıkları ayrıca kaydedildi.

Kaynak kimlikleri [SOURCE-MANIFEST](SOURCE-MANIFEST.json) içindedir. Yayın ve gerçekten yapılan kontroller yalnız [PUBLICATION](checks/PUBLICATION.md) tarafından kaydedilir; payload hazırlığı main yayını değildir.

## Sonraki sınır

Bu paket için sıradaki iş yayın/kapsam/geri okuma kapanışıdır. Yeni araştırma veya tasarım açılmaz. Sonraki kullanıcı yönüyle toplu okuma, sınırlı kaynak araştırması veya hedefe yönelik tasarım düşünülebilir; hiçbiri bu kayıtla otomatik etkinleşmez.
