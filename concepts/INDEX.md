# Kavram Çalışması

Amaç, aynı sözcükle farklı şeyler konuşmamızı önleyen, dış kaynaklarla bağlantılı bir ortak anlam zemini kurmaktır: **“Biz bu ifadeyi şu kapsamda kullanıyoruz.”** Evrensel sözlük veya SOUL tasarımı oluşturulmuyor.

## Nereden devam edilir?

Güncel `main` üzerindeki [AGENT.md](../AGENT.md) ve gereken protokoller → bu giriş → [STATE.md](STATE.md) → [METHOD.md](METHOD.md) → gerektiği kadar [WORKING.md](WORKING.md) ve [SOURCES.md](SOURCES.md).

| Dosya | Tek sorumluluğu |
|---|---|
| [STATE.md](STATE.md) | Şu anki iş, yetki, durma ve devam noktası. |
| [METHOD.md](METHOD.md) | Bağlı kavramları somut kullanım üzerinden inceleme ve düzeltme yöntemi. |
| [WORKING.md](WORKING.md) | Tek çalışma taslağı: devralınan anlamlar, ilişki haritası ve açık sorunlar. |
| [SOURCES.md](SOURCES.md) | Kaynak kayıtlarına dönüş; kanıtın kapsamı ve eksikleri. |
| [HISTORY.md](HISTORY.md) | Önceki dosyaların sabit Git geçmişi, sadeleştirme ve branch durumu. |

Bu dosyayla birlikte toplam altı dosya var. Ayrı araştırma/sentez/referans klasörleri ve her tur açılan sürüm dosyaları yok. **Kaynak gözlemi, assistant'ın çalışma tercihi ve kullanıcının açık değerlendirmesi yine ayrı statülerdir; bu ayrım ayrı klasör gerektirmez.**

## Çalışmanın yönü

Bir terime takılıp kalmadan bağlı kavramlarla ilerlenir; fakat yeni kelime bulunması yeni paket açma gerekçesi değildir. Önce mevcut tanımların aynı somut cümlede ne söylediğine bakılır. Gerçek bir boşluk veya çelişki çıkarsa gereken kaynak ve komşu kavram açılır, sonra o cümleye dönülür. Terim sayısı ve dosya sayısı başarı ölçütü değildir.

Çalışma tanımlarını seçme, gerekçelendirme ve gerektiğinde birlikte düzeltme yükü assistant'tadır. Kullanıcıdan her kelime için teknik tercih veya tek tek onay istenmez. Bununla birlikte, taslakların tamamı kullanıcı tarafından benimsenmiş gibi gösterilmez.

## Sınırlar

[Studies](../research/studies/INDEX.md) teknik araştırmayı, [explorations](../explorations/INDEX.md) geçmiş konuşmaları korur; buraya kopyalanmaz. Yerel kullanım dış kaynağın anlamını değiştirmez. Bu alan Foundation, SOUL/Development OS mimarisi veya agent-control otoritesi değildir.

Güncel iş yalnız STATE'ten alınır. Geçmiş sürümlerdeki “sonraki on terim” listeleri iş sırası değildir. Eski concepts branch'leri de alternatif güncel çalışma alanı değildir; doğrulanmış durumları HISTORY'dedir.
