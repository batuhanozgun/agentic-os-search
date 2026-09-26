# EXP-006 — WORK

**Rol:** Üst iş haritası ve çalışma sırası.  
**Statü:** Diyalog ve araştırma çalışma haritası; Development OS mimarisi değildir.  
**Üst amaç:** SOUL'u yaratabilecek Development OS çalışma düzenini ortaya çıkarmak.  
**Güncel iş:** S1 — araştırma örnekleri ve aktör özellikleriyle rol/sorumluluk adaylarını değerlendirmek.

## Ana zincir ve katmanlar

SOUL hedefi → DevOS'un SOUL üzerinde yapacağı işler → gereken kabiliyet/sorumluluklar → yapay zekâ rolleri, mekanik destek ve insan sınırı → S1 çapraz değerlendirmesi → daha sonra DevOS yapısı ve araç seçimleri.

Başlangıçtaki altı kök iş korunur: hedefi belirlemek; gereken işleri keşfetmek; yapılabilir hâle getirmek; gerçekleştirmek; sınamak/yeniden çalışmak; zaman içinde sürdürmek. B1–B9 bunların yerine geçen liste değil, iş keşfi sırasında çıkarılmış SOUL geliştirme alanlarıdır. Bir kapasitenin gereksinimini yazmak onu gerçekleştirmek değildir.

Roller işten türetilir. Rol ailesi aynı etkin görevlendirme veya tek model çağrısı değildir; rol sayısı ajan sayısı, M sayısı servis sayısı değildir.

## Birinci seviye iş haritası

| ID | DevOS'un SOUL üzerinde yaptığı iş | Statü | Ayrıntı |
|---|---|---|---|
| B1 | Ortak entelektüel çalışma tabanını geliştirmek | İlk ayrıştırma / aday | [B1](work/B1-common-intellectual-baseline.md) |
| B2 | Bilgi kapasitesini geliştirmek | İlk ayrıştırma / aday | [B2](work/B2-information-capacity.md) |
| B3 | Aktör kapasitesini geliştirmek | İlk ayrıştırma / aday | [B3](work/B3-actors-capacity.md) |
| B4 | İş kapasitesini geliştirmek | İlk ayrıştırma / aday | [B4](work/B4-work-capacity.md) |
| B5 | Ortam kapasitesini geliştirmek | İlk ayrıştırma / aday | [B5](work/B5-environment-capacity.md) |
| B6 | Dört zeminin ilişkilerini doğru işletme kapasitesini geliştirmek | İlk ayrıştırma / aday | [B6](work/B6-cross-ground-integration.md) |
| B7 | İşe göre çalışma sistemi oluşturma ve genişletme kapasitesini geliştirmek | İlk ayrıştırma / aday | [B7](work/B7-system-formation.md) |
| B8 | Süreklilik, değişim, toparlanma ve öğrenme kapasitesini geliştirmek | İlk ayrıştırma / aday | [B8](work/B8-continuity-change-recovery.md) |
| B9 | Bütünü birleştirmek ve gerçek görevlerle sınamak | İlk ayrıştırma / aday | [B9](work/B9-integration-and-testing.md) |

İlk ayrıştırma uygulanmış veya doğrulanmış SOUL kapasitesi değildir. Eski dal dosyalarının sonraki B yönlendirmeleri tarihsel üretim anlarıdır; güncel sıra STATE/HANDOFF'tan alınır. Kullanıcının devam izni teknik doğrulama veya bütün önerilerin kabulü değildir.

## S1 — Güncel çalışma

[Yöntem, kaynak rotaları ve dilim dizini](work/S1-role-responsibility-consolidation.md).

| Dilim | Katkı / statü |
|---|---|
| [S1-01](work/S1-01-production-review-correction.md) | İnceleme ailesi, üretim–düzeltme, teşhis/karar ve sürüme bağlı kanıt; G1 fiilî geliştirme sorumluluğu açıklığı. Aday. |
| [S1-02](work/S1-02-actor-conditioned-role-purpose.md) | Aktör türü, tutarlı başarı yönü ve aktöre göre uyarlama; aile/etkin görevlendirme ayrımı. Aday. |
| [S1-03](work/S1-03-role-purpose-activation-and-transfer.md) | Ortak taban, tetiklenme, sonuç tüketimi ve birikimin geliştiren→SOUL→kurulmuş role aktarımı. Aday. |
| [S1-04](work/S1-04-read-only-reviewer-development-chain.md) | Salt-okur inceleme kapasitesinde gereksinim→tasarım→üretim/uyarlama→kurulum→sınama zinciri ve teknik gerçekleştirme görev kartı. Bir örnek eşlendi; aday. |
| [S1-05](work/S1-05-initial-role-family-draft.md) | R1–R25 için ilk rol ailesi taslağı: F1 Tasarlama, F2 Teknik Gerçekleştirme, F3 İşletim, F4 Yönetişim/Kontrol, F5 Güvence, F6 Teşhis/Toparlanma, F7 Öğrenme/Uyarlama. Aday. |
| [S1-06](work/S1-06-full-role-family-mapping.md) | R1–R25 tam eşleme; F2 birincil owner açığı; R4 dual-family; R22 sınır vakası; research/decision için ayrı aile henüz yok. Aday. |
| [S1-07](work/S1-07-verification-assurance-family.md) | F5 sınandı: R2/R6/R8/R12/R15/R18 ortak assurance familyası; specialization'lar korunur; R18 composite assurance. Aday. |
| [S1-08](work/S1-08-design-formation-family.md) | F1 sınandı: domain/system/evaluation design specialization'ları ortak familyada; R4'ün F3 ataması geri açıldı. Aday. |
| [S1-09](work/S1-09-realization-implementation-family.md) | F2 sınandı: ayrı realization/implementation başarı yönü; R1–R25'te primary owner yok; M1–M9 realization specialization yüzeyi. Aday. |
| [S1-10](work/S1-10-operations-stewardship-coordination-family.md) | F3 sınandı: R5/R11/R14/R20/R21/R25 operational specialization'lar; coordination aynı familyada; Information Lifecycle Operations specialization açığı. Aday. |

**Son kullanıcı yönü:** Yönü koruyarak somut, doğru kabul edilmeden tartışılabilecek sonuçlarla devam et.

**Bu turdaki ilerleme:** G1 yalnız yeniden tarif edilmedi; bir örnekte çıktı, bilgi/yeterlik, mevcut R karşılığı, sonraki tüketici ve kanıt bağı gösterildi. R13 tasarım, R14 kurulum/işletim, R20 koordinasyon tanımlarının yeni kod üretimini kendiliğinden sahiplenmediği korunarak teknik gerçekleştirme görevlendirmesi önerildi. Mevcut rolün koşullu genişlemesi veya aynı yeterli aktörün farklı görevlerde kullanılması açık seçeneklerdir. Yeni R26 yok.

**Dönüş:** S1-10 F3 konsolidasyonunu kullanıcıya kısa ve doğrudan sun. Sonraki çalışma F4 Yönetişim/Kontrol familyasını ve insan yetki çekirdeği sınırını sınamaktır.

## Sonraki değerlendirmelerde korunacaklar

Her sorumluluk için: neden var; ne üretir; hangi bilgi/yeterlikle; hangi tutarlı başarı yönünde; hangi araç/yetkiyle; ne zaman tetiklenir; kim devralır; hangi kanıtla sınanır?

Tasarım, üretim, kurulum, işletim ve bağımsız hüküm aynı şey değildir. Aynı görevlendirmede birleşmeleri, uzmanlık ve başarı yönü uyumuna bağlı aday tercihtir. Genel tasarımda görünmeyen teknik üretim yükü, mekanik sistem adına yazılarak kapanmaz.

S1 bitmeden mimariye geçilmez. DevOS geliştirmesi, SOUL'un gelecekteki işi ve EXP-006 kayıt düzeni ayrı kalır. Keel ve OS Architect örnektir; eski emirleri, kuyrukları ve insan kapıları alınmaz. ACTORS ilk R1–R25/M1–M9 türetimlerini korur; S1 dosyaları sonraki aday değerlendirmeyi taşır. Kabul edilmiş çalışma anlaşmaları DECISIONS'tadır.
