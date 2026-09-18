# Kavram Çalışması — Tek Çalışma Taslağı

**Durum:** GELİŞEN ÇALIŞMA REFERANSI; kaynaklara dayanan yerel tercihler ve henüz yeniden incelenmemiş taslaklar birlikte, aşağıda ayrılarak tutulur. Kullanıcının her maddeyi tek tek benimsediği veya evrensel tanımlar seçildiği iddia edilmez. SOUL mimarisi değildir.

Önceki [v0.4 kaydının](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/synthesis/CORE-TERMS-WORKING-v0.4.md) 40 numaralı maddesi ve Task alt kullanımı sadeleştirmede buraya taşındı. 2026-09-18 devam incelemesinde Agent–Model–yapılandırma–Actor/Role–Identity–Run/Session–Context ilişkileri, model değiştirme ve oturumda devam örnekleri üzerinden düzeltildi. Tool ve Runtime ifadeleri de bu ilişkideki çağrı/yürütme farkını koruyacak şekilde güncellendi. Sonraki aynı tarihli inceleme, tamamlanma–doğrulama–yayımlama yetkisini bu kümeye bağladı. Diğer maddeler aynı olgunlukta sayılmaz.

Güncel iş [STATE](STATE.md), yöntem [METHOD](METHOD.md), dayanak ve gerçek okuma kapsamı [SOURCES](SOURCES.md)'taki tarihli bölümlerdedir. Bu dosya yerinde güncellenir; her tur yeni sürüm veya terim paketi açılmaz.

## Kullanım kapsamı ve açık sınırlar

- Aşağıdaki Agent kullanımı model tabanlı yazılım agent'ları içindir. Klasik AI'daki daha geniş kullanımları veya bir SDK'nın `Agent` sınıfını yanlış ilan etmez. Bir API sınıf adından davranış güvencesi çıkarılmaz.
- Agent'ın adımlarını modelle seçebilmesi, her çalıştırmada araç çağırması ya da uzun bir döngü yürütmesi gerektiği anlamına gelmez. Yalnız sınıflandırma çıktısı veren model çağrısını burada otomatik Agent saymıyoruz; çevresindeki yürütme kontrolüne ayrıca bakıyoruz. Evrensel bir agency eşiği kapatılmadı.
- Aynı kimlik, aynı yapılandırma, aynı model ve aynı geçmiş farklı iddialardır. Hiçbiri tek başına diğerlerini ya da davranış eşdeğerliğini kanıtlamaz.
- Context'te bulunma ile kodun/veri deposunun erişebildiği bilgi aynı değildir. Model/ürün/sağlayıcı ayrımı aşağıda yalnız bu örnekler için açıklanır; ürün kataloğu veya model performansı kıyası yapılmadı.
- Work birçok eski açıklamada kullanılıyor fakat burada ayrı bir çalışma tanımı yok. Bu turdaki kullanımı gündelik anlamıyla yürütülen iştir; Foundation anlamı veya veri modeli seçilmez.
- Model/oturum ve tamamlanma/yayım incelemeleri, önceki bütün kaynak iddialarını doğrulamaz. Bir işin tamamlanması, bir sonucun doğrulanması ve o sonuçla eylem yapma yetkisi ayrı sorulardır; zorunlu olarak ayrı kişiler veya ardışık aşamalar değildir. Diğer taslaklar ihtiyaç oldukça ele alınır.

## Çalışma tanımları

### Yürütme, aktör ve bilgi ilişkileri

1. **Agent** — Bir işi verilen amaç ve sınırlar içinde yürütmek üzere yapılandırılmış; aldığı bilgi ve sonuçlara göre işin sonraki adımını model kullanarak seçebilen yazılım birimi. Buradaki vurgu yalnız cevap üretmek değil, işi nasıl sürdüreceğine ilişkin model destekli yürütme kontrolüdür. Agent'ın tanımı, belirli kimlikle izlenen kullanımı ve tek çalıştırılması gerektiğinde ayrıca nitelenir.
2. **Model** — Eğitimle edinilmiş parametreler taşıyan, kullanıldığında girdilerden çıktılar üreten öğrenilmiş hesaplama bileşeni. Model adı, onu çağıran SDK nesnesi, erişim hizmeti veya kullanıcıya sunulan ürün aynı nesne değildir.
3. **LLM** — Dil anlama ve üretme görevleri için büyük ölçekli eğitilmiş Model türü. Model daha geniş sözcüktür; bu tur çok kipli modellerin sınıflandırmasını kapatmaz.
4. **Actor** — Belirli bir iş bağlamında katkı veya sorumluluk üstlenen katılımcı. Bir insan veya Agent bu bağlamda Actor olabilir; bu, Agent ile Actor sözcüklerini eşanlamlı yapmaz.
5. **Role** — Bir iş bağlamında katılımcıdan beklenen işlev ve sorumluluk. Aynı rolü farklı aktörler üstlenebilir; aynı rolü taşımak aynı kimliğe sahip olmak değildir.
6. **Run** — Bir agent veya akış için başlatılmış, kendi başlangıcı, yürütme durumu ve sona erme sınırı olan mantıksal çalışma girişimi. Geçici duraklama veya bir API çağrısının dönmesi zorunlu olarak Run'ın bittiği anlamına gelmez. Devamın aynı mantıksal Run mı yeni Run mı sayıldığı ilgili yürütme sözleşmesiyle belirtilir; tek Run birden fazla model çağrısı veya Agent içerebilir.
7. **Session** — İlişkili etkileşimlerin ve bunlara ait geçmiş/durumun belirli kapsam ve kimlik altında ilişkilendirildiği oturum. Birden fazla Run içerebilir; tanımı gereği tek Agent'a, tek işletim sistemi sürecine veya kalıcı depolamaya eşit değildir.
8. **Workflow** — Work'ü gerçekleştirmek için adım/koşul/Actor/Agent/Tool koordinasyon yapısı.
9. **Tool** — Bilgi edinme, hesaplama veya ortamda işlem yapma işlevini çağrılabilir biçimde sunan arayüz. Modelin araç çağrısı istemesi ile işlemin Runtime veya hizmet tarafından gerçekten yürütülmesi ayrı adımlardır.
10. **Harness** — Model/Agent'ı güvenilir/sınırlı/devam ettirilebilir Work'e çeviren model-dışı operating/control substrate.
11. **Runtime** — Agent ve akışları fiilen yürüten yazılım düzeni; model çağrıları, araç yürütme ve çalışma yaşam döngüsünü işler. Agent tanımı veya tek Run değildir; süreç değişimi ile mantıksal çalışma değişimi otomatik eşitlenmez.
12. **Context** — Bu çalışma kapsamında, belirli model çağrısına sunulan talimatlar ve çalışma bilgisi. Uygulama kodundaki bağımlılık/durum nesnesi gerektiğinde local/runtime context diye nitelenir; otomatik olarak modelin gördüğü bilgi sayılmaz.
13. **Memory** — gelecekteki Run/kararları etkileyebilmek için yaşam döngüsü yönetilen cross-time knowledge/state.
14. **Identity** — Belirli kapsamda hangi varlık veya kayıtla çalışıldığını ayırt eden kimliklendirme. Zamanlar arasında aynı varlık sayılması, o kapsamda kimliğin nasıl korunduğuna dayanır; aynı ad, rol, model veya prompt tek başına yeterli değildir. Kimlik, geçmişe erişim ya da yetki garantisi vermez.
15. **Capability** — Bir aktörün veya sistemin belirli koşullarda fiilen gerçekleştirebildiği işlev/eylem kapasitesi. Araç, model ve ortam bu kapasiteyi etkiler; teknik olarak yapabilmek, o işlem için yetkilendirilmiş olmak değildir.
16. **Authority** — Bir aktörün belirli iş ve kapsamda hangi kararları alıp eylemleri gerçekleştirmek üzere yetkilendirildiği. İşe atanma veya inceleme rolü tek başına yayımlama yetkisi vermez. Burada iş düzeyindeki yetkiyi anlatır; evrensel bir yetki hiyerarşisi değildir.
17. **Permission** — Belirli aktör, işlem, kaynak ve koşullar için tanınmış somut izin. Bir hesap veya araçtaki erişim hakkı, o erişimle yapılabilecek her işin kullanıcı tarafından yetkilendirildiğini göstermez. İznin varlığı ve teknik olarak uygulanması ayrıca ayrılır.
18. **Orchestration** — execution sırasında kim/ne zaman/hangi sırada çalışacak ve next step nasıl seçilecek kontrol mantığı.
19. **Handoff** — active responsibility/execution control'ünün bir Agent'tan diğerine devri.
20. **Subagent** — daha geniş Work içinde başka Agent/Orchestrator'a göre alt sorumluluk taşıyan Agent.

### Durum, ortam ve kontrol — seçili maddeler güncellendi; diğerleri devralınan taslak

21. **State** — entity/process/system'in belirli anda continuation/decision/control açısından anlam taşıyan current condition representation'ı.
22. **Work state** — Bir işin kapsamını, mevcut ilerleyişini, ilgili çıktı/sürümleri, açık işleri, sorumlulukları ve karar/kanıt durumunu devam için temsil eden bilgi. Tamamlanma beyanı, doğrulama sonucu ve yayımlama izni burada ayrı tutulabilir; kayda geçirilmiş olmak güncel veya doğru olmakla aynı değildir.
23. **Environment** — Work'ün gerçekleştiği dış koşullar ve erişilebilir kaynaklar bütünü.
24. **Workspace** — Work materyallerinin/files/repos/artefacts/outputs düzenlendiği alan.
25. **Sandbox** — execution erişimini files/processes/network/credentials/resources açısından sınırlayan controlled boundary.
26. **Policy** — expected/allowed/forbidden/conditional davranışları tarif eden rules/principles.
27. **Guardrail** — execution event'ini Policy/criteria/risk açısından check edip block/reject/transform/escalate edebilen aktif kontrol.
28. **Verification** — Belirli çıktı, sürüm, iddia veya işlemin tanımlı gereklilikleri karşılayıp karşılamadığını kanıtla sınama. Olumlu sonuç yalnız incelenen kapsamı destekler; bağımsızlık, ölçüt ve kanıtın uygunluğu ayrıca önemlidir. Tek başına eylem yetkisi vermez.
29. **Observability** — System/Run/Workflow'un fiilen ne yaptığı hakkında yeterli traces/logs/events/state visibility'si.
30. **Persistence** — State/Memory/Work state/artefact/identity-linked bilginin Run/process/session/runtime sınırı sonrasında da korunabilmesi.

### Amaç, iş ve değerlendirme — seçili maddeler güncellendi; diğerleri devralınan taslak

31. **Intent** — user/owner isteğinin arkasındaki asıl yön, amaçlanan anlam ve neden; henüz operational Goal olmayabilir.
32. **Goal** — Work'ün yöneldiği açık target state/outcome/success condition.
33. **Plan** — Goal'e ulaşmak için önerilen ve revize edilebilir decomposition/approach/sequence/dependency/actor/control representation.
34. **Work item** — daha geniş Work içinde ayrı identity/scope/standing ile track/assign/depend/verify/close/reopen edilebilen yönetilebilir Work birimi.
    - **Task** — genellikle action-like Work item; source-local semantics varsa korunur.
35. **Dependency** — bir Work/artefact/action'ın start/validity/timing/closure/outcome'ının başka bir condition/state/output'a bağlı olduğu ilişki.
36. **Readiness** — Belirli bir sonraki hareket için gerekli koşulların karşılanma durumu. “İncelemeye hazır” ile “yayımlamaya hazır” aynı değildir; ilgili hareketin bilgi, kalite, yetki ve ortam koşullarıyla değerlendirilir. Genel bir başarı veya izin etiketi değildir.
37. **Completion** — Belirli iş kapsamının kararlaştırılmış tamamlama koşullarının karşılandığı durum. “Tamamladım” beyanı ve sistemdeki kapalı statüsü bu duruma ilişkin kayıt/iddiadır; tek başına yeterli kanıt değildir. Doğrulama veya teslim, kapsam gerektiriyorsa tamamlanmanın koşulu olabilir. İptal ya da Run bitişi kendiliğinden başarılı tamamlanma değildir.
38. **Validation** — Sonucun amaçlanan kullanım ve gerçek ihtiyacı karşılayıp karşılamadığını sınama. Belirli teknik gereklilikleri sağlamak bu soruyu otomatik kapatmaz; aynı kontrol iki soruya da dayanak olabilir. Kaynakların bütün validation kullanımları bu yerel kapsama indirgenmez.
39. **Evaluation** — Model/Agent/System/result/process'i criteria/tasks/rubric/metric/benchmark altında sistematik ölçüp performance/quality/capability/risk judgment üretme.
40. **Evidence** — Belirli iddia veya kararı desteklemek, zayıflatmak ya da sınırlandırmak için kullanılan izlenebilir gözlem, kayıt, çıktı veya kontrol sonucu. Hangi nesne/sürüme ve koşula ait olduğu önemlidir; aynı agent kimliğiyle devam edilmesi eski kanıtı yeni çıktıya otomatik taşımaz.

<a id="model-degisimi-ve-devam"></a>
## Model değişimi ve oturumda devam — 2026-09-18

**Statü:** Kaynak belgelerindeki sözleşmelerle karşılaştırılmış yerel kullanım incelemesi. Aşağıdaki durumlar açıklayıcı örneklerdir; canlı ürün çalıştırması veya bağımsız kullanıcı-anlama deneyi değildir. Kaynak anahtarları SOURCES'teki aynı tarihli bölümdedir.

### Neyi aynı tuttuğumuzu söylemek

“Aynı agent” tek başına bütün benzerlikleri kapsamaz. İlgili cümlede gerektiği kadar şu ayrımları kullanıyoruz:

| Söylediğimiz şey | Kastettiğimiz kapsam | Kendiliğinden çıkmayan sonuç |
|---|---|---|
| Aynı agent tanımı/yapılandırması | Yeniden kullanılabilen çalışma tarifi ve ayarları. | Aynı canlı örnek, geçmiş veya sonuç. |
| Aynı kimlikle devam eden agent | İş bağlamında aynı mantıksal katılımcı olarak izlenen varlık. | Yapılandırmasının/modelinin değişmediği. |
| Aynı rol | Aynı katkı veya sorumluluk beklentisi. | Aynı kişi/Agent olduğu. |
| Aynı Session | Aynı kapsamda ilişkilendirilmiş etkileşim ve geçmiş. | Tek Agent veya tek Run olduğu. |
| Aynı Run | Aynı mantıksal yürütme girişimi, yaşam döngüsü korunuyorsa. | Aynı süreçte veya tek API çağrısında yürüdüğü. |

Bunlar yeni zorunlu nesne sınıfları değil, mevcut sözcükleri açık kullanma nitelemeleridir. Belirli bir üründeki `agent_id`, tanım adı ve oturum kimliği, kendi sözleşmesinden okunur; evrensel kimlik şeması varsayılmaz.

### Örnek A — “Agent'ın modelini değiştirelim”

Varsayımsal Kaynak İnceleyici, bir işte inceleme rolünü üstleniyor. “Sonraki çalışmada model B'yi kullansın; inceleme sorumluluğu ve erişim sınırı aynı kalsın” diyoruz.

**Yerel yorum:** Değiştirilen şey model seçimidir. Bunu aynı katılımcının güncellenmiş çalışma düzeni olarak izleyebiliriz; aynı model, aynı tam yapılandırma veya aynı davranış iddiası kurmuyoruz. Varsayılan tanımdaki model alanı değişirse yapılandırma değişmiştir. Yalnız o çalıştırma için seçim değişirse kalıcı tanım değişmeden etkin ayarlar değişebilir. OA-Run bu son ayrımın somut belge örneğidir.

**Karşı örnek:** Aynı tanımı iki ayrı iş için kopyalayalım; ikisine de inceleyici rolü verelim, fakat ayrı kimlikler ve geçmişler kullanalım. Aynı model, prompt ve rol bunları tek katılımcı yapmaz. Tersine, aynı kimliği koruma kararı alınmış bir katılımcıda model değişmesi de onu zorunlu olarak başka katılımcı yapmaz. Bu kimlik devamı yerel izleme tercihidir, model ayarının otomatik yan etkisi değildir.

**Teknik sınır:** “Model değiştirilebilir” ile “her model sorunsuz ikame edilebilir” aynı iddia değildir. Girdi biçimi, araçlar ve durum aktarımı uyumluluğu ayrıca gerekir; bu tur performans/eşdeğerlik testi yoktur. Kaynak: OA-Model.

**Adlandırma:** Model ailesi bir model grubunu, model kimliği/API seçim değeri çağrıda istenen seçimi, sağlayıcı erişimin sunulduğu hizmeti, ürün ise kullanıcıya sunulan uygulamayı anlatabilir. Bunlar aynı şey değildir. CC-Models'ta `opus` gibi takma adların çözümlemesi ile Claude Code ürün yüzeyi ayrı görülür. Sabit adın aynı model sürümüne sonsuza kadar işaret ettiği varsayılmaz. Önceki örnek ürün adları bu incelemeyle topluca doğrulanmış değildir.

“Hazır” veya “özelleştirilmiş” de burada teknik bir Agent türü değil, hangi çalışma tarifinin kimden geldiğine ve hangi kısmın uyarlandığına ilişkin nitelemedir. CC-Agents'taki dosya tabanlı özelleştirme, yeni model eğitmenin zorunlu olmadığını gösteren bir örnektir; bütün hazır-agent ürünlerinin sözleşmesini temsil etmez.

### Örnek B — “Aynı agent yeni oturumda devam etsin”

Bu cümlede üç farklı devamı ayırıyoruz:

| Durum | Daha açık ifade | Yerel sonuç |
|---|---|---|
| Önceki konuşma/oturum kaydı yeniden açılıyor. | Önceki Session'ın ilgili geçmişiyle yeni etkileşime devam et. | Uygulamanın yeniden açılması, mantıksal Session'ın yeni olması demek değildir. |
| Gerçekten yeni Session açılıyor, önceki iş bilgisi aktarılıyor. | Yeni Session'da, önceki işin geçerli durumunu ve gerekli geçmişini devralarak devam et. | Aynı işin sürmesi için aynı Session gerekmeyebilir; aktarımın yeterliliği ayrı incelenir. |
| Yarım yürütme kayıtlı durumdan sürdürülüyor. | Askıdaki Run'ı kendi yürütme sözleşmesine göre sürdür. | Bu, yalnız eski mesajları okutmakla eşit değildir. |

**Karşı örnek 1:** Aynı Agent tanımını ve aynı modeli kullanıp boş Session başlatmak, önceki işi hatırladığını göstermez. OA-Session, aynı tanımın farklı oturumlarla kullanımını belgeleyen örnektir.

**Karşı örnek 2:** İki ayrı Agent aynı Session geçmişini kullanabilir; ortak geçmiş onları tek kimlik yapmaz. OA-Session'daki paylaşım örneği, Session=Agent eşlemesini çürütür.

**Karşı örnek 3:** Önceki taslak Run'ı herhangi bir durma noktasında bitiyormuş gibi açıklıyordu. OA-Resume'da askıya alınmış yürütme kayıtlı durumla sürdürülebiliyor. Buna karşılık CC-Agents, bazı devamları aynı agent kimliği altında yeni Run olarak tarif ediyor. Yerel Run tanımı bu nedenle tek API çağrısı veya işlem ömrüne bağlanmadı; dış sözleşmeler zorla eşitlenmedi.

**Bilgi sınırı:** Saklanan veya kodun erişebildiği her şey modelin o anda gördüğü Context değildir. Devam için gereken bilgi çağrıya gerçekten taşınmalıdır. Ayrıca kayıtlı geçmiş, dış dünyadaki son durumu veya geçmiş iznin bugün geçerli olduğunu tek başına ispatlamaz. İlk cümle OA-Context'e dayanır; ikinci cümle bu örnekteki güvenli yorum sınırımızdır, yeni bir yetki sistemi tasarımı değildir.

**Daha açık birleşik cümlemiz:** “İnceleyici rolünü üstlenen aynı katılımcıyı koruyalım; sonraki çalıştırmada model B'yi kullansın. Yeni Session'a önceki işin geçerli durumunu ve gerekli geçmişini taşıyalım. Önceki Run'ı sürdürdüğümüzü ancak yürütme kaydı bunu gösteriyorsa söyleyelim.”

### Bu kümenin ilişki haritası

```text
Agent tanımı/yapılandırması — tarif eder → Agent'ın çalışma düzeni
Agent — kullanır → Model
LLM — bir türüdür → Model
Agent — belirli bir işte katılımcı olabilir → Actor
Actor — üstlenir → Role
Identity — kapsam içinde ayırt eder → Agent / Actor / ilgili kayıt

Runtime — yürütür → Run
Run — çalışmasına dahil edebilir → bir veya birden fazla Agent
Session — ilişkilendirir → etkileşimler / geçmiş / birden fazla Run

Session'dan seçilen geçmiş + geçerli talimatlar + gerekli iş bilgisi
    — çağrıya sunulduğunda oluşturur → Context

Aynı tanım ≠ zorunlu olarak aynı kimlik
Aynı kimlik ≠ zorunlu olarak aynı model veya davranış
Aynı geçmiş ≠ zorunlu olarak aynı Agent
Yeni süreç ≠ zorunlu olarak yeni mantıksal Run veya Session
```

Bu dört ayrım tablodaki örneklerin kısa sonucudur; tek başlarına test kanıtı değildir. Harita bir veri modeli veya zorunlu bileşen mimarisi seçmez.

### Bu incelemede kapanan ve açık kalan sınır

Model seçimi, yapılandırma, kimlik, rol, Run ve Session'ı iki başlangıç cümlesinde ayrı söyleyebilecek yerel zemini oluşturduk. Bütün ürünler için kimlik/migrasyon protokolü, her modelin ikame edilebilirliği, uzun işin devam bilgilerinin tam şeması ve tüm agency literatürü kapanmadı. Bir sonraki gerçek kullanım bunları gerektirirse yalnız gereken kısmı açılır; bu sorular otomatik araştırma kuyruğu değildir.

<a id="tamamlanma-ve-yayim"></a>
## Tamamlanma, doğrulama ve yayımlama — 2026-09-18

**Soru:** “İşi bitirdi; sonucu yayımlayabilir” cümlesi hangi durumları tek bir sonuç gibi gösteriyor? **Statü:** Belge karşılaştırması ve açıklayıcı örnek incelemesi; canlı ürün/güvenlik veya bağımsız iletişim deneyi değil. Kaynak anahtarları [SOURCES](SOURCES.md#tamamlanma-ve-yayim-2026-09-18)'dedir.

### Başlangıç cümlesini açıklamak

Önceki Kaynak İnceleyici bir rapor hazırlasın. “Bitti” derken bir Run'ın sona ermesini, rapor taslağının hazırlanmasını, incelemenin tamamlanmasını veya raporun doğru hedefe teslim edilmesini kastedebiliriz. Hangisi iş kapsamındaysa tamamlanma ona göre değerlendirilir. OA-End'in final-output kuralı bir yürütme bitişi örneğidir; bundan rapordaki iddiaların doğruluğu çıkmaz. WM-Closure da yürütme, iş kapanışı ve gerçekleşen etkiyi ayırır.

**İlk düzeltme:** Tamamlanma, doğrulama ve yayımlama zorunlu bir sıra değildir. Bir işin tamamlanmış sayılması doğrulamayı veya teslimi zaten gerektirebilir. Scrum-DoD'daki kaliteye bağlı Done kullanımı, “önce bitmiş olur, sonra doğrularız” şeklinde evrensel sıra kurmamıza karşı örnektir. Sadece Run durduğundan, başka işlem kalmadığından veya durum alanı kapalı olduğundan başarılı Completion sonucu çıkarılmaz.

**İkinci düzeltme:** Kontrol edilmiş sonuç ile işlem yapma yetkisini ayırıyoruz. NIST-VV'deki belirtilmiş gereklilik / amaçlanan kullanım ayrımını yerel Verification/Validation için kullanıyoruz; sözlükteki tüm farklı kullanımların aynı olduğunu iddia etmiyoruz. Yayımlama izni ise kim, hangi içerik ve hedef için ne yapabilir sorusudur. GH-Deploy'de onay işin ilerlemesine izin verir; yayımın başarıyla gerçekleşmesi ayrı olaydır.

### Aynı rapor üzerinde karşılaştırılan durumlar

Aşağıdaki koşullar varsayımsaldır. Sonuçlar metinsel tutarlılık incelemesidir, çalıştırılmış test sonucu değildir.

| Durum | Yerel anlatım / çıkarılmaması gereken sonuç |
|---|---|
| Run döndü; rapor R1 oluştu, içerik kontrolü yapılmadı. | Çalıştırma bitti, taslak var. Yalnız taslak hazırlamak istenmişse o kapsam tamamlanmış olabilir; doğrulanmış veya yayımlamaya hazır olduğu çıkmaz. |
| İşin tamamlanma koşulu kaynak kontrolünü de içeriyor; bu kontrol başarısız. | Dosya hazırlanmış olsa da bu kapsam tamamlanmış değildir. “Yazım bitti” ile “inceleme işi tamamlandı” ayrılır. |
| R1'in sayıları doğrulandı; yalnız iç ekip için paylaşma yetkisi var. | Sayısal doğrulama, kamusal yayım izni veya kamusal kullanım uygunluğu değildir. Teknik erişim de bu sınırı genişletmez. |
| Aynı agent, başka modelle R2'yi yazdı veya yayım hedefi değişti. | R1'e/önceki hedefe ait kanıt ve iznin ilgili yeni koşulları kapsayıp kapsamadığına bakılır. Maddi değişiklik yoksa her şeyi tekrar incelemek de zorunlu değildir. |
| R1 için yetki ve geçerli izin var; gerekli hizmet çalışmıyor. | Yetkili olmak, şu anda gerçekleştirebilmek veya gerçekleştirmiş olmak değildir. İşlem gerçekleşmeden “yayımlandı” denmez. |
| İş iptal edildi ve bekleyen adım kalmadı. | İptal sonucu kapanış, başarılı tamamlanma sayılmaz. Önceki “normal ilerleme gerektirmiyor” tanımı bu durumda fazla genişti. |

**Onay sözcüğünün kapsamı:** “İnceleme uygun bulundu”, “teslim kabul edildi” ve “şu işlem yapılabilir” farklı açıklamalardır. Bunların her biri için yeni nesne veya yeni insan onayı zorunlu değil. Önceden verilmiş koşullu yetki yeterli olabilir; OA-Approval bazı araçlarda kodla karar verilmesini de örnekler. Kaynağın approval işlevini genel kalite sertifikası diye çevirmiyoruz.

**Aynı nesneye bağlama:** Bu kullanım için gereken niteleme, örneğin “R1 raporu, iç ekip hedefi, kaynak kontrolü ölçütleri, geçerli izin”dir. Sabit veri şeması önermiyoruz. Aynı çıktı üzerinde birden fazla koşulun geçerli olması gerekirken farklı sürümlere/hedeflere ait olumlu kayıtların yanlışlıkla birleştirilmesini önlüyoruz.

### Önceki küme ile birlikte anlatım

“İnceleyici rolündeki agent yeni oturumda önceki iş bilgisini devraldı ve model B ile R2 raporunu hazırladı. R1 için verilen kontrol sonucunu R2'ye otomatik taşımıyoruz. R2'nin gerekli kontrolleri tamamlanınca inceleme işi kapatılabilir. Yayımlama ise ilgili hedef için geçerli yetki/izin ve uygulanabilirlik koşullarına bağlıdır; gerçekleştiği ayrıca kaydedilir.”

Bu örnek kimlik, model, oturum, çıktı, iş durumu, kanıt ve yetkiyi aynı anlatımda birleştirir. Her kelimeyi yeniden tanımlamadan hangi iddianın değiştiğini söyleyebiliyoruz. Yayımı iş kapsamına dahil etmişsek bütün iş, yalnız rapor hazırlanıp kontrol edilince tamamlanmış olmaz.

### İlişki haritası — aşama sırası değil

```text
İş kapsamı + tamamlama koşulları — belirler → Completion'ın neyi anlattığını
Çıktı/sürüm + gereklilikler + Evidence — sınanır → Verification
Amaçlanan kullanım + ihtiyaç + Evidence — sınanır → Validation
Verification/Validation — koşula dahil olabilir → Completion

Actor — belirli kapsamda yetkilidir → Authority
Somut işlem / kaynak / koşul — izinle sınırlanır → Permission
Araçlar + ortam — etkiler → fiili yapabilme / Capability
Bunların ilgili koşulları — birlikte etkiler → o yayıma Readiness

Runtime + Tool — izinli işlemi yürütür → gerçekleşen yayım etkisi
Etki ve kontrol kayıtları — günceller → Work state
Work state — yeni Session'da seçilerek devralınabilir → Context
```

Olumlu doğrulama tek başına yetki; izin tek başına gerçekleşme; kayıt tek başına doğruluk değildir. Bunları ayırmak, her sorumluluk için ayrı agent, servis veya kişi kurmak değildir.

### Dar sonuç ve devam sınırı

Bu örnekte tamamlanma beyanı/koşulu, doğrulama kapsamı, eylem yetkisi, somut izin, fiili olanak ve gerçekleşen sonuç ayrılabiliyor. Kullanılan yerel anlamlar çalışma için seçildi; bütün güvenlik/iş yönetimi alanı veya kırk madde tamamlanmış sayılmadı. Kaynaklar farklı sözleşmeler taşıdığı için tek bir evrensel durum makinesi kurulmadı.

Bu ve model/oturum kümesi artık birlikte açıklanabilir bir çekirdek adayıdır. Sonraki anlamlı adım yeni bir kavram paketi değil, mevcut bir dış kaynak bölümünü bu dille açıklayıp özgün anlamla geri karşılaştırmaktır. Gözlenen önemli bir eksik olmadıkça bu örneklerin bütün kaynak taraması tekrarlanmaz.

## Diğer kümelerin devralınan haritası — tamamlanma bağı dışında yeniden sınanmadı

```text
Intent
└── clarified-as → Goal
      ├── guides → Plan
      ├── target-for → Validation
      └── measured/judged-by → Evaluation

Plan
├── decomposes → Work items
├── proposes → Dependencies / sequencing / Actors
└── revised-by → Evidence / State / discovered Work

Work item
├── may depend-on → Work item / Artefact / Decision / external condition
├── has-derived → Readiness
├── progresses-through → Work state
└── may reach → Completion
                    │
                    ├── may require evidence from → Verification
                    └── does NOT imply → Goal achievement / Validation

Dependency ─contributes-to→ Readiness

Observability ─produces→ Evidence
Evidence
├── supports/challenges → Verification
├── supports/challenges → Validation
└── feeds → Evaluation

Verification ─asks→ specified claim/requirement satisfied?
Validation ─asks→ intended use / Goal / need satisfied?
Evaluation ─asks→ how well / under what criteria / at what risk?

State
├── specialization → Work state
├── may persist-via → Persistence
└── selected portion → Context

Work state
├── contains → Work item standing / Dependency / Readiness /
│              Completion / Evidence / next-resume
└── may persist-across → Runs / Sessions / Actors

Harness
└── connects/configures → Runtime / Context / Memory / Policy /
                         Sandbox / Orchestration / Verification /
                         Observability / Persistence

Runtime ─executes→ Agent / Workflow ─within→ Environment
Actor ─assumes→ Role
Actor ─operates-within→ Authority; somut işlem ayrıca Permission ile nitelenir
Agent ─may-be→ Actor
```

## Kritik ayrım zincirleri — devralınan diğer notlar

### Intent / Goal / Plan
- **Intent:** neyi/neden istiyoruz?
- **Goal:** hangi target state/outcome'a ulaşmak istiyoruz?
- **Plan:** oraya nasıl gitmeyi şu anda öneriyoruz?

### Work item / Dependency / Readiness
- **Work item:** ayrı yönetilen Work birimi.
- **Dependency:** başka bir condition/state/output'a bağ.
- **Readiness:** belirli next action için şu anda admissible/actionable mı?

### Completion / Verification / Validation
- **Completion:** bu iş kapsamının tamamlama koşulları karşılandı mı?
- **Verification:** ilgili çıktı/sürüm belirtilmiş gereklilikleri karşılıyor mu?
- **Validation:** amaçlanan kullanım ve ihtiyaç karşılanıyor mu?

Bunlar zorunlu sıra değildir; kontroller tamamlanmanın koşuluna dahil olabilir.

### Evaluation / Evidence
- **Evaluation:** criteria altında performans/quality/capability/risk judgment.
- **Evidence:** bu judgment/claim'leri dayandırdığımız traceable ground.

## Değişiklik kaydı

2026-09-18 sadeleştirmesi: v0.4'ün tanım, ilişki haritası ve ayrım gövdeleri buraya aktarıldı. Sürüm/kabul iddiaları ve otomatik sonraki-onlu yönlendirmesi devralınmadı. Kapsam uyarıları eklendi. O bakımda kaynak araştırması, tanım kabulü veya kullanım testi yapılmadı. Özgün sürümler ve ayrıntılı gerekçeler [HISTORY](HISTORY.md)'den geri bulunur.

2026-09-18 kullanım incelemesi: model değiştirme ve oturumda devam birlikte ele alındı. Agent'ın çalışma tarifi/kimliği/rolü ayrıldı; Model ve LLM ifadeleri sadeleştirildi; Run'ın kesintisiz çalışma veya tek çağrı sanılması, Session'ın tek Agent'a veya zorunlu kalıcılığa eşitlenmesi düzeltildi. Context'in yerel kod verisinden farkı geri getirildi. Tool/Runtime çağrı-yürütme sınırı açıklandı. Numaralı diğer maddeler korunur. Kaynak ve açıklayıcı karşı örnek incelemesidir; canlı SDK/ürün, model değişim performansı veya bağımsız iletişim testi değildir.

2026-09-18 tamamlanma/yayım incelemesi: Capability, Authority, Permission, Work state, Verification, Readiness, Completion, Validation ve Evidence yerel kullanımları somut durumlarla düzeltildi. Tamamlanma beyanı ve koşulların gerçekten karşılanması ayrıldı; doğrulamayı yalnız kapanış sonrasına koyan ok ve otomatik Authority→Permission görünümü düzeltildi. Önceki model/oturum örnek gövdesi korundu. Kaynaklar ve karşı örnekler SOURCES/ilgili bölümde; canlı uygulama veya bağımsız anlama deneyi yok.
