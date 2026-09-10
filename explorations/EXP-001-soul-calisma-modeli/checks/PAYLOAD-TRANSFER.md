# EXP-001 — Özgün eserleri yayımlama devam noktası

## Mevcut ayrım

Diyalog, öğrenme/değişim kayıtları ve retrieval metinleri GitHub `main` üzerinde yayımlanmıştır. Aşağıdaki **32 dosyanın byte içeriği henüz GitHub'da değildir**: altı özgün eser/ek ve kaynak ZIP'inden çıkarılan 26 dosya. SOURCE-MANIFEST'teki `github_payload: pending` bu nedenle korunur. Metin arşivini bu payload'ların tam arşivi sayma.

Yerel gerçek byte'lar **EXP001_Artefakt_Tamamlama_Paketi.zip** ile kullanıcıya teslim edilir. Bu ZIP tüm diyalogun ikinci bir kopyası değil, repository'deki eksik eser içeriklerini tamamlayan pakettir.

Beklenen `PAYLOAD-MANIFEST.json` SHA-256:

`f694d43923ec28e190f985aa30de6b9eefbe739bd00f0c773695785ee1a9e42c`

Paket içindeki `repo-overlay/` yolları repository köküne göredir. Toplam payload: **32 dosya, 6.176.086 byte** (ZIP sıkıştırması öncesi). Altı orijinalin bireysel kimliği SOURCE-MANIFEST'te, tüm 32 dosyanın kimliği tamamlama paketindeki manifesttedir. Tekrarlanan HTML/PDF/Markdown, özgün ZIP yapısının bilinçli ve byte-eşit kopyalarıdır; yeni canonical içerik değildir.

## Bu turdaki aktarım sınırı

GitHub connector'ünün `create_tree → create_commit → update_ref(force=false)` metin yayımlama yolu çalıştı. Yerel dosya yolunu alıp byte içeriğini doğrudan yükleyen eylem bu arayüzde bulunmadı. `create_blob` literal UTF-8/base64 içerik kabul eder; bu, yerel büyük dosyaları güvenilir biçimde aktaran bir dosya-köprü arayüzü değildir. Bu tur büyük payload aktarımı tamamlanmadı.

Container'dan standart HTTPS/Git yolu için ayrıca ağ erişimi denendi; raw GitHub host çözümlemesi `Temporary failure in name resolution` ile başarısız oldu. Yerel gh istemcisi veya kurulmuş GitHub CLI kimlik doğrulaması da gözlenmedi. Connector erişim belirteçleri başka bir yazma kanalına taşınmadı.

## Sonraki yetkili yürütücü için sınırlı iş

1. Canonical `AGENT.md`, paket STATE ve bu dosyayı oku. Bu devam işi yalnız arşiv payload'larını yayımlamaktır; Atlas geliştirme veya araştırma başlatma değildir.
2. Kullanıcının sağladığı aynı manifest hash'li tamamlama ZIP'ini güvenli bir dizine aç. Eksik ZIP'i özet veya hash'ten yeniden üretme.
3. Güncel `batuhanozgun/agentic-os-search` checkout'unda mevcut değişiklikleri koru. `repo-overlay/` içindeki yalnız manifestteki 32 yolu değerlendir.
4. Paketteki `tamamla.py <checkout>` varsayılan dry-run yapar. `--apply` yalnız eksik ve kaynak hash'i doğru dosyaları kopyalar; farklı mevcut hedefi veya symlink yolunu reddeder. Otomatik commit/push yapmaz. `--verify` tüm hedeflerin byte eşitliğini kontrol eder.
5. Gerçek değişiklikleri ve hassas bilgi bulunmadığını gözden geçir. Yalnız bu eser yollarını ve doğrulama sonucu gerektirdiği paket STATE/manifest/checks güncellemelerini commit et; unrelated dosyaları ekleme. Force push kullanma.
6. Remote HEAD/path/blob varlığını ve indirilen dosyaların SHA-256 değerlerini yeniden doğrula. Yeni remote kanıtı olmadan `pending` veya PARTIAL durumunu kaldırma.
7. SOURCE-MANIFEST, STATE, WORK-PLAN ve ARCHIVE-COVERAGE'i gerçek sonuca göre güncelle. Görünür diyalog aktarımı yine ham platform export'u olarak adlandırılmayacak.

## Yerel helper doğrulaması

Yalnız kopyalama helper'ı için 9 yerel sentetik kontrol geçti: dry-run yazmaz; eksik verify başarısız; 32 byte-eşit kopya; tam verify; aynı içerikte idempotent tekrar; farklı hedefte yazmadan durma; symlink reddi; yanlış repo origin reddi; bozuk kaynak reddi. Bu testler GitHub yayını, güvenlik sertifikasyonu veya SOUL ajan davranışı değildir.

## Tamamlama sonrası

Tamamlama paketinin işi bittiğinde EXP-001'in esas erişim yolu repository olmalıdır; bu sohbetin sandbox bağlantıları veya kişisel hafıza değildir. Ham platform export'u ayrıca elde edilirse kaynak aktarımı onunla karşılaştırılabilir; bu ek kontrol orijinal kaynak dosyalarını sessizce değiştirmemelidir.
