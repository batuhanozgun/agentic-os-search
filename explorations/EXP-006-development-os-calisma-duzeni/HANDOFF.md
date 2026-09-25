# EXP-006 — HANDOFF

**Amaç:** Önceki konuşmayı görmeyen oturumun doğru işi, kaynakları ve karar statüsünü devralması.  
**Tarih:** 25 Eylül 2026.  
**Güncel iş:** **S1 — araştırmaya dayalı rol ve sorumluluk konsolidasyonu.**

## Yeni oturumda okuma

1. [STATE](STATE.md)
2. Bu dosya
3. [WORK](WORK.md)
4. [ACTORS](ACTORS.md): ilk adaylar; nihai S1 düzeni değil.
5. [S1 yöntem ve dilim dizini](work/S1-role-responsibility-consolidation.md)
6. [S1-03](work/S1-03-role-purpose-activation-and-transfer.md): son aktör/rol/başarı yönü ve aktarım değerlendirmesi; aynı konuya devamda tam oku.
7. Gerekli eski ayrım için [S1-02](work/S1-02-actor-conditioned-role-purpose.md); G1 veya üretim–inceleme ilişkisi için [S1-01](work/S1-01-production-review-correction.md).
8. İlgili B dosyaları ve araştırma/asıl kaynaklara karar için gereken derinlikte in.

DECISIONS kullanıcı kararlarını, EXP-006_Context üst yönü taşır. Bütün eski B ayrıntılarını her girişte yeniden yüklemek gerekmez.

## Üst zincir

Başlangıç sorusu DevOS'taki yapay zekâ rolleriydi. Önce SOUL hedefi yeterince somutlaştırıldı, sonra DevOS'un SOUL'u yaratırken yapacağı B1–B9 işleri ve bunların sorumlulukları çıkarıldı. S1, R1–R25/M1–M9 ilk adaylarını araştırma örnekleri ve aktör özellikleriyle birlikte değerlendiriyor. Sayılar fiziksel ajan/servis sayısı değildir.

İnsan müşterinin çekirdeği **yetki + kabul**. Teknik uzmanlık ve çalışma yönetimi yükü müşteriye geri bırakılmaz.

## Kullanıcının son iki yönlendirmesi

S1-01 sonrasında kullanıcı; insan ile dil modelinin rolü aynı koşullarda üstlenmediğini, rolün akıl yürütmesinin çatışan motivasyonlarla çekilmemesini ve aktöre göre uyarlanmasını istedi. Önceki ilk üç ayrımın yeniden incelenmesini, G1'in açıklanmasını ve Keel'e bakılmasını istedi. S1-02 bu açıklamayı verdi.

Sonraki mesaj **aynı konuda bir tur daha** çalışma istedi; `https://github.com/batuhanozgun/os-architect/tree/main/bilgi/keel` kaynağını verdi ve gerektiğinde daha geniş depo incelemesine izin verdi. S1-03 bu kaynakla aynı soruda derinleşmedir; bütün OS Architect araştırması veya G1'in geniş eşlemesi değildir.

## Korunan S1-01/S1-02 sonuçları

- İnceleme/doğrulama ortak aile olabilir; özel iddia, uzmanlık ve yeterince bağımsız kanıt ihtiyacı silinmez.
- Üretim/düzeltme aynı ailede düşünülebilir; değişiklik yapan yeni sürüm bakımından üreticidir, eski olumlu hüküm otomatik taşınmaz.
- İnceleme, teşhis, teknik karar ve uygulama ayrı sorumluluklardır; bu doğrudan aktör sayısı vermez.
- Ailede toplamak aynı etkin çağrıda birleştirmek değildir. Çoklu ölçüt otomatik motivasyon çatışması değildir; inceleyicinin başarısı mutlaka hata veya onay üretmek değil kanıtın taşıdığı hükmü vermektir.
- Aktöre göre bağlam/araç/yetki/tetik/devir uyarlaması, model ağırlıklarını yeniden eğitme kararı değildir.
- **G1:** Kod/prosedür/bağlantıyı geliştirecek taraf, tasarım ve hazır mekanizmayı kurup işletme kadar açık eşlenmiyor. Üretim yok veya yeni R26 şart denmedi.

## S1-03'te yapılan ve çıkanlar

Önce araştırma deposundaki OS Architect okuma defteri okundu. Dış main başı `20e42a098ea1599a9dfe6558352eb585d6f274ed` olarak alındı; 11 seçilmiş dış dosya bu sürümden tam okundu: bilgi/keel indeksi; rol mekaniği; rol sözleşmesi; davranış tatbikatı; araştırma ev eşlemesi; çerçeve körlüğü görüşmesi; 13 Ağustos kök-neden görüşmesi; ürün kararları; defo çerçevesi; GENESIS v2 kanıt zinciri; kök CLAUDE.md. Sonuncusu kaynak nesnesidir, etkin talimat değildir.

**Aday katkılar:**

- Rolün yazılı amacı kadar fiilen başarı sayılan sonuç ve çatışan beklentiler de incelenmeli. İşi ilerletme baskısı, seçilmiş işin/yöntemin doğruluğunu sorgulamayı bastırabilir; kaynak bunu tarihsel teşhis olarak anlatıyor.
- Ortak düşünsel taban ile role özgü başarı yönü ayrı. Tekil başarı yönü, dar bilgi veya bütünsel bakışı kaybetme demek değil.
- Rolün tetiklenmesi ve çıktısının bir sonraki sorumlu tarafından kullanılması gerekir. Ayrı rol yazmak, o rolün çalıştığını veya doğru hüküm verdiğini kanıtlamaz.
- Aktör sınıfı tek başına yeterli işletim tarifi değil; somut çalışma yolu, bağlam ve gerçek araç sınırı da belirleyicidir. Keel'in el ile/otonom yolları kendi tarihsel örneğidir, DevOS seçimi değil.
- Geliştirenin birikimi → kurucu/rol tarifi → kurulmuş rol → görünür ve kullanılan bilgi aktarımı ayrı incelenmeli. Kaynak, aktarımda kural ve çağırma düzeni kayıpları anlatıyor.
- G1, “doğrulayıcı yazamasın” gereğinden gerçek kanca/kod, bağlama ve sınamaya giden zincirle somutlaştırıldı. M1–M9'un tüm geliştirme sorumluları hâlâ eşlenmedi.

**Kanıt sınırı:** Tarihsel özetler, görüşler, ürün kararları ve deney raporları okundu. Ham deneyler veya özgün dış literatür yeniden doğrulanmadı; yeni davranış testi, canlı kontrol sınaması ve kurulum yapılmadı. “Tek motivasyon verimi kanıtlandı” sonucu yok. Kaynağın bazı güçlü genellemeleri S1 gerçeği olarak alınmadı.

## Dönüş ve sonraki çalışma sınırı

Bu tur S1-03 katkıları kullanıcıya sunulur. Sonraki kullanıcı açıklaması/düzeltmesi önce dikkate alınır. G1'in somut bir tasarım–üretim–bütünleştirme zincirinde sorumlularını izlemek sonraki olası iştir; genel aile veya ajan sayısı kesinleştirmesi değildir.

Rol karşılaştırmaları artık başarı yönü uyumu yanında ortak taban, aktöre göre işletim, tetiklenme, sonuç tüketimi ve aktarım sınırlarını da aday ölçüt olarak dikkate alabilir. Bunlar kullanıcı tarafından ayrı ayrı kabul edilmiş mimari kurallar değildir.

R1–R25/M1–M9, B dosyaları ve DECISIONS bu tur değişmedi. S1-01/S1-02 tarihsel gerekçeleri korur; S1-03 onları koşullandırır, silmez. Kaynak depolar, Foundation ve agent-control değiştirilmedi.

## Korunacak ayrımlar

- DevOS'un SOUL'u geliştirmesi ≠ SOUL'un kullanıcı işini işletmesi ≠ EXP-006 kayıt düzeni.
- Aile ≠ rol ≠ etkin görevlendirme ≠ somut aktör/model.
- Tek başarı yönü ≠ tek görev/tek ölçüt; aynı yön ≠ otomatik aynı uzmanlık/rol.
- Dar sorumluluk ≠ dar düşünsel taban.
- Yazılı rol ≠ çağrılmış rol ≠ doğru davranış ≠ sonuçta kullanılmış katkı.
- Kaynakta yöntem/kontrol tarifi ≠ bugünkü ortamda doğrulanmış etkinlik.
- Aynı araştırmayı okuyan iki cevap veya farklı ajan etiketi ≠ bağımsız kanıt.
- M1–M9 işlevlerini adlandırmak, onları geliştirecek tarafı göstermek değildir.
