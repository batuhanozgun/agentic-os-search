# Kavram Çalışması — Tek Çalışma Taslağı

**Durum:** GELİŞEN ÇALIŞMA REFERANSI; kaynaklara dayanan yerel tercihler ve henüz yeniden incelenmemiş taslaklar birlikte, aşağıda ayrılarak tutulur. Kullanıcının her maddeyi tek tek benimsediği veya evrensel tanımlar seçildiği iddia edilmez. SOUL mimarisi değildir.

Önceki [v0.4 kaydının](https://github.com/batuhanozgun/agentic-os-search/blob/4d849afc2e8b6ef6173957e0923606290912da1e/concepts/synthesis/CORE-TERMS-WORKING-v0.4.md) 40 numaralı maddesi ve Task alt kullanımı sadeleştirmede buraya taşındı. 2026-09-18 devam incelemesinde Agent–Model–yapılandırma–Actor/Role–Identity–Run/Session–Context ilişkileri, model değiştirme ve oturumda devam örnekleri üzerinden düzeltildi. Tool ve Runtime ifadeleri de bu ilişkideki çağrı/yürütme farkını koruyacak şekilde güncellendi. Diğer maddeler aynı olgunlukta sayılmaz.

Güncel iş [STATE](STATE.md), yöntem [METHOD](METHOD.md), dayanak ve gerçek okuma kapsamı [SOURCES](SOURCES.md#model-degisimi-ve-devam-2026-09-18)'dedir. Bu dosya yerinde güncellenir; her tur yeni sürüm veya terim paketi açılmaz.

## Kullanım kapsamı ve açık sınırlar

- Aşağıdaki Agent kullanımı model tabanlı yazılım agent'ları içindir. Klasik AI'daki daha geniş kullanımları veya bir SDK'nın `Agent` sınıfını yanlış ilan etmez. Bir API sınıf adından davranış güvencesi çıkarılmaz.
- Agent'ın adımlarını modelle seçebilmesi, her çalıştırmada araç çağırması ya da uzun bir döngü yürütmesi gerektiği anlamına gelmez. Yalnız sınıflandırma çıktısı veren model çağrısını burada otomatik Agent saymıyoruz; çevresindeki yürütme kontrolüne ayrıca bakıyoruz. Evrensel bir agency eşiği kapatılmadı.
- Aynı kimlik, aynı yapılandırma, aynı model ve aynı geçmiş farklı iddialardır. Hiçbiri tek başına diğerlerini ya da davranış eşdeğerliğini kanıtlamaz.
- Context'te bulunma ile kodun/veri deposunun erişebildiği bilgi aynı değildir. Model/ürün/sağlayıcı ayrımı aşağıda yalnız bu örnekler için açıklanır; ürün kataloğu veya model performansı kıyası yapılmadı.
- Work birçok eski açıklamada kullanılıyor fakat burada ayrı bir çalışma tanımı yok. Bu turdaki kullanımı gündelik anlamıyla yürütülen iştir; Foundation anlamı veya veri modeli seçilmez.
- Kaynak notu düzeltilmiş olan bu dar küme, önceki bütün kaynak iddialarını doğrulamaz. Diğer kümelerdeki karışık dil ve eski harita bağlantıları sonraki gerçek kullanım ihtiyacında ele alınır.

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
15. **Capability** — Actor/Agent/System'in Model/Tool/Runtime/Environment sayesinde fiilen yapabildiği şey.
16. **Authority** — Actor/Agent'ın owner/system adına hangi karar ve sorumlulukları meşru biçimde üstlenebileceği.
17. **Permission** — belirli resource/Tool/action üzerinde belirli işlemi yapmaya verilen somut izin.
18. **Orchestration** — execution sırasında kim/ne zaman/hangi sırada çalışacak ve next step nasıl seçilecek kontrol mantığı.
19. **Handoff** — active responsibility/execution control'ünün bir Agent'tan diğerine devri.
20. **Subagent** — daha geniş Work içinde başka Agent/Orchestrator'a göre alt sorumluluk taşıyan Agent.

### State / Environment / control surfaces — bu tur yeniden incelenmedi

21. **State** — entity/process/system'in belirli anda continuation/decision/control açısından anlam taşıyan current condition representation'ı.
22. **Work state** — Work'ün identity/scope/standing/blockers/ownership/evidence/next-resume bilgisini taşıyan current/durable state.
23. **Environment** — Work'ün gerçekleştiği dış koşullar ve erişilebilir kaynaklar bütünü.
24. **Workspace** — Work materyallerinin/files/repos/artefacts/outputs düzenlendiği alan.
25. **Sandbox** — execution erişimini files/processes/network/credentials/resources açısından sınırlayan controlled boundary.
26. **Policy** — expected/allowed/forbidden/conditional davranışları tarif eden rules/principles.
27. **Guardrail** — execution event'ini Policy/criteria/risk açısından check edip block/reject/transform/escalate edebilen aktif kontrol.
28. **Verification** — specified claim/requirement/property'nin Evidence ve criteria karşısında gerçekten desteklenip desteklenmediğini değerlendirme.
29. **Observability** — System/Run/Workflow'un fiilen ne yaptığı hakkında yeterli traces/logs/events/state visibility'si.
30. **Persistence** — State/Memory/Work state/artefact/identity-linked bilginin Run/process/session/runtime sınırı sonrasında da korunabilmesi.

### Intent → Work → result → evidence hattı — bu tur yeniden incelenmedi

31. **Intent** — user/owner isteğinin arkasındaki asıl yön, amaçlanan anlam ve neden; henüz operational Goal olmayabilir.
32. **Goal** — Work'ün yöneldiği açık target state/outcome/success condition.
33. **Plan** — Goal'e ulaşmak için önerilen ve revize edilebilir decomposition/approach/sequence/dependency/actor/control representation.
34. **Work item** — daha geniş Work içinde ayrı identity/scope/standing ile track/assign/depend/verify/close/reopen edilebilen yönetilebilir Work birimi.
    - **Task** — genellikle action-like Work item; source-local semantics varsa korunur.
35. **Dependency** — bir Work/artefact/action'ın start/validity/timing/closure/outcome'ının başka bir condition/state/output'a bağlı olduğu ilişki.
36. **Readiness** — belirli next action için prerequisites/information/authority/capacity/environment/control koşullarının yeterli olduğuna ilişkin derived standing.
37. **Completion** — belirli scope'un kendi lifecycle/acceptance koşullarına göre artık normal progression gerektirmediğini belirten closure standing/claim.
38. **Validation** — result/system/artefact'ın intended use, stakeholder need, Intent/Goal açısından gerçekten uygun/yararlı olup olmadığını değerlendirme.
39. **Evaluation** — Model/Agent/System/result/process'i criteria/tasks/rubric/metric/benchmark altında sistematik ölçüp performance/quality/capability/risk judgment üretme.
40. **Evidence** — claim/standing/decision/Verification/Validation/Evaluation sonucunu destekleyen veya sınırlandıran traceable information/observation/artefact/test result/record.

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

## Diğer kümelerin devralınan haritası — bu tur yeniden sınanmadı

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
                    ├── may trigger → Verification
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
Actor ─operates-within→ Authority → Permissions
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
- **Completion:** scope kapandı mı?
- **Verification:** specified claim/requirement doğru mu?
- **Validation:** amaçlanan kullanım/Goal gerçekten karşılandı mı?

### Evaluation / Evidence
- **Evaluation:** criteria altında performans/quality/capability/risk judgment.
- **Evidence:** bu judgment/claim'leri dayandırdığımız traceable ground.

## Değişiklik kaydı

2026-09-18 sadeleştirmesi: v0.4'ün tanım, ilişki haritası ve ayrım gövdeleri buraya aktarıldı. Sürüm/kabul iddiaları ve otomatik sonraki-onlu yönlendirmesi devralınmadı. Kapsam uyarıları eklendi. O bakımda kaynak araştırması, tanım kabulü veya kullanım testi yapılmadı. Özgün sürümler ve ayrıntılı gerekçeler [HISTORY](HISTORY.md)'den geri bulunur.

2026-09-18 kullanım incelemesi: model değiştirme ve oturumda devam birlikte ele alındı. Agent'ın çalışma tarifi/kimliği/rolü ayrıldı; Model ve LLM ifadeleri sadeleştirildi; Run'ın kesintisiz çalışma veya tek çağrı sanılması, Session'ın tek Agent'a veya zorunlu kalıcılığa eşitlenmesi düzeltildi. Context'in yerel kod verisinden farkı geri getirildi. Tool/Runtime çağrı-yürütme sınırı açıklandı. Numaralı diğer maddeler korunur. Kaynak ve açıklayıcı karşı örnek incelemesidir; canlı SDK/ürün, model değişim performansı veya bağımsız iletişim testi değildir.
