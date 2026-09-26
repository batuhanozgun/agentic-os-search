# EXP-006 — WORK

**Rol:** Üst iş haritası ve çalışma sırası.  
**Statü:** Diyalog ve araştırma çalışma haritası; Development OS mimarisi değildir.  
**Üst amaç:** SOUL'u yaratabilecek Development OS çalışma düzenini ortaya çıkarmak.  
**Güncel iş:** S1-17 kapanış denetimi tamamlandı. S1 family/specialization konsolidasyonu CLOSURE-READY / CANDIDATE; kullanıcı değerlendirmesi bekleniyor. Sonraki aşama başlatılmadı.

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

## S1 — Current aday konsolidasyon sonucu

[S1 master](work/S1-role-responsibility-consolidation.md) yöntem ve dilim dizinidir. [S1-17](work/S1-17-consolidation-closure-audit.md) kapanış gerekçesi, kapsam matrisi, karşı vakalar ve kanıt sınırıdır.

| Family | Sonuç |
|---|---|
| F1 — Tasarlama/Oluşturma | Gerekçeli uygulanabilir tasarım; R4'ün design tarafı burada |
| F2 — Gerçekleştirme/Uygulama | Exact realization object + domain competence; yalnız M listesi, dosya uzantısı veya reusable niteliğiyle tanımlanmaz |
| F3 — İşletim/Stewardship/Koordinasyon | Current operasyon; Information Lifecycle ve Actor/Role Participation Lifecycle ayrı specialization'lar |
| F4 — Yönetişim/Yetki/Kontrol | Mandate, delegation ve governed-effect sınırı; human mandate source ayrı |
| F5 — Doğrulama/Güvence | Evidence-bounded hüküm; R18 composite assurance; üretici self-check bağımsız kanıt değil |
| F6 — Teşhis/Etki Analizi/Recovery Yönlendirme | Causal diagnosis ve impact/recovery routing; actual recovery ilgili familyaya gider |
| F7 — Öğrenme/Adaptasyon Yönlendirme | Experience→reusable change/no-change yönü; actual değişim F1/F2/F3'e gider |
| F8 — Araştırma/Keşif/Sentez | Esas bilgi teslimatı; diğer familyaların ortak araştırma kabiliyetini almaz |

S1-01–S1-17 ayrıntılı dilimler work/ altında korunur; eski next-step ifadeleri current sequencing authority değildir.

### Kapanış kapsamı

S1-17, mevcut B1–B9'daki 100 adlandırılmış C sorumluluğunu, altı kök işi ve R1–R25/M1–M9 lineage'ını karşılaştırdı. Yeni familya gerektiren boşluk bulmadı. Bu sayım evrensel kapsam, runtime correctness veya görev başarısı değildir.

F2 dosya üretimiyle eşitlenmez; tasarım/araştırma/verdict kendi ailesinde kalabilir. F3 kayıt/katılım işlemi, bilginin doğruluğu, grant'ın meşruluğu veya gerçek effect'in yerine geçmez. Current registry bu sınırları taşır.

**S1 sonucu:** family/specialization konsolidasyonu kapanışa hazır; kullanıcı kabulü ve nihai kadro değil. **EXP-006 açık kalır.**

### Sonraki mantıksal çalışma — henüz başlamadı

Bu modeli somut DevOS geliştirme işinde etkin görevlendirme ve devir düzenine dönüştürmek: exact iş/teslimat; gereken competence/source/context; actual actor ve Environment; tools/permission/authority; trigger; handoff/consumer; assurance ve independence.

Bu gerçek yükler S1'den sonraki işe devredilir, çözülmüş sayılmaz. Kullanıcı yönü olmadan yeni aşama, ajan sayısı, topology, host/runtime veya mimari seçimi başlatılmaz.

## Sonraki değerlendirmelerde korunacaklar

Her sorumluluk için: neden var; ne üretir; hangi bilgi/yeterlikle; hangi tutarlı başarı yönünde; hangi araç/yetkiyle; ne zaman tetiklenir; kim devralır; hangi kanıtla sınanır?

Tasarım, üretim, kurulum, işletim ve bağımsız hüküm aynı şey değildir. Aynı görevlendirmede birleşmeleri, uzmanlık ve başarı yönü uyumuna bağlı aday tercihtir. Genel tasarımda görünmeyen teknik üretim yükü, mekanik sistem adına yazılarak kapanmaz.

DevOS geliştirmesi, SOUL'un gelecekteki işi ve EXP-006 kayıt düzeni ayrı kalır. Keel ve OS Architect örnektir; eski emirleri, kuyrukları ve insan kapıları alınmaz. Kabul edilmiş çalışma anlaşmaları DECISIONS'tadır. S1-16'nın okuma-izi tamlık iddialarının current qualification'ı S1-17 §7'dedir; kesilmiş temsil tam kaynak sayılmaz.
