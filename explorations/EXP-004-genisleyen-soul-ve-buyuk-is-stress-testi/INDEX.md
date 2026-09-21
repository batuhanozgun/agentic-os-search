# EXP-004 — Genişleyen SOUL ve büyük-iş stress testi

Önce [STATE](STATE.md) okunur. **T1–T8 kavramsal çalışma; U016'nın önceliği arşiv onarımıdır.** Kaynak içerik onarılmıştır; main yayınının gerçek durumu [PUBLICATION](checks/PUBLICATION.md) ve STATE'te ayrı tutulur. Bu paket gerçek SOUL runtime'ı veya benimsenmiş mimari değildir.

## Kaynak, özet ve tarih

[Kaynak diyalog](sources/conversation/INDEX.md): U001–U016/S001–S015, **31 görünür mesaj**. S001–S013 artık özgün görünür yanıtlardan kısaltılmadan aktarılmıştır. Önceki yoğunlaştırılmış versiyonlar [ayrı tarihsel dizinde](artifacts/condensed-before-repair/README.md) aynı içerik kimlikleriyle korunur. S014 önceki yanlış tamlık bildirimini, S015 bunun açıklamasını taşır. [Aktarım sınırı](checks/TRANSCRIPTION-NOTE.md), [manifest](SOURCE-MANIFEST.json) ve [onarım kaydı](checks/REPAIR-20260921.md) farklı güvence türleridir.

[T1–T7 konsolidasyonu](artifacts/CONSOLIDATION.md) tarihsel türetilmiş eserdir. [T08 devam notu](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md), [tam S015 cevabıyla](sources/conversation/assistant/S015.md) aynı belge değildir. Son kullanıcı açıklaması [U016](sources/conversation/USER-MESSAGES.md#u016) ve ayrı [çerçeve notu](reflections/FRAME-CLARIFICATION-20260921.md) üzerinden bulunur.

## Amaç ve modelin evrimi

Başlangıçta agent, rol, iş, plan/workflow ve memory üzerinden büyük bir çalışma sistemi düşünülüyordu. Work/Actors/Information/Environment ve Composition araştırmalarıyla görev keşfi, hazırlık, gerçek etki, doğrulama, kabul ve devam ayrımları görünür oldu. Bu başlıklar bir yazılım modül listesi veya final ontoloji değildir.

SOUL'un oluşturduğu düzenle zorunlu olarak kopmadığı; işe göre yeni yetenekler ve aktörler eklerken mevcut sorumluluklarının yeni alanları da kapsayabileceği bir hipotez gelişti. U016, “büyüme”nin yalnız daha fazla parça anlamında düşünülmediğini açıklar. Dikey/yatay, iki dosya ve klasör ifadeleri açıklayıcı örneklerdir; fiziksel şema veya zorunlu araç kararı değildir. T08'in sadeleştirme/geri alma ihtimali bunlarla çatışan bir kullanıcı yasağı gibi okunmaz.

Sentetik vaka, bir eğitim yılı boyunca kullanılacak 4. sınıf matematik soru bankasını üretme, yayımlama ve sürdürmedir. Gerçek ülke, müfredat, eğitimsel etkinlik veya mevzuat araştırması yapılmadı. Her vaka bir başlığa yerleştirilebildi diye Foundation'ın ya da bir implementasyonun yeterliliği kanıtlanmış değildir.

## Nereden devam edilir?

Güncel amaç/yetki için STATE; T08 için S015 ve gerekiyorsa türetilmiş devam notu; son anlam düzeltmesi için U016 okunur. Önceki bir iddia karar açısından önemliyse kaynak S001–S013'e dönülür; konsolidasyon veya eski kısaltma onun yerine geçmez.

T08, olay kaydı, geri bildirimin kullanılması, kalıcı davranış değişimi, fayda, yetki ve başka işe aktarımı ayırır. Yöntem değişikliğinin kaydedilmesiyle aktif tüketicilere uygulanması eşitlenmez. Doğal sonraki soru eşzamanlı işlerin yöntem/kaynak/sürüm/yetki çatışmalarıdır; bu onarım turunda o test başlatılmadı.

## Okuma yolları

| İhtiyaç | Yol |
|---|---|
| Güncel durum ve yetki | [STATE](STATE.md) |
| Kaynak sırası ve tüm görünür gövdeler | [Diyalog INDEX](sources/conversation/INDEX.md) |
| Kaynak aktarımının sınırı | [TRANSCRIPTION-NOTE](checks/TRANSCRIPTION-NOTE.md), [ARCHIVE-COVERAGE](checks/ARCHIVE-COVERAGE.md) |
| İlk hata ve gerçek onarım | [FIDELITY](checks/FIDELITY-20260921.md), [REPAIR](checks/REPAIR-20260921.md) |
| T1–T7'nin tarihsel sentezi | [CONSOLIDATION](artifacts/CONSOLIDATION.md) |
| T1–T7 kazanım/görüş/terim kayıtları | [LEARNINGS](reflections/LEARNINGS.md), [EVOLUTION](reflections/EVOLUTION.md), [TERMS](reflections/TERMS.md) |
| T08 | [S015](sources/conversation/assistant/S015.md), [devam notu](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) |
| Yatay/dikey genişleme ve branch çağrışımı | [U016](sources/conversation/USER-MESSAGES.md#u016), [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) |
| Kanıt sınırları ve açık model soruları | [QUALIFICATIONS](reflections/QUALIFICATIONS.md), [OPEN-QUESTIONS](reflections/OPEN-QUESTIONS.md) |
| Konu/örnek bulma | [TOPIC-MAP](retrieval/TOPIC-MAP.md) |
| Dört denemeyi sıralı okuma | [CUMULATIVE-READING](retrieval/CUMULATIVE-READING.md); 126 adreslenen mesaj, paketlerin sınırları korunur |
| Önceki denemelerden devir | [PREDECESSORS](sources/PREDECESSORS.md) |
| Araştırma yolları / tarihsel citation'lar | [RESEARCH-REFERENCES](sources/RESEARCH-REFERENCES.md), [CITATION-KEY](sources/CITATION-KEY.md) |
| Güncel yayın ve eski teknik yayın | [PUBLICATION](checks/PUBLICATION.md), [HISTORICAL-PUBLICATION](checks/HISTORICAL-PUBLICATION-PR29-30.md) |

## Yetki ve koruma

Run / Execution Attempt, Qualification Case ve Re-entry Context aday çalışma ayrımlarıdır, zorunlu service/schema değildir. Branch çağrışımı araç seçimi değildir. U016'nın onarım yetkisi Foundation, studies, concepts, önceki EXP kaynakları, agent-control veya target implementation değişikliği olarak kullanılmaz.
