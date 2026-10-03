# Taslak 01 — Roman analojisi / ikinci yazım

- Durum: Üslup ve anlatım için olumlu kullanıcı geri bildirimi alındı; istenen çözüm adları kapanışa eklendi. Bu revizyonun değerlendirmesi bekleniyor; yayımlanmış veya nihai onaylanmış içerik değildir.
- Kaynak analoji: [Roman analojisi](../01-roman-analojisi-kullanici-talebinden-yasayan-is-tanimina.md)
- Kaynak konuşma: [EXP-001 U005](../../../../explorations/EXP-001-soul-calisma-modeli/sources/conversation/USER-MESSAGES.md#u005) ve [U006](../../../../explorations/EXP-001-soul-calisma-modeli/sources/conversation/USER-MESSAGES.md#u006).
- Önceki taslak: [01-roman-analojisi.md](01-roman-analojisi.md) — karşılaştırma için korunmuştur.
- Genel üslup rehberi: [BATU-YAZIM-REHBERI.md](../../../BATU-YAZIM-REHBERI.md)
- LinkedIn yayın rehberi: [LINKEDIN-YAYIN-REHBERI.md](../../LINKEDIN-YAYIN-REHBERI.md)
- Post gövdesi karakter sayısı: 2644 — boşluklar ve satır sonları dahil; dosyanın son satır sonu hariç.
- Üst sınır: 2800

## Kapanışın araştırma dayanağı — post gövdesine dahil değil

[Work-management çapraz sentezi](../../../../research/studies/work-management-project-control/08-CROSS-UNIT-SYNTHESIS.md), Beads'ın dependency/ready-frontier, OpenSpec'in living-plan ve Flowable'ın olay/koşul temelli yürütme mekanizmalarını birbirinden ayırır. [Flowable bulguları §5, §10–11](../../../../research/studies/flowable/FINDINGS.md), olayla etkinleşme/sonlandırma ile çalışan işin yeniden planlanmasının yalnız plan belgesini değiştirmek olmadığını gösteren kaynak-bazlı karşılaştırmadır. Bu ürünlerin birlikte seçildiği veya görev gerekçesindeki anlamsal değişimi kendiliğinden keşfettikleri ileri sürülmez.

DevOS'a hazırlanan tarihsel [P2-01 rol sözleşmelerinde](../../../../explorations/EXP-006-development-os-calisma-duzeni/work/P2-01-named-role-contracts.md) DR07 bilgi değişimi ve etkilenen tüketicileri, DR14 etki/invalidation kapsamını, DR01 plan revizyonunu, DR06 yürütme durumunun uzlaştırılmasını, DR08 yeni bağlamı taşır. Bunlar aday tasarım kayıtlarıdır; güncel kurulum kadrosu veya çalışan sistem kanıtı değildir. [SOUL ve DevOS raporu §22.4, §22.6, §22.8, §22.10](../../../../archives/devos-pre-claude-2026-09-29/soul-and-devos/SOUL_ve_DevOS.md), Loop/Context/Graph/Workflow Engineering ve Orchestration ilişkisini ayrıca açıklar.

Dış kavram kontrolü: [Lewis ve diğerleri — Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401), retrieval ile üretim ilişkisini; [NASA — Requirements Management §6.2](https://www.nasa.gov/reference/6-2-requirements-management/), izlenebilirlik, değişiklik etkisinin değerlendirilmesi ve onaylanmış değişikliğin ilgili taraflara iletilmesini açıklar. Post, RAG'nin bu bütünün bir parçası olamayacağını değil, tek başına görev yaşam döngüsünün yerine geçmediğini söyler.

Buradaki dependency tracking, yalnız görev sırası değil, görevin dayandığı koşul ve gerekçe ilişkisini izleme ihtiyacını ifade eder. Bu ilişkilerin keşfi ve doğruluğu ayrıca değerlendirilir. Olayın taşınması, etki hükmü, yetkili plan değişikliği ve çalışan göreve uygulanması aynı işlem değildir. Tek bir hazır ürün, SOUL'a özgü kanıtlanmış buluş veya tamamlanmış entegrasyon iddiası yoktur.

---

Bir AI'a “roman yazmak istiyorum” desem, konu sorup karakterleri oluşturmaya başlaması gayet makul. Sonunda elimde iyi yazılmış bir metin olabilir. Ama ben gerçekten ne elde etmek istiyordum? Bir Word dosyası mı, insanların okuyacağı bir kitap mı?

Bunu kendim de baştan bütün ayrıntılarıyla düşünmemiş olabilirim. Ben romanın derdindeyim; yayıncı, baskı, dağıtım, rafta yer bulma başka bir dünya. Bir yandan da belki yayımlamak istemiyorum, kendim için yazıyorum. Dolayısıyla sistemin benim yerime yayıncılık işine girişmesi de çözüm değil. Önce bu romanı niye yazmak istediğimi birlikte anlamamız gerekiyor.

Buraya kadar “işe başlamadan önce amacı netleştir” denebilir. Ama roman örneği bende orada bitmedi.

Diyelim yayımlanacak bir kitap istediğim netleşti. Artık ilk bölümü yazabiliriz. Bunun için hangi dağıtım şirketiyle çalışacağımızı da çözmüş olmamız gerekmiyor. Ben romanı yazarken dağıtım konusu aklımın bir kenarında durabilir; AI'la çalışan ekipte bunun karşılığı ne olacak?

Bir agent metni yazıyor, başka biri yayıncıları inceliyor, bir diğeri dağıtım seçeneklerini araştırıyor olsun. Yayıncıları inceleyen agent, seçtiğimiz yayıncının dağıtımı da üstlendiğini öğrensin.

Şimdi dağıtımcı arama işi ne olacak?

Bulguyu bir dosyaya yazmak yetmiyor. Diğer agent hâlâ şirketleri karşılaştırıyor olabilir. Hatta sonunda çok iyi bir rapor getirebilir. Ücretler, bölgeler, avantajlar... Yanlış bilgi de yoktur belki.

Ama artık o rapora ihtiyacımız yok.

İlginç olan şu: O görevi başta vermek hata değildi. Araştırmayı yapan agent da görevini yanlış yapmadı. İş yapılırken öğrendiğimiz bir şey, başka bir işin yapılma nedenini ortadan kaldırdı.

Bunun çözümü yalnız RAG değil. RAG ilgili bilgiyi bulup cevaba katabilir; hangi görevin artık gereksiz olduğunu değerlendirip çalışan agent'ı durdurmak başka bir sorumluluk.

Araştırırken karşıma çıkan yöntemler burada anlam kazanıyor: dependency tracking, yani görevin hangi koşullara dayandığını izlemek; change impact analysis, yani yeni bilginin hangi işleri etkilediğine bakmak; replanning, yani planı buna göre yeniden kurmak. Olay güdümlü orkestrasyon da bu değişikliği çalışan ekibe uygulatmanın tarafı. Listedeki kutuyu silmekle agent'ın çalışmasını durdurmak aynı işlem değil.

Bunlar tek bir ürünün adı değil, birlikte kurulması gereken mekanizmalar. Öğrenilen bilgi yalnız saklanmıyor; etkisi değerlendiriliyor, gerekiyorsa görev değişiyor ve ilgili agent'a uygulanıyor.

Ben bunun takibini sürekli kendim yapacaksam, kurduğum ekibin arasında haber taşıyan kişiye dönüşürüm. O ekibi biraz da öğrendiği şey yüzünden artık neyi yapmaması gerektiğini anlayabilsin diye istiyorum.
