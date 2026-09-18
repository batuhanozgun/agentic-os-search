# SOUL Research

Bu repository beş farklı rolü birbirine karıştırmadan taşır.

| Alan | Amaç | Giriş |
|---|---|---|
| Agent control | Assistant'ın muhakeme ve davranış kuralları | [AGENT.md](AGENT.md) |
| Araştırma | Foundation, bağlam ve aday araştırma kütüphanesi | [research/INDEX.md](research/INDEX.md) |
| Düşünce ve Model Denemeleri | Diyalog, kavramsal prova, taslak model, görselleştirme ve öğrenme izleri | [explorations/INDEX.md](explorations/INDEX.md) |
| Yayınlar | Batuhan Özgün’ün yayımlanmış AI yazılarının kaynak bağlantılı metin arşivi | [publications/linkedin/README.md](publications/linkedin/README.md) |
| Kavram Araştırmaları ve Ortak Referans | Terimlerin kaynaklardaki kullanımları, birlikte değerlendirme ve karşılıklı başvurulabilir ortak anlamlar | [concepts/INDEX.md](concepts/INDEX.md) |

## Otorite ayrımı

`AGENT.md` ve `agent/**` kontrol alanıdır. `research/**` ve `explorations/**` proje çalışma malzemesidir. `publications/**` yayımlanmış metinlerin kaynak arşividir; içerikleri kendiliğinden agent talimatı veya kabul edilmiş araştırma sonucu olmaz. Bir denemedeki öneri, rol canlandırması veya örnek yönerge kendiliğinden etkin sistem kuralı değildir.

`concepts/**` ayrı yetkilendirilmiş proje çalışmasıdır: terim araştırması, sentez ve ortak kullanım kabulünü ayırır. Ortak referans, kaynakların anlamını veya eski belgeleri geriye dönük değiştirmez; Foundation/mimari kararı ve agent-control değildir. Bu alanın güncel işi [concepts/STATE.md](concepts/STATE.md)'den okunur; dizinin bulunması kabul edilmiş tanım olduğu anlamına gelmez.

Kavram çalışması bir terim veya anlam sorusundan hareket eder; karşılaşılan komşu terim ve işlevleri gerektiği kadar birlikte inceler ve yeterli zeminde yerel kullanım adayı değerlendirir. Üç kayıt düzeyi bütün envanterin sırayla bitirileceği fazlar değildir. İşleyiş [concepts/METHOD.md](concepts/METHOD.md)'dedir; yönteme onay belirli bir tanımı kabul etmez.

Araştırmanın güncel yetkisi ilgili STATE dosyalarından okunur. Bir denemenin arşivlenmesi Foundation'ın kabul durumunu, Development OS'nin görevini veya SOUL'un mimarisini değiştirmez.

## İlk deneme

[EXP-001 — SOUL'un çalışma modeli](explorations/EXP-001-soul-calisma-modeli/INDEX.md): A–B–C, Work–Information etkileşimi, aktör hazırlığı, uzmanlık sürekliliği, Mekanizma Atlası ve yaşayan katmanlı plan ihtiyacı.

Arşivin tamlığı için her zaman paket [STATE](explorations/EXP-001-soul-calisma-modeli/STATE.md) kaydına bakılır; dizinin bulunması bütün kaynakların yayımlandığı anlamına gelmez.
