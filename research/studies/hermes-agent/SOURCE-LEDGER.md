# Hermes Agent — Birikimli kaynak ve yürütme defteri

**2026-09-07 / U01B aktarımıyla uzlaştırılmış kayıt.** Birincil pin: `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`.

FULL = önceki veya bu konuşmada tam içerik okunmuş; SELECTED = belirtilen aralık; LISTED = yalnız harita. Hiçbiri tek başına yürütme değildir. Eski okuma bu aktarım turunda yeniden yapılmış sayılmaz. Upstream test suite çalıştırılmadı; yalnız U01B'nin iki exact modüllü sentetik bileşen deneyi kayıtlıdır. Aktarımda deney yeniden koşturulmadı.

## H-kaynakları — mevcut kapsam

Aşağıdaki yollar primary pin'e göredir. Ayrıntılı ilk/curator turu provenance ve açıklamalar [aktarım öncesi immutable defterde](https://github.com/batuhanozgun/agentic-os-search/blob/000f691b9a94607c9a8219961b4618eda0f1014f/research/studies/hermes-agent/SOURCE-LEDGER.md) korunur. Bu eski defterdeki H22 eksikliği ve 'yalnız statik' durumu artık birikimli son durum değildir; aşağıdaki H22 ve S-kayıtları onu genişletir.

| ID | Yol | Blob SHA | Birikimli okuma |
|---|---|---|---|
| H01 | README.md | c05112266746ff99a3326a62c38c33fbc08ecd23 | FULL, ilk + curator turu |
| H02 | website/docs/developer-guide/architecture.md | 3640103c3de97ed7c01a3862b76b35371f9d5f06 | FULL, ilk + curator turu |
| H03 | website/docs/user-guide/features/memory.md | 0c03f4e8cb897bbfd0af29375d7a245fa5751499 | FULL, ilk tur |
| H04 | agent/background_review.py | 0e8e76ae235450f3e896a86951409cf82b7cca1e | FULL, ilk tur |
| H05 | tools/skill_manager_guards.py | 06df3cd695592fd2e582b49ce391d76fd137da3b | FULL, ilk + curator tekrar |
| H06 | tools/skill_provenance.py | 3df9cf143045644310fa7d27a65666c8c23caf95 | FULL, ilk tur |
| H07 | tools/write_approval.py | f1e99b46e934595c002c2bc659143fcbc1f9fe8d | FULL; U01B/S04 tekrar + dar bileşen deneyi |
| H08 | hermes_cli/write_approval_commands.py | 150b72dfd17696ab7a64f97057b7405128f5b352 | FULL; U01B/S05 tekrar, çalıştırılmadı |
| H09 | tests/run_agent/test_background_review_toolset_restriction.py | 3175aa394ce4aaa3258243cec82c546cdad73ba1 | FULL / TEST SOURCE INSPECTED |
| H10 | tests/tools/test_write_approval.py | 44db64514921b1cb892e16e913bffa641acb2947 | FULL / TEST SOURCE INSPECTED |
| H11 | pyproject.toml | 12c672ff3cdacd9d045d60d1cc4248e0aeba6f72 | SELECTED ilk manifest/dependency, curator 1–115 |
| H12 | agent/memory_manager.py | 44ca6f930e884a9667b54fce6e380d04bd001886 | SELECTED 1–120; sonraki prefix keşif |
| H13 | SECURITY.md | cea2a9a2e8869ac7a4b7307332b974a27e9fd27a | FULL, ilk + curator turu |
| H14 | AGENTS.md | aecd44860c669bbb997e90b11112dab540042f97 | FULL 1–170/171–340/341–EOF, araştırma nesnesi |
| H15 | agent/AGENTS.md | 7fb81c5a66a5eb944cabdd7a5a8a015a5a3621b4 | FULL, araştırma nesnesi |
| H16 | skills/AGENTS.md | 27e47db7b607a59f40652959ade4d51bf105016c | FULL, araştırma nesnesi |
| H17 | website/docs/user-guide/features/curator.md | 66dd545cc7e611c06095690b9d36404ffc35047e | FULL, ilk response + 230–EOF |
| H18 | agent/curator.py | 670abfb71d923918f53698226abdb7f494e11b57 | FULL, 200 satırlık ardışık aralıklar / EOF |
| H19 | tools/skill_usage.py | 48d7edc9d3cc636a5c8762304b870fd0a6d8e20d | FULL, 1–210/211–420/421–640/641–EOF |
| H20 | tests/agent/test_curator.py | dd4fd558093485e672cd3cf77dc4d29793282b8b | SELECTED 1–440 / TEST SOURCE INSPECTED |
| H21 | package.json | 406b73b205a32c1ddc7fd1dabfb02250efa5407f | FULL; Node manifest Python release'i değil |
| H22 | tools/skill_manager_tool.py | 81d64b909b6b482654060b38b63802460b63314b | FULL via U01B/S01; eski curator turunun 1–200/801–EOF kapsamı genişletildi. Çalıştırılmadı. |

## U01B S-kaynakları ve deney

[U01B/SOURCES.md](evidence/2026-09-07-u01b/SOURCES.md) tam path/ref/blob/aralık ve eski turun yürütme kaydıdır. S-ID'leri yereldir; H-ID'lerini yeniden numaralandırmaz.

- S01 = H22, tam mutator.
- S02 = tools/skill_manager_batch.py, blob `9f38adff284eede4234948f67e99a43752c0926e`, FULL + exact modül/sentetik bağımlılık deneyi.
- S03 = tests/tools/test_skill_manage_batch.py, blob `7e1c105339c347c950e0cf764d0043f106c9d239`, FULL / TEST SOURCE INSPECTED, upstream suite çalıştırılmadı.
- S04 = H07; S05 = H08.
- S06 = LICENSE, blob `75410e73319c72cd3e991a501c5455eb78f38375`, FULL ve kaynak kopyalarıyla korunmuş.

[Deney girişi](evidence/2026-09-07-u01b/component-probe/README.md) → harness + RESULT.json + stdout/stderr + iki upstream modül/lisans. UTC koşu `2026-09-07T09:35:13.772427+00:00`, Python 3.13.5/Linux. 10 tanılayıcı gözlem; bunlar ürün conformance PASS'i veya bağımsız araştırmacı tekrarı değildir. Gerçek single-op mutator/guard/profile taklitleri açıkça belirtilir. Kaynak blob doğrulaması içerik kimliğini, yeni aktarım manifest kontrolü teslim bütünlüğünü sınar; davranış kapsamını büyütmez.

## Tree, yöntem ve freshness rotaları

T00 root tree `f54f5e9d2682bf11f164de7b34ee10ec121b6434`; T01 apps tree `d6ec471bf1d4acfb42fef4b82b22ce91a2c50437`: non-recursive tam listeler. T02 primary commit / committer `2026-09-07T08:37:43Z`. T03 d8a077... ek root listesi. Recursive tam envanter, LOC sayımı veya Gstack büyüklük kıyası yoktur.

Curator turundaki `d8a07768c5ee59afae62e9fb51d45e1e30aa74da` primary pin'den bir commit ilerideydi; yalnız contributor/pt_input_extras/kitty-keypad testi ve iki CLI belge yolu değişmişti. O tur kullanılan H01/H02/H11/H13/H14–H21 değişmedi; H05/H22 doğrudan primary'den açıldı. Bu, tüm sonraki HEAD'leri doğrulamaz.

U01B'nin `7874ef9f62b9b533f8d3da6107eb2a52f4be252f` gözleminde yalnız S01/S02/S04 blob'ları primary ile karşılaştırıldı ve aynıydı. Current dependency closure veya kurulu release doğrulaması değildir. Bu aktarımda upstream yeniden revalidate edilmedi.

G01 Gstack METHOD blob `dc003b3f74115667a05787a847eadb10876784c8`; G02 META blob `f2ad498742f026aa84578e82ec7fd0cf6843da65`: araştırma yöntemi girdisi, HERMES teknik kanıtı değil. İlk ref 4cb42472..., sonraki aynı içerik e6bc6cd...; FULL okumalar eski defterde ayrılır.

## Erişim ve temsil sınırları

Geçmiş web keşifleri resmî belgeler içindi; teknik iddiaların dayanağı pinned kaynaklardır. İkincil yorumlardan teknik sonuç türetilmedi. Code-search navigation ref'leri tam kaynak yerine geçmedi. Container bulk erişim hatası ve curator turu 429'u ilgili okumaların sınırıdır; kalıcı erişim yokluğu değildir. U01B'nin önceki yayın engeli bu tur yeniden keşfedilen yazma yolu ile ele alınmıştır; neden araç setinin değiştiği belirlenmedi.

Tam okunmamış bölgeler: CONTRIBUTING/SOUL/compat; genel run_agent/turn/dispatch/plugin; memory mutator; ledger/backup/sync; session search/state; idle queue; provider/backend/delegation; gateway/cron/ACP/UI; install/CI/eval/trajectory. S01/S02 artık bu eksik listede değildir. Bir isim veya search hit'i FULL sayılmaz.

Yeni kaynak/koşu kendi ref, kimlik, kapsam ve turuyla eklenir. Bu defter continuity için sıkıştırılmıştır; önceki detaylar immutable Git geçmişinde, U01B ham kanıtları paket içindedir. [Aktarım kimlikleri ve sınırı](evidence/2026-09-07-u01b/PUBLICATION.md).
