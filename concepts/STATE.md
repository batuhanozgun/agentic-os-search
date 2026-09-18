# Concepts — Güncel Durum

**Tarih:** 2026-09-18. **Durum:** dosya sadeleştirmesi tamamlandı; kavram araştırması molada. Uzak branch ref'lerinin silinmesi açık kaldı. Yeni terim araştırması açılmadı.

## Son kullanıcı yönü ve yapılan düzenleme

Kullanıcı, mola değerlendirmesinden sonra `concepts/` içindeki dosya/klasör tekrarlarının ve main–branch belirsizliğinin giderilmesini istedi. Bu yetki yöntem ve kayıt düzenini sadeleştirmeyi kapsar; mevcut taslak tanımların kabulü veya SOUL tasarım kararı değildir.

Çalışma yüzeyi altı düz dosyaya indirildi: [INDEX](INDEX.md), [METHOD](METHOD.md), bu STATE, [WORKING](WORKING.md), [SOURCES](SOURCES.md), [HISTORY](HISTORY.md). Eski 23 dosyanın tamamı sabit bir önceki commit üzerinden geri bulunabilir. Ayrıntı ve branch incelemesi HISTORY'dedir; burada tanım ve harita kopyası tutulmaz.

## Bilinen durum

- WORKING, önceki v0.4'ün 40 numaralı maddesini ve Task alt kullanımını devralan **incelenecek taslaktır**; 40 kesinleşmiş anlam veya kullanıcının tek tek kabulü değildir.
- Kaynak gözlemleri, yerel tercihler ve sınanmamış iddialar SOURCES üzerinden ayrılır. Bu bakım dış kaynakların yeniden doğrulaması değildir.
- Bütün concepts branch uçlarının inceleme tabanı olan `4d849afc2e8b6ef6173957e0923606290912da1e` main geçmişinde bulunduğu doğrulandı. Main dışında kalmış concepts commit'i ve açık PR saptanmadı.
- **Uzak branch adlarının fiziksel silinmesi tamamlanmadı:** bağlı arayüz bu işlemi sağlamıyor. Dokuz eski branch HISTORY'de listelenir; yeni branch açılmadı. Başka araştırmaların branch'lerine dokunulmadı.

## Devam noktası

Yeni bir onlu liste üretme. Kullanıcı kavram çalışmasını yeniden sürdürdüğünde mevcut taslağı şu somut kullanımlar üzerinde incele: “Agent'ın modelini değiştirelim”, “Aynı agent yeni oturumda devam etsin”, “İşi bitirdi; yayımlayabilir.” Bunlar henüz yapılmış testler değildir ve yeni bir SOUL mimarisi kurmak için kullanılmaz.

Assistant, tanım ve ilişki seçimlerini kendisi gerekçelendirip düzeltebilir. Belirsizliği çözmek için bütün komşu alanların araştırılmasını veya her terimin kullanıcı tarafından onaylanmasını bekleme. Yalnız somut kullanımın gösterdiği eksikliği aç; kaynağa geri dön; aynı cümleyi yeniden açıkla.

**Bu turun dönüş koşulu:** sadeleşmiş main içeriğini, korunan geçmişi, gerçek kontrolleri ve tamamlanamayan branch silme işini kullanıcıya bildirmek. Bu bakımda söz konusu kullanım incelemeleri yapılmadı; yeni çalışma veya kabul edilmiş tanım üretilmedi.

## Yayın sınırı

Bu kayıt yalnız bulunduğu `main` sürümü için günceldir. Yayın, eski main'i parent alan tek commit'in force kullanılmadan ilerletilmesiyle yapılır; eşzamanlı değişiklik varsa önce uzlaştırılır. Kendi commit kimliği tahmin edilmez. Gerçek commit ve kapsam Git geçmişinden geri bulunur. Kontrol kapsamı HISTORY'de tutulur.
