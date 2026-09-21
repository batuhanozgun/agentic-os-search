# EXP-004 — Genişleyen SOUL ve büyük-iş stress testi

Önce [STATE](STATE.md) okunur. **Güncel çıktı: MS01 — SOUL Çalışma Sistemi Taslağı v0.1, Checkpoint B / REVIEW READY.** İsimli yapı, iki kurgusal yürüyüş ve sınırlı birleşim incelemesi hazırdır. Kullanıcı değerlendirmesi beklenir; nihai mimari, gerçek SOUL yeterliği veya implementasyon kabulü yoktur.

## 1. Güncel taslak paketi

| İhtiyaç | Yol |
|---|---|
| Baz SOUL, işe özgü genişleme, kayıtlar, K1–K7 ve P1–P9 | [MS01 ana taslak](artifacts/MS01-SOUL-WORKING-SYSTEM-DRAFT.md) |
| Talep→keşif→üretim→kabul→kaynak değişimi/kesinti→iç teslim | [Soru-bankası yürüyüşü — Checkpoint A](artifacts/MS01-QUESTION-BANK-WALKTHROUGH.md) |
| Yaratıcı başlangıç→sahne→motivasyon revizyonu→okuma→editoryal karar→koşullu teslim | [Roman yürüyüşü — Checkpoint B](artifacts/MS01-NOVEL-WALKTHROUGH.md) |
| Test/bulgu karşılıkları, birleşim/sadeleştirme, G01–G07 ve kaynaklar | [MS01 kapsam ve birleşim kaydı](artifacts/MS01-COVERAGE-AND-OPEN-MECHANISMS.md) |
| Drift değerlendirmesi ve taslakla kapanış hedefi | [RV01](reflections/RV01-DIRECTION-REVIEW-AND-MECHANISM-TARGET.md) |

Model yönlendirmesi ile hostun mekanik yaptırımı birlikte kullanılır. Mission başına tek mantıksal commit yolu paralel candidate üretimini dışlamaz. B0 ilk işi başlangıç yetkisiyle açar; henüz kurulmamış Mission Contract kendi oluşumuna izin veren kaynak değildir.

K1 Mission Interpreter/Discovery Driver; K2 Work Coordinator; K3 Context Builder; K4 Capability Binder/Method Selector; K5 Domain Workbench; K6 Run Controller/State Committer/Effect Broker; K7 Change & Recovery Manager. Bunlar yedi zorunlu agent/servis değildir. `before_work_start`, `before_effect`, `before_result_admission`, `after_state_change`, `on_resume` kurgusal kontrol noktalarıdır; çalışan API veya hook değildir.

B'nin somut katkısı: Work-mode/etki bazlı admission; exact sıralı Assembly Snapshot; tasarım/çalışma metni/teslim ayrımı; süren Reading Pass ve kaynak-bağlı açık sorular; birlikte yöntem incelemesi. Narrative Ledger, Scene Brief ve Revision Package mevcut kayıt/Work sözleşmelerinin alan görünümleridir. Yeni Canon Service veya her karaktere agent eklenmedi.

## 2. Okuma, değerlendirme ve sonraki yetki

Yeni devralış: **STATE → bu INDEX → RV01 → MS01 ana taslak → banka A → roman B → kapsama/birleşim**. Mevcut birikimin ilk devralışında SY01 ve DQ01–DQ04 tam okunur. Aynı konuşmada tam okunmuş değişmemiş canonical metinler kullanılabilir; yeniden okunmuş gibi gösterilmez. Karar-kritik ayrımda asıl T/kaynak ve ilgili research primary yüzeyine dönülür.

A'daki «roman sonraki iş» cümleleri tarihsel checkpoint'tir. Roman yürüyüşü B'de tamamlandı; **gerçek uzun roman üretme/değerlendirme kapasitesi G07 açık**. T1–T15/DQ01–DQ04 yeniden yapılacak iş değildir. MS01 bir kaynak transkripti veya yeni T16 değildir.

MS01 v0.1'in kavramsal teslimat koşulları assistant'ın sınırlı self-review'uyla karşılandı: isimli mekanizmalar, iki yürüyüş ve kapsam/açıklar birlikte var. EXP-004'ün kapanış adayı kullanıcı değerlendirmesini bekler. Otomatik yeni DQ05, genel araştırma kampanyası, ürün seçimi veya implementasyon açılmaz. Düzeltme gerekirse adı konmuş mekanizma ve kapsam üzerinden yapılır.

## 3. Önceki tamamlanmış kavramsal girdiler

| İhtiyaç | Yol |
|---|---|
| İki senaryonun ortak sorumlulukları, kapasite/kanıt ve üç düzey | [SY01](artifacts/SY01-CROSS-SCENARIO-WORK-SYSTEM-SYNTHESIS.md) |
| İşaret edilmemiş ihtiyaç, eksiklik teşhisi ve yeterlik | [DQ01](continuations/DQ01-UNSIGNALED-NEED-DISCOVERY-AND-CAPABILITY-QUALIFICATION.md) |
| Keşif yöntemi, uygulanabilir inceleme ve ortak körlük | [DQ02](continuations/DQ02-DISCOVERY-METHOD-SELECTION-AND-COMMON-BLIND-SPOTS.md) |
| Üst iş/başarı gerekçesini yeniden açma | [DQ03](continuations/DQ03-WORK-FRAME-REVISION-AUTHORITY-AND-PRESERVATION.md) |
| Koşullu aktarım, baz kabul ve seçici kullanım | [DQ04](continuations/DQ04-CONDITIONAL-TRANSFER-AND-BASE-ADMISSION.md) |
| Özgün yapı amacı ve test yöntemi | [U001](sources/conversation/USER-MESSAGES.md#u001), [S004](sources/conversation/assistant/S004.md), [S005](sources/conversation/assistant/S005.md) |
| İhtiyaç/aktör ayrımlarının özgün konuşma dayanakları | [S008 / T2](sources/conversation/assistant/S008.md), [S009 / T3](sources/conversation/assistant/S009.md) |
| T1–T7 tarihsel türev sentez | [CONSOLIDATION](artifacts/CONSOLIDATION.md) |
| Editoryal görüş ayrılığı ve seçim | [T15](continuations/T15-NOVEL-EDITORIAL-DISAGREEMENT-AND-CHOICE.md) |
| Uzun eser, kaynak/ilişki okuması | [T14](continuations/T14-NOVEL-READING-COVERAGE-AND-JOINT-CONTEXT.md) |
| Anlamsal revizyon ve korunacak metin | [T13](continuations/T13-NOVEL-SEMANTIC-REVISION-AND-IMPACT.md) |
| Romanın ilk yazılabilir işi ve yaratıcı durum | [T12](continuations/T12-NOVEL-FORMATION-AND-FIRST-WRITABLE-WORK.md) |
| İkinci senaryo seçimi ve sınırları | [SC02](continuations/SC02-NOVEL-SCENARIO-ASSESSMENT.md) |
| Kanıt yeterliliği, maliyet ve bitirebilme | [T11](continuations/T11-EVIDENCE-SUFFICIENCY-AND-BOUNDED-PROGRESS.md) |
| Yeni katılım ve kontrol kapsamı | [T10](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md) |
| Eşzamanlı değişim ve ortak koşullar | [T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md) |
| Geri bildirim ve kontrollü uyarlama | [T08 türev not](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md), [S015 özgün yanıt](sources/conversation/assistant/S015.md) |
| Yatay/dikey büyüme ve branch çağrışımı | [U016](sources/conversation/USER-MESSAGES.md#u016), [FRAME-CLARIFICATION](reflections/FRAME-CLARIFICATION-20260921.md) |

SY01/DQ/RV01/MS01 kaynak diyalog değildir. T12–T15 ve T08 de türetilmiş notlardır; S015 özgün görünür yanıt aktarımıdır. Kaynak tabloları asıl araştırmaya dönüş sağlar. RPD assessment'ın varlığı özgün eklerinin erişilebilirliği değildir.

## 4. Arşiv, onarım ve tarihsel erişim

Korunmuş U001–U016 / S001–S015 kesimi **31 görünür mesaj / 16 dosya**, kümülatif adres sayısı 126'dır. S001–S013 önce yoğunlaştırılmış, sonra görünür özgün yanıtlardan tam aktarılmıştır. Eski görünümler ayrı tarihsel dizinde aynı Git kimlikleriyle korunur. Platform export'u veya bağımsız transkripsiyon doğrulaması yoktur. MS01 bu sayımı artırmaz.

| İhtiyaç | Yol |
|---|---|
| Kaynak kesimi | [Diyalog INDEX](sources/conversation/INDEX.md), [USER-MESSAGES](sources/conversation/USER-MESSAGES.md) |
| Kimlikler ve aktarım sınırı | [SOURCE-MANIFEST](SOURCE-MANIFEST.json), [TRANSCRIPTION-NOTE](checks/TRANSCRIPTION-NOTE.md), [ARCHIVE-COVERAGE](checks/ARCHIVE-COVERAGE.md) |
| İlk hata/onarım | [FIDELITY](checks/FIDELITY-20260921.md), [REPAIR](checks/REPAIR-20260921.md), [eski yoğunlaştırmalar](artifacts/condensed-before-repair/README.md) |
| Onarım yayını | [PUBLICATION](checks/PUBLICATION.md), [HISTORICAL-PUBLICATION](checks/HISTORICAL-PUBLICATION-PR29-30.md) |
| Eski kazanımlar | [LEARNINGS](reflections/LEARNINGS.md), [EVOLUTION](reflections/EVOLUTION.md), [TERMS](reflections/TERMS.md) |
| Önceki açıklar/kanıt sınırları | [QUALIFICATIONS](reflections/QUALIFICATIONS.md), [OPEN-QUESTIONS](reflections/OPEN-QUESTIONS.md); current açıklar MS01'de |
| Kaynak konularına erişim | [TOPIC-MAP](retrieval/TOPIC-MAP.md), [CUMULATIVE-READING](retrieval/CUMULATIVE-READING.md) |
| Önceki EXP ve araştırma kaynakları | [PREDECESSORS](sources/PREDECESSORS.md), [RESEARCH-REFERENCES](sources/RESEARCH-REFERENCES.md), [CITATION-KEY](sources/CITATION-KEY.md) |
| MS01 A snapshot | [A taslak](https://github.com/batuhanozgun/agentic-os-search/blob/a0f3ab5f450b28d908a5a89d15a626637e322bfe/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/artifacts/MS01-SOUL-WORKING-SYSTEM-DRAFT.md), [A kapsam/kaynak defteri](https://github.com/batuhanozgun/agentic-os-search/blob/a0f3ab5f450b28d908a5a89d15a626637e322bfe/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/artifacts/MS01-COVERAGE-AND-OPEN-MECHANISMS.md), [A STATE](https://github.com/batuhanozgun/agentic-os-search/blob/a0f3ab5f450b28d908a5a89d15a626637e322bfe/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/STATE.md) |
| MS01 öncesi uzun giriş | [RV01 INDEX](https://github.com/batuhanozgun/agentic-os-search/blob/0dd58080eeea4ee8c7eaaaef0902d02fce825edc/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/INDEX.md), [RV01 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/0dd58080eeea4ee8c7eaaaef0902d02fce825edc/explorations/EXP-004-genisleyen-soul-ve-buyuk-is-stress-testi/STATE.md) |

Tarihsel yönler mevcut yetki/iş yerine geçmez. Kontrol dosyaları yalnız AGENT.md ve agent/** içindedir; bu proje taslağı etkin agent-control değildir.

## 5. Yetki ve koruma

Checkpoint B yeni roman yürüyüşünü, mevcut ana taslak/kapsam dosyalarını ve STATE/INDEX'i günceller. Bankanın A yürüyüşü, önceki T/SC/SY/DQ/RV metinleri, kaynak/manifest/onarım, Foundation, studies, concepts, diğer EXP'ler ve target implementation korunur.

Kurgusal mikro-pasajlar tam roman; yapı taslağı çalışan runtime; self-review bağımsız doğrulama değildir. Gerçek ürün veya model/okur/öğrenci deneyi yapılmadı. Sonraki yetki kullanıcı değerlendirmesine göre belirlenir; daha çok kontrol veya daha çok araştırma kendiliğinden hedef haline getirilmez.
