# U07 — Yeniden gönderme ve yayın doğrulaması

**2026-09-11 / CONTENT PREPARED — REF/READBACK PENDING.** Kullanıcının yeni yeniden gönderme isteği yalnız özgün U07 tesliminin yayınını yetkilendirir. Bu tur yeni HERMES araştırması, probe veya model/provider çağrısı yoktur. [STATE](../../STATE.md), [MANIFEST](MANIFEST.json), [RESULT](RESULT.json).

Başlangıç main `d928ee14b16a277c010a966816fc2c4097944aab`, paket tabanıyla aynı. Bağlı GitHub bu kez create_blob/create_tree/create_commit/update_ref eylemlerini sundu; bu gözlem önceki kısıtın nedeni hakkında teşhis değildir. ZIP SHA-256 `473b3ad8ad78692455cb2cdb895174fb05063b869a16688fa8263ed23fd57b40`. Paketin read-only validator'ı 19 candidate yol, 24 raw regular üye, sekiz DB snapshot ve input/result bağlarını doğruladı. Bu doğrulama HERMES probe'unu çalıştırmadı.

Özgün RESEARCH/SOURCES/SPEC/RESULT/MANIFEST/raw arşiv/not22/coverage ve artifact kayıtları korunur. Current girişler, katalog HERMES satırı ve evidence README/PUBLICATION yalnız yayın durumunu uzlaştırır. Gerçek content commit, nonforce main ref, scoped diff ve blob/content readback sonucu doğrulama sonrasında bu üst bölüme kaydedilir. Tree/blob yaratılması tek başına yayın değildir.

---

## İlk U07 girişimi — tarihsel özgün kayıt

Aşağıdaki “NOT PUBLISHED”, “main U06” ve “write yok” ifadeleri ilk teknik turun anlık durumudur. Güncel yayın hükmü bu dosyanın üst bölümünden okunur; aşağıdaki tarihçe yeni bir engel veya yeniden yapılacak deney değildir.

# U07 — Yayın yapılamadı: write eylemleri bu tur sunulmadı

**2026-09-11 / NOT PUBLISHED TO MAIN.** Bu dosya bir yayın başarı makbuzu değildir. Yeni U07 source study ve sınırlı queue/SQLite koşusu yerel teslimde korunur. [RESEARCH](RESEARCH.md), [SOURCES](SOURCES.md), [SPEC](SPEC.md), [RESULT](RESULT.json), [MANIFEST](MANIFEST.json).

## Gerçek canonical durum

Başlangıçta ve teknik çalışma/teslim hazırlığı sonunda `git/ref/heads/main` bağlı GitHub üzerinden tekrar okundu:

**`d928ee14b16a277c010a966816fc2c4097944aab` — U06/v0.19 yayın makbuzu.**

Son ek STATE readback: `main` üzerinden 1–24 satırları U06/v0.19 başlığını ve `34a0b9894c6d05fbf5f07e50e127c0b18ab92963` blob'unu tekrar döndürdü. Bu gerçek uzak okuma yalnız yayımlanmış U06'yı doğrular; yerel U07 dosyalarını uzaktan doğrulamış değildir.

U06 içerik commit'i `8779ce350b32d5a1ccee6fa48c31604dd93616cc` main'dedir. U04-A/B, U05 ve U06 yayınları tamamlanmış iştir; eski U06 ZIP'ini yeniden göndermek gerekmez. **Yeni bekleyen çalışma yalnız U07'dir.** Candidate v0.20 dosyaları remote main'e bağlanmadı; yeni oturum yalnız main okursa U07'yi bulamaz.

## Bu tur sunulan capability

GitHub create_tree discovery boş döndü; full GitHub listesi 48 read/search eylemi sundu, dosya/commit/ref write eylemi göstermedi. Son write query de boştu. Plugin directory GitHub'ın installed/enabled olduğunu doğruladı; bu nedenle plugin yok veya repo bağlantısı kesildi denmedi. Yerel ortamda gh komutu yoktu; credential aranmadı, izin/ayar değişmedi, yeni plugin/bağlantı kurulmadı.

**Create/update/commit/update_ref/write çağrısı yapılmadı; branch/PR oluşturulmadı.** Read aracına gizli write semantiği yüklenmedi, alternatif endpoint/encoding ile kısıt dolaşılmadı. Araçların bu tur write eylemi sunmaması GitHub repository izninin iptal edildiğine kanıt değildir. Önceki U06'daki tool safety block da farklı olaydır; bu kayıtta U06 başarısızlığı güncelmiş gibi tekrarlanmaz. Neden capability setinin değiştiğine teşhis verilmez.

Bağımsız kaynak erişim sınırı da vardı: upstream gateway/run.py 3150–3325 isteği 429; bu source-read engeli publication capability yokluğuyla birleştirilmez. Diğer cron kaynakları okunabildi, native queue diagnostic kurulabildi.

## Yerel olarak doğrulanan

Full queue kaynağı `689fd620d6193003bbd168a0e62770a0d0306ac6` ve MIT license `75410e73319c72cd3e991a501c5455eb78f38375` Git blob'larıyla eşleşti. SPEC/probe/input/RESULT bağları doğrulandı. Altı ordinary vaka ve N00–N02'nin özgün kayıtları, attempt-00 metadata hatası, stdout/stderr ve sekiz final DB snapshot'ı korunur.

24 regular üyeli raw archive 13.912 byte; SHA-256 `4fdf2481f64ef6b1ee1ac177f43f727958f7769cf976276266be71a570b9644b`, Git blob `b42a8116e38fa7fe2d58fff52476e7b347c7e191`. Native SPEC/RESULT arşiv kopyalarıyla byte-eşittir. Artifact kontrolleri yeni HERMES davranış deneyi veya independent replication değildir. Sekiz final DB snapshot'ı immutable read ile integrity=ok verdi; boş WAL/bookkeeping ve bytecode exclusion'ları manifestte açıkça listelendi, behavioral failure dışlanmadı.

Beş eski entry ile CATALOG baseline'ı eski U06 paketinden ancak yayımlanmış exact blob eşleşmesiyle materyalize edildi; current v0.19 dosyaları bu tur GitHub'dan da okundu. Eski unpublished U06 STATE/PUBLICATION/README baseline yapılmadı. Current STATE blob'u `34a0b9894c6d05fbf5f07e50e127c0b18ab92963`tir. Yeni candidate STATE bu exact snapshot üzerine tasarlanmış tam replacement adayıdır, yapılmış remote mutation değildir.

CATALOG baseline blob `8483cbd792542561eef926a83fc66349dcc06a17`; candidate'da yalnız HERMES satırı değişir. HERMES satırı çıkarıldığında kalan byte'lar aynı. Diğer yeni/current candidate yollar yalnız `research/studies/hermes-agent/**` içindedir. Foundation/control/context/diğer studies/eski Hermes not/evidence/synthesis/METHOD için candidate mutation yoktur.

## Gelecek yayın kapısı

Önce güncel main ve kontrol/STATE okunmalı. Bu teslimin üst README/PUBLICATION-HANDOFF, PACKAGE-MANIFEST ve evidence MANIFEST dosyaları doğrulanmalı. U07'nin source/RESULT/probe/SPEC/log/DB kanıtı yeniden üretilmemeli. Mevcut main ilerlediyse exact baseline compare yapılmalı; başka çalışma üzerine eski tree zorlanmamalıdır. Yeni hedef dosyası zaten varsa içeriği karşılaştırılmadan overwrite edilmemelidir.

Write aracı gerçekten sunulduğunda yalnız scoped değişiklikler hazırlanır; current STATE/META/INDEX/plan/ledger/questions/catalog ile bu PUBLICATION ve evidence README gerçek yayın durumuna göre uzlaştırılır. Note22/source/research/coverage içindeki ilk unpublished kayıtlar tarihsel ilk teslim anıdır; raw deney içeriği değiştirilmez. Ref force=false ilerletilir. Başarı ancak gerçek main ancestry, scoped diff, dosya kimlikleri ve gerekli içerik readback'iyle kaydedilir. O aşamada bu başarısız-publication kaydı tarihsel bölüm olarak korunabilir.

**Şu anda main yayını veya remote candidate içerik readback'i yoktur.** Sonraki teknik iş actual cron drainer/status consumer, occurrence/rearm ve run_job bağlamıdır; yayın açığı bunu yeniden araştırma kotasına dönüştürmez. Q40/Q42 ve diğer eski doğrulama borçları kapanmadı.
