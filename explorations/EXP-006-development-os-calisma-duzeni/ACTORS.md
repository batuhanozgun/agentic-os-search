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
| **F2 — Gerçekleştirme / Uygulama** | Tasarım/gereksinimi gerçek, kullanılabilir ve sınanabilir artefakt veya mekanizmaya dönüştürmek | **initial R1–R25 içinde primary owner yok**; M1–M9 mechanical realization yüzeyleri önemli specialization kaynağıdır, fakat instruction/role/configuration/procedure/adapter/test-harness gibi non-M artefakt realization'ı da F2 kapsamına girebilir |
| **F3 — İşletim / Stewardship / Koordinasyon** | Aktif Work/system/capability'yi current koşullarda doğru durumda yürütmek ve gerekli operational geçişleri yönetmek | context/retrieval ops (R5), Work admission/flow (R11), Environment ops (R14), configuration assembly/activation (R20), continuity/re-entry (R21), evaluation campaign ops (R25), **Information Lifecycle Operations — açık specialization**, **Actor / Role Lifecycle Operations — yeni açık specialization** |
| **F4 — Yönetişim / Yetki / Kontrol** | Mandate, delegation ve governed-effect sınırlarını korumak; technical capability ile legitimate authority'yi karıştırmamak | authority/delegation governance (R9), exact-effect/control/transition governance (R17) |
| **F5 — Doğrulama / Güvence** | Bir claim için kanıtın neyi gerçekten desteklediğine doğru hükmetmek | behavior (R2), information (R6), actor qualification (R8), Work/closure (R12), Environment/effect (R15), composite assurance (R18) |
| **F6 — Teşhis / Etki Analizi / Recovery Yönlendirme** | Failure/change sonrası doğru neden, etki, invalidation ve güvenilir geri dönüş yolunu belirlemek | causal diagnosis/root-cause routing (R3), change-impact/invalidation/recovery-path selection (R22) |
| **F7 — Öğrenme / Adaptasyon Yönlendirme** | Experience/outcome/feedback'in reusable change'e yükseltilip yükseltilmeyeceğini ve hangi scope'ta değişiklik gerektirdiğini yönetmek | learning/adaptation direction (R23) |

Bu model kullanıcı tarafından nihai DevOS kadrosu olarak kabul edilmiş değildir. S1-14 bütün familyaların B1–B9 coverage/overlap denetimini yaptı; F1–F7 reddedilmedi fakat research/discovery ayrı success direction olabilir ve bu soru ayrıca sınanacaktır.

## Açık family candidate — research / discovery / synthesis

S1-14, research'ü yalnız cross-family yöntem/kabiliyet saymanın artık yeterince güvenli olmadığını buldu.

Research:
- F1/F5/F6/F7 içinde yöntem olarak kullanılabilir;
- fakat bazı Work'lerde primary deliverable source-grounded bulgu, karşıörnek veya sentez olabilir;
- bu durumda tasarım, assurance verdict'i, recovery veya adaptation kararı üretmeden bounded biçimde kapanabilir.

Henüz `F8` kabul edilmedi.

Açık bounded test üç rivalı karşılaştıracaktır:
1. research yalnız cross-family method/capability;
2. research F1 içinde specialization;
3. research ayrı candidate success-direction familyası.

## Effective assignment için current aday formül

Bir somut rol görevlendirmesi yalnız familya adıyla tanımlanmaz.

Aday yapı:

**family / success direction × specialization × exact assignment object × actor operating profile → effective assignment**

Exact assignment object; göreve göre Work / claim / target / artifact / transition / experience ve ilgili scope'u açıkça bağlamalıdır. Family + specialization tek başına somut rol değildir.

Actor operating profile en az şu tür koşulları taşıyabilir:
- gerekli bilgi ve context;
- competence;
- tools/environment;
- permission/authority;
- trigger;
- handoff/consumer;
- verification/independence koşulları.

Bu şema da henüz nihai değildir.

## Initial R1–R25 lineage eşlemesi

Aşağıdaki kayıt ilk Work decomposition'ından gelen lineage'ı korur. **Current organizasyon listesi değildir.**

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

M1–M9 fiziksel modül veya servis sayısı değildir. F2 bu mekanik sorumlulukların realization işini taşıyabilir; F3 operating lifecycle'ını taşıyabilir; F5 ilgili claim'leri sınayabilir.

## Current açık sorular

S1-14 full-model audit sonucu:
- F1–F7 hard duplicate olmadan B1–B9'un ana responsibility gövdesini karşılıyor;
- F2 initial R-lineage primary-owner açığı sürüyor;
- F3 Information Lifecycle Operations specialization açığı doğrulandı;
- F3 **Actor / Role Lifecycle Operations** specialization açığı yeni bulundu;
- decision ayrı familya gerektirmiyor;
- coordination current evidence altında F3 içinde kalabiliyor;
- research / discovery / synthesis ayrı success direction olabilir ve henüz çözülmedi.

Current açıklar:
- research yalnız method/capability mi, F1 specialization mı, ayrı candidate familya mı?
- F2 realization specialization sınırları nasıl çizilmeli?
- iki yeni F3 operational specialization mevcut görevlendirmelerle ne ölçüde birleşebilir?
- exact assignment object + actor operating profile modeli yeterli mi?
- independence gerektiğinde actor/session/context ayrımı nasıl kurulmalı?
- kaç fiziksel actor/model/session gerekir?

Bu sorular çözülmeden familyaları nihai Development OS organizasyonu sayma.
