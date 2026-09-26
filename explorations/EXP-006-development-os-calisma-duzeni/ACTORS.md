# EXP-006 — ACTORS

**Rol:** Work'ten türeyen actor / role-family / specialization / mechanic registry'si.  
**Statü:** S1-17 sonrasında **CLOSURE-READY / CANDIDATE** konsolidasyon. Kullanıcıca kabul edilmiş nihai Development OS organizasyonu, actual assignment veya çalışan sistem değildir.

## Temel ayrımlar

- Aktör ≠ rol; rol familyası ≠ specialization; specialization ≠ effective assignment.
- Familya sayısından fiziksel agent/model/oturum sayısı çıkarılmaz.
- Aynı actor farklı zamanlarda farklı effective assignment'lar taşıyabilir.
- Aynı familya bütün specialization'ları aynı prompt'ta birleştirme emri değildir.
- Esas teslimat/success direction belirleyicidir; bir dosyanın yazılmış olması familyayı belirlemez.

## Aktör sınıfları

### İnsan

Bu çalışmada açılmış rolü **müşteri / principal**dır.

- **Yetki:** AI'ın hangi amaç ve sınırlar içinde müşteri adına hareket edebileceğinin meşru kaynağı.
- **Kabul:** Sonucun müşterinin ihtiyacını karşılayıp karşılamadığına ilişkin son hüküm.

Teknik keşif, koordinasyon, doğrulama veya implementasyon yükü varsayılan olarak müşteriye geri bırakılmaz. Müşteri kabulü teknik kanıt; teknik verdict müşteri kabulü değildir.

### Yapay zekâ

Şimdilik geniş actor sınıfıdır. LLM/agent/subagent/model-instance ayrımı Work gerektirmedikçe actor sınıfı olarak sabitlenmez.

## Current candidate role-family modeli

| Family | Başarı yönü | Current specialization / lineage |
|---|---|---|
| **F1 — Tasarlama / Oluşturma** | İhtiyaç, amaç, kısıt ve mevcut gerçeklerden kullanılabilir, gerekçeli ve sınanabilir tasarım üretmek | common baseline (R1), information lifecycle design (R4), role/actor formation (R7), Work formation/planning (R10), Environment design (R13), cross-ground composition design (R16), working-system formation (R19), evaluation design (R24) |
| **F2 — Gerçekleştirme / Uygulama** | Gereksinim/tasarımı gerçek kullanılabilir uygulama, artefakt, mekanizma veya uyarlamaya dönüştürmek | initial R1–R25 içinde primary owner yok; exact realization object + domain competence. M1–M9 mekanikleri ve gerektiğinde instruction/config/schema/procedure/adapter/integration/test-harness çıktıları; dosya türü tek başına yeterli değil, reusable olmak zorunlu değil |
| **F3 — İşletim / Stewardship / Koordinasyon** | Aktif Work/system/capability'nin current operasyon ve geçişlerini doğru yürütmek | context/retrieval (R5), Information Lifecycle Operations, Actor / Role Participation Lifecycle Operations, Work admission/flow (R11), Environment ops (R14), configuration assembly/activation (R20), continuity/re-entry (R21), evaluation campaign (R25) |
| **F4 — Yönetişim / Yetki / Kontrol** | Mandate, delegation ve governed-effect sınırlarını korumak | authority/delegation governance (R9), exact-effect/control/transition governance (R17) |
| **F5 — Doğrulama / Güvence** | Belirli iddia/target için kanıtın gerçekten neyi desteklediğine hükmetmek | behavior (R2), information (R6), actor qualification (R8), Work/closure (R12), Environment/effect (R15), composite assurance (R18) |
| **F6 — Teşhis / Etki Analizi / Recovery Yönlendirme** | Failure/change sonrası doğru neden, etki, invalidation ve geri dönüş yolunu belirlemek | causal diagnosis/root-cause routing (R3), impact/invalidation/recovery-path selection (R22) |
| **F7 — Öğrenme / Adaptasyon Yönlendirme** | Experience/feedback'in reusable change gerektirip gerektirmediğini ve hangi scope'ta gerektiğini yönetmek | learning/adaptation direction (R23); no-change/deprecation/simplification da gerekçeli sonuç olabilir |
| **F8 — Araştırma / Keşif / Sentez** | Yetkili bilgi sorusunu kaynak/gözlemle aydınlatmak; desteklenen bulgu, sınır ve açık soruları teslim etmek | kavramsal/karşılaştırmalı, mekanizma/yapılabilirlik ve ampirik inceleme olası yüzeyler; kesin ayrık alt taxonomy değil. Initial R listesinde bağımsız bilgi teslimatı ayrıca adlandırılmamıştı |

S1-14 F1–F7 coverage audit'i; S1-15 F8 adayı; S1-16 realization/lifecycle ayrımları; [S1-17](work/S1-17-consolidation-closure-audit.md) kapanış kapsamı ve sınır düzeltmeleridir. Sekiz familyanın zorunlu/optimal olduğu veya gerçek sistemde çalıştığı kanıtlanmadı.

## S1-17 sınırları

### F2: dosya değil esas dönüşüm

Tasarım belgesi yazmak F1, araştırma raporu F8, verdict raporu F5, current kaydı mevcut kurala göre güncellemek F3 olabilir. Bir role ait davranış gereğini gerçekten tüketilebilir yönerge/uygulama/mekanizmaya dönüştürmek F2 olabilir. Aynı belge birkaç katkı taşıyabilir; ayrı dosya/ajan zorunlu değildir.

F2 specialization, exact realization object ve gereken domain competence'ten türetilir; M1–M9'a bire bir sabit geliştirici listesi değildir. Tek işe özgü adapter veya uygulama da F2'dir. Mevcut mekanizmayla normal activation/configuration işletmek F3 olabilir. S1-09/S1-10/S1-16'nın reusable örnekleri sınırın tamamı değildir.

F2'nin yerel testi producer evidence'dır; bağımsız F5 assurance yerine otomatik geçmez. Uygulanamaz tasarım F1'e açılır; requirement, criterion veya authority sessizce gevşetilmez.

### F3: Information Lifecycle Operations

R5 context/retrieval ile aynı familyada fakat ayrı specialization'dır. Operational nesnesi canonical/qualified Information lifecycle state'idir.

Write/update/revise; supersede; archive/restore; retention/expiry/deprecation/forgetting; conflict/pending-update statüsünü koruma; currentness/index bakımını kapsar.

- Lifecycle semantiği F1/R4, mekanizması F2/M2'dedir.
- Meşru erişim ve governed mutation sınırı F4; integrity assurance F5/R6'dadır.
- Domain hükmünün kaydı F3'e gelmesiyle hüküm otomatik doğru veya accepted olmaz.
- Çelişkide keyfî tek doğru üretmek yerine gerekli domain kararı aranır, unresolved statü korunur.
- Yeni bilgi sorusu F8; adaptation promotion kararı F7; failure teşhisi F6 olabilir.

R5'in sorusu aktörün şimdi doğru görünümü alması; bu specialization'ın sorusu kalıcı/current bilgi nesnesinin doğru lifecycle durumunda tutulmasıdır. Aynı actor uygun scope/authority ile ikisini taşıyabilir.

### F3: Actor / Role Participation Lifecycle Operations

S1-14'teki geniş Actor / Role Lifecycle Operations adının S1-16'da daraltılmış hâlidir. Operational nesnesi actor–role participation/binding standing'idir.

Actor-role bind; assigned/active katılım ayrımı; scope/episode activation; deactivate; reassign/replace; participation retire; standing responsibility'nin yeni episode'a bağlanması.

R7 formation/design, R9 authority/delegation, R20 Working Configuration assembly ve R21 continuity/re-entry ile kesişir ama tek başına bunlara eritilmez. Normal runtime/process oluşturma ve health F3 Environment/R14'te; yeni bağlama/enforcement mekanizması F2'dedir. Participation state'i authority, runtime liveness veya joint readiness ile eşitlenmez.

R20 whole-configuration teslimatını; participation uzmanlığı exact katılım geçişini taşıyabilir. Somut atamada aynı exact geçişe belirsiz iki primary owner verilmez; birleştirme/ayırma actual competence ve authority ile değerlendirilir.

### Geliştiren ile geliştirilen ayrımı

Bu registry DevOS geliştirme sorumluluklarının adayıdır. B metinlerindeki gelecekteki SOUL davranışları otomatik DevOS production-operation görevi değildir. F3 örnekleri DevOS'un yetkili geliştirme/deneme/kurulum nesnesine bağlanır. SOUL'un daha sonra kurduğu rol, kendi Work/scope/authority koşullarında ayrıca değerlendirilir. EXP-006 dosyalarının düzgün olması bu zincirin fiilen çalıştığının kanıtı değildir.

## F8 sınırı — yöntem ile esas teslimat

Araştırma F1–F7 içinde yöntem/kabiliyet olarak kullanılmaya devam eder. F8, esas teslimatı tasarım, uygulama, assurance, recovery veya adaptation kararı değil **kaynaklı bilgi sonucu** olan Work'ü taşır.

F1 araştırma kullanabilir; F5 karşı kaynak arayabilir ve kriteri eleştirebilir; F6 investigation yapabilir. Bunlar kendiliğinden F8 olmaz. Bilinen kaydı context'e getirmek F3, mevcut bilgiyle Work/önkoşul keşfi F1 olabilir. F7 bulgunun reusable davranış/yöntem değişikliğine aktarımını ayrıca değerlendirir.

F1'i genişletmek veya F5 altında epistemik üst aile kurmak mantıken mümkündür; current tercih farklı teslimat ve epistemik konumu F8 ile görünür tutmaktır. Tek doğru ontoloji değildir. Araştırmacının kendi kontrolü bağımsız assurance değildir.

F8'in başarısı kaynak/sayfa veya kesinlik miktarı değildir. Gerekçeli yeni belirsizlik, çürütme veya sonuçsuz bulgu geçerli olabilir; erişim/bütçe nedeniyle kesilen araştırma çözülmüş soru diye sunulmaz. Her küçük arama için ayrı rol/ajan gerekmez.

## Effective assignment için current aday formül

**family / success direction × specialization × exact assignment object × actor operating profile → effective assignment**

Exact nesne; Work/claim/target/artifact/transition/experience/araştırma sorusunu ve scope'u bağlar. Esas teslimat, kriter ve consumer görünür olmalıdır. F8 için bilgi sorusu, beklenen bilgi teslimatı ve gerektiğinde zaman/sürüm de gerekir.

Actor operating profile: competence; gerekli kaynak/context; araç/Environment; permission/authority; trigger; handoff/consumer; verification/independence koşulları.

Bu semantic requirement adayıdır; çalışan dispatcher, manifest şeması veya actual assignment değildir. S1-17 bu düzeyde yeterli buldu; gerçek bağlama ve davranış yeterliği sonraki işte açıktır.

## Initial R1–R25 lineage eşlemesi

İlk türetim kaydıdır; current organizasyon listesi değildir. Araştırma kullanmaları nedeniyle eski roller otomatik F8'e taşınmaz; primary eşleme karma katkıların tamamını tüketmez.

| ID | İlk aday rol | Current family yorumu |
|---|---|---|
| R1 | Ortak Çalışma Tabanı Tasarımcısı | F1 — common-baseline design |
| R2 | Davranış Doğrulayıcısı | F5 — behavior assurance |
| R3 | Davranış Teşhisçisi / Değişiklik Analisti | F6 — causal diagnosis / routing |
| R4 | Information Steward / Bilgi Yaşam Döngüsü Tasarımcısı | F1 — information lifecycle design; initial operation kısmı açık değildi |
| R5 | Context & Retrieval Curator / Bağlam Kurucusu | F3 — context/retrieval operations |
| R6 | Information Integrity Reviewer | F5 — information assurance |
| R7 | Role & Actor Formation Designer | F1 — role/actor formation |
| R8 | Actor Qualification Reviewer | F5 — actor qualification assurance |
| R9 | Actor Governance Steward | F4 — authority/delegation governance |
| R10 | Work Formation & Planning Designer | F1 — Work formation/planning |
| R11 | Work Admission & Coordination Steward | F3 — Work operations/coordination |
| R12 | Work Progress & Closure Reviewer | F5 — Work/closure assurance |
| R13 | Environment & Capability Formation Designer | F1 — Environment design |
| R14 | Environment Operations & Readiness Steward | F3 — Environment operations |
| R15 | Environment Reality & Effect Reviewer | F5 — Environment/effect assurance |
| R16 | Cross-Ground Composition Designer | F1 — composition design |
| R17 | Cross-Ground Control & Transition Steward | F4 — exact-effect/control governance |
| R18 | Composition Integrity Reviewer | F5 — composite assurance |
| R19 | Working System Formation Designer | F1 — mission/system formation |
| R20 | Working Configuration Assembly Steward | F3 — configuration assembly/activation operations |
| R21 | Continuity & Re-entry Steward | F3 — continuity/re-entry operations |
| R22 | Change Impact & Recovery Steward | F6 — impact/invalidation/recovery routing |
| R23 | Learning & Adaptation Steward | F7 — learning/adaptation direction |
| R24 | SOUL Evaluation Architect | F1 — evaluation design |
| R25 | Evaluation Campaign Steward | F3 — evaluation campaign operations |

## Mekanik sorumluluklar — aktör/rol değildir

| ID | Sorumluluk | Kaynak Work | Statü |
|---|---|---|---|
| M1 | Mekanik davranış sınırı / identity-role-grant enforcement | B1, B3; B5/B6 ile kesişir | candidate requirement |
| M2 | Information persistence / retrieval / exposure mechanics | B2; B5/B6 ile kesişir | candidate requirement |
| M3 | Work identity / admission / claim / transition mechanics | B4; B6 ile kesişir | candidate requirement |
| M4 | Environment provisioning / runtime / workspace / isolation substrate | B5 | candidate requirement |
| M5 | Effect execution / readback / observability substrate | B5, B6 | candidate requirement |
| M6 | Cross-ground binding / standing checks / guarded-transition substrate | B6, B7 | candidate requirement |
| M7 | Working Configuration identity / binding / activation / lifecycle substrate | B7, B8 | candidate requirement |
| M8 | Durable continuity / handoff / stale-writer protection / recovery correlation substrate | B8 | candidate requirement |
| M9 | Evaluation harness / test isolation / evidence capture / target-version binding substrate | B9 | candidate requirement |

M1–M9 fiziksel modül/servis sayısı değildir. Gereksinim/tasarım, gerçekleştirme, işletim ve assurance ayrı katkılardır. F8 gereksinimi otomatik M10/B10 yaratmaz.

## Current açıklar

S1-17 family/specialization modelini mevcut kapsam için kapanışa hazır buldu; kullanıcı değerlendirmesi bekleniyor. Yeni familya/R/physical actor açılmadı.

Açık kalan gerçek işler: exact geliştirme teslimatı için actor/competence seçimi; bilgi ve araç/ortamın fiilî erişimi; yetki ve tetik; devir/tüketim; independence; aktarımın gerçek davranışta sınanması. Bunlar tamamlanmış sayılmadı. Yeni familya boşluğu göstermedikçe isim konsolidasyonunu baştan tekrarlatmaları gerekmez.

Current sıra STATE/HANDOFF'tadır. S1-16'nın bazı tam-okuma iddiaları için S1-17 §7'deki qualification geçerlidir.
