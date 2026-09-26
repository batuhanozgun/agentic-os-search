# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu DevOS tasarım çalışması.  
**Güncelleme:** 27 Eylül 2026, P1 kaynak incelemesi sonrası.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak.  
**Current:** **P1 BOUNDED SOURCE REVIEW COMPLETE / RUNTIME NOT TESTED / USER RETURN.** **P2 NEXT / NOT STARTED**; P3–P6 başlamadı.  
**Planın tek ana yüzeyi:** [WORK — master plan v1.1](WORK.md).  
**Son kullanıcı yönü:** Kalıcı planın hazırlanmasından sonra “tamam şimdi devam edebilirsin” — P1'i yürüt. P2 veya kurulum bu tur başlatılmadı.

## Sabit kapsam ve sınırlar

- **Environment:** Kullanıcının seçimi Claude Code cloud. P1 belge resmi var; hedef hesap/oturumun gerçek sürüm, araç ve izin yeterliği henüz gösterilmedi.
- **SOUL'u geliştiren:** Kurulacak DevOS ekibi. İlk ve sonraki SOUL işlerini ekip keşfeder, değerlendirir, planlar ve yürütür. Assistant burada ekibin çalışma düzenini tasarlar; onun yerine gerçek SOUL backlog'u seçmez.
- **K1 iletişim:** Talep → ilgili rolün çalışması → yanıt → gerçek kullanım. Yöntem açık; yalnız mesaj yazılması yeterli değil.
- **K2 normal ilerleme:** Her adımda Batu'nun “şimdi sıra sende” demesi gerekmez. Başlatma/yeniden başlatma, gerekli müdahale, meşru yetki ve kabul mümkündür. Sınırsız kesintisiz özerklik şartı yok.
- **Loopinance:** Kanon manuel tetikleme karşı örneği; v2 yalnız rutin kullanıcı tetiklemesi gerekmemesinin örneği. V2/ECC bütün olarak benimsenmedi.
- **Bilgi:** SOUL ürün çıktıları ile DevOS'un kendi plan/bilgi/karar/kanıt/devam kayıtları ayrı amaçlarla, ilişkileri korunarak yönetilir. Fiziksel depolama şeması seçilmedi.
- **Çalışma standardı:** Foundation düşünme kapsamını genişletir; studies uygulama ve karşı örnekleri sağlar. Kaynak isimleri yeterli kullanım değildir.

Kullanıcı kısıtları [DECISIONS](DECISIONS.md), kaynakları [U002](sources/U002-cloud-plan-and-autonomy.md)'dedir. Gereksinim, belge beyanı ve davranış kanıtı farklıdır.

## S1'den devralınan

SOUL hedefi → B1–B9 kapsamı → R1–R25/M1–M9 ilk türetim → S1-01–S1-17 → F1–F8 aday aile/specialization modeli → P1–P6 planı.

S1-17 **CLOSURE-READY / CANDIDATE** sonucu korunur; nihai rol kadrosu, sekiz ajan veya çalışan sistem kabulü değildir. Kullanıcı S1 kapanışı kaydedilmedi; sonraki tasarımın planı ve P1 ilerlemesi yetkilendirildi. Yeni somut çelişki yoksa S1 sınıflamasını tekrarlama.

[ACTORS](ACTORS.md) current aile/lineage kaynağıdır. F2 gerçek uygulama yükünü korur; her dosya yazımı F2 değildir. F3 Information/Participation yaşam döngüsü kaydı doğruluk, yetki veya gerçek etkiyi ikame etmez. S1-16'nın kesilmiş kaynaklara ilişkin tam-okuma etiketleri [S1-17 §7](work/S1-17-consolidation-closure-audit.md#7-okuma-izi-kaynak-katkısı-ve-önceki-kayıt-düzeltmesi) ile nitelendirilmiştir. B1–B9 referans kapsamdır; SOUL öncelik sırası değildir.

## P1 sonucu ve kanıt sınırı

Ayrıntı ve birincil kaynaklar: [P1-01 Environment haritası](work/P1-01-claude-cloud-environment-map.md).

- Cloud belgesi hem repository alt ajanlarını hem etkinleştirilebilir takımları anlatır. İletişim için takım zorunlu değildir; güncel alt ajan belgesi de ad/kimlik ve uygun araçlarla mesajlaşmayı tanımlar.
- Talep/bağlam/yanıt sahibinin kim olduğu, hangi talimatların gerçekten yüklendiği ve çalışma kipindeki araçlar ayrıca tasarlanmalıdır.
- Takım görev devri ve Claude'un çalışma döngüsü rutin ilerlemeyi destekleyen imkânlardır; doğru iş keşfi veya bütün SOUL'un tamamlanması garantisi değildir.
- Takım plan-onay olayı otomatik gerçekleşebilir; gerçek inceleme/güvence sayılmaz.
- Yerel hafıza ve runtime görev kayıtları kalıcı cross-cloud DevOS state'i sayılmaz. Erişim, kayıt/sürüm ve yeniden giriş yolu açık yüklerdir.
- Repo plugin'lerinin cloud'a yüklenmesinde iki alınmış resmî belge çelişir. ECC/plugin aktarımı doğrulanmış kabul edilmedi.
- Kanon ve v2'nin ilgili tanım/tetik dosyaları sabit commit'lerden incelendi; kullanıcı deneyimi, kaynak sözleşmesi ve gerçek çağrı izi ayrıldı. Canlı cloud/Loopinance testi yapılmadı.

**P1 kapanış kapsamı:** Kaynaklı Environment resmi P2 rol sözleşmelerini besleyecek düzeyde hazırdır. Q01–Q06 runtime/erişim/kalıcılık/güvence açıkları P1-01 §5'te görünürdür; teknik seçim bunlara dayanacaksa hedefli P1 doğrulaması gerekir. Belge resmi platform yeterlik kabulü değildir.

## Current next responsibility ve durma noktası

**Bu tur tamamlanan:** P1 kaynak incelemesi ve mevcut plan/devir yüzeylerine kayıt. Ajan dosyası, kurulum veya SOUL geliştirme görevi üretilmedi.

**Şimdi:** Kısa P1 sonucunu kullanıcıya döndür. **P2 otomatik başlamaz.**

**Sonraki kullanıcı devamında:** WORK/P2'de ACTORS aile ve sorumluluklarından anlaşılır rol isimleri/sözleşme adayları çıkar. P1'in iletişim, araç, bağlam ve güvence sınırlarını kullan; ilgili Actors/Work Foundation'ını ve ardından uygun studies'i oku. Aktör–aile–rol–motivasyon ve motivasyon başına ajan sorusu açık kalır; sekiz aileyi sekiz ajana çevirme.

**Daha sonraki harita:** P2 roller ↔ P3 WORK–INFORMATION → P4 bütünleşik seçim → P5 gerçekleştirme → P6 sınama/devir. P1'e yeni yük taşıyan Environment sorusunda hedefli dönülür. Plan kurulum/erişim/üretim için sınırsız yetki değildir.

## Fresh-session yolu

AGENT ve gereken kontrollerden sonra [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [ACTORS](ACTORS.md) → [U002](sources/U002-cloud-plan-and-autonomy.md) → [P1-01](work/P1-01-claude-cloud-environment-map.md) tam okunur. Aynı konuşmada unchanged tam içerik korunabilir. Sonra aktif aşamanın gerekli kaynaklarına inilir. S1/B/history/Context içindeki eski next ifadeleri current planı yönetmez.
