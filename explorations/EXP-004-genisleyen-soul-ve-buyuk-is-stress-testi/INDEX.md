# EXP-004 — Genişleyen SOUL ve büyük-iş stress testi

Önce [STATE](STATE.md) okunur. **Güncel çalışma: MS01 — SOUL Çalışma Sistemi Taslağı v0.1, Checkpoint A.** Kullanıcının RV01 sonrasında kabul ettiği planla ilk bütünleşik taslak ve soru-bankası yürüyüşü yazıldı. Romanın aynı yapı üzerinde tam yürüyüşü ve son birleşim değerlendirmesi açık; MS01/EXP-004 tamamlandı sayılmaz.

## 1. Güncel taslak paketi

| İhtiyaç | Yol |
|---|---|
| Baz SOUL, işe özgü genişleme, kayıtlar ve K1–K7 mekanizmaları | [MS01 ana taslak](artifacts/MS01-SOUL-WORKING-SYSTEM-DRAFT.md) |
| Talep→keşif→aktör/bağlam→üretim→kabul→değişim/kesinti→iç teslim | [MS01 soru-bankası yürüyüşü](artifacts/MS01-QUESTION-BANK-WALKTHROUGH.md) |
| T1–T15/DQ01–DQ04 karşılıkları, G01–G07 açıkları ve gerçek kaynak kapsamı | [MS01 kapsama/açıklar/kaynaklar](artifacts/MS01-COVERAGE-AND-OPEN-MECHANISMS.md) |
| Neden bağımsız DQ zincirinden mekanizma sentezine dönüldü? | [RV01](reflections/RV01-DIRECTION-REVIEW-AND-MECHANISM-TARGET.md) |

MS01; modelin yönlendirdiği, host kodunun durum/etki sınırlarını koruduğu hibrit bir başlangıç tercihidir. Mission başına tek mantıksal commit yolu ile paralel aday üretimi ayrıldı. İlk işi Bootstrap Actor B0 ve önceden hazırlanmış host/yetki zemini başlatır. RV01'in adları sabit sekiz servis sayılmadı; kayıtlar ve çalışan işlevler ayrıldı.

K1 Mission Interpreter/Discovery Driver; K2 Work Coordinator; K3 Context Builder; K4 Capability Binder/Method Selector; K5 Domain Workbench; K6 Run Controller/State Committer/Effect Broker; K7 Change & Recovery Manager. Kontrol noktaları hosttan bağımsız taslak adlarıdır; çalışan hook/API değildir. Yeni rol, yöntem veya araç bağlanması mevcut context, kabul, etki ve recovery kapsamına da katılmayı gerektirir.

Bu parça adları Concepts tanımı, Foundation ground'larının birebir servis karşılığı veya kabul edilmiş mimari değildir. Kurgusal walkthrough'da verilen olumlu/olumsuz sonuçlar gerçek agent performansı değildir.

## 2. Okuma ve devam yolu

Yeni devralış: **STATE → bu INDEX → RV01 → MS01 ana taslak → soru-bankası yürüyüşü → kapsama/açıklar**. Mevcut birikimin ilk tam devralışında SY01 ve DQ01–DQ04 tam okunur. Aynı konuşmada tam okunmuş değişmemiş canonical metinler kullanılabilir; yeniden okunmuş gibi gösterilmez. Karar-kritik noktada ilgili asıl T/kaynak ve research primary rotasına dönülür.

Sonraki bağlı iş G07 / roman yürüyüşüdür. İlk yazılabilir iş, creative/story state, uzun okuma, anlamsal revizyon, editoryal anlaşmazlık ve bütünsel teslim aynı K1–K7 üzerinde sınanacak; gerekirse bu taslak değişecek. Yeni DQ05 yöntem çatışması sorusu bağımsız varsayılan sonraki tur değildir; K4/K7'nin somut birleşim sorusu olarak gerektiğinde açılır.

Tamamlanma, iki senaryonun ve önceki bulguların mekanizma karşılığıyla, açıklanan/kısmi/açık statüsüyle bir araya gelmesini gerektirir. Canlı deney/implementasyon ayrı aşamadır. Mevcut Checkpoint A'da bütün EXP-004'e kapanış verilmez.

## 3. Önceki tamamlanmış kavramsal girdiler

| İhtiyaç | Yol |
|---|---|
| İki senaryonun ortak sorumlulukları, kapasite/kanıt ve üç düzey | [SY01](artifacts/SY01-CROSS-SCENARIO-WORK-SYSTEM-SYNTHESIS.md) |
| İşaret edilmemiş ihtiyaç, eksiklik teşhisi ve kullanım-bağlı yeterlik | [DQ01](continuations/DQ01-UNSIGNALED-NEED-DISCOVERY-AND-CAPABILITY-QUALIFICATION.md) |
| Keşif yöntemi, uygulanabilir inceleme ve ortak körlük | [DQ02](continuations/DQ02-DISCOVERY-METHOD-SELECTION-AND-COMMON-BLIND-SPOTS.md) |
| Üst iş/başarı gerekçesini yeniden açma, yetki ve geçerli işi koruma | [DQ03](continuations/DQ03-WORK-FRAME-REVISION-AUTHORITY-AND-PRESERVATION.md) |
| Koşullu aktarım, baz kabul ve uygun yerde seçme/kullanmama | [DQ04](continuations/DQ04-CONDITIONAL-TRANSFER-AND-BASE-ADMISSION.md) |
| Özgün yapı amacı ve test yöntemi | [U001](sources/conversation/USER-MESSAGES.md#u001), [S004](sources/conversation/assistant/S004.md), [S005](sources/conversation/assistant/S005.md) |
| İhtiyaç ve aktör yeterliğinin özgün konuşma dayanakları | [S008 / T2](sources/conversation/assistant/S008.md), [S009 / T3](sources/conversation/assistant/S009.md) |
| T1–T7 tarihsel türev sentez | [CONSOLIDATION](artifacts/CONSOLIDATION.md) |
| Editoryal görüş ayrılığı, tespit/tercih/yetki | [T15](continuations/T15-NOVEL-EDITORIAL-DISAGREEMENT-AND-CHOICE.md) |
| Uzun eserin okunması, ilişki kapsamı ve ortak bağlam | [T14](continuations/T14-NOVEL-READING-COVERAGE-AND-JOINT-CONTEXT.md) |
| Anlamsal değişiklik etkisi ve korunacak metin | [T13](continuations/T13-NOVEL-SEMANTIC-REVISION-AND-IMPACT.md) |
| Romanın ilk yazılabilir işi, canon/provisional/draft | [T12](continuations/T12-NOVEL-FORMATION-AND-FIRST-WRITABLE-WORK.md) |
| İkinci senaryo seçimi ve sınırları | [SC02](continuations/SC02-NOVEL-SCENARIO-ASSESSMENT.md) |
| Yeterli kanıt, araştırma maliyeti ve bitirebilme | [T11](continuations/T11-EVIDENCE-SUFFICIENCY-AND-BOUNDED-PROGRESS.md) |
| Yeni katılım ve kontrolün gerçek kapsamı | [T10](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md) |
| Eşzamanlı değişim ve ortak koşullar | [T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md) |
| Geri bildirim ve kontrollü uyarlama | [T08 türev not](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md), [S015 özgün yanıt](sources/conversation/assistant/S015.md) |
| Yatay/dikey büyüme ve branch çağrışımının kaynak sınırı | [U016](sources/conversation/USER-MESSAGES.md#u016), [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) |

Bu kaynakların varlığı yeniden yapılmaları gerektiği anlamına gelmez. SY01/DQ/RV01/MS01 kaynak diyalog değildir; notların kaynak tabloları asıl araştırmaya dönüşü sağlar. RPD assessment'ın bulunması özgün eklerinin erişilebilir olduğu anlamına gelmez.

## 4. Arşiv, onarım ve diğer geri erişim yolları

Korunmuş kaynak diyalog U001–U016 / S001–S015, **31 görünür mesaj ve 16 dosyadır**. S001–S013 önce yoğunlaştırılmış, sonra görünür özgün yanıtlardan tam aktarılmıştır. Eski yoğunlaştırmalar kendi Git kimlikleriyle ayrı dizindedir. S014 önceki yanlış tamlık bildirimi, S015 T08 cevabı, U016 onarım ve açıklama kaynağıdır. Platform export'u veya bağımsız transkripsiyon doğrulaması yoktur.

| İhtiyaç | Yol |
|---|---|
| Korunmuş kaynak kesimi | [Diyalog INDEX](sources/conversation/INDEX.md), [USER-MESSAGES](sources/conversation/USER-MESSAGES.md) |
| Kaynak kimlikleri ve aktarım sınırı | [SOURCE-MANIFEST](SOURCE-MANIFEST.json), [TRANSCRIPTION-NOTE](checks/TRANSCRIPTION-NOTE.md), [ARCHIVE-COVERAGE](checks/ARCHIVE-COVERAGE.md) |
| İlk hata ve onarım | [FIDELITY](checks/FIDELITY-20260921.md), [REPAIR](checks/REPAIR-20260921.md), [eski yoğunlaştırmalar](artifacts/condensed-before-repair/README.md) |
| Onarımın yayın tarihi | [PUBLICATION](checks/PUBLICATION.md), [HISTORICAL-PUBLICATION](checks/HISTORICAL-PUBLICATION-PR29-30.md) |
| T1–T7 tarihsel kazanımlar | [LEARNINGS](reflections/LEARNINGS.md), [EVOLUTION](reflections/EVOLUTION.md), [TERMS](reflections/TERMS.md) |
| Kanıt sınırları ve önceki sorular | [QUALIFICATIONS](reflections/QUALIFICATIONS.md), [OPEN-QUESTIONS](reflections/OPEN-QUESTIONS.md); yeni açıklar MS01'dedir |
| U016'ya kadarki konularda gezinme | [TOPIC-MAP](retrieval/TOPIC-MAP.md) |
| Dört denemeyi sıralı okuma | [CUMULATIVE-READING](retrieval/CUMULATIVE-READING.md); 126 kümülatif kaynak adresi |
| Önceki EXP ve araştırma dayanakları | [PREDECESSORS](sources/PREDECESSORS.md), [RESEARCH-REFERENCES](sources/RESEARCH-REFERENCES.md), [CITATION-KEY](sources/CITATION-KEY.md) |
| MS01 öncesi tam uzun giriş | [RV01 yayınındaki INDEX](https://github.com/batuhanozgun/agentic-os-search/blob/0dd58080eeea4ee8c7eaaaef0902d02fce825edc/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/INDEX.md), [STATE](https://github.com/batuhanozgun/agentic-os-search/blob/0dd58080eeea4ee8c7eaaaef0902d02fce825edc/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/STATE.md) |

MS01 ayrı derived taslak dosyalarıdır; kaynak sayımını artırmaz. Tarihsel ayrıntılı girişler korunmuş ref'lerden bulunur; current yön için bugünkü STATE geçerlidir. Kontrol dosyaları yalnız `AGENT.md` ve `agent/**` altındadır; bu proje notları agent-control yerine geçmez.

## 5. Yetki ve koruma

Bu checkpoint üç MS01 dosyasını oluşturur ve STATE/INDEX'i günceller. T1–T15, SC02, SY01, DQ01–DQ04, RV01, kaynak/manifest ve onarım metinleri korunur. Foundation, studies, concepts, diğer EXP ve target implementation değişmez. Araştırmaların eski doğrulama/erişim sınırları bu taslakla kapanmaz.

Gerçek ürün/öğrenci/okur/model deneyi, host kurulumu veya ortak baz davranış değişikliği yapılmadı. Kurgusal kontrol noktaları ve mekanizma tercihleri araştırılabilir taslak sözleşmeleridir. Sözleşmenin tarif edilmiş olması onun doğru, atlanamaz veya güvenilir biçimde uygulandığı anlamına gelmez.
