# Hermes Agent — Birikimli kaynak ve yürütme defteri

**Son ek: 2026-09-08 / U01B2 tesliminin canonical yayını; U01-D, U01-M ve context-transfer kanıtı korunur.** Birincil pin `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a` değişmedi. Current çalışma otoritesi STATE; defter kanıt/okuma rotasıdır.

FULL tam kaynak okuması; SELECTED belirtilen kesit/sembol; LISTED yalnız topoloji. Hiçbiri kendi başına execution değildir. Eski tam okumalar yeni turda yeniden yapılmış sayılmaz. Büyük façade'ların tüm metnine erişim, tüm dependency/compat yüzeyinin araştırma kapanışı değildir; caller turundaki karar taşıyan kesitler D defterinde SELECTED olarak sınırlandırılır.

## H-kaynakları — önceki birikimli kayıt korunur

Primary pin'e göre yollar ve kimlikler:

| ID | Yol | Blob SHA | Önceki birikimli okuma |
|---|---|---|---|
| H01 | README.md | c05112266746ff99a3326a62c38c33fbc08ecd23 | FULL, ilk + curator |
| H02 | website/docs/developer-guide/architecture.md | 3640103c3de97ed7c01a3862b76b35371f9d5f06 | FULL, ilk + curator |
| H03 | website/docs/user-guide/features/memory.md | 0c03f4e8cb897bbfd0af29375d7a245fa5751499 | FULL |
| H04 | agent/background_review.py | 0e8e76ae235450f3e896a86951409cf82b7cca1e | FULL; caller turu D18 ile yeniden açıldı |
| H05 | tools/skill_manager_guards.py | 06df3cd695592fd2e582b49ce391d76fd137da3b | FULL, ilk + curator |
| H06 | tools/skill_provenance.py | 3df9cf143045644310fa7d27a65666c8c23caf95 | FULL; caller turu D19 + dar execution |
| H07 | tools/write_approval.py | f1e99b46e934595c002c2bc659143fcbc1f9fe8d | FULL; U01B/S04 + dar execution; ayrı U01B2 arşiv okuması/koşusu aşağıda |
| H08 | hermes_cli/write_approval_commands.py | 150b72dfd17696ab7a64f97057b7405128f5b352 | FULL; S05 ve D17 tekrar, çalıştırılmadı |
| H09 | tests/run_agent/test_background_review_toolset_restriction.py | 3175aa394ce4aaa3258243cec82c546cdad73ba1 | FULL / TEST SOURCE INSPECTED |
| H10 | tests/tools/test_write_approval.py | 44db64514921b1cb892e16e913bffa641acb2947 | FULL / TEST SOURCE INSPECTED |
| H11 | pyproject.toml | 12c672ff3cdacd9d045d60d1cc4248e0aeba6f72 | SELECTED manifest/dependency, curator 1–115 |
| H12 | agent/memory_manager.py | 44ca6f930e884a9667b54fce6e380d04bd001886 | SELECTED 1–120; D15/D16 farklı dosyalardır |
| H13 | SECURITY.md | cea2a9a2e8869ac7a4b7307332b974a27e9fd27a | FULL, ilk + curator |
| H14 | AGENTS.md | aecd44860c669bbb997e90b11112dab540042f97 | FULL, araştırma nesnesi |
| H15 | agent/AGENTS.md | 7fb81c5a66a5eb944cabdd7a5a8a015a5a3621b4 | FULL, araştırma nesnesi |
| H16 | skills/AGENTS.md | 27e47db7b607a59f40652959ade4d51bf105016c | FULL, araştırma nesnesi |
| H17 | website/docs/user-guide/features/curator.md | 66dd545cc7e611c06095690b9d36404ffc35047e | FULL |
| H18 | agent/curator.py | 670abfb71d923918f53698226abdb7f494e11b57 | FULL, ardışık 200 satırlık aralıklar/EOF |
| H19 | tools/skill_usage.py | 48d7edc9d3cc636a5c8762304b870fd0a6d8e20d | FULL |
| H20 | tests/agent/test_curator.py | dd4fd558093485e672cd3cf77dc4d29793282b8b | SELECTED 1–440 / TEST SOURCE INSPECTED |
| H21 | package.json | 406b73b205a32c1ddc7fd1dabfb02250efa5407f | FULL; Node manifest Python release'i değil |
| H22 | tools/skill_manager_tool.py | 81d64b909b6b482654060b38b63802460b63314b | FULL via U01B/S01; eski orta aralık eksikliği kapanmış |

[U01B aktarım öncesi ayrıntılı defter](https://github.com/batuhanozgun/agentic-os-search/blob/000f691b9a94607c9a8219961b4618eda0f1014f/research/studies/hermes-agent/SOURCE-LEDGER.md) ve [v0.5 tam defter](https://github.com/batuhanozgun/agentic-os-search/blob/a218acfc20e7ece488709e00a9762166ec970fba/research/studies/hermes-agent/SOURCE-LEDGER.md) önceki tarih/ref/aralık ve erişim olaylarını değişmeden korur. Tarihsel 'yalnız statik', 'H22 eksik' veya 'caller erişilemiyor' cümleleri current birikimli durum değildir.

## U01B S-kaynakları ve ilk dar deney

[U01B/SOURCES.md](evidence/2026-09-07-u01b/SOURCES.md) exact path/ref/blob/aralık ve eski execution kaydıdır. S-ID'leri yereldir.

- S01 = H22, tam skill mutator.
- S02 = tools/skill_manager_batch.py, blob `9f38adff284eede4234948f67e99a43752c0926e`, FULL + exact modül/sentetik bağımlılık deneyi.
- S03 = tests/tools/test_skill_manage_batch.py, blob `7e1c105339c347c950e0cf764d0043f106c9d239`, FULL / TEST SOURCE INSPECTED; çalıştırılmadı.
- S04 = H07; S05 = H08.
- S06 = LICENSE, blob `75410e73319c72cd3e991a501c5455eb78f38375`, FULL ve kaynak kopyalarıyla korunmuş.

[Eski probe](evidence/2026-09-07-u01b/component-probe/README.md) → harness/RESULT/stdout/stderr/upstream/lisans. UTC `2026-09-07T09:35:13.772427+00:00`, Python 3.13.5/Linux. İki exact modül + sentetik bağımlılıklar, 10 tanılayıcı durum. Ürün conformance veya bağımsız araştırmacı tekrarı değil. Bu yayın turunda yeniden çalıştırılmadı. [Yayın aktarımı](evidence/2026-09-07-u01b/PUBLICATION.md) deneyden ayrı olaydır.

## Tree, yöntem ve freshness geçmişi

T00 root tree `f54f5e9d2682bf11f164de7b34ee10ec121b6434`; T01 apps tree `d6ec471bf1d4acfb42fef4b82b22ce91a2c50437`: non-recursive listeler. Primary committer zamanı `2026-09-07T08:37:43Z`. T03 d8a077... root gözlemi. Recursive tam envanter/LOC veya Gstack büyüklük kıyası yoktur.

Curator ref'i `d8a07768c5ee59afae62e9fb51d45e1e30aa74da` primary'den bir commit ilerideydi; yalnız contributor/pt_input_extras/kitty-keypad testi ve iki CLI belge yolu değişmişti. İlgili kaynaklar aynı blob'larla uzlaştırıldı. U01B'nin `7874ef9f62b9b533f8d3da6107eb2a52f4be252f` gözleminde yalnız S01/S02/S04 aynı blob taşıyordu. Bunlar bütün sonraki HEAD'lerin veya kurulu release'in doğrulanması değildir.

G01 Gstack METHOD `dc003b3f74115667a05787a847eadb10876784c8`; G02 META `f2ad498742f026aa84578e82ec7fd0cf6843da65`, önceki FULL okumalar: yöntem girdisi, Hermes teknik kanıtı değil. Canonical agent-control dosyaları corpus'a katılmaz.

## W01–W08 — ayrı unpinned belge katmanı

[Okuma/erişim defteri](evidence/2026-09-08-doc-contracts/READING-AND-ACCESS.md) URL/tarih/bölüm ve sınırları; [05 notu](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md) belge kontratı/karşı-sınama tasarımını taşır.

| ID | Resmî belge |
|---|---|
| W01 | Tools Runtime |
| W02 | Agent Loop Internals |
| W03 | Event Hooks |
| W04 | Persistent Memory |
| W05 | Prompt Assembly |
| W06 | Profiles |
| W07 | Session Storage |
| W08 | Context Compression and Caching |

W gözlemleri commit/blob'a bağlanmadı. H03 ile W04 aynı nesne sayılmaz. Belge turundaki iki `run_agent.py` path 429'u ve container DNS hatası tarihsel erişim sonucudur; o tur yeni caller kodu veya execution yoktu. K01–K09 o tarihte NOT RUN idi; güncel kısmi kaynak/probe durumları RESEARCH-PLAN v0.6'da ayrılır.

## D01–D22 — pinned caller / worker / memory kaynakları

[Tam D defteri](evidence/2026-09-08-context-transfer/SOURCES.md) exact path/blob ve FULL/SELECTED/EXECUTED derinliğini taşır. [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md) caller/transfer; [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md) memory/replay bulgularını içerir.

Caller turu `a218acfc...` research state'inden başladı. Path isteği yine 429 verdi; primary tree/blob API kaynak getirdi. Root'a ek agent/tools/hermes_cli non-recursive topolojisi görüldü; D09/D10/D19 yerel kopyaları ve LICENSE Git blob hash'leriyle doğrulandı. Bir source-transcription uyuşmazlığı execution öncesinde yakalanıp canonical blob yeniden alınarak düzeltildi; doğrulama eşiği değiştirilmedi.

[Transport probe](evidence/2026-09-08-context-transfer/README.md): UTC `2026-09-08T15:57:15.365904+00:00`, Python 3.13.5/Linux. Üç exact modül, sentetik callback API/profil marker/allowlist; P01–P07. Gerçek executor/PluginManager/AIAgent/MemoryStore ve profil resolver bu koşuda yoktur. Yedi beklenti matched; product conformance NOT ASSESSED. [Ham sonuç](evidence/2026-09-08-context-transfer/RESULT.json), [harness](evidence/2026-09-08-context-transfer/harness.py), [kimlik manifesti](evidence/2026-09-08-context-transfer/MANIFEST.json).

Güncel açık kapsam: ordinary dispatch entegrasyon sınaması; actual UI/approval/profile; curator nested batch/rapor; ledger/backup/restore/sync; cancellation/shared-store; prompt reload/invalidation; session search/archive; alternatif runtime, provider/backend/delegation/gateway/cron/UI; install/CI/eval/gelecek-task kalite. Kaynak okuması, dar modül yürütmesi, hash bütünlüğü ve tüm ürün doğrulaması ayrı tutulur. Current upstream yeniden doğrulanmadı; geçmiş W ve U01B statüleri değiştirilmedi.

## U01B2 — ayrı arşiv kaynaklı deney ve sonradan yayın

[08 canonical giriş](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md) → [özgün rapor](evidence/2026-09-08-u01b2/06-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md), [SOURCES.json](evidence/2026-09-08-u01b2/SOURCES.json), [RESULT](evidence/2026-09-08-u01b2/RESULT.json), [SPEC](evidence/2026-09-08-u01b2/SPEC.md), [probe](evidence/2026-09-08-u01b2/probe.py), [yayın](evidence/2026-09-08-u01b2/PUBLICATION.md).

U01B2 çalışma dilimi research `a218acfc...` arşivinden S02 ve S04/H07'yi FULL yeniden okudu; blob'lar sırasıyla `9f38adff284eede4234948f67e99a43752c0926e` ve `f1e99b46e934595c002c2bc659143fcbc1f9fe8d`. Yeni H-ID veya upstream güncellik doğrulaması değildir. Kaynak lisansı aynı `75410e...` blob'udur.

Koşu UTC `2026-09-08T15:48:02.995262+00:00`, Python 3.13.5/Linux; 12 tanılayıcı senaryo, G01 içinde 10 gate varyantı. Gerçek iki modül ile sentetik config/profile-origin/callback/guard/mutator/adapter/reentry. R03 önceki exception sınırının yeni fixture tekrarı; R04 deterministik araya-giren yazı, gerçek thread yarışı değildir. Gerçek production replay, kilitler, UI, ledger/sync veya kalite deneyi yapılmadı. HARNESS-CHECK yalnız değiştirilmiş kaynak kimliğinin execution öncesi reddini sınar.

Teslim ZIP'i bu yayın turunda açıldı; 14 manifest girdisinin byte/SHA-256 kontrolü yapıldı, MANIFEST dahil 15 özgün dosya korundu. Deney veya negatif kontrol yeniden çalıştırılmadı. Publication tabanı `29ab9b816843bab6f9e5f5b5815590fbac2b1713`; D kaynak/transport ilerlemesi aynen korunur. U01B2'nin eski NOT_PUBLISHED ve caller erişimi ifadeleri kendi tarihsel turuna aittir; current STATE değildir. Yerel D01 senaryosu D kaynak defterinin D01'iyle karıştırılmaz.
