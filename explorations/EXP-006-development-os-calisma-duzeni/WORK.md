# EXP-006 — WORK

**Rol:** Üst iş haritası ve çalışma sırası.  
**Statü:** Diyalog ve araştırma çalışma haritası; Development OS mimarisi değildir.  
**Üst amaç:** SOUL'u yaratabilecek Development OS çalışma düzenini ortaya çıkarmak.  
**Güncel iş:** S1 — rol/sorumluluk family modelini konsolide etmek. S1-16 realization/lifecycle specialization sınaması tamamlandı; final S1 consolidation/closure audit sırada.

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

[S1 master](work/S1-role-responsibility-consolidation.md) current konsolidasyon yöntemini ve dilim dizinini taşır.

### Aday family review sonuçları

| Family | Sonuç |
|---|---|
| F1 — Tasarlama/Oluşturma | aday olarak ayakta; R4'ün design tarafı burada |
| F2 — Gerçekleştirme/Uygulama | ayrı başarı yönü; specialization exact realization object + domain competence üzerinden; initial R1–R25 içinde primary owner yok |
| F3 — İşletim/Stewardship/Koordinasyon | aday olarak ayakta; Information Lifecycle Operations ve Actor / Role Participation Lifecycle Operations ayrı specialization olarak netleşti |
| F4 — Yönetişim/Yetki/Kontrol | aday olarak ayakta; human mandate source ayrı tutuldu |
| F5 — Doğrulama/Güvence | aday olarak ayakta; R18 composite assurance specialization'ı |
| F6 — Teşhis/Etki Analizi/Recovery Yönlendirme | aday olarak ayakta; R3 causal diagnosis, R22 impact/recovery routing |
| F7 — Öğrenme/Adaptasyon Yönlendirme | aday olarak ayakta; actual adaptation change F1/F2/F3'e gider |
| F8 — Araştırma/Keşif/Sentez | S1-15 ile ayrı aday; esas teslimatı kaynaklı bilgi olan Work'ü taşır, ortak araştırma kabiliyetini diğer ailelerden almaz |

S1-01–S1-15 ayrıntılı analiz slice'ları work/ altında tutulur. Bunlar current sequencing authority değildir; içlerindeki “next step” cümleleri üretildikleri turun tarihsel dönüş noktalarıdır.

### Current S1 durumu

S1-14 full-model audit, S1-15 research-family testi ve S1-16 specialization sınaması tamamlandı.

Korunan/netleşen:
- F1–F8 current candidate success-direction modeli.
- F2 realization specialization'ı fixed M-list değil, exact realization object + domain competence ile oluşur.
- F3 Information Lifecycle Operations ayrı specialization.
- F3 Actor / Role Participation Lifecycle Operations ayrı specialization.
- Decision ayrı familya gerektirmiyor.
- Coordination F3 operational familyası içinde kalabiliyor.
- Aynı actor birden fazla family/specialization assignment taşıyabilir; bu semantik ayrımları silmez.

Açık:
- family → specialization → exact assignment object → actor operating profile working candidate'tır; ayrıntılı effective-assignment düzeni henüz tasarlanmadı.
- S1'in kapanışa hazır olup olmadığı final consolidation/closure audit ile sınanmadı.

**Current dönüş:** final S1 consolidation/closure audit. Bu bitmeden S1'i kapatma; closure-ready olsa bile effective-assignment aşamasını otomatik başlatma.

## Sonraki değerlendirmelerde korunacaklar

Her sorumluluk için: neden var; ne üretir; hangi bilgi/yeterlikle; hangi tutarlı başarı yönünde; hangi araç/yetkiyle; ne zaman tetiklenir; kim devralır; hangi kanıtla sınanır?

Tasarım, üretim, kurulum, işletim ve bağımsız hüküm aynı şey değildir. Aynı görevlendirmede birleşmeleri, uzmanlık ve başarı yönü uyumuna bağlı aday tercihtir. Genel tasarımda görünmeyen teknik üretim yükü, mekanik sistem adına yazılarak kapanmaz.

S1 bitmeden mimariye geçilmez. DevOS geliştirmesi, SOUL'un gelecekteki işi ve EXP-006 kayıt düzeni ayrı kalır. Keel ve OS Architect örnektir; eski emirleri, kuyrukları ve insan kapıları alınmaz. ACTORS current candidate family registry'sini ve R1–R25 lineage eşlemesini taşır; S1-14/S1-15 analiz izini korur. Kabul edilmiş çalışma anlaşmaları DECISIONS'tadır.
