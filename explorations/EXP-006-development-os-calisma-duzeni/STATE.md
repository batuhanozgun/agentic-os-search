# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu DevOS tasarım çalışması.  
**Güncelleme:** 27 Eylül 2026, P2 ilk rol taslağı sonrası.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak.  
**Current:** **P2 FIRST ROLE-CONTRACT DRAFT / CANDIDATE / USER RETURN.** P1 kaynak incelemesi tamam, runtime sınanmadı. **P3 NEXT / NOT STARTED**; P4–P6 başlamadı.  
**Planın tek ana yüzeyi:** [WORK — master plan v1.2](WORK.md).  
**Son kullanıcı yönü:** Kullanıcı alt ajan/takım kararının P4'te verileceğini anladığını belirterek devam istedi. P2 rol taslağı bu yetkiyle açıldı; taslağın kabulü veya P4 teknik seçimi uydurulmadı.

## Sabit kapsam ve sınırlar

- **Environment:** Claude Code cloud. P1 belge resmi var; gerçek hesap/oturumun sürüm, araç, izin ve kalıcılık yeterliği henüz gösterilmedi.
- **SOUL'u geliştiren:** Kurulacak DevOS ekibi. İlk ve sonraki SOUL işlerini ekip keşfeder, değerlendirir, planlar ve yürütür. Assistant ekibin çalışma düzenini tasarlar; gerçek SOUL backlog'unu onun yerine seçmez.
- **K1 iletişim:** Talep → ilgili rolün çalışması → yanıt → gerçek kullanım. Yöntem P4'e kadar açık; yazılmış mesaj veya var olan rol dosyası yeterli değil.
- **K2 ilerleme:** Rutin rol geçişini Batu tetiklemez. Başlatma/yeniden başlatma, gerekli müdahale, meşru yetki ve kabul mümkündür; sınırsız özerklik hedef değildir.
- **Loopinance:** Kanon manuel tetikleme karşı örneği; v2 yalnız rutin kullanıcı tetiklemesi gerekmemesinin örneği. V2/ECC bütün olarak benimsenmedi.
- **Bilgi:** SOUL ürün çıktıları ile DevOS'un kendi iş/bilgi/karar/kanıt/devam kayıtları ayrı amaçlarla, ilişkileri korunarak yönetilir. Fiziksel depolama şeması seçilmedi.
- **Kaynak kullanımı:** Foundation gerekli ayrımları ve soruları açar; studies uygulama/karşı örnekler sağlar. Kaynak ismi veya yönerge varlığı davranış kanıtı değildir.

Kullanıcı kararları [DECISIONS](DECISIONS.md), kapsam kaynakları [U002](sources/U002-cloud-plan-and-autonomy.md)'dedir. Varsayılan kullanıcı cevabı kısa sonuç ve plan içindeki tek devam noktasıdır.

## Önceki birikim

SOUL hedefi → B1–B9 kapsamı → R1–R25/M1–M9 ilk türetim → S1-01–S1-17 → F1–F8 aday aileleri → P1–P6 planı.

S1-17 CLOSURE-READY / CANDIDATE korunur; kullanıcı kapanışı, nihai kadro veya sekiz ajan sonucu çıkarılmaz. B1–B9 referans kapsamdır, gerçek SOUL sırası değil. S1-16 tam-okuma iddialarının qualification'ı S1-17 §7'dedir. Somut yeni çelişki yoksa S1 taxonomy'si baştan çalışılmaz.

[P1-01](work/P1-01-claude-cloud-environment-map.md) kaynaklı Environment haritasıdır; canlı test değildir. Mesaj/çağırma, context, yetki, plugin çelişkisi ve cross-session kalıcılık için Q01–Q06 korunur. P2 yeni runtime iddiası üretmedi; yük taşıyan teknik tercihten önce ilgili açık P1'e hedefli dönüşle çözülür.

## P2 ilk taslak sonucu

Current isim/lineage registry'si [ACTORS](ACTORS.md), gerekçe ve sözleşmeler [P2-01](work/P2-01-named-role-contracts.md)'dedir.

- DR01–DR16 adlandırılmış rol sözleşmeleri üretildi: amaç/motivasyon, bilgi/yeterlik, tetik, teslimat/tüketici ve yetki sınırı. Bunlar **16 agent veya daima açık süreç kararı değildir**.
- Aile sınıflandırmadır; rol katkı sözleşmesidir. Motivasyon bu taslakta rolün başarı yönü olarak içeride yazılır; motivasyon başına agent otomatik çıkarılmaz. Bu aday yorumdur, deneysel model yasası veya kullanıcı kabulü değildir.
- İş keşfi/planlama ile koordinasyon; bilgi bakımı ile bağlam; sınama tasarımı, yürütmesi ve kanıt hükmü ayrı sorumluluklardır.
- Kapasite Tasarımcısı ve Güvence İnceleyicisi alan profili gerektirir; genel bir actor'un bütün uzmanlıkları taşıdığı varsayılmaz. Gerekirse P3 bulgusuyla ayrı rol sözleşmelerine ayrılır.
- R1–R25 primary lineage kaybı/tekrarı mekanik olarak kontrol edildi; iki F3 lifecycle uzmanlığı, F2 ve F8 görünür. Yeni canlı deney veya 100 C için bağımsız coverage testi yapılmadı.

**Kanıt sınırı:** Foundation/çalışma kayıtları ve seçilmiş source karşılaştırması; aynı assistant'ın aday tasarımı ve kayıt kontrolü. Gerçek yeterlik, doğru iş keşfi, iletişim veya independence kanıtı değil.

## Current next responsibility ve durma noktası

**Bu tur tamamlanan:** P2'nin ilk rol/sözleşme taslağı ve mevcut registry/plan/devir bağlantısı. **Şimdi kullanıcıya dön; P3 aynı turda otomatik başlamaz.**

**Sonraki kullanıcı devamında:** WORK/P3 kapsamında bu rollerin WORK–INFORMATION döngüsünü tasarla. İlk bounded kapsam hedef/birikimin devri → iş/bilgi ihtiyacının keşfi ve sorgulanması → rol talebi/yanıtı → gerekçeli plan/admission ilişkisidir. İlk SOUL teknik görevini veya hazır backlog'u seçme.

P3'te konuya göre karar sahibi, talep sahibi, anlaşmazlık yolu, bilgi/sürüm/yazıcı, tüketici ve rutin tetik açıklıklarını birlikte ele al; bu döngüde ortaya çıkan rol uyumsuzluğunu P2'ye geri bağla. Rol isimlerini yeniden teorik bir taxonomy araştırmasına çevirme.

**Sonraki harita:** P2 roller ↔ P3 iş/bilgi döngüsü → P4 bütünleşik alt ajan/takım ve allocation seçimi → P5 dosya/mekanizma → P6 sınama/devir. Teknik kurulum veya yetkisiz erişim için peşin sınırsız yetki yoktur.

## Fresh-session yolu

AGENT ve gereken kontroller → [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) → [P1-01](work/P1-01-claude-cloud-environment-map.md) → [P2-01](work/P2-01-named-role-contracts.md) tam okunur. Aynı konuşmada tam unchanged içerik korunabilir. Ardından current aşamanın Foundation/studies kaynaklarına inilir.

S1/B/history/Context'in tarihsel next ifadeleri current planı yönetmez. Current rol adları ACTORS'ta, ayrıntılı sözleşmeler P2-01'de, bütün plan yalnız WORK'tedir.
