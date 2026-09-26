# EXP-006 — ACTORS

**Rol:** EXP-006 sırasında Work'ten türeyen actor / role-family / specialization / mechanic registry'si.  
**Statü:** Current **candidate** çalışma yüzeyi; nihai Development OS organizasyonu değildir.

## Temel ayrımlar

- **Aktör ≠ rol.**
- **Rol familyası ≠ specialization.**
- **Specialization ≠ effective assignment.**
- Rol/familya sayısından fiziksel agent/model/oturum sayısı çıkarılmaz.
- Aynı actor farklı zamanlarda farklı effective assignment'lar taşıyabilir.
- Aynı familya aynı prompt içinde bütün specialization'ların birleştirilmesi anlamına gelmez.

## Aktör sınıfları

### İnsan

Bu çalışmada insanın açılmış rolü **müşteri / principal** olarak ele alınır.

Kabul edilmiş çekirdek:
- **Yetki:** AI'ın hangi amaç ve sınırlar içinde müşteri adına hareket edebileceğinin meşru kaynağı.
- **Kabul:** Sonucun müşterinin ihtiyacını karşılayıp karşılamadığına ilişkin son hüküm.

Teknik keşif, koordinasyon, doğrulama veya implementasyon yükü varsayılan olarak müşteriye geri bırakılmaz.

### Yapay zekâ

“Yapay zekâ” şimdilik geniş actor sınıfıdır. LLM/agent/subagent/model-instance ayrımı Work gerektirmedikçe actor sınıfı olarak sabitlenmez.

## Current candidate role-family modeli

| Family | Başarı yönü | Current specialization örnekleri / lineage |
|---|---|---|
| **F1 — Tasarlama / Oluşturma** | İhtiyaç, amaç, kısıt ve mevcut gerçeklerden downstream work'ün kullanabileceği uygulanabilir ve sınanabilir tasarım üretmek | common baseline (R1), information lifecycle design (R4), role/actor formation (R7), Work formation/planning (R10), Environment design (R13), cross-ground composition design (R16), working-system formation (R19), evaluation design (R24) |
| **F2 — Gerçekleştirme / Uygulama** | Tasarım/gereksinimi gerçek, kullanılabilir ve sınanabilir artefakt veya mekanizmaya dönüştürmek | **initial R1–R25 içinde primary owner yok**; specialization fixed M-list değil **exact realization object + domain competence** üzerinden oluşur. M1–M9 önemli mechanical coverage; instruction/role/config/schema/procedure/adapter/integration/test-harness gibi non-M artefaktlar da F2 olabilir |
| **F3 — İşletim / Stewardship / Koordinasyon** | Aktif Work/system/capability'yi current koşullarda doğru durumda yürütmek ve gerekli operational geçişleri yönetmek | context/retrieval ops (R5), **Information Lifecycle Operations**, **Actor / Role Participation Lifecycle Operations**, Work admission/flow (R11), Environment ops (R14), configuration assembly/activation (R20), continuity/re-entry (R21), evaluation campaign ops (R25) |
| **F4 — Yönetişim / Yetki / Kontrol** | Mandate, delegation ve governed-effect sınırlarını korumak; technical capability ile legitimate authority'yi karıştırmamak | authority/delegation governance (R9), exact-effect/control/transition governance (R17) |
| **F5 — Doğrulama / Güvence** | Bir claim için kanıtın neyi gerçekten desteklediğine doğru hükmetmek | behavior (R2), information (R6), actor qualification (R8), Work/closure (R12), Environment/effect (R15), composite assurance (R18) |
| **F6 — Teşhis / Etki Analizi / Recovery Yönlendirme** | Failure/change sonrası doğru neden, etki, invalidation ve güvenilir geri dönüş yolunu belirlemek | causal diagnosis/root-cause routing (R3), change-impact/invalidation/recovery-path selection (R22) |
| **F7 — Öğrenme / Adaptasyon Yönlendirme** | Experience/outcome/feedback'in reusable change'e yükseltilip yükseltilmeyeceğini ve hangi scope'ta değişiklik gerektirdiğini yönetmek | learning/adaptation direction (R23) |
| **F8 — Araştırma / Keşif / Sentez** | Yetkili bilgi sorusunu kaynak, gözlem ve uygun incelemeyle aydınlatmak; desteklenen bulgu, sınır ve açık soruları kullanılabilir bilgi olarak teslim etmek | S1-15 ile ayrı aday; kavramsal/karşılaştırmalı inceleme, mekanizma/yapılabilirlik, ampirik inceleme olası specialization yüzeyleridir. Initial R1–R25 içinde bağımsız araştırma teslimatı birincil rol olarak adlandırılmamıştı; yeni R26 atanmadı. |

Bu model kullanıcı tarafından nihai DevOS kadrosu olarak kabul edilmiş değildir. S1-14 F1–F7'nin B1–B9 coverage/overlap denetimiydi; [S1-15](work/S1-15-research-discovery-synthesis-family.md) araştırma sınırını derinleştirerek ayrı F8 adayını ekledi. Bu nitel model tercihi, sekiz familyanın zorunlu/optimal olduğunun veya gerçek sistemde çalıştığının kanıtı değildir.

## F2/F3 specialization sınırları — S1-16

### F2 realization

F2 specialization sabit rol kataloğundan veya M1–M9 kimliklerinden türetilmez.

**Current aday kural:** exact realization object + domain competence.

Realization nesnesi code/hook/service gibi mekanik artefakt olabileceği gibi instruction, role/config/schema, procedure, adapter/integration veya evaluation harness da olabilir.

- F1 tasarlar.
- F2 reusable/usable artefaktı veya mekanizmayı gerçekleştirir/değiştirir.
- F3 mevcut mekanizmayla current state/operation'ı yürütür.
- F4 governing sınırı korur.
- F5 claim'i sınar.

Aynı actor bu assignment'ları taşıyabilir; local producer test'i bağımsız assurance değildir.

### F3 Information Lifecycle Operations

R5 context/retrieval ile aynı familyada fakat ayrı specialization'dır.

Owned operational object: canonical/qualified Information lifecycle state.

Örnek işler: write/update/revise; supersede; archive/restore; retention/expiry/deprecation/forgetting; conflict/pending update'i doğru lifecycle state'e taşıma; currentness/index bakımının operasyonu.

Lifecycle semantics F1/R4; mechanism F2/M2; access/governance F4; integrity assurance F5/R6; diagnosis F6 tarafından taşınır.

### F3 Actor / Role Participation Lifecycle Operations

S1-14'teki “Actor / Role Lifecycle Operations” adı daraltıldı.

Owned operational object: actor–role participation/binding standing.

Örnek işler: actor-role bind; assigned ↔ active participation; scope/episode activation; deactivate; reassign/replace; retire; standing responsibility'yi yeni episode'a yeniden bağlama.

R7 formation/design, R9 authority/delegation governance, R20 Working Configuration assembly ve R21 continuity/re-entry bu specialization'la kesişir fakat onu tek başına ikame etmez.

Bu specialization'ların görünürleşmesi yeni R numarası, physical agent veya service kararı değildir.

## F8 sınırı — yöntem ile esas teslimat

Araştırma F1–F7 içinde yöntem/kabiliyet olarak kullanılmaya devam eder. F8, esas teslimatı tasarım, uygulama, güvence, recovery veya adaptation kararı değil **kaynaklı bilgi sonucu** olan Work'ü açıkça taşıma adayıdır.

- F1 araştırma bulgusunu kullanıp çözüm tasarlayabilir; aynı actor ikisini ayrı veya küçük işte birleşik görevlendirmeyle taşıyabilir.
- F5 de yeni soru/karşı kaynak arar; yalnız checklist rolü değildir. Araştırmacının kendi sonucuna yaptığı kontrol bağımsız F5 assurance yerine geçmez.
- F6'nın investigation'ı failure/change/geri dönüş sorusunu taşıdığı sürece F6 kalır.
- F3'ün bilinen kaydı bulup context'e sunması otomatik F8 değildir; Information kayıt bakımı da F3'tür.
- Work/önkoşul keşfi yalnız “keşif” adı nedeniyle F8'e taşınmaz.
- F7, bulgunun reusable davranış/yöntem değişikliğine yükseltilmesini ayrıca değerlendirir.

F1'in genişletilmesi veya araştırma/güvencenin geniş bir F5 epistemik üst aile altında toplanması mantıken mümkün alternatiflerdir. Current tercih, farklı teslimat ve epistemik konumu ayrı F8 ile görünür tutmaktır; tek doğru ontoloji iddiası değildir.

F8'in başarısı kaynak/sayfa veya kesinlik miktarı değildir. Sonuç yeni bir belirsizliği görünür kılabilir, mevcut varsayımı çürütebilir veya gerekçeli biçimde sonuçsuz kalabilir. Sınırlandırılmış/engellenmiş araştırma, çözülmüş soru diye sunulmaz. Her küçük arama için ayrı rol/ajan zorunlu değildir.

## Effective assignment için current aday formül

Bir somut rol görevlendirmesi yalnız familya adıyla tanımlanmaz.

Aday yapı:

**family / success direction × specialization × exact assignment object × actor operating profile → effective assignment**

Exact assignment object; göreve göre Work / claim / target / artifact / transition / experience / araştırma sorusu ve ilgili scope'u açıkça bağlamalıdır. F8'de beklenen bilgi teslimatı, araştırma alanı/hedefi ve gerektiğinde zaman/sürüm de görünür olur. Family + specialization tek başına somut rol değildir.

Actor operating profile en az şu tür koşulları taşıyabilir:
- gerekli bilgi ve context;
- competence;
- tools/environment;
- permission/authority;
- trigger;
- handoff/consumer;
- verification/independence koşulları.

Bu şema da henüz nihai değildir. S1-15 sözleşmesi aday gereksinimdir; çalışan görevlendirme mekanizması kurulmadı.

## Initial R1–R25 lineage eşlemesi

Aşağıdaki kayıt ilk Work decomposition'ından gelen lineage'ı korur. **Current organizasyon listesi değildir.** Araştırma kullanmaları nedeniyle eski roller otomatik F8'e taşınmaz.

| ID | İlk aday rol | Current family yorumu |
|---|---|---|
| R1 | Ortak Çalışma Tabanı Tasarımcısı | F1 — common-baseline design |
| R2 | Davranış Doğrulayıcısı | F5 — behavior assurance |
| R3 | Davranış Teşhisçisi / Değişiklik Analisti | F6 — causal diagnosis / routing |
| R4 | Information Steward / Bilgi Yaşam Döngüsü Tasarımcısı | F1 — information lifecycle design; F3 operation kısmı initial tanımda yeterince açık değildi |
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
| **M1** | Mekanik davranış sınırı / identity-role-grant enforcement | B1, B3; B5/B6 ile kesişir | candidate requirement |
| **M2** | Information persistence / retrieval / exposure mechanics | B2; B5/B6 ile kesişir | candidate requirement |
| **M3** | Work identity / admission / claim / transition mechanics | B4; B6 ile kesişir | candidate requirement |
| **M4** | Environment provisioning / runtime / workspace / isolation substrate | B5 | candidate requirement |
| **M5** | Effect execution / readback / observability substrate | B5, B6 | candidate requirement |
| **M6** | Cross-ground binding / standing checks / guarded-transition substrate | B6, B7 | candidate requirement |
| **M7** | Working Configuration identity / binding / activation / lifecycle substrate | B7, B8 | candidate requirement |
| **M8** | Durable continuity / handoff / stale-writer protection / recovery correlation substrate | B8 | candidate requirement |
| **M9** | Evaluation harness / test isolation / evidence capture / target-version binding substrate | B9 | candidate requirement |

M1–M9 fiziksel modül veya servis sayısı değildir. F2 bu mekanik sorumlulukların realization işini taşıyabilir; F3 operating lifecycle'ını taşıyabilir; F5 ilgili claim'leri sınayabilir. F8'in araç/deney gereksinimleri yeni M10 veya B10 yaratmaz; mevcut capability'ler yeterliyse kullanılır.

## Current açık sorular

S1-16 sonucu:
- F1–F8 candidate family modeli korunuyor;
- F2 realization specialization sınırı exact realization object + domain competence ile netleştirildi;
- F3 Information Lifecycle Operations ayrı specialization olarak korundu;
- F3 Actor / Role Participation Lifecycle Operations ayrı specialization olarak korundu;
- yeni familya/R numarası/physical actor açılmadı.

Current açıklar:
- final S1 consolidation/closure audit current modelde orphan/duplicate/handoff açığı buluyor mu?
- exact assignment object + actor operating profile modeli S1 closure için yeterli mi, yoksa eksik kısmı sonraki effective-assignment aşamasına mı ait?
- F8 dahil familyaların gerçek competence/tetik/devir/independence düzeni sonraki aşamada nasıl kurulmalı?
- kaç fiziksel actor/model/session gerekir?

Bu soruların son ikisi otomatik olarak S1 family/specialization problemi değildir. Final audit bu sınırı belirlemeden familyaları nihai Development OS organizasyonu sayma.

