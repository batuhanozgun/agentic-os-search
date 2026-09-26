# EXP-006 — HANDOFF

**Amaç:** Yeni oturumun son alt örneğe veya tarihsel next-step'e değil current üst işe dönmesi.  
**Güncelleme:** 26 Eylül 2026.  
**Son tamamlanan dilim:** [S1-17](work/S1-17-consolidation-closure-audit.md), final konsolidasyon/kapanış denetimi.  
**Current:** S1-CLOSURE-READY / CANDIDATE / USER-EVALUATION-PENDING. EXP-006 açık. S1 kullanıcıca kapatılmış değildir.

## 1. Fresh-session okuma

STATE → bu HANDOFF → WORK → ACTORS → S1 master tam okunur. Kapanışın gerekçesi veya sınırı değerlendiriliyorsa S1-17'ye; somut responsibility için ilgili B veya S1 slice'ına inilir. History ve eski slice next-step'leri current yetki değildir.

## 2. Neden buradayız?

SOUL'u yaratmak için DevOS'un çalışma düzenini arıyoruz. İki geniş actor sınıfı insan + AI; insanın müşteri çekirdeği yetki + kabul. AI rolleri hazır unvanlardan değil DevOS Work'ünden türetildi. SOUL hedefi bu aşama için yeterince somutlaştırıldı; B1–B9 geliştirme alanları, R1–R25/M1–M9 ilk adayları ve sonra S1 konsolidasyonu oluştu.

DevOS'un geliştirme işi, SOUL'un gelecekteki müşteri operasyonu ve EXP-006'nın kayıt düzeni ayrı düzeylerdir. B'deki target kapasiteyi yapmak, o kapasiteyi bir örnekte elle işletmekten farklıdır.

## 3. Devralınan aday sonuç

F1 tasarlama; F2 gerçekleştirme; F3 işletim/koordinasyon; F4 yönetişim/kontrol; F5 güvence; F6 teşhis/impact/recovery yönlendirme; F7 öğrenme/adaptasyon yönlendirme; F8 araştırma/keşif/sentez.

S1-01–S1-04 üretim/inceleme/düzeltme ve aktarım problemini açtı. S1-05–S1-13 yedi familyayı ayrı ayrı sınadı. S1-14 bütün-model audit'iydi. S1-15 F8'i aday olarak ekledi; her arama F8 değildir. S1-16 F2 kapsamını ve iki F3 specialization'ını netleştirdi:

- Information Lifecycle Operations;
- Actor / Role Participation Lifecycle Operations.

S1-17 mevcut B1–B9 sorumluluklarını ve kök amacı tekrar karşılaştırdı. Yeni familya gerektiren boşluk bulmadı; iki sınırı keskinleştirdi:

1. Dosya üretmek F2 olmak için yeterli değildir; tasarım F1, araştırma raporu F8, verdict F5 olarak kalabilir. Tek işe özgü gerçekleştirme de F2 olabilir; reusable şartı yok.
2. Information/Participation işletimi yeni truth, mandate veya gerçekleşmiş effect üretmiş gibi sayılmaz. Domain kararı, kaydı, katılım geçişi, ortam işlemi ve kanıt hükmü ayrı teslimatlar olabilir.

Aynı actor birçok katkıyı taşıyabilir; aynı exact teslimatın belirsiz iki primary owner'ı olmamalıdır. Aile sayısı fiziksel ajan sayısı değildir. Kaynak karşılaştırması aynı-assistant nitel incelemedir; bağımsız davranış testi değildir.

## 4. Kapanışa hazır olan ve açık kalan

**Kapanışa hazır:** family/specialization sorumluluk konsolidasyonu; mevcut named B kapsamı, R/M lineage ve kavramsal handoff sınırları.

**Açık:** exact geliştirme işi için actual actor/bearer seçimi; competence; gerçek context/source/araç/ortam; permission/authority; activation/tetik; devir ve consumer; claim-appropriate assurance/independence; gerçek davranış ve aktarım sınaması. Bunları family tablosu kendiliğinden sağlamaz.

G1'in responsibility görünürlüğü family düzeyinde karşılandı; bütün M1–M9 mekanizmalarının gerçekten geliştirilebildiği kanıtlanmadı. R1–R25 tarihsel lineage'dır; yeni R26/R27 atamak bu açığı otomatik çözmez.

**Kaynak izi uyarısı:** S1-16 §8'deki bazı `Tam` okumalar kesilmiş toplu tool yanıtına dayanıyordu. S1-17 §7 bu iddiayı nitelendirir; alınmış dosya ile model-visible tam okuma aynı değildir. Eski etiketi yeni güven kanıtı yapma.

## 5. Sıradaki sorumluluk ve yetki

Önce S1-17 sonucu kullanıcı değerlendirmesine döner. Sonraki mantıksal aşama, bu modeli **somut bir DevOS geliştirme işi üzerinde etkin görevlendirme/devir düzenine** dönüştürmektir; bu tur o aşama yürütülmedi.

Kullanıcı devam yönü verirse bu yeni mesajla current scope birlikte değerlendirilir. Amaç yalnız kart doldurmak değil, bir sorumluluğun gerçek actor/context/tool/authority/tetik/consumer koşullarını göstermek olacaktır. Mimari, ürün, host/runtime veya ajan sayısı otomatik seçilmez.

S1 yeni somut boşluk, sınır çelişkisi veya kullanıcı yönü varsa yeniden açılır. Henüz actual runtime olmadığı için bütün familya sınıflamasını tekrarlamak gerekmez; actual yeterlik açığı da çözülmüş diye gizlenmez.
