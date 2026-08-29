# keel — okuma defteri

Repo: `batuhanozgun/keel`  
Rol: somutlaşmış ürün/mekanizma yüzeyi  
Okuma stratejisi: öz-anlatı → kurucu model → defo modeli → seçici mekanik doğrulama

## Neden önemli

KEEL, durumsuz ajanlarla yazılım projesi kurup yürütmek için geliştirilmiş bir işletim disiplini. SOUL'un doğrudan öncülü olduğu varsayılmıyor; fakat oturum sürekliliği, rol/motivasyon ayrımı, insan karar kapıları, mekanik iz ve doğrulama gibi problemler üzerinde somut tasarım deneyimi taşıyor.

SOUL genel amaçlı bir agentic architecture hedeflediği için, KEEL'deki her mekanizma iki soruyla okunuyor:

1. Hangi gerçek problem/failure mode'u çözmeye çalışıyor?
2. Bu çözüm yazılım-projesi/Claude Code bağlamına mı özgü, yoksa daha genel bir ilke mi taşıyor?

## Okuma kaydı — öz-anlatı / kurucu model

| Kaynak | SHA | Tür | Maddi bulgu / işaretçi |
|---|---|---|---|
| `README.md` | `a221d174` | full | KEEL, dağınıklık/unutkanlık sorununa kanon, roller, kutular, mühürler ve kokpit ile cevap veren kurulum sistemi; "bilerek az anla, çalışan sistem bırak" merkezi |
| `GENESIS.md` | `a04b8060` | full | product plan yapmayan tek-seferlik kurucu; sabit plan, mühürler, çıkış ölçütleri, state dosyası ve mekanik sıra |
| `00_genesis/DEFO_MODELI.md` | `e9bddf5e` | full | on davranış defosu ve "öğüt yerine gözlemlenebilir iz/mekanik kapı" ilkesi |

## D geçişi — seçici mekanik doğrulama

### 1. Kurulum state'i ve oturumlar arası devam

| Kaynak | SHA | Tür | Mekanik bulgu |
|---|---|---|---|
| `00_genesis/GENESIS_DURUM.md` | `270e9153` | full | state tek makine-okur blokta: `Adım`, `Durum`, `Tamamlanan`; eski çift yazım ölçülmüş çelişki ürettiği için kaldırılmış |
| `.claude/settings.json` | `0d4db024` | full | `kurulum-surucu.sh` gerçek `Stop`, `acilis.sh` gerçek `SessionStart`, `kapanis.sh` gerçek `SessionEnd`, `file-guard.sh` gerçek `PreToolUse` kancalarına bağlı |
| `tools/guard/kurulum-surucu.sh` | `a386e36a` | selective code | eksik/tekrarlı alan, bilinmeyen durum, erken `.kurulum-tamam`, bayat `başlamadı`, tanınmayan adım ve kesintili tamamlanan-sıra fail-closed `exit 2`; kendi sınırı açık: işin gerçekten yapıldığını değil state/sıra tutarlılığını ölçer |

Hüküm: **durumsuz devam mekanizmasının bugünkü ağaçta gerçek kod karşılığı var.** Bu mekanizma görev doğruluğunu kanıtlamaz; yalnız kurulum yaşam döngüsünün tutarlı state'ini ve sırasını taşır.

### 2. Guard ve rol sınırı

| Kaynak | SHA | Tür | Mekanik bulgu |
|---|---|---|---|
| `tools/guard/README.md` | `dbcd0b03` | contract | `[SERT]`, `[SORULUR]`, rol kafesi, Bash/MCP dikişleri ve fail-yönleri tarifli; belge tek başına kanıt sayılmadı |
| `tools/guard/file-guard.sh` | `67abfd4f` | selective code | yazma/MCP/Bash kararları gerçek PreToolUse kodunda; kritik veri dosyaları okunamazsa çeşitli hatlarda fail-closed; `[SERT]`ten sonra rol kafesi gerçekten uygulanıyor |
| `tools/guard/file-guard.sh` rol-kafesi bölümü | `67abfd4f` | code | `.aktif-rol` bozuksa yazma engelleniyor; `yazamaz` rol yalnız geçerli kendi rol evine yazabiliyor ve kendi `ROL.md` sözleşmesi özellikle engelli |
| `.claude/agents/dogrulayici.md` | `6027a304` | full | doğrulayıcı araç listesi yalnız `Read, Grep, Glob`; yazma aracı yok; çalıştırma gerektiren doğrulama başka denetçi katmanına bırakılıyor |

Hüküm: **rolün kendi sözleşmesini ve koruma katmanını sessizce yeniden yazmasını azaltan gerçek mekanik sınırlar var.** Fakat bu bir güvenlik sınırı değil; README'nin kendisi Bash/MCP metin-eşleşmeli dikişlerin bilinen sınırlarını ilan ediyor.

### 3. Bekçi ve falsification yüzeyi

| Kaynak | SHA | Tür | Mekanik bulgu |
|---|---|---|---|
| `tools/bekci/README.md` | `91aa2d6b` | contract | sabit çekirdek + proje ayarı, makine satırı ve ayrı exit-code sözleşmesi; altı kurulumdaki watcher ayrışmasından doğmuş |
| `tools/bekci/test/` | — | index | tavan, şema, koruma, golden bağ, tek-ev ve bozma testleri ayrı dosyalar |
| `tools/bekci/test/bozma.test.mjs` | `3f5cb93e` | full test definition | temiz kurulum önce yeşil; ardından 9 kasıtlı mutasyonun `durduran`/`kilit` ve çıkış kodunu değiştirmesi bekleniyor. Hook kesme, bozuk JSONL, zorunlu dizin silme, kilitli karar değişimi, sembolik çapa, EL_KITABI başlığı silme, tavan aşımı, kadran ayrışması ve `[SERT]` kaçak dosya vakaları var |

**Verification sınırı:** mutation testlerinin bugünkü kodla gerçekten geçtiğini bu oturumda yeniden koşturamadım. Geçici ortamın GitHub ağı yoktu; release commit'i için GitHub Actions workflow run da görünmüyor. Son release commit mesajında "deneme kurulumu 1202 test yeşil" beyanı var, fakat bu commit-yazarı beyanıdır; bağımsız fresh execution değildir.

Hüküm: **test tasarımı falsification-capable görünüyor; fresh pass doğrulanmış değil.**

### 4. Karne / doğrulama / kapanış

| Kaynak | SHA | Tür | Mekanik bulgu |
|---|---|---|---|
| `.claude/agents/dogrulayici.md` | `6027a304` | full | kaynaksız iddia geçersiz; doğrulanamayana YEŞİL denmez; dosya-gerçeği katmanı salt-okur; aynı tür iki kanıt tek tür sayılır |
| `tools/sevk/sevk.sh` | `68f2a7d7` | selective code | bu dönemde iş zarfı olan kapalı görev için taze `YEŞİL` karne aranıyor; yok/bayat ise `dogrulayici` çağrılıyor; kırmızı/doğrulanamadı ayrı akış |
| `tools/sevk/sevk.sh` kapanış dalı | `68f2a7d7` | code | kapanış karnesi son iş zarfından sonra taze olmalı; YEŞİL kapanışta mühür paketine gidiliyor; KIRMIZI düzeltme adresine, DOĞRULANAMADI sahibin kararına gider |
| `.claude/settings.json` + `tools/sevk/zarf-bicim-kapisi.sh` | `0d4db024` / current | wiring+code | SubagentStop zarf kapısı gerçek hook'a bağlı; dönem içinde return schema/çatallar/kanıt alanları makinece değerlendiriliyor |

Hüküm: **"kimse kendi işine sadece kendi beyanıyla yeşil diyemez" ilkesinin bugünkü otonom akışta gerçek sevk/karne karşılığı var.** Bunun epistemik bağımsızlığı sınırlıdır: ayrı koltuk ve yazma yetkisi ortak model/ortak çerçeve hatasını ortadan kaldırmaz.

### 5. İnsan-okur ↔ makine-durum ayrımı

Somut örnekler:

- `GENESIS_DURUM`: state tek makine bloğunda; insan düzyazısında tekrar yok.
- bekçi: karar metin kelimesi taramasından değil makine satırı + exit code'dan türetiliyor.
- `sevk.sh`: kapalı görev tablosunu tek başına yeterli saymayıp zarf/karne tazeliğine bakıyor.

Hüküm: **geçmiş dış-göz seansındaki "insan-belgesi makine durumu taşıyor" kusurunun bazı kritik yüzeyleri bugün açık sözleşme ve ayrı makine alanlarıyla azaltılmış.** Ancak sistem bütünü hâlâ Markdown + dosya sözleşmeleri üzerinde; kusur tamamen yok olmuş sayılmıyor.

### 6. Ders → ihtiyaç anı / bağlam köprüsü

| Kaynak | SHA | Tür | Mekanik bulgu |
|---|---|---|---|
| `00_genesis/ROL_SKILL_KALIBI.md` | `92d04fef` | full | rol töreni ROL.md → DURUM.md → PANO sırasını zorunlu okuma olarak işaretliyor; bilgi kopyalanmıyor |
| `00_genesis/SOZLESME_KALIBI.md` | `f37a3d0a` | selective/full visible | role özel `Açılış ek-okumaları` alanı var; ilk kutudaki kayıt düzeni sonradan bu alanı güncelliyor; doğrulayıcı/üretici/domain/dış-göz modülleri doğuş derslerini sözleşmeye bağlıyor |
| `00_genesis/ILK_KUTU_KALIBI.md` | `c47f3c9b` | full | her iş rolü "süreçte neye ihtiyacım var / hafızasız oturum için ne kaydedilmeli" sorusunu cevaplıyor; `KAYIT_DUZENI.md` doğuyor ve rol `Açılış ek-okumaları` satırları buna göre güncelleniyor |
| `tools/guard/acilis.sh` | `c932a041` | selective code | yarım kurulum, sahip kuyruğu, dış-göz tazeliği, gece dönemi ve açık rol kafesi gibi belirli olayları SessionStart'ta görünür kılıyor; genel semantik ders retrieval'ı yapmıyor |

Hüküm: **ders→ihtiyaç köprüsü kısmen mekanikleşmiş ama tam çözülmüş değil.** State/rol/kayıt düzeni ve olay-tetikli hatırlatmalar ihtiyaç anına bazı bilgileri taşıyor; hangi geçmiş dersin yeni bir göreve semantik olarak ilgili olduğu ise büyük ölçüde ilk planlama sırasında doğru `ek-okuma` işaretçilerinin kurulmasına ve rol sözleşmesine bağlı.

## D geçişi — ara hüküm

KEEL'in öz-anlatısındaki temel mekanizmaların önemli bir kısmı bugünkü ağaçta yalnız düzyazı değil: hook wiring, fail-closed state parser, rol kafesi, salt-okur doğrulayıcı, taze-karne sevki ve kasıtlı bozma testleri var.

Buna rağmen üç sınır korunmalı:

1. **Claude Code bağımlılığı:** önemli garantiler hook olayları ve tool metadata'sına özgü.
2. **Model bağımsızlığı yok:** farklı koltuklar aynı temel model/çerçeve hatasını paylaşabilir.
3. **Ders retrieval'ı eksik:** bağlam köprüsü işaretçi ve planlama disipliniyle güçlenmiş, fakat genel "doğru dersi doğru anda getir" mekanizması değil.

Bu sınırlar, KEEL'i SOUL'a kopyalamak yerine failure sınıflarını yeniden türetme gereğini güçlendiriyor.

## Açık kalan doğrulama

- Fresh execution: bekçi/guard testlerini bu oturumda çalıştırıp yeşil olduklarını doğrulamak mümkün olmadı.
- Bazı büyük scriptler seçici bölümler halinde okundu; tüm satırların exhaustive audit'i yapılmadı.
- Hook/runtime davranışının Claude Code sürümüyle gerçek entegrasyonu bu repo-okuma turunda canlı harness üzerinde yeniden ölçülmedi.

## Sonraki yüksek-bilgi adımı

KEEL mekanizmasını daha fazla tüketmek yerine, **2026-08-11 araştırma-evi yönü ile 2026-08-25 SOUL bootstrap'ı arasındaki geçişi** os-architect karar/commit/kayıtlarından yeniden kurmak. Bu, SOUL Research'ün neden açıldığını doğrudan anlamak açısından yeni bir guard dosyası okumaktan daha değerlidir.
