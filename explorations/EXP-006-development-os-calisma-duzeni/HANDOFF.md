# EXP-006 — HANDOFF

**28 Eylül 2026 / P4 v3 stres testi ve sayfa sınırsız yeniden yazım / PAUSED / TESLİM DOĞRULANMADI.**

## 1. Ne devralınıyor?

Kullanıcı v2'nin 200 sayfa koşulu altında eksik veya az işlenmiş olabileceğini belirterek yapının stres testini ve raporun sayfa sınırı olmadan yeniden hazırlanmasını istedi. Son çalışma tamamlanmış yeni PDF/kaynak paketi olarak teslim edilmedi. Şimdi kullanıcı yeni oturumda devam etmek üzere duraklatıyor.

**Bu bir v2 uygulama devri değildir.** Yeni oturumun işi, SOUL hedefi karşısında v2'nin kapsamlı değerlendirmesini ve sayfa sınırsız yeni yazımı tamamlamaktır. P5/P6 başlamaz. 200 sayfa şartı kaldırılmıştır; ne 200'e sığdırma ne daha çok sayfa üretme başarı ölçütüdür.

## 2. Okuma ve gerçek dosya yolu

AGENT ve tetiklenen kontroller → INDEX → STATE → WORK → DECISIONS → [P4-03](work/P4-03-unbounded-stress-test-handoff.md) → [P4-02](work/P4-02-soul-derived-report-v2.md) → **gerçek v2 kaynakları**.

Bu konuşmada hazırlanmış `EXP-006_Yeni_Oturum_Devir_Paketi.zip` içinde v2 PDF ve orijinal `EXP-006_DevOS_v2_Kaynak_Paketi.zip` vardır. Kaynak ZIP açıldığında `source/DevOS_v2.md`, `source/catalog.json`, `contracts/`, `reference_model/` ve `qa/` bulunur. Kimlikler ve doğrulama kapsamı P4-03 §3'tedir.

Tam gövdeler GitHub'a yüklenmedi. Yeni oturuma bu devir paketi eklenmeli veya aynı hash'li v2 kaynakları erişilebilir olmalıdır. Eski conversation dosyalarının otomatik geleceği, hash'in erişim sağlayacağı veya repository özetinin raporun yerine geçeceği varsayılmaz. Erişim yoksa gereken tek kaynak paketi açıkça istenir.

Ayrıntılı yeniden değerlendirmede v2'nin tam Markdown gövdesi okunur; sözleşmeler ve model birlikte incelenir. Bu devir turu tam rapor incelemesi değildir: canonical kayıtlar, mevcut dosyalar, manifest ve tarihsel QA varlığı kontrol edildi. Rapor içeriği veya kod bu tur yeniden test edilmiş sayılmaz.

## 3. Kanıt statüsü — kritik

**Doğrudan kontrol edildi:** V2 PDF ve ZIP SHA-256 değerleri P4-02 ile eşleşti. ZIP CRC ve manifest'teki 22 dosyanın byte/hash değerleri eşleşti. Kaynak metin, sözleşme, model ve tarihsel QA dosyaları mevcut.

**Yalnız tarihsel kayıt:** V2 paketindeki 40 test ve dört guard-kaldırma sonucu. Bu tur yeniden çalıştırma yok; hedef PostgreSQL/Claude, gerçek kimlik/yayın/restore veya bilişsel yeterlik kanıtı değil.

**Yeniden doğrulanacak assistant iddiaları:** Aynı işlem anahtarının farklı hedeflerde kullanımı; zorunlu bilgisi eksik context'in kabulü; restore sonrası eski görevlendirme kimliğinin yeniden oluşması; graph sorgularında yol sayısının patlaması. Önceki son cevap bunları bulgu olarak anlattı, ancak bu tur ilgili v3 kod/log dosyaları recover edilemedi. Bunları doğrulanmış sonuç diye taşımak yasaktır; kapsamları önce yeniden üretilmeli veya çürütülmelidir.

**Teyit edilmedi:** “88 test geçti”, yeni PDF'nin hazır olduğu veya v3 düzeltmelerinin uygulanmış olduğu. Erişilen mounted dosyalarda v3 rapor/kod/ham log yoktu; yalnız v2 sayfa görüntüsü niteliğinde bir v3-work dizin kalıntısı vardı. Files araması da sonuç vermedi. Bu gözlem her olası depoda kalıcı kayıp kanıtı değildir.

## 4. Korunacak amaç ve tasarım sınırı

SOUL; gerekli işi keşfeden, işe özgü çalışma sistemi oluşturan, araştırmayı kullanan, uzun/bileşik eserleri sürdüren/değerlendiren ve yöntemleri gerekçeli uyarlayan hedef yapıdır. DevOS bu kabiliyetleri geliştirebilecek ve sınayabilecek düzene göre değerlendirilir; sadece kod görevi kuyruğu veya iyi dosya düzeni olarak daraltılmaz.

Cloud hedefi, K1/K2, kullanıcı yetki/kabulü, içerik sahibi–düzen sahibi ayrımı korunur. SOUL'un gerçek ilk işini assistant seçmez. Gereken kalite kolaylık lehine düşürülmez; daha fazla servis veya formalizm de kendi başına iyilik sayılmaz.

V2'nin PostgreSQL/typed graph, Git, memory/context, korunmuş publisher ve takım ağırlıklı önerileri inceleme nesnesidir; kullanıcıca kabul edilmiş mimari değildir. Önceki P4-01'in alt-ajan/Git ağırlıklı tercihi veya permission-matrix next'i current rota olmaz.

## 5. Sonraki anlamlı çalışma

P4-03 §5 tek ayrıntılı devam haritasıdır. Önce v2'yi dosya kimliğiyle kur; varsa gerçek v3 kaynaklarını inceleyerek kurtar. Bulunamazsa bilinmeyen v3 dosyalarını uydurmak yerine doğrulanmış v2'den devam et.

Tam tasarım okuması → SOUL hedefi/başarısızlık haritası → mevcut testlerin yeniden koşulması → ayrı falsifier/olumsuz senaryolar → bulgu ve kanıt kaydı → gerekçeli tasarım/sözleşme düzeltmeleri → yeniden sınama → bütünleşik sayfa sınırsız rapor/kaynak teslimi.

Dört ipucu incelemenin sınırı değildir. İş keşfi, rol/uzmanlık/iletişim, graph, memory/context, yetki/izolasyon, publication, concurrency, recovery, uzun/bileşik iş ve değerlendirme kapsamı birlikte ele alınır. Unit test sonuçları bu alanların tamamını doğrulamaz. Gerçek runtime erişimi olmayan testler yapılmış gösterilmez.

Yeni rapor normal akışla sayfalansın; eski renderer'ın 200 sayfa ve sayfa-başına metin zorlaması aktarılmasın. Son teslimde kaynaklar, ham test kayıtları, yapılmayanlar, dosya kimlikleri, link/görsel kontrolü ve repository readback'i birlikte korunur.

**Bu tur durma:** Devir kayıtları ve taşınabilir kaynak paketi hazırlanır; yeni stres testi veya yeniden yazım başlatılmaz. Kullanıcı yeni oturumda devam edecek. Tamamlanmamış v3 başarı olarak kapatılmaz.
