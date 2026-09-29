# Araştırma / kurulum ayrımı — depo bakım çalışması

**Kimlik:** REPO-SEPARATION-20260929  
**Durum:** DEVAM EDİYOR — başlangıç ve aşamalı bakım planı hazır; depo genelinde düzeltme ve arşivleme tamamlanmadı.  
**Tarih:** 29 Eylül 2026. **Yazar:** ChatGPT, Batu'nun açık yetkisiyle.  
**Kaynak:** [Görev belgesinin değiştirilmemiş kopyası](maintenance/2026-09-29-research-installation-separation/REQUEST.md). Son kullanıcı yönü: “iş büyük geldiyse parçalara bölüp planla, sonra turlarla eriterek bitirmeyi dene.”

Bu dosya yalnız `agentic-os-search` deposunu güncelleme çalışmasının planı, ilerleme kaydı ve devir noktasıdır. Yeni bir DevOS kurulum planı, SOUL iş listesi, mimari veya agent-control dosyası değildir.

## 1. Amaç ve yetki

Depoyu ilk kez okuyan Claude Code kurucusu, araştırma kütüphanesini tarihsel DevOS kurulum kayıtlarından ayırabilmeli; eski Codex/P5/DEVOS-001/002 yönlerini güncel kurulum işi sanmamalıdır. Araştırma içeriği, özgün kararların tarihçesi ve kanıt sınırları korunur.

DevOS'un geçerli kurulum yönü **Claude Code cloud**; kurulum planının tek geçerli evi [batuhanozgun/devos — plan/](https://github.com/batuhanozgun/devos/tree/main/plan), görevde belirtilen sürümü **2.1**'dir. Planın kopyası bu depoya konulmaz. Yeni ürün deposu `batuhanozgun/soul-system`; eski `batuhanozgun/soul` tarihsel denemedir ve değiştirilmez.

Yazma yetkisi yalnız `batuhanozgun/agentic-os-search` içindedir. `AGENT.md` ve `agent/**` değiştirilmez. Başka depolara, Supabase projelerine, hesaplara veya erişim ayarlarına yazılmaz. Kurulum yapılmaz. Bu deponun araştırma paketlerindeki kendi güncel durumları korunur; onlar Claude Code için kurulum talimatı değildir.

`batuhanozgun-devos` hesabının teknik yazma imkânı, bu depoya yazma yetkisi değildir. Bu hesapla ilişkilendirilmiş commit görülürse onu düzeltmeden önce Batu'ya bildirilir. Yetki/kimlik kontrolü her yayın öncesi yeni değişimlere karşı yenilenir.

Görev kaynağındaki tarihli platform karşılaştırmaları ve hesap oluşturma beyanları kullanıcıdan alınan bağlamdır; bu bakım çalışması onları yeni bir teknik yeterlik veya fiyat doğrulaması olarak onaylamaz. Verilmiş platform kararı yeniden açılmaz.

## 2. Ayrımın tasarımı

**Tercih: yerinde statü ve yönlendirme ayrımı; toplu dosya taşıma yok.**

- Foundation, studies, concepts ve kavramsal explorations kendi yerlerinde kalır. Bunların araştırma anlamı değiştirilmez.
- `development-os/**` ve EXP-006'nın eski kurulum/planlama yüzeyleri tarihsel statüyle bulunabilir kalır. Kaynak kullanıcı mesajları ve özgün araştırma gövdeleri geriye dönük yeniden yazılmaz.
- Kök ve alan girişleri araştırma, tarihsel kurulum, kontrol ve yayın arşivlerini açıkça ayırır. Doğrudan eski bir devir dosyasını açan okuyucunun da statüyü görebilmesi ayrıca denetlenir; yalnız kök uyarısı son kabul için yeterli değildir.
- Yeni erişilebilir rapor/paket kopyaları için `archives/devos-pre-claude-2026-09-29/` altında bir kaynak arşivi hazırlanması planlanır. Özgün gövdeler değişmez; statü, gerçek erişim ve kimlik bilgisi yan kayıtlarda taşınır. Bu yol henüz oluşturulmuş arşiv anlamına gelmez.
- [MOVES.md](MOVES.md) gerçekleşen taşımaların kaydıdır. Şu anda taşıma yoktur. Arşive ek kopya koymak taşınma sayılmaz; kopya/provenance ayrıca gösterilir. Toplu taşıma gerekirse uygulamadan önce Batu'ya kısa plan sunulur.

## 3. Beş iş paketi ve kapanış koşulları

Bir paket gerektiğinde birkaç tur sürebilir; tur sonunda kanıtlanmış sonuç ve tek devam noktası kaydedilir. Paket numarası otomatik tur sayısı değildir.

| Paket | Yapılacak | Kapanış koşulu | Durum |
|---|---|---|---|
| **A1 — Başlangıç ve kalıcı plan** | Görevi tam oku; başlangıç commit'ini, yazar sınırını ve dış plan adres/sürümünü kontrol et; bu bakım planını, özgün isteği, başlangıç kimliklerini ve kök yönlendirmeyi kaydet | Başlangıç kimlikleri ve kapsam açık; ilk değişiklik kümesi geri okunmuş; araştırma/agent-control gövdeleri değişmemiş | Bu değişiklik kümesinin kapsamı; uzak yayın ve geri okuma sonucu commit üzerinden ayrıca doğrulanır |
| **A2 — Karar ve güncel yönler** | D030; EXP-006 STATE/HANDOFF/INDEX/WORK/DECISIONS; development-os giriş ve deneme devirleri; soul-context yönleri; ilgili kök/alan bağlantıları | Eski kurulum yolu bu girişlerden güncel olarak devralınamıyor; D027/D029'un ortam kararı tarihsel olarak korunuyor; dış plan tek kurulum otoritesi | SIRADAKİ |
| **A3 — Rapor ve paket arşivi** | Yedi kaynak ailesini ara, gerçek gövdeleri kimlikleriyle doğrula, erişilenleri özgün biçimde arşivle; her birine istenen statü notu ve erişim kaydı koy | Her kaynak için doğrulanmış gövde veya açık erişim engeli; farklı P5 paketleri karıştırılmıyor; erişilemeyen dosya yeniden üretilmiyor | BEKLİYOR |
| **A4 — Depo geneli tarama ve ek düzeltmeler** | Bütün izlenen dosya yollarını envanterle; metinleri ve gerekli belge/ZIP içlerini tara; doğrudan girişler, bağlantılar, eski soul/current yönleri ve talimat gibi okunabilecek proje kayıtlarını değerlendir | Her riskli eşleşmenin düzeltme veya gerekçeli koruma kaydı; taranmayan/okunamayan kapsam açık; araştırma anlamı değişmemiş | BEKLİYOR |
| **A5 — Son karşılaştırma ve teslim** | Başlangıçtan son commit'e fark; silme/taşıma/gövde kimliği denetimi; bağlantılar; yeni okuyucu yürüyüşü; tam değişiklik ve gerekçe listesi | Gerçek değişiklik listesi ve commit'ler; kaynak erişim açıkları; kalan tarihsel sözcüklerin gerekçesi; kapsamı aşmayan tamamlama hükmü | BEKLİYOR |

## 4. A2 için bilinen hedefler

Bu liste tüm depo taramasının yerine geçmez. İlgili dosyalar değiştirilmeden önce güncel tam içerikleri ve bağlantılı durum yüzeyleri okunur.

- `explorations/EXP-006-development-os-calisma-duzeni/DECISIONS.md`: D030; eski karar metinleri korunarak güncel/tarihsel ayrımı.
- Aynı alanın `STATE.md`, `HANDOFF.md`, `INDEX.md`, `WORK.md`; P4/P5 teslim/devir kayıtları ve `work/p5/CODEX_START.md` gibi tek başına okunabilen eski uygulama başlangıçları.
- `development-os/INDEX.md`, `attempts/001/` ve `attempts/002/` içindeki durum/yönlendirme yüzeyleri.
- `research/soul-context/**` içindeki eski `soul` otoritesi, güncel DevOS/target bağlantıları; ilgili `research/INDEX.md`, `explorations/INDEX.md` ve katalog yönlendirmeleri.

Eski `soul` ve diğer deneme depolarına ilişkin tarihsel gözlem değişmez. Yeni ürün adresi mevcut kayıtların tarihli statü notlarında veya güncel yönlendirmesinde belirtilir.

## 5. A3 kaynak matrisi

| Kaynak | Verilecek statü | Bu turun gerçek erişim durumu |
|---|---|---|
| P4 v3 | Tarihsel; uygulama kaynağı değil | Yerel dosya adları görüldü; bütünlük/arşiv yayını A3'te |
| P4 v4 | Tarihsel; mimari kaynak; Codex ortam kararı geçersiz | Yerel MD/PDF/ZIP adları görüldü; A3'te kimlik kontrolü |
| P5 K00–K15 | Tarihsel; rol/veri modeli aktarımının kaynağı | `EXP-006_P5_Codex_Kurulum_ve_Devir_Paketi.zip` mevcut; bu tur hash/üye doğrulaması henüz yok |
| P5 S00–S12 | Tarihsel; senaryolar gelecekte sınav fikri olabilir | Repository'de teslim kaydı var; bu tur /mnt/data üst düzeyinde tam paket görülmedi. Alt dizin/ZIP, Files/Library ve repository araması A3'te yapılacak; bulunmuş sayılmaz |
| P5 v2 Codex arayüzü | Tarihsel; veri modeli aktarımının kaynağı | Yerel MD/PDF/ZIP adları görüldü; A3'te kimlik kontrolü |
| SOUL ve DevOS | Tarihsel kaynak; SOUL tanımı yeni planda güncellendi | Tam ve doğru kaynak kimliği henüz doğrulanmadı; farklı başlıklı bir metin yerine konulmaz |
| SOUL Academy | Keşif notu; karar/iş açma yetkisi değil | Önceki konuşmada Library kaydı okundu; A3'te gerçek gövde erişimi ve kimliği yeniden bağlanacak |

Aktarımın kaynak sadakatinin tamamen doğrulandığı iddia edilmez. Yeni planın değerlendirmesi yalnız [devos/plan/Inceleme_Degerlendirmesi_ChatGPT.md](https://github.com/batuhanozgun/devos/blob/main/plan/Inceleme_Degerlendirmesi_ChatGPT.md) bağlantısıyla bulunur; burada kopyalanmaz veya yeniden karara bağlanmaz.

## 6. Denetim yaklaşımı

Başlangıç commit'i **`8cd01e4afdcd0d37960b05930c91e1244678be6e`**. [BASELINE.json](maintenance/2026-09-29-research-installation-separation/BASELINE.json) kök tree/blob kimliklerini ve isteğin hash'ini taşır. Her yeni turda main ilerlediyse delta okunur; başka çalışmanın değişiklikleri geri alınmaz. Yayın force push olmadan yapılır; çakışan güncelleme sessizce ezilmez.

Tarama en az `Codex`, `güncel`, `current`, `sıradaki`, `next`, `DEVOS-001`, `DEVOS-002`, P4/P5 ve eski hedef repo adlarını kapsar. Tam yol envanteriyle karşılaştırılır; yalnız arama sonucunda görünmeyen bir dosya yok sayılmaz. Eşleşme tek başına hata değildir: kaynak alıntıları, tarihsel kanıt ve aktif araştırmanın kendi sonraki işi korunabilir. Her riskli eşleşme tür/statü/yönlendirme bakımından değerlendirilir. Arşivlerdeki özgün talimatlar açık pasif kaynak statüsüyle korunur; dosya içeriği sırf sözcük geçti diye değiştirilmez.

Son karşılaştırmada: silinen dosya sayısı sıfır; control blob/tree kimlikleri aynı; araştırma içerikleri aynı (yalnız yetkili statü/yönlendirme farkları gerekçeli); gerçek taşımalar varsa eski/yeni byte eşliği ve link düzeltmesi; yeni kaynaklar için hash ve kullanılabilir erişim yolu; yalnız bu repo üzerinde yazım.

Tam repo taraması ve bütün arşiv erişimi henüz yapılmadığı için “eski yönü güncel gösteren hiçbir kayıt kalmadı” hükmü verilemez. Erişilemeyen zorunlu arşiv varsa ilgili paket açık kalır; bağımsız durum/yönlendirme düzeltmeleri sürdürülebilir. Kullanıcıdan eksik teknik kararı çözmesi istenmez; yalnız gerçek kaynak engeli veya yetki çatışması bildirilir.

## 7. İlk turun kayıtları ve devam noktası

- Görev belgesi 108 satır olarak tam okundu; byte kimliği BASELINE.json'da.
- Main, kullanıcının belirttiği başlangıç commit'iyle aynı bulundu.
- AGENT taze okundu; dokuz protokolün blob kimlikleri bu konuşmada daha önce tam okunmuş sürümlerle aynı bulundu.
- Kök README ile EXP-006 INDEX, STATE, HANDOFF, WORK ve DECISIONS tam okundu; kesilen DECISIONS çıktısı ek aralıkla tamamlandı. Eski P5 paketine erişim bu tur sağlanmış sayılmaz.
- Dış plan yalnız 1–90. satırlarda sürüm/otorite açısından kontrol edildi; v2.1 başlığı görüldü. Planın tümü veya yeni ekler bu bakım turunda incelenmiş değildir.
- Main üzerinde `batuhanozgun-devos` author ve committer filtreli commit sorguları boş döndü. Bu sonuç tüm dallar veya ilişkilendirilemeyen kimlikler hakkında kesin yokluk kanıtı değildir.
- Bu ilk kümede yalnız kök README'nin statü/yönlendirmesi değiştirilir. Özgün README aynı Git blob'u ile `maintenance/.../baseline/README.md` altında tarihsel denetim kopyasıdır. Diğer eklemeler istek, başlangıç kimliği, bu bakım planı ve boş taşıma kaydıdır.
- D030 henüz eklenmedi; alt dosyalardaki eski güncel yönler ve rapor arşivi henüz düzeltilmedi. Kök uyarısı geçici korumadır, A2/A4 kapanışı değildir.

**Sonraki tek iş: A2 — D030 ve birbiriyle bağlantılı güncel durum/devir girişlerini düzeltmek.** Bu işe önce main delta ve yazar kontrolüyle başlanır. DevOS kurulumu veya planının yeniden yazılması bu çalışmanın devamı değildir.
