# Taslak 01 — Roman analojisi / ikinci yazım

- Durum: Önceki sürümün üslubu Batu tarafından kendisine benzemediği gerekçesiyle reddedildi. Bu sürüm, doğrudan yazar metnine dönülerek hazırlanmış yeni denemedir; üslup eşleşmesi ve yayın onayı henüz yoktur.
- Kaynak analoji: [Roman analojisi](../01-roman-analojisi-kullanici-talebinden-yasayan-is-tanimina.md)
- Kaynak konuşma: [EXP-001 U004–U006](../../../../explorations/EXP-001-soul-calisma-modeli/sources/conversation/USER-MESSAGES.md#u004).
- Doğrudan yazar referansı: [LLM Düşünmez — Batu'nun yazdığı makale](../../articles/2026-09-11-llm-dusunmez-zaxzf.md). Özellikle bilmediği alanda AI kullanma beklentisi, örneği açma biçimi ve cümle/paragraf akışı. Makaledeki teknik iddialar bu üslup çalışmasıyla doğrulanmış sayılmaz.
- Önceki taslak: [01-roman-analojisi.md](01-roman-analojisi.md). Bu dosyanın önceki gövdesi de Git geçmişinde korunur; yeni sürüm için farklı dosya açılmadı.
- Genel üslup rehberi: [BATU-YAZIM-REHBERI.md](../../../BATU-YAZIM-REHBERI.md). Assistant'ın rehber için ürettiği örnekler, Batu'nun özgün yazıları yerine üslup kanıtı sayılmadı.
- LinkedIn yayın rehberi: [LINKEDIN-YAYIN-REHBERI.md](../../LINKEDIN-YAYIN-REHBERI.md)
- Post gövdesi karakter sayısı: 2656 — boşluklar ve satır sonları dahil; dosyanın son satır sonu hariç.
- Üst sınır: 2800

## Araştırma dayanağı — post gövdesine dahil değil

[Work-management çapraz sentezi](../../../../research/studies/work-management-project-control/08-CROSS-UNIT-SYNTHESIS.md), Beads'ın dependency/ready-frontier, OpenSpec'in living-plan ve Flowable'ın olay/koşul temelli yürütme mekanizmalarını birbirinden ayırır. [Flowable bulguları §5, §10–11](../../../../research/studies/flowable/FINDINGS.md), olayla etkinleşme/sonlandırma ile çalışan işin yeniden planlanmasının yalnız plan belgesini değiştirmek olmadığını gösteren kaynak-bazlı karşılaştırmadır. Bu ürünlerin birlikte seçildiği veya görev gerekçesindeki anlamsal değişimi kendiliğinden keşfettikleri ileri sürülmez.

DevOS'a hazırlanan tarihsel [P2-01 rol sözleşmelerinde](../../../../explorations/EXP-006-development-os-calisma-duzeni/work/P2-01-named-role-contracts.md) DR07 bilgi değişimi ve etkilenen tüketicileri, DR14 etki/invalidation kapsamını, DR01 plan revizyonunu, DR06 yürütme durumunun uzlaştırılmasını, DR08 yeni bağlamı taşır. Bunlar aday tasarım kayıtlarıdır; güncel kurulum kadrosu veya çalışan sistem kanıtı değildir. [SOUL ve DevOS raporu §22.4, §22.6, §22.8, §22.10](../../../../archives/devos-pre-claude-2026-09-29/soul-and-devos/SOUL_ve_DevOS.md), Loop/Context/Graph/Workflow Engineering ve Orchestration ilişkisini ayrıca açıklar.

Önceki revizyondan korunan dış dayanaklar: [Lewis ve diğerleri — Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401), retrieval ile üretim ilişkisini; [NASA — Requirements Management §6.2](https://www.nasa.gov/reference/6-2-requirements-management/), izlenebilirlik, değişiklik etkisinin değerlendirilmesi ve onaylanmış değişikliğin ilgili taraflara iletilmesini açıklar. Bu tur dış kaynaklar yeniden doğrulanmadı. Güncel post gövdesi ayrı bir RAG tartışması açmaz; çözümün iş/plan/orkestrasyon tarafını adlandırır.

Buradaki dependency tracking, yalnız görev sırası değil, görevin dayandığı koşul ve gerekçe ilişkisini izleme ihtiyacını ifade eder. Bu ilişkilerin keşfi ve doğruluğu ayrıca değerlendirilir. Olayın taşınması, etki hükmü, yetkili plan değişikliği ve çalışan göreve uygulanması aynı işlem değildir. Tek bir hazır ürün, SOUL'a özgü kanıtlanmış buluş veya tamamlanmış entegrasyon iddiası yoktur. Roman/yayıncı durumu açıklayıcı varsayımsal örnektir; Batu'nun yaşanmış bir yayıncılık deneyimi olarak sunulmaz.

---

Ben yapay zekâya sadece nasıl yapılacağını bildiğim işleri daha hızlı yaptırmak istemiyorum. Bilmediğim bir işi de ele alabilsin istiyorum ama o zaman karşısına koyacağım talebin eksik olacağını da kabul etmem lazım. Bilmediğim şeyi eksiksiz tarif etmem zaten nasıl mümkün olacak?

Mesela roman yazmak istiyorum desem, aklımda konu var, karakterler var, hikâyenin nerede başlayıp nerede biteceği var ama kitabın bir dükkânda rafa nasıl girdiğini bilmiyorum. Ben hâlâ romanı yazma derdindeyim, sistem de sadece yazmaya odaklanırsa sonunda elimde güzel bir Word dosyası olur. Sonra? Kitabı kim basacak, kim dağıtacak, kim okuyacak? Bunları baştan söylemedim diye ihtiyacım ortadan kalkmadı. Tabii kendim için yazıyorsam da durup dururken yayıncı aramasın; neyi istediğimizi birlikte ortaya çıkarmamız gerekiyor.

Burada “tamam, önce bütün işi tanımlayalım sonra başlayalım” demek kolay ama o da başka bir yere takılıyor. Dağıtımcıyı bulmadan ilk bölümü yazamayacak mıyız? Romanın konusu netse yazabiliriz, dağıtım konusu da bir kenarda durur. İnsan olarak bunu yapabiliyorum; bir yandan yazarken bir yandan da “bunu nasıl yayımlatacağım acaba?” diye düşünüyorum. Agent'lardan oluşan bir ekipte bu bağlantıyı nasıl kuracağız?

Bir agent romanı yazsın, biri yayıncıları incelesin, başka biri de dağıtımcıları araştırsın. Sonra yayıncıları inceleyen, seçtiğimiz yayıncının dağıtımı da yaptığını öğrensin. (Her yayıncı böyle çalışıyor demiyorum, örneğimizde öyle olsun.) O zaman dağıtımcı arayanın işi kalmadı. Ama ona kim söyleyecek? Bulgu dosyaya yazıldı diye diğer agent'ın işi bırakmasını sağlayan bir şey yoksa araştırmaya devam eder, belki de çok güzel bir rapor getirir. Ben de okuyup “eline sağlık ama buna artık gerek kalmadı” derim.

Oysa başta o işi vermek yanlış değildi. Çalışırken bir şey öğrendik, öğrendiğimiz şey başka bir işi gereksiz hale getirdi. Demek ki yalnız iş listesi yetmiyor; işin hangi ihtiyaca, hangi koşula bağlı olduğunu da tutmak gerekiyor. Dependency tracking dediğimiz bağımlılık takibi burada işe yarıyor. Yeni bilgi geldiğinde bu bağlardan hangi işlerin etkilendiğine bakmak change impact analysis, planı buna göre değiştirmek de replanning.

Planı değiştirdik diye çalışan agent da durmuyor tabii. Değişikliği ona ulaştırıp görevin gerçekten durmasını sağlayacak olay güdümlü orkestrasyon tarafı da var. Yani bilgi bulmak, o bilginin işi değiştirdiğini anlamak ve değişikliği uygulatmak birbirinin yerine geçmiyor.

Bunları her seferinde ben ilişkilendirip aralarında haber taşıyacaksam roman yazmaya yardım eden bir ekip kurmuşum ama kendime de o ekibi idare etme işi çıkarmışım. Benim beklediğim biraz da o işi üstlenmesi.
