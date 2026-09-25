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

## Mekanik sorumluluklar — aktör/rol değildir

| ID | Sorumluluk | Kaynak Work | Statü |
|---|---|---|---|
| **M1** | Mekanik davranış sınırı / enforcement | B1; ileride B5/B6 | candidate requirement |
| **M2** | Information persistence / retrieval / exposure mekanikleri | B2; ileride B5/B6 | candidate requirement |

## Henüz kararlaştırılmayanlar

- Development OS'ta kaç yapay zekâ aktör örneği olacağı.
- R1–R6'nın kaç fiziksel agent/model/oturum tarafından taşınacağı.
- R1/R2/R3 veya R4/R5/R6'nın birleşip birleşmeyeceği.
- Bağımsız doğrulama için hangi teknik/organizasyonel izolasyonun gerektiği.
- Host/runtime/topoloji.

Yeni Work açıldıkça önce mevcut rollerin sorumluluk kapsamı değerlendirilir; sırf yeni sorumluluk bulundu diye yeni rol üretilmez.
