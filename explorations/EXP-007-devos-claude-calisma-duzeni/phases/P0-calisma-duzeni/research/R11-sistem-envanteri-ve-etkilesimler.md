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
2. **Beş repo olayının hepsinde hatayı sonunda Batu yakaladı ya da onarımı Batu'nun müdahalesi başlattı:**
   - soru bankası [K41];
   - EXP-005'teki devir [K35];
   - EXP-006'daki dokuzu aşkın düzeltme [K53];
   - EXP-004'teki arşiv onarım talebi [K54];
   - kanonda Batu'nun zamanlayıcı rolü [K34].

   Aynı modelden türeyen denetçiler aynı kör noktayı paylaşır [K106]. Bu yüzden Batu'nun dikkati bugün sistemin tek "aynı model olmayan" denetim kanalıdır. "Batu ile iş birliği" alt sistemi bir konfor eki değil, güvenlik alt sistemidir; Batu'nun masaj örneğinin bu sistemdeki karşılığı budur (çıkarım; olaylara dayalı).
3. **Etkileşim matrisinde bozulmalar en çok Batu'da ve kalite güvencesinde toplanıyor.** Başka alt sistemleri en çok etkileyenler kayıt mimarisi, orkestrasyon, bağlam ve gözlemlenebilirlik. Sayımlar §4.3'te. Kayıt mimarisi ve bağlam, METHOD v1'de "şasi" gibi ele alınmalı: zayıflıkları neredeyse her yere yayılıyor.
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

