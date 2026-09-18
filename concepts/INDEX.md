# Kavram Araştırmaları ve Ortak Referans

`concepts/`, repository'nin beşinci ana çalışma alanıdır. Amacı aynı sözcükle farklı şeyleri konuştuğumuzda bunu fark edebilmek; araştırmadaki kullanım, assistant'ın kastı ve kullanıcının anlayışı arasında başvurulabilir bir referans geliştirmektir. Hazır bir sözlük, nihai ontoloji, SOUL mimarisi veya agent-control katmanı değildir.

## Yeni oturumda giriş

Güncel [AGENT.md](../AGENT.md) ve gereken kontrol protokollerinden sonra:

1. [STATE.md](STATE.md): güncel iş, yetki, yayın durumu ve durma sınırı.
2. [PURPOSE.md](PURPOSE.md): amaç, kullanıcı düzeltmeleri ve bu programın gerekçesi.
3. [METHOD.md](METHOD.md): araştırma, karşılaştırma ve birlikte kullanım kararı arasındaki ayrımlar.
4. [PLAN.md](PLAN.md): aşamalı çalışma ve yayın kapsamı.
5. [TERM-INVENTORY.md](TERM-INVENTORY.md): yalnız ilgili gündem kaydı.
6. STATE'in gösterdiği çalışma belgesi; başlangıç adayı [Agent BRIEF](research/agent/BRIEF.md).

Bu INDEX güncel iş veya kabul durumunun ikinci kopyası değildir. Hazırlanmış brief araştırma sonucu değildir; sonraki işin listelenmesi tek başına yürütme yetkisi değildir.

## Üç seviye

| Seviye | Giriş | Görevi |
|---|---|---|
| 1 — Terim araştırmaları | [research/INDEX.md](research/INDEX.md) | İlgili kaynaklardaki kullanımları, örnekleri ve sınırları araştırmak. |
| 2 — Birlikte değerlendirme | [synthesis/INDEX.md](synthesis/INDEX.md) | Yeterince araştırılmış kullanımları karşılaştırmak; ilişkileri ve açık ayrımları göstermek. |
| 3 — Ortak referans | [reference/INDEX.md](reference/INDEX.md) | Araştırma ve karşılıklı değerlendirme sonrasında seçilen kapsamlı kullanımlara başvurmak. |

Bunlar kavramların parça hiyerarşisi veya üç özetleme basamağı değildir. Bir terim birden fazla anlama gelebilir; bir kavram birden fazla adla anılabilir. Her şey tek ağaca yerleştirilmez.

## Diğer alanlarla ilişki

[Research](../research/INDEX.md) ve [studies kataloğu](../research/studies/CATALOG.md) teknik ve kavramsal dayanakların kendi yerleridir. Buraya taşınmazlar. [Explorations](../explorations/INDEX.md) geçmiş diyalog ve geçici kullanımları korur; bugünkü anlamlar geçmiş metne sessizce uygulanmaz. [Repository girişi](../README.md) bütün alanların rollerini ayırır.

İlk yönlendirme adayları: [EXP-002 terim notları](../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/reflections/TERMS.md), [Context/Memory/Harness META](../research/studies/context-memory-harness-engineering/META.md) ve [iş yönetimi METHOD](../research/studies/work-management-project-control/METHOD.md). Bunlar başlangıç yollarıdır; güncel kaynak doğrulaması veya ortak tanım kabulü değildir. Tam corpus her oturumda yüklenmez.

Hazırlığın gerçekten yayımlanıp kontrol edildiği [STATE](STATE.md) ve [SETUP-VERIFICATION](checks/SETUP-VERIFICATION.md) üzerinden okunur. Bu alanın yöntem belgeleri yalnız bu yetkili çalışma programını tarif eder; assistant davranış kurallarının canonical kaynağı AGENT ve agent/ olarak kalır.
