# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu DevOS tasarım çalışması.  
**Güncelleme:** 27 Eylül 2026, P3 başlangıç tartışması.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak.  
**Current:** **P3 DISCUSSION BASELINE / CANDIDATE / USER DISCUSSION. P3 TAMAMLANMADI.** P2 ilk rol taslağı korunur; P1 kaynak incelemesi tamam, runtime sınanmadı. P4–P6 başlamadı.  
**Planın tek ana yüzeyi:** [WORK — master plan v1.3](WORK.md).  
**Son kullanıcı yönü:** Bu en önemli bölümü araştırma örnekleri/metodolojileriyle derin konuş; hemen karar verme; önce bir yapı sun, birlikte değerlendirelim. Bu istek P3'te tartışma başlangıcını yetkilendirir; tasarım kabulü veya P4'e geçiş değildir.

## Sabit kapsam ve sınırlar

- **Environment:** Claude Code cloud. P1 belge resmi var; gerçek hesap/oturumun sürüm, araç, izin ve kalıcılık yeterliği henüz gösterilmedi.
- **SOUL'u geliştiren:** Kurulacak DevOS ekibi. İlk ve sonraki SOUL işlerini ekip keşfeder, değerlendirir, planlar ve yürütür. Assistant ekibin çalışma düzenini tasarlar; gerçek SOUL backlog'unu onun yerine seçmez.
- **K1 iletişim:** Talep → ilgili rolün çalışması → yanıt → gerçek kullanım. Teknik yöntem P4'e kadar açık; yazılmış mesaj veya var olan rol dosyası yeterli değil.
- **K2 ilerleme:** Rutin rol geçişini Batu tetiklemez. Başlatma/yeniden başlatma, gerekli müdahale, meşru yetki ve kabul mümkündür; sınırsız özerklik hedef değildir.
- **Loopinance:** Kanon manuel tetikleme karşı örneği; v2 yalnız rutin kullanıcı tetiklemesi gerekmemesinin örneği. V2/ECC bütün olarak benimsenmedi.
- **Bilgi:** SOUL ürün çıktıları ile DevOS'un kendi iş/bilgi/karar/kanıt/devam kayıtları ayrı amaçlarla, ilişkileri korunarak yönetilir. Fiziksel depolama şeması seçilmedi.
- **Kaynak kullanımı:** Foundation gerekli ayrımları ve soruları açar; studies uygulama/karşı örnekler sağlar. Kaynak ismi veya yönerge varlığı davranış kanıtı değildir.

Kullanıcı kararları [DECISIONS](DECISIONS.md), kapsam kaynakları [U002](sources/U002-cloud-plan-and-autonomy.md)'dedir. Kullanıcıyla derinlik, kısa ve odaklı turlar içinde açılır; tek yanıtta bütün muhakeme anlatısı verilmez.

## Önceki birikim

SOUL hedefi → B1–B9 kapsamı → R1–R25/M1–M9 ilk türetim → S1-01–S1-17 → F1–F8 aday aileleri → P1–P6 planı.

S1-17 CLOSURE-READY / CANDIDATE korunur; kullanıcı kapanışı, nihai kadro veya sekiz ajan sonucu çıkarılmaz. B1–B9 referans kapsamdır, gerçek SOUL sırası değil. S1-16 tam-okuma iddialarının qualification'ı S1-17 §7'dedir. Somut yeni çelişki yoksa S1 taxonomy'si baştan çalışılmaz.

[P1-01](work/P1-01-claude-cloud-environment-map.md) kaynaklı Environment haritasıdır; canlı test değildir. Q01–Q06 erişim, araç, plugin, kalıcılık ve güvence açıkları korunur. Bu tur yeni Claude özelliği veya yeterlik iddiası üretilmedi.

[ACTORS](ACTORS.md) DR01–DR16 isim/lineage registry'sidir; [P2-01](work/P2-01-named-role-contracts.md) amaç, girdi/yeterlik, tetik, teslimat/tüketici ve yetki sözleşmelerini taşır. 16 sözleşme 16 agent değildir. Motivasyonun rolün başarı yönü olarak içeride tutulması aday yorumdur. DR02/DR13 gerekli alan profiliyle çalışır; bütün uzmanlıklar tek genel aktöre yüklenmez. R1–R25 mekanik eşleme kontrolü actual competence veya bağımsız doğrulama değildir.

## P3 tartışma başlangıcı

**Tek ayrıntı kaydı:** [P3-01 — iş merkezli işbirliği ve bilgi döngüsü](work/P3-01-work-information-discussion.md).

Başlangıç önerisi: **yaşayan iş ağı + ihtiyaca göre çalışma halkaları + kalıcı bilgi/role özgü bağlam**. Mantıksal ayrımlardır; üç servis, üç dosya veya üç ajan kararı değil.

- Hazır görev kuyruğu veya 16 rolü sırayla çalıştıran bant değil; iş ve bilgi ihtiyaçları çalışma içinde keşfedilir.
- Koordinatör çağrı/devir/bekleme akışını taşır; bütün teknik kararları tek başına vermez.
- Talep sahibi açık ihtiyacı ve sonucu kullanmayı; katkıyı veren rol kendi teslimatını taşır.
- Kaydın güncellenmesi ile doğru tüketicinin güncel bilgiye erişip kullanması ayrı tutulur.
- Küçük danışma/ayrı Work, karar/veto, sürüm yayılımı ve bootstrap koşulları henüz çözülmedi.

Bu kaynaklardan türetilmiş tartışma adayıdır; kullanıcıca seçilmiş yapı, uygulanmış düzen veya K1/K2 kanıtı değildir. ACTORS/P2 sözleşmeleri değiştirilmedi.

## Current next responsibility ve durma noktası

**Şimdi:** P3-01 başlangıç yapısını kullanıcıya sun ve birlikte değerlendir. İlk odak, rolün katkı talebinin işe dönüşmesi ve **akış sahibi ile karar sahibinin ayrımı**dır. Kullanıcının sonraki değerlendirmesi bu bazın üzerinde işlenir; sessiz kabul varsayılmaz.

**Yapılmayan:** P3 kapatılmadı; P4 seçimi, P5 dosyaları, P6 canlı sınaması veya ilk SOUL görevi yapılmadı. P4'e otomatik geçme. Yeni somut rol çakışması çıkarsa P2'ye hedefli dön; bütün aile sınıflamasını yeniden açma.

**Sonraki harita:** P2 roller ↔ P3 iş/bilgi döngüsü → P4 bütünleşik alt ajan/takım ve allocation seçimi → P5 dosya/mekanizma → P6 sınama/devir. Teknik kurulum veya erişim için peşin sınırsız yetki yoktur.

## Fresh-session yolu

AGENT ve gereken kontroller → [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) → [P1-01](work/P1-01-claude-cloud-environment-map.md) → [P2-01](work/P2-01-named-role-contracts.md) → [P3-01](work/P3-01-work-information-discussion.md) tam okunur. Aynı konuşmada tam unchanged içerik korunabilir. Sonra aktif sorunun Foundation/studies kaynaklarına inilir.

S1/B/history/Context'in tarihsel next ifadeleri current planı yönetmez. Current rol adları ACTORS'ta, sözleşmeleri P2-01'de, tartışma önerisi P3-01'de, bütün plan yalnız WORK'tedir.
