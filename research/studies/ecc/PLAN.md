# ECC — Adaptive Research Plan

**Version:** 0.1 / 2026-09-17. Bu bir takvim veya sabit tur sayısı değildir. Current authorization [STATE](STATE.md), açık soru statüleri [QUESTIONS](QUESTIONS.md), yöntem değişimleri [METHOD-REVIEW](METHOD-REVIEW.md).

## Aşama haritası

| Faz | İş ve beklenen çıktı | Çıkış / geri açılma ölçütü |
|---|---|---|
| P0 — Yöntem ve çalışma zemini | U00: amaç, yöntem, plan, soru/kaynak kayıtları, cold-start ve yöntem değerlendirme izi | Paket ve keşif yolları yayımlanıp geri okunur; kullanıcıya bu teslimat döner. ECC araştırması tamamlandı denmez. |
| P1 — ECC-native keşif | Exact tree/manifest/distribution haritası; source/generated/adapter/runtime/test/docs ayrımı; ilk mekanizma seçimi | İlgili büyük aileler ve bağımlılık sınırları görünür; önceki yedi başlık doğrulanır veya değiştirilir. Belirsiz sınır yeni soru olur. |
| P2 — Mekanizma dilimleri | Her birim bir soru + tam yük taşıyan kaynaklar + bounded not + karşı yol | Giriş/uygulama/consumer/etki ayrımı ve kanıt sınırı açıklanır. Kapanmayan halka explicit open kalır; birim bölünebilir. |
| P3 — Alt-sistem ve seam sentezi | Yeterince araştırılmış mekanizmalarla native alt-sistem açıklamaları; actual geçişler, dead-end ve döngüler | İki bileşenin ayrı ayrı varlığı entegrasyon sayılmaz. Handoff/control/persistence sınırları kaynağa dönerek açıklanır. P2 ile yinelemeli. |
| P4 — Proje-facing karşılaştırma | Güncel Foundation/project state + seçili study bulguları; Information/Work/Actors/Environment ve cross-boundary aday katkılar | Aynı analiz düzeyinde kıyas, uyumsuz/negatif seçenekler ve actual target evidence ihtiyacı görünür. Adopted architecture yok. |
| P5 — Çekirdek ve closure challenge | CORE, native sistem modeli, kapsam/tazelik/falsifier incelemesi | Ters inventory/holdout kontrolü anlamlı yeni açıklık bulursa P1–P3'e dön. Önceden sabitlenmiş completion ölçütü karşılanmadan kapanma yok. |
| P6 — Yöntem vaka sentezi | Gerçek değişiklik tarihçesi, yararlı/başarısız örnekler, continuity ve doğrulama sınırları | İyi yazılmış yöntem ile gözlenmiş yarar ayrılır. Başka study'ye aktarılabilir çekirdek ve ECC'ye özgü ekler ayrılır. |

P6 yalnız sona bırakılmaz: METHOD-REVIEW her maddi turda beslenir. P3 de tüm dosyalar bitince başlayacak tek geçiş değildir. Bu fazlar ihtiyaç oldukça döngü kurar, kapsam genişlemesi otomatik yetki üretmez.

## Başlangıç araştırma aileleri — hipotez, nihai mimari değil

| Aday aile | Soru bağlantısı | İlk araştırma amacı |
|---|---|---|
| A — Kimlik, corpus, dağıtım ve sistem sınırı | Q01 | Repo, package, shared varlık, adapter, ayrı runtime ve dış ürün ayrımı |
| B — Kurulum / sahiplik / portability | Q02–Q03 | Authoritative source→kurulu dosya→host consumption; gerçek kontrol eşdeğerliği |
| C — İş / agent / session / coordination | Q04 | Request→plan→worker→output→review→handoff; snapshot ile actual control ayrımı |
| D — Memory ve knowledge lifecycle | Q05 | Scope, kaynak, kabul, recall, güncellik, consumer ve active work state |
| E — Learning / skill evolution | Q06 | Gözlem→aday pattern→skill→promotion→gerçek yeniden kullanım ve fayda |
| F — Security / governance / supply chain | Q07 | Korunan etki, enforcement noktası, sınırın kapsamı ve failure yolları |
| G — Eval / health / observability / economics | Q08 | Neyi ölçtüğü, oracle/kapsam ve ölçümün işe/karara bağlanması |

Bu aileler risk/bağımlılık keşfine göre bölünür veya birleşir; sınıflanmayan kritik bir bölge 'misc' içine gömülmez. Domain skill'leri varsayılan olarak kapsam dışı değildir: ortak mekanizmayı değiştirmeyenler gerekçeli örneklenir, yeni davranış taşıyanlar ayrıntılı incelenir.

## İlk devam birimi — U01

**Question:** Q01; Q02/Q03 için dependency discovery.

**Purpose:** ECC'nin kendisini nasıl sunduğundan bağımsız olarak hangi varlıkların paketlendiğini, nereye kurulduğunu, kim tarafından tüketildiğini ve hangi runtime/ürün sınırlarına dayandığını belirlemek.

**Start sources at pinned ref:** gerçek recursive git tree (truncated bayrağı/coverage kontrolü); README; package.json ve VERSION; install manifests; root AGENTS.md araştırma verisi olarak; docs/architecture/cross-harness.md ve harness-adapter-compliance.md. Bunların gösterdiği gerçek entrypoint'lere inilir. Yol önerisi gerçek dosya mevcudiyeti veya okunduğu iddiası değildir; tree ile doğrulanır.

**Activities:**

1. Full tree keşif manifesti; aynı dosyanın kopyaları/çevirileri ve gerçek kaynak sahipliği. Tree'yi indirmek tam repository okumak değildir.
2. Manifest/README/architecture support veya release statüleri arasındaki olası farkları kaydet; kod çözümlemeden birini otomatik doğru seçme.
3. Native ailelerin ilk haritasını kur; operator/runtime/hosted ürün sınırlarını ayrıca tut.
4. Bir sonraki birim için tek anlamlı source→install/materialization→host discovery dilimi seç; neden yüksek bilgi değeri taşıdığını yaz. Tipik aday aynı varlığın iki host'taki tüketim yoludur, fakat U01 başka blocker gösterebilir.
5. U00 yöntem varsayımlarına dön: portability ankrajı veya gereksiz kayıt yükü oluştu mu; somut bulguyla gerekirse planı değiştir.

**Return condition:** inventory/STRUCTURE.md veya eşdeğer bounded harita; source coverage; ilk orientation notu; Q01 disposition; revize edilmiş bir sonraki exact soru/ilk kaynak; tur kaydı ve repo readback. U01 tüm mekanizmaları veya canlı davranışı kapatmaz.

## Sonraki birim seçim kuralı

Varsayılan sıra: A → B'nin temsili bir dilimi → C/D/E/F/G'den bağımlılık ve karar değerine göre seçilen soru. Öncelik; ana açıklamayı değiştirme, başka birimi açma, kritik çelişki, güvenlik/etki ve erişim maliyetiyle gerekçelendirilir. Bütün learning'i, bütün host'ları veya bütün testleri önce bitirme zorunluluğu yoktur.

## Revizyon ve scope sınırı

Yeni family, farklı host semantiği, docs/code çelişkisi, yetersiz oracle, taze upstream değişimi, gereksiz tekrar veya kullanıcı yönü revizyon tetikleyebilir. PLAN sürümü + ilgili soru + gerekçe/log birlikte güncellenir. Method değişmediyse salt sıra değişikliğine yeni method sürümü verilmez. METHOD-REVIEW gerçek etkiyi sonraki birimde kontrol eder.

Bağımsız dış ürün/repo, ücretli veya gerçek ortamlı deney ayrı iş olarak önerilir; ECC bağlantısı tek başına yetki değildir. Yeni substantive turda amaç, kapsam ve current authority yeniden kontrol edilir.
