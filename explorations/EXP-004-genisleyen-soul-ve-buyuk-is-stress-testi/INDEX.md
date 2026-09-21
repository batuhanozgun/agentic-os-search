# EXP-004 — Genişleyen SOUL ve büyük-iş stress testi

Önce [STATE](STATE.md) okunur. **Güncel odak: DQ01 — işaret edilmemiş ihtiyacın keşfi ve yetkinliğin gerekçelendirilmesi.** [DQ01](continuations/DQ01-UNSIGNALED-NEED-DISCOVERY-AND-CAPABILITY-QUALIFICATION.md), tamamlanmış SY01'in açık sorusunu kavramsal olarak ilerletir; çalışma hipotezidir, yeni T16 koşusu veya kapasite kanıtı değildir. [SY01](artifacts/SY01-CROSS-SCENARIO-WORK-SYSTEM-SYNTHESIS.md), T1–T15'in ortak sorumluluklarını, alana özgü yöntemlerini ve açık kapasite/kanıt yüklerini Development OS, SOUL ve kullanıcı işiyle ilişkilendiren tamamlanmış ara sentezdir. Son kavramsal test [T15](continuations/T15-NOVEL-EDITORIAL-DISAGREEMENT-AND-CHOICE.md), okuma kapsamı [T14](continuations/T14-NOVEL-READING-COVERAGE-AND-JOINT-CONTEXT.md), anlamsal revizyon [T13](continuations/T13-NOVEL-SEMANTIC-REVISION-AND-IMPACT.md), ilk yazılabilir Work [T12](continuations/T12-NOVEL-FORMATION-AND-FIRST-WRITABLE-WORK.md), senaryo seçimi [SC02](continuations/SC02-NOVEL-SCENARIO-ASSESSMENT.md)'de korunur. Bilinen kaynak onarımı main'de kapalı; [PUBLICATION](checks/PUBLICATION.md) o tarihsel onarımın yayın kaydıdır.

## Kaynak, özet ve tarih

[Kaynak diyalog](sources/conversation/INDEX.md): U001–U016/S001–S015, **31 görünür mesajlık korunmuş kesim**. S001–S013 özgün görünür yanıtlardan kısaltılmadan aktarılmıştır. Eski yoğunlaştırmalar [ayrı tarihsel dizinde](artifacts/condensed-before-repair/README.md) aynı Git kimlikleriyle durur. S014 önceki yanlış tamlık bildirimini, S015 açıklamasını taşır. [Aktarım sınırı](checks/TRANSCRIPTION-NOTE.md), [manifest](SOURCE-MANIFEST.json), [onarım](checks/REPAIR-20260921.md) farklı güvence türleridir.

[T1–T7 konsolidasyonu](artifacts/CONSOLIDATION.md) tarihsel türevdir. [T08](continuations/T08-FEEDBACK-AND-CONTROLLED-ADAPTATION.md) ile [tam S015](sources/conversation/assistant/S015.md) aynı belge değildir. U016 [kaynak mesaj](sources/conversation/USER-MESSAGES.md#u016) ve [çerçeve notu](reflections/FRAME-CLARIFICATION-20260921.md) ile bulunur. T09–T15, SC02, SY01 ve DQ01 notları kaynak arşivi sayısını artırmaz; assistant tam konuşma aktarımı diye okunmaz. SC02 kullanıcı mesajını ayrı alıntı olarak korur. SY01, eski CONSOLIDATION'ın yerine kaynak olarak geçirilmez; yeni tarihli ara yorumdur. DQ01 de SY01'i veya özgün test kaynaklarını yeniden yazmaz.

## Amaç ve modelin evrimi

Başlangıçtaki agent/rol/iş/plan/memory çerçevesi, Foundation ve studies'le iş keşfi, hazırlık, gerçek etki, doğrulama, kabul, süreklilik, değişim ve ilerleme sorularına açıldı. Work/Actors/Information/Environment ve Composition ayrımları düşünme zeminidir; final ontoloji veya yazılım modül listesi değildir.

SOUL'un oluşturduğu düzenden zorunlu olarak kopmadığı; yeni yeteneklerle mevcut işlevlerin kapsamının da değişebileceği hipotezi gelişti. U016'nın dikey/yatay, iki dosya ve klasör ifadeleri örnektir; branch çağrışımı araç seçimi değildir. Sadeleştirme/geri alma bunlarla yasaklanmış sayılmaz.

Soru-bankası vakası bir yıllık büyük programdır. T11'in küçük teslimat dilimi bu büyük hedefin yerine geçmez. Gerçek ülke, müfredat, eğitimsel etkinlik veya mevzuat araştırması yapılmadı. Bir vakayı mevcut kategorilerle anlatmak Foundation/implementasyon yeterliliğini doğrulamaz.

## Son devamlar

[T09](continuations/T09-CONCURRENT-CHANGE-AND-SHARED-CONSTRAINTS.md): yerel kararların ortak uygunluğu, kaynak taahhüdü ve güvenli geçiş.

[T10](continuations/T10-EXTENSION-ADMISSION-AND-CONTROL-COVERAGE.md): yeni aktör/araç/yolun mevcut yükümlülükler altında fiilen kapsanması; yetenek ile etkiye kabul; gerekli, uygulanan ve gözlenmiş kapsam.

[T11](continuations/T11-EVIDENCE-SUFFICIENCY-AND-BOUNDED-PROGRESS.md): açık soruların otomatik blocker olmaması; karar/kullanım için yeterli kanıt; zorunlu şartı gevşetmeden, önceden izinli ve kendi başına yararlı dilimi ilerletme; ek araştırmanın katkısı ve maliyeti; kaynak sınırı ile doğruluk/kabulü ayırma; sınırlı kapanış ve yeniden açma.

Bunlar kurulu karşıörnekler ve mekanizma ihtiyaçlarıdır, gerçek SOUL davranış güvencesi değildir.

## İkinci senaryo: neden roman, hangi sınırlarla?

Kullanıcı yazılım dışı ve bütünsel akıl yürütme gerektiren roman adayını sundu; yalnız kullanıcı önerdi diye kabul edilmemesini istedi. [SC02](continuations/SC02-NOVEL-SCENARIO-ASSESSMENT.md), romanı araştırma kitabı ve müze sergisiyle karşılaştırarak öncelikli aday olarak önerir. Roman uzun metin belleğinden öte, bölümlerin bütünsel etkisi, bakış açısına göre bilgi, amaçlı belirsizlik, yaratıcı keşif, geriye etkili yeniden yazım ve editoryal/okur değerlendirmesiyle önceki modele farklı baskı uygulayabilir.

Tek çağrıya sığmama evrensel model sınırı sayılmadı; sınırlı çalışma bağlamı ileride deney koşulu olabilir. Hazırlık bütün romanı önceden dondurmak değildir. Her bölüme ayrı ajan, tek evrensel yazar akışı, kesin kelime sayısı veya fiziksel veri yapısı seçilmedi. Romanın metin-odaklı sınırı korunur; fiziksel işletim ve bağımsız dış aktörleri kapsayan başka bir vaka ileride gerekebilir.

## Roman senaryosunda T12–T15

[T12](continuations/T12-NOVEL-FORMATION-AND-FIRST-WRITABLE-WORK.md): creative/story state, plan ve manuscript ayrılır; exploratory draft final manuscript veya canon değildir. Provisional, committed, rejected/superseded, deliberately unresolved, character-belief ve reader-exposure statülerinin karışması creative drift üretebilir. İlk yazılabilir Work bir exploratory scene/probe olabilir; her zaman Chapter 1 değildir. Context gerektiğinde asıl prose'u geri getirir.

[T13](continuations/T13-NOVEL-SEMANTIC-REVISION-AND-IMPACT.md): değişiklik etkisi kelime/dosya listesi değil, parçaların dayanağı ve birlikte ürettikleri anlamla ilgilidir. Derya'nın susmasının A/B gerekçeleri karşılaştırılır; B daha iyi sayılmaz. Aynı davranış korunabilir, açık olay bildirimi çelişebilir, hiç yazılmamış gerekçe yeni Work gerektirebilir. Doğru açıklama çok erken verilirse tutarlılık artarken amaçlanan etki bozulabilir. İçeriğin aynı kalması eski editoryal hükmün aynı bağlamda geçerli olduğunu göstermez.

[T14](continuations/T14-NOVEL-READING-COVERAGE-AND-JOINT-CONTEXT.md): aynı kaba özet, Derya'nın mektubu gördüğü/görmediği farkı kaybedebilir. Bölüm kapsaması ilişki değerlendirmesi değildir. Kaynak/sürüm, anlatı boyunca okuma, açık sorular ve gerektiğinde ilişkili asıl pasajların birlikte görülmesi korunur. Uygun özet kullanılabilir; her tur tam okuma veya zorunlu graph/üst-ajan önerilmez. Okura açılan metin gerçek okur bilgisi değildir; okuma izi anlama kanıtı değildir.

[T15](continuations/T15-NOVEL-EDITORIAL-DISAGREEMENT-AND-CHOICE.md): aynı kaynağı gören eleştiriler farklı yaratıcı öncelikler taşıyabilir. Tespit ile önerilen çözüm, kanıt ile tercih, değerlendirme ile yetkili karar ayrı. Çoğunluk/tek puan/uzlaşma otomatik üstünlük üretmez. Koşullu küçük revizyon yönü, seçilmeyen görüşün geçerli kaygısını korur; kararın dayanağı ve yeniden açma koşulu salınımı sınırlayabilir. Gerçek karşı kanıt kapanış nedeniyle susturulmaz.

Mikro-parçalar gerçek uzun romanın tamamını veya okur tepkisini temsil etmez. Her yeni fikir otomatik canon, her değişiklik tümünü-yeniden-yazma gereği, her çelişkisizlik edebî başarı değildir.

## SY01 — Ortak sorumluluk, farklı yöntem ve açık kapasite

[SY01](artifacts/SY01-CROSS-SCENARIO-WORK-SYSTEM-SYNTHESIS.md), sekiz geçici sorumluluk grubu ile iki senaryoyu ilişkilendirir. İşin takibi işin konusunu anlamak değildir; role/record/control düzeni alan yetkinliğini kendiliğinden sağlamaz. İhtiyaç, temsil, mekanizma adayı, gerçek kapasite ve gösterilmiş sonuç ayrıdır.

Kullanıcı işindeki sonuç → SOUL'un gerekeni fark edip karşılama kapasitesi → Development OS'un bunu geliştirme/doğrulama sorumluluğu ilişkisi kurulur; üç yazılım katmanı veya otomatik başarı aktarımı değildir. Ortak yükümlülükler farklı alanlarda farklı yöntemlerle karşılanabilir.

Work-first zorunlu zaman sırası değildir; koşullu frontier gerçek aktör/bilgi/ortam/yetkiyle değerlendirilir. Plan gerçek yürütme değildir ama ilgili kabul ve bağlar üzerinden denetim etkisi taşıyabilir. Her keşif meta-work değildir; faaliyet hangi nesneyi değiştirdiğine göre ele alınır. Yeni yorumlar eski kaynakları yeniden yazmaz.

## DQ01 — Bilinmeyen soru, eksiklik teşhisi ve kapasite kabulü

[DQ01](continuations/DQ01-UNSIGNALED-NEED-DISCOVERY-AND-CAPABILITY-QUALIFICATION.md) eksik cevabı bilmeden araştırılacak soruyu fark etmeyi, ihtiyacı karşılayabilme iddiasından ayırır. Kullanıcı tarafından söylenmemiş olanın kaynakta da bulunmadığı varsayılmaz. Amaç/kullanım ile yapılacak iş/çıktı arasındaki dayanak sorgulanır; yeni adayın hedefin gereği mi, seçilmiş yöntemin bağımlılığı mı, yaratıcı tercih mi olduğu ayrıca incelenir.

Eksik bilgi, yanlış/eski görünüm, bilgiyi kullanamama, yöntem/ölçüt kusuru, alan yeterliği ve ortam/yetki sorunları aynı teşhis değildir. Yeni rol veya araç adı yeterlik yaratmaz. Denemeye değer aday, belirli kullanım için desteklenen kapasite ve somut çıktı/etki kabulü ayrı kalır.

Gereksinim listesiyle değerlendirmenin aynı körlüğü paylaşması, çok sayıda başarılı kontrolü yanıltabilir. Bilinen T14 kusurunu yeniden açıklamak işaretlenmemiş keşif kanıtı değildir. Uygun ve hatalı durumları ayırma, belirsizliği koruma, gereksiz iş üretmeme ve yararlı ilerleme yükleri birlikte düşünülür. DQ01 bir çalışma hipotezidir; canlı test, mimari veya yeni T16 değildir. RPD özgün ek erişim sınırı ve dar NASA HTML reuse'u notun kaynak bölümünde kayıtlıdır.

## Nereden devam edilir?

STATE → DQ01 → SY01 → sorunun gerektirdiği T1–T15 kaynağı. Yeni oturumda bu üç kavramsal giriş (STATE/INDEX, DQ01 ve SY01) tam okunur; karar-kritik ayrımda ilgili asıl kaynağa dönülür. Son roman testi T15'tir. İhtiyaç/aktör ayrımlarının özgün kaynakları S008/S009, yeterlilik/kapanış T11, kapsama T10, ortak değişim T09, yöntem uyarlaması S015/T08 ve örnek sınırları U016'dadır. Özet kaynak yerine geçmez; RPD assessment'ın bulunması özgün eklerinin de erişilebilir olduğu anlamına gelmez.

T1–T15 ve SY01 tamamlanmıştır; DQ01 onların açık kapasite sorusunu kavramsal olarak ilerletir. Sonraki mantıklı dar soru, alan yeterliği henüz belirsizken keşif/değerlendirme yaklaşımını seçmek ve ortak körlüğünü makul maliyet altında sınamaktır. Bu yeni mekanizma karşılaştırması veya deney olarak başlatılmadı; sonraki yetkili iş güncel kullanıcı yönü ve kapsamıyla belirlenir.

## Okuma yolları

| İhtiyaç | Yol |
|---|---|
| Güncel durum/yetki | [STATE](STATE.md) |
| İşaret edilmemiş ihtiyaç, eksiklik teşhisi ve kullanım-bağlı yetkinlik desteği | [DQ01](continuations/DQ01-UNSIGNALED-NEED-DISCOVERY-AND-CAPABILITY-QUALIFICATION.md) |
| İki senaryonun ara sentezi: sorumluluk/kapasite/kanıt ve üç düzey | [SY01](artifacts/SY01-CROSS-SCENARIO-WORK-SYSTEM-SYNTHESIS.md) |
| İhtiyaç ve aktör yeterliğinin özgün konuşma dayanakları | [S008 / T2](sources/conversation/assistant/S008.md), [S009 / T3](sources/conversation/assistant/S009.md) |
| Editoryal görüş ayrılığı: tespit, tercih, yetki ve kapanış | [T15](continuations/T15-NOVEL-EDITORIAL-DISAGREEMENT-AND-CHOICE.md) |
| Uzun eseri okuma: bölüm/ilişki kapsaması, özet ve ortak bağlam | [T14](continuations/T14-NOVEL-READING-COVERAGE-AND-JOINT-CONTEXT.md) |
| Büyük yaratıcı değişiklik: anlamsal etki, koruma ve revizyon | [T13](continuations/T13-NOVEL-SEMANTIC-REVISION-AND-IMPACT.md) |
| Roman: ilk yazılabilir Work, canon/provisional/draft ayrımları | [T12](continuations/T12-NOVEL-FORMATION-AND-FIRST-WRITABLE-WORK.md) |
| İkinci senaryo seçimi: roman, alternatifler ve sınırlar | [SC02](continuations/SC02-NOVEL-SCENARIO-ASSESSMENT.md) |
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

Run / Execution Attempt, Qualification Case ve Re-entry Context aday ayrımlardır, zorunlu service/schema değildir. Metareasoning/RPD, Re3/DOC, counterfactual rewriting, FABLES, NoLiMa ve LLM-judge referansları algoritma benimsemesi veya bugünkü model performansı iddiası değildir. Mesleki editörlük rehberi evrensel estetik oracle değildir. SY01 ve DQ01 de zorunlu modül, tek ekip veya uygulanmış sistem tarifi değildir. NASA referansları SOUL/roman yeterliğini doğrulamaz. Kaynak arşivi/manifest, önceki eserler (T1–T15, SC02, SY01 dahil), onarım kanıtı, Foundation, studies, concepts, agent-control, önceki EXP ve target implementation bu devamda değiştirilmez.
