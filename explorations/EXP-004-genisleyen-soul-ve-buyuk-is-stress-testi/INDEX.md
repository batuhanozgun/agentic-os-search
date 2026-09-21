# EXP-004 — Genişleyen SOUL ve büyük-iş stress testi

Önce [STATE](STATE.md) okunur. **Güncel devam T11: kanıt yeterliliği, araştırmayı sınırlama ve ilerleyebilme.** [T11](continuations/T11-EVIDENCE-SUFFICIENCY-AND-BOUNDED-PROGRESS.md) türetilmiş kavramsal kayıttır; canlı test veya mimari kabul değildir. Bilinen kaynak onarımı önceki turda main'de kapandı; [PUBLICATION](checks/PUBLICATION.md) o onarımın tarihsel yayın kaydıdır.

## Kaynak, özet ve tarih

[Kaynak diyalog](sources/conversation/INDEX.md): U001–U016/S001–S015, **31 görünür mesajlık korunmuş kesim**. S001–S013 özgün görünür yanıtlardan kısaltılmadan aktarılmıştır. Eski yoğunlaştırmalar [ayrı tarihsel dizinde](artifacts/condensed-before-repair/README.md) aynı içerik kimlikleriyle durur. S014 önceki yanlış tamlık bildirimini, S015 açıklamasını taşır. [Aktarım sınırı](checks/TRANSCRIPTION-NOTE.md), [manifest](SOURCE-MANIFEST.json), [onarım](checks/REPAIR-20260921.md) farklı güvence türleridir.

[T1–T7 konsolidasyonu](artifacts/CONSOLIDATION.md) tarihsel türevdir. [T08](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) ile [tam S015](sources/conversation/assistant/S015.md) aynı belge değildir. U016 [kaynak mesaj](sources/conversation/USER-MESSAGES.md#u016) ve [çerçeve notu](reflections/FRAME-CLARIFICATION-20260921.md) ile bulunur. T09–T11 devam notları kaynak arşivi sayısını artırmaz; tam konuşma aktarımı diye okunmaz.

## Amaç ve modelin evrimi

Başlangıçtaki agent/rol/iş/plan/memory çerçevesi, Foundation ve studies'le iş keşfi, hazırlık, gerçek etki, doğrulama, kabul, süreklilik, değişim ve ilerleme sorularına açıldı. Work/Actors/Information/Environment ve Composition ayrımları düşünme zeminidir; final ontoloji veya yazılım modül listesi değildir.

SOUL'un oluşturduğu düzenden zorunlu olarak kopmadığı; yeni yeteneklerle mevcut işlevlerin kapsamının da değişebileceği hipotezi gelişti. U016'nın dikey/yatay, iki dosya ve klasör ifadeleri örnektir; branch çağrışımı araç seçimi değildir. Sadeleştirme/geri alma bunlarla yasaklanmış sayılmaz.

Soru-bankası vakası bir yıllık büyük programdır. T11'in küçük teslimat dilimi bu büyük hedefin yerine geçmez. Gerçek ülke, müfredat, eğitimsel etkinlik veya mevzuat araştırması yapılmadı. Bir vakayı mevcut kategorilerle anlatmak Foundation/implementasyon yeterliliğini doğrulamaz.

## Son devamlar

[T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md): yerel kararların ortak uygunluğu, kaynak taahhüdü ve güvenli geçiş.

[T10](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md): yeni aktör/araç/yolun mevcut yükümlülükler altında fiilen kapsanması; yetenek ile etkiye kabul; gerekli, uygulanan ve gözlenmiş kapsam.

[T11](continuations/T11-EVIDENCE-SUFFICIENCY-AND-BOUNDED-PROGRESS.md): açık soruların otomatik blocker olmaması; karar/kullanım için yeterli kanıt; zorunlu şartı gevşetmeden, önceden izinli ve kendi başına yararlı dilimi ilerletme; ek araştırmanın katkısı ve maliyeti; kaynak sınırı ile doğruluk/kabulü ayırma; sınırlı kapanış ve yeniden açma.

Bunlar kurulu karşıörnekler ve mekanizma ihtiyaçlarıdır, gerçek SOUL davranış güvencesi değildir.

## Nereden devam edilir?

STATE → T11. Kapsama bağlamı için T10, ortak değişim için T09, yöntem uyarlaması için S015/T08, örnek sınırları için U016. Karar açısından önemli önceki ifadede tam kaynak S001–S013'e dönülür; özet kaynak yerine geçmez.

T11'in bounded sorusu ele alındı. Sonraki doğal karşı-test aynı modeli farklı bir büyük iş alanına taşımaktır; bu tur ikinci alan testi yapılmadı. Uygulama/ürün seçimi otomatik sonraki iş değildir.

## Okuma yolları

| İhtiyaç | Yol |
|---|---|
| Güncel durum/yetki | [STATE](STATE.md) |
| Kanıt yeterliliği, araştırma maliyeti ve bitirebilme | [T11](continuations/T11-EVIDENCE-SUFFICIENCY-AND-BOUNDED-PROGRESS.md) |
| Yeni katılım ve kontrol kapsamı | [T10](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md) |
| Eşzamanlı değişim ve ortak koşul | [T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md) |
| Korunmuş kaynak kesimi | [Diyalog INDEX](sources/conversation/INDEX.md) |
| Aktarım/kapsam | [TRANSCRIPTION-NOTE](checks/TRANSCRIPTION-NOTE.md), [ARCHIVE-COVERAGE](checks/ARCHIVE-COVERAGE.md) |
| İlk hata ve onarım | [FIDELITY](checks/FIDELITY-20260921.md), [REPAIR](checks/REPAIR-20260921.md) |
| T1–T7 tarihsel sentez/kazanım | [CONSOLIDATION](artifacts/CONSOLIDATION.md), [LEARNINGS](reflections/LEARNINGS.md), [EVOLUTION](reflections/EVOLUTION.md), [TERMS](reflections/TERMS.md) |
| T08 | [S015](sources/conversation/assistant/S015.md), [not](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) |
| Yatay/dikey kapsama ve branch çağrışımı | [U016](sources/conversation/USER-MESSAGES.md#u016), [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) |
| Kanıt sınırları/önceki sorular | [QUALIFICATIONS](reflections/QUALIFICATIONS.md), [OPEN-QUESTIONS](reflections/OPEN-QUESTIONS.md); yeni sorular ilgili devam/STATE'te |
| U016'ya kadarki konuda gezinme | [TOPIC-MAP](retrieval/TOPIC-MAP.md) |
| Dört denemeyi sıralı okuma | [CUMULATIVE-READING](retrieval/CUMULATIVE-READING.md); 126 kaynak mesaj adresi, sonraki notlar ayrı |
| Önceki denemeler ve research kaynakları | [PREDECESSORS](sources/PREDECESSORS.md), [RESEARCH-REFERENCES](sources/RESEARCH-REFERENCES.md), [CITATION-KEY](sources/CITATION-KEY.md); devamların ek kaynakları kendi notlarında |
| Onarımın yayın tarihi | [PUBLICATION](checks/PUBLICATION.md), [HISTORICAL-PUBLICATION](checks/HISTORICAL-PUBLICATION-PR29-30.md) |

## Yetki ve koruma

Run / Execution Attempt, Qualification Case ve Re-entry Context aday ayrımlardır, zorunlu service/schema değildir. Metareasoning/RPD referansları algoritma benimsemesi değildir. Kaynak arşivi/manifest, önceki eserler, onarım kanıtı, Foundation, studies, concepts, agent-control, önceki EXP ve target implementation bu devamda değiştirilmez.
