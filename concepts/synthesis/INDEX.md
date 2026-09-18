# Seviye 2 — Birlikte Değerlendirme ve Referans Adayları

Bu alan ilgili kullanımları, işlevleri ve ilişki sorularını karşılaştırır; ortak konuşmamız için gerekçeli yerel kullanım adaylarını taşır. Tekil raporları kısaltma, bütün envanteri tamamlama veya kavramları zorunlu bir ağaca yerleştirme aşaması değildir.

## Aktif aday

| Konu | Kayıt | Statü |
|---|---|---|
| İlk 10 bağlı terim | [CORE-TERMS-WORKING-v0.1](CORE-TERMS-WORKING-v0.1.md) | Assistant tarafından çakışma kontrolü yapılmış working local reference candidate; batch-level kullanıcı yönü/itirazı bekliyor. |

Bu batch Agent, Model, LLM, Actor, Role, Run, Session, Workflow, Tool ve Harness'i tek ilişki sistemi içinde tanımlar. Amaç tek tek terim onayı toplamak değil; tanımlar birbirini bozdukça aynı batch içinde fine-tune etmektir.

Önceki [Agent boundary adayı](AGENT-BOUNDARY-CANDIDATE-v0.1.md) tarihsel ara sentez olarak korunur; aktif karar yüzeyi değildir. Agent için geniş/dar A/B ayrımı, U03 batch'inde dar/model-yönlendirmeli çalışma tanımı seçilerek çalışma varsayımına dönüştürüldü. Bu seçim henüz `reference/` altında ACCEPTED değildir.

Bir terim ve onu anlamak için gereken birkaç komşu aynı değerlendirmede ele alınabilir. Eksik olan yalnız belirli bir ayrım ise [kaynak incelemesine](../research/INDEX.md) dönülür; komşunun bütün alanını araştırmak otomatik önkoşul olmaz.

Bir aday kayıtta gerektiği kadar şu ayrımlar geri bulunabilir olmalıdır: dayanak kaynaklar; kaynak gözlemi ile assistant yorumu; ilişki/çakışma testleri; yerel ifade ve kapsam; açık sınırlar; batch düzeyindeki kullanıcı yönü.

## Kayıt ve kabul sınırı

Working reference candidate, kabul edilmiş reference değildir. Kullanıcı tek tek tanım değerlendirmek zorunda değildir; batch'in yönünü uygun bulması, genel itiraz vermesi veya belirli çatışma göstermesi sonraki adımı belirleyebilir. ACCEPTED statüsüne geçişte hangi batch/sürümün değerlendirildiği görünür tutulur.

Güncel iş ve yetki [STATE](../STATE.md), tam işleyiş [METHOD](../METHOD.md), giriş [INDEX](../INDEX.md)'dedir. Sentez/aday bulunması SOUL veya Development OS tasarım yetkisi vermez.
