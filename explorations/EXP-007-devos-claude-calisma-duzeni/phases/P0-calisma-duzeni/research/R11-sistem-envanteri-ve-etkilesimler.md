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

