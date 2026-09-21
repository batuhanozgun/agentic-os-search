# ECC — Bağlamlı kullanım kayıtları

2026-09-21 · **B6 / C1–C4-DURABLE-COMPLETE / C5a-COMPLETE / C5b-COMPLETE / C5c-U12-COMPLETE / C5-U10–U12-COMPLETE / PACKAGE-PARTIAL / C6-NEXT**.

Bu dosya research/studies/ecc/ Concepts kullanım girişidir. Gerçek dosya/sürüm ve okuma kapsamı [READING.md](READING.md), program yetkisi [global STATE](../../STATE.md) içindedir. ECC source-study ayrı ACTIVE/PARTIAL çalışmadır; son gözlenen kaynak STATE U13-A'yı complete ve U13-B'yi in progress gösteriyordu. Güncel source yetkisi kendi STATE'inden alınır; Concepts kaynak araştırmasını yürütmez. Yeni U13 materyali READING §6/C6 delta hesabındadır.

## 1. Bağlı kullanım dosyaları

| Kaynak ailesi | Bağlamlı kullanım kaydı | Aktarım durumu |
|---|---|---|
| U01–U02 / C1 | [TERMS-SURFACES-INSTALLATION.md](TERMS-SURFACES-INSTALLATION.md), S01–S56 | Complete |
| U03–U04 / C2 | [TERMS-WORK-EXECUTION-MEMORY.md](TERMS-WORK-EXECUTION-MEMORY.md), W01–W89 | Complete |
| U05–U06 / C3 | [TERMS-LEARNING-GOVERNANCE.md](TERMS-LEARNING-GOVERNANCE.md), L01–L104 | Complete |
| U07–U09 / C4 | [TERMS-REVIEW-RUNTIME-OPERATOR.md](TERMS-REVIEW-RUNTIME-OPERATOR.md), R01–R176 | Complete |
| U10-A / C5a | [TERMS-EVALUATION-REGISTRY.md](TERMS-EVALUATION-REGISTRY.md), E01–E50 | Complete |
| U10-B / C5a | [TERMS-OFFLINE-CAPSULES.md](TERMS-OFFLINE-CAPSULES.md), O01–O69 | Complete |
| U11-A / C5b | [TERMS-NATIVE-REVIEW.md](TERMS-NATIVE-REVIEW.md), N01–N77 | Complete |
| U11-B / C5b | [TERMS-SCHEDULED-WORK.md](TERMS-SCHEDULED-WORK.md), SC01–SC61 | Complete |
| U11-C / C5b | [TERMS-REMOTE-REQUESTS.md](TERMS-REMOTE-REQUESTS.md), RD01–RD70 | Complete |
| U11-D / C5b | [TERMS-BACKLOG-COORDINATION.md](TERMS-BACKLOG-COORDINATION.md), BC01–BC70 | Complete |
| U11-E / C5b | [TERMS-TEMPLATE-LAUNCH.md](TERMS-TEMPLATE-LAUNCH.md), TL01–TL74 | Complete |
| U12-A / C5c | [TERMS-EXECUTION-PROFILES.md](TERMS-EXECUTION-PROFILES.md), EP01–EP84 | Complete |
| U12-B1 / C5c | [TERMS-OPENCODE-CALLBACKS.md](TERMS-OPENCODE-CALLBACKS.md), OC01–OC92 | Complete |
| U12-B2 / C5c | [TERMS-OPENCODE-INSTALLATION.md](TERMS-OPENCODE-INSTALLATION.md), OD01–OD91 | Complete |
| U12-C / C5c | [TERMS-PYTHON-PROVIDERS-AND-TOOLS.md](TERMS-PYTHON-PROVIDERS-AND-TOOLS.md), PY01–PY108 | Bu tur complete; C5c/C5 kaynak-aile aktarımı kapandı |

Bütün kimlikler ECC- öneki taşır. Bunlar kullanım adresleridir; bağımsız kavram, kanıt veya ilerleme yüzdesi değildir. Bağlı dosyalardaki tarihsel PARTIAL/next ifadeleri kendi checkpoint'lerine aittir. Current aktarım durumu burada ve READING'dedir. Bu tablo paket-geneli C6 coverage hükmü değildir.

## 2. Package-level expressions — korunur

| ID / ifade | ECC araştırmasındaki kullanım | Sınır |
|---|---|---|
| ECC-P01 — ECC | Procedural assets, install/distribution, work/runtime, memory/learning, evaluation and governance surfaces taşıyan external target. | Tek uniformly integrated runtime olarak varsayılmaz. |
| ECC-P02 — source surface | Repo'daki authored/configured mechanism surface. | Installed/live/effective behavior değil. |
| ECC-P03 — mechanism slice | Bounded trigger→selection→effect→acceptance/failure chain araştırma birimi. | Whole subsystem veya whole product değil. |
| ECC-P04 — bounded source answer | Exact pinned source + declared evidence class altında answered question. | Product-wide/current empirical closure değil. |
| ECC-P05 — local execution | Exact isolated fixture'da unchanged source behavior observation. | Live host/model/product validation değil. |
| ECC-P06 — source-derived counter-path | Multiple code paths together imply a reachable contrast/failure condition. | Observed production incident değil. |
| ECC-P07 — evidence class | Target claim/source observation/test inspected/local execution gibi claim-strength qualifier. | Tek eksenli confidence score değil. |
| ECC-P08 — installed ≠ discoverable ≠ selected ≠ followed ≠ effective | ECC METHOD'in recurring distinction. | Universal ontology değil; source-study methodological boundary. |
| ECC-P09 — recorded ≠ accepted | Stored/report state ile governance/work acceptance ayrımı. | Every record untrusted demek değil. |
| ECC-P10 — test-green ≠ valid oracle | Passing/expected test result'in measured claim'e uygun oracle olma gereği. | Tests useless demek değil. |

## 3. Current-next ve kapanış sınırı

**U12-C aktarımı, mevcut E09'un read-only ham kayıt incelemesiyle tamamlandı. C1–C4 ile başlangıçta tanımlanmış C5/U10–U12 kaynak-aileleri complete. Exact next: ECC C6 — paket geneli reconciliation. ECC Concepts paketi PARTIAL.**

C6, READING'deki **yedi tam tarihsel manifest + current kayıt**, bütün ECC TERMS, kalan root/master-history/inventory/evidence ve **eşzamanlı U13-A/U13-B/sonraki source delta** hesabını devralır. Yeni kaynaklar eski C1–C5 planında adı yok diye dışlanmaz. Önce fresh canonical source state ve tam current file manifest alınır; eski 159-file baseline current census sayılamaz. Bu, ECC teknik araştırmasına veya B8 ortak kavram kabulüne geçiş değildir.

B7 geçmeden B8 başlamaz. ECC package closure sonrasında seri sıradaki paket work-management-project-control'dür. Post-S1 agentmemory/claude-swap/cli-continues/ponytail kapsamı B7 öncesi ayrıca hesaplanır.

## 4. Önceki ilişki ve düzeltmelerin tam kaydı

U12-B1 kapanışına kadarki geniş ilişki yönlendirmeleri [5852459 TERMS'in tam sürümünde](https://github.com/batuhanozgun/agentic-os-search/blob/5852459c9dc273f3b7aa2911978883424cd5aca7/concepts/studies/ecc/TERMS.md), blob **c4f11c6b2e076b25b8f2e1d021e9ac9a8e652ccd**, korunur. B2 kapanışındaki tam router da [592b11b TERMS](https://github.com/batuhanozgun/agentic-os-search/blob/592b11bd726fd39e84e53098507cf5b1a60d92e3/concepts/studies/ecc/TERMS.md), blob **853822149439da418dc4f48d3b008f2221182458** olarak korunur. Bunlar C6 girdileridir; tarihsel next ifadeleri bugünkü işi belirlemez. Önceki tüm kullanım dosyaları ve yorum/düzeltme bölümleri yerinde, değişmeden durur.

Geri çağırma noktaları: O03 capsule/O69 journal; N21 trigger/N76 security dimension ve N32/N77 kaynak eksenleri; SC47 finite schedule/SC61 terminal handling; TL38 slots/TL74 refusal, TL50 completion/TL73 accepted output ve TL72 warning; EP29/EP84 host izinleri ve EP33/EP83 program/base_args. Kaynak gerekçeleri ve etki hesapları ilgili TERMS dosyalarındadır. OC25/OC55 code-span düzeltmesi biçimseldir; MR26'nın static-import şüphesini bırakması OC75'te tarihsel araştırmacı değişimidir.

Aynı sözcükten ortak mekanizma türetilmez: skill/Rust/Node evaluation; session-state/registry transaction; scheduler/remote/backlog error continuation; template creation/delegate reuse; profile selection/native/text/control enforcement kendi consumer ve evidence kapsamlarında kalır. Bu router tam ilişki kaydı veya source evidence yerine geçmez.

## 5. U12-B2 ilişkileri — korunur

OD kayıtları package contents/selected entry, compiled payload/source-plugin route, recorded consent/classifier coverage, file-origin/export identity, trusted-root/canonical-legacy role, successful write/surviving payload ve inventory/command/report/query/scan ayrımlarını taşır.

OC82–OC87 preparation helper'ının çağrılma sorusu OD13'te actual registry caller'a bağlandı; yine transitive import veya callback uyumu sertifikası değildir. OC88–OC92 materializer/package açıklıkları OD01–OD25 ile tamamlanır. OC07 barrel, OD35–OD38 ayrı-origin factory ilişkisiyle birlikte okunur. OC46'nın çalışan after-hook'u, declined consent kapsamında kalabilen plugin ve duplicate-origin örnekleri için anlamlı conditional consumer'dır; OC21/OC24 replacement-output bulgusu değişmez.

OC11'in dependency-analyzer registration işareti OD61–OD69/OD91 ile implementation/output anlamına kavuşur. Plugin map'inin iki kaydı bütün sekiz doğrudan tool/barrel kataloğuyla aynı küme değildir. OD70–OD72 command recommendation, OD73–OD75 mevcut report comparison, OD76 gerçek Git query implementation ve OD80 bounded scan olarak ayrı tutulur. Default sıfır ölçülmüş sıfır değildir; OD78 hata-boşluğu OD79 clean hükmünü daraltır.

OD17 materialization filtresi ile OD90 .npmignore, OD65 success:true ile OD91 öneri metni ilk remote yayından önce ayrı adreslenmişti. O tur eski TERMS'i değiştiren maddi düzeltme veya yeni host/build/installation/deney yapılmamıştı. B1/B2/installed/current sınıfları ayrı; Q02b3/Q03c açık kalır.

## 6. U12-C'nin yeni kullanım ve ilişki sınırları

PY01–PY21 selector/provider/model yollarını ayırır. PY14 saved LLM_MODEL, PY20 input.model veya PY21 provider default'un yerine geçmez. PY34/PY37 optional prompt/template yardımcıları, PY05/PY06 gerçek generate/loop caller'larının zorunlu adımları değildir.

PY42 ilk-request tool-definition conversion, PY43 response normalization ve PY52–PY59 next-request history conversion farklı sorumluluklardır. Yerel normal tool round trip PY72, native SDK/API acceptance'ı kanıtlamaz. PY60 registry, PY62 advertised list, PY65/PY66 schema/strict beyanı ve PY67 Python invocation ayrı kabul yüzeyleridir; PY64 unknown-name refusal gerçek olumlu kontrol olarak kalır.

PY74 iteration limit, son effect'i engelleyen bir sınır değildir: PY75'te araç etkisi oluşur, PY76'da loop sentetik limit çıktısı verir. PY78 sonradan provider exception ve PY79 fresh retry, durable/idempotent continuation değildir. PY81 text/id retention ile PY82 structural error field kaybı birlikte korunur; bütün hata bilgisinin yokluğu söylenmez.

Ham E09'dan görülen PY66 strict:true yerel executor şema kontrolü; PY83 accepted scripted result gerçek iş kabulü; PY80 no_internal_retry ise bütün SDK davranışı olarak okunmadı. PY103 sekiz predeclared karşılığın tek run'da uyuşmasıdır; bağımsız sekiz doğrulama veya ürün başarı oranı değildir. PY101/PY102 iki-field checker/corrected fixture, API deneyi değildir.

PY19/PY106 normalization/refusal, PY31/PY107 ModelInfo/list_models ve PY47/PY108 global/CN ilk yayın öncesi ayrı adreslendi. Önceki TERMS dosyalarını değiştirmeyi gerektiren maddi çelişki saptanmadı. Kaynak bağlantıları, sekiz vaka hesabı ve açıklama rolleri yeni dosyanın §12–§13'ündedir. E09 carrier recovery, byte/CRC/member kontrolü ve ham içerik okuması yeni target execution sayılmaz; Q02c2'nin installed/remote/authority/recovery/accepted-outcome sınırları açıktır.

## 7. İki risk

Batu okuma anındaki anlam seçimlerini denetleyemediğinden dayanak, yorum, belirsizlik ve maddi değişim izlenebilir olmalıdır. Ortak sözcükler ortak anlamı garanti etmez; kaynak kullanımı, araştırmacı/extractor açıklaması ve kullanıcı onayı teknik doğruluk bakımından ayrı kalır. U12-C'deki somut ayrım, recorded preference/consumed field ile strict/accepted/retry etiketlerinin actual consumer kapsamlarıdır. B8 ortak tanım veya mimari kabulü yapılmadı.
