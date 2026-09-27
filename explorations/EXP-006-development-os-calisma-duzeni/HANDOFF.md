# EXP-006 — HANDOFF

**Güncelleme:** 27 Eylül 2026, P3 başlangıç tartışması.  
**Devralma:** **P3 DISCUSSION BASELINE / CANDIDATE / USER DISCUSSION. P3 TAMAMLANMADI.** P2 ilk sözleşme taslağı korunuyor; P1 kaynaklı harita, runtime sınanmadı. P4–P6 başlamadı.  
**Üst amaç:** SOUL'u geliştirecek Claude Code cloud ekibinin çalışma düzeni; assistant'ın SOUL backlog'unu seçmesi değil.

## 1. Okuma yolu

[STATE](STATE.md) → HANDOFF → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) → [P1-01](work/P1-01-claude-cloud-environment-map.md) → [P2-01](work/P2-01-named-role-contracts.md) → [P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı conversation içinde tam unchanged içerik tekrar yüklenmez.

S1 gerekçesi için S1 master/ilgili slice; iş kapsamı için B dosyalarına inilir. P3 Work/Information Foundation'ını, ardından ilgili studies'i gerçekten kullanır. P3-01 §7 bu turun yeni okumalarıyla aynı konuşmadan yeniden kullanılan kaynakları ayırır; bütün korpus veya asıl dış kaynaklar yeniden okunmuş değildir.

## 2. Neden bu noktadayız?

SOUL hedefinden B1–B9, R/M ve S1 aile konsolidasyonu oluştu. Kullanıcı ilk SOUL işini dışarıdan seçme yönünü düzeltti; bunu kurulacak ekip yapmalı. Cloud hedefi, K1 iletişim ve K2 rutin kullanıcı tetiklemesi gerekmemesi belirlendi. P1–P6 bu aynı EXP-006'nın master planıdır.

P1 kaynak resmi rol tasarımını besledi; teknik seçim P4'e bırakıldı ve kullanıcı bunu anlayarak P2'ye devam istedi. P2'de DR01–DR16 ilk sözleşmeleri üretildi. Son kullanıcı mesajı P3'ün önemini vurguladı; araştırma örneklerinden yararlanıp **hemen karar vermeden bir yapı sunmamızı ve birlikte derin değerlendirmemizi** istedi. Bu nedenle current iş P3'ü bitirip P4'e geçmek değil, ilk öneri üzerinde diyalogdur.

## 3. Korunan P2 ve kapsam sınırları

ACTORS isim/lineage registry'si, P2-01 sözleşme kaynağıdır. 16 rol 16 agent değildir. İş keşfi bütün rollerden beslenir; DR01 bütünleştirir. DR06 akışı işletir; bütün teknik hükümleri üstlenmez. DR07 kalıcı lifecycle, DR08 consumer görünümü; DR04/11/13 sınama tasarımı, yürütmesi ve güvenceyi ayırır. DR02/13 gerekli alan profiliyle çalışır. P3 somut uyumsuzluk gösterirse P2'ye hedefli dönüş mümkündür.

Motivasyonun rolün başarı yönü olarak içeride yazılması aday yorumdur. Runtime allocation, dosya biçimi veya motivasyon başına agent seçilmedi. R1–R25/M1–M9 ve S1-17'nin candidate/closure-ready sonucu korunur. S1-16 full-read qualification'ı S1-17 §7'dedir.

K1 talep→çalışma→yanıt→kullanımı; K2 her rolü Batu'nun açmamasını ister. Başlatma/yeniden başlatma, gerçek müdahale ve yetki/kabul mümkündür; sınırsız gözetimsizlik hedef değildir. SOUL ürünleri ile DevOS çalışma/bilgi/kanıt kayıtları ayrı amaçlıdır; fiziksel depolama seçilmedi. Kanon/v2/ECC hazır mimari olarak alınmadı.

P1 Q01–Q06 cloud araç/sürüm/erişim, plugin doküman çelişkisi, kalıcılık ve güvence açıklarıdır. Bunlar belgeyle çözülmüş veya P3 önerisiyle doğrulanmış sayılmaz. Teknik seçim yük taşıdığında hedefli P1 kontrolü gerekir.

## 4. Current tartışma önerisi

[P3-01](work/P3-01-work-information-discussion.md) önerisi: **ortak iş-bilgi zemini üzerinde ihtiyaç etrafında çalışma halkaları**.

Üç mantıksal unsur: yaşayan iş ağı; gerekli rollerin belirli soru/teslimat etrafındaki işbirliği; kalıcı bilgi ve role özgü bağlam. Bu ne üç modül ne tüm rollerin her işte sırayla çağrıldığı bir süreçtir.

İlk somutlaştırma bir tasarım sırasında araştırma ihtiyacıdır: soruyu/karar bağını açma → uygun katkıyı etkinleştirme → kaynaklı yanıt → talep sahibinin sonucu kullanması veya gerekçeli reddi → etkilenen iş/kayıt/bağlamın güncellenmesi. SOUL'un gerçek ilk işi veya çalıştırılmış deney değildir.

Başlangıç önerisinde koordinatör akışın sahibidir, bütün kararların sahibi değil. Teknik karar ilgili yetkili uzmanlıkta; kanıt hükmü güvencede; yetki çatışması ilgili authority yolunda kalır. Karar/veto ve küçük danışma/ayrı Work sınırı henüz üzerinde anlaşılmış sözleşme değildir. Bu bölümü accepted tasarım diye devralma.

## 5. Sonraki sorumluluk ve durma

**Önce kullanıcı bu öneriyi değerlendirecek.** İlk konuşma odağı: bir rolün katkı talebi nasıl işe dönüşür; açık talebi, akışı ve teknik kararı kim taşır? Kullanıcının tepkisiyle aynı öneri üzerinde derinleş; her tur yeni sistem veya tümden yeni plan kurma.

Devam açıklıkları: konuya göre karar/itiraz/veto; küçük danışmanın kayıt ağırlığı; bağlam yeterliği ve kaynaklara geri dönüş; yeni sürümün tüketiciye etkisi; bekleyen işin devir ve durma yolu; başlangıç grant/yeterlik/tetik önkoşulları. Bunlar sonraki P3 diyalog konularıdır; bu listeyi otomatik uygulama kuyruğuna çevirme.

P3 tamamlandı deme ve P4'e geçme. P4 bütünleşik teknik seçim, P5 dosya/mekanizma, P6 gerçek sınamadır. Henüz keşfedilmemiş SOUL görevini assistant seçmez. Yeni bir design baseline'ı kaydetmek onu kabul ettirmek değildir.

## 6. Kayıt ve kullanıcıya dönüş

P3 ayrıntısı P3-01; current STATE; devir HANDOFF; bütün harita WORK. Rol adı/sözleşmesi ancak tartışmada somut değişirse ACTORS/P2-01'e yansır. Bu tur onlar değişmedi. Kaynak atıfları ve aday gerekçeler accepted karar tablosuna taşınmaz.

Kullanıcıya başlangıç yapısını, anlaşılır bir etkileşim örneğini ve tek odaklı tartışma noktasını kısa ver. Derinlik birden çok odaklı konuşmayla açılır; uzun iç değerlendirme metni veya bütün araştırma geçmişi varsayılan cevap değildir.
