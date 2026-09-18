# Kavram Araştırmaları ve Ortak Referans

`concepts/`, aynı sözcükle farklı şeyler konuştuğumuzda bunu fark etmek ve kaynaklarla bağlantılı yerel kullanımlar geliştirmek içindir: **“Biz bu ifadeyi şu kapsamda kullanıyoruz.”** Evrensel sözlük, nihai ontoloji, SOUL mimarisi veya agent-control katmanı değildir.

Bir terimden veya somut anlam sorusundan başlanır; araştırmada çıkan terimler, işlevler ve ilişki soruları gerektiği kadar birlikte incelenir. Yeterli zeminde ortak kullanım adayı değerlendirilir. Bütün terimleri önce araştırıp en sonunda referans oluşturma, tek bir terimi komşularından bağımsız kapatma veya her yeni kaynakla yön değiştirme zorunluluğu yoktur.

## Yeni oturumda giriş

Güncel [AGENT.md](../AGENT.md) ve gereken kontrol protokollerinden sonra:

1. [STATE.md](STATE.md): mevcut odak, iş/yetki, yayın ve durma sınırı.
2. [PURPOSE.md](PURPOSE.md): amaç ve U01 sonrası kullanıcı düzeltmesi.
3. [METHOD.md](METHOD.md): bağlantılı inceleme, yeterlilik, kaynak sadakati ve karşılıklı kullanım kabulü.
4. [PLAN.md](PLAN.md): esnek çalışma hareketleri; tarihsel P0 hazırlığı güncel iş değildir.
5. [TERM-INVENTORY.md](TERM-INVENTORY.md): ilgili başlangıç/keşif kaydı; zorunlu araştırma sırası değildir.
6. STATE'in gösterdiği çalışma: Agent için [BRIEF](research/agent/BRIEF.md) ve [U01](research/agent/U01-SOURCE-USES.md); varsa ilgili sentez/aday/referans kaydı.

Current entry/method dosyalarını tam, kaynak ve eski araştırmayı sorunun gerektirdiği derinlikte oku. Sonra mevcut soruya dön: ne zaten araştırılmış, hangi ayrım açık, komşuya neden girilecek, hangi aday veya kapsam gerçekten kabul edilmiş? Aynı araştırmayı veya P0 kurulumunu yeniden başlatma.

Bu INDEX ikinci bir STATE değildir. Bir sonraki işin aday gösterilmesi tek başına yürütme yetkisi, yöntemin kabulü de terim tanımının kabulü değildir.

## Üç kayıt düzeyi, bağlantılı çalışma döngüsü

| Düzey | Giriş | Görevi |
|---|---|---|
| 1 — Kaynak ve kavram incelemesi | [research/INDEX.md](research/INDEX.md) | Kaynak kullanımları, örnekler, karşılaşılan komşular ve açık sınırlar. |
| 2 — Birlikte değerlendirme ve adaylar | [synthesis/INDEX.md](synthesis/INDEX.md) | İlgili anlam/işlev/ilişki ayrımlarını gerekçelendirmek; yerel kullanım adaylarını tartışmak. |
| 3 — Ortak referans | [reference/INDEX.md](reference/INDEX.md) | Açık kapsamı ve karşılıklı değerlendirmesi kayıtlı yerel kullanımlara başvurmak. |

Düzeyler epistemik rollerdir; tek yönlü büyük fazlar, üç özetleme basamağı veya kavramların parça hiyerarşisi değildir. Aynı küçük bağlantılı kümede ileri/geri çalışılabilir. Her keşfedilen kelime için ayrı dosya veya yeni ad oluşturulmaz.

## Diğer alanlarla ilişki

[Research](../research/INDEX.md) ve [studies kataloğu](../research/studies/CATALOG.md) kendi teknik araştırmalarını korur. Buraya taşınmaz; gereken bulgu ve kaynağa bağlantı verilir. [Explorations](../explorations/INDEX.md) geçmiş diyalog ve geçici kullanımları korur; bugünkü anlam geçmiş metne sessizce uygulanmaz. [Repository girişi](../README.md) alanların rollerini ayırır.

İlgili soruda [EXP-002 terim notları](../explorations/EXP-002-soul-baz-yapi-ve-entelektuel-taban/reflections/TERMS.md), [Context/Memory/Harness META](../research/studies/context-memory-harness-engineering/META.md) ve [iş yönetimi METHOD](../research/studies/work-management-project-control/METHOD.md) seçici başlangıç yollarıdır. Bu bağlantılar tanım kabulü, güncel dış kaynak doğrulaması veya her oturumda hepsini okuma zorunluluğu değildir.

## Yayın ve tarihsel kayıt

Güncel yayın STATE'te, v0.2 yöntem uyarlamasının dosya bazlı kapsamı ve gerçek kontrolleri [METHOD-ALIGNMENT](checks/METHOD-ALIGNMENT-2026-09-18.md)'dedir. [SETUP-VERIFICATION](checks/SETUP-VERIFICATION.md) yalnız tamamlanmış P0 hazırlığının tarihli kanıtıdır; sonraki araştırmanın yokluğunu veya bugünkü çalışma durumunu bildirmez.

Bu alanın yöntem belgeleri yetkilendirilmiş proje çalışmasını tarif eder. Assistant davranış kurallarının canonical kaynağı AGENT ve agent/ olarak kalır.
