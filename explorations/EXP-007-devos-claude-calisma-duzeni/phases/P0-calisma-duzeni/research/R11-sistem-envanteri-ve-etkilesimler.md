# R11 — Sistem envanteri ve alt sistemler arası etkileşim

**Tür:** Alt ajan araştırma notu (model çıktısı). EXP-007 P0.3, 27 Eylül 2026. Salt okuma kısıtıyla üretildi; yazılan tek dosya budur.
**Görev tanımı:** [briefs/R11](../briefs/R11.md); ortak kurallar [briefs/ORTAK](../briefs/ORTAK.md).
**Beslediği karar:** METHOD v1'in kapsamı, yani "arabada hangi sistemlerin bulunması gerektiği".
**Kullanım sınırı:** Bu not bir envanter ve etkileşim haritasıdır. Hiçbir bileşenin bu ortamda çalıştığını göstermez. Bağlam, bellek ve kalıcı rollerin ayrıntılı standardı R07–R10'un konusudur; burada envanter düzeyinde ele alındılar. Bu not R07–R10'u okumadı.

## 0. Soru, kaynaklar, okuma kapsamı ve kanıt dili

### 0.1 Soru

Bir ana oturumun (Claude Code) alt ajanlarla çalıştığı, bir insan müşterinin (Batu) amaç, yetki ve kabulü elinde tuttuğu, uzun soluklu, çok oturumlu, çok ajanlı bir tasarım işini yürüten çalışma sisteminin standart seviyede hangi alt sistemlere ihtiyacı var? Bu alt sistemler birbirini nasıl etkiliyor? Bir alt sistemde "yeterli" görünen hangi seçim başka bir alt sistemi yetersizleştiriyor?

### 0.2 Kaynaklar ve okuma kapsamı

Yollar repo köküne göredir. EXP-006 dosyaları `origin/main` (`ed2bf6e`) üzerinden okundu; B2, B8 ve B9'un çalışma ağacındaki haliyle `origin/main` hali aynıdır (`git diff HEAD origin/main` bu üç dosyayı listelemedi).

| Kaynak | Kapsam |
|---|---|
| `briefs/ORTAK.md`, `briefs/R11.md` | tam |
| EXP-007: README, STATE, DECISIONS, P0 README; `sources/conversation/` U001–U005, A001–A003, INDEX | tam |
| R01 (ortam) | kısmi: üç belge ekseninin araştırmacı özetleri ve iddiaları, repo ekseni, loopinance ekseni ve eksik-arayıcı tam; doğrulayıcı alt bölümleri (satır 113–226, 339–458, 559–654) okunmadı |
| R02, R03, R04, R05, R06 | tam |
| `research/studies/agentic-ai-systems-roadmap/`: INDEX, META, STATE, INITIAL-ASSESSMENT, SOURCE-VISUAL | tam; görsel dosyası (`source/*.jpg`) açılmadı, transkripsiyonu kullanıldı |
| `research/soul-foundations/`: STATE, INDEX; `08_…/CASE-AUDIT.md`, `DISCUSSION-HANDOFF.md`, `REUSE.md` | tam |
| `research/studies/gstack/CORE.md` | tam |
| `research/studies/ecc/`: META, INDEX | tam; CORE kısmi (§1–3.1, §7–10); `notes/32-…` kısmi (§1–4) |
| `research/studies/anthropic-ai-native-sdlc-playbook/`: META | tam; 01 kısmi (§2–4, §7.2–7.5, §11–12, §17–19); 04 kısmi (F2, F9, F10, F13, F14, F16–F18); 03 yalnız başlıklar |
| `research/studies/multi-agent-patterns/SOUL-DEVELOPMENT-OS-ASSESSMENT.md` | kısmi (§6 paralellik uyarısı ve birleştirme, §7 yönetici, §9 insan, §12 C1–C9) |
| `research/studies/CATALOG.md`; `concepts/` INDEX, STATE, CHARTER | kısmi (katalog satırları, CHARTER'ın amaç ve "iki risk" bölümü) |
| EXP-004: `artifacts/MS01-SOUL-WORKING-SYSTEM-DRAFT.md`, `MS01-COVERAGE-AND-OPEN-MECHANISMS.md` | tam |
| EXP-004: T08 (§1–3), T14 (§1–4), QUALIFICATIONS (Q12–Q16), `checks/` REPAIR, FIDELITY, HISTORICAL-FIDELITY-T08 (baş kısımları), USER-MESSAGES U015–U016 | kısmi |
| EXP-006 (`origin/main`): ACTORS, `work/P2-01…`, `work/P3-01…`, `work/B2…`, `work/B8…`, `work/B9…` | tam |
| EXP-005: `reflections/LESSONS-AND-OPEN-QUESTIONS.md` | tam; `sources/conversation/08-…` kısmi (U043–A044) |
| `AGENT.md` | kısmi (satır 80–160, rota kaydı); veri olarak incelendi, uygulanmadı. Protokol dosyalarının yalnız satır sayısı alındı |
| `batuhanozgun/loopinance_v2@07cd81b`: `docs/arsiv/ilk-plan-2026-09-24.md`, `docs/DEFO_MODELI.md` | tam; GitHub MCP okuma aracıyla, 27.09.2026 |
| R07–R10 görev tanımları ve notları | okunmadı (paralel çalışma; bu notun girdisi değil) |
| Kanon deposu (`loopinance-claude-code`), gstack/ECC sentezleri, CMH, work-management, superpowers, Batu'nun makaleleri | okunmadı; yalnız R01, R03 ve R05'in aktardığı kadarıyla kullanıldı |

Web'e ayrıca gidilmedi. Claude Code hakkındaki belge iddiaları R01'den alındı; R01'in ajanları code.claude.com sayfalarına 26.09.2026'da erişti. Bu iddiaları yeniden doğrulamadım. Yalnız ortam değişkenlerini ve depo yapılandırmasını kendim gözledim [K16].

### 0.3 Kanıt dili

- **Etiketler:** kaynak diyor / gözledim / çıkarım / varsayım / bilinmiyor.
- **Kanıt türleri** (güçten zayıfa değil, türe göre):
  - Batu'nun sözü (birebir kaynak);
  - repo olayı: repoda kayıtlı gerçek bir olay; kaydı çoğunlukla aynı asistan tuttu;
  - tedarikçi belgesi (Anthropic);
  - ürün kaynağı okuması: açık kaynak bir sistemin kaynağını okuyan çalışma; sistem çalıştırılmadı;
  - kavramsal analiz: Foundation, EXP-004, EXP-006; aynı asistanın akıl yürütmesi;
  - alt ajan raporu (R01–R06): ikincil kaynak;
  - gözlem: bu oturumda benim gördüğüm.
- **Bağımsız ölçüm yok.** Envanterdeki hiçbir mekanizmanın canlı ajanlarla etkinliği ölçülmemiş. R05'in tespiti burada da geçerli: "No study measured how well any of these mechanisms work with live agents."
- Her iddianın kaynağı, kısa alıntısı, etiketi ve kanıt türü **Ek A — Kanıt kaydı**'ndadır. Metinde `[Kxx]` ile anılır. Claude Code ile ilgili kayıtlarda cloud oturumuna uygulanıp uygulanmadığı ayrıca yazılıdır.

## 1. Kısa sonuç

1. **Hipotezdeki 18 alt sistemin hiçbiri kanıtsız değil; hiçbiri çıkarılmadı.** Ama dört yapısal düzeltme gerekiyor, envanter 21 alt sisteme çıkıyor (§2):
   - **İhtiyaç ve kapsam keşfi**, plan yönetiminden ayrıldı. Keşif hatası ile plan hatası farklı bozulur ve farklı yakalanır: plan öz-denetimi yalnız plandaki işi görür [K79]. Repodaki üç olay keşif hatasıdır [K38, K41, K52].
   - **Orkestrasyon ve bütünleştirme**, kalıcı rollerden ayrıldı. Rol yapısı durağan bir tasarım nesnesidir; dağıtma, paralellik ve birleştirme ise işleyiştir. Birleştirme ayrıca bozulabilir: parçalar sağlamken bütün yanlış olabilir [K76].
   - **Muhakeme disiplini ve bilinen ajan kusurları** eklendi. Batu "alt ajanlar nasıl düşünürdü" diye sordu [K03]. Repo bu işi zaten ayrı bir katmanda yürütüyor: AGENT.md'nin R01/R02/R06 rotaları [K78] ve loopinance'ın defo modeli [K33].
   - **Terim ve ortak dil**, "anlam bütünlüğü: kaynak sözü, terim ve özet sadakati" olarak genişletildi. Terim kayması, Batu'nun sözünün parafraza dönüşmesi ve özetlerde nitelik kaybı aynı mekanizmadır: anlam her yeniden ifade edilişte kaybolabilir [K49, K50, K54, K77].
   - Ayrıca "Ortam ve araçlar" yapılandırma yönetimini içerecek biçimde genişletildi.
2. **Beş repo olayının dördünde hatayı Batu yakaladı ya da onarımı Batu'nun müdahalesi başlattı:**
   - soru bankası [K41];
   - EXP-005'teki devir [K35];
   - EXP-006'daki dokuzu aşkın düzeltme [K53];
   - EXP-004'teki arşiv: asistan sadakat kaybını T08'de kendisi fark etti, ama onarım Batu'nun U016 talebine kadar bekledi [K54].

   Kanonda ise 54 günlük duraklamayı otomatik bekçi söylemedi. Duraklama, yeni düzene geçilirken yazılan geriye dönük değerlendirmede ortaya çıktı; Batu o düzende zamanlayıcıydı [K25, K34].

   Aynı modelden türeyen denetçiler aynı kör noktayı paylaşır [K106]. Bu yüzden Batu'nun dikkati bugün sistemin tek "aynı model olmayan" denetim kanalıdır. "Batu ile iş birliği" alt sistemi bir konfor eki değil, güvenlik alt sistemidir; Batu'nun masaj örneğinin bu sistemdeki karşılığı budur (çıkarım; olaylara dayalı).
3. **Bozulmalar en çok kalite güvencesinde, Batu'da, planda ve süreklilikte toplanıyor** (§4.3).
   - Giriş sayıları: KG 12, Batu 11, plan 9, süreklilik 9.
   - Olayla desteklenen 44 kenarın 10'u Batu'da bitiyor. Başka alt sistemlerin zayıflığı sonunda Batu'nun iş yükü olarak görünüyor.
   - Olayla desteklenen çıkışlarda öne çıkanlar: kayıt ve bilgi mimarisi (5) ile ihtiyaç ve kapsam keşfi (4). Bu ikisi METHOD v1'de "şasi" gibi ele alınmalı.

   Çıkış sayıları benim numaralandırma tercihimi yansıtır, ölçüm değildir. Bir seçim etkisi de var: Batu'nun fark etmediği hatalar büyük olasılıkla kayda hiç geçmedi (çıkarım).
4. **Hız varsa fren de olmalı; bu artık somut.** Sürekli yetki (K-002) kendiliğinden geçiş verir. Bunun freni ilerleme ölçüsü ve takılma alarmıdır. Kanonda bekçi 742 kez koştu ama 54 günlük duraklamayı söylemedi; çünkü ilerlemeyi değil canlılığı ölçüyordu [K25].
5. **A003 (v0) 21 alt sistemin 3'ünü "nasıl" düzeyine yakın, 16'sını kısmen kuruyor, 2'sini hiç kurmuyor** (kalıcı roller ve maliyet; §6). v0'ın güçlü olduğu yerler, dayandığı R02–R06 okumalarının odaklandığı yerlerle örtüşüyor. Batu'nun adını koyduğu bağlam, bellek ve kalıcı roller ise en zayıf yerler (çıkarım).
6. **Karşı ağırlık: standart seviye, her alt sistem için ayrı dosya, ajan ya da tören demek değildir** [K42, K43, K57, K76].
   - Loopinance'ın beşinci düzeni, önceki dördünün "kendi ağırlığı altında" durduğunu kaydediyor [K28].
   - Defo modeli "hiç koşulmamış töreni önceden inşa etme" diyor [K33].

   Bu yüzden envantere "yöntemin ağırlık bütçesi" ve "sadeleştirme" bileşenleri de girdi. Hız için fren neyse, standart seviye için hafiflik de odur.
7. **v0'daki bazı seçimler tam Batu'nun tarif ettiği türden:** tek başına makul, bütünde başka bir sistemi zayıflatıyor. Örnekler:
   - ana oturumun az okuması;
   - tek soruluk geçici alt ajanlar;
   - üç tekrar kuralı;
   - aynı model karşı-okumanın doğrulama sayılma riski;
   - tek ekranlık durum dosyası.

   §5'te 20 örnek var; her biri için dengeleyici bileşen verildi.
8. **Kanıt gücü sınırlı.** Kanıtların çoğu aynı asistanın kaydettiği repo olayları, tedarikçi belgeleri, kaynağı okunmuş ama çalıştırılmamış sistemler ve aynı asistanın kavramsal analizleridir. Envanter "bu bileşenler olmadan şu bozulur" der. "Bu bileşenler varken bozulmaz" diyemez.

## 2. Başlangıç hipotezinin sınanması

### 2.1 Karar tablosu

| # | Hipotezdeki alt sistem | Karar | Gerekçe ve kanıt |
|---|---|---|---|
| 1 | Yönetişim ve yetki | korundu (S1) | K-002 sürekli yetki, karar katmanları, yükseltme. Repodaki durma kuralları özerkliği yetkiden bağımsız olarak durduruyor [K88]. |
| 2 | Metodoloji ve yaşam döngüsü | korundu (S3); "ağırlık bütçesi" ve "tören orantısı" eklendi | Harita yokluğu EXP-006 kaymasının birinci nedeni [K46, K110]. Önceki düzenler kendi ağırlığı altında durdu [K27, K28]. |
| 3 | Plan ve iş yönetimi | **bölündü**: iş keşfi S4'e çıktı; kalan kısım S5 | Plan öz-denetimi yalnız plandaki işi görür [K79]. Keşif hatasını plan mekanizmaları yakalamaz: EXP-005 [K38], soru bankası [K41], EXP-006 rol türetimi [K52]. EXP-004 de keşfi ilk açık mekanizma (G01) olarak ayrı adlandırdı [K60]. |
| 4 | Bağlam yönetimi | korundu (S7) | Batu'nun açık gereksinimi [K01/K-007]. Ortamda %80 otomatik sıkıştırma [K16, K18]. |
| 5 | Bellek yönetimi | korundu (S8); sınırı S9'dan ayrıldı | Bellek, neyin hangi otoriteyle hatırlanıp nasıl geri çağrılacağının politikasıdır; kayıt mimarisi bunun yapısıdır. B2 bu iki başarı yönünü ayırır [K63]. Cloud'da auto memory taşınmaz [K20]. |
| 6 | Bilgi ve araştırma kullanımı | korundu, yeniden adlandırıldı: "Araştırma birikiminden yararlanma" (S6) | Keşif kısmı S4'e gitti. Kalan kısım, bilginin doğru anda kullanılması ve izinin tutulmasıdır. Foundation "yeterlik, bulunabilirlik, uygulama ayrı sorular" der [K41]. |
| 7 | Roller ve ajanlar | **bölündü**: kalıcı roller (S11) + orkestrasyon ve bütünleştirme (S12) | Batu kalıcı rol yapısı istedi [K02]. Dağıtma, paralellik ve birleştirme ise ayrı bozulan işleyişlerdir. Yönetici tek tek sağlam dönüşleri yanlış bütüne birleştirebilir [K76]. Paralellik inceleme kapasitesini aşabilir [K72]. |
| 8 | Ajanlar arası arayüzler | korundu (S13) | Görev tanımı ve dönüş şeması [K79, K101]. |
| 9 | Kalite güvencesi ve doğrulama | korundu (S14) | Öz-onay kayması [K47]; tamamlanma katları [K69]. |
| 10 | Süreklilik ve kurtarma | korundu (S18) | VM kaybı [K19], sıkıştırma [K18], EXP-005 devir hatası [K35]. |
| 11 | Gözlemlenebilirlik ve ilerleme | korundu (S17) | 742 koşu [K25]. |
| 12 | Öğrenme ve uyarlama | korundu (S21); "sadeleştirme" ve "yöntemin sınanması" eklendi | Yazılı kural davranışa dönüşmedi [K48]. "More harness ≠ better harness" [K62]. |
| 13 | Ortam ve araçlar | genişletildi: "Ortam, araçlar ve yapılandırma" (S19) | CLAUDE.md, `.claude/agents`, skills ve hook'lar yöntemin taşıyıcısıdır. Yüklenmezlerse ya da kaymaya uğrarlarsa yöntem kâğıtta kalır [K16, K17, K72 (F16), K73 (DP-01)]. |
| 14 | İnsan iş birliği | korundu, yeniden adlandırıldı: "Batu ile iş birliği" (S2) | Tek insan aktör; güvenlik işlevi (§1 madde 2). |
| 15 | Maliyet ve kaynak | korundu (S20) | Paylaşılan limitler [K22]. Harcanan 4,1 M token [K81]. Ölçülen maliyetin anlamı tüketiciye göre değişebilir [K74]. |
| 16 | Güvenlik ve bütünlük | korundu (S16) | Bu alt ajanın araç listesinde durum değiştiren araçlar görünüyor [K24]. Repodaki bayat talimatlar kaymaya yol açabilir (K-004). |
| 17 | Terim ve ortak dil | **genişletildi ve yeniden adlandırıldı**: "Anlam bütünlüğü: kaynak sözü, terim ve özet sadakati" (S10) | Terim kayması [K50], Batu'nun sözünün parafraza dönmesi [K49], arşivde özet kaybı [K54] ve devir özetinde nitelik kaybı [K55, K56] aynı mekanizmadır. Batu'nun concepts programı bu riski ayrıca adlandırıyor [K77]. AGENT.md'de ayrı bir rotası var (R05) [K78]. Tek başına "sözlük" bu olayların üçünü karşılamaz. |
| 18 | Kayıt ve bilgi mimarisi | korundu (S9); "yayılım kontrolü" ve "hijyen sahipliği" eklendi | Aynı durumun 5–7 dosyada kopyalanması [K49]; Foundation'da çelişen STATE'ler [K86]; tek karar değişince 14 spec'in yeniden yazılması [K31]. |
| — | **yeni** | **Muhakeme disiplini ve bilinen ajan kusurları** (S15) | Batu'nun U003 sorusu [K03]. Repo bu işi ayrı bir katmanda yürütüyor: AGENT.md R01/R02/R06 [K78]. Loopinance'ın en değerli çıktısı olarak anılan defo modeli [K33]. gstack'in on bir alt sisteminden biri "investigation / causal control" [K67]. Kalite güvencesi çıktıyı sonradan sınar; bu alt sistem üretim sırasındaki düşünmeyi korur. |

### 2.2 Ayrı alt sistem yapılmayan adaylar

Aşağıdakiler gerçek ihtiyaçlar, ama kendi başına ayrı bir bozulma yüzeyi oluşturmuyorlar. Bu yüzden ilgili alt sistemin bileşeni oldular:

- **Risk ve varsayım yönetimi** → S5 bileşeni (varsayım ve risk kaydı) ile S15 bileşeni (karar-kritik varsayım disiplini). Gerekçe: bu işteki riskler çoğunlukla epistemik (çöken varsayım) ya da operasyonel (VM kaybı, limit). Operasyonel olanların sahibi S18 ve S20 [K110, K15]. Dış metodolojilerin (R08) ayrı bir risk alt sistemi önermesi olası; P0.4'te karşılaştırılmalı.
- **Hata teşhisi** → S21 (olay sınıflandırması) ve S18 (hata türüne göre kurtarma). B8 ve P2-01 teşhisi, olaydan kurtarmayı ve yöntem değişikliğini ayrı tutar; teşhis ikisine de hizmet eder [K61, K65].
- **Yayın ve teslim** (main'e birleştirme, yayın, geri okuma) → S9 (dal ve yayın politikası) ve S18 (devir kimliği) [K39, K54, K87].
- **Önyükleme** (CLAUDE.md, oturum açılışı) → S19 (yükleme doğrulaması) ve S18 (açılış protokolü) [K16, K17].
- **Dış hatlarla koordinasyon** (EXP-006 ChatGPT hattı) → S1 (hatlar arası otorite) ve S9 (dal politikası). U005'teki birleştirme çakışması bunun somut örneği [K87].
- **Ritim ve zamanlama** → S3 (ritimler) ve S18 (uyandırma mekanizması).

### 2.3 Tasarım ilkesi: alt sistem, dosya, ajan ve tören farklı şeylerdir

Envanter işlevleri sayar; dosya, ajan ya da tören sayısı çıkarmaz.

- Foundation: "A branch is not a mandatory service, file or agent" [K42].
- MS01: "K1–K7 işlev kimlikleridir, yedi zorunlu ayrı process/agent değildir" [K57].
- Çok ajanlı örüntüler çalışması: korunan bir gereksinimi olmayan karmaşıklık şüphelidir [K76].
- Foundation REUSE aynı cümlede iki yönü de korur: "a simpler arrangement is not adequate merely because it is simple" [K43].

21 alt sistemin çoğu birkaç şablon alanı, bir kontrol sorusu ya da bir kayıt satırıyla karşılanabilir. Bu notun iddiası şudur: her birinin *sahibi ve karşılığı* olmalıdır. Ayrı bir ajan ya da dosya iddia edilmez.

### 2.4 Nihai envanter: 21 alt sistem, altı grup

Gruplar, araba benzetmesindeki "aktarma, fren, güvenlik, konfor" gibi işlev kümeleridir. Katman değildirler. Yol haritası çalışmasının uyarısı geçerli: yönetişim, gözlem ve doğrulama sona eklenen katmanlar değil, her katmanı kesen denetimlerdir [K70].

| Grup | Alt sistemler |
|---|---|
| A. Yön ve yetki | S1 Yönetişim ve yetki · S2 Batu ile iş birliği |
| B. İşin akışı | S3 Metodoloji ve yaşam döngüsü · S4 İhtiyaç ve kapsam keşfi · S5 Plan ve iş yönetimi · S6 Araştırma birikiminden yararlanma |
| C. Bilgi taşıma | S7 Bağlam yönetimi · S8 Bellek yönetimi · S9 Kayıt ve bilgi mimarisi · S10 Anlam bütünlüğü |
| D. Aktörler | S11 Kalıcı roller · S12 Orkestrasyon ve bütünleştirme · S13 Ajanlar arası arayüzler |
| E. Kesişen denetimler (fren ve güvenlik) | S14 Kalite güvencesi ve doğrulama · S15 Muhakeme disiplini ve ajan kusurları · S16 Güvenlik ve bütünlük · S17 Gözlemlenebilirlik ve ilerleme |
| F. Dayanıklılık ve evrim | S18 Süreklilik ve kurtarma · S19 Ortam, araçlar ve yapılandırma · S20 Maliyet ve kaynak · S21 Öğrenme ve uyarlama |

**Kapsam yoklayıcılarıyla çapraz kontrol** (çıkarım). Her yoklayıcının öğeleri bu 21 alt sistemden birine ya da birkaçına düştü; karşılıksız öğe kalmadı:

- Yol haritası görselinin 5 katmanı ve 11 kutusu [K70];
- Foundation'ın dört zemini ve bileşimi: bağlama, statü, kontrol, geçiş/yayılım, geri bildirim/uyarlama [K42];
- gstack'in 11 alt sistemi [K67];
- ECC'nin mekanizma notları [K75];
- playbook'un A–G katmanları [K71];
- MS01 K1–K7 ve G01–G07 [K57, K60];
- EXP-006 M1–M9 [K64].

Karşılığı en zayıf öğeler de var. Bunlar SOUL üretim ortamına özgü, bu tasarım işinde düşük öncelikli:
- yol haritasının "data privacy controls" ve "horizontal scaling" kutuları;
- gstack'in "browser runtime" ve "deploy/canary" alt sistemleri.

## 3. Nihai envanter

**Nasıl okunur:** Her alt sistem için önce amaç, sonra standart seviyedeki bileşenler, en sonda alt sistem zayıfsa nelerin bozulduğu verilir. Her bileşen için dört şey yazılıdır: ne işe yaradığı, yokluğunda neyin bozulduğu (başka alt sistemler dahil, "→ Sx"), bedeli ve hangi koşulda gerçekten gereksiz olduğu. "Gereksiz: –" o bileşenin bu işte hiçbir koşulda düşürülemeyeceğini söyler. Kanıtlar Ek A'dadır.

Bileşenlerin çoğu bu notun **çıkarımıdır**: kaynaklardaki mekanizmaların bu işe uyarlanmasıdır. Kaynakta doğrudan bu biçimde geçenler kanıt sütununda işaretlidir. Claude Code'a bağlı bileşenlerde cloud geçerliliği Ek A'daki kayıttadır.

### Grup A — Yön ve yetki

#### S1 — Yönetişim ve yetki

**Amaç:** Kimin neye karar verebileceğini, Batu'nun yetkisinin nasıl devredildiğini ve sınırın nerede olduğunu açık, kayıtlı ve oturumlar arası geri kazanılabilir tutmak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Karar hakları tablosu (mekanik / tercih / amaç-kapsam-ölçüt katmanları; kabul, erişim, P4 durağı) | "Kim karar verir" her seferinde yeniden tartışılmaz | Ya her şey Batu'ya gider (→S2), ya Claude Batu adına amaç değiştirir (→S5) | Bir kez yazılır; değişince bakım | Tek oturumluk salt okuma işinde | K15, K113, K112 |
| Sürekli yetki kaydı (geçişler, duraklar, yükseltme tetikleri, bütçe, izinli denemeler; birebir kaynağa bağlı) | Yeni ya da uyandırılmış oturum yetkiyi repodan çözer | Oturum fail-closed durur ya da kapsam uydurulur (→S18) | Batu'dan bir karar; değişince güncelleme | Batu her adımı canlı izliyorsa (bu iş öyle değil) | K15, K88, K105 |
| Soru sınıflama ve yükseltme kuralı (repoda var / araştırılır / teknik karar / denenir / Batu'nun değeri) | Batu'yu arama motoru ya da gizli birleştirici yapmaz | Aşırı sorma veya sessiz değer seçimi (→S2, S15) | Her soruda kısa sınıflama | – | K110 (A003 §3.1), K76, K33 |
| Otomatik seçim kaydı (Batu adına verilen tercih kararları; kontrol noktasında toplu sunum) | "Eksik kararı fark etmek onu verme izni değildir" ilkesi işler | Tercihler görünmeden birikir; kabulde sürpriz ve yeniden iş çıkar (→S2, S5) | Karar başına bir satır | Tercih içermeyen mekanik işte | K101, K113 |
| Kapsam ve çerçeve değişikliği kontrolü (neyin değiştiğini ayırma: yürütme / yöntem / başarı anlayışı / Batu'nun amacı) | Amaç kayması sessizce olmaz | Yönü bir önceki tur belirler (→S5, S3) | Revizyonda bir sınıflama satırı | – | K46, K111 |
| Kontrol katmanı değişiklik kuralı ve hatlar arası otorite (CLAUDE.md, `.claude/agents`, AGENT.md değişikliği Batu onaylı; EXP-006 hattıyla ilişki) | Ajan kendi kurallarını sessizce yeniden yazmaz; iki hat çakışmaz | Kural kayması; dal çakışması (→S9, S19) | Onay beklemesi | – | K92, K87 |
| Karar kaydı (Batu'nun kararları ile Claude'un tasarım kararları ayrı; gerekçe, yanlışsa bedeli, yeniden açma koşulu) | Kararın nedeni oturumlar arası taşınır | Kararlar yeniden tartışılır (salınım) ya da unutulur (→S18, S5) | Düşük | – | K79, K83 |

**S1 zayıfsa:** Batu ya her aşama sınırında "devam" yazmak zorunda kalır ya da adına karar verilir (→S2). Plan kimin onayıyla değiştiği belirsiz biçimde kayar (→S5). Yeni oturum yetkiyi çözemez (→S18). Araç gücü yetki sanılır (→S16).

#### S2 — Batu ile iş birliği

**Amaç:** Batu'nun amaç, yetki ve kabul rolünü en az bilişsel yükle ve en yüksek dikkatle yerine getirmesini sağlamak. Onu gizli koordinatör, mesaj taşıyıcı ya da arama motoru yapmamak. Dikkatini, sistemin aynı model olmayan tek denetim kanalı olarak korumak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Mesaj biçimi sözleşmesi (sonuç, kararı etkileyen belirsizlik, haritadaki yer; üç bitiş biçimi) | "Şu an ne yapıyoruz" sorusunun cevabı hep açıktır | Uzunluk ve "laf ebeliği"; yön anlaşılmaz (→S1) | Düşük | – | K110, K82 |
| Kontrol noktası raporu (özerk koşu için: ne yapıldı, hangi karar değişti, otomatik seçimler, açıklar, nereye bakmalı) | Batu commit okumadan denetleyebilir | Özerk koşu görünmez; ya kabul körleşir ya Batu commit okur (→S1, S14) | Kontrol noktası başına bir sayfa | Birkaç dakikalık tek adımlı işte | K89 |
| Soru kuyruğu (önerili, etkisi ve etkilediği kalemler yazılı) | İş durmaz, soru kaybolmaz | Sorular ya işi durdurur ya kaybolur (→S5) | Kuyruk bakımı; geç cevapta yeniden iş | – | K15, K34 |
| Kabul paketi (exact sürüm, kriterler, teknik doğrulama durumu ayrı satırda, bilinen açıklar, öneri) | Kabul ile teknik doğrulama birbirine karışmaz | Kabul törene döner ya da Batu teknik doğrulayıcı olur (→S1, S14) | Kabul başına bir paket | – | K29, K72, K107 |
| Hatırlatma ve düzeltme kaydı (her hatırlatma bir kusurdur; hangi alt sistemin kusuru olduğu da yazılır) | Gizli koordinasyon yükü ölçülür | Batu'nun taşıdığı iş görünmez kalır (→S17, S21) | Düşük; sayı tek başına proxy tuzağıdır (§5 Y13) | – | K05, K37 |
| Bilişsel yük bütçesi (okuma yükü sınırı; Batu'nun kelimeleri; "okuman gereken tek belge" ilkesi) | Dikkat korunur; yön ve kabul kararları daha isabetli olur | Batu yorulur; tek bağımsız denetim kanalı zayıflar (→S14, S1) | Yazım disiplini | – | K99, K82 |
| Bildirim ve tetik kuralları (aşama sonu, gerçek karar, tıkanma, ilerlemenin durması; kanal) | Sessiz başarısızlık önlenir | Batu'nun tek döngüsü bayat bilgiyle döner (→S17) | Kanal cloud'da bilinmiyor | – | K25, K89 |

Batu'nun sözlerinin birebir kaydı S10'dadır; sahibi S10'dur.

**S2 zayıfsa:** Kabul ve yetki kararları körleşir (→S1). Çerçeve hatalarını yakalayan tek kanal zayıflar (→S14). Keşif yükü Batu'ya kayar (→S4). Takılma geç fark edilir (→S17). Konfor burada güvenliğin parçasıdır. Batu'nun olaylarda hata yakalayan kişi olduğu kaynak diyor [K35, K41, K53]; dikkati tükendiğinde bu hataların geçeceği çıkarımdır.

### Grup B — İşin akışı

#### S3 — Metodoloji ve yaşam döngüsü

**Amaç:** İşin hangi aşamalardan, hangi iş kalemi döngüsüyle, hangi ritimle ve hangi kapılardan geçtiğini tanımlamak. Bunu yaparken tören düzeyini riske ve belirsizliğe orantılı tutmak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Aşama haritası (her aşamanın sorusu, teslimatı, giriş/çıkış ölçütü, Batu'nun rolü) | Yön haritadan gelir, bir önceki turdan gelmez | EXP-006 E1 kayması (→S5, S1) | Düşük | Tek adımlık işte | K46, K110 |
| İş kalemi döngüsü (amaç zinciri → bitti tanımı → yap → karşı-oku → kaydet) | Her kalemde aynı asgari disiplin | Kalem kalem değişen kalite (→S14) | Kalem başına sabit ek yük | Küçük mekanik işlerde kısaltılabilir | K110 |
| Ritimler (oturum açılış/kapanış, kalem kapanışı, aşama kapanışı, periyodik yön gözden geçirmesi) | Kontrol noktaları zamana bağlanır, "hatırlanınca" yapılmaz | Kayıt ve yön kontrolü unutulur (→S18, S17) | Sabit ek yük; kanondaki "atlanamaz" kapanış ritüeli bu bedelin uç örneği | – | K34, K79 |
| Kapılar ve durma koşulları (hangi geçiş kendiliğinden, hangisi Batu'da; yapıldı / doğrulandı / işe yarıyor / kabul ayrımı) | Hız ile fren aynı yerde tanımlanır | Ya durmadan akış (kayma) ya her aşamada durma (→S1, S2) | Düşük | – | K15, K88, K69 |
| Tören orantısı (risk, belirsizlik, geri dönülebilirlik ve **aşağı akış yükü** → kontrol ağırlığı) | Yöntem kendi ağırlığı altında çökmez | Ya "boş tören" ya eksik kontrol (→S14, S20) | Yanlış sınıflama riski (§5 Y7) | – | K10, K76, K28 |
| Pilot, sonra ölçekle (önce tek gerçek işte dene, gözden geçir, sonra genişlet) | Yöntem kâğıtta değil işte sınanır | 17 dilim kâğıt üstünde ilerleme (→S21) | Zaman | Yöntem zaten aynı koşulda sınanmışsa | K110 (A003 §2, §5), K82 |
| Yöntemin ağırlık bütçesi ve meta-iş sınırı (yöntem işine giden payın izlenmesi; "istenmedikçe süreç inşa etme") | Süreç ürünün yerine geçmez | "Süreç kendisi ürün oldu"; asıl teslimat ertelenir (→S5, S17) | Ölçüm | – | K27, K28, K46 |

**S3 zayıfsa:** Plan kalemleri tutarsızlaşır (→S5). İlerleme ölçüsü tanımsız kalır (→S17). Doğrulamanın ne zaman yapılacağı belirsizleşir (→S14). Tören şişkinliği maliyete döner (→S20).

#### S4 — İhtiyaç ve kapsam keşfi (yeni; S5'ten ayrıldı)

**Amaç:** Gerekli ama kimseye verilmemiş işi, önkoşulu, bakış açısını ve kaynak alanını, Batu'nun hatırlatmasına gerek kalmadan bulmak ve plana gerekçesiyle sokmak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Amaçtan geriye önkoşul keşfi ("bu amaç için önce ne doğru olmak zorunda?") | İş yapılmadan önce iş ortaya çıkarılır | EXP-005 sonucu: keşif yükü kullanıcıya döner (→S2) | Aşama başında keşif turu | İş tamamen önceden tanımlıysa (bu işte değil) | K38, K60 |
| Bakış açısı taraması (üretim, kullanım, etki; Foundation'ın "neyi kaçırıyorum?" merceği) | İlk göze çarpan görüşe çapalanılmaz | Soru bankasındaki üretim perspektifi kaybı (→S14) | Tarama başına okuma | – | K41, K42 |
| "Kimseye verilmemiş iş var mı?" kapanış sorusu ve eksik-arayıcı rolü | Plan öz-denetiminin kör noktası kapanır | Erken kapanış (→S14, S5) | Kapanış başına bir tarama | Geri alınması ucuz ve kimsenin dayanmadığı ara adımda | K79, K110 |
| Keşfin kökeni ve akıbeti kaydı (kim buldu: ana oturum / alt ajan / karşı-okuma / Batu; kullanıldı mı, düştü mü) | Batu'nun bulduğu açıklar ölçülür | Keşif başarısı Batu'nun katkısıyla şişer (→S17, S2) | Satır başına kayıt | – | K60, K79 |
| Amaç ihtiyacı ile yöntem ihtiyacı ayrımı | Seçilen yöntemin doğurduğu iş amaç sanılmaz | Meta-iş büyür (→S3) | Bir sınıflama satırı | – | K83 |
| Kaynak alanı seçimi keşfin parçasıdır (verilen kaynak listesi bütün alan sayılmaz) | Dar kaynak seçimi keşfi sınırlamaz | "Niye sadece EXP-004'e gönderiyorsun?" (→S6) | Seçim gerekçesi | – | K40 |
| Çerçeve yeterliği sınaması (türetimin doğru kaynaktan gelip gelmediği) | Yanlış çerçeveden türetim erken yakalanır | Roller SOUL yeteneklerinden türedi, ekibin kendi döngüsünden değil (→S11) | Aşama başında bir soru | – | K52 |

**S4 zayıfsa:** Keşif Batu'ya kalır ve Batu gizli koordinatöre dönüşür (→S2). Plan eksik kalır (→S5). Doğrulama yalnız plandaki işi sınar ve eksik iş "tamam" damgası alır (→S14). Araştırma birikimi olduğu halde kullanılmaz (→S6).

#### S5 — Plan ve iş yönetimi

**Amaç:** Bilinen işi yaşayan bir planda tutmak: statüleri, bağımlılıkları, sahipleri, varsayımları ve değişiklik geçmişiyle birlikte. Revizyonu kontrollü yapmak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Tek ana harita ve aşama iş listesi | Yönün tek kaynağı | Yön dağılır (→S1, S3) | Düşük | – | K110 |
| Kalem şeması (amaç = hangi karar; bitti tanımı; kapsam dışı; sahip; köken; statü: aday → kabul → sürüyor → bitti → doğrulandı; park; düştü + gerekçe) | "Olmadı"nın nedeni korunur; aday ile kabul edilmiş iş ayrışır | Bütün kalemler "iptal" ya da "bitti"ye çöker (→S17, S14) | Kalem başına birkaç alan | – | K110, K112 |
| Bağımlılık türleri ("seçtiğimiz sıra" ≠ "zorunlu önkoşul" ≠ "keşfedildiği iş") | Hazır iş doğru hesaplanır | Gereksiz bekleme ya da yanlış sıra (→S12) | Düşük | – | K79, K83 |
| Varsayım ve risk kaydı (aşamanın dayandığı varsayımlar; çökerse revizyon tetiği) | Plan kırılganlığı görünür olur | Çöken varsayım fark edilmez (→S15, S18) | Aşama başına bir liste | – | K110 |
| Revizyon protokolü (tetik, sınıflama, karar yetkisi, tarihli not, kabul edilen sürümün korunması, sapma kaydı) | Kötü plan sonradan "hep doğruymuş" görünmez | Plan geçmişi yeniden yazılır (→S9, S1) | Revizyon başına bir not | – | K100, K110 |
| Hazır iş ve akış sınırı (açık ≠ yürütülebilir; aynı anda açık iş sınırı) | Çok iş başlatmak ilerleme sanılmaz | Yarım işler birikir (→S12, S20) | Düşük | Tek iş kalemli aşamada | K112, K79 |
| Dilim boyutlandırma (dilim, ürettiği sonucu doğru üretebilecek kadar büyük olur) | Soru üreten dilimlerden kaçınılır | 16 görevin hiçbiri kod üretmedi; teknik sorular Batu'ya gitti (→S2) | Planlamada düşünme | – | K30 |
| Park, düşürme ve yeniden açma koşulu (adı konmuş tetik, en küçük kapsam) | Bekleyen iş unutulmaz; kapanmış iş keyfî açılmaz | Sessiz kayıp ya da sonsuz yeniden açma (→S14) | Düşük | – | K83, K110 |

**S5 zayıfsa:** İlerlemenin neye göre ölçüleceği belirsizleşir (→S17). Dağıtım gerekçesiz yapılır (→S12). Yeni oturum sıradaki işi bilemez (→S18). Yönü Batu vermek zorunda kalır (→S2).

#### S6 — Araştırma birikiminden yararlanma

**Amaç:** Foundation, studies, explorations ve dış kaynakları doğru anda ve doğru derinlikte kullanmak; kullanımın kararı nasıl değiştirdiğini izlenebilir kılmak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Başvuru tetikleri (aşama başında soru genişletme; tasarım seçimi; mekanizma icadı öncesi; sürpriz ya da çelişki; terim kayması; her Claude Code iddiası) | Araştırma rastlantıya kalmaz | Birikim var ama kullanılmaz (→S4) | Tetik başına okuma | – | K110 (A003 §3.5) |
| Sıra: önce Foundation (mercek), sonra studies (örnekler) | Bakış genişler, sonra örnek okunur | Örneklere dar bakışla gidilir (→S4) | Düşük | – | K82 |
| Okuma kaydı (kaynak, sürüm/SHA, kapsam tam/kısmi/okunmadı, hangi soru için, neyi değiştirdi) | "Tam okudum" iddiası sınanabilir olur; tekrar okuma önlenir | Kesik araç çıktısı "tam" etiketi alır (→S14) | Okuma başına satır (§5 Y14) | Karar taşımayan göz atmada | K51, K110 |
| Araştırma izi (her tasarım kararı için: hangi bulgu; destekledi mi, değiştirdi mi, bir seçeneği eledi mi, hiçbir şey değiştirmedi mi; neyi kanıtlamadığı; "yalnız akıl yürütme" işareti) | Araştırmanın gerçekten kullanıldığı görünür | Tasarım gerekçesiz kalır; Batu'nun "ben araştırtmak zorunda mıyım" eleştirisi (→S15, S2) | Karar başına kısa kayıt | – | K43, K110 |
| Birlikte okuma (kaynaklar farklı ajanlara bölündüğünde çapraz kaynak iddiaları için) | Kaynaklar arası ilişki karşılaştırılır | Her parça okunur ama ilişki kaybolur (→S12, S14) | Ek okuma | Tek kaynaklı soruda | K56 |
| Tazelik ve yeniden doğrulama (studies'teki teknik bilgi eskiyebilir; Claude Code iddiası güncel belge ve canlı denemeyle sınanır) | Eski belgeden yanlış kabiliyet çıkarılmaz | "Üç kat iç içe alt ajan" yanılgısı (→S19) | Doğrulama maliyeti | Kavramsal ve kalıcı ayrımlarda | K91, K71 |
| Kanıt gücü etiketi (tedarikçi / ürün kaynağı / aynı-asistan kavramsal / bağımsız ölçüm) | Aynı kaynaktan türeyen kopyalar bağımsız kanıt sanılmaz | Güven şişer (→S14) | Düşük | – | K45 |
| Durma ölçütü (ek okuma kararı değiştirmeyecekse dur; bütçenin bitmesi "bitti" değildir) | Sonsuz okuma ve sahte kapanış önlenir | Maliyet ya da erken kapanış (→S20, S14) | Düşük | – | K83, K110 |

**S6 zayıfsa:** Keşif beslenmez (→S4). Tasarım "yalnız akıl yürütme"ye kalır (→S15). İddialar kaynaksız doğrulanır (→S14). Gereksiz okuma maliyeti oluşur (→S20).

### Grup C — Bilgi taşıma

S7 ve S8'in ayrıntılı standardı R07–R10'un konusudur. Burada yalnız envanter düzeyi ve başka alt sistemlerle bağları verilir.

#### S7 — Bağlam yönetimi

**Amaç:** Her aktörün, ana oturumun ve her alt ajanın, o an yaptığı iş için yeterli, güncel ve yetkili bir bilgi görünümüne sahip olmasını sağlamak. Bağlam penceresini sınırlı bir kaynak olarak yönetmek.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Bağlam bütçesi ve sıkıştırma politikası (ana oturumda %80'de otomatik sıkıştırma; sıkıştırmadan önce kayıt; planlı taze oturum) | Sıkıştırma kaybı öngörülür | Ara akıl yürütme ve araç çıktısı kaybolur (→S18) | Kayıt disiplini; taze oturum başlatma maliyeti | – | K16, K18 |
| Açılış seti (her oturumda okunanlar) ve boyut sınırı | Yeniden yükleme ucuz kalır | Açılış seti 110 KB'a çıktı, sınır 50 KB'tı (→S20) | Kırpma disiplini | – | K26, K23 |
| Bağlam paketi (yük taşıyan içerik ve işaretçi birlikte; hangi pasaj, neden) | Alt ajan içeriği görür, yalnız yolunu değil | "Pointer ≠ content": verilen yol okunmayabilir (→S13) | Brief uzar | İçerik kısa ve alt ajanın okuması garantiyse | K84, K63 |
| Okuma işinin alt ajanlara dağıtılması (bağlam izolasyonu) | Ana oturum hafif kalır | Koordinatörün bağlamı dolar (→S12) | Özet kaybı riski (§5 Y2) | Kısa işte | K06, K17 |
| Seçilen ≠ sunulan ≠ kullanılan ayrımı (kritik bilgi için kullanım kanıtı) | Bilginin gerçekten karara girdiği görülür | Bilgi verildi ama kullanılmadı; bu fark edilmez (→S14) | Kritik yerde bir kontrol | Kritik olmayan bilgide | K63 |
| Sıkıştırma ve yeniden başlama sonrası yeniden yükleme protokolü (kurallar ve durum dosyaları yeniden okunur) | Kurallar özetten değil kaynağından gelir | Önceki talimatlar "unutulur" (→S15) | 60 KB + 50–100 KB yeniden okuma | – | K23, K18 |
| Role özgü görünüm (aynı bilgi, farklı rol için farklı biçimde) | Her rol ihtiyacı kadarını görür | Ya bilgi boğulması ya kritik eksik (→S11) | Görünüm hazırlığı | Tek rollü işte | K63, K66 |
| Gürültü disiplini (büyük araç çıktıları bağlama dökülmez) | Sıkıştırma döngüsü önlenir | "Autocompact thrashing" (→S18, S20) | Düşük | – | K18 |

**S7 zayıfsa:** Koordinatör yalnız özetlerle hüküm verir (→S14, S12). Nitelikler kaybolur (→S10). Sıkıştırmada iş kaybolur (→S18). Maliyet artar (→S20).

#### S8 — Bellek yönetimi

**Amaç:** Neyin, hangi otoriteyle, ne zaman kalıcı hale getirileceğini, nasıl geri çağrılacağını, ne zaman güncelleneceğini ya da unutulacağını yönetmek.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Bellek türleri ve otorite sınıfları (çalışma durumu, kararlar, kaynak ve kanıt, dersler ve yöntem, oturum günlüğü; kanonik ≠ türetilmiş) | Türetilmiş bellek kanonik durumu ezmez | Eski özet güncel sanılır (→S10, S18) | Sınıflama | – | K63, K67 |
| Yazma politikası ve zamanlaması (kalem kapanışı, sıkıştırmadan önce, VM kaybı riski) | Bulgular oturum ölmeden kalıcılaşır | Tartışma ve düzeltme kaybolur (→S18) | Commit ritmi | – | K41, K102, K19 |
| Geri çağırma yolu (giriş dosyası → soruya özgü harita → özgün bölüm) | Bulunabilirlik; tekrar okuma azalır | Kayıt var ama bulunamaz (→S7, S6) | Dizin bakımı | – | K110, K61 |
| Güncelleme, üzerine yazma (supersession) ve unutma | Eski kayıt tarihsel olarak doğru, operasyonel olarak geçersiz tutulabilir | Tarih güncel otorite sanılır (→S1, S10) | Bakım | – | K44, K61 |
| Ortam gerçeği: repo tek güvenilir bellek (cloud'da auto memory taşınmaz; rol belleği commit edilmeli) | Bellek oturumlar arası gerçekten taşınır | Makinede kalan bellek kaybolur (→S18, S11) | Commit disiplini | – | K20, K21, K17 |
| Rol belleği (kalıcı rolün birikimi) | Rol her çağrıda sıfırdan başlamaz | K-007'nin "her seferinde yeniden rol biçmek" eleştirisi (→S11) | Bakım; bayatlama riski | Rol tek seferlikse | K02, K21 |
| Bellek bütünlüğü denetimi (bayatlık, çelişki, türetilmişin kanoniği ezmesi) | "Historical artifact mistaken for current truth" önlenir | Bayat bellekle devam edilir (→S18, S14) | Periyodik tarama | – | K67, K61 |

**S8 zayıfsa:** Devir kopar (→S18). Roller birikim taşımaz (→S11). Dersler kalıcılaşmaz (→S21). Taşıdığı işten ağır bellek açılış setini şişirir (→S7) [K26].

#### S9 — Kayıt ve bilgi mimarisi

**Amaç:** Kalıcı kayıtların nerede, hangi biçimde, tek kaynaktan, hangi statü sözlüğüyle ve hangi sürümle tutulduğunu güvenceye almak; bir değişikliğin ona bağlı kayıtlara yayıldığını kontrol etmek.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Dosya görevleri tablosu (her yüzeyin tek işi) | Hangi değişikliğin nereye yazılacağı bellidir | Aynı bilgi birden çok yerde (→S18) | Düşük | – | K88 (R01 güçlü yanlar) |
| Tek kaynak kuralı (bir bilgi tek yerde durur; başka yerlerde yalnız işaretçi) | Çelişen kopya oluşmaz | "NOT STARTED" beş dosyada ve WORK'te yedi kez; 14 spec'in yeniden yazılması (→S5, S18) | İşaretçi takibi (§5 Y10) | – | K49, K31 |
| Statü sözlüğü (aday / kabul / sürüyor / bitti / doğrulandı / park / düştü; ayrıca bilinmiyor, değerlendirilmedi, bayat) | "Yanlış" ile "değerlendirilmedi" karışmaz | Belirsiz statü kesinliğe döner (→S14, S10) | Düşük | – | K112, K69 |
| Sürümleme ve tam bağlama (hangi iddia hangi dosya sürümüne dayanıyor; SHA/blob) | Kanıt belirli bir sürüme bağlanır | "Dosya adı var" yeterli sanılır (→S14) | Düşük (git) | – | K67, K110 |
| Yayılım kontrolü (bir karar değişince ona bağlı dosyalar güncellendi mi) | "Onaylanan değişiklik ≠ uygulanan değişiklik" ayrımı korunur | Foundation'da çelişen STATE'ler (→S18, S1) | Değişiklik başına tarama | – | K86, K31, K72 (F16) |
| Yönlendirici bakımı ve giriş yolu (README, INDEX, okuma sırası) | Soğuk başlayan oturum doğru işe gider | Bayat tabela oturumu DEVOS-002'ye götürür (→S18, S1) | Düşük | – | K88, K92 |
| Dal ve yayın politikası; geri okuma (readback) | Yeni oturum doğru durumu görür; yayın ile içerik kimliği karışmaz | Kanonik durum bölünür; "yansımadı" karışıklığı (→S18, S2) | Politika kararı; PR bakımı | – | K87, K39, K54 |
| Hijyen ve bakım sahipliği (bayat "sıradaki" satırları, eski kopyalar, dal birikmesi) | Tarihsel metin talimat gibi okunmaz | 27 dosyada "Authority notu" kalıbı; tarihsel "next" satırları (→S16, S7) | Periyodik iş | – | K95, K32 |

**S9 zayıfsa:** Yeni oturum yanlış ya da bayat yüzeyi okur, ya da çelişki yüzünden durur (→S18). Açılış yükü artar (→S7). Yetki çözülemez (→S1). Türetilmiş metin kaynak sanılır (→S10).

#### S10 — Anlam bütünlüğü: kaynak sözü, terim ve özet sadakati (genişletildi)

**Amaç:** Anlamın her yeniden ifade edilişte korunmasını sağlamak: özet, devir notu, sıkıştırma, alt ajan dönüşü ve terim seçimi. Batu'nun sözünün ve niyetinin yorumla karışmasını önlemek.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Batu'nun sözlerinin birebir deposu ve statü etiketi (amaç / kısıt / karar / örnek / çağrışım / açık soru) | Düzeltmeler parafrazda kaybolmaz; örnek kapsam sanılmaz | EXP-006'da 53 bin kelimenin yalnız 1.494'ü Batu'nun sözü (→S1, S2) | Aktarım emeği | – | K49, K82 |
| Kaynak ≠ türetilmiş görünüm etiketi (her özet "görünüm" diye işaretli ve kaynağına bağlı) | Parafraz kaynak diye okunmaz | EXP-004 arşivi: özet kaynak aktarımı diye sunuldu (→S9, S14) | Düşük | – | K54, K78 |
| Nitelik koruyan özet ve devir şablonu (kararlar, çözülmemişler, reddedilenler, kaynaklar, statüler; belirsizlik kesinliğe dönmedi mi kontrolü) | "Payload survives; qualifier disappears" önlenir | Kabul edilmemiş sonuç güncel sanılır (→S18) | Şablon disiplini | – | K67, K55, K102 |
| Özet yeterliği sınaması (bu özet şu soruya yeterli mi?) | Doğru cümlelerden oluşan ama yanlış hükme götüren özet yakalanır | "Mektubu kimin gördüğü" kaybolur (→S14) | Kritik devirde bir soru | Karar taşımayan özette | K56 |
| Terim sözlüğü ve Batu'nun kelimesine dönüş | Kavram kayması görünür | "Motivasyon" → "başarı yönü" (→S2) | Bakım | – | K50, K77 |
| Yorum izi (önemli yorum, belirsizlik ve yorum değişikliği görünür) | Batu okuma anındaki anlam seçimini denetleyebilir | "Anladı sanıyoruz" (→S2, S14) | Karar başına bir satır | – | K77, K82 |
| Reddedilen seçeneklerin korunması | Reddedilen seçenek özetle geri sızmaz | Kapanmış tartışma geri döner (→S5) | Düşük | – | K83 |

**S10 zayıfsa:** Batu'nun kararı yanlış okunur ve yetkisiz bir amaç değişikliği olur (→S1). Doğrulayıcı yanlış iddiayı doğrular (→S14). Devir notu statü kaybeder (→S18). Batu anlaşıldığını sanır (→S2).

### Grup D — Aktörler

#### S11 — Kalıcı roller (S12'den ayrıldı)

**Amaç:** Tekrarlanan katkı türlerini sabit, sürümlü ve birikim taşıyan rol tanımlarına bağlamak; her görevde rolü yeniden biçmemek.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Rol sözleşmesi (amaç ve başarı yönü; girdi ve yeterlik; tetik; teslimat ve tüketici; yetki ve olumsuz sınır) | Rol her görevde aynı ölçütle çalışır | Brief her seferinde rolü baştan anlatır, sonuç tutarsızlaşır (→S13) | Rol başına bir tanım | Tek seferlik iş türünde | K65, K58 |
| Rol kaydı ve sürümü (rol adı → dosya → sürüm; hangi görev hangi rol sürümüyle koştu) | Rol değişikliğinin etkisi izlenir | Neyin işe yaradığı ölçülemez (→S21) | Düşük | – | K109 |
| Türetme kaynağı (işin kendi çalışma döngüsü ve ihtiyacı) | Roller doğru kaynaktan doğar | Roller SOUL yeteneklerinden türedi; ekibin döngüsü geç geldi (→S4) | Keşif turu | – | K52, K110 |
| Yeterlik dayanağı (rol adı yeterlik değildir) | Uzmanlık gerektiren iş, adı konmuş ama yetersiz role verilmez | Kalite sessizce düşer (→S14) | Yeterlik kontrolü | Genel okuma işlerinde | K58, K65 |
| Rol belleği ve birikimi (S8'le bağlı) | Uzmanlık oturumlar arası birikir | Her çağrı sıfırdan (→S21) | Bakım; bayatlama riski | – | K02, K21 |
| Rol başına araç ve yetki sınırı (agent tanımında araç listesi; durum değiştiren araçlar yalnız ana oturumda) | Alt ajan kendi başına oturum ya da tetik açamaz | Kontrolsüz etki ve maliyet (→S16, S20) | Tanımda bir alan | – | K24, K17 |
| Rol yaşam döngüsü (açma, birleştirme, kapatma; süregelen sorumluluk ≠ sürekli çalışan ajan) | Rol sayısı işle orantılı kalır | Rol enflasyonu, koordinasyon yükü (→S12, S3) | Periyodik gözden geçirme | – | K64, K58 |
| Çalışma rolleri ≠ DevOS rolleri ayrımı | P2'nin cevabı önceden verilmez | İki düzey karışır (→S1) | Düşük | – | K110 (A003 §3.2) |

Ortam gerçeği: repo içindeki `.claude/agents/` cloud oturumuna otomatik taşınır [K17]. Alt ajan kendi alt ajanını açamaz (depth = 1) [K16]. Rol dosyası tavsiyedir, zorlama değildir [K71].

**S11 zayıfsa:** Brief'ler uzar ve tutarsızlaşır (→S13). Dersler bağlanacak bir taşıyıcı bulamaz (→S21). Dağıtım keyfîleşir (→S12). Brief yazma maliyeti artar (→S20).

#### S12 — Orkestrasyon ve bütünleştirme (S11'den ayrıldı)

**Amaç:** İşi alt ajanlara bölmek, paralelliği sınırlamak, dönüşleri toplamak ve çelişkileri koruyarak tek bir gerekçeli bütüne (karar, taslak) dönüştürmek.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Dağıtım kararı (hangi iş hangi role; tek mi paralel mi; hangi korunan gereksinim için) | Karmaşıklık gerekçeli olur | Gereksiz ajan ve tören (→S20, S3) | Karar başına bir satır | – | K76 |
| Paralellik bütçesi ve bağımsızlık koşulu | Paralel iş bağımsızsa ve incelenebiliyorsa açılır | İnceleme kapasitesi aşılır; korele sonuçlar bağımsız sanılır (→S14, S2) | Hız kaybı | – | K72 (F10), K45, K112 |
| Birleştirme sözleşmesi (ortak taban, çatışma tanımı, birleştirme yetkisi, çelişkili kanıtın korunması, birleştirmenin kendi doğrulaması) | Parçalar sağlamken bütünün yanlış olması yakalanır | "Worker outputs … individually sound … wrong global conclusion" (→S14) | Birleştirme başına yapı | Tek dönüşlü işte | K76 |
| Akış sahipliği ≠ karar sahipliği | Koordinatör görünmez bir düşünce filtresine dönüşmez | Bütün kararlar koordinatörde toplanır (→S1, S7) | Karar sahiplerinin tanımı | – | K66 |
| Tek yazıcı ve tek mantıksal commit yolu | Paralel yazımlar kanonik kaydı bozmaz | Çakışan yazımlar (→S9) | Darboğaz (§5 Y5) | – | K59, K110 |
| Yeniden deneme kuralı (değiştirilmeden tekrar gönderme yok; durum kodları; üç başarısızlıkta devre kesici) | Kör tekrar önlenir | Aynı hata tekrarlanır, maliyet büyür (→S20) | Düşük | – | K79 |
| Alt ajan yaşam döngüsü ve kaybı (VM geri alınınca arka plan ajanları gider; göndermeden önce HEAD kaydı; yarım iş tespiti) | Kayıp iş fark edilir ve yeniden başlatılır | Yarım iş sessizce kaybolur ya da çakışan yazım kalır (→S18) | Kayıt satırı | – | K19, K79 |
| Kalıcı topoloji durumu (açık dallar, beklenen dönüşler) | Oturum kaybından sonra yeniden kurulur | Hangi alt ajanın ne yaptığı unutulur (→S18) | Düşük | Tek oturumluk kısa işte | K76 (C7) |
| Koordinatör kararlarının görünürlüğü (ayrıştırma ve birleştirme gerekçesi repoda) | Yönetici hatası sınanabilir | "Akıllı koordinatör halleder" kutusu (→S14) | Karar başına not | – | K76, K108, K09 |

Ortam gerçeği: depth = 1 olduğu için roller arası her istek ana oturumdan ya da repo dosyalarından geçer (merkezli yıldız, "hub-and-spoke") [K16]. Paylaşılan kullanım limitleri paralelliğin tavanını belirler [K22].

**S12 zayıfsa:** Birleştirilmiş sonucu kimse sınamaz (→S14). Koordinatörün bağlamı dolar (→S7). Paralel patlama limitleri tüketir (→S20). Batu gizli birleştirme algoritmasına dönüşür (→S2).

#### S13 — Ajanlar arası arayüzler

**Amaç:** Görev tanımı, dönüş biçimi, devir notu ve roller arası istek için sabit ve sürümlü sözleşmeler kurmak. Alt ajanın "emir eri"ne dönüşmesini önlemek ve dönüşü kanıt değil veri olarak ele almak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Görev tanımı şablonu (amaç zinciri, tek soru, kapsam, bağlayıcı kararlar, kaynaklar ve sürümleri, yöntem, kanıt dili, dönüş biçimi, durma ölçütü, yazma izinleri) | Alt ajan rota, hedef ve ölçütle çalışır | "Emir erine dönüşür" (→S15) | Brief başına yazım | – | K110, K82 |
| Dönüş şeması (durum kodu; iddia + kanıt işaretçisi + etiket; varsayımlar ve otomatik seçimler; açık sorular; okuma kapsamı; dokunulan dosyalar) | Dönüş denetlenebilir ve birleştirilebilir | Nitelik kaybı; birleştirme belirsizliği (→S10, S12) | Düşük | – | K79, K101 |
| Devir notu şablonu (kararlar, çözülmemişler, reddedilenler, kaynaklar, etiketler, sıradaki sorumluluk) | Devir statü kaybetmez | "Devir notunu kısaltma, karar-kritik statüyü silme izni değildir" (→S18) | Düşük | – | K83, K102 |
| Roller arası istek biçimi (hangi soru, hangi karar için, kapsam, dönüş noktası) | İstek kaybolmaz; cevap talep sahibine döner | "Sonraki açılışında" cevaplanan sahipsiz kalemler (→S12, S2) | Düşük | – | K66, K34 |
| Dönüş = veri kuralı (kararı taşıyan iddia kaynağından kontrol edilir) | Yanlış iddia karara girmez | "Üç kat iç içe" yanılgısı (→S14) | Kontrol maliyeti | – | K91 |
| Brief sürümü ve kaydı (hangi alt ajan hangi brief sürümüyle koştu) | Geç sonuç doğru sürümle uzlaştırılır; aynı tanımla yeniden başlatılabilir | Etki ölçülemez; yeniden çalıştırılamaz (→S21, S18) | Düşük | – | K109 |
| Tüketim kanıtı (talep sahibi sonucu nasıl kullandığını ya da neden kullanmadığını gösterir) | İstek → çalışma → kullanılan sonuç zinciri kapanır | "Mesaj gitmesi … tüketicinin sonucu kullandığını kanıtlamaz" (→S14) | Karar başına bir satır | – | K65, K66 |

**S13 zayıfsa:** Nitelik kaybolur (→S10). Birleştirme belirsizleşir (→S12). İddialar yeniden kontrol edilemez (→S14). Brief düşünme koşullarını taşımazsa muhakeme disiplini alt ajana ulaşmaz (→S15).

### Grup E — Kesişen denetimler (fren ve güvenlik)

Bu gruptaki alt sistemler bir aşamaya bağlı değildir; her aşamayı keser. Yol haritası çalışması da yönetişim, gözlem ve doğrulamanın "sona eklenen katman" olmadığını söyler [K70].

#### S14 — Kalite güvencesi ve doğrulama

**Amaç:** Ölçütü önceden koymak, çıktıyı üretenden ayrı bir yolla sınamak, tamamlanma katlarını ayırmak ve kanıt gücünü adıyla söylemek.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Önceden yazılı ölçüt ve ölçüt bütünlüğü (sonuç görüldükten sonra sessizce değişmez) | Kötü sonuç ölçüt değiştirilerek iyi gösterilmez | "Testi geçirecek şekilde değiştirilen test" (→S1, S21) | Düşük | – | K62, K110 |
| Tamamlanma katları (alt ajan "tamam" ≠ kontrol edildi ≠ karşı-okuma çürütemedi ≠ Batu kabul etti; yapıldı / doğrulandı / işe yarıyor / kabul) | Sahte kapanış görünür olur | "Work performed ≠ … authorized acceptance" (→S17, S1) | Düşük | – | K69, K110 |
| Ayrı girdili karşı-okuyucu (gerekçeyi görmez; ölçüt, kaynak ve tam sürümle çalışır; hangi hata sınıflarını denetlediğini söyler) | Üreticinin çerçevesine bağlanmadan sınar | Öz-onay: EXP-006'da hiçbir aile elenmedi (→S1) | Ek alt ajan | Düşük riskli ve geri alınabilir ara adımda | K47, K79, K76 |
| Kanıt gücü ve bağımsızlık beyanı ("taze gözle karşı-okuma", bağımsız doğrulama değil) | Aynı modelin kör noktası gizlenmez | "Doğrulandı" etiketi şişer (→S2) | Düşük | – | K13, K106 |
| Hata duyarlılığı sınaması (bilerek bozulmuş örnekte kırmızı veriyor mu?) | Denetçinin ayırt etme gücü bilinir | İki yöntem aynı 4/4 PASS'i aldı, ayırt edilemedi (→S21) | Hazırlık maliyeti | Denetçi başka bağlamda zaten sınanmışsa | K96, K62 |
| Kalem denetimi (DONE / PARTIAL / NOT DONE / CHANGED / UNVERIFIABLE) | Sessiz toptan onay önlenir | Eksik kalem "bitti" görünür (→S5) | Düşük | – | K79 |
| Bütünsel inceleme (parçaların toplamı değil, tam sürümdeki bütün) | Parçalar arası uyumsuzluk yakalanır | Yerel kontrollerin toplamı bütünün kabulü sanılır (→S12) | İnceleme maliyeti | Tek parçalı çıktıda | K57, K60 |
| Düzeltme turu sınırı; park ve yükseltme | Sonsuz eleştiri döngüsü durur | Ya sonsuz döngü ya sessiz kapanış (→S20, S5) | Açık bulgu kaydı | – | K11, K79 |
| Bulgu akıbeti (her bulguya karşılık: uygulandı / gerekçeyle reddedildi / park) | Her itirazın bir karşılığı olur | Bulgular kaybolur (→S21) | Bulgu başına bir satır | – | K66, K65 |

**S14 zayıfsa:** Batu'nun kabulü teknik doğrulamanın yerine geçer (→S1). Dersler kanıtsız kalır (→S21). İlerleme iddiası kanıtsız olur (→S17). Batu hata avcısına dönüşür (→S2). Batu'nun kendi ifadesi: "kullanıcının sonradan itiraz etmesi temel kalite kontrolü olamaz" [K77].

#### S15 — Muhakeme disiplini ve bilinen ajan kusurları (yeni)

**Amaç:** Üretim sırasında düşünmenin kalitesini iz bırakan uygulamalarla korumak: varsayımların görünürlüğü, alternatif üretme, nedensel derinlik, onay baskısına direnç ve "bilmiyorum" diyebilme. Kalite güvencesi çıktıyı sonradan sınar; bu alt sistem çıktının nasıl üretildiğini korur.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Defo modeli (yağcılık, aynalama, şişme, drift, sahte menü, uydurma, öz-onay, aşırı sorma, karar-yükleme, örtme; her biri için ateşlenme anı ve iz kontrolü) | Bilinen eğilimler "yokmuş gibi" değil "varmış gibi" ele alınır | Eğilimler makul görünen çıktı üretir ve yakalanmaz (→S14, S2) | Kısa bir referans belgesi; brief'e ve role girer | – | K33, K82 |
| İz ilkesi (yumuşak öz-yargı yerine gözlenebilir iz; "mekanik kapı > iz isteyen yazılı prosedür > salt öğüt") | Kural, yazılı olduğu için değil iz bıraktığı için bağlar | "Daha dikkatli olacağım" türü vaatler (→S21) | İz alanları | – | K33, K82 |
| Karar-kritik varsayım disiplini | Tek senaryo kesin sanılmaz | Çöken varsayım plan boyunca taşınır (→S5) | Düşük | – | K78 (R01) |
| Kanıt dışı etkiye direnç (Batu'nun beklentisi, tamamlanma ve onay baskısı) | "Haklısın, bunu düşünmemiştim" döngüsü kırılır | Yön itirazla savrulur (→S1, S2) | Düşük | – | K78 (R02), K82 |
| Nedensel derinlik (belirti ≠ kök neden; sorunun adı çözüm değildir) | Yanlış düzeltme önlenir | Sorun erken "eksik motor" diye adlandırıldı (→S21) | Teşhis zamanı | Mekanik hatada | K78 (R06), K40 |
| Alternatif ve karşı kanıt arama (brief'teki yöntem alanı) | İlk çerçeveye çapalanılmaz | Tek seçenekli tasarım (→S4) | Düşük | – | K110 (A003 §3.3) |
| Belirsizlik beyanı ("bilmiyorum"; durulması gereken yerde durmak) | Uydurma yerine işaretli boşluk | Boşluk düzlenir (→S10, S14) | Düşük | – | K33, K82 |
| Uzun özerk koşuda öz-denetim tetiği (yağcılık ve drift kontrolü) | Uzun koşu yerel optimuma kaymaz | Kanonun 742 koşusu gibi "hareket var, ilerleme yok" (→S17) | Tetik başına kısa kontrol | Kısa işte | K82, K25 |
| Disiplinin alt ajanlara taşınması (AGENT.md kendiliğinden yüklenmiyor; alt ajanlar rota kapısını koşmuyor; taşıyıcı brief ve rol tanımıdır) | Disiplin yalnız ana oturumda kalmaz | Alt ajan emir eri ve yağcı olur (→S13) | Brief alanı | – | K78, K16 |

**S15 zayıfsa:** Doğrulayıcı aynı kusuru paylaşır (→S14). Sahte menü ve aşırı sorma Batu'ya yük olur (→S2). Aynalama ve uydurma anlamı bozar (→S10). Drift keşfi daraltır (→S4).

#### S16 — Güvenlik ve bütünlük

**Amaç:** Okunan içeriğin talimat sayılmasını, yetkisiz ya da yıkıcı etkiyi önlemek; yazma sınırlarını ve durum değiştiren araçları denetim altında tutmak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Veri ile talimatın ayrımı (repo kontrol dosyaları, alt ajan dönüşleri ve dış içerik veridir) | Talimat enjeksiyonu ve rol karışması önlenir | Okunan metin yetki sayılır (→S1) | Düşük | – | K78, K44, K83 |
| Bayat talimat kirliliğine karşı koruma (EXP-006'nın "sıradaki" satırları ve durma noktaları) | Eski hattın yönü yeni hattı sürüklemez | K-004'ün önlemek istediği kayma (→S5) | Okuma başına dikkat | – | K92, K49 |
| Yazma sınırları (alt ajan yalnız kendi dosyasına yazar; kanonik dosyaların tek yazıcısı) | Kanonik kayıt korunur | Çakışan ya da yetkisiz yazım (→S9) | Düşük; yalnız talimatla zorlanıyor | – | K59, K110 |
| Durum değiştiren araçların yönetimi (oturum ve tetik açan araçlar alt ajanlarda görünüyor; rol başına kısıt; sayı sınırı; denetim listesi) | Kontrolsüz oturum ya da tetik açılmaz | Maliyet patlaması; talimat enjeksiyonuyla zamanlama (→S20) | Rol tanımında araç listesi | – | K24 |
| Yıkıcı ve geri alınamaz işlem koruması (git işlemleri, silme; cloud'da bypass yok, Stop hook var) | Geri dönülemez etki önlenir | Kayıp iş ya da tarihin yeniden yazılması (→S18) | Düşük | – | K113, K17 |
| Geçişli yetki (bir ajan, başkası üzerinden etki yaptıramaz) | Dolaylı yoldan yasak etki önlenir | "An agent with no direct … route may still obtain effect" (→S1, S12) | Tasarım dikkati | – | K73, K65 |
| Zorlama ile tavsiye haritası (hangi kural hook ya da izinle zorlanıyor, hangisi yalnız talimat) | Kontrol yanılsaması önlenir | "Advisory instruction ≠ deterministic enforcement" (→S19) | Harita bakımı | – | K85, K71, K67 |

**S16 zayıfsa:** Etki gücü yetki sanılır (→S1). Kontrolsüz tetik maliyeti büyür (→S20). Yetkisiz yazım kanonik kaydı bozar (→S9). Oturum yanlış bir talimatla devam eder (→S18).

#### S17 — Gözlemlenebilirlik ve ilerleme

**Amaç:** Ne olduğunu, ne kadar ilerlendiğini ve nerede takılındığını görünür kılmak. Bunu canlılığı değil ilerlemeyi ölçerek yapmak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Olay ve iş günlüğü (hangi ajan, hangi brief, ne döndü, ne commit edildi) | Denetim ve teşhis mümkün olur | Ne olduğu sonradan kurulamaz (→S21, S18) | Satır başına kayıt | – | K71, K59 |
| İlerleme ölçüsü (kapanan soru, verilen karar, kabul edilen çıktı; "son karardan bu yana ne kadar zaman geçti") | Canlılık ilerleme sanılmaz | 742 koşu ve 54 gün (→S5, S1) | Düşük | – | K25, K110 |
| Takılma tespiti ve türü (engelli, bekliyor, işçi yok, işçi kayıp, hareket var ama ilerleme yok) | Doğru müdahale seçilir | Takılma yanlış teşhis edilir (→S12, S18) | Sınıflama | – | K79 |
| Alarm ve bildirim eşikleri (örneğin N kalem ya da N oturum boyunca karar yoksa ilk söylenen şey bu olur) | Fren kendiliğinden devreye girer | Sürekli yetki frensiz kalır (→S1, S2) | Eşik ayarı | – | K25, K90 |
| Metriklerin anlam bütünlüğü (aynı ölçü farklı tüketicilerde aynı anlamda mı; bilinmeyen ≠ sıfır) | Ölçüye dayalı karar yanlış tetiklenmez | Kümülatif maliyetin toplanması durdurma kararını bozabilir (→S20) | Tanım | – | K74, K72 (F14) |
| Açılış sinyali (oturum başında ilerleme ve hijyen özeti) | Her oturum ilk olarak takılmayı görür | Takılma oturumlar boyunca sessiz kalır (→S18) | Düşük | – | K25, K88 |
| Hatırlatma kaydı (S2 ile ortak) ve maliyet görünürlüğü (S20 ile ortak) | Gizli yük ve harcama görünür | (bkz. S2, S20) | – | – | K05, K81 |

**S17 zayıfsa:** Plan kayması görünmez olur (→S5). Batu durumu sormadan bilemez (→S2). Neyin işe yaradığı ölçülemez (→S21). Sürekli yetki frensiz kalır (→S1). Gözlem, güvence değildir: telemetri yalnız kanıt altyapısıdır [K72 (F18)].

### Grup F — Dayanıklılık ve evrim

#### S18 — Süreklilik ve kurtarma

**Amaç:** Oturum değişimi, sıkıştırma, VM kaybı ve aktör değişimi arasında işin amacı, yetkisi, durumu ve açık yükleriyle kaldığı yerden doğru devam etmesini; yarım kalan işin güvenle toparlanmasını sağlamak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Oturum açılış protokolü (okuma sırası; önceki devir notu iddia sayılır ve git geçmişiyle karşılaştırılır) | Bayat devir notu yön vermez | "Checkpoint … is newest ≠ … still current truth" (→S5, S1) | Açılış okuması | – | K110, K79, K67 |
| Oturum ve kalem kapanış protokolü (kayıt, commit, push; açık yükler; sonraki başlangıç noktası) | Taze oturum işi geri kazanır | Tartışma ve düzeltme kalıcılaşmaz (→S8) | Kapanış başına kısa iş | – | K41, K82 |
| Kontrol noktası ve commit ritmi (VM kaybında commit edilmemiş iş kaybolur) | Kayıp en fazla bir kalem kadar olur | Yarım iş ve bulgular kaybolur (→S12) | Commit disiplini | – | K19, K17 |
| Sıkıştırmaya dayanıklılık (kritik durum dosyada; sıkıştırmadan sonra yeniden okuma) | Sıkıştırma kayma yaratmaz | Ara akıl yürütme ve kurallar kaybolur (→S15, S7) | Yeniden okuma maliyeti | – | K18, K23 |
| Yarım kalan alt ajan işinin tespiti ve yeniden başlatılması (aynı brief'le; kısmi yazımların uzlaştırılması) | Makine kaybı iş kaybına dönmez | Eksik not fark edilmez ya da çakışan kısmi yazım kalır (→S12, S9) | Düşük | – | K79, K109 |
| Uyandırma ve devam mekanizması (alt ajan bitince ana oturum yeniden çağrılır; send_later ve Routine'ler bu ortamda denenmedi) | "Devam" yazma yükü Batu'dan kalkar | Batu tetikleyici olur (→S2) | Canlı sınama gerekiyor | – | K104, K19 |
| Devir kimliği ve dal politikası (hangi dal, hangi HEAD; yayın ≠ içerik kimliği) | Doğru durumdan devam edilir | EXP-005: devir main'den başlayacaktı, iş PR dalındaydı (→S2, S9) | Politika kararı | – | K35, K87, K39 |
| Soğuk başlangıç testi (konuşmayı hiç görmemiş taze oturuma yalnız repo verilir) | Süreklilik okumayla değil davranışla sınanır | "Fresh-session continuation yalnız dosya okunmasıyla test edilmiş sayılmaz" (→S14) | Bir alt ajan koşusu | Aşama içinde; aşama sonunda gereksiz değil | K62, K110 |
| Bilinmeyen etki ve kör yeniden deneme yasağı (zaman aşımı "olmadı" demek değildir; kısmi yazım olabilir) | Çift ya da kısmi etki önlenir | Aynı iş iki kez yazılır ya da yarım kalır (→S9) | Kontrol adımı | Yan etkisi olmayan okuma işlerinde | K61, K59 |

**S18 zayıfsa:** Plan sürümleri karışır (→S5). Devri Batu hatırlatır (→S2) [K35]. Dallar ayrışır (→S9). Belleğin kalıcılığı ancak kapanış protokolüyle anlam kazanır (→S8).

#### S19 — Ortam, araçlar ve yapılandırma (genişletildi)

**Amaç:** Claude Code cloud'un gerçek kabiliyetlerini ve sınırlarını bilmek. Yöntemin dayandığı yapılandırmayı (CLAUDE.md, `.claude/agents`, skills, hook'lar, izinler) sürümlü tutmak, yüklendiğini doğrulamak ve zorlama ile tavsiyeyi ayırmak.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Kabiliyet ve sınır haritası; her satırda kanıt türü (belge / gözlem / denenmedi) | Tasarım gerçek ortama dayanır | Belgeden çıkarılan yanlış kabiliyet, örneğin iç içe alt ajan (→S12) | Bakım | – | K16, K19, K91 |
| Canlı doğrulama seti (uyandırma, tetik, izin davranışı) | "Belgede var" ile "burada çalışıyor" ayrılır | Süreklilik kâğıt üstünde kalır (→S18) | Deneme maliyeti; Batu izni | – | K104 |
| Yapılandırmanın kod gibi yönetilmesi (repo'da, sürümlü; kullanıcı düzeyindeki `~/.claude` cloud'a taşınmaz) | Her yeni oturum aynı yöntemi yükler | Yöntem oturumdan oturuma değişir (→S3, S11) | Batu onayı (A-04) | – | K17, K92 |
| Yükleme doğrulaması (talimat dosyası gerçekten yükleniyor mu) | Yazılı disiplin gerçekten bağlama girer | AGENT.md otomatik yüklenmiyor; CLAUDE.md yok (→S15, S18) | Düşük | – | K16, K78 |
| Zorlama ve tavsiye katmanı (CLAUDE.md bağlamdır; hook ve izin zorlar; `settings.json` hook'ları yalnız tek repolu oturumda) | Kural doğru katmana yerleşir | Tavsiye zorlama sanılır (→S16) | Katman seçimi | – | K71, K17 |
| Yapılandırma değişikliğinin regresyon kontrolü (CLAUDE.md, rol, skill ya da model değişince yeniden sınama; politika ile kopyası arasındaki kayma) | Yapılandırma sessizce bozulmaz | Değişiklik sonrası davranış kayar; kopyalar ayrışır (→S21, S9) | Sınama maliyeti | Değişiklik yoksa | K73, K72 (F16, F17) |
| Model ve efor seçimi politikası | İş, uygun model ve efor düzeyiyle eşleşir | Ya gereksiz maliyet ya yetersiz kalite (→S20, S14) | Düşük | – | K70, K71 |
| İzin modu ve onay davranışı (Auto mod; yanıtsız onay istemi işi bekletir) | Özerk koşu onay isteminde takılmaz | Oturum beklerken VM geri alınır (→S18) | Ayar | – | K104, K17 |
| Platform değişikliği takibi (özellikler hızla değişiyor) | Düzen belirli bir özelliğe değil ilkeye dayanır | Arka plan varsayılanı değişince iş akışı takıldı (→S12, S18) | Periyodik kontrol | – | K79, K110 |

**S19 zayıfsa:** Muhakeme disiplini yüklenmez (→S15). Varsayılan mekanizma çalışmaz (→S18). Tavsiye zorlama sanılır (→S16). Topoloji depth = 1 bilinmeden kurulur (→S12).

#### S20 — Maliyet ve kaynak

**Amaç:** Token, kullanım limiti, zaman ve paralellik harcamasını işin değerine göre bütçelemek; limite çarpmayı önceden görmek.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Bütçe ve harcama kaydı (koşu ve aşama başına) | Harcama işin değeriyle karşılaştırılır | P0.3'e kadar 4,1 M token; bütçe yoktu (→S12, S3) | Düşük | – | K81 |
| Limit farkındalığı (5 saatlik ve haftalık limitler hesapta paylaşılıyor; limitte duruş ve yeniden başlama) | Duruş öngörülür | Büyük bir fan-out haftalık limiti bitirebilir (→S12, S18) | Düşük | – | K22 |
| Paralellik tavanı (eşzamanlı alt ajan sayısı ve fan-out boyutu) | Hız, limitle ve inceleme kapasitesiyle dengelenir | Limit tükenir, iş yarım kalır (→S12) | Hız kaybı | – | K22, K72 (F10) |
| Model ve efor seçimi (S19 ile ortak) | Pahalı model gereken yerde kullanılır | (bkz. S19) | – | – | K70 |
| Kontrol maliyeti orantısı (aynı modelle iç içe inceleme pahalı ve korele) | Güvence ile maliyet dengelenir | Tek bir iç içe inceleme yaklaşık 15 M token tuttu (→S14) | Düşük | – | K80 |
| Ölçünün doğruluğu (bilinmeyen ≠ sıfır; kümülatif satırlar toplanmaz) | Bütçe kararı doğru veriye dayanır | Yanlış durdurma ya da kör harcama (→S17) | Tanım | – | K74 |
| Uyanma maliyeti (önbellek süresi dolduktan sonra uzun konuşma yeniden okunur; taze oturum tercih edilir) | Uzun oturum pahalı hale gelmez | Her uyanış pahalı olur (→S18) | Oturum planlaması | – | K103 |

**S20 zayıfsa:** Paralellik limiti tüketir ve iş durur (→S12). Maliyet baskısıyla kontrol kırpılır (→S14). Limitte kesinti olur (→S18). Batu beklenmedik bir duraklamayla karşılaşır (→S2).

#### S21 — Öğrenme ve uyarlama

**Amaç:** Hatalardan ve deneyimden gerekçeli, sınanmış yöntem değişiklikleri çıkarmak; değişikliğin davranışı gerçekten değiştirdiğini doğrulamak; gerektiğinde sadeleştirmek. Çalışma düzeninin kendisi de bu alt sistemin nesnesidir.

| Bileşen | Ne işe yarar | Yokluğunda ne bozulur | Bedel | Ne zaman gereksiz | Kanıt |
|---|---|---|---|---|---|
| Olay ve hata sınıflandırması (bilgi eksikliği / belirsiz talimat / mekanik değişmez / kabiliyet sınırı / yanlış çerçeve / bayat ortam; hangi alt sistem) | Düzeltme doğru yere gider | Her hataya daha çok talimat eklenir (→S19, S7) | Teşhis zamanı | – | K71, K61 |
| Ders kaydı (tetikleyen hata; kaynak: Batu mu söyledi, çıkarım mı; nereye işlendi; durum "doğrulanmadı") | Ders izlenebilir olur | Aynı hata tekrarlanır (→S2) | Satır başına kayıt | – | K110 (A003 §3.10) |
| Dersin yerinin seçimi (yasak / tarif / zorunlu alan / koşul / mekanik kontrol / "yeni kural yok") | Ders doğru katmana girer | Talimat birikir (→S19) | Karar | – | K33, K68, K71 |
| Davranış değişiminin doğrulanması (edinim / kalıcılık / ifade; sonraki bir oturumda gözlem) | Kayıtlı ders ile değişen davranış ayrılır | "Kısa cevap kuralı vardı, cevaplar yine uzun kaldı" (→S15, S2) | Gözlem | – | K48, K44, K61 |
| Retrospektif ritmi (aşama sonu) | Deneyim düzenli olarak işlenir | Ders fırsatları kaybolur (→S3) | Aşama başına kısa iş | – | K110 |
| Yöntem değişikliği kontrolü (METHOD değişikliği de bir iştir; kabul, sürüm, Batu onayı gereken kısımlar) | Yöntem sessizce kaymaz | Ajan kendi kurallarını yeniden yazar (→S1) | Onay | – | K112, K92 |
| Sadeleştirme ve kaldırma (ablation, deprecation) | Yöntem yalnız büyümez | "Kendi ağırlığı altında durdu" (→S3, S20) | Periyodik gözden geçirme | – | K28, K62 |
| Yöntemin sınanması (pilot, soğuk başlangıç, gerçek işte gözlem) | "İşe yaradı" iddiası kanıta dayanır | Tasarlayan ile denenen aynı olduğu için kendini aklama (→S14) | Deneme maliyeti | – | K110 (A003 §6, §5) |
| P3 kanıtı olarak kayıt (bu düzenin işleyişi DevOS için kanıttır, ama DevOS'un düzeni değildir) | DevOS'a kanıtsız aktarım önlenir | "İşe yaradı" diye taşınır (→S1) | Düşük | – | K110 (A003 §3.10) |

**S21 zayıfsa:** Defolar tekrarlanır (→S15). Yöntem ya şişer ya donar (→S3). Yapılandırma kurallarla dolar (→S19). Batu aynı şeyi yeniden anlatır: "Ben bunu geçen hafta da aynı şekilde anlatmıştım" [K82] (→S2).

## 4. Etkileşim matrisi

### 4.1 Nasıl okunur

- **Satır X zayıfsa, sütun Y bozulur.** Hücredeki numara, §4.4'teki kenarın kimliğidir (E01, E02 …).
- **İşaretler:**
  - ● bu örüntü Batu'nun projelerinde yaşanmış bir olayla destekleniyor (EXP-004/005/006, Foundation, loopinance, kanon, EXP-007);
  - ◐ bir kaynak (belge, çalışma, kavramsal analiz) böyle diyor, ama olay olarak gözlenmedi;
  - ○ benim çıkarımım.
- **Boş hücre "etki yok" demek değildir;** o bağ için kanıt ya da güçlü bir gerekçe aranmadı ya da bulunamadı.
- **Çıkış sayıları anlamlı değildir.** Her satır için 3–6 kenar yazdım. Satırların çıkış sayıları bu seçimimi yansıtır; bir ölçüm değildir. Anlamlı olanlar giriş sayıları ve ● sayılarıdır (§4.3).

### 4.2 Matris

| zayıf ↓ / bozulan → | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **S1** Yetki | · | 01● |  |  | 03● |  |  |  |  |  |  | 06○ |  | 05◐ |  | 04◐ |  | 02◐ |  |  |  |
| **S2** Batu | 07● | · |  | 11● | 10◐ |  |  |  |  |  |  |  |  | 08● |  |  | 09◐ |  |  |  |  |
| **S3** Yöntem |  |  | · |  | 12● |  |  |  |  |  |  |  |  | 15◐ |  |  | 13◐ |  |  | 14● | 16● |
| **S4** Keşif |  | 17● |  | · | 18● | 21◐ |  |  |  |  | 20● |  |  | 19● |  |  |  |  |  |  |  |
| **S5** Plan |  | 24● |  |  | · |  |  |  | 26◐ |  |  | 25○ |  |  |  |  | 22◐ | 23● |  |  |  |
| **S6** Araştırma |  |  |  | 27● |  | · |  |  |  |  |  |  |  | 29● | 28◐ |  |  |  | 30● |  |  |
| **S7** Bağlam |  |  |  |  |  |  | · |  |  |  |  | 31◐ | 35◐ |  | 34◐ |  |  | 32◐ |  | 33● |  |
| **S8** Bellek |  |  |  |  |  |  | 39● | · |  | 40◐ | 37○ |  |  |  |  |  |  | 36● |  |  | 38◐ |
| **S9** Kayıt | 43◐ | 44● |  |  | 42● |  | 45● |  | · |  |  |  |  | 46● |  |  |  | 41● |  |  |  |
| **S10** Anlam | 47● | 50● |  | 51◐ |  |  |  |  |  | · |  |  |  | 49◐ |  |  |  | 48◐ |  |  |  |
| **S11** Rol |  |  |  |  |  |  |  |  |  |  | · | 54● | 52◐ |  |  | 55◐ |  |  |  |  | 53○ |
| **S12** Orkestrasyon |  | 59● |  |  |  |  | 57◐ |  | 61◐ |  |  | · |  | 56◐ |  |  |  | 60◐ |  | 58◐ |  |
| **S13** Arayüz |  |  |  |  |  |  |  |  |  | 62◐ |  | 65◐ | · | 63● | 64◐ |  |  |  |  |  | 66◐ |
| **S14** KG | 67● | 70◐ |  |  |  |  |  |  |  |  |  |  |  | · |  |  | 69◐ |  |  |  | 68● |
| **S15** Muhakeme | 75● | 72● |  |  | 73● |  |  |  |  | 74◐ |  |  |  | 71◐ | · |  |  |  |  |  |  |
| **S16** Güvenlik | 76◐ |  |  |  | 77◐ |  |  |  | 79○ |  |  |  |  |  |  | · |  |  |  | 78◐ |  |
| **S17** Gözlem | 81◐ | 82● |  |  | 80● |  |  |  |  |  |  |  |  |  |  |  | · |  |  | 84◐ | 83◐ |
| **S18** Süreklilik |  | 85● |  |  | 86● |  |  |  | 87● |  |  | 88◐ |  |  |  |  |  | · |  |  |  |
| **S19** Ortam |  |  |  |  |  |  |  | 101◐ |  |  |  | 90◐ |  | 93● | 89◐ | 92◐ |  | 91◐ | · |  |  |
| **S20** Maliyet |  |  |  |  |  |  |  |  |  |  |  | 95◐ |  | 94◐ |  |  |  | 96◐ |  | · |  |
| **S21** Öğrenme |  | 99● | 100● |  |  |  |  |  |  |  |  |  |  |  | 97● |  |  |  | 98◐ |  | · |

### 4.3 Sayımlar: nerede toplanıyor, nereden kaynaklanıyor

Toplam 101 kenar: 44 tanesi ● (olayla destekli), 52 tanesi ◐ (kaynak diyor), 5 tanesi ○ (çıkarım). Tablo, olayla desteklenen giriş sayısına göre sıralıdır.

| Alt sistem | Giriş (onu bozan alt sistem sayısı) | ● giriş | Çıkış | ● çıkış |
|---|:-:|:-:|:-:|:-:|
| S2 Batu | 11 | 10 | 5 | 3 |
| S5 Plan | 9 | 7 | 5 | 2 |
| S14 KG | 12 | 6 | 4 | 2 |
| S1 Yetki | 7 | 4 | 6 | 2 |
| S18 Süreklilik | 9 | 3 | 4 | 3 |
| S21 Öğrenme | 6 | 2 | 4 | 3 |
| S20 Maliyet | 5 | 2 | 3 | 0 |
| S4 Keşif | 3 | 2 | 5 | 4 |
| S7 Bağlam | 3 | 2 | 5 | 1 |
| S12 Orkestrasyon | 8 | 1 | 6 | 1 |
| S15 Muhakeme | 5 | 1 | 5 | 3 |
| S9 Kayıt | 4 | 1 | 6 | 5 |
| S11 Rol | 2 | 1 | 4 | 1 |
| S19 Ortam | 2 | 1 | 6 | 1 |
| S3 Yöntem | 1 | 1 | 5 | 3 |
| S17 Gözlem | 4 | 0 | 5 | 2 |
| S10 Anlam | 3 | 0 | 5 | 2 |
| S16 Güvenlik | 3 | 0 | 4 | 0 |
| S13 Arayüz | 2 | 0 | 5 | 1 |
| S6 Araştırma | 1 | 0 | 4 | 3 |
| S8 Bellek | 1 | 0 | 5 | 2 |

### 4.4 Kenar listesi

Biçim: **Exx** X→Y işaret — X zayıfsa Y şöyle bozulur. [kanıt]


**S1 Yetki zayıfsa:**

- **E01** S1→S2 ● — Sürekli yetki repoda çözülemezse kurallar her aşama sınırında durdurur; “devam” yükü Batu’ya döner. [K88, K04]
- **E02** S1→S18 ◐ — Yetki yalnız sohbette kalırsa sonraki oturumda yoktur; uyandırılan oturum ya fail-closed durur ya kapsamı uydurur. [K105, K88]
- **E03** S1→S5 ● — Çerçeve değişikliği kontrolü yoksa plan bir önceki turun seçimiyle kayar. [K46, K111]
- **E04** S1→S16 ◐ — Yetki ile teknik erişim ayrılmazsa araç gücü yetki sanılır. [K65, K85]
- **E05** S1→S14 ◐ — Kabul hakkı doğrulamadan ayrılmazsa Batu’nun onayı teknik doğrulama sayılır. [K72, K107]
- **E06** S1→S12 ○ — Karar hakları tanımsızsa koordinatör, akış sahipliğinden karar sahipliğine kayar. [K66]

**S2 Batu zayıfsa:**

- **E07** S2→S1 ● — Kabul paketi yoksa kabul törene döner: “Onaylar seremoniye döndü. Mühürler itirazsız geçti.” [K29]
- **E08** S2→S14 ● — Batu’nun dikkati tükenirse çerçeve hatalarını yakalayan tek aynı-model-olmayan kanal kapanır; beş olayın dördünde hatayı Batu yakaladı ya da onarımı o başlattı. [K35, K41, K53, K54]
- **E09** S2→S17 ◐ — Kontrol noktası raporu tanımsızsa özerk koşunun ne yaptığı ancak commit okunarak görülür. [K89]
- **E10** S2→S5 ◐ — Soru kuyruğu yoksa sorular sahipsiz kalır, “sonraki açılışta” cevaplanır ya da kaybolur. [K34]
- **E11** S2→S4 ● — Keşif sisteme verilmezse Batu keşfeder: erişim, kaynak kapsamı, yayın ve devir hatırlatmaları kullanıcıdan geldi. [K37]

**S3 Yöntem zayıfsa:**

- **E12** S3→S5 ● — Aşama haritası yoksa yön bir önceki turdan gelir (EXP-006 E1). [K46, K110]
- **E13** S3→S17 ◐ — Bitti tanımı ve kapı yoksa ilerleme ölçülemez; dar soru zincirleri üst teslimata dönmez. [K108, K110]
- **E14** S3→S20 ● — Tören orantısı yoksa yöntem kendi ağırlığı altında durur; sabit kapanış ritüeli her geçişte ödenir. [K28, K34]
- **E15** S3→S14 ◐ — Kapı tanımsızsa ya her şeye tören yapılır ya hiçbir şey kontrol edilmez. [K10, K76]
- **E16** S3→S21 ● — Meta-iş sınırı yoksa süreç ürüne dönüşür: KEEL’e yaklaşık 90 commit; EXP-006’da 17 dilim, platform hiç araştırılmadı. [K27, K46]

**S4 Keşif zayıfsa:**

- **E17** S4→S2 ● — Keşif zayıfsa eksik işi Batu bulur (soru bankası; EXP-005’in sonucu). [K41, K38]
- **E18** S4→S5 ● — Plan yalnız bilinen işi taşır; gerekli iş hiç görünmez. [K79]
- **E19** S4→S14 ● — Doğrulama yalnız plandaki işi sınar; eksik iş “tamam” damgası alır: “The assistant nevertheless declared the example finished.” [K41]
- **E20** S4→S11 ● — Çerçeve yeterliği sınanmazsa roller yanlış kaynaktan türer. [K52]
- **E21** S4→S6 ◐ — Kaynak alanı dar seçilirse birikim olduğu halde uygulanmaz. [K40, K41]

**S5 Plan zayıfsa:**

- **E22** S5→S17 ◐ — Kalem statüsü ve bitti tanımı yoksa ilerleme ölçüsünün dayanağı kalmaz. [K112]
- **E23** S5→S18 ● — Neyin kapandığı, neyin devralındığı kayıtlı değilse yeniden giriş güvenilmez olur. [K36]
- **E24** S5→S2 ● — Kötü tanımlanmış dilim Batu’ya soru üretir; 16 görevin hiçbiri kod üretmedi. [K30]
- **E25** S5→S12 ○ — Bağımlılık türleri ayrılmazsa paralel dağıtım yanlış sıralanır ya da gereksiz bekler. [K79]
- **E26** S5→S9 ◐ — Sapma kaydı yoksa kötü plan sonradan hep doğruymuş görünür. [K100]

**S6 Araştırma zayıfsa:**

- **E27** S6→S4 ● — Birikim uygulanmazsa keşif ilk göze çarpan görüşe çapalanır. [K41]
- **E28** S6→S15 ◐ — Araştırma izi yoksa tasarım “yalnız akıl yürütme”ye kalır. [K82, K43]
- **E29** S6→S14 ● — “Tam okudum” iddiası sınanamazsa doğrulama yanlış zemine dayanır (S1-16’nın “Tam” etiketleri). [K51]
- **E30** S6→S19 ● — Claude Code iddiası ortamda sınanmazsa yanlış kabiliyet varsayılır (“üç kat iç içe”). [K91]

**S7 Bağlam zayıfsa:**

- **E31** S7→S12 ◐ — Ana oturum yalnız özetlerle birleştirirse kaynaklar arası ilişkiler karşılaştırılmaz. [K56, K06]
- **E32** S7→S18 ◐ — Sıkıştırmadan önce kayıt yoksa ara akıl yürütme ve araç çıktıları kaybolur. [K18]
- **E33** S7→S20 ● — Açılış seti şişerse her oturum pahalılaşır (110 KB, sınır 50 KB). [K26]
- **E34** S7→S15 ◐ — Sıkıştırmada kurallar özetlenirse davranış kayar; önceki talimatlar “unutulur”. [K18, K23]
- **E35** S7→S13 ◐ — Brief yalnız dosya yolu verirse alt ajan içeriği görmeyebilir. [K84]

**S8 Bellek zayıfsa:**

- **E36** S8→S18 ● — Yazma politikası yoksa tartışma ve düzeltme kalıcılaşmaz: “The intervening discussion and its correction had not been persisted.” [K41]
- **E37** S8→S11 ○ — Rol belleği yoksa rol birikim taşımaz; her çağrı sıfırdan başlar. [K02, K21]
- **E38** S8→S21 ◐ — Ders bulunabilir ve seçilebilir değilse davranış değişmez. [K61, K44]
- **E39** S8→S7 ● — Bellek taşıdığı işten ağırlaşınca açılış bağlamı dolar. [K26]
- **E40** S8→S10 ◐ — Türetilmiş bellek kanonik kaydı ezerse iş yanlış statüyle sürer. [K63, K67]

**S9 Kayıt zayıfsa:**

- **E41** S9→S18 ● — Aynı durum çok dosyada kopyalanırsa çelişen yüzeyler oluşur; yeni oturum yanlışını okur ya da durur. [K49, K86]
- **E42** S9→S5 ● — Tek kaynak yoksa karar değişikliği pahalılaşır (14 spec). [K31]
- **E43** S9→S1 ◐ — Bayat yönlendirici oturumu yanlış işe götürür ve yetki çelişkisi doğurur. [K88, K92]
- **E44** S9→S2 ● — Yayın görünümü ile içerik kimliği karışırsa yayını Batu kontrol etmek zorunda kalır. [K39, K37]
- **E45** S9→S7 ● — Kayıt şişerse (6 dakikada 36 commit; 27 dosyada kalıp not) okuma yükü artar. [K94, K95]
- **E46** S9→S14 ● — Başarılı merge ve readback, kaynak sadakatinin kanıtı sanılır. [K54]

**S10 Anlam zayıfsa:**

- **E47** S10→S1 ● — Batu’nun düzeltmeleri parafrazda yaşarsa kararları yanlış okunur. [K49]
- **E48** S10→S18 ◐ — Devir özetinde nitelik düşerse ardıl, kabul edilmemiş sonucu güncel sanar (kurulu karşıörnek). [K55, K67]
- **E49** S10→S14 ◐ — Yanlış cümle içermeyen bir özet, hükmün ihtiyaç duyduğu ayrımı kaybedebilir (kurulu karşıörnek). [K56]
- **E50** S10→S2 ● — Terim kayması Batu’nun metni izlemesini zorlaştırır (“motivasyon” → “başarı yönü”). [K50]
- **E51** S10→S4 ◐ — Batu’nun örneği kapsam sanılırsa keşif daralır. [K82]

**S11 Rol zayıfsa:**

- **E52** S11→S13 ◐ — Rol her görevde yeniden biçilirse brief’ler uzar ve tutarsızlaşır (K-007’nin eleştirisi). [K02, K08]
- **E53** S11→S21 ○ — Kalıcı rol yoksa dersler bağlanacak bir taşıyıcı bulamaz. [K02]
- **E54** S11→S12 ● — Rol sınırı dosya sahipliğiyle katılaşırsa her devir yeni bir oturum ister (kanon). [K34]
- **E55** S11→S16 ◐ — Rol başına araç sınırı yoksa alt ajan durum değiştiren araçlara erişir. [K24]

**S12 Orkestrasyon zayıfsa:**

- **E56** S12→S14 ◐ — Birleştirme sözleşmesi yoksa tek tek sağlam dönüşler yanlış bir bütüne birleşir. [K76]
- **E57** S12→S7 ◐ — Tek koordinatör her şeyi taşırsa bağlamı dolar ve darboğaz olur. [K09, K108]
- **E58** S12→S20 ◐ — Paralel fan-out limitleri tüketir; tek bir iç içe inceleme yaklaşık 15 M token tuttu. [K22, K81, K80]
- **E59** S12→S2 ● — Koordinasyon sistemde değilse Batu zamanlayıcıya dönüşür (kanon). [K34, K32]
- **E60** S12→S18 ◐ — Arka plan ajanları VM kaybında gider; topoloji kaydı yoksa yarım iş kaybolur. [K19, K79]
- **E61** S12→S9 ◐ — Tek yazıcı kuralı yoksa paralel yazımlar kanonik dosyada çakışır. [K59]

**S13 Arayüz zayıfsa:**

- **E62** S13→S10 ◐ — Dönüş şeması statüyü taşımazsa nitelik kaybolur. [K83]
- **E63** S13→S14 ● — Dönüş veri sayılmazsa yanlış iddia karara girer (“üç kat iç içe”). [K91]
- **E64** S13→S15 ◐ — Brief rota, hedef ve ölçüt vermezse alt ajan emir erine döner. [K82]
- **E65** S13→S12 ◐ — Aynı eksik brief birkaç inceleyiciye verilirse eksik hepsinde ortak kalır. [K101]
- **E66** S13→S21 ◐ — Brief sürümü kaydedilmezse hangi değişikliğin etkili olduğu ölçülemez. [K109]

**S14 KG zayıfsa:**

- **E67** S14→S1 ● — Aynı yazar kendi işini denetlerse hiçbir aday elenmez; Batu’nun önüne sınanmamış seçenek gelir. [K47]
- **E68** S14→S21 ● — Denetçi hataya duyarsızsa yöntem karşılaştırması ayırt edemez (iki tarafa da 4/4 PASS). [K96]
- **E69** S14→S17 ◐ — “Tamam” denetlenmezse ilerleme ölçüsü şişer. [K69, K33]
- **E70** S14→S2 ◐ — Doğrulama zayıfsa Batu hata avcısına dönüşür; oysa Batu’nun sonradan itirazı temel kalite kontrolü olamaz. [K77]

**S15 Muhakeme zayıfsa:**

- **E71** S15→S14 ◐ — Denetçi aynı modelse aynı defoyu paylaşır; muhakeme disiplini doğrulamanın taban kalitesidir. [K106, K33]
- **E72** S15→S2 ● — Sahte menü, aşırı sorma ve karar-yükleme Batu’ya yük olur; teknik sorular Batu’ya gitti. [K33, K30]
- **E73** S15→S5 ● — Çapa dosyadan yüklenmezse tur yerel optimuma çekilir (drift). [K33, K46]
- **E74** S15→S10 ◐ — Aynalama ve uydurma anlamı bozar: “Biz de bunu ‘anladı’ sanıyoruz.” [K33, K82]
- **E75** S15→S1 ● — Öz-onay kapanışı hızlandırır, kapanış da yetki sınırını zorlar: S1-17 “kapanışa hazır” dedi ve SOUL’un ilk işini asistanın seçmesini önerdi; Batu reddetti (D012). [K111, K47]

**S16 Güvenlik zayıfsa:**

- **E76** S16→S1 ◐ — Okunan talimat yetki sayılırsa yetkinin kaynağı bozulur. [K44, K78]
- **E77** S16→S5 ◐ — Eski “sıradaki” satırları talimat sayılırsa plan eski yöne çekilir (K-004). [K92, K49]
- **E78** S16→S20 ◐ — Durum değiştiren araçlar sınırsızsa kontrolsüz oturum ve tetik maliyeti doğar. [K24]
- **E79** S16→S9 ○ — Yazma sınırı zorlanmazsa alt ajan kanonik kaydı bozabilir; broker yaptırım değildir. [K59]

**S17 Gözlem zayıfsa:**

- **E80** S17→S5 ● — Canlılık ölçülüp ilerleme ölçülmezse 54 günlük duraklama fark edilmez. [K25]
- **E81** S17→S1 ◐ — Sürekli yetki frensiz kalır; özerk döngü ilerleme yokken ilerleme bildirebilir. [K90, K25]
- **E82** S17→S2 ● — Pano bayatlarsa Batu’nun tek döngüsü yanlış yönlenir (“sıradaki oturum” satırı bayat ve yanlıştı). [K25]
- **E83** S17→S21 ◐ — Ölçüm yoksa “ders işe yaradı” iddiası kanıtsız kalır. [K62, K44]
- **E84** S17→S20 ◐ — Maliyet ölçüsü anlamını kaybederse durdurma kararı yanlış tetiklenir. [K74]

**S18 Süreklilik zayıfsa:**

- **E85** S18→S2 ● — Devir kimliği doğrulanmazsa hatayı Batu yakalar (EXP-005 U044). [K35]
- **E86** S18→S5 ● — Yeniden girişte kapanan ve açık kalanın izi yoksa iş tekrarlanır ya da kaybolur. [K36]
- **E87** S18→S9 ● — Dal politikası belirsizse kanonik durum bölünür; U005 çakışması. [K87]
- **E88** S18→S12 ◐ — Uyandırma ve yarım iş tespiti yoksa alt ajan sonuçları kaybolur. [K19, K104]

**S19 Ortam zayıfsa:**

- **E89** S19→S15 ◐ — Talimat dosyası kendiliğinden yüklenmiyorsa disiplin yalnız istemde yaşar (CLAUDE.md yok; gözlem). [K16, K78]
- **E90** S19→S12 ◐ — Belge ortamla sınanmazsa topoloji yanlış kurulur (depth = 1). [K16, K91]
- **E91** S19→S18 ◐ — Denenmemiş uyandırma mekanizmasına dayanılırsa süreklilik kâğıtta kalır. [K104]
- **E92** S19→S16 ◐ — Tavsiye zorlama sanılırsa kontrol yanılsaması doğar. [K71, K67, K85]
- **E93** S19→S14 ● — Araç çıktısı kesilirse “tam okuma” iddiası çürür (ChatGPT dönemi). [K51]
- **E101** S19→S8 ◐ — Ortam gerçeği bilinmezse bellek makinede tutulur ve cloud’da kaybolur (auto memory; commit edilmemiş rol belleği). [K20, K21]

**S20 Maliyet zayıfsa:**

- **E94** S20→S14 ◐ — Bütçe baskısı kontrolü kırpar; bütçenin bitmesi “bitti” sanılır. [K83]
- **E95** S20→S12 ◐ — Limit dolunca paralel iş durur ve yarım kalır. [K22]
- **E96** S20→S18 ◐ — Uyanma maliyeti uzun oturumu pahalı kılar; planlı taze oturum gerekir. [K103]

**S21 Öğrenme zayıfsa:**

- **E97** S21→S15 ● — Yazılı kural davranışa dönüşmez; aynı hata tekrarlanır (D010). [K48]
- **E98** S21→S19 ◐ — Her hata için talimat eklenirse CLAUDE.md şişer (talimat birikimi). [K71]
- **E99** S21→S2 ● — Ders kalıcılaşmazsa Batu aynı şeyi yeniden anlatır. [K82, K02]
- **E100** S21→S3 ● — Sadeleştirme yoksa yöntem yalnız büyür ve sonunda durur. [K28, K62]


### 4.5 Sayımların yorumu ve birbirini besleyen döngüler

**Batu bir "havuz".** Olayla desteklenen 44 kenarın 10'u S2'de bitiyor. A003'ün başarı ölçüsü, yani Batu'nun hatırlatma sayısı [K05], bu havuzu ölçer (çıkarım).
- Ölçü değerlidir ama gecikmelidir. Batu fark ettiğinde hata çoktan yayılmıştır.
- Seçim etkisi taşır: Batu'nun görmediği hata sayılmaz.

Standart seviyede bu ölçü tek başına kalmamalı. Yanında kaynak alt sistemlerde erken uyarı veren ölçüler olmalı:
- yayılım kontrolü (S9);
- "kimseye verilmemiş iş" taraması (S4);
- ilerleme ölçüsü (S17).

**Kalite güvencesi en çok etkilenen alt sistem (12 giriş).** Pek çok zayıflık, "yanlış bir şeyin doğrulamadan geçmesi" olarak ortaya çıkıyor. Doğrulama yalnız kendisine verileni sınayabilir; ne yakalayabileceğini girdileri belirler:
- plandaki iş kapsamı (S4);
- özetin sadakati (S10);
- okuma iddiası (S6);
- birleştirme (S12);
- dönüş biçimi (S13).

Bu yüzden S14 tek başına tasarlanamaz (çıkarım; K41, K54, K56, K76).

**Plan ve süreklilik (9'ar giriş), uzun soluklu işin birikim yerleri.** Oturumlar arası taşınan her zayıflık, sonunda yanlış plan durumu ya da yanlış devir olarak görünüyor (K35, K36, K46).

**Olayla desteklenen kaynaklar kayıt mimarisi (5) ve keşif (4).** Kayıt mimarisi sürekliliğin, bağlamın ve yetkinin şasisidir (K31, K49, K54, K86). Keşif ise "Batu'nun bulmak zorunda kaldığı" işin kaynağıdır (K38, K41, K52).

**Olay yokluğu risk yokluğu değildir.** S16 güvenlik ve S20 maliyetin olayla desteklenen çıkışı sıfır. Bunun olası nedeni, işin şimdiye kadar insan hızında ve büyük ölçüde salt okuma olarak yürümesidir. Sürekli yetki ve paralel alt ajanlarla bu iki alt sistem yük taşımaya başlar (çıkarım; K22, K24). Foundation'ın ifadesiyle: "all listed sources checked ≠ all materially relevant sources listed" (R04 (b)5).

**Birbirini besleyen döngüler.** Batu'nun "bütünsel bakış" uyarısının en somut karşılığı bunlardır: tek bir alt sistemi güçlendirmek döngüyü kırmayabilir. Her bağlantının kanıtı ayrı; döngünün kendisi çıkarım.

1. **Şişme döngüsü: S9 → S7 → S20 → S10 → S18 → S9.**
   - Kayıt şişer [K49, K94].
   - Açılış yükü artar [K26].
   - Maliyet artar; bunu azaltmak için kısa özetlere gidilir [K12].
   - Özette nitelik düşer [K67].
   - Devir hatası çıkar [K35]; onu önlemek için daha çok açıklama yazılır.
   - Loopinance'ın "kendi ağırlığı altında durma" kaydı bu döngünün uç noktasıdır [K28].
2. **Öz-onay döngüsü: S15 → S14 → S17 → S1 → S15.**
   - Öz-onay [K33] ve aynı modelle karşı-okuma [K106] ilerlemeyi şişirir.
   - İlerleme ölçüsü de şişer [K69].
   - Sürekli yetki frensiz kalır [K90]; özerk koşu uzar ve öz-onay fırsatı artar.
   - Kanondaki 742 koşu ile EXP-006'da hiçbir ailenin elenmemesi bu döngünün izleridir [K25, K47].
3. **Batu yükü döngüsü: S4 → S2 → S14 → S2.**
   - Keşif zayıfsa eksik işi Batu bulur [K37].
   - Batu'nun dikkati tükendikçe tek bağımsız kanal zayıflar [K106].
   - Daha çok hata geçer ve Batu'nun yükü artar.
   - EXP-005 bunu tek cümleyle kaydetti: "Önlemeye çalışılan kullanıcıya bağımlı … keşfi sorunu, onu düzeltmek için yürütülen süreçte yeniden ortaya çıktı." [K38]
4. **Kural birikimi döngüsü: S21 → S19 → S7 → S15 → S21.**
   - Her hata için talimat eklenir [K71].
   - Bağlam şişer [K26].
   - Sıkıştırmada kurallar özetlenir [K18].
   - Davranış değişmez [K48] ve yeni bir talimat eklenir.
   - Defo modelinin sıralaması bu döngünün panzehiri olarak okunabilir: "mekanik kapı > iz isteyen yazılı prosedür > salt öğüt" [K33].

### 4.6 Beş repo olayı: alt sistemler arası zincirler

Her zincirde ilk halka, zayıflığın başladığı alt sistemdir. Zincirler olayların kayıtlarına dayanır; alt sistemlere atama benim çıkarımımdır.

**(a) EXP-005'teki devir hataları: S19 → S9 → S18 → S2; ayrıca S5 → S18.**
- **Ortam ve erişim.** Cloud çalışması kaynak erişimi olmadan yürüdü; local'e geçişte Research deposu önce bulunamadı. Ders: ortamın adı, gerçek kabiliyetin kanıtı değildir (D03) [K40].
- **Kayıt ve yayın.** Local hash, PR head ve "1 dakika önce" görünümü birbirine karıştı (D06) [K39].
- **Devir kimliği.** Asistan "Artık doğru ortamdayız." dedi ve local oturumu `main`'den başlatacak bir devir mesajı yazdı; oysa iş PR dalındaydı. Batu sordu: "bizim cloude ortamdaki çalışma yansımamıştı onunla ilgili problem olmaz mı". Asistan kabul etti: "önceki mesajı olduğu gibi gönderseydik sorun olabilirdi" [K35].
- **Plan ile devir.** Görev sözleşmesi vardı; ama "yeniden girişlerde hangi engelin kapandığı, hangi sonucun devralındığı, hangi ana kabulün hâlâ açık olduğu güvenilir biçimde yönetilemedi" [K36].
- **Sonuç: yük Batu'da.** Erişim, kaynak kapsamı, yayın ve devir hatırlatmaları kullanıcıdan geldi [K37].

**(b) EXP-006'nın kayması: S3/S5 → S1; S4 → S11; S14 → S1; S21 → S15; S9 → S7; S10 → S2.**
- **Harita yoktu.** Yönü bir önceki tur belirledi [K46, K110].
- **Çerçeve.** Roller SOUL'un hedef yeteneklerinden türetildi, ekibin kendi çalışma döngüsünden değil [K52].
- **Öz-onay.** Aynı yazar kendi işini denetledi; hiçbir aile elenmedi [K47].
- **Öğrenme.** Kısa cevap kuralı yazılıydı, cevaplar yine uzun kaldı [K48].
- **Kayıt.** Aynı durum çok dosyada tekrarlandı; 53 bin kelimenin yalnız 1.494'ü Batu'nun sözü [K49, K94, K95].
- **Anlam.** "Motivasyon" "başarı yönü"ne dönüştü [K50].
- **Yönetişim ve süreklilik.** Repodaki durma kuralları her aşamada durmayı emretti [K88].
- **Sonuç.** Batu dokuzu aşkın kez yön düzeltmek zorunda kaldı [K53].

**(c) Foundation'daki soru bankası olayı: S6 ↛ S4 → S14 → S2; ayrıca S8 → S18.**
- **Bilgi vardı ama uygulanmadı.** Üretim tarafı yeterince sınanmadı; asistan "nevertheless declared the example finished". Eksik perspektifi Batu gösterdi [K41].
- **Foundation'ın kendi sonucu:** "The adequacy of the knowledge, its discoverability and its actual application must remain separable questions." Araştırmadan yararlanma (S6), keşif (S4) ve doğrulama (S14) ayrı alt sistemler olmalı; bu, §2'deki bölmenin doğrudan gerekçesi.
- **Süreklilik.** Tartışma ve düzeltme kalıcılaştırılmamıştı: "The intervening discussion and its correction had not been persisted." [K41]

**(d) Kanondaki bekçi, 742 koşu: S17 → S5 → S2; S11/S12 → S2; S8/S9 → S7; S5 → S2.**
- **Gözlem yanlış şeyi ölçtü.** "Bekçi 742 kez koştu ama "54 gündür kod yok" demedi." Ders 5: "İlerleme ölçülmedi, sadece canlılık ölçüldü." [K25]
- **Roller ve orkestrasyon.** Rol, oturumun açıldığı klasöre bağlıydı ve her dosyanın tek yazıcısı vardı. Her devir, Batu'nun açtığı yeni bir oturum demekti [K34]. Koordinatörün commit'lerinin %37'si "evrak"tı [K32].
- **Bellek ve bağlam.** Açılış seti 110 KB'a çıktı; sınır 50 KB'tı [K26].
- **Plan.** Motorsuz ekstre dilimi soru üretti; 16 görev hiç kod üretmedi [K30].
- **Ardıl düzenin karşılıkları.** Her ders bir mekanizmaya dönüştü: "son koddan bu yana X gün" sayacı, dilim kuralı, tek karar dosyası, defo modeli [K25, K33].
- **Çekince.** R01, kanonun sağlık dosyasında son koşunun #713 olduğunu kaydetti; arşiv 742 diyor. Sayı farkı sonucu değiştirmiyor.

**(e) EXP-004'teki özet kayıpları: S10 → S9/S14 → S18.** Gerçek olay:
- İlk arşiv S001–S013'ü kaynak aktarımı diye sundu; oysa metinler "özetlendi, yeniden ifade edildi ve bazı kaynak-sonrası cümleler eklendi". "Başarılı merge/readback kaynak sadakati kapanışı gibi sunuldu." [K54]
- Asistan bunu T08'de kendisi fark etti; onarım Batu'nun U016 talebiyle yapıldı.

Kurulu karşıörnekler (gerçek olay değil):
- T08: nitelik düşen devir özeti, tüketiciyi kabul edilmemiş sonucu güncel sanmaya götürür [K55].
- T14: yanlış cümle içermeyen bir özet "mektubu kimin gördüğünü" kaybeder [K56].

Bu olay aynı zamanda olumlu bir kanıttır: asistanın sadakat denetimi, uygulandığında hatayı yakaladı. Eksik olan, bulunan açığın kendiliğinden onarım işine dönüşmesiydi. S14 ile S5 arasındaki bağ bu yüzden önemli.

## 5. "Yeterli görünüp yetersizleştiren" seçimler

Batu'nun masaj örneğiyle aynı yapıdaki seçimler: tek alanda makul görünür, bütünde bir başka alt sistemi zayıflatır. Her madde dört satırdan oluşur: nedeni, bedeli, kanıtı ve **dengeleyicisi**. Dengeleyici, standart seviyede o seçimin yanında bulunması gereken eşlik bileşenidir. Seçimi reddetmek değil, onu frenle birlikte kurmaktır. "v0" etiketi seçimin A003'te bulunduğunu gösterir. Etiket: çıkarım; bağlantıların kanıtı köşeli parantezde.

**Y1. Kısa sohbet, ayrıntı repoda** (S2 konforu; v0 §3.9).
- *Neden yeterli görünür:* Batu uzun metinden şikâyet etti [K82].
- *Neyi zayıflatır:* Özerk koşunun ne yaptığı ancak commit okunarak görülür. Kabul ve yön düzeltmesi körleşir (→S1, S14) [K89, K29].
- *Dengeleyici:* Kontrol noktası raporu, detaya inilebilen bağlantılar, kabul paketi. Batu'nun dikkati sistemin tek aynı-model-olmayan denetçisidir; onu rahatlatan her şey güvenliği artırır. Ama "kısa" ile "görünmez" aynı şey değildir.

**Y2. "Ana oturum az okur, okumayı alt ajanlar yapar"** (S7 bağlam ekonomisi; v0 §3.9).
- *Neden yeterli görünür:* Ana oturumun bağlamı korunur; sıkıştırma sonrası yeniden yükleme ucuzlar [K06].
- *Neyi zayıflatır:* Koordinatör yalnız özetlerle karar verir ve birleştirir. Kaynaklar arası ilişkiler hiç karşılaştırılmaz. Koordinatör "görünmez düşünce filtresi"ne dönüşür (→S12, S14, S6) [K56, K66, K76].
- *Dengeleyici:* Karar taşıyan iddiaların kaynağından kontrolü (v0'da var), birlikte okuma işleri, birleştirme sözleşmesi, nitelik koruyan dönüş şeması.

**Y3. Tek soruluk geçici alt ajanlar** (S7 temiz bağlam; v0 §3.2).
- *Neden yeterli görünür:* Her görev temiz bağlamla başlar.
- *Neyi zayıflatır:* Birikim oluşmaz. Her brief rolü baştan anlatır. Dersler bağlanacak taşıyıcı bulamaz (→S11, S13, S21) [K07, K02].
- *Dengeleyici:* Kalıcı rol tanımı, rol belleği; brief yalnız göreve özgü kısmı taşır. Görev geçici kalabilir, rol kalıcı olmalıdır.

**Y4. "Üç tekrardan sonra kalıcı ajan"** (S21 kanıta dayalı genelleme; v0 §3.3).
- *Neden yeterli görünür:* Defo modeli de "genelleme 2–3 gerçek gözlem ister" der [K33].
- *Neyi zayıflatır:* Kalıcı roller gecikir; üç tutarsız koşu kaçınılmaz olur (→S11). K-007 bunu açıkça reddetti [K02, K08].
- *Dengeleyici:* İkisini ayırmak. Rol iskeleti işin kendi döngüsünden şimdiden türetilebilir: okuyucu, araştırmacı, karşı-okuyucu, eksik-arayıcı gibi bilinen katkılar. Özel mekanizmalar ve yeni rol türleri kanıt bekler.

**Y5. Tek koordinatör, tek yazıcı** (S9 bütünlüğü; v0 §3.2, §6).
- *Neden yeterli görünür:* Kanonik kayıt çakışmaz [K59].
- *Neyi zayıflatır:* Darboğaz oluşur. Koordinatör bağlamı hızla dolar ve daha sık sıkıştırılır. Tek hata noktası oluşur (→S12, S7, S18). v0 bunu kendisi söylüyor [K09]. RV01'in uyarısı: "akıllı koordinatör halleder" kutusu [K108].
- *Dengeleyici:* Alanlara göre yazma devri (alt ajan kendi dosyasını yazar), koordinatör kararlarının repoda gerekçeli durması, bağlam bütçesi, planlı taze oturum.

**Y6. Aynı modelle taze bağlamda karşı-okuma** (S14 ucuz doğrulama; v0 §3.3).
- *Neden yeterli görünür:* Ucuzdur ve bir şeyler yakalar; v0 ona dürüstçe "bağımsız doğrulama değil" diyor [K13].
- *Neyi zayıflatır:* Kayıtlarda "doğrulandı"ya dönüşürse Batu'nun kabulü bu etikete yaslanır. Ortak kör nokta görünmez olur (→S1, S2) [K106, K72 (F9), K47].
- *Dengeleyici:* Hata duyarlılığı sınaması, bağımsızlık beyanı, kabul paketinde "bunu kimse bağımsız doğrulamadı" satırı.

**Y7. Kontrolün ağırlığı risk ve geri alınabilirlikle orantılı** (S3 ve S20 hızı; v0 §3.8).
- *Neden yeterli görünür:* Tören şişmez [K10].
- *Neyi zayıflatır:* Belgeler git ile geri alınabilir görünür; ama üzerine kurulan kararlar, aşağı akıştaki işler ve Batu'nun güveni geri alınamaz. "Düşük risk" sınıfı eleştirisiz kararları yayar (→S14, S9) [K61, K31].
- *Dengeleyici:* Risk ölçütüne "bu çıktıya kaç karar dayanacak" sorusunu (aşağı akış yükü) eklemek.

**Y8. En fazla üç eleştiri turu** (S14 ve S20 döngü freni; v0 §3.7).
- *Neden yeterli görünür:* Sonsuz döngü engellenir [K11].
- *Neyi zayıflatır:* Park edilen bulgular görünmez biçimde birikir; kalite bir tavana takılır (→S5, S2).
- *Dengeleyici:* Park kaydı, yükseltme yolu, kapanışta açık bulgular listesi, her bulgunun akıbeti [K66].

**Y9. Durum dosyası tek ekranı geçmez** (S2 ve S7 konforu; v0 §3.6).
- *Neden yeterli görünür:* Hızlı yeniden giriş [K12].
- *Neyi zayıflatır:* Sıkıştırılmış durum nitelik kaybeder. Yeni oturum durum dosyasına güvenir (→S10, S18) [K67, K55].
- *Dengeleyici:* Durum dosyası işaretçi ve statü taşır, ayrıntı bağlantıyla verilir. Devir notu iddia sayılır ve git geçmişiyle karşılaştırılır (v0'da var).

**Y10. "Her şeyi repoya yaz"** (S18 dayanıklılığı; v0 §3.4, §3.6).
- *Neden yeterli görünür:* Makine kaybı iş kaybına dönmez [K19].
- *Neyi zayıflatır:* Kayıt şişer; kopyalar çelişir; açılış yükü ve maliyet artar (→S9, S7, S20) [K49, K94, K26, K86]. Şişme döngüsünün başlangıcıdır (§4.5).
- *Dengeleyici:* Tek kaynak kuralı, dosya görevleri, açılış seti bütçesi, hijyen sahibi.

**Y11. "Sorular birikir, iş durmaz"** (S2 konforu ve hız; K-002).
- *Neden yeterli görünür:* Batu her an rahatsız edilmez, iş akar [K15].
- *Neyi zayıflatır:* Yanlış çerçeve daha uzun süre fark edilmez. Geç gelen cevap yeniden iş dalgası başlatır (→S5, S1). EXP-006'da çerçeve on yedi dilim boyunca düzeltilmedi [K46].
- *Dengeleyici:* Soruların etkilediği kalemlerin işaretlenmesi. "Çerçeve sorusu" ayrı bir sınıftır ve biriktirilmez.

**Y12. Sürekli yetkiyle kendiliğinden geçiş** (S1 hızı; K-002).
- *Neden yeterli görünür:* "Devam" yükü kalkar [K04, K15].
- *Neyi zayıflatır:* Aşamalar arasında doğal kontrol noktası kalmaz; tek fren gözlem olur (→S17, S14). Kanonun 742 koşusu [K25, K90].
- *Dengeleyici:* İlerleme ölçüsü, takılma alarmı, periyodik yön gözden geçirmesi, P4 durağı.

**Y13. Hatırlatma sayısı başarı ölçüsü** (S17 ölçümü; v0 §3.2).
- *Neden yeterli görünür:* Gizli yükü doğrudan ölçer [K05].
- *Neyi zayıflatır:* Vekil ölçü (proxy) tuzağı. Daha az soru sorarak ve daha az rapor vererek sayı düşürülebilir. Batu yorulunca hatırlatmayı bırakabilir (→S2) [K72 (F14)].
- *Dengeleyici:* Eşli ölçüler: Batu'nun yakaladığı hata türü, kabulde bulunan açık sayısı, kaynak alt sistemlerdeki erken uyarılar. Sayı hedef değil, teşhis girdisi olmalı.

**Y14. Her okuma için okuma kaydı** (S6 izlenebilirliği; v0 §3.4).
- *Neden yeterli görünür:* "Tam okudum" iddiası sınanabilir olur [K51].
- *Neyi zayıflatır:* Maliyet artar. Okuma kaydı anlamanın kanıtı sanılır: "Okuma izi süreç kanıtıdır; anlama … için otomatik oracle değildir" (→S20, S14) [K56].
- *Dengeleyici:* Ayrıntılı kayıt yalnız karar taşıyan okumalarda tutulur. "Neyi değiştirdi" alanı zorunludur.

**Y15. Kaynak seçimini brief'e bırakmak** (S7 ve S12 kapsam kontrolü; v0 §3.5).
- *Neden yeterli görünür:* Alt ajan dağılmaz [K14].
- *Neyi zayıflatır:* Keşif, koordinatörün kaynak seçimiyle sınırlanır. Brief'teki eksik hem üretene hem inceleyene geçer (→S4, S6) [K40, K101].
- *Dengeleyici:* "Şu alana bakılmalı" bildirim yükümlülüğü (v0'da var). Eksik-arayıcıya brief'ten bağımsız bir kaynak alanı verilir.

**Y16. "Batu'ya sormak son seçenek"** (S2 konforu; v0 §3.1).
- *Neden yeterli görünür:* Batu gizli teknik işçi yapılmaz [K76].
- *Neyi zayıflatır:* Değer seçimleri sessizce verilir. Kabulde sürpriz çıkar (→S1) [K101].
- *Dengeleyici:* Otomatik seçim kaydı ve kontrol noktasında toplu sunum.

**Y17. Dersi CLAUDE.md'ye kural olarak yazmak** (S19 ve S21 için hızlı düzeltme).
- *Neden yeterli görünür:* Her oturumda yüklenir.
- *Neyi zayıflatır:* Talimat birikir. Tavsiye, zorlama sanılır. Davranış değişmeyebilir. Bağlam şişer (→S15, S7) [K48, K71]. Defo modeli bunun için "salt öğüt en zayıf biçimdir" der [K33]. Kural birikimi döngüsü (§4.5).
- *Dengeleyici:* Dersin yerini seçmek (mekanik kapı > iz isteyen prosedür > öğüt) ve davranış değişimini doğrulamak.

**Y18. Kalıcı rolleri erken ve çok sayıda tanımlamak** (S11 tutarlılığı; Batu'nun gereksinimine aşırı cevap riski).
- *Neden yeterli görünür:* Tutarlılık sağlar [K02].
- *Neyi zayıflatır:* Koordinasyon yükü artar (EXP-006 P2-01'de 16 rol sözleşmesi) [K65]. Yanlış kaynaktan türemiş roller donar [K52]. "Süreç kendisi ürün olur" [K27] (→S12, S3, S21).
- *Dengeleyici:* Rolleri işin kendi döngüsünden türetmek, az sayıyla başlamak, sürümlemek ve gözden geçirme tetiği koymak.

**Y19. Güvenliği hook'larla zorlamak** (S16).
- *Neden yeterli görünür:* Zorlama tavsiyeden güçlüdür [K71].
- *Neyi zayıflatır:* Özerk koşuda gereksiz durmalar olur. Tek bir zorlama noktası kapsam yanılsaması yaratır [K67]. Cloud'da `settings.json` hook'ları yalnız tek repolu oturumda geçerlidir [K17]. Batu'nun sözü: "Hepsine kurmak da imkânsız." [K82] (→S18, S12)
- *Dengeleyici:* Zorlama haritası; hook yalnız bilinen kayma noktalarına konur.

**Y20. Paralel çok ajanla hız** (S12).
- *Neden yeterli görünür:* Süre kısalır.
- *Neyi zayıflatır:* Limitler tükenir. Birleştirme yükü ve Batu'nun inceleme kapasitesi aşılır. Korele sonuçlar bağımsız kanıt sanılır (→S20, S14, S2) [K22, K72 (F10), K45].
- *Dengeleyici:* Paralellik bütçesi, bağımsızlık koşulu, birleştirme sözleşmesi.

**Ortak desen** (çıkarım): Maddelerin çoğunda "yeterli" görünen seçim ya **konfor** (Y1, Y9, Y11, Y16), ya **hız** (Y7, Y12, Y20) ya da **bağlam ekonomisidir** (Y2, Y3, Y15). Zayıflattığı yer ise çoğunlukla bir **frendir**: doğrulama, gözlem ya da Batu'nun dikkati. Batu'nun "hız varsa fren de olmalı" uyarısının bu sistemdeki karşılığı budur: hız ve konfor seçimleri, yanlarında fren bileşeni olmadan kurulamaz.

## 6. A003 (v0) kapsamı

**Ölçek:**
- **Kurmuş:** bileşenlerin çoğu var ve çoğu "nasıl" düzeyinde (kim, ne zaman, hangi alanlarla).
- **Kısmen:** bileşenlerin bir kısmı var ya da çoğu yalnız ilke cümlesi düzeyinde.
- **Kurmamış:** alt sistemin adı ve bir-iki ilke dışında karşılığı yok.

"≈x/y" sütunu, §3'teki y bileşenden kaçının A003'te bir karşılığı olduğunu gösterir. Yarım karşılık 0,5 sayıldı. Sayım benim yargımdır (çıkarım); A003'ün bölüm numaralarına bağlıdır. Kaynak: `sources/conversation/A003.md` [K110].

| Alt sistem | v0 durumu | ≈x/y | v0'da olanlar (A003 §) | Başlıca eksikler |
|---|---|:-:|---|---|
| S1 Yönetişim ve yetki | Kısmen | 6/7 | Karar katmanları (§3.6); kim karar verir (§3.7); bilinmeyenlerin sınıflanması (§3.1); tercihlerin toplu sunumu (§3.6); DECISIONS'ta Claude'un kararları da (§5) | Çoğu tek cümlelik ilke. Yükseltme tetikleri, bütçe ve izinli denemeler sürekli yetki metninde yok. Hatlar arası otorite yok (A-06 sonradan çıktı) |
| S2 Batu ile iş birliği | Kısmen | 4,5/7 | Üç bitiş biçimi, "sana yalnız şu durumlarda gelirim" (§3.9); hatırlatma = kusur (§3.2) | Uzun özerk koşu için kontrol noktası raporu; kabul paketi; bilişsel yük bütçesi; bildirim kanalı |
| S3 Metodoloji ve yaşam döngüsü | Kısmen | 5,5/7 | Düşünme sırası (§3.1); harita ve kontrol noktaları (§3.6); pilotlar (§5); tören orantısı (§3.8) | Oturum açılış/kapanış ritimleri tanımsız. Ağırlık bütçesi yalnız risk olarak anılmış (§6) |
| S4 İhtiyaç ve kapsam keşfi | Kısmen | 4/7 | "Kimseye verilmemiş iş var mı?" (§3.8); eksik-arayıcı (§3.2); kalemin kökeni: "benden, bir alt ajandan, karşı-okumadan ya da senden" (§3.6) | Keşif ayrı bir sorumluluk olarak adlandırılmamış. Amaç ihtiyacı ile yöntem ihtiyacı ayrımı yok. Çerçeve yeterliği yalnız bir ders olarak var (§2) |
| S5 Plan ve iş yönetimi | **Kurmuş** | 6/8 | Kalem şeması ve statüler; sıra ≠ önkoşul (§3.6); revizyon tetikleri, sınıflama, yetki, kayıt, sınırlar (§3.7) | Hazır iş ve akış sınırı; dilim boyutlandırma |
| S6 Araştırma birikiminden yararlanma | **Kurmuş** | 8/8 | Tetikler, sıra, araştırma izi (§3.5); okuma yolu, okuma kaydı, birlikte okuma (§3.4); kanıt gücü (§3.8) | Kanıt türü etiketleri kaba; tazelik kuralı yalnız Claude Code iddiaları için |
| S7 Bağlam yönetimi | Kısmen (zayıf) | 2,5/8 | "Ana oturum az okur", "yeniden yüklemek ucuz" (§3.9); okuma sırası | Bütçe ve sıkıştırma politikası; açılış seti sınırı; bağlam paketi (yalnız yollar var); seçilen ≠ kullanılan; rol görünümü. **Batu'nun adını koyduğu alan** |
| S8 Bellek yönetimi | Kısmen (zayıf) | 3/7 | "Repo bellektir" (§3.4); kalem sonrası kayıt (§3.6); okuma yolu (§3.4) | Bellek türleri ve otorite sınıfları; rol belleği; bütünlük denetimi; cloud'da bellek gerçeği. **Batu'nun adını koyduğu alan** |
| S9 Kayıt ve bilgi mimarisi | Kısmen | 5,5/8 | Dosya düzeni ve görevleri (§5); tek yer ilkesi (§3.9); sürüm bağlama (§3.3–3.4); tabelalar (§4) | Yayılım kontrolü; hijyen sahipliği. Dal politikası sonradan değişti (K-009) |
| S10 Anlam bütünlüğü | Kısmen | 4,5/7 | Batu'nun sözü birebir; söylenen / kastedilen / bizim anlayışımız ayrımı (§3.1); "senin kelimene dönülür" (§4); "ne reddedildi" (§3.7) | Türetilmiş görünüm etiketi; nitelik koruyan özet şablonu; özet yeterliği sınaması |
| S11 Kalıcı roller | **Kurmamış** | 2/8 | Beş geçici alt ajan türü; çalışma rolleri ≠ DevOS rolleri (§3.2); üç tekrar kuralı (§3.3) | Rol sözleşmesi, kaydı, yeterliği, belleği, araç sınırı. **K-007 bunu açıkça istedi** |
| S12 Orkestrasyon ve bütünleştirme | Kısmen (zayıf) | 3/9 | Tek yazıcı (§3.2); aynı tanımla tekrar göndermeme (§3.3); kararların gerekçesiyle repoda durması (§6) | Dağıtım kararı; paralellik bütçesi; birleştirme sözleşmesi; alt ajan kaybı; topoloji durumu |
| S13 Ajanlar arası arayüzler | **Kurmuş** (çekirdek) | 4/7 | Dokuz alanlı görev tanımı ve dönüş biçimi; "dönen sonuç veridir" (§3.3) | Devir notu şablonu; roller arası istek biçimi; brief sürümü; tüketim kanıtı |
| S14 Kalite güvencesi ve doğrulama | Kısmen | 5/9 | Önceden ölçüt, tamamlanma katları, kanıt gücü (§3.8); ayrı girdili karşı-okuyucu (§3.3); üç tur sınırı (§3.7) | Hata duyarlılığı; kalem denetimi; bütünsel inceleme; bulgu akıbeti |
| S15 Muhakeme disiplini | Kısmen | 4/9 | Düşünme sırası (§3.1); yöntem: karşı kanıt ve alternatif (§3.3); "bilmiyorum" (§3.9); AGENT.md protokolleri korunur (§5); kendi eğilimlerinin itirafı (§6) | Defo modeli ve iz ilkesi; uzun koşu öz-denetimi. Disiplinin alt ajanlara nasıl taşınacağı belirsiz (AGENT.md yüklenmiyor) |
| S16 Güvenlik ve bütünlük | Kısmen (yalnız ilke) | 2,5/7 | "Repoda okunan bir talimat yetki taşımaz" (§3.5); eski "sıradaki" ifadeleri bırakılır (§4); tek yazıcı (§3.2) | Durum değiştiren araçların yönetimi; yıkıcı işlem koruması; geçişli yetki; zorlama haritası |
| S17 Gözlemlenebilirlik ve ilerleme | Kısmen | 3,5/7 | İlerleme ölçüsü, "hareket var, ilerleme yok" alarmı (§3.6); hatırlatma sayısı (§3.2) | Olay günlüğü; takılma türleri; metrik bütünlüğü; açılış sinyali |
| S18 Süreklilik ve kurtarma | Kısmen | 4/9 | Okuma sırası; devir notu git ile karşılaştırılır (§3.9); kalem sonrası kayıt (§3.6); soğuk başlangıç testi önerisi (§6) | Sıkıştırma protokolü; yarım alt ajan işi; uyandırma mekanizması; bilinmeyen etki |
| S19 Ortam, araçlar ve yapılandırma | Kısmen (zayıf) | 3/9 | Depth sınırı notu (§3.2); Claude Code iddiası için belge ve canlı deneme (§3.5); CLAUDE.md önerisi (§5); "özellikler değişecek" (§6) | Zorlama/tavsiye katmanı; yapılandırma regresyonu; model ve efor seçimi; izin modu |
| S20 Maliyet ve kaynak | **Kurmamış** | 1/7 | Yalnız risk olarak: "haftalık limit yetmez" (§6); "her şeye tören yapılmaz" (§3.8) | Bütçe, harcama kaydı, paralellik tavanı, model/efor politikası |
| S21 Öğrenme ve uyarlama | Kısmen | 5/9 | Ders kaydı, dersin yeri, davranış değişiminin doğrulanması, P3 kanıtı (§3.10); pilotlar ve soğuk başlangıç (§5, §6) | Olay sınıflandırması; yöntem değişikliği kontrolü; sadeleştirme |

**Özet:** 3 kurmuş (S5, S6, S13), 16 kısmen, 2 kurmamış (S11, S20).

**Gözlem** (çıkarım):
- v0'ın "nasıl" düzeyine yaklaştığı üç alt sistem, dayandığı okumaların odağıyla örtüşüyor: plan ve devir (R05), araştırma kullanımı (R03, R04), görev tanımı (R05).
- En zayıf alanlar ise Batu'nun U004'te adını koyduğu alanlar (bağlam, bellek, kalıcı roller) ile hiçbir okumanın hedeflemediği alanlar (orkestrasyon, ortam ve yapılandırma, maliyet).

v0'ın kapsamı, sistemin ihtiyaç kapsamını değil, okunan araştırmanın kapsamını izlemiş görünüyor. Batu'nun "sözde geniş kapsam ama çıktıda yeterli seviye" eleştirisinin mekanizması muhtemelen budur [K01]. Bir envanter adımının METHOD v1'den önce gelmesinin gerekçesi de budur.

## 7. Açık sorular ve bu notun kanıtlamadıkları

### 7.1 Açık sorular

1. **Paketleme.** 21 alt sistem METHOD v1'de nasıl paketlenecek? Hangileri ayrı bir dosya ya da rol ister, hangileri bir şablon alanı ya da kontrol sorusuyla karşılanır? Bu not sahip ve karşılık ister; biçim P0.4'ün kararıdır.
2. **Fren eşikleri.** Sürekli yetkinin freni olan ilerleme ölçüsünün eşikleri ne olacak (kaç kalem ya da kaç oturum boyunca karar çıkmazsa alarm)? Alarm Batu'ya cloud'da hangi kanaldan ulaşacak? Bildirim kanalı bilinmiyor [K104].
3. **Aynı model olmayan ikinci bir denetim kanalı var mı?** Örneğin aşama sonlarında eleştirmen olarak ChatGPT (A-03). S14'ün bağımsızlığı bu cevaba bağlı. Cevap yoksa Batu'nun dikkati tek kanal olarak kalır ve S2'nin önemi daha da artar.
4. **Batu'nun bilişsel yükü nasıl ölçülür?** Repoda bu konuda ölçüm yok. Katalogdaki `i-have-adhd` çalışması "user-conditioned output policy" başlığını taşıyor ama henüz başlamamış; yalnız katalog satırı okundu.
5. **Kardeş notlarla tutarlılık.** Bu envanter R07–R10 okunmadan yazıldı. Bağlam, bellek ve rol bileşenlerinin ayrıntısı o notlarla P0.4'te karşılaştırılmalı. R08'in ayrı bir risk yönetimi alt sistemi önerme olasılığı §2.2'de not edildi.
6. **Yöntemin ağırlık bütçesi ne olmalı?** Loopinance'ın açılış seti sınırı (50 KB) bir örnek [K26]. Bu iş için "süreç ürüne dönüşüyor" sinyalini erken veren ölçü tanımlanmadı.
7. **Canlı doğrulama yok.** Süreklilik alt sisteminin (S18) dayandığı uyandırma mekanizmaları (send_later, tetikler) bu ortamda denenmedi [K104]. Denemeler Batu'nun iznine bağlı.
8. **Matris eksik.** Boş hücreler değerlendirilmedi. Hücrelerin ikinci bir göz tarafından çürütülmeye çalışılması (P0.5'in 2. eleştirisi) eksik bağları bulabilir. Özellikle olay kaydı bulunmayan S16 ve S20 satırları zayıf.
9. **S7–S10 sınırları.** Bağlam, bellek, kayıt ve anlam arasındaki sınırlar benim seçimim. P0.4 bunları birleştirmeyi seçebilir. Bu durumda her birinin bileşen listesi korunmalı; aksi halde birleştirme Batu'nun "yeterli seviye" eleştirisine döner.

### 7.2 Bu not neyi kanıtlamıyor

- **Envanterin tam olduğunu.** Kapsam yoklayıcılarının hepsi bu reponun kendi kaynaklarıdır. Foundation'ın uyarısı burada da geçerli: "all listed sources checked ≠ all materially relevant sources listed" (R04 (b)5). Dış metodolojilerle karşılaştırma R08'in işi.
- **Herhangi bir bileşenin bu ortamda işe yaradığını.** Hiçbir bileşen canlı sınanmadı. "Standart seviye" burada "incelenen olgun sistemler ve repo olaylarından çıkan bileşen seti" demektir; sektör çapında bir anketin sonucu değildir.
- **Kenarların nedensel olduğunu.** Olayların alt sistemlere atanması benim çıkarımımdır. Olay kayıtlarının çoğunu da aynı asistan tuttu.
- **Sayımların bir ölçüm olduğunu.** Kenarları ben sıraladım. Olayla desteklenen kenar sayısı, kayda geçen olaylarla sınırlı; Batu'nun fark etmediği hatalar yok.
- **v0 değerlendirmesinin nesnel olduğunu.** "≈x/y" sayıları yargıdır; A003'ün bölüm numaralarıyla sınanabilir.
- **Bağımsızlığı.** Bu not aynı modelin analizidir. P0.5'teki eleştiri turunda üretenin gerekçesini görmeyen bir karşı-okuyucuya verilmelidir.

## Ek A — Kanıt kaydı

**Sütunlar:**
- **Etiket:** kaynak diyor / gözledim / çıkarım.
- **Tür:** Batu'nun sözü, repo olayı, tedarikçi belgesi, ürün kaynağı okuması, kavramsal analiz, alt ajan raporu (ikincil), gözlem.
- **Cloud:** yalnız Claude Code iddiaları için; bu iddianın cloud oturumuna uygulanıp uygulanmadığı.

R01 üzerinden aktarılan belge alıntıları R01'in 26.09.2026 tarihli erişimine dayanır; ben yeniden erişmedim. İngilizce alıntılar özgün dilindedir. K93, K97 ve K98 numaraları kullanılmadı.

| ID | Kaynak | Kısa özgün alıntı | Etiket | Tür | Cloud |
|---|---|---|---|---|---|
| K01 | `EXP-007/sources/conversation/U004.md` | "yeterli seviye ile standart seviye arasında fark var" · "bütünsel bakıldığında yeterli seviyesi diye düşündüğün şeyler diğer  mekanizmaların yetersizleşmesine sebebiyet verir" · "sözde geniş kapsam ama çıktıda "yeterli seviye" şeklinde bir yaklaşımın var" | kaynak diyor | Batu'nun sözü | — |
| K02 | `U004.md` | "kullandığın alt ajanların da kalıcı bir rol yapısına ihtiyacı var gibi duruyor, her seferinde yeninden alt ajana rol biçmek doğru değil" | kaynak diyor | Batu'nun sözü | — |
| K03 | `U003.md` | "alt ajanlar nasıl düşnürdü, düşünmek için repodan nasıl yararlanırdı, foundation ve studies alanlarından nasıl ve ne zaman bilgi alması gerektiğini nasıl bilirdi" | kaynak diyor | Batu'nun sözü | — |
| K04 | `U002.md` | "chatgpt'de her tur sonunda durup benim chat'e bir şey yazmam gerekiyor" | kaynak diyor | Batu'nun sözü | — |
| K05 | `A003.md` §3.2 | "Bana yaptığın her hatırlatma bir kusur olarak kayda geçer; düzenin gerçek başarı ölçüsü bu sayıdır." | kaynak diyor | v0 önerisi | — |
| K06 | `A003.md` §3.9 | "Ana oturum az okur, okumayı alt ajanlar yapar. Böylece bağlam sıkıştırıldığında yeniden yüklemek ucuz olur." | kaynak diyor | v0 önerisi | — |
| K07 | `A003.md` §3.2 | "Alt ajanlar: tek soruluk, geçici çalışanlar." | kaynak diyor | v0 önerisi | — |
| K08 | `A003.md` §3.3 | "Bir görev kalıbı üç kez aynı şekilde tekrarlanınca kalıcı bir ajan tanımına dönüşür, önce değil." | kaynak diyor | v0 önerisi | — |
| K09 | `A003.md` §6 | "Tek koordinatör: her şey benden geçtiği için hem darboğaz hem tek hata noktasıyım." | kaynak diyor | v0 önerisi | — |
| K10 | `A003.md` §3.8 | "Kontrolün ağırlığı risk ve geri alınabilirlikle orantılıdır. Her şeye tören yapılmaz." | kaynak diyor | v0 önerisi | — |
| K11 | `A003.md` §3.7 | "bir çıktı en fazla üç kez eleştirilip düzeltilir. Yakınsamazsa açık sorun olarak park edilir ya da sana gelir." | kaynak diyor | v0 önerisi | — |
| K12 | `A003.md` §3.6 | "Durum dosyası tek ekranı geçmez" | kaynak diyor | v0 önerisi | — |
| K13 | `A003.md` §3.3 | "Aynı model olduğu için buna "bağımsız doğrulama" değil, "taze gözle karşı-okuma" derim." | kaynak diyor | v0 önerisi | — |
| K14 | `A003.md` §3.5 | "Kendi başına Foundation'a dalmaz; hangi kaynağa bakacağını görev tanımı söyler." | kaynak diyor | v0 önerisi | — |
| K15 | `A002.md`; `DECISIONS.md` K-002 | "P1→P2↔P3→P4 geçişleri kendiliğinden olsun." · "Sorular biriksin, iş durmasın." | kaynak diyor | Batu'nun onayladığı metin | — |
| K16 | Bu oturumdaki kabuk gözlemi, 27.09.2026 | `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`, `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80`; repo kökünde `CLAUDE.md` ve `.claude/` yok | gözledim | gözlem | evet |
| K17 | R01 `cloud` C8 → code.claude.com/docs/en/cloud-environments.md; R01 `cloud` özeti (4) | "Cloud sessions start from a fresh clone of your repository. Anything you commit to the repo is available." · "(settings.json only in single-repo sessions)" | kaynak diyor | tedarikçi belgesi (R01 üzerinden) | evet |
| K18 | R01 `cloud` C11–C12 → context-window.md | "It replaces the verbatim conversation: full tool outputs and intermediate reasoning are gone." · "Claude may start "forgetting" earlier instructions" | kaynak diyor | tedarikçi belgesi (R01 üzerinden) | evet (cloud oturumu sıkıştırmayı erken tetikler) |
| K19 | R01 `multiagent` C5 → claude-code-on-the-web.md | "Background work that was still running when the VM was reclaimed, such as subagents and shell commands, isn't restored." | kaynak diyor | tedarikçi belgesi | evet |
| K20 | R01 `cloud` C10 → memory.md | "Auto memory is machine-local. … Files are not shared across machines or cloud environments." | kaynak diyor | tedarikçi belgesi | evet |
| K21 | R01 `multiagent` C8 → sub-agents.md | "`project` is the recommended default scope. It makes subagent knowledge shareable via version control." | kaynak diyor | tedarikçi belgesi | belirsiz (commit edilmezse kaybolur; R01 çıkarımı) |
| K22 | R01 `continuation` C14; `cloud` C15 → claude-code-on-the-web.md, errors.md | "cloud sessions share rate limits with all other Claude and Claude Code usage within your account." · "A single burst of heavy activity, such as a large workflow fanout, can exhaust the weekly allowance" | kaynak diyor | tedarikçi belgesi | evet |
| K23 | R01 repo ekseni, "Süreklilik açıkları" | "After each compaction or resume, the six mandatory EXP-006 files (about 60 KB) and the loaded protocols (about 50–100 KB) must be re-read." | kaynak diyor | alt ajan raporu | evet |
| K24 | Bu alt ajanın araç listesi (gözlem); R01 eksik-arayıcı | create_session, create_trigger, send_later, add_repo bu alt ajanda görünür · "The state-changing tools … are exposed to subagents" | gözledim | gözlem + alt ajan raporu | evet |
| K25 | `batuhanozgun/loopinance_v2@07cd81b` `docs/arsiv/ilk-plan-2026-09-24.md` §2, §3 (ders 5), 27.09.2026 | "Bekçi 742 kez koştu ama "54 gündür kod yok" demedi. Panodaki "sıradaki oturum" satırı bile bayat ve yanlıştı." · "İlerleme ölçülmedi, sadece canlılık ölçüldü." · "Her oturum açılışında "son koddan bu yana X gün" yazılır." | kaynak diyor | repo olayı (asistanın retrospektifi) | — (düzen yerel Mac'te çalıştı) |
| K26 | aynı dosya §3 ders 4 | "Bellek, taşıdığı işten ağırlaştı. Oturum başında okunacak dosyalar 110 KB'a çıktı; sınır 50 KB'tı." | kaynak diyor | repo olayı | — |
| K27 | aynı dosya §3 ders 9 | "Süreç kendisi ürün oldu. Aynı dönemde süreç şablonuna (KEEL) yaklaşık 90 commit gitti." | kaynak diyor | repo olayı | — |
| K28 | aynı dosya §3 giriş | "Bu, beşinci çalışma düzeni denemesi. Her önceki deneme gerçek bir soruna çözüm üretti, sonra kendi ağırlığı altında durdu." | kaynak diyor | repo olayı | — |
| K29 | aynı dosya §3 ders 8 | "Onaylar seremoniye döndü. Mühürler itirazsız geçti." | kaynak diyor | repo olayı | — |
| K30 | aynı dosya §2; §3 ders 3 ve 7 | "Sonraki 16 görevin hepsi "bu yanlış sayıları nasıl gösterelim" tartışmasıydı ve hiçbiri kod üretmedi." · "Dilim doğru sayı üretemiyorsa soru üretir." · "Sana teknik sorular gitti" | kaynak diyor | repo olayı | — |
| K31 | aynı dosya §3 ders 6 | "Karar değiştirmek pahalıydı. Bir karar değişince 14 spec'in yeniden yazılması gerekiyordu." | kaynak diyor | repo olayı | — |
| K32 | aynı dosya §3 ders 1 | "Koordinatör ise vault commit'lerinin %37'sini attı ama bunların çoğu evraktı." | kaynak diyor | repo olayı | — |
| K33 | `loopinance_v2@07cd81b` `docs/DEFO_MODELI.md`; arşiv planı §3 ders 10 | "Yumuşak öz-yargı kendini geçirir" · "mekanik kapı > iz isteyen yazılı prosedür > salt öğüt. Salt öğüt en zayıf biçimdir" · "makul görünen çıktı üreten defolar (1-4) kendiliğinden asla yakalanmaz" · "hiç koşulmamış töreni önceden inşa etme (tek örnekten şablon türetilmez; genelleme 2-3 gerçek gözlem ister)" · "çapa DOSYADA yaşar, tur başında okunur" · "sürecin en değerli çıktısı buydu" | kaynak diyor | uygulayıcı pratiği (Batu'nun deposunda damıtılmış; bağımsız ölçüm yok) | — |
| K34 | R01 loopinance ekseni (`loopinance-claude-code@e54b69f` kanon) | "Rolün = açıldığın klasör." · "Günlük döngün: `00_pano/PANO.md`'yi aç → "SIRADAKİ OTURUM: <rol>" satırını gör → o rolün klasöründe oturum aç → "devam" yaz." · "hedef rol sonraki açılışında cevaplar" · "Her dosyanın başında yazıcı rolü yazar; başkası yazamaz" · "Kapanış adımları (sırayla, atlanamaz)" · son sağlık koşusu "#713" | kaynak diyor | repo olayı (R01 üzerinden; ben okumadım) | — (yerel Mac) |
| K35 | `EXP-005/sources/conversation/08-LOCAL-KURULUM-VE-EKSIK-DEVIR.md` A043, U044, A044 | A043: "Artık doğru ortamdayız." · U044: "bizim cloude ortamdaki çalışma yansımamıştı onunla ilgili problem olmaz mı şu an bu mesajı gönderirken?" · A044: "önceki mesajı olduğu gibi gönderseydik sorun olabilirdi; çünkü local Codex şu an `main` / `d27bf17...` üzerinde." | kaynak diyor | repo olayı (birebir aktarım) | — |
| K36 | `EXP-005/reflections/LESSONS-AND-OPEN-QUESTIONS.md` §4 (D02) | "yeniden girişlerde hangi engelin kapandığı, hangi sonucun devralındığı, hangi ana kabulün hâlâ açık olduğu güvenilir biçimde yönetilemedi." | kaynak diyor | repo olayı (asistanın retrospektifi) | — |
| K37 | aynı dosya §9 (D07) | "erişim kontrolünün hatırlatılması (U020/U021), kaynak kapsamının genişletilmesi (U023), erişim seçeneklerinin sorgulanması (U026/U030/U032), yayının kontrolü (U035) ve son Cloud işinin devre alınması (U044) kullanıcıdan geldi." | kaynak diyor | repo olayı | — |
| K38 | aynı dosya, Sonuç | "Önlemeye çalışılan kullanıcıya bağımlı ihtiyaç/önkoşul/devir keşfi sorunu, onu düzeltmek için yürütülen süreçte yeniden ortaya çıktı." | kaynak diyor | repo olayı | — |
| K39 | aynı dosya §2 tablo (D06), §8 | "Local hash, PR head, shell auth ve “1 dakika önce” görünümü karıştı" · "Devir, yalnız repository adını ve geçmiş özeti değil, gerçek güncel içerik/kimlik ve tamamlanmamış yükleri geri kazanmalıdır." | kaynak diyor | repo olayı | — |
| K40 | aynı dosya §3 (D01), §5 (D03), §6 (D04); R03 §2 | "A002'de “eksik merkezi motor” dili" · "Ortam adı, gerçek kabiliyet kanıtı değildir" · "Erişim, kaynak seçimi, gerekli derinlikte okuma, anlamı kullanma ve karar/eyleme katkı ayrı gözlem yükleridir." · Batu: "niye sadece EXP-004'e gönderiyorsun?" | kaynak diyor | repo olayı; Batu'nun sözü (R03 üzerinden) | — |
| K41 | `research/soul-foundations/08_foundation-sufficiency-reuse-review/DISCUSSION-HANDOFF.md` §1–3; Foundation STATE | "The intervening discussion and its correction had not been persisted." · "The assistant nevertheless declared the example finished." · "The adequacy of the knowledge, its discoverability and its actual application must remain separable questions." | kaynak diyor | repo olayı | — |
| K42 | `research/soul-foundations/STATE.md` "Confirmed research purpose" | "Structural coverage is not engineering sufficiency. A branch is not a mandatory service, file or agent" | kaynak diyor | kavramsal analiz | — |
| K43 | `08_…/REUSE.md` "Research-to-target reasoning" | "A role need does not imply an AI agent, and an instruction need does not imply that a particular file enforces it. … Conversely, a simpler arrangement is not adequate merely because it is simple." | kaynak diyor | kavramsal analiz | — |
| K44 | `08_…/CASE-AUDIT.md` C4 | "Preserve history without granting it timeless operational authority." · "Measure the claimed behavioral/effect property rather than infer it from a changed file." | kaynak diyor | kavramsal analiz | — |
| K45 | `08_…/CASE-AUDIT.md` C1 | "Multiplying copies does not increase independent observation count." | kaynak diyor | kavramsal analiz | — |
| K46 | R02 §4 (E1, E2); U002-A (ana oturum doğruladı) | "Every slice from S1-05 on ends with a next step the assistant chose itself" · "bir önce konuşma bir sonraki konuşmanın içeriğini belirledi" · "17 slices turned R1–R25 into F1–F8 plus specializations. No role was named and the platform was never researched." | kaynak diyor | repo olayı (R02 üzerinden) | — |
| K47 | R02 §3 | "One producer judged everything, and says so" · "S1-07–S1-13 each kept its family … None was rejected" | kaynak diyor | repo olayı (R02 üzerinden) | — |
| K48 | R02 §4 (E3); A003 §1 | "D010 and the Context “iletişim disiplini” section already existed at `23280ab` (26 Sep), yet U002-A on 27 Sep still complains about length." · "Kısa cevap kuralı vardı, cevaplar yine uzun kaldı." | kaynak diyor | repo olayı | — |
| K49 | R02 ölçek paragrafı, §6.2; A003 §1 (ana oturum 53.346 / 1.494 sayılarını doğruladı) | "Only about 1.5k words of the user's own text are kept verbatim" · "Every other user correction survives only as the assistant's paraphrase" · "“NOT STARTED” appears in INDEX, STATE, HANDOFF, DECISIONS and the S1 master, and 7 times in WORK." | kaynak diyor | repo olayı | — |
| K50 | R02 §6.6 | "The user's “motivasyon” became “başarı yönü/success direction”." | kaynak diyor | repo olayı | — |
| K51 | R02 §3 | "S1-16 §8 labelled five sources “Tam” although the bulk tool output had been cut off." | kaynak diyor | repo olayı | — |
| K52 | R02 §4 (b) | "Roles were derived from SOUL's target capacities (B1–B9), not from the DevOS team's own working loop." | kaynak diyor | repo olayı (R02 çıkarımı; A003 §1'de Batu'ya sunuldu, K-006 ile kabul gördü) | — |
| K53 | R02 §4 (d) | "There were nine or more corrections" | kaynak diyor | repo olayı | — |
| K54 | `EXP-004/checks/REPAIR-20260921.md` §1; `HISTORICAL-FIDELITY-T08.md`; `USER-MESSAGES.md` U016 | "metinler özetlendi, yeniden ifade edildi ve bazı kaynak-sonrası cümleler eklendi. Kaynak metin ile türetilmiş görünüm karıştı. Başarılı merge/readback kaynak sadakati kapanışı gibi sunuldu." · "Başarılı PR/merge/readback dosyaların yayımlandığını doğrular; kaynak aktarımının tamlığını doğrulamaz." · U016: "Repoda eksiklik varsa çalışmaya mola ver ve repoyu olması gereken hale getir." | kaynak diyor | repo olayı | — |
| K55 | `EXP-004/continuations/T08-…` §2 | "kaynak çıktıda nitelikler var; ara özette yok; tüketici yanlış statüyle ilerliyor. Bu, gerçek ürün olayı değil, hata yerini belirlemek için açıkça kurulmuş bir karşıörnektir." | kaynak diyor | kavramsal analiz (kurulu karşıörnek) | — |
| K56 | `EXP-004/continuations/T14-…` §2–3 | "Bu özet iki varyantta da içerik bakımından yanlış olmak zorunda değildir; fakat mektubu kimin gördüğünü kaybeder." · "Okuma izi süreç kanıtıdır; anlama ve gerekçeli hüküm için otomatik oracle değildir." | kaynak diyor | kavramsal analiz (kurulu karşıörnek) | — |
| K57 | `EXP-004/artifacts/MS01-SOUL-WORKING-SYSTEM-DRAFT.md` §7 | "K1–K7 işlev kimlikleridir, yedi zorunlu ayrı process/agent değildir." · "Gereksiz sürekli çalışan supervisor veya evrensel policy arbiter eklenmedi." | kaynak diyor | kavramsal analiz | — |
| K58 | aynı dosya §3 | "Yeni rol = talimat + gerçek model/insan/program taşıyıcısı + uygun context + araç/etki kapsamı + ilgili yeterlik dayanağı. Rol adı model eğitimi değildir." | kaynak diyor | kavramsal analiz | — |
| K59 | aynı dosya §1 (P2), §5 (K6) | "Paralel aktörler candidate çıktı ve karar önerisi üretebilir. Ortak current state'e geçiş ise tek mantıksal commit sınırında uzlaştırılır." · "Worker doğrudan ortak yazma/yayın credential'ı taşıyıp bu yolu aşabiliyorsa broker yaptırım değildir." | kaynak diyor | kavramsal analiz | — |
| K60 | `EXP-004/artifacts/MS01-COVERAGE-AND-OPEN-MECHANISMS.md` §5 | "G01 — Discovery/Frame Adequacy \| K1 eksik soruyu bulma; K2 doğru üst karara dönüş." · "G05 — Useful Progress/Capacity" | kaynak diyor | kavramsal analiz | — |
| K61 | `EXP-006/work/B8-continuity-change-recovery.md` giriş, C6, C12, C13 | "session continuity ≠ Work continuity" · "stored lesson ≠ operative use ≠ persistent adaptation" · "Unknown effect ≠ no effect." · "Learning yalnız eklemek değil, gerektiğinde **sadeleştirmek ve geri çekmek** de olmalıdır." | kaynak diyor | kavramsal analiz | — |
| K62 | `EXP-006/work/B9-integration-and-testing.md` C7, C10, C13 | "Fresh-session continuation yalnız dosya okunmasıyla test edilmiş sayılmaz." · "Testi geçirecek şekilde değiştirilen test, aynı run'ın bağımsız doğrulaması sayılamaz." · "More harness ≠ better harness." | kaynak diyor | kavramsal analiz | — |
| K63 | `EXP-006/work/B2-information-capacity.md` giriş, C1, C9, R5 | "bulunabilir olması ile belirli Work/Actor/use için seçilmesi; seçilmesi ile aktöre gerçekten görünür olması; görünür olması ile anlaşılması/kullanılması" · "canonical current state ile derived/learned memory aynı authority class'ında olmamalıdır." · "R5'in başarı yönü ise **şu anki işi yapan aktörün doğru şeyi görmesidir.**" | kaynak diyor | kavramsal analiz | — |
| K64 | `EXP-006/ACTORS.md` (`origin/main` `ed2bf6e`) | M1–M9 tablosu · "**Süregelen sorumluluk ≠ daima çalışan agent:**" · "**16 sözleşme, 16 ajan veya 16 kalıcı süreç kararı değildir.**" | kaynak diyor | kavramsal analiz (ChatGPT hattı adayı) | — |
| K65 | `EXP-006/work/P2-01-named-role-contracts.md` (`origin/main`) §1, §3, §5 | "Her sözleşme amaç/başarı yönü, bilgi ve uzmanlık, etkinleşme nedeni, teslimat/tüketici, yetki ve olumsuz sınır taşır." · "Mesaj gitmesi veya dosya yazılması, tüketicinin sonucu kullandığını kanıtlamaz." · "Başka role istekte bulunmak yasak etkiyi dolaylı yoldan yaptırma yetkisi vermez." · "İsim yeterlik değildir." | kaynak diyor | kavramsal analiz (ChatGPT hattı adayı) | — |
| K66 | `EXP-006/work/P3-01-work-information-discussion.md` (`origin/main`) §1, §4, §5 | "Ortak bir iş ve bilgi zemini üzerinde, ihtiyaç etrafında kurulan çalışma halkaları." · "koordinatör akışın sahibi olsun; bütün teknik kararların sahibi olmasın." · "Çok merkezi düzen, koordinatörü darboğaz ve görünmez düşünce filtresi yapabilir." · "her itirazın kaybolmadan bir karşılığı olmalıdır." · "Talep sahibi sonucu ilgili kararda nasıl kullandığını veya neden kullanmadığını gerekçesiyle gösterir." | kaynak diyor | kavramsal analiz (ChatGPT hattı adayı; kabul edilmemiş) | — |
| K67 | `research/studies/gstack/CORE.md` §4, §8.3, §11 | 11 alt sistem listesi (ör. "investigation / causal control", "memory / learnings / GBrain") · "one enforcement point succeeds != protected effect is controlled end-to-end" · "payload survives; qualifier disappears" · "Historical artifact mistaken for current truth" | kaynak diyor | ürün kaynağı okuması (gstack v1.79; çalıştırılmadı) | — (Claude hook'larının başka host'ta tavsiyeye düşmesi CORE'da anılıyor) |
| K68 | aynı dosya §12 | "prose / local convention → real failure → named state distinction → reusable helper/resolver/runtime rule → structural invariant/scanner → behavioral/environment E2E → CI/release consequence when justified" | kaynak diyor | ürün kaynağı okuması | — |
| K69 | aynı dosya §6 (Work), §10 (P7) | "Work performed != target condition achieved != evidence supports success != authorized acceptance/progression" · "Liveness as correctness" | kaynak diyor | ürün kaynağı okuması | — |
| K70 | `research/studies/agentic-ai-systems-roadmap/` SOURCE-VISUAL; INITIAL-ASSESSMENT §3; STATE | Katman listesi (ör. "Model routing (small ↔ frontier models)", "Task success metrics", "Drift detection") · "Governance is probably not “last”" · "potentially more useful as a **counterexample to naive layering** than as a layering model to adopt" | kaynak diyor | uygulayıcı görseli + aynı-asistan değerlendirmesi | — |
| K71 | `research/studies/anthropic-ai-native-sdlc-playbook/` META bulgu 2; 01 §7.2, §11, §17 | "Behavioral guidance and hard enforcement are different layers." · "Claude treats both as **context, not enforced configuration**" · "the system can accumulate a growing instruction file that attempts to solve mechanical failure with more prose." · "persistent work state + context/knowledge surfaces + bounded actors + layered action controls + verification/evaluation + observability + feedback/evolution + human authority boundaries + actual execution environment" | kaynak diyor | tedarikçi belgesi (Anthropic playbook ve belgeleri; 04.09.2026 gözlemi) | genel (cloud'a özgü değil) |
| K72 | aynı paket `04-FALSIFIERS-…` F9, F10, F14, F16, F17, F18 | "Human gate can become hidden technical verification" · "increasing production concurrency without increasing integration/verification capacity can simply relocate the bottleneck again." · "fewer review findings may mean better generation or weaker reviewer sensitivity" · "policy changes but Skill does not" · "Controls should therefore be designed to depend as little as practical on one model behaving “as expected,”" · "Observability is evidence infrastructure." | kaynak diyor | kavramsal analiz (tedarikçi kaynağına karşı okuma) | genel |
| K73 | aynı paket META bulgu 3–4; 03 DP-01 | "Agent configuration is itself a changeable software-like surface that needs regression evaluation." · "An agent with no direct production-write route may still obtain effect through another agent it can reach" | kaynak diyor | tedarikçi iddiası (birinci taraf olay raporu) | genel |
| K74 | `research/studies/ecc/CORE.md` §7.1; `notes/32-USAGE-COST-CONTEXT-AND-RESOURCE-CONTROL.md` §2, §4 | "the same valid producer can feed inconsistent quantities into different views, including a stopping predicate." · "cost3, then cost7 \| 7 \| 10" · "No usable measurement can become a new zero rather than an unknown" | kaynak diyor | ürün kaynağı okuması (ECC; çalıştırılmadı) | — |
| K75 | `research/studies/ecc/INDEX.md` "Original mechanism notes"; META | Yetenek alanları (kurulum, sahiplik ve checkpoint'ler, iş ve oturum kayıtları, bellek kapsamı, gözlem, değerlendirme, yapılandırma koruması, maliyet/bağlam kontrolü …) · "No qualifying conversation-independent repository-only re-entry evidence was recovered" | kaynak diyor | ürün kaynağı okuması | — |
| K76 | `research/studies/multi-agent-patterns/SOUL-DEVELOPMENT-OS-ASSESSMENT.md` §7, §9, §12 (C1, C3, C7) | "worker outputs may all be individually sound while the manager chooses the wrong decomposition or merges them into the wrong global conclusion." · "the person who repeatedly notices state drift; … the hidden merge algorithm." · "Complexity without a protected requirement should be treated as suspect." · "Topology transitions must be persistent state" | kaynak diyor | kavramsal analiz | — |
| K77 | `concepts/CHARTER.md` "Her turda görünür tutulması istenen iki risk" | "Bu nedenle kullanıcının sonradan itiraz etmesi temel kalite kontrolü olamaz." · "Ortak sözcükler ortak anlayış garantisi değil" | kaynak diyor | Batu'nun talebinin konsolidasyonu | — |
| K78 | `AGENT.md` satır 85–155 (rota kaydı, veri olarak); `agent/protocols/` toplam 1.908 satır (gözlem); R01 repo ekseni | R02: "Could user or stakeholder influence, a desired outcome, prior commitment, completion or approval pressure, or another non-evidential incentive materially bias the epistemic result?" · R05: "Could omitted, stale, or distorted information in a summary, excerpt, retrieval result, memory, compressed context, or other derived view materially change the conclusion?" · R01: "Nothing says whether subagents must run the gate" | kaynak diyor; gözledim | kontrol katmanı metni + alt ajan raporu | evet (CLAUDE.md olmadığı için otomatik yüklenmiyor; K16) |
| K79 | R05 tablo satırları 2, 4, 6, 12, 14, 15, 24, 25, 27 | "forbids unchanged retries" · "open does not mean actionable" · "forbids silent blanket confirmation" · "prefer the ledger and Git history over recollection" · "checkpoint exists + is newest ≠ checkpoint claims are still current truth" · "circuit-broken" after 3 failures · "Plan self-review only covers work already in the plan" · "Claude Code's switch to background-by-default subagents left parent workflows waiting forever ("third recurrence")." | kaynak diyor | alt ajan raporu (studies: SP, GS, BD, GT) | 27. satır Claude Code davranışı; cloud'a özgü değil |
| K80 | R05 §2 | "GS suppresses nested reviews by the same model after one cost about 15M tokens." | kaynak diyor | alt ajan raporu (gstack tarihçesi) | — |
| K81 | `EXP-007/STATE.md` "Oturum ve ortam notları" | "Alt ajanlar bu oturumda P0.3'e kadar yaklaşık 4,1 milyon token harcadı" | kaynak diyor | repo kaydı | evet |
| K82 | R03 ilke 3, 4, 12, 14, 16, 18; §2; §4 gerilim 1; §5 madde 2 | "Every reminder he has to give counts as a defect." · "Artık emir erine dönüşmüştür." (A4) · "laf ebeliği yapıyorsun" · "Ben bunu geçen hafta da aynı şekilde anlatmıştım." · "Hepsine kurmak da imkânsız." (A4) · "Biz de bunu "anladı" sanıyoruz." (A4) · "neden bu kadar bilgiyi sana ben araştırtmak zorundayım?" · "An agent running alone for 40 minutes must trigger its own check for flattery (A4)." | kaynak diyor | Batu'nun sözü (R03 üzerinden; alıntıların bir kısmını ana oturum doğruladı) | — |
| K83 | R06 tablo (T08, T11, T12, DQ01, L07) | "devir notunu kısaltma, karar-kritik statüyü silme izni değildir" · "«token bütçesi bitti» birer faaliyet/kaynak olayıdır; doğrulama sonucu değildir" · "Beklemede olmak unutulmak veya sessizce silinmek değildir." · "Rejected options must not come back in through summaries." · "Eksik cevabı uydurmak yerine eksik soruyu kurmak, keşfin bir parçasıdır." | kaynak diyor | kavramsal analiz (R06 üzerinden) | — |
| K84 | R04 (b)2 (Foundation E5) | "Locator, content presence, interpretation, acceptance and action are not equivalent" · "do not assume unobserved model knowledge, a forgotten earlier session or another worker's private state as that side information." | kaynak diyor | kavramsal analiz (R04 üzerinden) | — |
| K85 | R04 (d)4 (Foundation CC, RUA) | "advisory instruction != deterministic enforcement" · "one denied tool path != all effect paths closed" | kaynak diyor | kavramsal analiz | — |
| K86 | R04 "Route problems" 3 | "They are a live example of the propagation failure TP describes" (Selection STATE ile 07/root STATE çelişkisi) | kaynak diyor | repo olayı (R04 bildirdi; ana oturum doğrulamadı) | — |
| K87 | R01 repo ekseni "Süreklilik açıkları"; `EXP-007/sources/conversation/U005.md` | "State written by Claude (STATE, HANDOFF, WORK) is invisible to the next fresh session and to ChatGPT on main." · U005 bağlamı: "Birleştirme çakışma verdi: EXP-006, main'de ChatGPT hattında üç commit ilerlemişti" | kaynak diyor | alt ajan raporu + repo olayı | evet (push yalnız çalışma dalına) |
| K88 | R01 repo ekseni (hüküm, SP12, SP27, güçlü yanlar) | "The rules would still stop it, in about the same places ChatGPT stopped." · "current authorization çözülemiyor" (fail-closed) · "INDEX.md's file-responsibility table says which surface is updated for which kind of change" | kaynak diyor | alt ajan raporu | evet |
| K89 | R01 repo ekseni "Süreklilik açıkları" | "Batu cannot audit what happened across unattended steps without reading commits. That is the reading burden D010 was meant to remove." | kaynak diyor | alt ajan raporu | evet |
| K90 | R01 eksik-arayıcı | "The /goal judge only reads the transcript ('doesn't run commands or read files independently', goal.md)." · "An autonomous loop can report progress without making any." | kaynak diyor | alt ajan raporu | belirsiz (/goal'un cloud desteği açık değil) |
| K91 | `A003.md` §3.3 | "bir rapor "alt ajanlar üç kat iç içe çalışabilir" dedi; ortamda bakınca burada bunun kapalı olduğunu gördüm." | kaynak diyor | repo olayı | evet |
| K92 | `EXP-007/README.md` "Sınırlar"; `DECISIONS.md` K-004, A-04, A-05 | "Kontrol ve yapılandırma değişiklikleri (CLAUDE.md, `.claude/agents`, skills, hook'lar) Batu onaylamadan kurulmaz" · "EXP-006'daki ChatGPT dönemi dosyaları Claude'da kaymaya yol açmamalı." | kaynak diyor | Batu'nun kararı | — |
| K94 | R02 §1 madde 6 | "That produced 36 commits in about 6 minutes, mostly one file each." | kaynak diyor | repo olayı | — |
| K95 | R02 §4 (c), §6 madde 3 | "The drift cleanup left "Authority notu" boilerplate in 27 files." · "Historical "next" lines remain in 27 files" | kaynak diyor | repo olayı | — |
| K96 | `EXP-005/reflections/LESSONS-AND-OPEN-QUESTIONS.md` §7 (D05) | "İki taraf da 4/4 PASS ve 23/23 gözlem aldı" | kaynak diyor | repo olayı | — |
| K99 | `loopinance_v2@07cd81b` `docs/arsiv/ilk-plan-2026-09-24.md` §7 (Aşama 2) | "Senden okumanı isteyeceğim tek belge bu." | kaynak diyor | uygulayıcı pratiği | — |
| K100 | R05 tablo satırı 9 (PB F4; WM) | "A bad plan can appear to have been 'correct' because it is revised after implementation." | kaynak diyor | alt ajan raporu | — |
| K101 | R05 tablo satırları 1 ve 3; R04 (a)2 (ana oturum doğruladı) | "A worker and reviewer can share the same omission when they share an incomplete brief" · risk: "Value choices made silently" · "Discovering a missing decision is not permission to make it on the owner's behalf." | kaynak diyor | alt ajan raporu; kavramsal analiz | — |
| K102 | R05 tablo satırları 16–17 (CMH, GS) | "findings ... before session death" · "Check each summary for: decisions kept, unresolved issues, rejected alternatives, source references, uncertainty turned into certainty, status labels." · "payload survives; qualifier disappears" | kaynak diyor | alt ajan raporu (literatür ve ürün kaynağı) | genel |
| K103 | R01 eksik-arayıcı (claude-projects.md:406) | "A thread or session revived after more than about 1 hour of cache expiry re-reads its whole conversation" | kaynak diyor | tedarikçi belgesi (R01 üzerinden) | belirsiz (Projects bağlamında belgeli) |
| K104 | R01 eksik-arayıcı | "No continuation mechanism has been tested live in this environment." · "One unanswered prompt can stall a /goal loop or let the VM expire mid-run" | kaynak diyor | alt ajan raporu | evet (denenmemiş) |
| K105 | R01 repo ekseni SP05 | "Autonomy granted only in chat is also lost at the next fresh session." | kaynak diyor | alt ajan raporu | evet |
| K106 | R03 §4 gerilim 8 (A2†); R06 §3 madde 5 (EXP-002 Q03) | "Tüm roller aynı temel modeli ... paylaştığı için, defekt hepsinde aynı kökten çıkıyor" · "Farklı rol, taze çağrı veya farklı isim, aynı varsayım/kaynak/yanılgıların paylaşılmasını dışlamaz" | kaynak diyor | Batu'nun yayımladığı yazı (AI destekli); kavramsal analiz | — |
| K107 | `EXP-004/reflections/QUALIFICATIONS.md` Q15 | "Pozitif kullanıcı değerlendirmesi teknik doğrulama veya belirsiz her tasarım seçiminin onayı sayılmaz." | kaynak diyor | kavramsal analiz | — |
| K108 | R06 §3 madde 3 (RV01 §7); §2 G05 | "bütün zor yükleri adı konmuş «akıllı koordinatör halleder» kutusuna bırakmak yeterli taslak değildir" · "chains of "next narrow question" that never get integrated" | kaynak diyor | kavramsal analiz (R06 üzerinden) | — |
| K109 | R06 tablo (DQ03 satırı) | "Record which version of the brief each subagent ran under, and reconcile late results against that version." | kaynak diyor | kavramsal analiz (R06 çıkarımı) | — |
| K110 | `A003.md` §1–§7 (bölüm numaralarıyla anıldı) | Örn. §1: "Ortada harita yoktu ve repodaki kurallar her aşamada durmayı emrediyordu." · §3.8: "gerekli olduğu halde kimseye verilmemiş iş var mı?" · §3.10: "Değişim görülene kadar ders "doğrulanmadı" sayılır." | kaynak diyor | v0 önerisi | — |
| K111 | R02 §1 madde 7, §4 (E5) | "The assistant offered to pick SOUL's first job (fea5d50)." · "The user objected to ""ilk somut SOUL geliştirme işini assistant seçsin"", which became D012." | kaynak diyor | repo olayı | — |
| K112 | R04 (a)1, (a)4, (a)6, (d)2 | "Treating all of these as `cancelled` destroys the reason Work ceased or never began." · "does not establish … who may select, commit, reprioritise, waive, accept, terminate or reactivate Work" · "more work started does not logically entail better end-to-end system progress." · "false != unknown / indeterminate != not evaluated != not applicable != stale." | kaynak diyor | kavramsal analiz (R04 üzerinden) | — |
| K113 | R05 tablo satırları 21–22 (SP, GS) | "It stops only for irreversible or destructive actions, security-sensitive actions, external effects that normally need consent, and cases where "every way forward is a guess"." · "Mechanical — auto-decide; Taste — auto-decide, record, surface at final gate" | kaynak diyor | alt ajan raporu (ürün kaynağı okuması) | — |
