# EXP-006 — STATE

**Durum:** AÇIK / yeni oturum için duraklatıldı. **Güncelleme:** 28 Eylül 2026.
**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini, SOUL'un gerektirdiği gerçek kabiliyetlere göre ortaya koymak.
**Current:** **P4 / SAYFA SINIRSIZ STRES TESTİ VE RAPOR v3 / YARIM KALDI / TESLİM DOĞRULANMADI.** Yeni oturumda aynı iş devralınacak. V2 son dosya kimliği doğrulanmış rapor tabanıdır; mimari kabulü değildir. P5 kurulumu ve P6 hedef kabulü yapılmadı.
**Üst plan:** [WORK](WORK.md) v1.6. **Aktif devir kaydı:** [P4-03](work/P4-03-unbounded-stress-test-handoff.md). **V2 provenance:** [P4-02](work/P4-02-soul-derived-report-v2.md).

## Son kullanıcı yönü

V2 yapısını stres testine sokmak ve raporu **sayfa sınırı olmadan** yeniden hazırlamak istendi. Önceki 200 sayfa koşulu artık geçerli değildir. İstenen iş yüzeysel metin taraması, yalnız graph eki veya sayfa sayısını artırmak değildir; SOUL hedefi karşısında bütün tasarımın yeterliğini sınamak ve gerekçeli biçimde yeniden yazmaktır.

Bu çalışma yeni rapor olarak teslim edilemedi. Kullanıcı ardından repository'nin yeni oturumda devam etmeye uygun olmasını istedi. **Bu tur yalnız devir ve kaynak koruması yapıldı; stres testi/yeniden yazım ilerletilmedi.**

## Doğrulanabilen ve doğrulanamayan

- V2 PDF ve kaynak ZIP'si mevcut; byte/SHA-256 kimlikleri P4-02 ile eşleşiyor. ZIP bütünlüğü ve manifest'teki 22 üyenin hash/boyutları kontrol edildi. Kaynak gövde, sözleşmeler, referans model ve tarihsel QA kayıtları korunuyor.
- V3 raporu, kodu veya ham test sonuçları bu tur erişilen mounted dosyalarda bulunamadı. Files aramasında sonuç alınmadı; bütün olası saklama yerlerinde yokluk iddia edilmez.
- Önceki assistant'ın dört kusur iddiası P4-03'te **yeniden doğrulanacak ipuçları** olarak tutulur. Yeniden üretilmiş bulgu, düzeltilmiş hata veya hedef Claude arızası sayılmaz.
- “88 test geçti / v3 hazır” teyit edilmedi. V2'nin 40 test/dört guard-kaldırma kaydı yalnız v2'nin tarihsel sınırlı kanıtıdır; bu tur yeniden koşturulmadı.
- Eksiklerin 200 sayfa sınırından kaynaklandığı kanıtlanmış değildir. Sayfa sınırını kaldırmak daha uzun metni otomatik daha sağlam mimari yapmaz.

## Kaynak erişimi

**Repository tek başına tam rapor gövdesini içermiyor.** Yeni oturum için konuşmada `EXP-006_Yeni_Oturum_Devir_Paketi.zip` oluşturuldu: doğrulanmış v2 PDF + orijinal kaynak ZIP + erişim/kanıt sınırları. Ad/hash ve içerik P4-03 §3'te.

Devir kayıtları repository'dedir; gerçek rapor/sözleşme/kod çalışması için bu ek veya aynı hash'li v2 kaynakları da gerekir. Mevcut değilse özetten devam edilmez. Yeni oturumun bu container'ı ya da eski ekleri kendiliğinden görebileceği varsayılmaz.

## Korunan sınırlar ve mimari taban

Claude Code cloud hedefi; SOUL'un ilk/sonraki gerçek işlerini ekibin keşfetmesi; K1 talep→çalışma→yanıt→kullanım; K2 rutin rol geçişlerinde Batu'nun tetikleyici olmaması; gerçek müdahale/yetki/kabul korunur. D021 içerik–çalışma alanı sahipliği ve G/Y hedef ayrımı sürer. Rol sayısı agent sayısı değildir.

V2'nin takım ağırlıklı bilişsel ekip, korunan kontrol hizmetleri, PostgreSQL canlı durum/typed relations, Git ürün sürümü, kaynak/kanıt gövdeleri, memory/context compiler ve kontrollü yayın/recovery önerileri **stres testinin nesnesidir**. Kolay olduğu için korunmaz, karmaşık olduğu için üstün sayılmaz. P4-01 eski baseline'dır; current mimari veya next-work değildir.

## Yeni oturumda devam

AGENT ve gereken kontroller → [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → [WORK](WORK.md) → [DECISIONS](DECISIONS.md) → [P4-03](work/P4-03-unbounded-stress-test-handoff.md) → [P4-02](work/P4-02-soul-derived-report-v2.md) → gerçek v2 kaynak paketi.

Kullanıcının yeni oturumdaki devamıyla: kaynakları doğrula; tam rapor ve sözleşme bağlamını oku; varsa gerçek v3 dosyalarını kurtar, yoksa v2'den izlenebilir biçimde stres testini yeniden kur. Bulguları yeniden üret/çürüt; bütün mimariyi SOUL gerekliliklerine karşı değerlendir; kanıt ve düzeltmelerle sayfa sınırsız raporu tamamla. Ayrıntılı iş haritası P4-03 §5'tedir.

P5'e, hedef cloud kurulumuna veya eski P4-01 izin-matrisi next'ine geçilmez. Yeni genel rol taxonomy'si açılmaz. Yeni rapor ve test sayıları gerçek dosya/koşu/geri okuma ile doğrulanmadan tamamlandı denmez. Bu tur burada durur.
