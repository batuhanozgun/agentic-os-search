# U08 — Yayın ve geri okuma makbuzu

**2026-09-12 / CONTENT PREPARED — REF/READBACK NOT YET VERIFIED.** Bu başlık gerçek main geri okumasından sonra güncellenecek; tree/blob oluşturmak yayın değildir. [STATE](../../STATE.md), [RESEARCH](RESEARCH.md), [MANIFEST](MANIFEST.json).

Yayın tabanı `4c372138b7d652b1921e96ef9158b32b05c05fc8`. Native compare, U07 yayın makbuzundan iki commit ileri ve yalnız Foundation yollarında değişiklik gösterdi; o değişiklikler korunur. Kullanıcı önce U08 yayınını doğrulamayı, sonra kayıtlı araştırmaya devamı onayladı. Bu checkpoint yeni davranış koşusu değildir.

Özgün ZIP SHA-256 `4a1eda333c689efe90f51d34822bb0d2e3daa29f829337d79a83b851ab1de0ca`. Read-only validator 21 aday dosyayı, altı baseline kopyasını, 12 ham arşiv üyesini ve source/SPEC/probe/RESULT/effect bağlarını doğruladı. HERMES probe'u yeniden çalıştırılmadı. Raw manifest/ARTIFACT-CHECKS ve source metinlerindeki local/not-published alanları ilk teknik turun tarihsel kaydıdır; güncel yayın hükmü bu üst bölümdedir.

---

## İlk U08 girişimi — özgün tarihsel kayıt

Aşağıdaki yayın yokluğu ve capability cümleleri ilk teknik tura aittir. Özgün araştırma ve deney kimliklerini değiştirmez.

# U08 — Yerel teslim ve gerçek repository durumu

**2026-09-12 / NOT PUBLISHED TO MAIN — NATIVE WRITE ACTIONS NOT EXPOSED.** Bu dosya bir remote yayın başarı makbuzu değildir. Yeni kaynak araştırması ve bounded native async-bridge koşusu yerelde saklandı. Önceki U07 yayını tamamdır; yeni bekleyen birim U08. [STATE](../../STATE.md), [RESEARCH](RESEARCH.md), [MANIFEST](MANIFEST.json).

## Gerçek repo okumaları

Araştırma başında main: `188095b930ac77f8d2a5dd605191a09a369a57ce`. Kapanışta yeniden okunan main: **`a6c47ef3ff697c2d23c492dcf4ccfa32003040da`**. Native compare status=ahead, ahead_by=1, behind_by=0; yalnız `research/soul-foundations/**` yolları değişti. HERMES/CATALOG/agent-control değişen yollarda yoktu. Yeni ref'ten HERMES STATE 1–16 satırları yeniden U07/v0.20 ve **`26d9b5c590b856c439869f4affe80c1c4ff6835c`** blob'unu gösterdi.

Bu Foundation commit'i bu tur oluşturulmadı; bir aktör/diğer çalışma aracına atfedilmedi. HERMES yayını daha sonra **güncel main'i koruyarak** yapılmalı; başlangıç root tree'si üzerine force yazılmamalı. Dosya-baseline kimliklerinin aynı olması bütün root tree'nin aynı olduğu anlamına gelmez.

## Capability sınırı

Create-tree / create discovery boş döndü. Full GitHub listesi 48 read/search eylemi sundu. Update-file sorgusu benzer read araçlarını döndürdü; actual update_file yoktu. Son create_commit sorgusu altı commit-read/search aracı döndürdü; actual create_commit yoktu. Plugin directory GitHub'ı installed/enabled gösterdi. Bu bilgi bağlantının/izinlerin değişme nedenini teşhis etmez.

**Bu tur create/update/blob/tree/commit/ref yazısı, branch/PR veya upstream değişikliği yapılmadı.** Read tool'u gizli write için kullanılmadı. Credential aranmadı, izin/ağ/plugin ayarı değiştirilmedi. Önceki U06 security block ve U07 yayın geçmişi farklı olaylardır; bu engelin nedeni olarak gösterilmez.

## Saklanan kanıt

S04 tam original async_utils.py byte kimliği Git blob ile eşleşti. SPEC/probe/input/result hash bağları, yerel effect dosyaları, stdout/stderr, runtime excerpt/fingerprint ve lisanslar raw arşivdedir. Native SPEC ve RESULT raw arşiv kopyalarıyla aynı byte'lardır. B01–B03 tek recorded run; N01/N02 validator kontrolleri source mutant değildir. Yeni ağ/SessionDB/full-gateway/gerçek duplicate testi yapılmadı.

Yerel [ARTIFACT-CHECKS](ARTIFACT-CHECKS.json) ve teslimin validator çıktısı **artifact transfer/readback** kontrolüdür, ikinci davranış koşusu veya independent replication değildir. Arşive koşudan sonra yalnız lisans bildirimleri eklendi; source/SPEC/probe/INPUTS/RESULT/effect/log yeniden üretilmedi.

## Baseline ve scoped candidate

INDEX, META, OPEN-QUESTIONS, PLAN, SOURCE-LEDGER ve CATALOG yerel baseline'ları, eski teslim metni ile yeniden okunan current publication metni birleştirildikten sonra **tam current Git blob eşleşmesiyle** kabul edildi. Eşleşmeyen ara baseline'lar kullanılmadı. STATE bu tur canonical'dan tam okundu; baseline JSON'da expected blob/byte metadata'sı taşınır, yerel byte-eşit STATE baseline kopyası iddia edilmez. Candidate STATE tam replacement önerisidir; yayında gerçek head içeriği ayrıca karşılaştırılır.

Yalnız `research/studies/hermes-agent/**` ile CATALOG Hermes satırı değişiklik adayıdır. Diğer katalog satırları ve rehberi current baseline ile byte-eşittir. Eski notes01–22, tüm U04–U07 evidence, METHOD ve merkezi synthesis01–03 candidate değişiklik listesinde yoktur. Yeni derived map state authority değildir.

## Yayın devri

Sonraki yayın, teslim üst README/BASELINE/PACKAGE-MANIFEST/PUBLICATION-HANDOFF üzerinden başlayabilir. Önce current AGENT/STATE/main; sonra yeni head ile path-level karşılaştırma. Yeni dosya zaten varsa kör overwrite yapılmaz. Ham deneyler tekrar çalıştırılmaz. U08 root entry/CATALOG/README/PUBLICATION içindeki local/not-published durumları yalnız gerçekleşen publication'a göre uzlaştırılır; raw manifest ilk teslim anını tarihsel metadata olarak tutabilir.

Gerçek native write eylemleri sunulduğunda scoped content commit, nonforce ref ve actual main/diff/content/hash readback gerekir. Bu dosya gelecekteki commit'i tahmin etmez. **Şu an U08 remote publication veya remote U08 content readback yoktur.** Kullanıcının eski U07 ZIP'ini yeniden göndermesi gerekmiyor; korunması gereken yeni paket U08'dir.
