# O0 — Ana oturumun kendi okumaları (DevOS için)

**Okuyan:** ana oturum (Claude), 27 Eylül 2026. Alt ajan notu değildir. Aşağıdaki dosyaları baştan sona kendim okudum:
- `research/soul-context/current/DEVELOPMENT-OS-BOOTSTRAP.md`
- `research/soul-context/current/briefs/CODEX-DEVOS-CONSTRUCTION-PLAN.md`
- `research/soul-context/STATE.md`
- `research/soul-context/current/claude-code-devos-preparation/OWNER-CONTEXT.md`, `WORK.md`, `CLAUDE-TASK-01.md`
- `development-os/INDEX.md`, `development-os/attempts/002/README.md`
- `development-os/attempts/001/BRIEF.md`, `METHOD.md`, `REVIEW.md`
- `/home/user/soul-development-os3_claudecode/CLAUDE.md`, `STATE.md`, `OWNER.md`

## 1. En önemli bulgu: aynı hata tekrar ediyor

Batu, DevOS için istediklerini önceki denemelere de yazdı; ben bunları okumadan sordum.
- **Önceki Claude denemesi** (`soul-development-os3_claudecode`, 23–24 Eylül) şunlarla açıldı: "Tüm sorumluluk sende olacak. Bana yalnız SOUL'un ne olması, nasıl bir şey olması gerektiği konusunda soru sorabilirsin." (OWNER O-01)
- Aynı denemede: "Kullanım limitinin tamamını sadece bu konuya ayırabilirsin. Sınır yok." (O-20). Ben U012'de limit sorusunu yeniden sordum.
- O deneme, studies'in tamamını (893 dosya, 74 okuma birimi) alt ajanlarla okudu. Sonra okuma, ChatGPT ile yazışma (C-001…C-005) ve "E19" soru bankası sınamalarında kaldı. DevOS kurulmadı. Batu 24 Eylül'de "Tüm çalışmaları durdur. Hepsini." dedi (O-28).
- DEVOS-001'in dersi (`development-os/attempts/001/REVIEW.md`): iş, "bütün çalışma yapısına ilişkin korpus okumasının ve ortak karar hazırlığının" yerine yerel karşılıklı eleştiriye daraldı.
- Batu'nun ChatGPT'ye yazdığı ve aktarılan söz (OWNER.md, son bölüm): "Bütün repoyu gözden geçireceksiniz, her turda development os'u kuracak yapıya katkı sağlayacak tüm fikir ve örnek yapıları sonradan okuyabileceğiniz bir şekilde kayıt altına alacaksınız. Tüm okuma ve kayıt altına alma bitince de bu kayıtlardan nasıl bir çalışma yapısı çıkaracağınıza karar vereceksiniz. 4 bacak diye konuştuk, iş ne kim yapacak nasıl takip edilecek hangi ortamda yapılacak hepsinin cevabı var"; "Az laf çok icraat".

**Sonuç:** Bu turun işi sınırlı bir okuma ve kayıt turu, ardından yapı kararı ve somut dokümandır. Okuma, yeni bir sonsuz hazırlık olmayacak. CODEX-DEVOS-CONSTRUCTION-PLAN §1'in uyarısı: "Önüne yeni bir sonsuz hazırlık sistemi koyma."

## 2. Depo topolojisi ve roller (BOOTSTRAP §1, §6; 002 README)

- `agentic-os-search`: SOUL Research (Foundation, studies, bağlam).
- Development OS reposu: SOUL'u araştıran, tasarlayan, kuran, doğrulayan ve geliştiren çalışma sistemi. Denemeler:
  - `soul-development-os` (Codex);
  - `soul-development-os_02` (Codex);
  - `soul-development-os3_claudecode` (Claude, DEVOS-001; Batu: "senin repon").
- DEVOS-002: "Kullanıcı Claude için yeni repo açacağını bildirdi; adı/adresi verilmedi."
- `soul-production`: SOUL ürün reposu.
- İnsan sahip (Batu): vizyon, değer, kapsam ve belirlenmiş onaylar. "should not remain the technical coordinator or verifier" (BOOTSTRAP §6).
- Batu'da kalan kararlar (CONSTRUCTION-PLAN §9):
  - temel ürün amacı ve maddi kapsam, risk ya da bütçe değişimi;
  - yüksek etkili ya da geri dönüşsüz dış işlemler;
  - SOUL ürününün yazımı, sürümü ve kabulü;
  - yeni sağlayıcıya özel veri;
  - kimlik bilgisi, hesap, güvenlik ve kalıcı izinler;
  - ücretli altyapı;
  - kabul ölçütünün ya da verilen yetkinin genişletilmesi.

  Aynı yerde: "Normal teknik sıralama ve doğrulama işini owner kararı diye kullanıcıya yığma."

## 3. DevOS'tan beklenen aktör (BOOTSTRAP §4)

Programcı değil; şunları yapabilen bir geliştirme aktörü:
- amacı ve durumu geri kazanır;
- kullanıcının amacını önerilen yöntemden ayırır;
- çerçeveye ve mevcut yapıya kanıtla itiraz eder;
- karar taşıyan varsayımları bulur;
- ne zaman araştırma gerektiğine karar verir;
- araştırmayı kabul edilmiş mimari saymadan kullanır;
- yetkisi içinde teknik karar verir;
- kendi işini kendisi onaylamaz;
- kanıtı, kökeni ve tazeliği korur;
- doğru sonraki işi seçer;
- gizli insan koordinasyonu olmadan devam eder;
- kendi çalışma sistemini yönetilen koşullarda geliştirir.

Çerçeve: DevOS = Aktörler + Bilgi + İş + Ortam + bunların ilişkileri. Uyarı: bunlar dört klasör, servis ya da ajan değildir.

## 4. Sabit gereksinim listeleri

### 4.1 Batu'nun altyapı gereksinimleri (OWNER O-01, "asgari, tamamı değil")
1. **Zorunluluk:** Protokollerin gerçekten yüklenmesi modelin hatırlamasına bırakılmaz. Hangi kuralın talimat olarak kalacağı, hangisinin ortam tarafından zorlanacağı gerekçelendirilir.
2. **Görünürlük:** Her turda hangi protokollerin yüklendiği ve hangi dosyaların değiştiği görülür. Kontroller sessizce atlanamaz.
3. **Süreklilik:** Yeni oturum amacı, kuralları, durumu ve kararları yalnız repodan geri kazanır. Bağlam sıkıştırması fark edilir.
4. **Kayıt düzeni:** Karar, öneri, varsayım ve doğrulanmış bilgi karışmaz. Tek asıl kopya olur. Eskiyen kayıt fark edilir.
5. **Kural değişikliği:** O-20'den beri Claude'un sorumluluğundadır ve kayda geçer.
6. **Doğrulama:** Kuralları bilerek çiğneyen denemelerle gösterilir. Neyin doğrulandığı yazılır. Platform güncellenince yeniden sınanabilir.
7. **Güvenli çalışma:** Bozulan denetim işi kilitlemez, ama sessizce de kapanmaz; görünür olur.
8. **Büyüme:** Alt ajanlar aynı disiplini ve kayıt düzenini taşır.
9. **Gerçek ortam bilgisi:** Güncel belgelerden ve bu ortamda denenerek doğrulanır.

Ek ilkeler:
- O-16: Örneğin altında değil, üstünde kur. Dar kurma. "Sonra genişletiriz" ancak tetikleyicisiyle yazılır.
- O-17: Önce kendi çalışma düzenine uygula.
- O-18: Repo çöplüğe dönmesin; düzen repoyla birlikte büyüsün; execution bias'a düşme.
- O-20: Kurallar Claude'undur. Cevabı kaynakta olan soru sorulmaz.
- O-21: Foundation'daki dört bacak bakışı değiştirir. "Nasıl" studies'te, somut örnekler explorations'tadır.

### 4.2 Codex çekirdeği kabul kapsamı K01–K12 (CONSTRUCTION-PLAN §8; Claude'a uyarlanacak)
- **K01:** Yeni repo, gerçek yetki ve güncel iş doğru geri kazanılır.
- **K02:** Maddi iş yapan alt ajan doğru kontrolü ve protokolleri gerçekten bulup kullanır; eksik ya da yanlış sürümlü kontrol işi durdurur.
- **K03:** Araştırma tasarım kararını gerçekten etkiler.
- **K04:** Alt ajan kusurlu bir öncülü fark eder ve sorgular.
- **K05:** Görev, sonuç ve birleştirme kesin hedef ve deneme kimliği üzerinden çalışır; bozuk sonuç sahte başarıya dönmez.
- **K06:** Geliştirici gerçek değişiklik üretir. Ayrı başlatılmış değerlendirme yapılır. Atlanan ya da koşmayan test yeşil sayılmaz.
- **K07:** Hedef, kontrol ya da ölçüt değişince eski PASS yeniden kullanılmaz. Aday kendi ölçütünü gevşetemez.
- **K08:** Sınır dışı etki durdurulur. Talimat biçimli kaynak ya da bellek içeriği yetki kazanamaz.
- **K09:** Tek yazıcı, devir, zaman aşımı, kısmi etki ve yeniden deneme güvenlidir.
- **K10:** Eksik kaynak ya da kullanım sınırı görünürdür; güvenli checkpoint vardır.
- **K11:** Yerel çıktı, commit, push, uzak içerik ve kontrolün fiilen yüklenmesi ayrı gösterilir. Kesintiden sonra taze bağlam işi insan özeti olmadan geri kazanır.
- **K12:** Yararlı bir pilot şu zinciri uçtan uca işletir: kaynak → karar → üretim → test ve ayrı değerlendirme → birleştirme → geri okuma → kalıcı devam.

### 4.3 Köprünün bitiş koşulları (BOOTSTRAP §6; kendi kendine sürme kanıtı)
Taze oturum şunları geri kazanıp kullanabilmeli:
1. amaç;
2. durum;
3. güncel ve sonraki iş ile iş seçme disiplini;
4. yetki sınırı;
5. araştırma ihtiyacı;
6. tasarım, yapım, doğrulama ve kabul ayrımı;
7. kanıta dayalı tamamlanma;
8. kesin durum ve devir;
9. kesintiden dönüş;
10. kendi kabul kurallarını sessizce değiştirmeden yönetilen revizyon.

"File existence is insufficient."

## 5. Ortam gerçekleri (DEVOS-002 §4–§5; belgeli, bu hesapta bütünü sınanmamış)
- Hesapta etkin plugin'ler bulut oturumuna "synced plugin" olarak yüklenir. Repo `enabledPlugins` bildirimi bulutta marketplace kurmaz.
- Tek repolu oturumda repo skills, agents, commands, rules, settings hook'ları, izinler ve MCP yüklenir. Çok repolu oturumda repo settings ve hook yüklemesi aynı değildir.
- Setup script ilk kurulumdan sonra önbelleğe alınır (yaklaşık 7 gün). Resume setup'ı yeniden çalıştırmaz. SessionStart ayrıdır.
- VM süresi dolunca konuşma geri gelir; çalışan alt ajan ve shell işleri geri gelmez.
- Kaynak sınırı yaklaşık 4 vCPU, 16 GB RAM ve 30 GB disk.
- SSH yok. Mac kapalı olabilir; iş Mac'e bağlanmamalı.
- ECC önerisi: ECC, SOUL'un değil DevOS'un tabanı olabilir. Ama "ECC kurmak tek başına Development OS'u kurmaktır" kabul edilmedi. ECC2 (Rust operator) ayrıdır ve alpha aşamasındadır.

## 6. Önceki Claude denemesinin iyi yanları (alınacak)
`soul-development-os3_claudecode/CLAUDE.md`:
- kısa giriş dosyası;
- OWNER (Batu'nun birebir sözleri) ile PLAN ("[Claude seçimi]" etiketi) ayrımı;
- oturum başı sırası: STATE → PLAN → JOURNAL → OWNER;
- `git fetch` ve uzak geri okuma;
- araştırma reposu dışarıda, `register_repo_root` çağrılmadan okunur;
- soru kapısı (O-20);
- "Okudum" yalnız baştan sona okunan için söylenir;
- "Örneğin üstünde kur";
- bilgi türleri etiketi.

Sorunu kurallar değildi. Sorun, işin kurulum yerine okuma ve yazışmada kalmasıydı. Ayrıca oturumun dalı main'den başlıyor ve kalıcılık için main'e yazmak gerekiyordu; önceki deneme bunu çözmüştü (O-08).
