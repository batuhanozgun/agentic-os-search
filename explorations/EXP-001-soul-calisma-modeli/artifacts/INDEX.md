# EXP-001 — Eser envanteri ve sürüm sınırları

**Remote payload durumu için [STATE](../STATE.md) ve [SOURCE-MANIFEST](../SOURCE-MANIFEST.json) birlikte okunur.** Bu dizinin varlığı veya aşağıdaki yolların yazılması, büyük dosyaların GitHub'a aktarılmış olduğu anlamına gelmez. Bu arşivleme turunda altı özgün dosya yerelde byte-eşit korunmuştur.

## Konsolidasyon v0.1

Hedef dizin: `consolidation-v0.1/`.

- `SOUL_Calisma_Anlayisi_Konsolidasyon_v0_1.md` — 87.606 byte.
- `SOUL_Calisma_Anlayisi_Konsolidasyon_v0_1.pdf` — 651.941 byte; 35 sayfa.

İçerik: 18 ana bölüm, Ek A değişen kabuller, Ek B özgün çizim, Ek C konu kapsamı ve Ek D kaynaklar. U001–U011 boyunca gelişen içerik U012 isteğiyle diyalogdan bütünlüklü metne çevrilmiştir. Platform transcript'i değildir. Yaşayan katmanlı planın Atlas sonrası tartışmasını içerdiği varsayılmaz.

İlgili kaynak teslim: [S012](../sources/conversation/assistant/S012.md).

## Mekanizma Atlası v0.1

Hedef dizin: `mechanism-atlas-v0.1/`.

- `SOUL_Mekanizma_Atlasi_v0_1.html` — 490.297 byte.
- `SOUL_Mekanizma_Atlasi_v0_1.pdf` — 1.332.083 byte; 51 sayfa.
- `SOUL_Mekanizma_Atlasi_v0_1_Kaynaklar.zip` — 756.782 byte; 26 ZIP üyesi.
- `source/` — ZIP içinden göreli yol ve byte eşitliğiyle çıkarılmış incelenebilir kaynaklar; canonical eserin yerine yeniden yazılmış sürüm değildir.

Ortak modelin içerik sayımları bu tur JSON'dan tekrar okundu: 22 işlem, 11 bilgi nesnesi, 8 overview grubu, toplam 41 node; 71 ilişki; 7 görünüm; 10 demo adımı; 12 açık mekanizma; 21 hayali dosya kaydı. Bunlar kapsam sayımıdır, çalışma etkinliği kanıtı değildir.

26 ZIP üyesi: README, DOGRULAMA.json, MANIFEST.sha256, HTML/PDF, app.js, build_atlas.py, template.html, style.css, model.json, render_and_test.py, dayanak/consolidation.md ve actor/change/execution/information/intake/overview/readiness için 7 DOT + 7 SVG.

İlgili kaynaklar: [U013–U015](../sources/conversation/USER-MESSAGES.md#u013), [S013](../sources/conversation/assistant/S013.md), [S014](../sources/conversation/assistant/S014.md), [S015](../sources/conversation/assistant/S015.md).

## Özgün çizim

Hedef: `sources/original-sketch.png`, 602.469 byte. U006'da C adayları, C4 ve Work adımları boyunca değişen C/W ilişkisi çizilmiştir. Yeniden çizim veya OCR ürünü değil, özgün PNG korunur. Metinsel bağlam: [U006](../sources/conversation/USER-MESSAGES.md#u006).

## Sonraki tartışmanın yeri

[U016–U017](../sources/conversation/USER-MESSAGES.md#u016) ve [S016](../sources/conversation/assistant/S016.md)/[S017](../sources/conversation/assistant/S017.md), Atlas v0.1'in yaşayan proje planı bakımından kısmi kaldığını tespit eder. Bu bilgi v0.1 dosyalarının içine sonradan eklenmemiştir. [LEARNINGS L13–L14](../reflections/LEARNINGS.md) ve [OPEN-QUESTIONS O01–O02](../reflections/OPEN-QUESTIONS.md) üzerinden bulunur.

## Özgünlük ve doğrulama

Hash'ler SOURCE-MANIFEST'tedir. PDF sayıları ve ZIP CRC bu tur tekrar kontrol edildi; eski DOGRULAMA.json'un 24 arayüz kontrolü bu tur tekrar koşuldu diye sunulmaz. Arşivleme, yeni SOUL runtime/agent doğrulaması değildir. Eksik remote payload tamamlama paketi gerçek orijinal byte'ları taşır; yeniden üretim yerine kopyalama tercih edilir.
