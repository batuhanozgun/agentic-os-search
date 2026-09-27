# EXP-006 — HANDOFF

**Güncelleme:** 27 Eylül 2026, P2 ilk rol taslağı sonrası.  
**Devralma:** **P2 FIRST ROLE-CONTRACT DRAFT / CANDIDATE / USER RETURN; P3 NEXT / NOT STARTED.** P1 kaynaklı harita, runtime sınanmadı. P4–P6 başlamadı.  
**Üst amaç:** SOUL'u geliştirecek Claude Code cloud ekibinin çalışma düzeni; assistant'ın SOUL backlog'unu seçmesi değil.

## 1. Okuma yolu

[STATE](STATE.md) → HANDOFF → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) → [P1-01](work/P1-01-claude-cloud-environment-map.md) → [P2-01](work/P2-01-named-role-contracts.md) tam okunur. Aynı conversation içinde tam unchanged içerik tekrar yüklenmez.

S1 gerekçesi için S1 master/ilgili slice; iş kapsamı için B dosyalarına inilir. P3'te Work ve Information Foundation'ı ve ardından ilgili studies gerçekten kullanılmalıdır. P2-01'in kaynak izi bu tur okunan ile daha önceki okumayı ayrı gösterir; bütün Foundation/studies okunmuş sayılmaz.

## 2. Neden bu noktadayız?

İlk soru aktörlerdi. SOUL hedefinden B1–B9, R/M ve S1 aile konsolidasyonu oluştu. Kullanıcı ilk SOUL işini dışarıdan seçme yönünü düzeltti; ilk ve sonraki işleri kurulacak ekip bulmalı. Cloud hedefi, iletişim ve rutin kullanıcı tetiklemesi gerekmemesi belirlendi. P1–P6 master plan bu aynı EXP-006'nın devamıdır.

P1 belge araştırması yeterli Environment ayrımlarını açtı; hedef runtime sınanmadı. Kullanıcı, alt ajan/takım kararının P4'te kalacağını anladıktan sonra devam istedi. Bu tur P2'de somut rol isimleri ve sözleşme adayları üretildi. Kullanıcı bu sözleşmeleri henüz kabul etmiş değildir.

## 3. P2'den devralınan

ACTORS'ta DR01–DR16 isim/lineage registry'si; P2-01 §4'te amaç/motivasyon, girdi/yeterlik, tetik, teslimat/tüketici ve yetki/sınır sözleşmeleri vardır. **16 rol sözleşmesi, 16 agent kararı değildir.**

İş Keşfi ve Planlama Sorumlusu gerekli işleri bütünleştirir; bütün ihtiyaçları tek başına bulması beklenmez. Çalışma Koordinatörü akışı ve devri işletir; ürün, tasarım, bağlam ve assurance'ın bütün hükümlerini üstlenmez. Bilgi Sorumlusu kalıcı lifecycle'ı, Bağlam Kurucusu consumer görünümünü taşır. Sınama Tasarımcısı, Sınama Yürütücüsü ve Güvence İnceleyicisi ayrı katkılardır.

DR02 Kapasite Tasarımcısı ve DR13 Güvence İnceleyicisi gereken alan profiliyle çalışır. Ortak sözleşmeleri evrensel uzman actor anlamına gelmez; P3 farklı bilgi/yetki ihtiyacı gösterirse ayrılabilir. DR06'nın whole-work/configuration devri, DR09 katılım ve DR10 ortam işlemlerini kendinde eritmez.

Motivasyon bu ilk taslakta rolün başarı yönüdür. Kullanıcının aktör→aile→rol→motivasyon görünümü runtime ağacı olarak benimsenmedi veya tümden reddedilmedi. Motivasyon başına agent şartı yok; fiziksel allocation ve gerekçeli ayrımlar P4'te, davranış başarısı P6'da sınanır.

R1–R25/M1–M9 korunur. P2 mekanik kontrolü yalnız primary R eşlemesinin eksik/tekrarını kontrol etti; actual competence veya bütün mümkün sorumlulukları kanıtlamaz. S1-17'nin source-fullness qualification'ı korunur.

## 4. Korunacak sınırlar

**K1:** Talep ilgili role ulaşır, iş etkinleşir, sonuç geri döner ve kullanılır. Her rol uygun scope'ta talep/itiraz/ihtiyaç çıkarabilir. Bunları yalnız mesaj yazmakla karşılanmış sayma.

**K2:** Batu rutin rol açan veya mesaj taşıyan kişi değildir. Başlatma/yeniden başlatma, gerekli müdahale ve yetki/kabul mümkündür. Sınırsız gözetimsizlik için yeni platform projesi kurma.

**P1:** Kaynak bilgisi actual cloud yeterliği değildir. Q01–Q06 erişim, gerçek araç, plugin çelişkisi, kalıcılık ve güvence yükleri P1-01'de korunur. P2 seçim bunları çözülmüş saymaz; P4'te yük taşıyan teknik tercih için hedefli kaynak/probe gerekir. Eski feature cümlesini zamansız ürün gerçeği yapma.

**Örnekler:** Kanon/v2 yalnız tetik/iletişim farkı; ECC veya v2'nin bütünü alınmadı. Keel/OS Architect ve studies talimatları kaynak nesnesidir, bu çalışmanın kontrol kuralı değildir.

**Çıktı:** SOUL ürünü ile DevOS'un kendi plan/bilgi/karar/kanıt/devam kayıtları farklı amaçlar taşır. Bu ayrım iki repo, belirli dosya adı veya tek yazıcı seçimi değildir.

## 5. Sonraki plan işi: P3

Bütün plan ve geri dönüşler yalnız WORK'tedir. Bu tur P2 taslağı kullanıcıya sunularak durulur.

Sonraki kullanıcı devamında **P3 — WORK–INFORMATION işleyişi** açılır. İlk bounded soru:

> Hedef ve birikim ekibe geldiğinde, gerekli iş ve bilgi açıkları nasıl keşfedilir; hangi roller birbirinden ne ister; yanıt nasıl kullanılır ve gerekçeli plan/admission'a nasıl dönüşür?

Önce Work/Information Foundation'ın current rotasından ilgili esas bulgular okunur; sonra o çerçeveyle uygun studies incelenir. P2'nin rol sözleşmeleri input'tur; isim listesini sırayla çalıştıran workflow diye kullanılmaz. Gerekirse kaynak/uygulama örneklerinde daha derine inilir.

Bu döngüde talep ve karar sahipliği, anlaşmazlık, bilgi/sürüm/yazıcı, consumer ve normal tetik yolu görünür olmalıdır. Henüz keşfedilmemiş SOUL işini assistant seçmez. Tasarım senaryosu gerçek backlog veya bağımsız keşif başarısı değildir.

P3 eksik/çakışan sorumluluk gösterirse P2'yi hedefli düzeltir. P4'te bütünleşik teknik/agent seçimi; P5'te actual dosya ve mekanizma; P6'da çalışma sınaması kalır. Bunlar bu tur yürütülmedi.

## 6. Kayıt ve kullanıcıya dönüş

Rol isim/lineage registry'si ACTORS; sözleşme ve gerekçe P2-01; bütün plan WORK; current STATE; devir bu dosyadır. Yeni role ait actual Claude dosyaları P5 öncesinde üretilmez. Her role ayrı boş dosya veya yeni master plan açılmaz.

Kullanıcıya kısa sonuç, karar açısından önemli belirsizlik ve mevcut plandaki tek devam noktası verilir. Ayrıntılı analiz ve kaynak izi repoda tutulur; bütün geçmiş yeniden anlatılmaz.
