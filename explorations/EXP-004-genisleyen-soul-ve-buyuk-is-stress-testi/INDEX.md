# EXP-004 — Genişleyen SOUL ve büyük-iş stress testi

Önce [STATE](STATE.md) okunur. **Güncel devam T09: eşzamanlı değişiklikler ve ortak koşullar.** [T09 notu](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md) türetilmiş kavramsal kayıttır; canlı sistem testi veya mimari kabul değildir. U016'nın istediği bilinen kaynak onarımı önceki turda main üzerinde kapatılmıştır; [PUBLICATION](checks/PUBLICATION.md) o onarımın tarihsel yayın kaydıdır.

## Kaynak, özet ve tarih

[Kaynak diyalog](sources/conversation/INDEX.md): U001–U016/S001–S015, **31 görünür mesajlık korunmuş kesim**. S001–S013 özgün görünür yanıtlardan kısaltılmadan aktarılmıştır. Önceki yoğunlaştırılmış versiyonlar [ayrı tarihsel dizinde](artifacts/condensed-before-repair/README.md) aynı içerik kimlikleriyle korunur. S014 önceki yanlış tamlık bildirimini, S015 bunun açıklamasını taşır. [Aktarım sınırı](checks/TRANSCRIPTION-NOTE.md), [manifest](SOURCE-MANIFEST.json) ve [onarım kaydı](checks/REPAIR-20260921.md) farklı güvence türleridir.

[T1–T7 konsolidasyonu](artifacts/CONSOLIDATION.md) tarihsel türetilmiş eserdir. [T08 devam notu](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md), [tam S015 cevabıyla](sources/conversation/assistant/S015.md) aynı belge değildir. U016 açıklaması [kaynak mesaj](sources/conversation/USER-MESSAGES.md#u016) ve ayrı [çerçeve notu](reflections/FRAME-CLARIFICATION-20260921.md) üzerinden bulunur. T09 kaynak arşivi sayısını artırmaz; yeni bir tam konuşma aktarımı yapılmış gibi okunmaz.

## Amaç ve modelin evrimi

Başlangıçta agent, rol, iş, plan/workflow ve memory üzerinden büyük bir çalışma sistemi düşünülüyordu. Work/Actors/Information/Environment ve Composition araştırmalarıyla görev keşfi, hazırlık, gerçek etki, doğrulama, kabul ve devam ayrımları görünür oldu. Bu başlıklar bir yazılım modül listesi veya final ontoloji değildir.

SOUL'un oluşturduğu düzenle zorunlu olarak kopmadığı; işe göre yeni yetenekler ve aktörler eklerken mevcut sorumluluklarının yeni alanları da kapsayabileceği bir hipotez gelişti. U016, «büyüme»nin yalnız daha fazla parça anlamında düşünülmediğini açıklar. Dikey/yatay, iki dosya ve klasör ifadeleri açıklayıcı örneklerdir; fiziksel şema veya zorunlu araç kararı değildir. T08'in sadeleştirme/geri alma ihtimali bunlarla çatışan bir kullanıcı yasağı gibi okunmaz.

Sentetik vaka, bir eğitim yılı boyunca kullanılacak 4. sınıf matematik soru bankasını üretme, yayımlama ve sürdürmedir. Gerçek ülke, müfredat, eğitimsel etkinlik veya mevzuat araştırması yapılmadı. Her vaka bir başlığa yerleştirilebildi diye Foundation'ın ya da bir implementasyonun yeterliliği kanıtlanmış değildir.

## T09 ne ekledi?

İki yerel değişiklik, birbirinin kalmasını varsaydığı denetimi kaldırırsa tekil uygunluklar ortak uygunluk sağlamaz. Değişikliğin dayanak koşulları ve korunan ortak yükümlülük önemlidir. 60 dakikalık ortak kapasiteye karşı 40+35 dakikalık işler de ayrı ayrı hazır adaylarla birlikte başlatılabilir kümenin farklı olduğunu gösterir.

Güncel duruma bağlı kabul, ortak koşulun kapsamı, ilgili kaynak taahhüdü ve aktif geçiş birlikte düşünülür. Tek merkezi karar verici veya bütün sistemi sıralama zorunluluğu çıkarılmaz. Eski/yeni düzen arasındaki geçiş de denetlenir; yazılmış hedef yöntem aktif kontrol değildir. Bunlar mantıksal karşıörnekler ve mekanizma ihtiyaçlarıdır, canlı davranış güvencesi değildir.

## Nereden devam edilir?

Güncel amaç/yetki için STATE → T09; önceki yöntem-değişimi bağlamı gerekiyorsa S015/T08, kullanıcının örnek sınırı için U016. Önceki bir iddia karar açısından önemliyse kaynak S001–S013'e dönülür; konsolidasyon veya eski kısaltma onun yerine geçmez.

Bir sonraki doğal soru yeni aktör/araç/yol katıldığında ortak yükümlülüklerin fiilî kapsamasıdır. Bu tur T10 veya uygulama başlatılmadı. Branch benzetmesi araç/mekanizma seçimi değildir.

## Okuma yolları

| İhtiyaç | Yol |
|---|---|
| Güncel durum ve yetki | [STATE](STATE.md) |
| Eşzamanlı değişiklikler, kaynak ve ortak koşul | [T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md) |
| Korunmuş kaynak kesimi ve görünür gövdeler | [Diyalog INDEX](sources/conversation/INDEX.md) |
| Kaynak aktarımının sınırı | [TRANSCRIPTION-NOTE](checks/TRANSCRIPTION-NOTE.md), [ARCHIVE-COVERAGE](checks/ARCHIVE-COVERAGE.md) |
| İlk hata ve gerçek onarım | [FIDELITY](checks/FIDELITY-20260921.md), [REPAIR](checks/REPAIR-20260921.md) |
| T1–T7'nin tarihsel sentezi | [CONSOLIDATION](artifacts/CONSOLIDATION.md) |
| T1–T7 kazanım/görüş/terim kayıtları | [LEARNINGS](reflections/LEARNINGS.md), [EVOLUTION](reflections/EVOLUTION.md), [TERMS](reflections/TERMS.md) |
| T08 | [S015](sources/conversation/assistant/S015.md), [devam notu](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) |
| Yatay/dikey genişleme ve branch çağrışımı | [U016](sources/conversation/USER-MESSAGES.md#u016), [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) |
| Kanıt sınırları ve açık model soruları | [QUALIFICATIONS](reflections/QUALIFICATIONS.md), [OPEN-QUESTIONS](reflections/OPEN-QUESTIONS.md); yeni T09 soruları ayrıca T09/STATE'te |
| Konu/örnek bulma | [TOPIC-MAP](retrieval/TOPIC-MAP.md); kaynak kesimi U016'ya kadardır |
| Dört denemeyi sıralı okuma | [CUMULATIVE-READING](retrieval/CUMULATIVE-READING.md); 126 adreslenen kaynak mesaj, daha sonraki devam notları ayrı |
| Önceki denemelerden devir | [PREDECESSORS](sources/PREDECESSORS.md) |
| Araştırma yolları / tarihsel citation'lar | [RESEARCH-REFERENCES](sources/RESEARCH-REFERENCES.md), [CITATION-KEY](sources/CITATION-KEY.md); T09 kendi ek dayanaklarını taşır |
| Onarım yayını ve eski teknik yayın | [PUBLICATION](checks/PUBLICATION.md), [HISTORICAL-PUBLICATION](checks/HISTORICAL-PUBLICATION-PR29-30.md) |

## Yetki ve koruma

Run / Execution Attempt, Qualification Case ve Re-entry Context aday çalışma ayrımlarıdır, zorunlu service/schema değildir. T09 için kullanılan Beads/Gas Town araştırmaları ve PostgreSQL/Kubernetes mekanizma örnekleri ürün seçimi yapılması değildir. Kaynak arşivi, önceki eserler, Foundation, studies, concepts, önceki EXP kaynakları, agent-control ve target implementation bu devamda değiştirilmez.
