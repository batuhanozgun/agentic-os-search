# EXP-006 — HANDOFF

**Amaç:** Önceki konuşmayı görmeyen bir oturumun doğru işi, kaynakları ve karar statüsünü devralması.  
**Tarih:** 25 Eylül 2026.  
**Güncel iş:** **S1 — araştırmaya dayalı rol ve sorumluluk konsolidasyonu.**

## Yeni oturumda okuma

1. [STATE](STATE.md)
2. Bu dosya
3. [WORK](WORK.md)
4. [ACTORS](ACTORS.md)
5. [S1 yöntem ve dilim dizini](work/S1-role-responsibility-consolidation.md)
6. [S1-02](work/S1-02-actor-conditioned-role-purpose.md): son aktör/rol/motivasyon değerlendirmesi; tam oku.
7. [S1-01](work/S1-01-production-review-correction.md): A1–A4 veya G1 geliştirilecekse tam oku.
8. İlgili B dosyalarına ve araştırma/asıl kaynaklara karar için gerektiğinde in.

DECISIONS kullanıcı kararlarını, EXP-006_Context üst yönü taşır. Bütün eski B ayrıntılarını her girişte yeniden yüklemek gerekmez.

## Üst zincir

Başlangıç sorusu DevOS'taki yapay zekâ rolleriydi. Önce SOUL hedefi somutlaştırıldı; sonra DevOS'un SOUL'u yaratırken yapacağı B1–B9 işleri ve bunların gerektirdiği sorumluluklar çıkarıldı. S1 bu adayları araştırmalara dayanarak birlikte değerlendirmektedir.

B1–B9'un ilk ayrıştırmaları tamamlandı; teknik doğrulama veya mimari değildir. ACTORS, R1–R25/M1–M9 ilk türetimlerini korur. S1 dosyaları sonraki aday değerlendirmedir; kimlikler henüz birleştirilmedi.

İnsan müşterinin çekirdeği **yetki + kabul**. Teknik uzmanlık ve çalışma yönetimi yükü müşteriye geri bırakılmaz.

## Son kullanıcı yönü

S1-01'in ardından kullanıcı şu noktaları gündeme getirdi:

- İnsan ile dil modeli aynı şekilde rol üstlenmez. Dil modelinin girdisi/bağlamı ve davranışı yönlendiren ifadeler önemlidir.
- Etkin rolün akıl yürütmesi iki çatışan motivasyon arasında çekilmemeli. Ailede gruplamak kabul edilebilir, fakat aktörün özellikleri hesaba katılmalıdır.
- Roller aktör türüne göre uyarlanabilir; aktör özelliklerini hangi aşamada ele alacağımız değerlendirilebilir.
- Önceki ilk üç ayrımı bu açıdan tekrar irdele; dördüncü maddedeki geliştirme sorumluluğu açıklığını anlat.
- Önce araştırma reposundaki Keel kaydına, sonra ilgili asıl Keel dosyalarına bak.

Bu mesaj geniş G1 ayrıştırmasını otomatik sürdürmek yerine yukarıdaki soruları önceliyor. Kullanıcının hipotezleri bilimsel olarak doğrulanmış veya katı mimari kural kabul edilmez.

## S1-01'den kalanlar

- A1: İnceleme/doğrulama ortak aile olabilir; uzmanlık ve bağımsız kanıt ihtiyacı silinmez.
- A2: Üretim/düzeltme aynı ailede olabilir; değişiklik yapan yeni sürüm bakımından üreticidir.
- A3: İnceleme, teşhis, teknik karar ve uygulama ayrı sorumluluklardır; aktör sayısı bundan doğrudan çıkmaz.
- A4: Yeni sürüm veya bütünleştirilmiş sonuç eski olumlu hükmü otomatik devralmaz.
- G1: Kod/prosedür/bağlantıyı geliştirme işinin taşıyıcısı, tasarım ve hazır sistemi kurup işletme kadar açık eşlenmemiştir. Üretim yok veya yeni R26 şart denmedi.

## S1-02'de yapılan

Keel'in research/soul-context/repos/keel/README.md kaydı tam okundu. Asıl main `669c5445cf34dcf15ed4f4d435b5f3657077550a` üzerinden GENESIS, G2, sözleşme kalıbı, defo modeli, rol açılış kalıbı ve doğrulayıcı dosyası okundu; README default main'den okundu. Tam/seçici kapsam ve bloblar S1-02'de.

Foundation aktör/rol/etkin katılım bulgusu da kullanıldı. Dışarıda Anthropic bağlam mühendisliği yazısı ile EMNLP 2024 rol kişiliği çalışmasının yayın özeti dar kapsamda kontrol edildi; tüm araştırma korpusu veya yeni deney değildir.

**Aday sonuç:** Ailede gruplamak ≠ aynı görevlendirmede çalıştırmak. Etkin rolün başarı yönü açık ve tutarlı olmalı; çoklu ölçüt otomatik çatışma değildir. İnceleyicinin işi mutlaka hata veya onay üretmek değil, kanıtın taşıdığı hükmü vermektir.

Aktörün genel koşulları önce kabaca ele alınabilir; rol ve somut görev belli olduğunda bağlam/araç/yetki/tetik/devir düzeni somut aktöre göre uyarlanır. Bu bir model eğitimi kararı veya zorunlu aktör > aile > rol hiyerarşisi değildir.

**G1 açıklaması:** Belleğin gereksinimini belirlemek; gerekli kod/bağlantıyı geliştirmek; onu kurmak/bütünleştirmek; davranışını sınamak farklı işlerdir. İkinci işin açık sorumlusunu göstermek istiyoruz. Geniş M1–M9 geliştirme eşlemesi henüz yapılmadı.

## Dönüş ve sonraki çalışma sınırı

S1-02 yanıtı kullanıcıya sunulur. Sonraki mesajdaki açıklama/düzeltme önce dikkate alınır. Yeni devam yönünde rol birleştirme ölçütlerine tutarlı başarı yönü ve aktöre göre işletim koşulları dahil edilir; G1 tasarım–üretim–bütünleştirme eşlemesi bunlarla sürdürülebilecek sonraki olası iştir.

Bu tur canlı model/Keel/DevOS testi, kurulum, kod üretimi, yeni rol, model eğitimi veya nihai aile sayısı yapılmadı. Keel'in kendi sabit kadro ve insan kapıları DevOS'a aktarılmadı. Kaynakta kontrol tarifi görmek, çalışan kontrolde başarı kanıtı değildir.

## Korunacak ayrımlar

- DevOS'un SOUL'u geliştirmesi ≠ SOUL'un müşteri işini işletmesi ≠ EXP-006 kayıt düzeni.
- Aile ≠ rol ≠ etkin görevlendirme ≠ somut aktör/model.
- Tek başarı yönü ≠ tek görev/tek ölçüt; tutarlı amaç ≠ denetimsiz yetki.
- Rol yönergesi ≠ modelin eğitimi; bağlam uyarlaması ≠ garanti edilmiş davranış.
- Farklı çağrı/ajan etiketi ≠ bağımsız kanıt.
- Keel'in bütün kusurları tek onay itkisine bağlaması, bütün modeller için kanıtlanmış yasa değildir.
- M1–M9'un işlevini yazmak onları geliştirecek tarafın yerine geçmez.

STATE/HANDOFF/S1 güncel yönü, S1-01/S1-02 gerekçeleri, ACTORS ise korunmuş ilk adayları taşır. Yeni önerileri kullanıcı onayı veya doğrulanmış nihai düzen sayma.
