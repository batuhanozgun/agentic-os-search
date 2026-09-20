# ECC — Okuma ve kalıcı çıkarım durumu

2026-09-20 · **B6-T17-C5b / U11-D TRANSFER-COMPLETE / C5b-PARTIAL / PACKAGE-PARTIAL**.

Bu dosya Concepts okuma ve devam durumudur. [TERMS.md](TERMS.md) kullanım girişidir; [global STATE](../../STATE.md) programın güncel işini taşır. ECC source-study ACTIVE/PARTIAL, U12-C / plan 0.29'a kadar yayımlanmış; U13-A/Q07d1 NOT STARTED. Concepts onun yeni araştırmasını başlatmaz. §3–5 önceki U11-C turunu, §7 yeni U11-D aktarımını kaydeder; current-next §6'dadır.

## 1. Kaynak ve değişmez okuma geçmişi

- Research repository: batuhanozgun/agentic-os-search.
- U11-C giriş main/snapshot: **f0d9ae31062459cf7b2cd982eaf484cbdfc336e8**; kendi önceki kapanışıyla compare-identical.
- U11-D giriş main/snapshot: **57cfd5de6eeaa3de4c5cb41ae8741ffa96c75817**; U11-C final kapanışıyla compare-identical.
- Kaynak paket: research/studies/ecc/.
- Korunan ECC package tree: **b6df4013a0f8275da82d6f27a2cd354201c5c70b**. Önceki kaynak evrenidir; giriş karşılaştırmalarında source package değişikliği yoktur. Yeni whole-package census yapılmadı.
- Ayrı upstream research pin: **affaan-m/ECC@8321021c54d670126ce3b2969d5deb880b4b0c2a**. Repository snapshot'ı upstream pin veya installed binary değildir.
- Concepts METHOD v0.3-working, SCOPE S1 ve açık post-S1 delta hesabı korunur.

**Önceki ayrıntılı okuma kayıtları silinmiş/iptal edilmiş değildir; exact checkpoint'lerinden devralınır:**

| Kapsam | Değişmez tam kayıt | Blob |
|---|---|---|
| C1–C4 / U01–U09 | [753a4c6 READING](https://github.com/batuhanozgun/agentic-os-search/blob/753a4c6696740664d359a293ee8d300a45ade6d8/concepts/studies/ecc/READING.md) | a027c7cb71f06de5355fcb4783f9a0a88d581c0c |
| C5a, U11-A/E08 ve U11-B; önceki kaynak manifestleri, düzeltmeler ve yayın geçmişi | [f0d9ae3 READING](https://github.com/batuhanozgun/agentic-os-search/blob/f0d9ae31062459cf7b2cd982eaf484cbdfc336e8/concepts/studies/ecc/READING.md) | 0c740a10a604774ce8c1df4a967a419de69c6ca5 |

Bu iki bağlantı özet değil tam eski dosyalardır. F0 kaydı U11-C'den önceki turda tam geri okunmuştu; U11-C girişinde compare-identical ve yazımdan hemen önce aynı blob doğrulandı. U11-C veya U11-D için yeni tam geçmiş okuması iddia edilmez. C6 iki tam tarihsel kaydı, bu dosyayı ve ilgili TERMS dosyalarını birlikte devralır; yalnız mevcut tabloyla package closure vermez. Önceki evidence istisnaları, kapsam açıkları ve extractor düzeltmeleri geçerlidir. Tarihsel current-next ifadeleri bugünkü iş değildir.

Önceki inventory hesabı 60 root + 27 notes + 68 evidence + 4 inventory = 159 dosyadır. Bu sayı bu tur yeniden sayılmadı ve semantik tamlık/ilerleme yüzdesi değildir.

## 2. Güncel partition ve kullanım kayıtları

| Bölüm | Concepts durumu | Kullanım kaydı |
|---|---|---|
| C1 — U01–U02 | Durable-complete, korunur | TERMS-SURFACES-INSTALLATION.md; S01–S56 |
| C2 — U03–U04 | Durable-complete, korunur | TERMS-WORK-EXECUTION-MEMORY.md; W01–W89 |
| C3 — U05–U06 | Durable-complete, korunur | TERMS-LEARNING-GOVERNANCE.md; L01–L104 |
| C4 — U07–U09 | Durable-complete, korunur | TERMS-REVIEW-RUNTIME-OPERATOR.md; R01–R176 |
| C5a — U10-A/U10-B | Transfer complete, korunur | TERMS-EVALUATION-REGISTRY.md E01–E50; TERMS-OFFLINE-CAPSULES.md O01–O69 |
| C5b — U11-A | Transfer complete, korunur | TERMS-NATIVE-REVIEW.md; N01–N77 |
| C5b — U11-B | Transfer complete, korunur | TERMS-SCHEDULED-WORK.md; SC01–SC61 |
| C5b — U11-C | Transfer complete, korunur | TERMS-REMOTE-REQUESTS.md; RD01–RD70 |
| C5b — U11-D | Bu tur transfer complete | TERMS-BACKLOG-COORDINATION.md; BC01–BC70 |
| C5b — U11-E | Sırada; gövdesi okunmadı | İlk giriş Note23/U11-E |
| C5c — U12-A/B1/B2/C | Bekliyor | Profiles/OpenCode/Python |
| C6 — package-wide reconciliation | Bekliyor | History/inventory/evidence, bütün TERMS ve delta |

Bütün kullanım kimlikleri ECC- öneki taşır. Sayılar bağımsız kavram/kanıt veya ilerleme yüzdesi değildir. C5a/b/c mevcut C5'in yürütme dilimleridir; yeni phase veya kaynak dışlama kararı değildir. **C5b bütünü, C5 ve ECC Concepts paketi tamamlanmadı.** Önceki kullanım dosyaları bu tur değiştirilmedi.

## 3. U11-C exact okuma manifesti — korunmuş kayıt

Aşağıdaki yollar research/studies/ecc/ tabanında, U11-C snapshot'ına bağlıdır. FULL yalnız bu araştırma dosyasının tamamını belirtir; atfedilen upstream dosyaların o tur okunması değildir.

| Yol | Git blob | Gerçek okuma |
|---|---|---|
| notes/21-REMOTE-INTAKE-DISPATCH-AND-RESULT-BOUNDARIES.md | 2f854ecb06772115c16a8e7b0a023b1b64ea4818 | FULL; 1–70 + 71–EOF |
| evidence/U11-C-SOURCES.md | cd6f2381455a17fde44426a73c43fbce09d56be5 | FULL; 1–100 isteği EOF'a ulaştı |
| ROUND-U11-C.md | a4540413a09855d45dfa741815e2061052251500 | FULL |
| PUBLICATION-U11-C.md | 49b523036d24050b966228c8961f72e0b3bde98f | FULL |

U11-C yeni deney içermeyen source inquiry'dir. Ayrı yeni U11-C raw run dosyası varmış gibi envanter veya sonuç üretilmedi. Eski E08/E07 veya sonraki E09 scheduling/remote deneyi sayılmadı. Evidence decode, schema rerun, test, Rust/SQL, HTTP request veya server çalıştırılmadı.

**U11-C giriş bağlamı:** Fresh AGENT aynı aea3dd845e0f0bbcfb34465edb23782e99f95c80 kimliğindeydi; aynı konuşmanın tam R01–R09 metinleri korundu. Concepts INDEX/global STATE/yerel READING/TERMS'in değişmemiş tam içerikleri önceki canonical okumalardan devralındı. CHARTER, ORIGIN, METHOD, PLAN, SETUP-REVIEW ve SCOPE o tur canonical yoldan tam geri kazanıldı. METHOD'in kesilen kısmı örtüşen aralıklarla; PLAN'ın son revizyonları 73–90 ile tamamlandı. PLAN 90–160 boş dönüşü yeni içerik okuması sayılmadı. Control dosyaları araştırma korpusuna dahil edilmedi.

Source-study META/STATE/INDEX de snapshot'tan tam okundu: sırasıyla cceb79c6f536f1e6ac12140d145ac35e4d794e1c, ed8a1fa7c7ca6fbc05c1a716f0081b92e7b630c1 ve 678e351be2ba39dda3078c74b33c4ed3cb2c8307. Bunlar source-study'nin ACTIVE/PARTIAL statüsünü ve Note22'nin exact yolunu doğrular; yeni U12/U13 gövde okuması veya source-study devam yetkisi değildir.

## 4. U11-C kaynak–kayıt kontrolü — korunmuş kayıt

[TERMS-REMOTE-REQUESTS.md](TERMS-REMOTE-REQUESTS.md) **ECC-RD01–RD70** kullanım/ilişki kaydı içerir. Her satır note bölümü ve K/Y/T/H rolüyle bağlanır; §9 kaynak tarafındaki bölümlerden kayıtlara dönüşü ve önceki kayıtlarla ilişkiyi taşır. Türkçe karşılıklar extractor paraphrase'idir. Kaynak yorumu, tarihli dış sözleşme, incelenmiş test ve Concepts okuması eşitlenmez.

Başlıca ayrımlar:
- HTTP intake, kalıcı request, ayrı dispatch ve accepted task output farklı sınırlardır.
- Target session lead olabilir; gerçek alıcı result_session_id ile ayrı tutulur.
- Successful SET NULL referential integrity'yi korurken never-targeted/target-disappeared ayrımını kaybedebilir. Fresh read ve önceden tutulmuş Some snapshot farklı sonuç yollarıdır.
- Valid profile name, reused delegate'in effective policy'si değildir; yeni-session profil uygulaması pozitif karşılıktır.
- Request priority ve handoff priority farklı consumer aşamalarındadır.
- DeferredSaturated current outcome iken persistent request Pending kalır; Failed sonraki pending seçiminden dışlanır.
- Kalıcı routing result ve per-item failure isolation vardır; scheduler'ın timestamp-only ve first-error sonuçları remote'a taşınmaz.
- Read marker, alıcı acknowledgment'ı ve verified output ayrı tutulur.
- source=http etiketi testin network/authentication testi olduğu anlamına gelmez.

U11-C turunda kaynak ile önceki kullanım kayıtları arasında onları yeniden yazmayı gerektiren maddi çelişki saptanmadı. Yeni counterpart'lar ayrı RD kimlikleriyle kaydedildi. Koşullu target-deletion, resource-blocking ve competing-dispatch örnekleri observed incident veya yeni deney diye yükseltilmedi. Pozitif token/input/profile checks, result linkage ve failure isolation kaybolmadı.

İki risk sürer: Batu okuma anındaki anlam seçimlerini denetleyemediği için dayanak/yorum/belirsizlik izlenebilir olmalıdır; aynı sözcük ortak anlamı veya teknik doğruluğu garanti etmez. Kaynak kullanımı, araştırmacı/extractor yorumu ve kullanıcı onayı birbirinin doğrulaması değildir. U11-C'deki somut karşılık acceptance/dispatch/completion ile lead/receiver ve None kökenlerinin ayrı gösterilmesidir.

## 5. U11-C yayın ve kontrol sınırı — korunmuş kayıt

- Yeni TERMS commit: **26e5381d10c8153e55ef65f1f8b1e22a9a827a42**.
- Geri okunan blob: **59e50f2af1fa8933fa1213589ff9ae6f956bf884**.
- Tam readback: **1–55, 56–110, 111–EOF**. RD01–RD70 satırları ve kaynak/sınır bölümleri görünür içerikten kontrol edildi.
- Local READING: **07e15e8e4b454222ac15f0de3b1d3261fe9a5b38**, blob **ec1a62d6424627dc8e4d6ab6b71809e50fdead92**.
- TERMS router: **44c1b0ac17e0d38cc01b545882b7c4c4a5c48405**, blob **0e6ff571580d911145c464e318c1b7d92e07620f**.
- Final STATE/main/readback: **57cfd5de6eeaa3de4c5cb41ae8741ffa96c75817**. Dört commit/dört Concepts path kapsamı kontrol edildi; yeni U11-D giriş karşılaştırması aynı checkpoint'i doğruladı.

Bu, aynı assistant'ın kaynak-kayıt/readback kontrolüdür. Otomatik tüm-repo ID/link suite'i, bağımsız aktör incelemesi veya yerel tam-byte/hash-match iddiası yoktur. U11-C turunda raw download denenmedi; önceki araştırmadaki DNS/payload hataları güncel hata diye tekrarlanmaz.

Önceki ayrıntılı okuma kayıtları §1'deki immutable sürümlere bağlanarak current yüzeyden ayrıldı; eski TERMS veya kaynak dosyaları değiştirilmedi. U11-C'nin chronological future-readback ifadeleri o kapanışın tarihidir; yeni publication-repair işi değildir.

## 6. Exact next ve açık kapsam

**B6-T17-C5b / U11-E:** research/studies/ecc/notes/23-TEMPLATE-RESOLUTION-AND-LAUNCH-COMPOSITION.md → evidence/U11-E-SOURCES.md → ROUND-U11-E.md → PUBLICATION-U11-E.md; bağlı evidence kendi gerçek kapsamıyla devralınır. Yol önceki tam source INDEX ve U11-D handoff'uyla bağlıdır; Note23 gövdesi bu tur okunmadı. Sonra C5c/U12-A/B1/B2/C.

C6; bu dosya ve §1'deki iki tam tarihsel READING, kalan master-history/inventory/evidence hesapları, bütün ECC TERMS, kaynak delta'sı ve paket geneli source-to-record/ID/role tutarlılığını kapsar. Post-S1 eklemeler agentmemory, claude-swap, cli-continues, ponytail B7 öncesi global kapsam hesabına alınacaktır. U11-C Q04e2b ve U11-D Q04e3b stronger runtime/authority/concurrency/recipient-acceptance soruları Concepts tarafından çözülmedi ve otomatik yeni deney borcu değildir.

U11-A/E08, U11-B, U11-C ve U10 tamamlanmış aktarım olarak korunur. E06 excluded, iki E05 geçmişi ve E04/E07/E08/E09 kendi scope'larında kalır. B7/B8, Foundation/SOUL/Development OS mimarisi ve source-study U13-A bu checkpoint'in işi değildir.

## 7. U11-D gerçek okuma, aktarım ve yayın hesabı

### 7.1 Preflight ve kaynak manifesti

Giriş **57cfd5de6eeaa3de4c5cb41ae8741ffa96c75817 → main identical**. Fresh AGENT aea3dd845e0f0bbcfb34465edb23782e99f95c80 ile aynıydı. R06 canonical tam metni yeniden alındı: 91a07c45e6956ba51b89dc81d45b25e30a2afc38. Diğer gerekli protokollerin ve Concepts INDEX/STATE/CHARTER/ORIGIN/METHOD/PLAN/SETUP-REVIEW/SCOPE, yerel READING/TERMS ve ECC META/STATE/INDEX'in aynı konuşmadaki tam, değişmemiş canonical içerikleri korundu. Yeni oturum veya bütün geçmişi yeniden okuma iddiası yoktur. Control dosyaları araştırma korpusuna katılmadı.

Aşağıdaki dört mevcut dosya research/studies/ecc/ altında, U11-D giriş snapshot'ına bağlıdır:

| Yol | Git blob | Gerçek okuma |
|---|---|---|
| notes/22-BACKLOG-COORDINATION-AND-CONSUMPTION.md | 261d6fc497f3ec608a883f3ebf919671ed7b7f23 | FULL; 1–80 + 81–170 isteğiyle EOF |
| evidence/U11-D-SOURCES.md | 33b057b0c14dad46820b4b19b95640cd74fe6988 | FULL; 1–100 isteğiyle EOF |
| ROUND-U11-D.md | c554edb1f5803afad8b6fe9bc67cb0395152c505 | FULL; 1–130 isteğiyle EOF |
| PUBLICATION-U11-D.md | 691d618f237578cccf304c5d2cfdedb72a051ca5 | FULL; 1–130 isteğiyle EOF |

FULL bu research dosyalarının okunmasıdır; ledger'ın anlattığı upstream full/selected/retained/test okumaları Concepts tarafından yeni yapılmış sayılmaz. U11-D source-only inquiry'dir; ayrı yeni E09/raw run varmış gibi dosya veya sonuç üretilmedi. Mevcut E08/E07 veya sonraki Python E09 yeniden koşulmadı; yeni experiment, source test veya model/provider çağrısı yoktur.

### 7.2 Kullanım ve kaynak tarafından kontrol

Yeni [TERMS-BACKLOG-COORDINATION.md](TERMS-BACKLOG-COORDINATION.md): **ECC-BC01–BC70**. Kaynak §1–8 kullanım kayıtlarına geri eşlenmiş, K/Y/T/H rolü ve koşullu/observed ayrımı korunmuştur. Note, ledger, method round ve publication receipt birbirinden bağımsız ürün kanıtları sayılmaz.

Temel aktarım ayrımları: message/routing attempt/session/accepted task; unread recipient/declared lead role; launch arguments/companion handoff; repeated forwarding/decomposition; drain routing guard/rebalancer destination inequality; all-unread/task-handoff load; post-effect marker/exclusive claim; persistent cooloff/timed backoff; current capacity/historical inhibition; routing pressure/accepted deliverable; shown inbox set/marked incoming set.

Source-side kontrol yalnız kusur aramadı: default automation off, DeferredSaturated'da unread retention, per-candidate state reread, from_session guard ve positive rebalance/recovery yolları da korundu. Tekrar-delegasyon automation/admission/no-intervening-consumer koşullarıyla taşındı; infinite-growth veya incident rate iddiasına yükseltilmedi. Cooloff ve rebalancer interleaving'leri yeni deney sonucu değildir. Manager/daemon testleri routing/marker/closure oracles ile sınırlıdır; canlı tüketim veya çok-döngülü iyileşme kanıtı sayılmaz.

Önceki RD64/RD65 daha ayrıntılı BC62/BC63 ve BC11/BC18/BC27'ye bağlandı; RD56 remote failure isolation BC40 backlog loop'una taşınmadı. Önceki TERMS'i yeniden yazmayı gerektiren maddi çelişki saptanmadı. Yeni dosyanın ilk source/readback kontrolünde kayıt ayırma düzeltmesi gerektiren maddi hata saptanmadı; sırf önceki turlarda düzeltme yapılmış diye yeni sorun üretilmedi. Açık native enum adı verilmeyen absorbable-backlog ifadesine dışarıdan isim atanmadı.

### 7.3 Gerçek yayın ve sınırı

Yeni TERMS commit: **b9343fd9fc23c67131b00a974e4abf1fd6902fe1**. Tam readback blob: **05b33fd9cac4b6dfd69bf980b937d65060ed73df**; **1–65 / 66–125 / 126–210 üzerinden EOF**. Yetmiş kullanım satırı ve §10–12 kaynak/ilişki/sınır bölümleri doğrudan görüldü. Bu adresleme kontrolü otomatik tüm-repo ID/link suite'i veya bağımsız semantik doğrulama değildir.

TERMS sonrası b9343fd→main compare-identical bulundu; bu READING/router/global STATE yazılarından önce intervening değişiklik yoktu. Final main/ref/diff ve entry readback bu güncellemelerden sonra yapılır; kendi gelecekteki hash veya yapılmamış doğrulama uydurulmaz. Bu tur raw indirme, local full-byte/hash-match, code execution veya bağımsız aktör kontrolü iddiası yoktur.

U11-D source-local aktarımı kapanır; **C5b'nin U11-E bölümü, C5c, C6 ve B7/B8 açıktır**. Q04e3b'nin actual repeated-run/host/OS, task/message identity/uptake/acceptance, concurrency/cancellation/fairness, leaf/termination, cooloff recovery/observer freshness ve custom-consumer soruları kaynak araştırmasında açık kalır.
