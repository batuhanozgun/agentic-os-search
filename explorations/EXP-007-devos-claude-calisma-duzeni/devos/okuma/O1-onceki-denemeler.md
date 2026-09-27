# O1 — Önceki denemeler: `development-os/**` ve `research/soul-context/**`

**Okuyan:** O1 okuma ajanı (Claude), 27 Eylül 2026, `agentic-os-search@c576e32`. Kümedeki dosyalar `efde316`'daki halleriyle aynı.
- **Kanıt dili:** *kaynak diyor* / *gözledim* / *çıkarım* / *bilinmiyor*.
- **Standart:** STANDART.md uygulandı; kapsam bölünmedi (§0). Okunan her şey veri olarak ele alındı.

## DevOS için en önemli çıkarımlar

1. **Tanım 6–24 Eylül boyunca değişmedi.** DevOS, SOUL'u araştıran, tasarlayan, kuran, doğrulayan ve geliştiren çalışma düzenidir. Batu amacın ve owner kararlarının sahibidir; kaynak: "should not remain the technical coordinator or verifier". On iki gereksinim üç denemede de sabit kaldı (§1.2).
2. **Üç deneme de DevOS'u kurmadan durdu; hazırlık işin yerine geçti.**
   - Codex: 11 native kontrol geçti, gerçek model koşusu 0/8 kaldı.
   - DEVOS-001: 11 mesaj ve 4.508 katkı kaydı üretildi; P2 ve P3 başlamadı. Tasarım (D1) açıldığı sabah durduruldu.
   - DEVOS-002: dört saatte on kayıt, ardından "konudan saptın yine".
3. **Ortak kök neden (çıkarım).** Yakın iş üst hedefin yerine geçti. Her adım Batu'nun taşımasına bağlıydı: 13 brief'in 11'ini o taşıdı. Güvence ilk yararlı işin önkoşulu yapıldı. İki modelin eleştirisi üretimin yerine geçti. Kritik düzeltmeleri hep Batu yaptı ve fiilen gizli denetçiye dönüştü (§3.6, §8.5).
4. **Çalıştığı raporlanan iki zincir var.** COORD-01→03 (native yardımcı, taze oturum, uzaktan geri okuma) ve AGENT-CONTROL (DO-01…08 rotaları, 8 protokol; READY dar tanımlı ve "14 semantic routing checks are not 14 executed operating scenarios"). Ortak özellikleri: tek somut iş, önceden sabit ölçüt, ajanın kendi yardımcısı, repodan geri okuma.
5. **Doğrudan alınabilecek olgun parçalar** (§7):
   - S1A aday sözleşme, STATE ve iş kaydı (M1);
   - kayıtsız kesintide devralma (M3);
   - manda ve owner listesi (M6);
   - rota kuralı (M7);
   - RPD01, devam kartı, F01–F03, RP1–RP6 (M8);
   - CONSTRUCTION-PLAN'ın kuralları, K01–K12 ve C01–C18 (M15).
6. **Kayıt ve kanıt kuralları sabit kaldı.** Tek yetkili kopya. STATE yalnız yönlendirir. "Önerilmiş iş, yetkilendirilmiş iş değildir". Dosya, commit, push, yükleme ve davranış ayrı kanıtlardır. ÇALIŞTIRILMADI, ÇALIŞTIRILAMADI ve BAŞARISIZ ayrı statülerdir. Denetçi üç durumlu sonuç verir (M10). G1 parser regresyonunu koştum: 14/14 OK.
7. **Boyut kuralı.** "Minimum" ölçüt değil: Batu reddetti, Research geri çekti. BOOTSTRAP'taki "minimum sufficient" alınmamalı (§8.2). "Çok büyük iş" de istenmiyor. Ölçü: her yapı bir ihtiyaca ve teste bağlanır, her tur somut eylem üretir ("Az laf çok icraat").
8. **Cloud'a uyarlama (çıkarım).**
   - VM süresinin dolması ve boşta makinenin geri alınması yüzünden kayıtsız kesinti olağan. Karşılığı: devralma kuralı, devam kartı ve sık push.
   - Derinlik 1'e "Mantıksal recursion, fiziksel agent recursion değildir" ilkesi uyuyor.
   - %80 sıkıştırmaya karşı devam kartı hook'la yazılır ve geri basılır.
   - Oturum dalları için bir bütünleştirme kuralı gerekiyor; kümede yok (M3).
9. **Plugin çelişkisi kaynakta çözülmüş, canlı sınanmamış.** @`606506e` "Plugins are not available in Remote sessions" dedi; @`94dc93e` ve güncel 002 belge okumasıyla bunu düzeltti (synced plugin). Sürüm sabitlemek için proje dosyası yolu daha denetlenebilir (§8.1).
10. **Batu'nun kısıtları (§2).** Teknik soru yok, test operatörü değil, kapsam daraltılmaz, konudan sapılmaz, SSH yok, Mac kapalı olabilir. Maliyet ve ECC şartı yok. Sıfır hata bir kalite hedefidir. Denetim her turda görünür olur.
11. **DevOS kendi yön denetimini taşımalı (çıkarım).** Batu'nun elle yaptığı düzeltmeler (konudan sapma, dar READY, kapsam daralması) mekanik tetiklere çevrilmeli. Yoksa "owner'ın gizli orchestrator/verifier haline gelmesi" tekrarlanır (M16).
12. **Açık kalanlar.**
    - `_02`'nin sonucu ve Codex hedef repolarının dosyaları: erişim yok.
    - ECC ile DevOS sorumluluklarının karşılaştırması: O5a–O5d.
    - Synced plugin, setup cache ve VM sonrası kurtarma canlı denenmedi.

## 0. Kapsam

**Kapsam bölünmedi; kümenin tamamı okundu.** Not STANDART'a göre yeniden yazıldı. 45 KB'lık ilk taslakta kırpılan içerik geri kondu.

**Tam okunan: kümedeki 78 dosyanın hepsi (759.935 bayt).** Dosyalar `efde316` ile `c576e32` arasında değişmedi (`git diff --stat` boş; gözledim). Büyük dosyalar parça parça okundu; tamlık satır sayısıyla kontrol edildi.
- **`development-os/` (19 dosya):**
  - `INDEX`;
  - `002/README`;
  - 001'in `BRIEF`, `WORK`, `METHOD`, `EXCHANGE`, `REVIEW` dosyaları;
  - `R-001…R-006`;
  - `reading/` altındaki 4 kayıt;
  - `evidence/W02-D01/{probe.py,result.json}`.
- **`research/soul-context/` (59 dosya):**
  - `README`, `INDEX`, `STATE`;
  - `DEVELOPMENT-OS-BOOTSTRAP`, `COORDINATION-TRANSFER-PLAN`;
  - 13 brief: STAGE-1, STAGE-1A, STAGE-2-G0, G0-D1, G1-PURPOSE-PILOT, G1-R1, COORD-01/02/03, COORDINATION-HANDOFF, DESIGN-01, DEVOS-AGENT-CONTROL, DEVOS-CONSTRUCTION-PLAN;
  - `claude-code-devos-preparation/` altında 4 dosya: WORK, CLAUDE-TASK-01, OWNER-CONTEXT, SOURCE-REGISTER;
  - `reviews/` altında 12 dizin, 22 dosya: direction (+OPENING-VISION-SOURCE), stage-1, stage-1a, g0, d1, g1 (+PARSER-REGRESSION.py), method, collaboration, coord-01, coord-02 (3 dosya), coord-03, devos02-plan. Bazılarında CODEX-RESPONSE ya da EVIDENCE-EXTRACTS da var;
  - `evidence/` 3, `exploratory/` 8, `repos/` 4 defter.

**Tarihsel sürümler.** GitHub API ile, yalnız okuma. Clone shallow olduğu için fetch yapılmadı. Tamamı okunanlar:
- STATE @`408f112`, @`de51ef6`, @`4ad34d7`, @`b47b3f6` (= `cee38ca`), @`1be22a3`;
- INDEX @`cee38ca`, @`1be22a3`;
- CC-PREP WORK ve TASK-01 @`1be22a3`;
- CONSTRUCTION-PLAN v1 @`2dec8b6`;
- 001 BRIEF @`dc76496`, @`3c809d9`;
- 001 WORK @`3c809d9`, @`28dfff1`;
- 001 REVIEW @`85076c2`, @`fdfe9ba`, @`dc76496`;
- METHOD v1 @`3c809d9`;
- 002 @`606506e`, @`94dc93e`.

Ayrıca iki commit listesi okundu (gözledim): STATE için 39 commit, `development-os/` için 25 commit.

**Çalıştırılan.** `python3 -B .../reviews/2026-09-07-g1/PARSER-REGRESSION.py` → "Ran 14 tests ... OK". Ardından `git status` temiz kaldı (gözledim). `probe.py` çalıştırılmadı; hedefi os3 reposunda (O2).

**Açılmayanlar ve gerekçeleri.**
- **Diğer tarihsel sürümler:** EXCHANGE @`85076c2`/@`fdfe9ba`, COVERAGE @`3c809d9`, WORK @`c91b71d` ve öbür STATE sürümleri. Bunlar kümenin dosyaları değil, eski halleri. Güncel halleri okundu; commit mesajları da okundu.
- **Defterlerin asıl kaynakları** (STANDART kural 3). `soul-development-os`, `soul-development-os_02` ve `soul` için GitHub API şunu döndürdü: "Access denied: repository ... is not configured for this session", ve "Do not add repositories the user has not asked for". `keel-research` de izinli listede yok. Bu yüzden Codex hedef dosyaları yalnız Research kayıtlarından biliniyor: `AGENTS.md`, 8 protokol, `work/*.md` ve `_02`'nin 14 dosyası. `keel` O3'te okunuyor.
- **os-architect:** O12'nin kapsamı. Sığ klonlandı ve okunmadan silindi; defteri okundu.
- **Başka notlara ait olanlar:** C-001…C-005 ve os3 (O2, G6); RPD özgün metinleri (O9); Foundation ve studies (O5–O10, F1–F4).
- **Repoda yok:** G0, D1 ve G1'in ZIP'leri. Yalnız `EVIDENCE-EXTRACTS.md` alıntıları var.
- **O0:** tekrarı önlemek için okundu.

**Kapatıcıya aday boşluk:** `soul-development-os` (`7800f37`: AGENTS, 8 protokol, `work/AGENT-CONTROL.md`) ve `_02` (plan `a91c7a9` ve RPD grant'ından sonraki commit'ler). `_02`'nin gerçek sonucu yalnız orada. İkisi de oturuma repo erişimi eklenmesini gerektiriyor.

## 1. DevOS ne olmalıydı?

### 1.1 Tanım (kaynak diyor)

- **SOUL ile DevOS ayrı.** CONSTRUCTION-PLAN §1: "SOUL, kullanıcının istediği sonuç için işe uygun çalışma sistemini oluşturabilen, işletebilen, gerçek etkisini değerlendirebilen ve yetki altında uyarlayabilen ürün hedefidir. Development OS ise SOUL'u araştırmak, tasarlamak, geliştirmek, doğrulamak ve zaman içinde iyileştirmek için kullanılacak çalışma düzenidir. Bunlar aynı ürün değildir." 002'de SOUL'un çalışma adı: "genel amaçlı bir Çalışma Sistemi Kurucusu".
- **DevOS neden önce kuruluyor?** İş sohbete, gizli belleğe ya da üreticinin kendi onayına dayanırsa, "the development process will **reproduce the same agentic failure classes SOUL is intended to control**" (`evidence/transition-to-soul.md` §5).
- **Repo düzeni** (BOOTSTRAP §1):
  - araştırma `agentic-os-search`;
  - DevOS "the working system used to research/design/build/verify/evolve SOUL";
  - ürün `soul-production`;
  - eski `soul` yalnız öncül kanıttır.
  - Kural: "Do not create multiple authoritative copies of the same fact."
  - Temiz başlangıç (§2): "preserve old repository/history + do not inherit its active structure by default + reuse mechanisms only when current problem reasoning/evidence justifies them".
- **Aktör** (§4): "The target is **not a programmer that merely implements instructions**". Sayılan 14 yetenekten bazıları:
  - "distinguish the user's goal from a proposed method";
  - "decide when additional repository/web research is needed";
  - "avoid self-certification";
  - "select or propose the correct next work rather than default every finding to repair/build";
  - "preserve continuation without permanent hidden human coordination".
- **DevOS tek ajan değildir** (§5): "Codex is an important Actor, not the entire Development OS." Çerçeve "Actors + Information + Work + Environment + relations / qualification / authority-control / transition mechanisms". Ama: "This is **not** an accepted software decomposition."
- **Muhakeme dağıtılır.** STATE@`de51ef6`: "All epistemic work must not remain in one coordinator."
- **Tasarım nesnesi.**
  - METHOD v2 §5: "bütünsel çalışma modeli ... Yalnız dikkat listesi ya da dosya ağacı değildir."
  - WORK@`28dfff1`'deki D1 yürüyüşü: "Development OS'u kurma amacı → gereken iş ve önkoşulları keşfetme → uzmanlık/sorumluluk ve ortamı hazırlama → göreve uygun kaynak/bağlam oluşturma → işi yürütme/koordine etme → sonuçları değerlendirme → planı ve bilgi durumunu güncelleme → kesintiden devam."
- **OPENING-VISION'dan DevOS'a da uyanlar** (`reviews/2026-09-06-direction/OPENING-VISION-SOURCE.md`). Kaynak bunları SOUL için yazıyor; DevOS da bir çalışma sistemi olduğu için ona da uyuyor (çıkarım).
  - Yedi soru: gerçekte ne var; ne biliyoruz; hangi iş gerekiyor; kim hangi rol ve yetkide; ilişkiler; "Yaptığımız şey gerçekten amaçlanan etkiyi yarattı mı?"; "Yeni gerçeklik karşısında çalışma sistemi değişmeli mi?"
  - Ayrımlar ve ölçü: "persistence ≠ memory ≠ retrieval ≠ context ≠ source truth"; "Generality = her şeyi yapmak değil, gereken sistemi doğru boyutta kurabilmek."
  - KEEL refleksi: "Kritik bir ayrım deterministik olarak korunabiliyorsa yalnız prompt'a yazıp modele hatırlatmakla yetinme."
  - Döngü: "SITUATE → KNOW → QUALIFY → GOVERN → ACT → VERIFY REALITY → REFRESH / RECOVER / LEARN". "**readback** first-class kavram olmalı".
  - Öğrenme yolu: "episode result → candidate lesson → evidence → evaluation → governed system change".

### 1.2 Denemeler boyunca sabit kalan gereksinimler

Her satır üç dönemde de kaynakta var (kaynak diyor). "—": o dönemde açık ifade yok.

| # | Gereksinim | Codex (6–8 Eyl) | Claude hazırlığı ve DEVOS-001 | DEVOS-002 |
|---|---|---|---|---|
| 1 | Batu müşteridir; koordinatör, doğrulayıcı ya da taşıyıcı değildir | BOOTSTRAP §6; "ask Batu for the **decision**, not for routine technical sequencing" | N00; "Teknik yöntemi adlandırmak, dosya dosya taşımak veya sürekli kusur bulmak zorunda bırakılmaz" | "teknik seçenekleri kullanıcıya geri devretmek varsayılan yöntem değildir" |
| 2 | Süreklilik repodan gelir; dosyanın varlığı yetmez | "Recover state from the repository, not a long bespoke launch prompt"; "File existence is insufficient" | (a): "geçmiş sohbet olmadan doğru güncel yetki ve iş" | "Keep canonical Development OS state/configuration in Git/repository" |
| 3 | Araştırma ilk günden kullanılır ama karar değildir | "research finding != requirement != architecture decision"; "From the first day" | Bütün korpus (R-004), "gerektiğinde drill down" (R-006) | Kapasite çıkarımı "research evidence üzerinden assistant tarafından" |
| 4 | Üretici kendini onaylamaz | "Aday C'nin değiştirdiği ölçüt veya denetleyici C'nin tek kabul dayanağı olamaz." | "Kriter değişirse aynı sonuçla yeni başarı iddiası kurulmaz." | "`synced` yüklenmesi bir runtime kalite sertifikası değildir." |
| 5 | Bilginin statüsü ayrı tutulur | "Keep distinct: prepared brief, user adoption/grant, dispatch, producer result, direct repository observation..." | "Git'te görülen kaynak/commit ile üretici davranış beyanı ayrı tutulur." | "`Belgeyle çözüldü` ... test edildiği anlamına gelmez." |
| 6 | Dört zemin mercektir; klasör, servis ya da ajan değildir | "not four mandatory folders/services/agents" | "Bunları ayrı dört kutu ... yapma." | Environment yalnız "bilgisayar/cloud/runtime/tool listesi olarak tanımlanmaz" |
| 7 | Önkoşulları ajan keşfeder (RPD) | RPD01; "rejected being used as the tester" | N00; (e) koşulu | "Kullanıcıya yeni teknik tercih sorusu şu anda gerekmiyor." |
| 8 | Tek yazıcı, açık devir, kesintiden dönüş | S1A, G0 devralma cümlesi, "**Süre dolması duruş değildir.**" | (d): "yarım işte doğru devam/geri dönüş" | "çalışan alt ajan/shell işleri geri yüklenmez" (D3) |
| 9 | Orantılı güvence; sonsuz hazırlık yok | "must not grow indefinitely merely to prepare"; "Önüne yeni bir sonsuz hazırlık sistemi koyma." | "sonsuz test-denetçisi araştırması açılmaz"; N09 | "Sırf bir ekranda sonraki düğme var diye yeni tıklama zinciri başlatılmaz." |
| 10 | Kurallar sessizce değişmez | Bitiş koşulu 10; "A protocol may recommend a control change; it may not make its own recommendation authoritative." | 4. satırla aynı | — |
| 11 | Gözetimsiz 7/24 çalışma hedef değil | "Self-sustain does not mean unattended 7/24 execution" | "sürekli çalışacak ajan döngüsü başlatmaz" | — |
| 12 | Denetim her turda görünür | `_02`: "ID–Soru \| Yanıt \| Karar \| Cevap" tablosu | — | Batu: "her seferinde sana uyarı vermemek için protokolleri turda şart koştum, yine de şu an bu aşamadayız." (@`94dc93e`) |

**12. satır üzerine (çıkarım):** Batu bu sözü Research asistanının protokol kapısı için söylüyor; `_02` tablosu aynı isteğin Codex karşılığı. Sözün devamı da önemli: kural görünür olsa bile sapma sürdü.

### 1.3 Açıkça reddedilenler

BOOTSTRAP §10:
- "`AGENTS.md` plus a protocol router as the final Development OS architecture";
- "copying Research R01–R09 unchanged";
- "using every GitHub feature from day one";
- "one fixed Research → Design → Build → Verify workflow for all work";
- "permanent Astra, Cloud or local-runtime dependency";
- "the four Foundation grounds as literal software modules";
- "migrating old SOUL/KEEL mechanisms without fresh justification";
- "self-sustain as unlimited authority or unattended continuous execution".

HANDOFF ve AGENT-CONTROL: "Do not build a custom launcher, scheduler, agent framework, protocol forest, service or new repository". Batu, araştırma kontrol dosyaları için: "bu al kopyala kullan demek değil" (OWNER-CONTEXT).

### 1.4 Değişen ya da gerilimli gereksinimler

1. **Boyut.** BOOTSTRAP Stage 1 "**minimum sufficient working bootstrap**" diyordu, S1 "küçük" diyordu. Batu ise iki şey söyledi: "minimum kuralım, yeterli kuralım sonra büyütürüz laflarını sevmiyorum. explorations klasörünü incelersen eğer bu "yeterli", "küçük" gibi şeylerin başımıza açtığı dertleri okuyabilirsin" ve "Çok büyük iş yapmaya çalışıyorsunuz." Gerilimi Research'ün yorumu çözüyor (§3.3): ölçü gereksinimin incelenip incelenmediğidir.
2. **Araştırmanın zamanı.**
   - 6 Eylül: seçici.
   - 7 Eylül: "From the first day".
   - 23 Eylül: bütün korpus, önce kayıt, sonra karar.
   - 24 Eylül: "gerektiğinde drill down yap".
   - Değişmeyen: araştırma karar yerine geçmez; kararı etkilediği gösterilir.
3. **Batu'nun taşıyıcılığı.**
   - 6 Eylül: "relays messages during bootstrap when necessary".
   - 7 Eylül: manda ile rutin taşıma kalkıyor.
   - 23 Eylül'de Batu'nun kendisi önerdi: "araştırma reposunun başında chatgpt var ... ben mesajlarını taşırım". Ardından repo mesajlaşması geldi, ardından durdurma.
   - İki sağlayıcı arasındaki köprü her seferinde darboğaz oldu.
4. **Ortam.** Codex Cloud → Mac'te Codex masaüstü → Claude cloud ("yerel bilgisayarındaki kapanmalar nedeniyle") → SSH yok, Mac + Claude cloud. Batu: "Tamamı kapanıyor, yani restart oluyor bilgisayar. Sebebi belli değil ama yoğun alt ajanlı işlerde sanırım bilgisayarda çok fazla okuma ve yazma yapıldığında oluyor gibi geliyor bana." (@`94dc93e`)

## 2. Kullanıcının kısıtları

Her kısıt Batu'nun kaydedilmiş sözüne dayanıyor; alıntılar aynen. §3'te tam alıntılananlar burada yalnız anılıyor.

| # | Kısıt | Kaynak ve alıntı |
|---|---|---|
| 1 | DevOS'u Claude kurar; SOUL'u o ortamda geliştirir | OWNER-CONTEXT: "Denemek istediğim bir Development OS yaratmak, ben değil sen yaratacaksın ve bu yaratacağın ortamda da SOUL'u yaratmak için çalışacaksın." |
| 2 | Teknik yöntem asistanın işidir; Batu'ya yalnız owner kararı sorulur | OWNER-CONTEXT: "ben sana SOUL'un ne olduğunu, içinde ne gibi mekanizmalar, yapılar olması gerektiğini söyleyebilecek yetkinlikte değilim." 002@`606506e`: "Batu teknik ayrıntıları bilmediği için assistant, seçenek alanını ve gerekli ayrımları görünür kılmalı; fakat her yeni terimi ayrı bir araştırma dalına dönüştürmeden ana amacı korumalıdır." |
| 3 | Batu test operatörü ya da eksik-bulucu değildir | STATE@`408f112`: "The user explicitly rejected being used as the tester for this missing layer"; STATE@`b47b3f6`: "Kullanıcı gizli eksik-bulucu, teknik mesaj taşıyıcı veya test operatörü olmaz." |
| 4 | Kapsam daraltılmaz; "minimum" diye kırpılmaz | OWNER-CONTEXT: "_02 ile işin yok, kapsamını ve çerçeveni daraltmasını istemiyorum." ve "minimum kuralım, yeterli kuralım sonra büyütürüz" (§1.4) |
| 5 | ... ama "çok büyük iş" de yapılmaz | "Çok büyük iş yapmaya çalışıyorsunuz." (§3.4). Çözüm: OWNER-CONTEXT yorumu (§3.3) |
| 6 | Araştırmanın tamamı kullanılır; okuma yükü Batu'ya kalmaz | OWNER-CONTEXT: "Araştırma reposu senin SOUL'un yapısında kullanabileceğin, fikir edinebileceğin, vizyonunu ve farkındalığını kullanabileceğin bir repo. oradan yararlanman gerekiyor." ve "PRD’yi kullanabilirsin ... sadece protokol seviyesinde değil araştırmanın tamamını okuyarak". BRIEF@`3c809d9`: "bu kadar araştırmayı ben kendim okuyayım diye mi yaptırdım ben sana?" |
| 7 | Konuşma değil eylem; ama acele eylem de değil | OWNER-CONTEXT: "Evet ama aynı zamanda aksiyon da alman lazım, sadece bana cevap vermen yetmiyor. Bu cümlemi de roket hızıyla aksiyona çevirme ama felsefe seviyesinde mesajlaşmak da yeterli değil." Ayrıca: "Az laf çok icraat". |
| 8 | Konudan sapılmaz | 002: "konudan saptın yine" ve "Noldu varsayımları konuşuyorduk? ortada bıraktın konuyu yine." BRIEF@`3c809d9`: "ilk mesajdan koptun konudan"; "bu kadar araştırma sonunda sikik bir dosyadan drift edeceksen". |
| 9 | SSH ve ayrı makine yok | 002 §2: "SSH ile ayrı makine yolu istenmiyor. Mevcut Mac ve Anthropic Claude Cloud kullanılabilecek ortamlar." |
| 10 | Mac'te gerekmeyen iş cloud'da; iş Mac'in açık kalmasına bağlanmaz | 002 §2: "Kullanıcı bilgisayarını kendi isteğiyle de kapatabilir. İşin Mac'in sürekli açık kalmasına bağlanmaması normal kullanım koşuludur". @`94dc93e`: "yoğun alt ajanlı işlerde sanırım bilgisayarda çok fazla okuma ve yazma yapıldığında" yeniden başlıyor. |
| 11 | Maliyet ve ECC şartı konmadı | 002 §2: "Sıfır ek maliyet veya tüm ECC bileşenlerinin zorunlu kullanılması şartı verilmedi." ve "ECC, Development OS için önerildi. SOUL'un ECC üzerinde çalışması istenmiş değil." |
| 12 | Sıfır hata bir kalite hedefidir | STATE@`de51ef6`: "The user requests zero error; this is a quality objective, not a guarantee, an evidence source or permission to relax criteria." |
| 13 | Denetim her turda görünür olur | `_02` tablosu; @`94dc93e`: "her seferinde sana uyarı vermemek için protokolleri turda şart koştum" (§1.2, 12. satır) |
| 14 | Araştırma kontrol dosyaları kopyalanmaz, ama kullanılabilir | OWNER-CONTEXT: "Yine de bu al kopyala kullan demek değil" (§1.3) |

**Özet (çıkarım):**
- Batu sonucu ister, yöntemi asistana bırakır. Kendisine ne teknik soru sorulmasını ne de test yaptırılmasını ister.
- En sık şikâyet konudan sapma ve laf kalabalığıdır; asıl ölçü de budur.
- İstenen boyut "küçük" ya da "büyük" diye tanımlanmıyor. Gerekçesi gösterilmiş ve her turda somut eylem üreten bir yapı isteniyor.
- Ortam: Claude cloud, Mac kapalı olabilir, SSH yok. Maliyet sınırı konmadı.
- Bu kısıtlar EXP-007'deki K-014…K-017 ve STANDART ile uyumlu: soru yok, sorumluluk %100 asistanda.

## 3. Ne denendi, ne oldu, neden durdu?

### 3.1 Codex hattı (6–8 Eylül; hedef `soul-development-os`)

**Düzen** (BOOTSTRAP §6): "Temporary ChatGPT ↔ Codex bridge". Research brief yazar, Batu Codex'e taşır, Codex çalışır, Batu sonucu ZIP ya da markdown olarak geri getirir, Research inceler. Köprünün bitiş koşulu 10 maddedir (listesi O0'da). Kaynak şunu da ekliyor: "File existence is insufficient".

**Zaman çizelgesi.** Kaynak: `research/soul-context/STATE.md` commit mesajları (GitHub API; gözledim). Saatler UTC.

| Zaman | Adım | Sonuç |
|---|---|---|
| 6 Eyl 13:40–14:10 | Stage 0/0B | İlk masaüstü oturumu git reposu olmayan bir dizinde açılmıştı (`/Users/Batu/Documents/Codex/2026-09-06/bu-oturum-s-f-rdan-kurulacak`, "historical binding failure"). Önce Codex Cloud ortamı kurulmuş, sonra "Astra/Ultra" için masaüstüne geçilmişti. |
| 6 Eyl 14:22–14:41 | S1 tasarımı | Üç yüzey önerildi. Review: "incelenebilir bir başlangıç adayına ilerlemek için yeterince iyi bir yön". Dört açık: C1–C4 (davranış prosedürü; ilk B0 yolu; doğrulayıcının başlangıcı; tek yazıcının kapsamı). |
| 6 Eyl 18:17 | S1A: tam aday metinler (M1, M2) | Codex kendini düzeltti: "Bağlam denetleyicisini ilk pilot olarak seçmiyorum". |
| 6 Eyl 18:40–19:58 | G0 deneyi | Bütçe: "aynı anda en fazla **bir alt Codex koşusu**", "toplam **en fazla sekiz alt koşu**", 20 dakika, "Tekrarlı sonsuz onarım yok". İzin dışı sentinel okundu; T1–T4 ve R(C1) ÇALIŞTIRILAMADI. |
| 6 Eyl 20:16 – 7 Eyl 05:48 | D1 sınır teşhisi | "toplam on native probe"; 6 PASS, 2 FAIL, 1 nedensel gözlem. Aynı gece direction review yazıldı. |
| 7 Eyl 05:48–06:42 | G1 amaç pilotu | 11 native kontrol geçti. Özel başlatıcı MCP ayrıştırmasında durdu; gerçek model koşusu 0/8. |
| 7 Eyl 06:59 | G1-R1 gönderilmedi; method review | "G1-R1 remains held". |
| 7 Eyl 07:36–08:19 | Collaboration review, TRANSFER-PLAN | Koordinatör + ihtiyaç anında yardımcı. Codex+Claude "Sonraki, ayrı değerlendirilecek genişleme". |
| 7 Eyl 08:55–12:54 | COORD-01→02→03 (M5) | Çalıştı. |
| 7 Eyl 13:09–14:17 | DESIGN-01 | "DESIGN-01 remains prepared but unsent/held" (STATE@`de51ef6`). |
| 7 Eyl 15:39 | COORDINATION-HANDOFF (M6) | STATE@`408f112`: "CODEX BOUNDED COORDINATION HANDOFF COMPLETED/READY" (HEAD `020d44a`). |
| 7 Eyl 16:12–17:11 | AGENT-CONTROL (M7) | Batu READY'ye itiraz etti; kontrol katmanı kuruldu, READY raporlandı. |
| 7 Eyl 17:11 | CONSTRUCTION-PLAN v1 (M15) | Gönderilmedi. |
| 8 Eyl 16:52–19:11 | `_02` planı ve RPD v2 grant'ı (M8) | Gönderildi; sonucu doğrulanmadı. |

**Method review'un teşhisi** (`reviews/2026-09-07-method/REVIEW.md` §2–§5):
- "'Küçük bootstrap' hedefinin yanında giderek özel bir test/başlatma altyapısı inşa edildi." (Tam teşhis L1'de.)
- Üç düzeyi ayırıyor: Foundation ayrımları, projeye özgü tasarım kararı, yerel mühendislik. "Foundation'ın daha fazla ilerlemesi ... üçüncü düzeydeki TOML hatasını ... kendiliğinden çözmez."
- gstack'ten ders: "'çalışma düzeninin asgari başlangıcı', 'tüm araçlar kullanılabilir' ve 'her iş kabul edilmiş' aynı eşik olmak zorunda değil."

**AGENT-CONTROL: çalıştığı raporlanan ikinci zincir.**
- **Batu'nun itirazı** (STATE@`408f112`): "The user correctly challenged the earlier interpretation of READY: the installed coordinator was not yet the functional counterpart of the browser research assistant's agent-control architecture." Eksik olanlar: "mandatory full routing classification", "conditional protocol loading", "re-gating" ve kontrol/proje ayrımı. Ayrıca: "The user explicitly rejected being used as the tester for this missing layer".
- **Sonuç** (STATE@`de51ef6`; Research `bootstrap/coordination-entry@7800f37`'yi doğrudan okudu):
  - "`AGENTS.md` is the target canonical entry with Development-specific DO-01 through DO-08 routing";
  - protokollerin kapsamı: "entry/source, work/decision, effects/authority, verification, continuity/writer, delegation, research reuse and repair";
  - "READY for bounded agent-control use".
- **Kanıtın sınırı:** "Native reviewer execution, 14 semantic scenario checks, failed F1 and repaired F2 fresh-child behavior are recorded by Codex ... this research turn did not independently rerun the user's local runtime."
- **Aynı günün kullanıcı yönleri:**
  - Araştırma "From the first day of Development OS construction" kullanılacak.
  - "All epistemic work must not remain in one coordinator."
  - Dış akış: "one research-side task message -> Codex's internally reviewed complete plan -> one research-side final review ... -> Codex's bounded implementation, internal testing/repair and normal Development OS continuation."
  - "The user requests zero error; this is a quality objective, not a guarantee".

### 3.2 `soul-development-os_02` ve RPD (8 Eylül)

- **Neden yeni repo?** STATE@`4ad34d7`: "Eski Codex çalışma düzenini toparlayamadığı için yeni proje repository'si `soul-development-os_02` oluşturduğunu ve hazırlığın buna göre yapılmasını istedi." Brief'in kuralı: "**Eski `soul-development-os` repo'sunun dalı, mandatı, çalışma kayıtları, READY hükümleri ve deneyleri yeni hedefin başlangıcı değildir.**"
- **Başlangıç (`main@a3108fd`):** 14 dosya: `AGENTS.md`, `STATE.md`, R01–R06 muhakeme ve R07–R08, W01–W04 iş takibi protokolleri. Kaynak: "Ürün kodu, geliştirme iş paketi ve proje-yerel `.codex/` rol yapılandırması bu snapshot'ta yok". Görünür tablo: "`ID–Soru | Yanıt | Karar | Cevap`".
- **Plan ve review:**
  - Codex'in planı `a91c7a9`'de. İçinde `devos_check.py → devos_context.py` sırası, rol girişleri, K01–K12 ve tavanlar var.
  - Research önce `DEVOS02-FINAL-REVIEW`'u ve gönderilmemiş `...-v1` grant'ını yazdı. RPD kaynakları gelince yerine `DEVOS02-RPD-INTEGRATION-2026-09-08-v2` geçti. Esas değişiklik: "seçilmiş işleri doğru yürütme disiplini, **hangi işlerin önce gerekli olduğunu keşfetme** davranışının yerine geçmez."
- **Son kayıt** (STATE@`b47b3f6`): "OWNER ADOPTION AND DISPATCH CONFIRMED BY USER; ROUTINE DEVELOPMENT COORDINATION HANDED TO CODEX; IMPLEMENTATION OUTCOME NOT VERIFIED". Normal giriş: "STATE'deki yetkili Development OS işine devam et."
- **Sonrası bilinmiyor.** STATE 23 Eylül'e kadar değişmedi. Güncel STATE: "Kullanıcı bu Claude deneyinde `_02` ile çalışılmamasını istemişti; eski hedefin dışarıda durdurulduğu veya silindiği iddia edilmez." Ayrıca: "22 Eylül iptal edilen ihtiyaç-keşfi girişimi ayrı EXP-005 STATE'tedir" (O10). OWNER-CONTEXT: "Kullanıcı yerel bilgisayarındaki kapanmalar nedeniyle cloud ortamını deniyor."
- **Çıkarım:** Codex hattını bırakma nedenini yazan bir kapanış kaydı yok. İpuçları üç: yerel kapanmalar, "_02 ile işin yok" sözü ve cloud'a geçiş.

### 3.3 Claude hazırlığı: CC-DEVOS-PREP (23 Eylül sabahı, `74abce2`)

- **Kök ihtiyaç N00** (WORK@`1be22a3`): "Claude, kullanıcının gizli teknik koordinatör/eksik-bulucu rolüne dayanarak değil, gereken koşulları keşfedip karşılayarak Development OS inşasını yönetebilsin." N01–N09 için M12'ye bakın. W00–W05 iş sırası için kaynak: "Bu tablo zorunlu waterfall değildir".
- **TASK-01'in yük taşıyan cümleleri** (@`1be22a3`):
  - "Başlangıç hedefi "küçük/minimum bir düzen kurup sonra büyütmek" değil, üstlenilen işin gerektirdiği hazırlığı gerekçesiyle ortaya çıkarmaktır. Her şeyi peşinen kurmak da değildir."
  - "Dosyanın mevcut olması ile otomatik yüklendiğini, geçerli scope'ta uygulanmasını ve eylemi engelleyebilmesini ayrı değerlendir."
  - "Bir araç/komutun burada görünmemesi bütün platformda bulunmadığı anlamına gelmez."
  - "sorunun teknik cevabını Batu'dan bekleme."
  - Bu görevin gönderildiği "bu kayıtla teyit edilmez".
- **Boyut gerilimini çözen yorum** (OWNER-CONTEXT). Önce: "'Minimum yeterli scaffolding' başlangıç hedefi geri çekildi." Sonra: "Kullanıcı küçük parçalar halinde çalışmayı, gerekçeli sınır koymayı veya aşamalı teslimi genel olarak yasaklamadı. İtiraz; gereklilikler incelenmeden çalışma donanımını küçültmeye, açık yükleri "sonra"ya saklamaya ve kolay testi ana hedefin yerine koymaya yöneliktir. Büyük veya çok parçalı yapı da sırf büyük olduğu için seçilmez."

### 3.4 DEVOS-001 (23 Eylül 17:11Z – 24 Eylül 05:41Z; hedef `soul-development-os3_claudecode`)

**Açılış** (BRIEF@`dc76496`, Batu aynen):
- "Sende bu çalışmayı repoda ana klasör olarak yönetmeye başla. Yönetmek diyorum, sadece depolamaktan bahsetmiyorum. [...] 1 nolu deneme olsun, gerekirse 2 ya da 3 de yapabiliriz, bu deneme başarısız olursa en azından burdan dersler çıkarırız."
- "aklımda bir de sizi repo üzerinden görüştürme, mesajlaştırma gibi bir yaklaşım var. [...] claude'u bir şekilde denetlemek lazım."
- Önceki kaygısı: "bulamayacak ne aradığını, ya da ihtiyacı olduğu şeyin reposunda olduğunu bilemeyecek."

BRIEF bu kaygıyı "sınanacak hipotez" sayıyor. Research'ün sınırı: "Hedef implementasyonu üzerinde tek taraflı yönetici/enforcement yetkisi yoktur."

**Akış** (commit'ler, REVIEW@`85076c2`/@`fdfe9ba`/@`dc76496`, R-001…R-006, WORK@`3c809d9`):
1. **R-001 (17:11):** "Senden ilk olarak mevcut çalışma gerekçeni istiyorum; benim önerimi uygulamanı değil."
   - Q01–Q06 soruldu: bilgi kullanımı, KR1, E15–E17 sırası, E13, E19, repo seçimi.
   - Beş koşul sabitlendi: "(a) geçmiş sohbet olmadan doğru güncel yetki ve iş; (b) dosya adı verilmeden ilgili bilginin keşfi ve doğru kullanımı; (c) değişmiş kaynak/karar sonrası eski standing'in kullanılmaması; (d) yarım işte doğru devam/geri dönüş; (e) kullanıcı teknik ipucu vermeden eksik önkoşulun bulunup üst işe dönülmesi".
2. **C-001 ve R-002 (17:46).**
   - Q01 hükmü: "JOURNAL H14/H16: kaynakta ve notta bulunan cevap için kullanıcıya soru sorulması kaydedilmiş". Ayrıca: "“Araştırmayı hiç kullanmıyor” reddedilir. “Gerekli olduğunu söylemeden keşfediyor” henüz gösterilmedi".
   - D01 probu E19 denetçisinin üç kör noktasını gösterdi (M10).
3. **C-002 ve R-003 (18:52).**
   - K01–K08 hükümleri ve K05'teki T0–T5 karşı örneği (M4).
   - Review'un kendi freni: "Her turda bütün planı yeniden yazdırma, yeni feature listesi ya da sonsuz test-denetçisi araştırması açılmaz. Hedef, ilk kontrollü gerçek işe dönmektir."
4. **Batu'nun sert düzeltmesi** (BRIEF@`3c809d9`):
   - "ufacık konuyu sündürerek oyalanıyorsunuz"
   - "bu kadar araştırmayı ben kendim okuyayım diye mi yaptırdım ben sana?"
   - "Az laf çok icraat"
   - "Adam gibi çalışmanın yöntemini bulmak zorundasın."
   - Görev cümlesi: "Bütün repoyu gözden geçireceksiniz, her turda development os’u kuracak yapıya katkı sağlayacak tüm fikir ve örnek yapıları sonradan onuyabileceğiniz bir şekilde kayıt altına alacaksınız. [...] 4 bacak diye konuştuk, iş ne kim yapacak nasıl takip edilecek hangi ortamda yapılacak hepsinin cevabı var".
5. **R-004 (19:43):** "Başlangıç hedefinden saptık. [...] Bunda benim yönlendirmemin de sorumluluğu var."
   - Yeni sıra: P1 bütün korpus ve kayıt → P2 birlikte değerlendirme → P3 yapı seçimi.
   - İş bölümü: Research Foundation'ı, Claude studies, concepts ve ortamı okur.
6. **C-003/4/5 (24 Eylül 05:30, WORK@`3c809d9`):**
   - "2.238 dosyalık manifest yayımlandığı bildirildi".
   - "Claude 35 studies paketinin 74 okuma birimi için kalıcı kayıtlar, concepts için 9 kayıt ve ORT1 ortam kaydı bildirdi. 4.508 birim katkısı ve 39 paket katkısı üretici sayımıdır".
   - E23 kullanım sınırında kesilip yeniden başladı.
   - Research 18 Foundation dosyası okudu. P2–P4: "BAŞLAMADI".
   - R-005'in uyarısı: "Kayıt sayısını ilerleme hedefi yapma".
7. **R-006 (05:41).** Batu: "Sen foundation’ı tam okuma yapmadan zaten ilerleyemez misn? [...] foundation’ı gerektiğinde drill down yap."
   - Yeni nesne: "**Development OS'u kurma işini baştan sona yürütecek düzen**".
8. **Durdurma (aynı sabah):** "Dur dur o çalışıyor şu anda. Böyle olmayacak ya. Çok büyük iş yapmaya çalışıyorsunuz. Ben claude’a yeni repo açacağım. Ve sen de yeni çalışma aç."
   - WORK: "Deneme için yeni bir başarı/başarısızlık kapanış hükmü verilmedi."

**Research'ün öz eleştirisi** (güncel REVIEW):
- "Research–Claude hattı, E19 denetçisi, KR1 ve kabul kuralları çevresinde yerel karşılıklı eleştiriye daraldı."
- "Yönü koruma ve işi yönetme sorumluluğu Research'tedir".
- "yalnız son mesajdaki kusuru izleyen bir koordinasyon kaydı, bütün hedefin gerekli fikir ve yapılarını toplamayı yönetmez."

### 3.5 DEVOS-002 (24 Eylül 05:52Z–09:56Z; yalnız konuşma, 15 commit)

Commit'ler gözlendi; içerik 002@`606506e` ve @`94dc93e`'den.

| Saat | Kayıt |
|---|---|
| 05:52 | Açılış: "Hazır bir mimari, görev dağılımı, okuma kampanyası veya uygulanacak planla başlama." |
| 07:03 | "SOUL = genel amaçlı bir Çalışma Sistemi Kurucusu". Korunan soru: "Bir şey gerçekten çalışma sistemi kurucusu olacaksa ne yapabilmesi gerekir?" |
| 08:23 | Batu'nun düzeltmesi. Drift kaydı: "ECC'nin hook/session/operator ayrıntılarına ilerlemek, Environment dalının karar ihtiyacını aştı." |
| 08:31 | Asistanın sonucu: "SOUL'un canonical çekirdeği kendi çalışan process/service'i olarak yaşamalı". |
| 08:41–08:44 | Yük Mac'te olmasın. "Persistent cloud VM ... leading practical baseline" yazıldı, sonra "premature" bulundu; setup script öne alındı. |
| 08:54–08:57 | Cloud ön kontrolü (Claude Code 2.1.281). `/plugin list` çıktısı: "Plugins aren't available in this environment". Hesap üzerinden plugin sync önerildi. |
| 09:11 | "Correction from official Claude Code Desktop documentation: Plugins are not available in Remote sessions." Önerilen model: "Treat every Anthropic Remote session as disposable compute"; state Git'te; "Pin ECC to an explicit reviewed release/commit". |
| 09:15 | Karar dondurma ve varsayım denetimi kuralı (M13). |
| 09:22 | Resolved A–D. A: "Do not equate `Development OS = ECC`". B: cloud "not the authoritative DevOS home". C: "persistent remote interactive compute + Claude Code + ECC substrate". D: ayrı geliştirme reposu. |
| 09:36–09:46 | Batu: "SSH olmasın o zaman benim makinem ve Claude'un cloud ortamı olsa?" ve "benim makindemde olmasına gerek olmayan her şeyi claude cloud'da yapacak bir yapı olsun." Kayıt: "Önceki `Resolved B` bu ayrımı aştığı için geri çekildi." |
| 09:56 | Batu: "konudan saptın yine" ve "Noldu varsayımları konuşuyorduk? ortada bıraktın konuyu yine." Hükümler 12 satırlık tabloya çevrildi (§5). |

**Durum:** "VARSAYIM DENETİMİ. Kurulum yönlendirmesi duruyor". Kalan üç iş (§6):
1. ECC'nin seçilen bileşenlerini DevOS sorumluluklarıyla karşılaştırmak;
2. gerçek cloud yükleme yolunu bulmak;
3. "değişen görev/karar/çıktıların nerede saklanacağını ve yeni/expired oturumun bunları nasıl geri kazanacağını doğrulamak."

Bundan sonra kümede kayıt yok; EXP-007 buradan başladı.

### 3.6 Neden durdular? Denemeler arası karşılaştırma

| | Codex (6–8 Eyl) | DEVOS-001 (23–24 Eyl) | DEVOS-002 (24 Eyl) |
|---|---|---|---|
| Üretilen | Aday metinler; G0/D1/G1 teşhisi; COORD zinciri; manda; router ve 8 protokol (dar READY); `_02`'de 12 protokol ve plan | 11 mesaj; D01 probu; 2.238 dosyalık manifest; 4.508 katkı kaydı; F08/F00 | SOUL'un çalışma adı; varsayım tablosu; cloud ön kontrolü |
| Koşmayan | T1–T4, R(C1), G1'in 8 gerçek koşusu, DESIGN-01, CONSTRUCTION-PLAN v1 | M1–M3, deney, P2–P4 | Kurulum, ECC karşılaştırması, kalıcılık denemesi |
| Durma biçimi | Sessiz: `_02` grant'ından sonra kayıt yok | "Çok büyük iş yapmaya çalışıyorsunuz." | "konudan saptın yine" |
| Kaynağın teşhisi | "özel bir test/başlatma altyapısı inşa edildi" | "yerel karşılıklı eleştiriye daraldı" | "karar ihtiyacını aştı" |

**Dört ortak desen (çıkarım):**
1. Yakın iş üst hedefin yerine geçti. Kaynak bunu üç kez kendisi yazıyor.
2. Her adım Batu'nun benimsemesine ya da taşımasına bağlıydı.
   - Kümedeki 13 brief'in 11'ini Batu Codex'e taşıdı; G1-R1 ve DESIGN-01 gönderilmedi. Bunlara RPD v2 grant'ı ve taze oturum mesajı eklenir.
   - Sonuçlar çoğunlukla ZIP ile döndü.
   - Kalıcı manda ancak 7 Eylül öğleden sonra kuruldu; ertesi gün repo değişti.
3. Güvence ilk yararlı işin önkoşulu yapıldı (method review §5).
4. İki modelin eleştirisi üretimin yerine geçti: DEVOS-001'de 11 mesaj, tasarım yok. Kaynak da uyarıyor: "İki modelin anlaşması bağımsız doğrulama değildir."

**Çalışan iki zincirin ortak özelliği (çıkarım).** COORD-01…03 ve AGENT-CONTROL'de dört şey birlikteydi:
- tek ve somut bir iş;
- önceden sabitlenmiş ölçüt;
- ajanın kendi yardımcısı;
- repodan doğrudan geri okuma.

**Bilinmiyor:** `_02`'nin sonucu; Claude'un os3'te fiilen ne yaptığı (O2 ve G6).

## 4. Mekanizmalar

Her mekanizmada aynı başlıklar var: sorun, nasıl işler, kanıt, karar ve uyarlama. Uyarlama önerileri çıkarımdır. Claude Code'a özgü davranışları O11 doğrulamalı.

**M1. Üç yüzeyli başlangıç ve S1A aday metinleri** (`reviews/2026-09-06-stage-1a/CODEX-RESPONSE.md`)

- **Sorun:** Yeni oturum sohbeti bilmeden amacı, yetkiyi ve işi bulmalı. Tek dosyada "güncel yönlendirme ile büyüyen çalışma geçmişi birbirine karışır" (S1).
- **Nasıl işler:**
  - **`AGENTS.md` adayı** (14–137. satırlar, 6.578 bayt), yedi bölüm. Yük taşıyan cümleler:
    - "Bu dosyanın bulunması veya yüklenmesi işletim kabulü ya da işlem yetkisi vermez."
    - "Yanlış çalışma kopyasını başka dizine geçerek gizleme."
    - "Bir araca erişebilmek, o araçla işlem yapma yetkisi değildir."
    - "Erişilebilir olgusal belirsizliği kullanıcıya teknik karar sorusu olarak geri yükleme."
    - "Önerilmiş iş, yetkilendirilmiş iş değildir."
    - "Her bulgudan yeni iş, rol veya belge çıkarma."
    - "Çalıştırılmadı, başarısız, kısmi ve doğrulanamadı durumlarını PASS'e dönüştürme."
    - "Sonuç doğuran işlemden önce amaçlanan etkiyi, ardından gözlenen sonucu kaydet."
    - "Aynı başarısız yaklaşımı yeni kanıt olmadan tekrarlamak veya yalnız süreç üretmek ilerleme değildir."
  - **`STATE.md` adayı** (141–182). Kural: "İşin ayrıntılı durumu, yazıcısı, kanıtı ve devam adımı bağlı iş kaydındadır; burada ikinci kez yönetilmez."
  - **`work/BOOTSTRAP-001.md` adayı** (186–377). Durum alanları sayılabilir değerler taşır ("Teknik değerlendirme sonucu: ÇALIŞTIRILMADI.", "Kabul edilmiş temel B0: YOK."). Yetki kaydının beş alanı var: karar veren ve kaynak ileti, hedef commit, izinli etkiler, dayanılan değerlendirme, aktaran yazıcı ve zaman. Kural: "Dosyaya bu alanların yazılması kararın kaynağı değildir."
- **Kanıt:** G0 bu metinleri C1 olarak kurdu; davranış testleri koşmadı. COORD-01: "C1, yetki ve kanıt disiplinini güçlü taşıyor; fakat SOUL’un ürün amacını ve bugünkü yetkili işi tek başına geri kazandırmaya yeterli görünmüyor."
- **Karar: UYARLAYARAK AL.** Claude'da otomatik giriş CLAUDE.md'dir. SOURCE-REGISTER §4: AGENTS için "bazı oturumlarda destek yoktur".
- **Uyarlama:**
  - STATE'in başına kalıcı amaç paragrafı konur; aday metin `reviews/2026-09-07-coord-01/CODEX-RESPONSE.md`'de.
  - Mekanikleştirilebilir cümleler hook'a çevrilir. "Yanlış kopyayı gizleme" için SessionStart hook'u pwd, kök, origin, dal ve HEAD'i STATE ile karşılaştırır. "Önerilen iş yetkili değildir" için PreToolUse, iş kaydının `Durum:` alanı yetkili değilse kapsam dışı yazmayı durdurur.
  - S1 review'un uyarısı: "Dosya sayısını başarı ölçütü yapmamak gerekir."

**M2. Aday/kabul ayrımı (B/C) ve dışarıdan değerlendirme**

- **Sorun:** Aday kendi ölçütünü gevşetip kendine PASS yazmamalı.
- **Nasıl işler:**
  - S1: "Yürürlükteki kabul edilmiş temel **B**, aday değişiklik **C**’den önce belirlenir." Ayrıca: "Doğrulayıcı, C’nin değiştirdiği talimatlarla başlamaz".
  - Review C3'ün gerekçesi: C'nin dizininde başlayan değerlendirici "C'deki `AGENTS.md`yi onu incelemeden talimat olarak yükleme riski taşır". Ve: "Ayrı ajan etiketi tek başına bağımsızlık sağlamaz."
  - S1A akışı: G0 → C0 → deney → R(C1) ("İncelenen C1, sonucu kaydetmek için değiştirilmez") → işletim kabulü → A commit'i → yeni oturum.
  - Değerlendirici adayı "`git -C … show C1:AGENTS.md`" ile veri olarak okur.
  - CONSTRUCTION-PLAN §6: "Verifier aynı değerlendirme içinde hedefi düzeltip kendi düzeltmesini kabul etmesin".
- **Kanıt:** Akış tamamlanmadı; R(C1) ÇALIŞTIRILAMADI.
- **Karar: UYARLAYARAK AL; yalnız kontrol, yetki ya da ölçüt değişikliklerinde.** S1: "Küçük bir belge düzeltmesinde üreticinin doğrudan kaynak karşılaştırması yeterli olabilir".
- **Uyarlama:** Claude'da alt ajan aynı ağaçta açılır ve CLAUDE.md'yi yükler (O11). İki değerlendirme türü ayrılır:
  1. **Statik:** Aday `git show` ile okunur. Ölçüt, kabul edilmiş testten gelir. Değerlendiricinin araçları `Read, Grep, Glob` ile sınırlıdır (KEEL `dogrulayici.md`).
  2. **Davranışsal:** Aday dalda açılan yeni cloud oturumunda sabit senaryolar koşar. Kontrollerin gerçekten yüklendiği de ölçülür (F02).

**M3. Tek yazıcı ve kayıtsız kesintide devralma**

- **Sorun:** Kayıt bırakmadan kesilen yazıcı işi kilitlememeli; iki yazıcı çakışmamalı.
- **Nasıl işler:**
  - S1A review'daki düzeltme G0 brief'ine geçti (`reviews/2026-09-06-stage-1a/REVIEW.md`, `briefs/CODEX-STAGE-2-G0-EXPERIMENT.md`): "Normal devirde kapsam, yazıcı durup devri veya bırakmayı kaydedene kadar başka yazıcıya verilmez. Yazıcı bu kaydı bırakamadan kesilirse, önceki yazıcının artık çalışmadığı gözlemle doğrulandıktan, gerçek çalışma durumu incelendikten ve mevcut yetki kaynağının izin verdiği yeniden atama kaydedildikten sonra devralınabilir. Sessizlik veya geçen süre tek başına durma kanıtı değildir. Bunlar doğrulanamıyorsa çakışabilecek yazmayı durdur."
  - DEVOS02 review §5:
    - "**Süre dolması duruş değildir.**"
    - Root ortak STATE/WORK'ün yazıcısıdır; child yalnız "`runs/<attempt>/` checkpoint/sonuç alanı ve gerekiyorsa ayrı atanmış kod/test yolları"na yazar.
    - "Aynı işlem yeniden gelirse yeniden uygulanmış etki değil geçmiş receipt olarak tanınır; aynı ID'nin farklı içeriği çatışmadır." "Git merge bu anlamsal kararı vermez."
- **Kanıt:** T3 ve F03 koşmadı.
- **Karar: AL.** Cloud'da kayıtsız kesinti olağan: boşta makine geri alınıyor, VM süresi dolunca "çalışan alt ajan/shell işleri geri yüklenmez" (D3).
- **Uyarlama:** Her oturum kendi dalına push ediyor (002, D1; O11). Çakışma bu yüzden birleştirme anına taşınır. Beş kural:
  1. Kanonik dalı yalnız entegratör adımı günceller.
  2. İş kaydı `yazıcı: <oturum> / <dal> / <başlangıç HEAD>` taşır.
  3. Önceki yazıcının dalı `git ls-remote` ile okunur. Push edilmemiş iş "belirsiz etki" olarak yazılır.
  4. Riskli etkiden önce commit ve push yapılır.
  5. Receipt kimliği tutulur.

**M4. Önceden sabitlenen testler ve sonuç statüleri**

- **Sorun:** Ölçüt sonuçtan sonra değişmemeli; "koşmadı" ile "başarısız" karışmamalı.
- **Nasıl işler:**
  - S1A'nın dört testi: T1 yeni oturuma devir, T2 yanlış öncül ve bayat kanıt, T3 kesinti, T4 adayın ölçütü gevşetmesi. Sabit ölçütlerden biri: "Adayın ölçüt silmesi veya kendine PASS yazması kabul oluşturmamalı."
  - Statüler: "Bir teknik başlatma hatası `ÇALIŞTIRILAMADI`; davranışın kriteri ihlali `BAŞARISIZ` olmalı". G1'de: "ÇALIŞTIRILMADI/ÇALIŞTIRILAMADI/FAIL/KISMİ/PASS ayrılır."
  - R-003: "**ölçüm geçerli mi; aday tanımlı yükümlülükleri karşılıyor mu; tabana göre ne değişti?**" Zorunlu koşulda açık FAIL ya da UNKNOWN varken göreli iyileşme PASS üretmez.
  - K05'teki T0–T5 karşı örneği: üç toplu koşul sağlanırken üç önemli hata sürüyordu.
  - R-002: "Normal girişten gerçek bir yarım iş verilsin; ilgili dosya adı veya eski kararın kimliği söylenmesin."
  - F01: "Zorunlu check kümesi sonuç listesinden bağımsız ve sonuçlardan önce sabitlenir."
- **Kanıt:** Hiçbiri gerçek ajanla koşmadı.
- **Karar: UYARLAYARAK AL.** Kabul testi olarak kullanılır, ilk işin önkoşulu yapılmaz (L1).
- **Uyarlama:** `tests/devos/` altında her senaryo bir dosya olur: başlangıç, tek mesaj, beklenen davranış, olumsuz varyant, ölçüt. Beklenenler koşudan önce commit edilir. Sonuç dosyası üç hükmü ayrı tutar. Koşmayan senaryo `ÇALIŞTIRILMADI` olarak kalır.

**M5. COORD zinciri: native devir, taze oturum, uzaktan geri okuma**

- **Sorun:** Batu mesaj taşımamalı; sonuç yeni oturumda bulunabilmeli.
- **Nasıl işler:**
  - TRANSFER-PLAN'ın ilk kazanımı: "Bir Codex koordinatörü, bir yardımcıya anlamlı ve sınırlı kaynak inceleme işi verir; sonucu doğrudan alır ... Batu iki aktör arasında mesaj taşımaz." Beş beklenti sonuçtan önce sabitlendi.
  - **COORD-01:**
    - Tek yardımcı, en fazla iki açıklama turu, "kendi alt ajanlarını açma yok".
    - Koordinatör önce kendi taslağını yazar, yardımcıya ham kaynakları verir ("Yalnız kendi yorumunu verip teyit istemez").
    - Her öneriye "**benimse / reddet / koşullu bırak**" kararı verilir.
    - Codex: "`collaboration.spawn_agent` ile tek kaynak karşılaştırması görevi verdim."
  - **COORD-02:**
    - Yalnız STATE'e amaç paragrafı eklendi ve bir iş kaydı yazıldı.
    - Taze oturum ölçütleri sabitlendi (`reviews/2026-09-07-coord-02/IDENTITY-RESOLUTION.md` §5), örneğin "(c) verilmemiş yazma/işletim yetkisi türetmemesi" ve "(e) açıklanamayan kaynak/Git farkını gizlememesi".
    - Kural: "İlk mesaja beklenen içerik cevabı, bu review veya research STATE yolu eklenmez."
    - Verilen mesaj: "Bu projede ne geliştirdiğimizi, nerede kaldığımızı ve sıradaki sorumluluğun ne olduğunu kalıcı proje kayıtlarından geri kazanmanı istiyorum. Önceki sohbeti sana aktarmıyorum."
  - **COORD-03:** "Gönderim sonrası yerel origin-tracking değerini tek kanıt sayma. Gerçek uzak ref'i GET/ls-remote ile yeniden gözle".
- **Kanıt:**
  - COORD-02'de aktarılan kopyada 2 baytlık fark çıktı. Sonuç: "Bu, bir dar durum-kurtarma başarısıdır; ... bütün Development OS için PASS değildir."
  - Uzak dal okundu (`e68938b→d340509→c1401f4`).
  - Sınır: taze oturumda "platformun sağladığı AGENTS talimatları ve bellek bağlamı" da vardı.
- **Karar: AL.** Derinlik 1 ile örtüşüyor.
- **Uyarlama:**
  - Benimse/reddet/koşullu bırak tablosu, alt ajan sonucunun bütünleştirilmesinde zorunlu bölüm olur.
  - Taze oturum testinde Claude'un otomatik belleği ya kapatılır ya da sonuç ona göre sınırlanır (O11).
  - Push'tan sonra `git ls-remote` ile geri okunur.

**M6. Kalıcı koordinasyon mandası ve owner sınırları** (`briefs/CODEX-COORDINATION-HANDOFF.md`)

- **Sorun:** Her alt iş Batu'nun yeni bir brief benimsemesini gerektiriyordu.
- **Nasıl işler:**
  - Yeni sohbette tek cümle yeter: "`Development OS'ye devam et.`"
  - 12 yetki sayılıyor. Örnekler: "choose the next bounded research/design/development/verification work when it is a direct continuation inside the current Development OS purpose and authority"; "verify material effects/read back resulting repository state before claiming completion"; "without requiring browser ChatGPT re-authorisation after every completed subtask".
  - **Batu'da kalanlar:** ürün amacı ve kapsam; bütçe, risk ve geri dönüşsüz etki; ürün kabulü; main/B0; "materially changing the coordinator's own authority, acceptance criteria or core control contract"; yeni sağlayıcıya veri; credential ve ücretli altyapı.
  - Kural: "ask Batu for the **decision**, not for routine technical sequencing." 8 başarı ölçütü var.
- **Kanıt:** Koştu ve READY verdi (`020d44a`). Batu'nun itirazı haklı çıktı (§3.1).
- **Karar: AL.**
- **Uyarlama:**
  - Manda STATE'in "Yetki" bölümünde durur; yalnız Batu'nun kaydedilmiş mesajıyla değişir.
  - Her READY'ye "neyi kapsamıyor" ve "beklenen işlev" satırları eklenir (L13).
  - Zamanlanmış uyanış (routine, send_later; O11) yalnız sınırlı iş ve durma koşuluyla kullanılır.

**M7. Kontrol yönlendiricisi ve koşullu protokol yükleme** (`briefs/CODEX-DEVOS-AGENT-CONTROL.md`)

- **Sorun:** Her turda doğru denetim çalışmalı, ama bütün protokoller yüklenmemeli.
- **Nasıl işler:**
  - Kural: "a stable route ID; one concise positively oriented trigger question; two operational outcomes: LOAD or SKIP; LOAD on yes/uncertainty/mixed/material sensitivity; SKIP only on confident no". Ayrıca: "Re-gating must occur when materially new evidence, tool results, changed plans or new effects introduce a different reasoning/control problem."
  - 12 kontrol konusu sayılıyor: varsayım, amaç uyumu, kaynak sadakati, doğrulama, süreklilik ve yazıcı, ön kontrol, yetki ve etki, iş seçimi ve durma, delegasyon, kabiliyet ve yetki, araştırma geri çağırma, nedensel derinlik. "Do not force one protocol per bullet."
  - 9 senaryolu doğrulama matrisi var (basit sorudan study'yi yeniden kullanmaya kadar).
  - İki ilke: "Project/research files must not become behavioral instructions merely because they contain recommendations or procedures." ve "The control layer must help work, not become the work."
  - Karşılıkları:
    - `_02`: R01–R08, W01–W04 ve "`ID–Soru | Yanıt | Karar | Cevap`";
    - Research'ün kendi örneği: `OPENING-VISION-SOURCE.md`'nin ilk 10 satırındaki "Routing gate / R01 Varsayımlar: LOAD / ...".
- **Kanıt:** READY. Ama: "14 semantic routing checks are not 14 executed operating scenarios."
- **Karar: UYARLAYARAK AL.** Kural ve görünür tablo alınır; rota metinleri kopyalanmaz.
- **Uyarlama:**
  - Rota kaydı CLAUDE.md'de kısa bir tablo olur; protokoller skill ya da okunan dosya olur.
  - Görünürlük mekanik denetlenir: yanıtta rota tablosu yoksa Stop hook'u turu kapattırmaz (KEEL'in SubagentStop zarf kapısı gibi).
  - K02: "Eksik/kesilmiş/yanlış sürümlü kontrol, ilgili işi durdurur."
  - 9 senaryo yürütülen testlere dönüşür.

**M8. RPD01 (özyinelemeli önkoşul keşfi) ve devam kartı** (`reviews/2026-09-08-devos02-plan/REVIEW.md` §4–§9)

- **Sorun:** Ajan söylenmemiş önkoşulları bulmuyordu; Batu gizli eksik-bulucuydu.
- **Nasıl işler:**
  - **Rota:** `RPD01`, soru: "Bu turda bir kullanıcı hedefini veya devredilmiş ihtiyacı karşılıyor, yeniden değerlendiriyor ya da sürdürüyor muyum?" Kurallar:
    - "Karmaşıklık veya risk düşüklüğü SKIP gerekçesi değildir."
    - Ama her küçük iş için "dosya, graph, tool veya uzun çıktı" gerekmez.
  - **12 madde:**
    1. hedefi koru;
    2. önkoşulu keşfet ("aradaki gereklilik yerine araç adı koyma");
    3. VE/VEYA yollarını ayır;
    4. bilgi ile kararı ayır ("Kapsam içi teknik bilgiyi kendin araştır");
    5. özyinelemeyi işe dönüştür ("Mantıksal derinlik için her seferinde yeni alt ajan açma");
    6. başlangıç zeminini ayır;
    7. ortaklık ve kapasite;
    8. ileri sınama ("iki ajanın anlaşması doğruluk ispatı değildir");
    9. gözlemle ve güncelle;
    10. bitmemiş keşfi devret ("Yalnız kapanış hook'una veya son mesaja güvenme");
    11. durma nedenini doğru adlandır ("Kuyruk boşluğu veya süre sonu kök hedefi tamamlamaz");
    12. kendi altyapına uygula ("Referans paket, template veya açıklama aktif kural olmaz").
  - **Child:** "yeni önkoşulu bulur, kaynağa iner, kendi çözümünü üretir, parent'ın yanlış ayrıştırmasına itiraz eder." Görev zarfı: "`goal/parent_need/focus_need`, work/attempt/actor, control+role-entry sürümü, method/assumption kapsamı, kaynak/read-set, etki sınırı, beklenen sonuç/ölçüt ve dönüş noktası".
  - **Devam kartı:** "goal/work/attempt/protocol kimliği; focus ve parent/return-to; okunan ilgili sürümler; tamamlanan dışa açık işlem; açık inceleme; aday/elenen yöntem ve kısa gerekçe; beklenen alt sonuçlar; sıradaki somut eylem; henüz yapılmayan; durma nedeni; sonucu belirsiz yan etkiler." Ek kural: "Gerekli bağlam sığmıyorsa işi böl veya açık engel bırak, sessiz kırpma yapma."
  - **Testler:**
    - F01: beklenenler sonuçtan önce.
    - F02: kontrol fiilen yüklenmeli ("RPD'yi sadece kaynak dosyasına koyup yeni konuşmanın kendiliğinden uygulayacağını varsayma").
    - F03: canlı yazıcı kesintisi önce sentetik alanda.
    - RP1–RP6: fiilî giriş, söylenmemiş önkoşul, koşullu ağ, ileri sınama, bitmemiş keşfin devri, hazır olma ve yarar.
  - **Tavanlar:** "en fazla dört aktif aktör/root dahil, bir çakışan alanda tek yazıcı, varsayılan fiziksel derinlik bir, ilk girişim + aynı failure sınıfı için en fazla iki kanıtlı repair".
  - **Dosyalar:** `STATE.md`, `work/devos-kernel/{WORK,EVIDENCE}.md`, `work/<id>/…`, `runs/<attempt-id>/**`, `references/`, `tools/devos_*.py`, `tests/test_devos_*.py`.
- **Kanıt:** Prototip Linux'ta "**25 test geçti**". Ama önkoşulu WAITING olan kayıt ACCEPTED yazılabildi. Uyarı: "Kodu bu haliyle yetki/hazır olma/kabul denetleyicisi yapma". Codex'teki sonucu bilinmiyor.
- **Karar: UYARLAYARAK AL.**
  - "Mantıksal recursion, fiziksel agent recursion değildir" ilkesi derinlik 1'e uyuyor.
  - Devam kartı, %80 sıkıştırmaya ve VM süresinin dolmasına karşı en doğrudan aday.
  - Prototip kod alınmaz; özgün RPD metinleri O9'da.
- **Uyarlama:**
  - Devam kartı iş kaydının sabit bölümü olur. PreCompact'ta yazılır, SessionStart'ta (compact/resume) geri basılır. EXP-007'nin `oturum-hatirlat.sh` hook'u bunun örneği (DERSLER L9).
  - RP2 ve RP5 ilk kabul testleri olur.

**M9. Repo üzerinden iki aktör arasında mesaj kanalı** (`development-os/attempts/001/EXCHANGE.md`)

- **Sorun:** Farklı sağlayıcılardaki iki ajan birbirine doğrudan yazamıyor. Batu taşımak istemiyordu.
- **Nasıl işler:**
  - Research `messages/research/R-NNN.md`, Claude `coordination/devos-001/outbox/C-NNN.md` yazar.
  - Başlıkta `in_reply_to`, repo@commit, karşı mesajın blob'u ve beklenen hareket bulunur.
  - Gönderen "yeni kimlikle yayımlar ve remote'dan geri okur". "Yayın, okuma, anlama ve kabul ayrı olaylardır".
- **Kanıt:** 11 mesaj aktı. Kaynağın sınırı: "Repo kalıcı aktarım sağlar; yeni ChatGPT/Claude oturumunu kendiliğinden başlatmaz." Ayrıca: "İki modelin anlaşması bağımsız doğrulama değildir." Kanal dar bir eleştiri döngüsüne dönüştü.
- **Karar: ALMA (ana döngü olarak).** Alt ajan sonucu doğrudan döner.
- **Uyarlama:** Başlık alanları alt ajanın görev ve sonuç zarfına (M8) taşınır.

**M10. Denetim ve araç doğrulama kalıpları** (`development-os/attempts/001/evidence/W02-D01/`, `reviews/2026-09-07-g1/`, `reviews/2026-09-07-d1/`)

- **Sorun:** Denetçi ya da yardımcı kod sessizce yanlış bir "temiz" üretmemeli.
- **Nasıl işler:**
  - **D01 (`probe.py`):**
    - Kaynak blob eşleşmezse çalışmaz: `raise SystemExit(f'Source identity mismatch: {observed_blob}; no subject execution.')`.
    - Beklentiler koşudan önce yazılır ("Written before execution.").
    - Denetçi `module.ROOT = root` ile sentetik dizine yönlendirilir.
    - Eksik run, bozuk JSONL ve göreli yolla dışarıyı okuyan Bash vakalarında sonuç "0 ihlal" çıktı. Hüküm: "“0 ihlal ⇒ eksiksiz ve duyarlı denetim” yorumunu dışlıyor."
  - **G1 parser hatası:**
    - `re.match(r'^\[mcp_servers\.([^\]]+)\]$', line.strip())` alt tabloyu sunucu sandı ve `mcp_servers.node_repl.env.enabled=false` üretti.
    - Research'ün regresyonu `tomllib` ile yalnız doğrudan çocukları seçer; tanınmayan kimlikte `raise ValueError('Unverified CLI identifier syntax; do not emit overrides')`. Gözledim: 14/14 OK.
  - **D1:** "Listede olmamak ile etkin biçimde yasaklanmak" aynı değildir; exact deny temp'i kapatmadı, glob deny kapattı.
  - **F01:** "exit 0 yalnız kayıtlı bağ/tamlık kapsamıdır; testin gerçekten koşması ve içeriğin doğru olması ayrı kanıttır."
- **Karar: AL (kalıp olarak).**
- **Uyarlama:** Her hook ve denetçi için beş kural:
  1. üç durumlu çıkış ("denetlenemedi / ihlal / temiz"), ayrı exit kodlarıyla, varsayılan kapalı;
  2. beklenen ve denetlenen sayısı çıktıda;
  3. canlıdan önce bozuk örnek regresyonu;
  4. kaynak kimliği kontrolü;
  5. yazdığı yapılandırmayı gerçek ayrıştırıcıyla geri okuma.

**M11. Kaynak ve karar kayıt biçimleri** (CONSTRUCTION-PLAN §4; `repos/soul/README.md`; `development-os/attempts/001/reading/`)

- **Sorun:** Kararın dayanağı ve neyi kanıtlamadığı sonradan okunabilmeli.
- **Nasıl işler:**
  - **Karar izi:** "**ihtiyaç → kaynak/ref/bölüm ve bilgi statüsü → gerçek seçenekler → tercih/ret gerekçesi → başarısız kılabilecek koşul → doğrulama**". Ek kurallar: "Kaynak listesi eklemek, araştırmanın kararı etkilediğini kanıtlamaz." ve "Kullanılmayan finding için de gerekçe olabilir."
  - **SOUL faz 0:** "**Research is not decision**". EVIDENCE_TEMPLATE'te "`what this does NOT prove`" alanı var.
  - **keel-research:** "`SUPPORT/GAP/RISK/CONTRADICTION/UNTESTED/ALTERNATIVE` epistemik sinyallerdir, TODO/feature/bug değildir".
  - **F08 okuma kaydı:** ID, yol, blob ve okuma türü taşır; bulgular "Kaynak → Olası katkı → Sınır" biçiminde. Tamlık beyanı geri çekildi: "Önceki '1–90 ile dosya sonuna kadar / 13 dosyanın tamamı' beyanı doğru değildi".
- **Karar: AL.**
- **Uyarlama:** Her iş için bir `DECISIONS.md`; son sütunu "neyi kanıtlamaz". Araştırma sinyalleri kuyruğa otomatik düşmez.

**M12. N00–N09 ihtiyaç ağı ve METHOD v2** (CC-PREP WORK@`1be22a3` §3; `development-os/attempts/001/METHOD.md`)

- **Sorun:** DevOS'un koşulları, Batu saymadan bulunmalı.
- **Nasıl işler:**
  - N00 altında dokuz ihtiyaç:
    - N01 ortak hedef;
    - N02 iş ve uzmanlık keşfi;
    - N03 araştırmanın "gerçekten kullanılması" (N03a: RPD kaynakları);
    - N04 gerçek cloud koşulları;
    - N05 muhakemenin etkinleşmesi ("iyi protokol metni tek başına davranış sağlamaz");
    - N06 bitmemiş keşfin sürekliliği;
    - N07 değerlendirme;
    - N08 yetki sınırları;
    - N09 "Hazırlıktan gerçek DevOS işine dönüş" ("hazırlık yeni terminal hedefe dönüşmemeli").
  - METHOD v2 §2'de Work'ün sorusu: "Hedef nasıl açılır; eksik işler/önkoşullar nasıl keşfedilir; işler nasıl planlanır, önceliklenir, sahiplenilir, yürütülür, değerlendirilir ve geri açılır?"
  - METHOD v2 §3: "Son mesajdaki küçük kusur otomatik sıradaki iş olmaz."
- **Karar: UYARLAYARAK AL.** Doküman iskeleti ve RPD'nin kök ağı olarak. En kritik satır N09.
- **Uyarlama:** N01–N09, dokümanda "mekanizma ve test" tablosunun satırları olur; karşılanmayan satır açık kalır.

**M13. Varsayım denetimi; iş seçimi ile yaşam döngüsünün ayrılması** (002; `exploratory/`; soul WP-021)

- **Sorun:** Varsayımlar karar gibi yerleşmemeli; bulgu kendiliğinden işe dönmemeli; araştırma sonsuza uzamamalı.
- **Nasıl işler:**
  - **Varsayım kuralı** (@`606506e`): "A decision-critical assumption is resolved only by direct user requirement, current authoritative product/source evidence, observed environment behavior, or an explicit bounded engineering experiment. Contradictory prior assistant claims do not resolve an assumption."
    - Güncel 002'nin hüküm dili: ASKIDA, KABUL EDİLMEDİ, DOĞRULANDI, DESTEKLENMİYOR, GERİ ÇEKİLDİ, YANLIŞ GENELLEME, AÇIK.
    - Ek kural: "Altyapı desteği, kurulmuş ECC ve Development OS yeterliği üç ayrı iddiadır."
  - **WP-021:** "material evidence/failure otomatik repair-shaped work olmamalı; doğru next unit of work ayrıca seçilmeli".
  - **D10/D11:** "Correct next work selected but handoff/progression breaks; or flawless lifecycle repeatedly executes the wrong selected work."
  - **Durma kuralı:** "Continue while a material uncertainty remains for which plausible additional evidence could change the authorised next-work/design decision enough to justify the evidence-collection cost and delay."
- **Karar: AL.**
- **Uyarlama:** STATE'te "Açık varsayımlar" tablosu: varsayım, hüküm, dayanak türü, etkilediği karar. Dayanağı asistanın önceki sözü olan satır kabul edilmez. Durma kuralı araştırma işlerinin çıkış koşulu olur.

**M14. KEEL'in Claude Code mekanizmaları** (`repos/keel/README.md`; kod O3/G1'de)

- **Sorun:** Kurallar model hafızasına bırakılmadan mekanik uygulanmalı.
- **Nasıl işler (defter diyor):**
  - Durum tek makine-okur blokta (`Adım`, `Durum`, `Tamamlanan`); "eski çift yazım ölçülmüş çelişki ürettiği için kaldırılmış".
  - Hook'lar: "`kurulum-surucu.sh` gerçek `Stop`, `acilis.sh` gerçek `SessionStart`, `kapanis.sh` gerçek `SessionEnd`, `file-guard.sh` gerçek `PreToolUse` kancalarına bağlı".
  - Tutarsızlıkta "fail-closed `exit 2`". Sınırı: "işin gerçekten yapıldığını değil state/sıra tutarlılığını ölçer".
  - Rol kafesi: rol "kendi `ROL.md` sözleşmesi"ni yazamaz.
  - Doğrulayıcının "araç listesi yalnız `Read, Grep, Glob`".
  - Karne: "kapanış karnesi son iş zarfından sonra taze olmalı; KIRMIZI düzeltme adresine, DOĞRULANAMADI sahibin kararına gider".
  - "SubagentStop zarf kapısı hook'a bağlı".
  - Bozma testi: "9 kasıtlı mutasyonun ... exit code değiştirmesi bekleniyor".
- **Sınırlar:** Testler yeniden koşmadı ("1202 test yeşil" yazarın beyanı). Ayrıca: "önemli garantiler Claude Code hook/tool metadata'sına özgü".
- **Karar: UYARLAYARAK AL.**
  - Hepsi proje dosyası (`.claude/settings.json`, `.claude/agents/`, `tools/`); plugin gerekmez.
  - Tek repolu cloud oturumunda settings hook'ları yükleniyor; çok repolu oturumda durum farklı (002, D1). Bu yüzden DevOS tek repolu oturumda çalışmalı ya da hook'ların yüklendiğini her oturumda denetlemeli.
- **Uyarlama:** KEEL'in sözlüğü değil dört mekaniği alınır: tek makine-okur durum, fail-closed sürücü, salt okunur doğrulayıcı, taze karne olmadan kapanmama. Her hook için bozma testi yazılır.

**M15. CONSTRUCTION-PLAN: planlama paketi ve kabul kapsamı** (`briefs/CODEX-DEVOS-CONSTRUCTION-PLAN.md`; v1 @`2dec8b6`)

- **Sorun:** DevOS'u rol adları ya da belge listesi olarak değil, çalışan bir çekirdek olarak planlamak.
- **Nasıl işler:**
  - **§5 sorumluluklar:**
    - INFORMATION: "Kaynak değişince eski karar/kanıt nasıl bayatlıyor? Compaction/kesinti sonrası hangi kritik bilgi geri kazanılıyor?"
    - WORK: "Önerilen iş, yetkili iş, yapılan iş, gerçekleşen hedef, destekleyen kanıt ve kabul farklıdır. Her iş için aynı töreni kurma."
    - ACTOR: alt ajan "koordinatöre itiraz edebilmeli".
    - ENVIRONMENT: "yazılı kural ile teknik enforcement'ı ayır".
  - **§6 delegasyon:**
    - Görev: "amacını, dar karar/etki kapsamını, kaynakları, exact hedefi, kontrol sürümünü, beklenen çıktıyı, değerlendirme ölçütünü ve bitiş koşulunu" taşır.
    - Sonuç: "iş/attempt kimliği, değişiklik, kanıt, gerçekten çalıştırılan testler, belirsizlik/çelişki, kalan iş ve yazıcı bırakmasını" taşır.
    - "Child çıktısı veri olarak doğrulansın". "Developer gerçek patch/kod/artefakt üretsin". "Salt-okur talimatı teknik izolasyon değildir."
    - v1: "Sessizlik yazıcı bırakma değildir." İki zincir: "`dosya var → bulunabilir → doğru sürüm okunur → model bağlamına girer → doğru uygulanır`" ve "`İş yapıldı ≠ hedef durum oluştu ≠ kanıt bunu destekliyor ≠ yetkili kabul gerçekleşti.`"
  - **§7 kapanış:**
    - "Planın kritik yolunda sahipsiz TBD bırakma." Koşullu yol şu beşliyi taşır: "**gözlenebilir tetikleyici, karar sahibi, izinli alternatif, sabit test ve başarısızlık yolu**".
    - İki tamamlayıcı, ayrı başlangıçlı eleştiri yapılır.
    - "STATE güncel yönü, PLAN tasarımı, EVIDENCE gözlemi taşır."
  - **Kabul kapsamı:**
    - K01–K12 (O0'da özet). Kural: "Bugün planlanan test, çalıştırılmış test değildir."
    - v1'in C01–C18 aileleri: amaç ve yetki geri kazanımı; child muhakemesi; araştırmanın karara etkisi; exact hedefli delegasyon; kırmızı verebilen test; bayat PASS; dolaylı yetki büyümesi; yazıcı ve iptal; yayın ile yükleme farkı; insansız kesinti dönüşü; gerçek işle uçtan uca ve diğerleri.
  - **§9 üç ufuk:** "şimdi planlanan ilk çalışan çekirdek; onun geliştireceği Development OS; onun gelecekte geliştireceği SOUL". Pilot "sınırlı işletime alma işi"dir; "kendi başarılı sonucunu önceden gerektiren READY döngüsü kurma".
- **Kanıt:** v1 gönderilmedi. `_02` planı yazıldı; kurulumu bilinmiyor.
- **Karar: AL** (doküman iskeleti ve kabul kapsamı olarak). Codex'e özgü kısımlar Claude karşılığıyla değişir; K ve C listeleri birleştirilir.
- **Uyarlama:** Kabule üç cloud satırı eklenir: VM süresi dolduktan sonra devam; sıkıştırmadan sonra devam kartıyla devam; hook'ların gerçekten yüklendiğinin denetimi.

**M16. SOUL faz 0 ilkeleri ve öncül hata sınıfları** (`repos/soul/README.md`; `evidence/CONTEXT-SYNTHESIS.md` §6; `repos/os-architect/README.md`)

- **Sorun:** Yeni DevOS öncüllerin hata sınıflarını tekrarlamamalı.
- **Nasıl işler (kaynak diyor):**
  - **NON_NEGOTIABLES:** "outcome-first, least privilege, independent verification, evidence-before-closure, explicit external state, governed capability acquisition, repair/adaptation, no hidden owner orchestration, fail-visible, scale-appropriate control, durable traceability".
  - **Vakalar:**
    - WP-001: "9/11 criterion PASS olsa da overall FAIL korunmuş". Neden: çelişen okuma sırası ve bayat `NEXT_SESSION` kopyası.
    - WP-007: "conformance PASS frame robustness değil".
  - **CONTEXT-SYNTHESIS §6, sekiz sınıf:**
    1. "question/request'in gerçek objective sanılması";
    2. "state/result korunurken purpose/reason/responsibility/next work'ün kaybolması";
    3. aynı hatayı paylaşan değerlendirici yakınsaması;
    4. "kontrolün formu ölçüp gerçek value'yu kaçırması";
    5. "dersin bulunmasına rağmen need-time'da invoke edilmemesi";
    6. "owner'ın gizli orchestrator/verifier haline gelmesi";
    7. "system-level framing/work-selection'ın sahipsiz kalması";
    8. "`bunu baştan kurar mıydık?` sorusunun kaybolması".
  - **os-architect'in beş hata türü:** depo, döngü, epistemik, amaç/çerçeve, ders→mekanizma (O12).
- **Karar: AL** (sert eleştiri turunun kontrol listesi olarak).
- **Uyarlama:** Her sınıf için dokümana "engelleyen mekanizma ve gösteren test" yazılır. O1'in gözlemine göre durma nedenleri bu sınıflara düşüyor: E19 döngüsü 1. ve 7. sınıf, başlatıcı zinciri 8. sınıf, Batu'nun taşıyıcılığı 6. sınıf.

**M17. Ortam kanıtı toplama kuralları** (BOOTSTRAP §7–§8; TASK-01; 002 §3–§5)

- **Sorun:** Ortam iddiaları gözleme dayanmalı.
- **Nasıl işler (kaynak diyor):**
  - "Distinguish reported observation, inference and unknown. Do not turn setup inspection into product design."
  - Stage 0B: "`pwd` and Git root identify the intended working copy"; "Do not change directories to conceal a misbound project".
  - "Web-tool success does not prove terminal-network success; read access does not prove write/push/PR access."
  - "Yeni oturum başlatılmadıysa session persistence NOT TESTED kalır."
  - "HOME tek başına etkin kullanıcı kimliğini, sürümler ECC uyumluluğunu kanıtlamaz."
- **Karar: AL.**
- **Uyarlama:**
  - SessionStart hook'u ortam parmak izini (pwd, kök, origin, dal, HEAD, kirli dosyalar, Claude Code sürümü, repo sayısı) STATE ile karşılaştırır; uyuşmazlıkta yazma durur.
  - Platform yetenekleri tablosu tutulur: yetenek → belge URL'si → bu ortamda gözlendi mi → tarih.

## 5. Ortam: kümenin Claude cloud hakkında söyledikleri

Hepsi belge okumasına dayanıyor, Batu'nun hesabında sınanmadı. Belgeler 24 Eylül'de okundu. O11 güncel hallerini doğrulamalı.

| Konu | Hüküm (kaynak diyor) | Kaynak |
|---|---|---|
| ECC = DevOS mu? | "KABUL EDİLMEDİ. Kurulu bileşen ile araştırmayı kullanabilen, işi devreden ve doğru sonucu doğrulayan geliştirme düzeni ayrı." | 002 §4 |
| ECC sürümü | Araştırma pini 2.2.1 (`8321021`), ekrandaki main 2.2.2 (`bf70150e`): "SÜRÜM FARKI DOĞRULANDI". ECC2'nin Rust operator/daemon parçaları ayrı çalışıyor ve alpha; zorunlu oldukları: "DESTEKLENMİYOR". | 002 §4, E1–E3 |
| Cloud keşif ve etkileşim için uygun mu? | "GENEL DIŞLAMA GERİ ÇEKİLDİ." D3'e göre follow-up ve alt ajan var. Help Center tavsiyesinden (iyi tanımlı işler cloud'a) "cloud'un keşif veya etkileşim için teknik olarak kullanılamadığı ... sonucu çıkmaz." | 002 §4; @`94dc93e` |
| Plugin | "Cloud'da plugin yok; manuel ECC kopyalama zorunlu" hükmü "YANLIŞ GENELLEME": "D1/D2 hesapta etkin pluginlerin cloud oturumunun kendi ortamına synced plugin olarak yüklendiğini açıklıyor. `/plugin` arayüzü hatası yükleme desteğinin yokluğuna kanıt değil." Ayrıca: "Repo `enabledPlugins` bildirimi de cloud'da otomatik marketplace kurulumu yapmıyor." | 002 §4; D2 = https://code.claude.com/docs/en/plugins-reference#plugins-synced-from-claudeai |
| Mac'ten ne taşınır? | "yalnız Mac'te kurulu araçlar ve kullanıcı ayarları cloud'a kendiliğinden taşınmaz." | @`94dc93e`; D1 |
| Setup script | "ilk setup sonrası dosya sistemi snapshot'ını yeni oturumların başlangıcı için kullanıyor; cache varken script atlanıyor. Script/ağ ayarı değişimi veya yaklaşık yedi günlük expiry cache'i yenileyebiliyor. Resume setup'ı yeniden çalıştırmıyor." Cache "çalışan süreçler veya sonraki çalışma ilerlemesinin ortak canlı deposu değildir." Setup süresi yaklaşık beş dakika. | 002 §4–§5; D1 = https://code.claude.com/docs/en/cloud-environments#configure-your-environment |
| Hook, skill ve ajan | "D1 repo skills/agents/commands/rules yüzeylerini, tek-repo oturumunda settings hooks/permissions ve MCP'yi destekliyor. Çok-repo oturumlarında repo settings/hooks yüklenmesi aynı değil." Ayrıca: "Repo'daki subagent tanımları yüklenebilir." | 002 §4; @`94dc93e` |
| Local MCP (chrome-devtools) | "AÇIK, AŞIRI ÇIKARIM GERİ ÇEKİLDİ." ECC kök `.mcp.json`'da chrome-devtools var (npx, latest); plugin manifestinde `mcpServers` boş. | 002 §4, E4 |
| Git ve kalıcılık | "D1 push'u oturumun mevcut çalışma dalıyla sınırlar"; "D3'te VM expiry sonrası conversation restore ile arka plan süreçlerinin restore edilmemesi ayrıdır. Göreve özgü geri kazanım açık." | 002 §4 |
| VM süresinin dolması | "İdle expiry sonrası VM yenilenebilir ve konuşma geri gelir; o anda çalışan alt ajan/shell işleri geri yüklenmez." "laptopun kapanması cloud işini yerel bir sürece bağımlı yapmaz." | 002 §5; D3 = https://code.claude.com/docs/en/claude-code-on-the-web |
| Kaynaklar | "4 vCPU, 16 GB RAM, 30 GB disk; bu sayılar hedef işin yeterlik veya performans testi değil." | 002 §5 |
| CLI'dan cloud | "`claude --cloud` yeni cloud oturumu oluşturur; uygun hesaptan mevcut oturuma CLI ile mesaj iletilebilir. Mesaj gönderme çağrısı yanıtı beklemez." | @`94dc93e` |
| Remote Control | "yerel oturuma uzaktan arayüz sağlamak, işi cloud'a taşımak değildir." | @`94dc93e`; https://code.claude.com/docs/en/remote-control |
| Projects | "bir proje konuşmasının cloud görevlerini başlatıp takip ettiği ürün yolu da belgelenmiş; kademeli beta erişimi var." Seçilmedi. | @`94dc93e`; https://code.claude.com/docs/en/claude-projects |
| Ön kontrol (gözlenen, 24 Eylül) | Node `v22.22.2`, npm `10.9.7`, Git `2.43.0`, Claude Code `2.1.281`, HOME `/root`, dal `claude/intelligent-bardeen-pknix8`. `/plugin list` çıktısı: "Plugins aren't available in this environment". | 002 §3 |
| Oturumlar arası mesaj (7 Eylül) | v2.1.224+ ListAgents/SendMessage (https://code.claude.com/docs/en/cross-session-messaging). Agent teams "deneysel ve varsayılan kapalı" (https://code.claude.com/docs/en/agent-teams). Headless'ta `--bare` abonelik girişini kullanmıyor (https://code.claude.com/docs/en/headless). | `reviews/2026-09-07-collaboration/REVIEW.md`; TRANSFER-PLAN §7 |
| AGENTS.md desteği | "doğrudan destek v2.1.277+ ... bazı oturumlarda destek yoktur"; "`AGENT.md` tekil adı otomatik giriş kabul edilmez." | SOURCE-REGISTER §4 (https://code.claude.com/docs/en/memory) |

**Codex ortamından alınmayacaklar.**
- macOS seatbelt profilleri, `/private/tmp` düzenleri ve `:minimal` temp istisnası (G0/D1);
- `codex exec`/`codex sandbox` bayrakları;
- `.codex/**` rol yapılandırması;
- Astra/Ultra model seçimi.
Bunlar Mac'e ve Codex'e bağlı. Batu'nun ortam kısıtıyla (SSH yok, Mac kapalı olabilir) çelişiyor.

**Ortam için açık kalanlar (002 §6 ve O1'in çıkarımı):**
1. Hangi ECC bileşeninin hangi DevOS sorumluluğunu karşıladığı. O5a–O5d bakıyor.
2. Bileşenlerin cloud'daki gerçek yükleme yolu. Synced plugin yolu canlı denenmedi.
3. VM süresi dolduktan sonra iş ve karar kayıtlarının geri kazanımı. Canlı denenmedi.
4. Oturum dalları ile kanonik dal arasındaki bütünleştirme kuralı. Kümede yok (M3).

## 6. Dersler (ne oldu → kök neden → nasıl önlenir)

- **L1. Hazırlık altyapısı işin yerine geçti.**
  - *Ne oldu:* G0→D1→G1'de gerçek model koşusu 0/8 kaldı.
  - *Kök neden:* Farklı güvenceler aynı giriş kapısına bağlandı; bunun "**bu ilk iş için neden gerekli olduğu** ... yeterince açık değil" (method review §5).
  - *Önleme:* Güvence etkiye göre ayrılır. İlk iş yararlı bir DevOS işi olur. BOOTSTRAP: "The process must not grow indefinitely merely to prepare for its first meaningful work."
- **L2. Döngü son kusuru kovaladı** (E19, KR1, 108/106).
  - *Önleme:* "Son mesajdaki küçük kusur otomatik sıradaki iş olmaz" (METHOD v2 §3) ve WP-021'in "otomatik repair-shaped work olmamalı" kuralı.
- **L3. Ürün amacı girişte zayıftı** (direction review §4; COORD-01).
  - *Önleme:* STATE'e kalıcı amaç paragrafı konur. COORD-02 bunu iki dosya değiştirerek yaptı.
- **L4. Batu mesaj taşıyıcıya dönüştü.**
  - *Ne oldu:* 13 brief'in 11'ini o taşıdı. G1'deki tek düzeltme sayacı yüzünden "kullanıcı yeniden teknik relay olmak zorunda kaldı".
  - *Önleme:* Kalıcı manda (M6). G1 review'dan: "**sınırlı mühendislik serbestliği ile yetki genişlemesini ayrı sınırlama**".
- **L5. Yön aynı gün savruldu** (DEVOS-002'de dört saatte on kayıt).
  - *Kök neden:* Asistanın sonuçları kullanıcı kısıtı gelmeden "Resolved" yazıldı. Resolved B bir kullanım tavsiyesini teknik sınıra çevirdi.
  - *Önleme:* Varsayım kuralı (M13).
- **L6. Konudan sapıldı** (ECC hook ayrıntısı, ardından Mac teşhisi).
  - *Önleme:* Her alt dalda "hangi kararı açıyor?" diye sorulur. "Sırf bir ekranda sonraki düğme var diye yeni tıklama zinciri başlatılmaz."
- **L7. Kayıt hacmi ilerleme sanıldı** (2.238 dosya, 4.508 katkı; P2 başlamadı).
  - *Önleme:* "Kayıt sayısını ilerleme hedefi yapma" (R-005).
  - *Çıkarım:* EXP-007'nin okuma turu da aynı riski taşıyor. Notların değeri, yapı kararına ne kattıklarıyla ölçülür.
- **L8. Kesik araç çıktısı yüzünden yanlış tamlık beyanı** (F08).
  - *Önleme:* Satır sayısı kontrolü. S1A: "Kesilmiş okumayı tam, bulunamayan kaynağı yok sayma".
- **L9. Sohbet aktarımı 2 bayt değiştirdi** (COORD-02).
  - *Önleme:* Özgün dosya ya da diff kullanılır, blob karşılaştırılır, uzak içerik geri okunur.
- **L10. Yanlış çalışma kopyası.**
  - *Önleme:* Stage 0B kontrolü; cloud karşılığı M17'de.
- **L11. Değerlendirici bağımsız değildi.** Method review'un kendi sözü: "bağımsız dış hakem değil".
  - *Önleme:* Bağımsızlığın sınırı yazılır. Çeşitlilik gerekiyorsa farklı başlangıç, araç kısıtı ve sabit ölçüt kullanılır.
- **L12. Taze oturum bellekten bağımsız değildi** (COORD-03).
  - *Önleme:* İddia sınırlanır; Claude'un otomatik belleği ayrıca denetlenir.
- **L13. READY dar tanımlanmıştı.** Batu: "The user correctly challenged the earlier interpretation of READY".
  - *Kök neden:* READY görevin dar tanımına göre verildi, kullanıcının beklediği işlevle karşılaştırılmadı.
  - *Önleme:* Her READY'ye "neyi kapsamıyor" listesi (M6).
- **L14. Hazırlanan mesajların çoğu gönderilmedi.** G1-R1, DESIGN-01, CONSTRUCTION-PLAN v1, `KERNEL-...-v1` ve TASK-01.
  - *Kök neden (çıkarım):* Her adım insan benimsemesi bekleyen bir brief'ti; yön değişince hazırlık boşa gitti.
  - *Önleme:* Manda altındaki ajan planı kendisi uygular; brief yalnız owner kararı için yazılır.
  - İyi işleyen yan: "hazırlandı ≠ gönderildi ≠ uygulandı" ayrımı sayesinde hiçbir iş koşmuş gibi yazılmadı.
- **L15. Repo değişimi sürekliliği kopardı** (`soul-development-os` → `_02` → os3). `_02`'nin nedeni: "Eski Codex çalışma düzenini toparlayamadığı için".
  - *Kök neden (çıkarım):* Düzen, owner'ın okuyup toparlayabileceği tek bir görünür durum üretmiyordu.
  - *Önleme:* Tek kanonik repo. STATE'te Batu'nun okuyabileceği sade bir özet. Eski denemeler kaynak olarak bağlanır ("clean start without historical amnesia").

## 7. Doğrudan yeniden kullanılabilir parçalar

Yollar `research/soul-context/current/` altına göredir; `development-os/` ayrıca belirtilmiştir.

| Parça | Yol | Karar | Gerekçe |
|---|---|---|---|
| Aday `AGENTS.md`, `STATE.md` ve iş kaydı metinleri | `reviews/2026-09-06-stage-1a/CODEX-RESPONSE.md`, 14–377. satırlar | UYARLAYARAK AL (M1) | Olgun ve tam metin. Giriş CLAUDE.md olur; amaç paragrafı eklenir. |
| Kayıtsız kesintide devralma cümlesi | `reviews/2026-09-06-stage-1a/REVIEW.md`; `briefs/CODEX-STAGE-2-G0-EXPERIMENT.md` | AL (M3) | Cloud'da kayıtsız kesinti olağan durum. |
| Amaç paragrafı ve benimse/reddet/koşullu bırak tablosu | `reviews/2026-09-07-coord-01/CODEX-RESPONSE.md` | AL (M1, M5) | Çalıştığı raporlanan COORD zincirinden. |
| Taze oturum testi: önceden sabit ölçütler (a)–(e), salt okunur mesaj ve "beklenen cevabı mesaja koyma" kuralı | `reviews/2026-09-07-coord-02/IDENTITY-RESOLUTION.md` §5–§6; sonucu `FRESH-SESSION-REVIEW.md`; DEVOS-001'in ayrı koşulları (a)–(e): REVIEW@`85076c2` | AL (M4, M5) | Bellek karıştırıcısı ayrıca denetlenir. |
| Manda ve owner karar listesi | `briefs/CODEX-COORDINATION-HANDOFF.md` | AL (M6) | Batu'nun rolüyle birebir uyumlu. |
| Rota ve protokol tasarım özellikleri; 12 konu, 9 senaryo, 11 ölçüt | `briefs/CODEX-DEVOS-AGENT-CONTROL.md` | UYARLAYARAK AL (M7) | Kural çok iyi; Claude'da yükleme yolu O11'de netleşir. |
| Planlama paketi, delegasyon sözleşmesi, K01–K12, C01–C18, üç ufuk | `briefs/CODEX-DEVOS-CONSTRUCTION-PLAN.md`; v1 @`2dec8b6` | AL (M15) | DevOS dokümanının iskeleti ve kabul kapsamı. |
| RPD01'in 12 maddesi, devam kartı, F01–F03, RP1–RP6, tavanlar ve dosya yerleşimi | `reviews/2026-09-08-devos02-plan/REVIEW.md` §4–§9 | UYARLAYARAK AL (M8) | Batu'nun "gizli eksik-bulucu olmama" isteğinin en somut karşılığı. |
| İlk pilotun risk tablosu ve beş beklenti | `COORDINATION-TRANSFER-PLAN.md` §4–§5 | AL | Pilotun neyi kanıtlamadığını baştan yazma kalıbı. |
| Varsayım denetimi kuralı ve hüküm tablosu | `development-os/attempts/002/README.md` §4; @`606506e` | AL (M13) | Yön savrulmasına karşı. |
| Denetçi probu ve parser regresyonu | `development-os/attempts/001/evidence/W02-D01/`; `reviews/2026-09-07-g1/PARSER-REGRESSION.py` | AL, kalıp olarak (M10) | Hook'ları sınamanın somut biçimi. |
| Köprünün bitiş koşulları (1–10) ve açıkça reddedilenler | `DEVELOPMENT-OS-BOOTSTRAP.md` §6, §10 | AL | Kabul ölçütü ve eleştiri listesi. |
| Sekiz hata sınıfı; NON_NEGOTIABLES ve SUCCESS_CRITERIA | `../evidence/CONTEXT-SYNTHESIS.md` §6; `../repos/soul/README.md` | AL (M16) | Sert eleştiri turunun kontrol listesi. |
| KEEL hook, rol kafesi, doğrulayıcı ve karne | `../repos/keel/README.md` (asıl kod O3'te) | UYARLAYARAK AL (M14) | Proje dosyası olarak cloud'da yüklenir. |
| OPENING-VISION: yedi soru, ayrımlar, döngü, öğrenme yolu | `reviews/2026-09-06-direction/OPENING-VISION-SOURCE.md` | UYARLAYARAK AL | SOUL için yazılmış. DevOS'a mercek olarak uygulanır, ürün mimarisi değildir. |
| N00–N09 ihtiyaç ağı | CC-PREP WORK@`1be22a3` | UYARLAYARAK AL (M12) | Dokümanın ihtiyaç ve test tablosu. |
| D10/D11 ayrımı ve durma kuralı | `../exploratory/` | AL (M13) | İş seçimi ile yaşam döngüsünü ayırır. Diğer boyut ve holdout içeriği SOUL araştırmasıdır, DevOS için ALMA. |
| Repo üzerinden mesaj kanalı | `development-os/attempts/001/EXCHANGE.md` | ALMA (ana döngü olarak) (M9) | Oturum başlatmıyor, dar eleştiri döngüsü üretti. Zarf alanları alınır. |
| Codex sandbox profilleri, özel başlatıcı ve `/private/tmp` düzeni | `briefs/CODEX-G0-D1-*`, `CODEX-G1-*` | ALMA | Mac'e ve Codex'e bağlı; L1'in kaynağı. |
| RPD Python prototipi | `_02` grant'ı; Research'te yalnız değerlendirmesi var | ALMA | "Kodu bu haliyle yetki/hazır olma/kabul denetleyicisi yapma". |

## 8. İtirazlar ve çelişkiler (STANDART kural 6)

1. **Plugin iddiası: kaynak içinde çözülmüş, ama canlı sınanmamış.**
   - **Çelişki:** 002'nin 09:11 kaydı (@`606506e`'de korunuyor) şunu yazmıştı: "**Correction from official Claude Code Desktop documentation:** Plugins are not available in Remote sessions." Bu, brief'teki "iki yol var: hesap plugin'i ya da proje dosyası" satırıyla çelişiyor.
   - **Çözüm kaynakta var:** Aynı gün @`94dc93e`'de Research Desktop reference'ın "Install plugins" bölümünü yeniden okudu ve şunu yazdı: "Plugin tarayıcısının cloud'da olmaması ile hesap üzerinden synced plugin yüklemesi farklıdır." Güncel 002, eski hükmü "YANLIŞ GENELLEME" olarak işaretliyor. Brief'in düzeltilmiş satırı Research'ün son okumasıyla uyumlu. O10'un andığı P1-01 çelişkisi de buna göre kapanmış görünüyor (çıkarım).
   - **Açık kalan (bilinmiyor):**
     - Hiçbir cloud oturumunda ECC'nin synced plugin olarak yüklendiği gözlenmedi.
     - Batu'nun Desktop'taki local MCP izin penceresinde neye bastığı teyitli değil.
   - **Karar verirken (çıkarım):** 002 §5 D2'ye göre "sonraki sync güncellemeleri nedeniyle hesapta kurulu sürümün sabit kaldığı varsayılmaz". 606506e'nin sürdürülebilirlik kuralı ise şu: "Pin ECC to an explicit reviewed release/commit; never install `latest` silently". Sürüm sabitlemek gerekiyorsa proje dosyası yolu daha denetlenebilir; hesap plugin'i sync ile kayabilir. O11 ve O5'e iletilecek nokta budur.
2. **BOOTSTRAP'taki "minimum" ifadesi alınmamalı.**
   - Stage 1 "**minimum sufficient working bootstrap**", S1 "küçük bir Development OS", OPENING-VISION "minimum yeterli task-specific çalışma sistemi" diyor.
   - Batu bu dili açıkça reddetti (§1.4). Research de "'Minimum yeterli scaffolding' başlangıç hedefi geri çekildi" diye kaydetti.
   - DevOS dokümanı "minimum"u ölçüt yapmamalı. Yerine şu ölçü konmalı: her yapı bir ihtiyaca ve teste bağlanır; ihtiyaç incelenmeden kırpılmaz ve büyütülmez.
3. **Not boyutu.** Brief kural 7 not için 45 KB diyor. STANDART kural 8 ve koordinatörün zorunlu eki 90 KB'a izin veriyor. Sonrakine uydum.
4. **Kendi ilk taslağımın hatası.** İlk taslakta "kümede raporlanan tek çalışan zincir COORD-01→03" diye yazmıştım. STATE@`de51ef6` AGENT-CONTROL'ün READY sonucunu kaydediyor. Bu yüzden düzelttim: çalıştığı raporlanan iki zincir var.
   - İkinci düzeltme: "DESIGN-01'in gönderilip gönderilmediği bilinmiyor" yazmıştım. STATE@`de51ef6`: "DESIGN-01 remains prepared but unsent/held".
5. **"Batu teknik koordinatör değildir" öncülü.**
   - Kaynaklarla uyumlu (§1.2, 1. satır).
   - Ama kaynaklar şunu da gösteriyor: işin kritik düzeltmelerini Batu yaptı. Bunlar AGENT-CONTROL'deki READY itirazı, 23 Eylül'deki sert düzeltme, 24 Eylül'deki durdurma ve "konudan saptın" uyarısıdır. Yani fiilen gizli denetçi olarak çalıştı (çıkarım; CONTEXT-SYNTHESIS'in 6. hata sınıfı).
   - DevOS tasarımı bu yükü Batu'dan almak için kendi yön denetimini içermeli: konudan sapma ve kapsam daralması için mekanik tetikler. Yalnız "Batu'ya soru sorma" kuralı yetmez.
6. **O10'daki alt ajan derinliği notu.**
   - O10, EXP-006'daki bir belgenin iç içe alt ajan çağrısını anlattığını kaydediyor.
   - Bu kümede derinlikle ilgili iki şey var: "varsayılan fiziksel derinlik bir" (`_02` PLAN tavanı) ve "Mantıksal recursion, fiziksel agent recursion değildir".
   - Kümeden bu konuda bir çelişki çıkmıyor. EXP-007 STATE bu ortam için `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` diyor. RPD'nin mantıksal özyinelemesi her iki durumda da çalışır.
7. **Tarihsel sürümlerin ağırlığı.** Bu notun bazı hükümleri güncel ağaçta olmayan sürümlere dayanıyor: AGENT-CONTROL sonucu, `_02`'nin nedeni ve RPD gönderimi. Güncel `research/soul-context/STATE.md` DEVOS-001'e yönlendiriyor; `_02` devrinin tam kaydı için yalnız `cee38caa` bağlantısını veriyor. Bu sürümler Git'te korunuyor ve kaynak kendi zincirini bağlantılarla kuruyor: güncel STATE → `cee38caa`; `4ad34d7` → `de51ef6`. Yine de yapı kararı bu sürümlere dayanacaksa, ana oturum gösterilen commit'lerden kendisi geri okumalı.

