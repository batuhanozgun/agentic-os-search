# EXP-004 — Genişleyen SOUL ve büyük-iş stress testi

Önce [STATE](STATE.md) okunur. **Güncel devam T10: yeni katılım, etki yolları ve denetim kapsamı.** [T10 notu](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md) türetilmiş kavramsal kayıttır; canlı sistem testi veya mimari kabul değildir. Bilinen kaynak onarımı önceki turda main'de kapandı; [PUBLICATION](checks/PUBLICATION.md) o tarihsel onarımın yayın kaydıdır.

## Kaynak, özet ve tarih

[Kaynak diyalog](sources/conversation/INDEX.md): U001–U016/S001–S015, **31 görünür mesajlık korunmuş kesim**. S001–S013 özgün görünür yanıtlardan kısaltılmadan aktarılmıştır. Önceki yoğunlaştırılmış versiyonlar [ayrı tarihsel dizinde](artifacts/condensed-before-repair/README.md) aynı içerik kimlikleriyle korunur. S014 önceki yanlış tamlık bildirimini, S015 bunun açıklamasını taşır. [Aktarım sınırı](checks/TRANSCRIPTION-NOTE.md), [manifest](SOURCE-MANIFEST.json) ve [onarım kaydı](checks/REPAIR-20260921.md) farklı güvence türleridir.

[T1–T7 konsolidasyonu](artifacts/CONSOLIDATION.md) tarihsel türetilmiş eserdir. [T08 notu](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md), [tam S015 cevabıyla](sources/conversation/assistant/S015.md) aynı belge değildir. U016 açıklaması [kaynak mesaj](sources/conversation/USER-MESSAGES.md#u016) ve ayrı [çerçeve notu](reflections/FRAME-CLARIFICATION-20260921.md) üzerinden bulunur. T09 ve T10 notları kaynak arşivi sayısını artırmaz; yeni bir tam konuşma aktarımı yapılmış gibi okunmaz.

## Amaç ve modelin evrimi

Başlangıçta agent, rol, iş, plan/workflow ve memory üzerinden büyük bir çalışma sistemi düşünülüyordu. Work/Actors/Information/Environment ve Composition araştırmalarıyla görev keşfi, hazırlık, gerçek etki, doğrulama, kabul ve devam ayrımları görünür oldu. Bu başlıklar bir yazılım modül listesi veya final ontoloji değildir.

SOUL'un oluşturduğu düzenle zorunlu olarak kopmadığı; yeni yetenek ve aktörlerle mevcut sorumlulukların kapsamının da değişebileceği hipotezi gelişti. U016'nın dikey/yatay, iki dosya ve klasör ifadeleri açıklayıcı örneklerdir; fiziksel şema veya araç kararı değildir. T08'in sadeleştirme/geri alma ihtimali bunlarla çatışan kullanıcı yasağı gibi okunmaz.

Sentetik vaka, bir eğitim yılı boyunca kullanılacak 4. sınıf matematik soru bankasını üretme, yayımlama ve sürdürmedir. Gerçek ülke, müfredat, eğitimsel etkinlik veya mevzuat araştırması yapılmadı. Bir vakayı mevcut kategorilerle anlatmak Foundation/implementasyon yeterliliğini doğrulamaz.

## Son iki devam ne ekledi?

[T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md): iki yerel değişiklik birbirinin dayandığı kontrolü kaldırabilir; tekil hazırlık ortak kaynak taahhüdü değildir; iki uygun uç durum geçişin de uygun olduğunu göstermez. Bunlar kurulu mantıksal/aritmetik karşıörneklerdir, canlı davranış güvencesi değil.

[T10](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md): yeni aktör/araç/yayın yolu eski kontrolü bozmadan kapsam dışına çıkabilir. Yetenek oluşturma ile ilgili yükümlülükler altında etkin katılım ayrı. Aynı yükümlülük aynı kontrol tekniğini, kapsamın genişlemesi bütün erişimlerin genişlemesini gerektirmez. Gerekli kapsam/uygulanmış kontrol/gözlem kanıtı ve doğrudan/dolaylı etkiler ayrılır. Kritik etkiyi sınırlarken güvenli çalışma devam edebilir; titizlik kontrol sayısı değildir.

## Nereden devam edilir?

STATE → T10; ortak değişiklik bağlamı için T09, yöntem uyarlaması için S015/T08, örnek sınırları için U016. Karar açısından önemli önceki iddiada tam kaynak S001–S013'e dönülür; özet onun yerine geçmez.

Doğal sonraki karşı-test, kontrol/araştırma yükünün işi bitiremez hale getirmesidir: hangi kanıt yeterli, ne zaman ilerlenir/beklenir, kaynak ve gecikme nasıl değerlendirilir? Bu soru bu tur çalıştırılmadı. Farklı büyük-domain karşı testi de açık; ürün/uygulama yetkisi yok.

## Okuma yolları

| İhtiyaç | Yol |
|---|---|
| Güncel durum ve yetki | [STATE](STATE.md) |
| Yeni katılım, etki ve kontrol kapsamı | [T10](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md) |
| Eşzamanlı değişiklikler ve ortak koşul | [T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md) |
| Korunmuş kaynak kesimi | [Diyalog INDEX](sources/conversation/INDEX.md) |
| Aktarım/kapsam sınırı | [TRANSCRIPTION-NOTE](checks/TRANSCRIPTION-NOTE.md), [ARCHIVE-COVERAGE](checks/ARCHIVE-COVERAGE.md) |
| İlk hata ve onarım | [FIDELITY](checks/FIDELITY-20260921.md), [REPAIR](checks/REPAIR-20260921.md) |
| T1–T7 tarihsel sentezi | [CONSOLIDATION](artifacts/CONSOLIDATION.md) |
| T1–T7 kazanım/görüş/terimler | [LEARNINGS](reflections/LEARNINGS.md), [EVOLUTION](reflections/EVOLUTION.md), [TERMS](reflections/TERMS.md) |
| T08 | [S015](sources/conversation/assistant/S015.md), [devam notu](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) |
| Yatay/dikey kapsama ve branch çağrışımı | [U016](sources/conversation/USER-MESSAGES.md#u016), [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) |
| Kanıt sınırları / önceki açık sorular | [QUALIFICATIONS](reflections/QUALIFICATIONS.md), [OPEN-QUESTIONS](reflections/OPEN-QUESTIONS.md); sonraki sorular T09/T10/STATE'te |
| Korunmuş kesimde konu bulma | [TOPIC-MAP](retrieval/TOPIC-MAP.md); U016'ya kadar |
| Dört denemeyi sıralı okuma | [CUMULATIVE-READING](retrieval/CUMULATIVE-READING.md); 126 kaynak mesaj adresi, sonraki notlar ayrı |
| Önceki denemelerden devir | [PREDECESSORS](sources/PREDECESSORS.md) |
| Araştırma/citation yolları | [RESEARCH-REFERENCES](sources/RESEARCH-REFERENCES.md), [CITATION-KEY](sources/CITATION-KEY.md); T09/T10 ek kaynakları kendi notlarında |
| Onarımın yayın tarihi | [PUBLICATION](checks/PUBLICATION.md), [HISTORICAL-PUBLICATION](checks/HISTORICAL-PUBLICATION-PR29-30.md) |

## Yetki ve koruma

Run / Execution Attempt, Qualification Case ve Re-entry Context aday ayrımlardır, zorunlu service/schema değildir. Kullanılan araştırmalar veya dış teknik örnekler ürün seçimi değildir. Kaynak arşivi/manifest, önceki eserler, onarım kanıtı, Foundation, studies, concepts, agent-control, önceki EXP kaynakları ve target implementation bu devamda değiştirilmez.
