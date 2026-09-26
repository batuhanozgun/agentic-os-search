# EXP-006 — HANDOFF

**Amaç:** Yeni oturumun son alt konu kadar onun üst işteki nedenini ve dönüş noktasını devralması.  
**Güncelleme:** 26 Eylül 2026.  
**Güncel iş:** S1 — araştırmaya dayalı Development OS rol/sorumluluk konsolidasyonu.  
**Son teslimat:** [S1-06](work/S1-06-full-role-family-mapping.md), R1–R25 tam aile eşlemesi; aday sonuç.

## 1. Yeni oturumda okuma

STATE → bu dosya → WORK → ACTORS → S1 yöntem/dilim dizini. Aynı G1 örneğine devam edilecekse S1-04 tam okunur. Başlangıç gerekçesi veya altı kök iş için EXP-006_Context; kabul edilmiş çalışma anlaşmaları için DECISIONS. Önceki ayrım gerekiyorsa S1-01/02/03; sonra yalnız ilgili B ve asıl araştırma kaynakları.

ACTORS ilk R1–R25/M1–M9 türetim kaydıdır; S1 sonuçları oraya nihai birleşme olarak geçirilmiş değildir. Eski B/S1 dosyalarındaki dönüş cümleleri üretim anlarına aittir; güncel sıra STATE/HANDOFF'tan alınır.

## 2. Başlangıçtan bugüne neden zinciri

SOUL'u yaratmak istiyoruz. Tek insanın üretim/uzmanlık kapasitesi ve tek konuşmanın bağlamı bu işin bütünü için yeterli kabul edilmediği için DevOS çalışma düzenini konuştuk. İlk soru aktörlerdi: insan + yapay zekâ. İnsanın müşteri rolünde yetki ve kabul çekirdeği kaldı; teknik uzmanlık ve iş yönetimi ona geri bırakılmıyor.

Yapay zekânın rollerini jenerik unvanlardan çıkarmamak için önce DevOS işini; işi anlayabilmek için SOUL hedefini somutlaştırdık. EXP-001/002/004 okumalarından çıkan hedef bu aşama için yeterli kabul edildi. Ardından B1–B9 geliştirme işleri, onların kabiliyet/sorumlulukları ve R/M adayları türetildi. Şimdi S1 bu adayları birlikte değerlendiriyor; henüz DevOS mimarisi veya kurulumu değil.

İlk altı kök iş: hedefi belirleme; gereken işi keşfetme; yapılabilir kılma; gerçekleştirme; sınama/yeniden çalışma; zaman içinde sürdürme. B1–B9 bunların yerine geçmez; keşfedilmiş SOUL geliştirme alanlarıdır. Gereksinim yazmak gerçekleştirme değildir. EXP-006 dosya düzeni de SOUL veya DevOS'un kurulmuş hâli değildir.

## 3. Son kullanıcı yönü ve S1 birikimi

Kullanıcı önce araştırmaları S1'e kattı; sonra aktör türü, dil modelinin bağlamı ve birbiriyle çatışmayan rol motivasyonu üzerinde durdu. Keel ve OS Architect kaynakları bu sorular için incelendi, onların geliştirme programı devralınmadı. Ardından zinciri toparlamamızı istedi; son mesajı yönün net olduğunu, somut sonuçları doğru kabul etmeden değerlendirebileceğimizi söyleyerek devam yetkisi verdi.

- **S1-01:** İnceleme ailesi; üretim/düzeltme; teşhis/karar; sürüme bağlı yeniden sınama. G1: kod/prosedür/bağlantıyı geliştiren tarafın açık eşlemesi eksik.
- **S1-02/03:** Ortak aile aynı etkin çağrı değildir. Çoklu ölçüt otomatik çatışan motivasyon değildir. Dar sorumluluk, dar düşünsel taban demek değildir. Rolün gerekli bilgiyle tetiklenmesi, katkısının tüketilmesi ve birikimin geliştiren→SOUL→kurulmuş role aktarımı ayrıca değerlendirilir.
- **S1-04:** Bu koşullar ilk G1 örneğinde somut geliştirme teslimlerine uygulandı. Aşağıdaki sonuçlar adaydır; kullanıcı kabulü veya bağımsız doğrulama değildir.

## 4. S1-04'te tam olarak ne yaptık?

**Örnek:** SOUL, salt-okur inceleme gereken durumda inceleyiciyi belirli ürün sürümüne bağlasın; inceleyici hedefi/ölçütü değiştirmeden okuyup bulgu teslim etsin. Her inceleyici her zaman yazamaz kararı verilmedi. Ayrı rapor alanı veya çalıştırmalı inceleme ihtiyacı ayrıca tanımlanmalı.

**Geliştirme zinciri:**

1. Rol gereği ve yetki sınırı: R7, R1/R9 girdileriyle.
2. Gerçekleştirme yolu ve kontrol kapsamı: R13, R16/R17 katkılarıyla.
3. **Fiilî teknik gerçekleştirme:** açık görev kartı adayı; mevcut R14/R20 tanımlarından yeni kod üretme sorumlusu otomatik çıkarılmadı.
4. Kurulum/bütünleştirme: R14; birden çok parçanın koordinasyonu gerekiyorsa R20.
5. Sınama: R24/R25'in yöntem/yürütüm sorumluluklarının bu kapsama uyarlanması adayı; R15 gerçek etki, R18 birleşik hüküm. Davranış iddiası ayrıca varsa R2.
6. Sorun halinde R3 teşhis; ilgili tasarım/üretim/kurulum/test halkasına açık geri dönüş.

Bunlar atanmış gerçek kişiler değil, mevcut aday kapsamlarıyla eşlemedir. Satırdaki destekleyici roller ortak ve belirsiz sahipliğe dönüştürülmemeli; gerçek görevde teslim sorumlusu belli olmalı.

**Teknik gerçekleştirme kartı:** Amaç, gereği kullanılabilir ve sınanabilir çıktıya çevirmek. Girdi; gerekçe, hedef/sürüm, izinli davranış, çözüm kararı, asıl kaynaklar, mevcut kod/test, gerçek ortam bilgisi ve değişiklik yetkisi. Çıktı; sürümlü kod/ayar/prosedür/bağlantı, yerel test kanıtı, kurulum bilgisi ve açık eksikler. Tasarım yanlışsa gerekçeyle geri açılır, gereksinim sessizce gevşetilmez. Kendi kontrolü bağımsız hüküm değildir.

**Birlikte taşıma adayı:** Yeterli aktörde tasarım, üretim ve düzeltme aynı sonuca hizmet edebilir. R14 küçük kurulum ayarını taşıyabilir; yeni mekanizma geliştirecekse yeterlik/çıktı/yetki açık eklenmeli. R20 üretimi koordine edebilir; bunu yapması kodun üreticisi olduğu anlamına gelmez. Yeni R26 veya kalıcı aile yok.

**Yeni somut ayrım:** Mekanizmayı geliştiren DevOS aktörünün yazması ile üretilmiş SOUL inceleyicisinin ürüne yazamaması çelişmez; farklı iş, hedef ve yetki bağlarıdır. Elle hazırlanmış tek deneme yerine, SOUL'un sonraki inceleyiciyi oluşturup bağlaması da sınanmalıdır.

## 5. Kanıt ve sınama sınırı

Bu tur S1-01 tam; B1/B3/B5/B6/B7/B9'un ilgili rol/sınır bölümleri seçici okundu. Superpowers'ın daha önce incelenmiş sabit sürümünde üretici şablonu tam; Keel'in sabit sürümünde rol-ac.sh tam, file-guard.sh başlangıç sözleşmesi seçici okundu. Ayrıntılı ref/blob ve okuma kapsamı S1-04'tedir.

Keel rol-ac.sh bu sürümde otomatik temizlik yolunun kaldırıldığını belirtiyor; tarihsel OS Architect kaydındaki önceki tasarım current davranış diye kullanılmadı. Koruma betiği bütünü, alt bağımlılıklar, yeni sağlayıcı belgeleri ve güncel kurulu davranış bu tur doğrulanmadı.

S1-04 meşru okuma/raporlama, yasak değişiklik, eksik kontrol, yeni rol oluşumu, düzeltme sonrası yeni sürüm ve kasıtlı bozma senaryolarını **önerdi**; koşmadı. Mekanik engel başarısı iyi muhakeme kanıtı; yazma denemesi olmaması da engelin çalıştığının kanıtı değildir. Canlı DevOS/SOUL/Keel testi ve mekanizma uygulaması yok.

## 6. Kalıcı iletişim kuralı ve sonraki sınırlı iş

EXP-006 cevapları kısa ve doğrudan olmalı: önce ne yaptığımız, sonra bu turda ne çıktığı, sonra sıradaki adım. Örnekler ana sonucu gömmemeli. Bu kural EXP-006_Context ve DECISIONS içinde kalıcılaştırıldı.

S1-06 tam eşlemeyi kullanıcıya sun. Ardından ilk gerçek aile konsolidasyonunu F5 Doğrulama/Güvence üzerinde yap: R2/R6/R8/R12/R15/R18'in ortak başarı yönünü, gereken uzmanlıkları, independence koşullarını ve aynı/different effective role sınırını test et.

Devamda bu görevlendirmenin başka bir geliştirme alanında aynı başarı yönüyle çalışıp çalışamayacağını karşılaştırmak mümkündür. Örneğin bilgiye erişim/bağlam üretimi başka uzmanlık isteyebilir; tek güvenlik örneğinden evrensel geliştirici rolü çıkarılmaz. Böyle bir ikinci örnek bu tur yapılmadı. Genel aile sayısı, fiziksel aktör, araç/ortam, model eğitimi ve mimari kararları açık kalır.

ACTORS, DECISIONS, B dosyaları, Foundation ve kaynak depolar değişmedi. S1-04 ile S1/WORK/STATE/HANDOFF güncellendi. Önceki tam oturum okuma sınırı geçerlidir: görünür geçmişte aktarılmamış bölümler vardır; ayrıca bir tam döküm önceki aramalarda bulunamadı, yokluğu kanıtlanmadı. Bu tur eksiksiz sohbet tam okuması iddiası yok.
