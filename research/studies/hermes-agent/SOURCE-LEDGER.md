# Hermes Agent — Kaynak ve okuma defteri

**Gözlem tarihi:** 2026-09-07. Bu defter ilk ve ek kaynak turlarının birikimli kaydıdır. Tüm H-kaynakları aşağıdaki immutable pin'e bağlıdır:

`NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`.

FULL dosya içeriğinin tamamının okunduğunu; SELECTED yalnız adı verilen kapsamı; LISTED bir tree girdisinin görüldüğünü belirtir. Bir dosyayı indirmek/getirmek tek başına okumak değildir. Tool çıktısı kesildiğinde eksik içerik sonraki aralık veya response-resource okumasıyla tamamlandı; tamamlanmayan dosyalar SELECTED kaldı. İncelenen testler yürütülmedi. Birikimli kayıttaki eski FULL, her yeni turun aynı dosyayı tekrar okuduğu anlamına gelmez.

## Pinned kaynaklar

| ID | Dosya / doğrudan kaynak | Blob SHA | Okuma | Kullanım / tur |
|---|---|---|---|---|
| H01 | [README.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/README.md) | `c05112266746ff99a3326a62c38c33fbc08ecd23` | FULL | İlk tur + ek tur yeniden okuma. Tanıtım iddiaları, ürün girişleri, migration; runtime başarı kanıtı değil. |
| H02 | [website/docs/developer-guide/architecture.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/website/docs/developer-guide/architecture.md) | `3640103c3de97ed7c01a3862b76b35371f9d5f06` | FULL | İlk tur + ek tur yeniden okuma. Native harita/facade/giriş yolları; sayılar ölçülmedi. |
| H03 | [website/docs/user-guide/features/memory.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/website/docs/user-guide/features/memory.md) | `0c03f4e8cb897bbfd0af29375d7a245fa5751499` | FULL | İlk tur. Bellek/skill/review/onay/sonraki kullanım kontratı; performans iddiaları bağımsız doğrulanmadı. |
| H04 | [agent/background_review.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/agent/background_review.py) | `0e8e76ae235450f3e896a86951409cf82b7cca1e` | FULL | İlk tur. Fork/runtime/digest/persistence/whitelist/cancellation ve review promptları. |
| H05 | [tools/skill_manager_guards.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tools/skill_manager_guards.py) | `06df3cd695592fd2e582b49ce391d76fd137da3b` | FULL | İlk tur + ek tur c4a5de... yeniden okuma, 1–200/201–EOF. Ownership/pinned/externals, read marks, delete/consolidation/org mirror guard. |
| H06 | [tools/skill_provenance.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tools/skill_provenance.py) | `3df9cf143045644310fa7d27a65666c8c23caf95` | FULL | İlk tur. Foreground/background-review ContextVar. |
| H07 | [tools/write_approval.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tools/write_approval.py) | `f1e99b46e934595c002c2bc659143fcbc1f9fe8d` | FULL | İlk tur. Gate, pending store, diff; stage I/O failure return yolu. |
| H08 | [hermes_cli/write_approval_commands.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/hermes_cli/write_approval_commands.py) | `150b72dfd17696ab7a64f97057b7405128f5b352` | FULL | İlk tur. Pending list/approve/reject/diff; apply hedefleri. |
| H09 | [tests/run_agent/test_background_review_toolset_restriction.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tests/run_agent/test_background_review_toolset_restriction.py) | `3175aa394ce4aaa3258243cec82c546cdad73ba1` | FULL / TEST SOURCE INSPECTED | İlk tur. Mock config/whitelist assertions; full-vs-partial read marks. Çalıştırılmadı. |
| H10 | [tests/tools/test_write_approval.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tests/tools/test_write_approval.py) | `44db64514921b1cb892e16e913bffa641acb2947` | FULL / TEST SOURCE INSPECTED | İlk tur. Default/invalid config, inline approve/deny, approve-all, validation. Çalıştırılmadı. |
| H11 | [pyproject.toml](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/pyproject.toml) | `12c672ff3cdacd9d045d60d1cc4248e0aeba6f72` | SELECTED — ilk manifest/dependency kesiti; ek tur 1–115 | 0.21.0, Python >=3.11,<3.14, core/optional ayrımı. Bütün manifest okunmadı; security yorumları olay kanıtı değil. |
| H12 | [agent/memory_manager.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/agent/memory_manager.py) | `44ca6f930e884a9667b54fce6e380d04bd001886` | SELECTED — 1–120 tam aralık; daha sonraki prefix yalnız keşif | İlk tur. Context aktarımı ve tool-exposure helpers; provider lifecycle kapanmadı. |
| H13 | [SECURITY.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/SECURITY.md) | `cea2a9a2e8869ac7a4b7307332b974a27e9fd27a` | FULL | İlk tur + ek tur yeniden okuma. Declared threat model; compliance kanıtı değil. |
| H14 | [AGENTS.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/AGENTS.md) | `aecd44860c669bbb997e90b11112dab540042f97` | FULL — 1–170/171–340/341–EOF | Ek tur. Native kaynak rotaları, facade/compat ve test yaklaşımı; araştırma nesnesi, assistant kontrolü değil. Belgedeki sayılar ölçülmedi. |
| H15 | [agent/AGENTS.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/agent/AGENTS.md) | `7fb81c5a66a5eb944cabdd7a5a8a015a5a3621b4` | FULL | Ek tur. Loop/turn/runtime/prompt ve memory/context-engine ayrımları için keşif rotası. |
| H16 | [skills/AGENTS.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/skills/AGENTS.md) | `27e47db7b607a59f40652959ade4d51bf105016c` | FULL | Ek tur. Skill package kontratı; curator ownership açıklaması diğer kaynaklarla karşı okundu. |
| H17 | [website/docs/user-guide/features/curator.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/website/docs/user-guide/features/curator.md) | `66dd545cc7e611c06095690b9d36404ffc35047e` | FULL — ilk response ve 230–EOF tamamlaması | Ek tur. Deterministik bakım/opt-in consolidation, policy/adoption, lifecycle ve recovery kontratı. |
| H18 | [agent/curator.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/agent/curator.py) | `670abfb71d923918f53698226abdb7f494e11b57` | FULL — 1–200/201–400/401–600/601–800/801–1000/1001–EOF | Ek tur. Lifecycle, fork, reporting/classification, cron rewrite, defaults ve hata yolları. Çalıştırılmadı. |
| H19 | [tools/skill_usage.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tools/skill_usage.py) | `48d7edc9d3cc636a5c8762304b870fd0a6d8e20d` | FULL — 1–210/211–420/421–640/641–EOF | Ek tur. Policy/telemetry/lifecycle ayrımı, archive/restore, best-effort yan kayıtlar. |
| H20 | [tests/agent/test_curator.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tests/agent/test_curator.py) | `dd4fd558093485e672cd3cf77dc4d29793282b8b` | SELECTED 1–440 / TEST SOURCE INSPECTED | Ek tur. Fixture, pin/first-run/cron/hub ve dry-run banner. Tam test dosyası okunmadı, test çalıştırılmadı. |
| H21 | [package.json](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/package.json) | `406b73b205a32c1ddc7fd1dabfb02250efa5407f` | FULL | Ek tur. Workspaces/installation-entry ayrımı. Private Node manifest 1.0.0 değeri Python ürün release'i olarak yorumlanmadı. |
| H22 | [tools/skill_manager_tool.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tools/skill_manager_tool.py) | `81d64b909b6b482654060b38b63802460b63314b` | SELECTED 1–200 ve 801–EOF | Ek tur, doğrudan primary pin. Başlangıç validation/profile bağlama ve son schema/registry/compat kesiti. 201–800 okunmadı; 201–400 isteği 429 ile içerik getirmedi. |

## Ek tur: ref uzlaştırması ve yeniden okuma sınırı

Ek tur H01/H02/H11/H13/H14–H21 içeriklerini `d8a07768c5ee59afae62e9fb51d45e1e30aa74da` üzerinden gördü. Paket daha önce c4a5de... pin'iyle kayıtlı olduğundan GitHub commit karşılaştırması açıldı: d8a077... bir commit ileride; yalnız contributor kaydı, `hermes_cli/pt_input_extras.py`, `tests/cli/test_kitty_keypad_parity.py` ve iki CLI belge yolu değişmişti. Yukarıdaki okunan kaynaklar değişmedi. Bu, aynı içerikleri primary pin'e bağlar; primary pin'i değiştirmez ve bütün sonraki HEAD'leri doğrulamaz. [Karşılaştırma](https://github.com/NousResearch/hermes-agent/compare/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a...d8a07768c5ee59afae62e9fb51d45e1e30aa74da).

H05 ve H22 ek turda doğrudan c4a5de... üzerinden okundu. H03/H04/H06–H10/H12'nin ilk tur kaynak okumaları korunur; ek turda onların hepsinin tekrar okunduğu iddia edilmez. Mevcut 00-WHY/META/STATE/INDEX/METHOD/PLAN/LEDGER/OPEN-QUESTIONS/inventory ve 01/02 notları Research `e6bc6cd...` üzerinden tam geri kazanıldı. Yayın öncesi `408ee3ce...` ile karşılaştırma Hermes paketinde değişiklik olmadığını, aradaki iki commit'in context köprüsünde olduğunu gösterdi.

## Tree / snapshot kaynakları

- **T00:** [kök tree](https://api.github.com/repos/NousResearch/hermes-agent/git/trees/f54f5e9d2682bf11f164de7b34ee10ec121b6434), non-recursive liste tam, `truncated:false`. Bütün repository içerik kapsamı değildir.
- **T01:** [apps tree](https://api.github.com/repos/NousResearch/hermes-agent/git/trees/d6ec471bf1d4acfb42fef4b82b22ce91a2c50437), non-recursive liste tam, `truncated:false`.
- **T02:** ilk main gözlemi commit'i `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, tree `f54f5e9d...`, committer timestamp `2026-09-07T08:37:43Z` olarak bağladı. [Immutable commit](https://github.com/NousResearch/hermes-agent/commit/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a).
- **T03:** ek tur d8a077... non-recursive kök tree'si tam geri kazanıldı. Recursive bütün dosya/LOC ölçümü veya Gstack büyüklük kıyası yapılmadı.

## Yöntem karşılaştırması

Bunlar HERMES'in teknik davranışına kanıt değil, araştırma yöntemine girdidir. ID'ler agent-control route ID'leri değildir.

- **G01:** `research/studies/gstack/METHOD.md`, ilk araştırma ref'i `4cb42472e3e8391f91836c5f4518db3fc30b89af`, blob `dc003b3f74115667a05787a847eadb10876784c8`, FULL. Ek tur e6bc6cd... üzerinden aynı blob yeniden okundu.
- **G02:** `research/studies/gstack/META.md`, aynı ilk ref, blob `f2ad498742f026aa84578e82ec7fd0cf6843da65`, FULL. Ek tur e6bc6cd... üzerinden yeniden okundu.

## Değişebilir web keşfi

2026-09-07'de resmî repository/ürün belgeleri web yoluyla da arandı: `https://hermes-agent.nousresearch.com/docs/`, architecture ve memory sayfaları. Bu web keşfi ayrı bir pinned corpus değildir; yük taşıyan teknik notlar H-kaynaklarına bağlandı. Release/issue/code-search sonuçları incelenmiş runtime veya tam release incelemesi sayılmadı. İkincil yorumlardan teknik sonuç üretilmedi. Sonraki bir source-search ref'inin görünmesi bütün o ref'in okunduğu anlamına gelmez.

## Keşfedildi fakat full read yapılmadı

`CONTRIBUTING.md`, `SOUL.md`, compat manifestleri; `run_agent.py`, conversation/turn modülleri; `model_tools.py`, `hermes_cli/plugins.py`; memory mutator, skill_manager_tool'un eksik orta bölümü, skill_manager_batch, ledger/backup/sync; session-search ve state yardımcıları; review-idle queue; provider/backend/delegation; gateway/cron/ACP/UI; kurulum, CI/eval ve trajectory yüzeyleri.

Bazıları tree veya belgede adlandırıldı, bazıları code-search excerpt'inde görüldü. Bunların hiçbiri FULL kapsamına eklenmez. Search miss, kaynak yokluğu değildir; örneğin ilk turda test dosyası ilk dosya-adı aramasında görünmeyip sembol aramasında bulunabildi.

## Araştırma ortamı sınırı

GitHub bağlantısıyla kaynak okuma başarılıydı. Bulk indirme yolu başarılı olmadı; local tam-clone envanteri veya yerel upstream test koşusu yapılmış gibi davranılmadı. Son ek kaynak isteğinde 429/fail-fast geldi; o aralık açık kaldı. Daha sonraki Research yayın preflight'ının çalışması bu kayıp aralığı okunmuş yapmaz. Kurulum, provider çağrısı, upstream mutation veya test koşusu yapılmadı.

## Yeniden giriş

Her nottaki H-ID → bu tablodaki path/ref/blob → ilgili sembol/bölüm. Kaynak pin değişmeden blob değişirse işlem durdurulup binding açıklanır. Yeni okumalar derinlik ve hangi soruyu değiştirdiğiyle eklenir; mevcut tabloya yalnız dosya sayısını büyütmek için keşif sonucu FULL olarak yazılmaz.
