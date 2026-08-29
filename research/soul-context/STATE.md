# SOUL Context — STATE

**Durum:** AÇIK  
**Faz:** 7 — SOUL Research ↔ SOUL architecture research boundary  
**Son güncelleme:** 2026-08-29

## Ana hedef

Üç kaynak repoyu sistematik okuyarak SOUL Research projesinin gerçek araştırma niyetini yeniden kurmak; erken mimari çözüm üretmemek.

## Kaynak repoların güncel rolleri

- `soul`: **birincil SOUL intent + Development OS + work/verification evidence**. Default `main` minimaldir; yüksek-bilgi kaynak `phase0/development-os` ve seçili work/review dallarıdır.
- `os-architect`: tarihsel arıza, yöntem, araştırma, sahip düzeltmeleri ve KEEL'in üst-seviye yeniden değerlendirilmesi.
- `keel`: somut mekanizma/runtime yüzeyi; tarihsel iddiaların bugünkü mekanik karşılığını sınamak için.

## Önemli düzeltme

Önceki `soul` değerlendirmesinde "repo küçük / yalnız README" hükmü yalnız default `main` dalına dayanıyordu. Dal taraması çok sayıda work/verify/review/audit dalı ve `phase0/development-os` dalını ortaya çıkardı.

Bu omission maddi olduğu için eski repo-geneli çıkarım geçersizdir. `repos/soul/README.md` güncellendi.

## Tamamlanan araştırma geçişleri

### A — çalışma düzeni ve araştırma yöntemi

Doğrulandı:
- depo/temsil failure'ı,
- çalışma-döngüsü failure'ı,
- epistemik süreç failure'ı.

### B — KEEL problem ve kanıt modeli

Kanıt statüleri ayrıldı:
- gözlenen arıza,
- ölçüm/tatbikat,
- tasarım hükmü,
- dış yakınsama.

### C — önceki araştırma ve dış-göz kayıtları

Doğrulandı:
- soru ≠ görev,
- amaç/öncül yeniden türetme ihtiyacı,
- uzman–sahip asimetrisi,
- session context'in sonuç taşırken amaç/neden kaybetmesi,
- sorgulama için `üreteç + tetik + kanıt zinciri`,
- ders→ihtiyaç köprüsü problemi.

Sınır: geçmiş altı kalemlik programın yalnız 1, 2 ve 6 repo ayağı tamamlanmış; 3–5 araştırılmış sayılmıyor.

### D — KEEL mekanik karşı-okuma

Seçici kod/sözleşme/test okuması doğruladı:
- fail-closed state/order parser,
- gerçek Claude Code hook wiring,
- role/write cage,
- salt-okur verifier yüzeyi,
- fresh card / fail-visible closure,
- mutation-test definitions,
- kısmi lesson→need işaretçi mekanizması.

Sınır: fresh execution bu oturumda üretilemedi; test tasarımı ile güncel pass ayrı tutuluyor.

### E — KEEL → SOUL geçişi

#### os-architect tarihsel pivot

2026-08-08..13 kayıtlarında problem ürün-bug seviyesinin üstüne çıktı:
- mekanizma gerçekten gerekli mi / doğru katmanda mı,
- sistem sahibini amacına taşıyor mu,
- koltuk-içi akıl güçlü iken koltuk-üstü akıl sahipsiz mi,
- gate biçim ölçerken değer/uyum/geçen-zaman ölçülüyor mu,
- owner hidden orchestrator oluyor mu,
- doğru ders ihtiyaç anında çağrılıyor mu,
- root cause yalnız mekanik kusur değil danışmanın framing/çalışma biçimi olabilir mi.

2026-08-11 kaydı: `araştırma evi kurulacak`; araştırmalar sonraki yeni geliştirme çalışmasına girdi olacak. Bu yön beyanıdır, formal D-kararı değildir.

`os-architect` 2026-08-13 sonrası 25 Ağustos'a kadar commit taşımaz; exact launch/naming kararı bu repodan tek başına çıkarılamaz.

#### SOUL birincil kaynakları

`phase0/development-os` branch'inde okundu:

- `development/README.md`
- `00_foundation/VISION.md`
- `DEFINITION.md`
- `NON_NEGOTIABLES.md`
- `SUCCESS_CRITERIA.md`
- `04_work/WP-000-DEVELOPMENT-OS.md`
- `04_work/WP-001-PHASE0-VERIFICATION.md`
- `06_reviews/VERIFICATION-WP-000-2026-08-25.md`
- `05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`

## Artık birincil kaynakla doğrulanan SOUL amacı

### Ürün

SOUL preset workflow/team/template değil. Temel işi **system formation**:

1. intended outcome'u anlamak,
2. gereken working system'i belirlemek,
3. gereken capability'leri yaratmak/organize etmek,
4. sistemi outcome'a doğru işletmek,
5. progress/correctness doğrulamak,
6. assumptions gerçeklikle bozulduğunda adapt etmek,
7. continuity/governance/state'i zaman içinde korumak.

### Development OS

SOUL'u geliştirirken SOUL'un kontrol etmeyi amaçladığı aynı agentic failure class'ları yeniden üretmemek için ürün mimarisinden önce durable repository-based development OS kuruluyor.

WP-000 açıkça şunları non-scope yapıyor:
- complete capability architecture,
- implementation technology choices,
- KEEL folder mapping,
- runtime code.

Yani "first principles" yalnız söylem değil; mevcut çözümü ürün mimarisine erken taşımamaya dönük scope control.

## İlk Development OS verification sonucu

WP-001 fresh verifier, exact commit'e karşı WP-000'ı değerlendirmiş ve overall `FAIL` vermiş.

FAIL nedenleri:

1. cold-start mandatory read order'ları birbirleriyle uyumsuz;
2. `NEXT_SESSION.md` current WP bilgisini stale duplicate olarak taşıyor ve canonical `STATE.md` ile drift ediyor.

Dokuz başka kriter PASS olsa da iki mandatory kriter FAIL olduğu için overall FAIL korunmuş. Verifier repair yapmamış; changed target için yeni verifier zorunlu.

Bu, independent/fail-visible verification'ın yalnız manifesto olmadığını gösteren doğrudan davranış kanıtıdır.

## Öncül repo → SOUL bağlantısı artık doğrudan kanıtlı

`REASONING-POLICY-SYNTHESIS-2026-08-26.md`, KEEL-Work, keel-dev, oyun2, os-architect ve keel-research kaynaklarını blob SHA'larıyla listeliyor.

Kaynaklardan türetilen recurring principles ile SOUL-specific synthesis decisions ayrı tutuluyor.

Doğrudan taşınan problem/principle sınıfları arasında:
- external project truth,
- objective/method/state/evidence/authority separation,
- observation/inference/assumption/verification ayrımı,
- producer/tool/retrieval/repeated-model agreement'ın proof olmaması,
- existing mechanism/plan/tool'un privileged default sayılmaması,
- framing/necessity/alternative-layer/falsification,
- owner value vs technical authority,
- proximal + root-cause failure analysis,
- observable/mechanical controls,
- proportional deep reasoning,
- exact-target verification freshness
var.

SOUL bunları klasör/ritüel olarak kopyalamıyor; yeni canonical reasoning/cold-start/governance synthesis'e dönüştürüyor.

## Bağımsız sentez notu

`research/soul-context/notes/transition-to-soul.md`

Bu not doğrudan kanıt, kaynak boşluğu ve halen çıkarım olan SOUL Research amacı ifadesini ayrı tutuyor.

## SOUL Research amacı için mevcut en güçlü çalışma hükmü

### Doğrudan kanıtlanan arka plan

SOUL, KEEL'den daha genel bir probleme yöneliyor: herhangi bir intended outcome için doğru controlled working system'i oluşturmak ve işletmek.

SOUL'un kendi development process'i ürün mimarisini erken kapatmamak; chat memory/self-certification/framing drift gibi failure'ları kendi içinde yeniden üretmemek için önce kontrol altına alınıyor.

### Güçlü fakat hâlâ çıkarım olan SOUL Research amacı

SOUL Research projesi büyük olasılıkla, SOUL mimarisine girecek **genel problem modelini ve kanıt tabanını** üretmek için ayrı tutuluyor:

- KEEL'e özgü mekanizmaları evrensel gereksinim sanmamak,
- mevcut araç/runtime affordance'larının mimariyi belirlemesini önlemek,
- aynı model/çerçevenin sahte yakınsamasını azaltmak,
- tarihsel dersleri first-principles genellenebilirlik testine sokmak,
- dış literatür/alternatif sektör/mimari evidence ile challenge etmek,
- sonunda SOUL architecture work'ün kullanabileceği durable research artefacts üretmek.

Bu ifade henüz kaynaklarda bulunan verbatim bir `SOUL Research charter` değildir; direct SOUL foundation + predecessor evidence chain + bu projenin kullanıcı tarafından tanımlanan araştırma rolünden çıkarılan en güçlü çalışma hükmüdür.

## Şimdi — F geçişi: research → architecture boundary

En yüksek bilgi değerli soru:

**SOUL product-development repo'su dış araştırma/evidence'i architecture kararlarına hangi sözleşmeyle sokuyor ve hangi araştırma boşluklarını açık bırakıyor?**

Öncelik:

1. `phase0/development-os` içinde yalnız reasoning/adversarial work packages'tan yeni failure class üreten kayıtları oku (`WP-005` ve ilgili re-verification/adversarial result girişleri).
2. `development/01_governance` içinde evidence/research → decision sınırını taşıyan policy'leri seçici oku.
3. Sonraki capability/failure architecture work'ün external research/evidence yükümlülüklerini haritala; bütün work branch'lerini tüketme.
4. Bir verbatim SOUL Research charter / separate research boundary bulunursa mevcut çıkarım onunla revize edilir.

## Yeni oturumda devam

1. Fresh canonical `AGENT.md` ve routing protokolleri.
2. `research/soul-context/README.md`.
3. Bu `STATE.md`.
4. `research/soul-context/notes/transition-to-soul.md`.
5. `research/soul-context/repos/soul/README.md`.
6. F geçişinin ilk yüksek-bilgi dosyasından devam.

## Henüz yapılmaması gerekenler

- SOUL mimarisi önermek.
- KEEL mechanisms = SOUL requirements eşitliği kurmak.
- second-order literature summaries'i primary evidence saymak.
- same-model verifier'ı true independent ground truth saymak.
- `SOUL Research'ün amacı kesin olarak X` demek; verbatim charter bulunana veya alternative frame'ler kapanana kadar çalışma hükmü olarak tut.
