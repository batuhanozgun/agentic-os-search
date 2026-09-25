# EXP-006 — ACTORS

**Rol:** EXP-006 sırasında Work'ten türeyen aktör/rol/sorumluluk registry'si.  
**Statü:** Çalışma yüzeyi; nihai Development OS organizasyonu değildir.

## Temel ayrım

**Aktör ≠ rol.** Aynı aktör farklı zamanlarda farklı rolleri üstlenebilir; aynı rol farklı aktör örneklerince taşınabilir. Rol sayısından fiziksel agent/model/oturum sayısı çıkarılmaz.

## Aktör sınıfları

### İnsan

Bu çalışmada insanın şu an açılmış rolü **müşteri**dir.

**Konuşmada netleşen çekirdek:**
- **Yetki:** Yapay zekânın hangi amaç ve sınırlar içinde müşteri adına hareket edebileceğinin meşru kaynağı.
- **Kabul:** Ortaya çıkan sonucun müşterinin ihtiyacını karşılayıp karşılamadığına ilişkin son hüküm.

Bu, insanın bütün olası rollerinin tanımı değildir. Teknik keşif/koordinasyon yükü varsayılan olarak müşteriye geri bırakılmaz.

### Yapay zekâ

“Yapay zekâ” şimdilik geniş aktör sınıfıdır. LLM/agent/subagent/model-instance ayrımı bu Work gerektirmedikçe aktör sınıfı olarak sabitlenmez.

## Aday yapay zekâ rolleri

| ID | Aday rol | Kaynak Work | Temel başarı yönü | Statü |
|---|---|---|---|---|
| **R1** | Ortak Çalışma Tabanı Tasarımcısı | B1 | SOUL aktörlerinde ortak çalışma davranışını araştırmak, tanımlamak ve aktarım/kontrol gereksinimine çevirmek | candidate |
| **R2** | Davranış Doğrulayıcısı | B1 | Aktörün iddia edilen ortak çalışma tabanıyla gerçekten davranıp davranmadığını sınamak | candidate |
| **R3** | Davranış Teşhisçisi / Değişiklik Analisti | B1, B2 | Failure'ın doğru nedenini/katmanını bulmak ve hangi DevOS Work'ünün yeniden açılacağını belirlemek | candidate / cross-domain expansion |
| **R4** | Information Steward / Bilgi Yaşam Döngüsü Tasarımcısı | B2 | Bilginin tür/statü/otorite/provenance/lifecycle düzenini tasarlamak ve denetlemek | candidate |
| **R5** | Context & Retrieval Curator / Bağlam Kurucusu | B2 | Belirli Work + Actor + use için doğru/yeterli/güncel bilgi görünümünü kurmak | candidate |
| **R6** | Information Integrity Reviewer / Bilgi Yeterliği Doğrulayıcısı | B2 | Kaynak→statü→sürüm→seçim→exposure→use zincirinin iddiayı taşıyıp taşımadığını sınamak | candidate |
| **R7** | Role & Actor Formation Designer / Rol ve Aktör Oluşum Tasarımcısı | B3 | Work ihtiyacını role contract'a ve uygun actor oluşum/bağlama gereksinimine çevirmek | candidate |
| **R8** | Actor Qualification Reviewer / Aktör Yeterlilik Doğrulayıcısı | B3 | Belirli actor'un belirli role/scope için competence ve fit'ini sınamak | candidate |
| **R9** | Actor Governance Steward / Aktör Yetki ve Yönetişim Sorumlusu | B3 | Authority, delegation, obligation, participation ve attribution ilişkilerini meşru source/scope'a bağlı tutmak | candidate |
| **R10** | Work Formation & Planning Designer / İş Oluşum ve Yaşayan Plan Tasarımcısı | B4 | Amaç ve gelişen anlayıştan gerekli Work adaylarını keşfedip yaşayan Work/plan yapısına dönüştürmek | candidate |
| **R11** | Work Admission & Coordination Steward / İş Kabul ve Koordinasyon Sorumlusu | B4 | Candidate→admission/frontier, dependency, concurrency, coordination ve flow'u yönetmek | candidate |
| **R12** | Work Progress & Closure Reviewer / İş İlerleme ve Kapanış Doğrulayıcısı | B4 | Gerçek progress'i ve execution/verification/fitness/acceptance/parent closure ayrımlarını sınamak | candidate |
| **R13** | Environment & Capability Formation Designer / Ortam ve Kabiliyet Oluşum Tasarımcısı | B5 | Work/Actor ihtiyacını gerekli Environment capability/configuration/provisioning planına dönüştürmek | candidate |
| **R14** | Environment Operations & Readiness Steward / Ortam İşletim ve Hazırlık Sorumlusu | B5 | Environment'ın provision edilmiş, erişilebilir, healthy, yeterli ve current kalmasını yönetmek | candidate |
| **R15** | Environment Reality & Effect Reviewer / Ortam Gerçekliği ve Etki Doğrulayıcısı | B5 | Tool/runtime kaydından bağımsız actual Environment state/effect iddiasını sınamak | candidate |
| **R16** | Cross-Ground Composition Designer / Çapraz-Zemin İlişki Tasarımcısı | B6 | Exact cross-ground bindings ve composite readiness/actionability/qualification semantiğini tasarlamak | candidate |
| **R17** | Cross-Ground Control & Transition Steward / Kontrol ve Geçiş Sorumlusu | B6 | Governing basis, authority, gate, enforcement coverage ve realized transition/propagation ilişkilerini yönetmek | candidate |
| **R18** | Composition Integrity Reviewer / Birleşim Bütünlüğü Doğrulayıcısı | B6, B7 | Ground-local gerçeklerden türeyen birleşik hükmün ve Working Configuration joint readiness/fit iddiasının desteklenmesini sınamak | candidate / reused for B7 qualification |
| **R19** | Working System Formation Designer / Çalışma Sistemi Oluşum Tasarımcısı | B7 | Mission için gerekli capacity set'ini keşfedip reuse/configure/acquire/create/defer kararlarıyla yeterli Working Configuration tasarlamak | candidate |
| **R20** | Working Configuration Assembly Steward / Çalışma Konfigürasyonu Kurulum Sorumlusu | B7 | Seçilmiş configuration'ın capability sahipleri üzerinden gerçekten assemble/activate/reconfigure/retire edilmesini koordine etmek | candidate |

## Mekanik sorumluluklar — aktör/rol değildir

| ID | Sorumluluk | Kaynak Work | Statü |
|---|---|---|---|
| **M1** | Mekanik davranış sınırı / identity-role-grant enforcement | B1, B3; ileride B5/B6 | candidate requirement |
| **M2** | Information persistence / retrieval / exposure mekanikleri | B2; ileride B5/B6 | candidate requirement |
| **M3** | Work identity / admission / claim / transition mechanics | B4; ileride B6 | candidate requirement |
| **M4** | Environment provisioning / runtime / workspace / isolation substrate | B5; ileride B6 | candidate requirement |
| **M5** | Effect execution / readback / observability substrate | B5, B6 | candidate requirement |
| **M6** | Cross-ground binding / standing checks / guarded-transition substrate | B6, B7 | candidate requirement |
| **M7** | Working Configuration identity / binding / activation / lifecycle substrate | B7 | candidate requirement |

## Henüz kararlaştırılmayanlar

- Development OS'ta kaç yapay zekâ aktör örneği olacağı.
- R1–R20'nin kaç fiziksel agent/model/oturum tarafından taşınacağı.
- R1/R2/R6/R8/R12/R15/R18 gibi verification sorumluluklarının, R4/R5/R6 Information rollerinin, R7/R9 Actor-governance rollerinin, R10/R11 Work rollerinin, R13/R14 Environment rollerinin, R16/R17 cross-ground rollerinin veya R19/R20 system-formation rollerinin ileride birleşip birleşmeyeceği.
- Bağımsız doğrulama için hangi teknik/organizasyonel izolasyonun gerektiği.
- Host/runtime/topoloji.

Yeni Work açıldıkça önce mevcut rollerin sorumluluk kapsamı değerlendirilir; sırf yeni sorumluluk bulundu diye yeni rol üretilmez.
