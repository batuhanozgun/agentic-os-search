# ECC — Question Register

**Initial date:** 2026-09-17. Sorular ilk taramadan türetilmiştir; cevap/nihai taxonomy değildir. Bir sorunun current epistemic state'i burada, aktif birimin yetkisi STATE'tedir. ID'ler korunur; bölünürse eski soru çocuklarına yönlenir.

| ID / initial status | Soru ve rakip açıklama | Ayırt edici kanıt / bounded kapanış |
|---|---|---|
| Q01 / OPEN — U01 adayı | ECC tek coherent runtime mı; taşınabilir varlık+adapter bileşimi mi; farklı olgunluktaki ürün/yönlerin birleşimi mi? | Pinned tree, manifests, actual entrypoints ve dependency/consumer haritası; repo/package/hosted/alpha sınırı. Marketing adları cevap sayılmaz. |
| Q02 / OPEN | Ortak davranış gerçekten taşınıyor mu; yalnız metin mi taşınıyor? Native/adapter/instruction etiketleri hangi etkiyi garanti ediyor? | Aynı mekanizmanın farklı host yolları; loading/event/tool/permission/consumer farkları; declared support ile runtime kanıtı ayrı. |
| Q03 / OPEN | Kaynak, installed state ve ownership aynı anda tutarlı mı? Update/uninstall/partial failure neyi koruyor? | Plan/apply/ledger ve actual readback; kullanıcı dosyası/kopya/generated içerik ayrımı; conflict, rollback ve idempotence yolları. |
| Q04 / OPEN | Work/session/worker state gerçekten işleri yönetiyor mu, yoksa yalnız raporluyor mu? Resume snapshot'tan fazla ne gerektiriyor? | Producer→canonical record→consumer/effect zinciri; approval/delegation/handoff; stale state, crash ve başka oturum/host'a geçiş. |
| Q05 / OPEN | Memory veri mi, davranış otoritesi mi; scope filtre mi, güvenlik sınırı mı? Yazılmış bilgi gerçekten uygun işe giriyor mu? | Save/search/read/acceptance yolları; source/trust/freshness; user/team/project sınırı; no-result ile incomplete-read ayrımı ve gerçek tüketici. |
| Q06 / OPEN | Instinct/skill üretmek öğrenme sayılıyor mu; geçerli, kabul edilmiş ve yararlı yeniden kullanım var mı? | Observation→candidate→promotion→loading/use→outcome; confidence oracle, contamination/forgetting, başarısız örnek, nedensel fayda sınırı. |
| Q07 / OPEN | Security scan/guard neyi ve hangi anda koruyor; instruction, static diagnosis ve runtime enforcement karışıyor mu? | Tehdit modeli, protected effect, call site ve bypass; dış AgentShield dependency sınırı. Eski issue'lar ancak güncel durum/patch bağıyla kullanılır. |
| Q08 / OPEN | Eval/health/observability gerçek kaliteyi mi yoksa varlık/sayı/biçimi mi ölçüyor? | Test oracle, fixture, negative control, coverage, criterion freshness; metriğin sonraki karar/değişikliğe bağlanması; maliyetin doğru paydası. |
| Q09 / OPEN — geç sentez | SOUL/Development OS için ne gerçekten yeni/değerli, ne tekrar/uyumsuz/henüz kanıtsız? | ECC-native bulgular + seçili eski study evidence + güncel Foundation/target scope. Eşdeğer olmayan katmanlarda kıyas yapılmaz. |
| Q10 / OPEN — yöntem | Yöntem önemli soruları keşfetmeye, izlenebilir senteze ve doğru devralmaya yardım ediyor mu; yoksa kayıt/checklist yükü üretiyor mu? | METHOD-REVIEW'da gerçek yöntem değişimi→sonraki birim etkisi; repository-only yeniden giriş; kaçırılan/yeniden açılan soru, tekrar ve aktarım sınırları. |

## Başlangıçta korunacak alternatifler

ECC'nin değeri yalnız portability olmayabilir. Host'un sağladığı davranış ECC'nin başarısı sayılmayabilir. Aynı code core aynı entrypoint davranışı demek değildir. Sentezimiz temiz görünürken gerçek ürün parçalı kalabilir. Metodumuz ayrıntılı olduğu halde kritik üretim/consumer/etki sorusunu kaçırabilir. Bunlar kanıtla ayrıştırılacak alternatiflerdir, varsayılan suçlama veya sonuç değildir.

## Güncelleme kaydı biçimi

Bir sorunun statüsü değişince ilgili not/kanıt ve gerekçe bağlanır: OPEN; ACTIVE; BOUNDED-ANSWERED; BLOCKED; DEFERRED (tetikleyiciyle); REOPENED; SUPERSEDED (yeni ID ile). Bounded answer güçlü runtime/effectiveness genellemesini zorunlu olarak kapatmaz. Açık riskin kaydı kapanış olarak sayılmaz.

Her maddi soruda sonradan doldurulacak içerik: kapsam; sahiplenen birim; alt sorular/bağımlılıklar; kaynak/not bağlantıları; savunulan kısa sonuç; counterexample; açık sınır; yeniden açılma koşulu. Bugün sonuç yok; alan doldurmak için hayali bulgu üretilmez.
