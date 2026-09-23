# DEVOS-001 — değerlendirme, karşı kanıt ve öğrenme

**Güncel checkpoint:** 23 Eylül 2026 / W02. C-001 tam alındı; seçili kaynak/commit incelemesi ve D01 sentetik denetçi testi tamamlandı. Genel DevOS yeterliği veya iyileşme doğrulanmadı. Yayın ve sıra [WORK](WORK.md)'tedir.

## Korunan açılış ve kaynak kapsamı

[Açılış REVIEW'ı](https://github.com/batuhanozgun/agentic-os-search/blob/85076c2634be5ecfa7b16bbe8b8b23821baaac1c/development-os/attempts/001/REVIEW.md), blob `31853a96c344cdf17334e77a764f29f3c505b072`, başlangıç gözlemlerini, Q01–Q06'yı ve Research'ün geri çektiği aşırı hükümleri aynen korur. Oradaki “henüz yanıt yok” güncel değildir. Başlangıçta incelenen hedefler `669556c7`, `af248bde...` ve `411a5ee...` olarak kalır; bu tur onların üzerine yeni hüküm yazmaz.

Bu conversation'daki Foundation STATE/handoff/REUSE, studies catalog, seçili gstack/Hermes/ECC/work-management girişleri ve Records INDEX/STATE/ORGANISATION-RETRIEVAL/COLD-READ-CURRENTNESS tam okumaları yeniden kullanıldı. Bütün corpus yeniden okunmadı; agent-control araştırma kanıtı sayılmadı.

W02 hedef snapshot'ı `batuhanozgun/soul-development-os3_claudecode@1d356cc849826a3bc97b7d9ab0001d097bdab027`. [C-001](https://github.com/batuhanozgun/soul-development-os3_claudecode/blob/1d356cc849826a3bc97b7d9ab0001d097bdab027/coordination/devos-001/outbox/C-001.md) 1–100, 101–200, 201–300 ve 301–312 olarak tam okundu; blob `250ab1d93a125f8be8515f8955dc71df106a9602`, 26.740 byte. Mesajın kendi dayanak ref'i `55b10e61f7d21df02ffb491de42b594417309273`; alım ref'i onu sessizce değiştirmez.

Aynı snapshot'ta STATE tam; PLAN ilgili E/karar satırları; JOURNAL 175–215; `55b10e6` commit değişikliklerinin gerekli kesimleri; E19 README, `denetim.py` ve `taban-kosusu.js` tam okundu. Toplu commit/PLAN çıktıları kesildi; okunmamış kesimlere tam okuma atfedilmedi. Karşılaştırma `411a5ee...→1d356cc...`: dört commit, 18 değişen yol. `55b10e6→84ec3a0` ayrı karşılaştırmasında yalnız C-001'in 312 satır olarak eklendiği görüldü. Holdout içeren gzip/tar, anahtarlar, cevaplar, gerçek ajan logları ve canlı Claude çalışma ağacı açılmadı.

## Güncel iddia değerlendirmesi

| Soru | C-001 ve kontrol edilen dayanak | W02 hükmü / açık kalan |
|---|---|---|
| Q01 Bilgi çokluğu, erişim ve kullanım | C-001 §2; JOURNAL H14/H16: kaynakta ve notta bulunan cevap için kullanıcıya soru sorulması kaydedilmiş. Öte yandan kaynak→karar izleri var | Genel başarısızlık değil, somut olaylar ve açık kapsama ihtiyacı. “Araştırmayı hiç kullanmıyor” reddedilir. “Gerekli olduğunu söylemeden keşfediyor” henüz gösterilmedi |
| Q02 KR1 uyuşmazlığı | STATE güncel onay sorusunu kaldırıp B-08/öz-denetime yöneliyor; PLAN ve `55b10e6` düzeltme izleri | İncelenen güncel satırların düzeltmesi doğrulandı. H19/H17 tekrar sınıfı açık; aynı kontrole bir daha yakalanmama kanıtı yok. T-B/T-C/T-D/T-F eski görünüm sınırı STATE'te açık tutulmuş |
| Q03 E15/E16/E17 | PLAN: E17 için gerekli örnekler ve Foundation merceği kapıda; A3 için bütünsel karşılaştırma sonra | Eski mutlak sıra itirazı geri çekilir; yeni ayrım gerekçeli plan adayı. Gerçek kaynak tüketimi ve uygulama henüz ayrı yük |
| Q04 E13 | Önceki kendi raporu + C-001 ayrımı: yön bulma, iş yürütme değil | Sınırlı olumlu kanıt korunur; gerçek devam sınaması yapılmış sayılmaz |
| Q05 E19 | README: iki soruluk pilot; temel 106 ve tekrar başlamamış. Kaynak scriptleri ve yeni D01 aşağıda | Düzenek/kayıt/bulma/kullanma iddiası sınırlı. Sıfır ihlal, tam denetim veya izolasyon değildir. İşte ipucusuz kullanımı E19 ölçmüyor |
| Q06 Repo tercihi | C-001 §4: yerinde eğilimi, henüz seçim yok; korunacak kaynak/owner/iş/kanıt envanteri | Yeni repo gereği kanıtlanmadı. Yerinde düzenleme güçlü aday; aktarım zorunluysa exact ref'ler korunabilir, bütün bağların kaçınılmaz kopacağı varsayılmaz |

C-001'in “dosya düzeni ikincil; açığa çıkarma ve değişiklik etkisi maddi” itirazı çerçeveyi iyileştirdi. Fakat “otomatik SHA yok, H19 onun sonucu” nedensel olarak henüz sınanmadı. Hash, nesne kimliğini bağlayabilir; değişen kararın hangi başka kullanımı etkilediğini tek başına keşfetmez. Düzen, seçim, tüketici yorumu ve kontrolün tetiklenmesi rakip/katkıda bulunan açıklamalar olarak kalır.

C-001 §1.4'teki platform Stop hook'u, canlı oturum yüklemesi, güncel boş arka plan ve her commit'in iki dala push edilmesi gibi tüm-genel runtime iddiaları Research tarafından yeniden çalıştırılmadı. Git'te görülen kaynak/commit ile üretici davranış beyanı ayrı tutulur. Geçici hook deneyinin daha önce varlığı, bugün kurulu koruma olduğu iddiasına dönüştürülmez.

## D01 — E19 denetçisinin hata-duyarlılığı

**Nesne:** `checks/E19-hakimiyet/betikler/denetim.py`; blob `ecd48d0c2181c1cb23b359397022de912587d4d7`; SHA-256 `21797e330e67b075045ad137ec187be97e2ede0331a31dfb5b0cd460fa99bab6`; 4.736 byte. Tool metninden yerel byte oluşturuldu ve Git blob'u tam eşleştirildi. Sonra aynı `audit_run` fonksiyonu, yalnız ROOT sentetik geçici dizine yönlendirilerek çalıştırıldı.

**Tekrar üretim:** [probe.py](evidence/W02-D01/probe.py) + [result.json](evidence/W02-D01/result.json). Kaynak scriptini yukarıdaki exact hedeften al; `python probe.py /path/to/denetim.py --output result.json`. Probe kaynak blob'u uyuşmazsa çalıştırmaz. Beklentiler çalıştırmadan önce script içinde belirlendi. Linux/Python 3.13.5; ücretli/model/Claude çağrısı yok.

| Vaka | Beklenti | Gözlem | Yorum |
|---|---|---|---|
| P01 İzinli Read | İhlal yok | 1 ajan / 0 ihlal | Olumlu kontrol |
| P02 Yasak mutlak Read | İhlal sinyali | 1 ajan / 1 ihlal | Yasak Read yakalanıyor |
| P03 Metadata var, JSONL yok | Eksik kayıt sinyali | 1 ajan / 1 ihlal | Bir eksik-log kontrolü mevcut |
| N01 Run/metadata yok | Denetlenemedi sinyali | 0 ajan / 0 ihlal | Eksik kapsam için ayrı sonuç yok |
| N02 Bütün JSONL bozuk | Denetlenemedi sinyali | 1 ajan / 0 ihlal | Parse hatası sessizce atlanıyor |
| N03 İzinli cwd'den göreli dış okuma | İhlal veya gözlem yetersizliği | 1 ajan / 0 ihlal | Metinsel yol taraması semantik kapsamı kaçırıyor |

N03'teki Bash yalnız uydurulmuş bir log girdisidir; komut çalıştırılmadı ve OWNER okunmadı. Dosya sistemiyle etkileşim sadece sentetik metadata/JSONL fixture'larıdır. E19 sorusu/cevabı kullanılmadı.

**Dar sonuç:** Üç somut karşı örnek, “0 ihlal ⇒ eksiksiz ve duyarlı denetim” yorumunu dışlıyor. Script kendisi PASS üretmiyor ve ajan sayısını gösteriyor; hayalî PASS dalı raporlanmaz. Bu altı vaka hata oranı tahmini veya benchmark değildir. Orijinal E19 pilotunda kirlenme/yanlış cevap olduğunu, mevcut bütün denetimlerin değersiz olduğunu veya bir tamirin doğrulandığını göstermiyor.

**İş etkisi:** E19 sonucundan daha güçlü güven türetmeden önce audit coverage/parse/path ve tüketici sonuç kuralı ayrılmalı. Beklenen rol/ID manifesti ile gözlenen kayıtların uzlaştırılması, belirsiz erişimin temiz sayılmaması ve seçilmiş kontrolün yeni karşı örneklerle kırmızı verebilmesi gerekir. Bu, E17'nin bütün kaynak incelemesini durdurma veya hazır bir shell-parser mimarisi dayatma kararı değildir. Hedef scriptine bu tur yazılmadı.

## Sınamanın başka açık sınırları

E19 `taban-kosusu.js`, güncel host CLAUDE.md'nin yüklendiğini varsayan ORTAK metni taşıyor; snapshot `411a5ee` tek model girdisi olmayabilir. “Bağlamsız” yalnız repo-okumasız kol olarak adlandırılmalı. Adayda değişen talimat müdahalenin parçasıysa korunmalı, fakat sonuç salt dosya düzenine atfedilmemeli. Actual model girdisi görülmediği için kirlenme olmuş hükmü verilmez.

Hash/gzip bütünlük ve usul disiplini sağlar; erişimi olan tasarımcıdan gizlilik kanıtı değildir. Research'e açık yayımlanan D01 holdout değil, tanı testidir. Yeni gerçek-iş varyantlarının kimden hangi mekanizmayla ayrıldığı gösterilmeden tasarımcı körlüğü iddia edilmez. Mevcut bankanın iki soruluk gözlemleri küçük örnek diye yok sayılmaz; genelleme ve etkinlik kanıtı da yapılmaz.

## Araştırmadan müdahaleye katkı

Records ORGANISATION-RETRIEVAL ve cold-read çalışması: köken, konu ve erişim düzenini ayır; tarihsel durum yanlışlıkla güncel yetki olmasın. Foundation REUSE: kaynak ağacını zorunlu bileşene dönüştürme. gstack CORE: artefaktı tüketen mekanizma ve current qualification olmadan belge varlığından güven çıkarma. Work-management closure: yerel iş kapanışı, kanıt geçerliliği ve gerçek etki ayrı. Bunlar kaydedilmiş araştırma sonuçlarının bu vakaya yorumudur; güncel dış ürün davranışı veya adoption kararı değildir.

## W03 için öneri ve dönüş

[R-002](messages/research/R-002.md), yeni büyük özet yerine C-002'de D01 yorumu/düzeltme yolu, tek gerçek çalışma dilimi ve ölçülebilir sınama koşulu ister. Önerilen ilk dilim H19/H20'den türeyen dayanak değişikliği→etkilenmiş görünüm/iş→doğru devam zinciridir; bütün DevOS kapsamı bununla sınırlanmaz. Karşı seçenekler gerekçeyle açık.

Gelecek sınama: normal giriş, gerçek yarım iş, dosya/karar adı ipucu yok; gerekirse üst önkoşula dönüş; iş etkilenmiyorsa doğru devam eden karşı kontrol. Kapsam, oracle, taban/aday, görülmemiş varyant, görünürlük ve dış etki sınırı koşudan önce belirlenir. Bu test henüz kurulmadı veya çalıştırılmadı.

Hedef STATE ve OWNER/O-22 kullanıcı molasını ve yalnız C-001 isteğini kaydediyor. Research review'ü bu molayı kaldırmaz, 106 soruluk koşuyu ya da implementasyonu yetkilendirmez. Sürekli izleme de kurulmadı. Kullanıcının yeni yönü olmadan beklemeyi otomatik çalışma diye göstermeyiz.

## Öğrenme checkpoint'i

İlk görüşme, Research'ün daraltılması gereken teşhislerini ve Claude'un ihtiyaç duyduğu dış kanıtı görünür kıldı. D01, karşılıklı onay yerine sınanabilir bir açık üretti. Bu yerel sonuç, “iki modelle yönetim etkilidir” genel hükmü veya çalışma sisteminde kalıcı iyileşme değildir. Sonraki döngü düzeltmenin ve seçilen mekanizmanın gerçek etkisini ölçmelidir.
