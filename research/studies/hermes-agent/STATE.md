# Hermes Agent — STATE

**Durum:** ACTIVE RESEARCH / PINNED CALLER AND MEMORY SOURCE ANALYSIS + BOUNDED CONTEXT-TRANSFER AND RECOVERED U01B2 EVIDENCE  
**Son kayıt tarihi:** 2026-09-08  
**Kaynak pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`  
**Mevcut plan:** [RESEARCH-PLAN.md](RESEARCH-PLAN.md), v0.6; U01B2 yayını çalışma sırasını değiştirmedi.  
**Araştırma tamamlandı mı?** HAYIR. Ordinary caller/dispatch ve memory kesitleri ilerledi; bütün caller varyantları, öğrenme kalitesi ve genel sistem sentezi kapanmadı.

## Yetkilendirilmiş amaç ve sınırlar

Kullanıcı HERMES'i dipten yukarı araştırmayı, kanıtla planı değiştirmeyi ve kalıcı study kaydını yetkilendirdi; 2026-09-08'de devam edip operasyonel sınıra kadar çalışmayı yeniden onayladı. Her iç kaynak grubu için yeni izin gerekmez. Hedef önce HERMES-native model, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesidir.

OpenClaw ayrı sonraki araştırma adayıdır. Kurulum, provider/model çağrısı, hesap/credential kullanımı, Codex görevi, Foundation aktivasyonu, upstream değişikliği veya benimseme bu yetkinin parçası değildir. Zararsız, offline bileşen araştırması ile bütün ürünü çalıştırma ayrılır. Yanıtlar arasında otomatik/background araştırma yapılmaz.

## Birikimli çalışma ve geçmişin korunması

1. İlk keşif pin/tree ve çalışma sınırlarını kurdu; [02 review](notes/02-BACKGROUND-LEARNING.md) notu conversation snapshot, fork, köken/guard ve pending kesitini kaydetti.
2. [03 curator](notes/03-SKILL-CURATION.md), skill bakım politikası, otomatik/LLM yolları, rapor/cron ve rollback sınırlarını ekledi. U01-C kimliği korunur; o notun H22 orta aralığına ait tarihsel 429'u current eksik okuma değildir.
3. U01B, H22/S01 tam okuması ve iki exact modülle 10 sentetik durum üretti. Önce sohbet ZIP'i olarak kalan kanıt, main `000f691...` üzerine mevcut curator içeriği korunarak yayımlandı; plan v0.4 oldu. [04 notu](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [eski deney](evidence/2026-09-07-u01b/component-probe/README.md), [aktarım](evidence/2026-09-07-u01b/PUBLICATION.md) değişmeden korunur.
4. İlk 2026-09-08 devamında pinned caller isteği iki 429 verdi; sekiz unpinned resmî belge [05 sözleşme notunu](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) ve K01–K09 planned kontrollerini üretti. V0.5 ve önceki ayrıntılı durum [a218acfc tarihsel STATE](https://github.com/batuhanozgun/agentic-os-search/blob/a218acfc20e7ece488709e00a9762166ec970fba/research/studies/hermes-agent/STATE.md) içinde recover edilebilir. Bu belge turu yeni kod/deney değildi.
5. Caller devam turu `a218acfc20e7ece488709e00a9762166ec970fba` üzerinden başladı. Path isteği yine 429 verdi; ancak aynı yetkili bağlantıda pinned Git tree → blob yolu kaynakları getirdi. [06 caller/aktarım](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md) ve [07 bellek/replay](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md) oluştu. [D kaynak defteri](evidence/2026-09-08-context-transfer/SOURCES.md) gerçek okuma derinliklerini; [yeni probe](evidence/2026-09-08-context-transfer/README.md) üç exact modüllü yedi tanılayıcı durumu taşır. Plan v0.6; yayın `29ab9b816843bab6f9e5f5b5815590fbac2b1713`.
6. Kullanıcının yazmayı yeniden deneme talebi üzerine, sohbet ZIP'inde kalan ayrı U01B2 dilimi `29ab9b8...` tabanı korunarak bu pakete eklendi. [08 U01B2 girişi](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md), [özgün teslim/kanıt](evidence/2026-09-08-u01b2/README.md) ve [yayın uzlaştırması](evidence/2026-09-08-u01b2/PUBLICATION.md). ZIP manifestinin 14 içerik girdisi byte/SHA-256 ile kontrol edildi; manifest dahil 15 özgün dosya korundu. Bu aktarım yeni deney değildir; 06/07 ve transport kanıtı ezilmedi. V0.6 planı ve ilk sonraki iş değişmedi.

Önceki notların içerikleri ve kanıtları yeni inceleme gibi sayılmaz. Birikimli kaynak otoritesi [SOURCE-LEDGER](SOURCE-LEDGER.md); D-ID'leri eski H/S/W-ID'lerini yeniden numaralandırmaz. U01B2'nin yerel B/W/D01 deney kimlikleri diğer defterlerdeki aynı harflerle karıştırılmaz.

## Yeni bulguların statüsü

**Kaynakla görülen:** Ordinary loop'ta özel bellek ve genel araç yollarından önce ortak kontrol katmanı; sıralama kararıyla thread yerleşiminin ayrılığı; ContextVar/callback ve thread-local whitelist'in farklı aktarım araçları; tool-result persistence ile completion bildirimi sırası; memory lock/reload/final-budget batch/frozen snapshot; ortak pending apply'in payload tabanlı çağrısı.

**Dar yürütme kanıtı:** UTC `2026-09-08T15:57:15.365904+00:00`, Python 3.13.5/Linux. D09/D10/D19 exact modülleri; sentetik terminal callback API, profil işareti ve allowlist. Origin/profil ve callback'ler taşınırken ayrı sentetik thread-local allowlist taşınmadı; açık worker binding duyarlılık kontrolü reddi geri getirdi. Yedi tanılayıcı beklenti karşılandı; product conformance NOT ASSESSED. Gerçek PluginManager/AIAgent/executor/profile resolver çalıştırılmadı.

**Çıkarım / açık aday:** Review thread'inde kurulan whitelist'in worker içinde görülmesi için control-context süreksizliği adayı; memory write exception'ında live-store/disk ayrışması; batch `content`/`new_text` kontrol kapsamı farkı. Bunlar tüm ürün arızası, gerçekleşmiş güvenlik olayı veya öğrenme kalitesi hükmü değildir.

**Ayrı U01B2 kanıtı:** UTC `2026-09-08T15:48:02.995262+00:00`, Python 3.13.5/Linux; S02 ve S04/H07'nin arşivdeki aynı iki modülü, sentetik adapter/reentry/config/guard/mutator ve 12 tanılayıcı senaryo. Default-name payload yeterliliği, canlı önizlem/hedef sürümü, normal hata/istisna/snapshot ve kontrollü araya-giren yazı/rollback ayrımları. Gerçek replay, üretim kilitleri veya eşzamanlılık erişilebilirliği bu deneyle doğrulanmadı. Koşu transport deneyinden ayrıdır ve yayın turunda tekrarlanmadı.

U01B'nin 2026-09-07 koşusu tekrarlanmadı. W01–W08 pin'e bağlanmamış belge olarak kalır. Güncel upstream HEAD/kurulu release, tüm UI/transport, provider, ledger/sync ve bağımsız araştırmacı doğrulaması yapılmadı. Üç ayrı deney kaydı tek toplam ürün PASS sayısına dönüştürülmez.

## İlk sonraki yetkili iş

**Gerçek ordinary executor + gerçek whitelist tüketicisi + zararsız handler ile worker sınırını birlikte doğrulamak.** 06'nın statik trace'i ve üç modüllü probe'u bir üst entegrasyon seviyesinde sınamak; önceden başka callsite'ın aynı kısıtı uygulaması veya worker-local kurulum ihtimalini dışlamadan genel bypass hükmü vermemek.

Gerekli dependency closure kurulamıyorsa sınırlı statüyü koru; bütün HERMES'i kurmaya veya provider çağırmaya sessizce geçme. Tek aday boşluk çalışma ailesini yutmasın: bu sınır kaynak/kanıtla yeterince açıklanınca aşağıdaki sıraya geç.

Ardından gerçek CLI/gateway/pending caller'da onaylayan/profil/store bağını, bellek dosyası–canlı nesne–snapshot–gönderilen istek ayrımını ve 07/M01–M02 karşı-sınamalarını ele al. Sonra ledger/backup/restore/sync, sonraki skill/cache yükleme ve U01-C curator batch raporu/cron ilişkisini birleştir. Bu pending/skill işlem çalışmalarında 08/U01B2'nin default_name üretim–staging–replay bağı ve rollback sırasında diğer yazarları dışlayan kontrol soruları da kullanılır. Kaynak bağımlılığı sıra değiştirirse kanıtı plana kaydet.

**Eski devam noktasını tekrar etme:** `run_agent.py` ilk kaynak erişimi artık aşılmıştır. H22/S01 orta aralığı zaten tam okunmuştur. Yeni oturum sırf eski not veya U01B2 teslimi öyle diyordu diye bunları ilk kez okunacak işler sanmamalı; karar taşıyan iddiada yeniden kaynak açmak ayrı iştir.

## Hâlâ açık geniş kapsam

Bütün source families'in alt envanteri; alternatif transport/caller/worker yolları; review cancellation ve shared store eşzamanlılığı; actual pending UI; curator nested batch/report; skill ledger/backup/sync; model-visible reload/invalidation; gateway/cron/provider/backend/delegation/UI; kurulum/update/CI/eval ve gelecek-task kalite. Native alt-sistem sentezleri, genel ilişkiler, dört-alan projeksiyonu ve CORE henüz yok.

## Yeni oturum girişi

Canonical agent bootstrap → research root/studies catalog → bu paketin META/STATE/INDEX → METHOD ve güncel plan → 06/07 ve D kaynak/deney defteri. U01B2 için 08 girişi → PUBLICATION → özgün not/RESULT/SPEC/probe. Önceki 02/03/04/05 notlarına incelenen mekanizmanın ilgili iddiaları için dön; onların tarihsel okuma/engel durumlarını current authority sanma. 06/07/08'in statik/deney/çıkarım sınırları full-read ile korunur.

U01B2 içindeki NOT_PUBLISHED ve v0.5/v0.6 önerileri özgün teslimin tarihsel kaydıdır; güncel durum bu STATE ve yeni PUBLICATION dosyasıdır. Yazma araçları bu denemede kullanılabildi; önceki sunum farkının teknik nedeni doğrulanmadı. Kullanıcının ZIP'i elle yüklemesi gerekmez.

Aynı görevde actual source ile derived view çatışırsa kaynağa dön. Mandatory control erişimi yoksa etkilenen çalışma durur. Diğer iş hatlarının yetkisi kendi STATE yüzeylerinde kalır. Bu yayın yalnız HERMES package ve katalog satırını etkiler; Foundation/context/Codex/control/başka study'leri değiştirmez. Bitiş ölçütü METHOD'dur; dosya veya test sayısı tamamlanma yüzdesi değildir.
