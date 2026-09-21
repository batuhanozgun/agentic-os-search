# EXP-004 — Genişleyen SOUL ve büyük-iş stress testi

**Güncel durum:** Önce [STATE](STATE.md) okunur. T1–T7'den sonra [T08 — Geri bildirim ve kontrollü uyarlama](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) türetilmiş devam notu eklendi; canlı sistem testi veya mimari kabul değildir.

**Kaynak sadakati düzeltmesi — 2026-09-21:** Önceki arşiv, 14 kullanıcı mesajını ve 13 assistant yanıtına adreslenmiş yoğunlaştırılmış görünümleri taşır. Assistant kayıtları eksiksiz özgün cevaplar değildir; yalnız whitespace/UI farkı söz konusu değildir. [FIDELITY-20260921](checks/FIDELITY-20260921.md) eski tam-kaynak/tam-okuma ifadelerini nitelendirir. Tam özgün aktarımın onarımı açıktır. Başarılı main yayını kaynak sadakatini kanıtlamaz.

**Tür:** Kavramsal diyalog + araştırma yeniden-kullanımı + sentetik büyük-iş stress testi.
**İlk kaynak oturum:** 20–21 Eylül 2026; tekil mesaj saatleri üretilmez.
**İlk adreslenen kesim:** U001–U014 ve S001–S013: 27 mesaj referansı. T08 bu eski kesime kaynak mesaj olarak eklenmedi.
**Önceki denemeler:** [EXP-001](../EXP-001-soul-calisma-modeli/INDEX.md) → [EXP-002](../EXP-002-soul-baz-yapi-ve-entelektuel-taban/INDEX.md) → [EXP-003](../EXP-003-ek-hafiza-ve-arastirma-temelli-guvenilirlik/INDEX.md).

## Bu denemenin konusu

Kullanıcı, Foundation ve studies birikimini kullanarak SOUL'un büyük, uzun soluklu ve baştan tamamen bilinmeyen bir işi yapmak için nasıl bir çalışma yapısına ihtiyaç duyacağını düşünmek istedi. Başlangıçta agent'lar, roller, ortadaki iş, iş akışı/plan ve memory adayları vardı. Bu beşli doğrudan mimariye çevrilmedi; Work / Actors / Information / Environment ile Composition ayrımları ve candidate studies'teki mekanizma/karşıörnekler kullanıldı.

Sentetik vaka bir eğitim yılı boyunca kullanılacak kapsamlı bir 4. sınıf matematik soru bankasını üretme, yayımlama ve sürdürme programıdır. Amaç eğitim ürünü tasarlamak değil, çalışma sisteminin ihtiyaçlarını zorlamaktır. Ülke, gerçek müfredat, mevzuat veya gerçek kullanıcı grubu seçilmedi.

## Modelin evrimi

İlk arşiv kesiminde, SOUL ile oluşturduğu çalışma sistemi arasında zorunlu sert ayrım kurmak yerine baz SOUL'un işe göre genişlemesi hipotezi ortaya çıktı. T08 bunu yalnız boyut artışı olarak değil; göreve uygun yeniden yapılandırma, sadeleştirme ve gerektiğinde geri alma olarak inceltir.

Work / Actors / Information / Environment ile Binding / Standing / Control / Transition, düşünme ve ilişki kurma zemini olarak kullanılır. Her birinin ayrı yazılım modülü olması gerektiği sonucuna varılmadı. Bir vakayı bu başlıklarla tarif etmek, Foundation'ın veya oluşacak sistemin yeterliliğini doğrulamaz.

Mission qualification, ihtiyaç/önkoşul keşfi, Work admission/readiness, role/Actor, context, Environment, Run, evidence/qualification, acceptance, integration, recovery ve adaptation ilişkili sorumluluklar olarak ele alınır. Tek zorunlu linear pipeline kabul edilmedi.

## Güncel T08 sorusu

Bir hatayı düzeltmek ile gelecekte o hata sınıfına verilen tepkiyi kalıcı değiştirmek farklıdır. Kaydedilmiş ders, aktif yöntem, korunmuş davranış değişimi, fayda, yetki ve başka işe aktarım ayrı değerlendirilir. T08, yöntemin de kapsamı, kanıtı, uygulanma yolu ve geri dönüşü olan Work olarak ele alınabileceğini sınar. Yeni zorunlu Learning Agent veya learning-service mimarisi kabul etmez.

## Okuma yolları

| İhtiyaç | Yol |
|---|---|
| Güncel devam ve yetki | [STATE](STATE.md) |
| Test 8 ve kanıt sınırı | [T08](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) |
| İlk arşivin tamlık sorunu | [FIDELITY-20260921](checks/FIDELITY-20260921.md) |
| İlk 27 mesaj referansının sırası ve arşiv görünümleri | [Diyalog INDEX](sources/conversation/INDEX.md); assistant metinleri yoğunlaştırılmıştır |
| T1–T7'nin bütünlüklü tarihsel modeli | [CONSOLIDATION](artifacts/CONSOLIDATION.md) |
| Önceki kazanımlar ve görüş değişimi | [LEARNINGS](reflections/LEARNINGS.md), [EVOLUTION](reflections/EVOLUTION.md) |
| Yerel geçici terimler | [TERMS](reflections/TERMS.md); Concepts kabulü değil |
| Önceki epistemik nitelendirmeler | [QUALIFICATIONS](reflections/QUALIFICATIONS.md), sonraki kaynak düzeltmesi FIDELITY-20260921 |
| Açık model soruları | [OPEN-QUESTIONS](reflections/OPEN-QUESTIONS.md) |
| Konu ve örnek bulma | [TOPIC-MAP](retrieval/TOPIC-MAP.md) |
| Önceki denemelerle sıralı erişim | [CUMULATIVE-READING](retrieval/CUMULATIVE-READING.md); eski 122/tam-okuma dili kaynak sadakati notuyla sınırlıdır |
| Araştırma kullanım yolları | [RESEARCH-REFERENCES](sources/RESEARCH-REFERENCES.md); T08 kendi ek dayanaklarını taşır |
| İlk teknik yayın | [PUBLICATION](checks/PUBLICATION.md); kaynak aktarımının eksiksizliğini kanıtlamaz |
| Önceki aktarım/kapsam açıklamaları | [TRANSCRIPTION-NOTE](checks/TRANSCRIPTION-NOTE.md), [ARCHIVE-COVERAGE](checks/ARCHIVE-COVERAGE.md); sonraki FIDELITY notu ile birlikte |

## Sınırlar ve sonraki kullanım

Bu çalışma SOUL mimarisini kabul etmedi; Development OS veya gerçek ajan çalıştırmadı. Run / Execution Attempt, Qualification Case ve Re-entry Context aday çalışma ayrımlarıdır, zorunlu schema/service değildir. Mevcut araştırma teknik gerekçe/karşıörnek sağlayabilir; kaynakların sayısı veya aynı assistant'ın tekrar onayı bağımsız kanıt oluşturmaz.

T08 sonrası doğal karşı-test eşzamanlı işlerin yöntem, kaynak, sürüm ve yetki çatışmasıdır. Ayrıca önceki assistant metinlerinin eksiksiz özgün aktarımı açık arşiv işi olarak kalır. Bunların güncel sorumlulukları STATE'de ayrıdır; uygulama aşamasına kendiliğinden geçilmez.
