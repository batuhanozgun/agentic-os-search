# Hermes Agent — Kaynak ve okuma defteri

**Gözlem tarihi:** 2026-09-07. Tüm H-kaynakları aşağıdaki immutable pin'e bağlıdır:

`NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`.

FULL dosya içeriğinin tamamının okunduğunu; SELECTED yalnız adı verilen kapsamı; LISTED bir tree girdisinin görüldüğünü belirtir. Bir dosyayı indirmek/getirmek tek başına okumak değildir. Tool çıktısı kesildiğinde eksik içerik sonraki aralık veya response-resource okumasıyla tamamlandı; tamamlanmayan dosyalar SELECTED kaldı. İncelenen testlerin hiçbiri bu tur yürütülmedi.

## Pinned kaynaklar

| ID | Dosya / doğrudan kaynak | Blob SHA | Okuma | Bu turun kullanımı |
|---|---|---|---|---|
| H01 | [README.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/README.md) | `c05112266746ff99a3326a62c38c33fbc08ecd23` | FULL | Tanıtım iddiaları, ürün girişleri, migration; runtime başarı kanıtı değil. |
| H02 | [website/docs/developer-guide/architecture.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/website/docs/developer-guide/architecture.md) | `3640103c3de97ed7c01a3862b76b35371f9d5f06` | FULL | Native harita, facade/alt modüller, giriş yolları; sayılar ölçülmedi. |
| H03 | [website/docs/user-guide/features/memory.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/website/docs/user-guide/features/memory.md) | `0c03f4e8cb897bbfd0af29375d7a245fa5751499` | FULL | Bellek/skill/review/onay/sonraki kullanım kontratı; performans iddiaları bağımsız doğrulanmadı. |
| H04 | [agent/background_review.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/agent/background_review.py) | `0e8e76ae235450f3e896a86951409cf82b7cca1e` | FULL | Fork/runtime/digest/persistence/whitelist/cancellation ve review promptları. |
| H05 | [tools/skill_manager_guards.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tools/skill_manager_guards.py) | `06df3cd695592fd2e582b49ce391d76fd137da3b` | FULL | Ownership, pinned/externals, path read marks, delete/consolidation/org mirror guard. |
| H06 | [tools/skill_provenance.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tools/skill_provenance.py) | `3df9cf143045644310fa7d27a65666c8c23caf95` | FULL | Foreground/background-review ContextVar. |
| H07 | [tools/write_approval.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tools/write_approval.py) | `f1e99b46e934595c002c2bc659143fcbc1f9fe8d` | FULL | Gate, pending store, diff; stage I/O failure return yolu. |
| H08 | [hermes_cli/write_approval_commands.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/hermes_cli/write_approval_commands.py) | `150b72dfd17696ab7a64f97057b7405128f5b352` | FULL | Pending list/approve/reject/diff; apply çağrı hedefleri, başarı/başarısızlık. |
| H09 | [tests/run_agent/test_background_review_toolset_restriction.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tests/run_agent/test_background_review_toolset_restriction.py) | `3175aa394ce4aaa3258243cec82c546cdad73ba1` | FULL / TEST SOURCE INSPECTED | Mock config/whitelist assertions; full-vs-partial read marks. Çalıştırılmadı. |
| H10 | [tests/tools/test_write_approval.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/tests/tools/test_write_approval.py) | `44db64514921b1cb892e16e913bffa641acb2947` | FULL / TEST SOURCE INSPECTED | Default/invalid config, inline approve/deny, approve-all, validation. Çalıştırılmadı. |
| H11 | [pyproject.toml](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/pyproject.toml) | `12c672ff3cdacd9d045d60d1cc4248e0aeba6f72` | SELECTED — başlangıç/manifest ve dependency bölümü | 0.21.0, Python >=3.11,<3.14, core/optional ayrımı. Bütün manifest okunmadı; security yorumları olay kanıtı değil. |
| H12 | [agent/memory_manager.py](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/agent/memory_manager.py) | `44ca6f930e884a9667b54fce6e380d04bd001886` | SELECTED — 1–120 tam aralık; daha sonraki prefix yalnız keşif | Context aktarımı ve tool-exposure helpers. Provider lifecycle bütünlüğü çıkarılmadı. |
| H13 | [SECURITY.md](https://github.com/NousResearch/hermes-agent/blob/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a/SECURITY.md) | `cea2a9a2e8869ac7a4b7307332b974a27e9fd27a` | FULL | Declared threat model: process/terminal ayrımı ve external surface auth. Compliance kanıtı değil. |

## Tree / snapshot kaynakları

- **T00:** [kök tree](https://api.github.com/repos/NousResearch/hermes-agent/git/trees/f54f5e9d2682bf11f164de7b34ee10ec121b6434), non-recursive liste tam, `truncated:false`. Bütün repository içerik kapsamı değildir.
- **T01:** [apps tree](https://api.github.com/repos/NousResearch/hermes-agent/git/trees/d6ec471bf1d4acfb42fef4b82b22ce91a2c50437), non-recursive liste tam, `truncated:false`.
- **T02:** main gözlemi commit'i `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, tree `f54f5e9d...`, committer timestamp `2026-09-07T08:37:43Z` olarak bağladı. [Immutable commit](https://github.com/NousResearch/hermes-agent/commit/c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a).

## Yöntem karşılaştırması

Bunlar HERMES'in teknik davranışına kanıt değil, araştırma yöntemine girdidir. ID'ler agent-control route ID'leri değildir.

- **G01:** `research/studies/gstack/METHOD.md`, araştırma ref'i `4cb42472e3e8391f91836c5f4518db3fc30b89af`, blob `dc003b3f74115667a05787a847eadb10876784c8`, FULL.
- **G02:** `research/studies/gstack/META.md`, aynı ref, blob `f2ad498742f026aa84578e82ec7fd0cf6843da65`, FULL.

## Değişebilir web keşfi

2026-09-07'de resmî repository/ürün belgeleri web yoluyla da arandı: `https://hermes-agent.nousresearch.com/docs/`, architecture ve memory sayfaları. Bu web keşfi ayrı bir pinned corpus değildir; bu turun yük taşıyan teknik notları H-kaynaklarına bağlandı. Release/issue arama sonuçları incelenmiş runtime veya tam release incelemesi sayılmadı. İkincil yorumlardan teknik sonuç üretilmedi.

## Keşfedildi fakat bu tur full read yapılmadı

`AGENTS.md`, `CONTRIBUTING.md`, `SOUL.md`, compat manifestleri; `run_agent.py`, conversation/turn modülleri; `model_tools.py`, `hermes_cli/plugins.py`; memory/skill mutators ve ledger/curator/sync; session-search ve state yardımcıları; review-idle queue; provider/backend/delegation; gateway/cron/ACP/UI; kurulum, CI/eval ve trajectory yüzeyleri.

Bazıları tree veya belgede adlandırıldı, bazıları code-search excerpt'inde görüldü. Bunların hiçbiri FULL kapsamına eklenmez. Search miss, kaynak yokluğu değildir; örneğin test dosyası ilk dosya-adı aramasında görünmeyip sembol aramasında bulunabildi.

## Bu turun araştırma ortamı sınırı

GitHub bağlantısıyla kaynak okuma başarılıydı. Araştırma çalışma alanına bulk indirme yolu başarılı olmadı; bu yüzden local tam-clone envanteri veya yerel upstream test koşusu yapılmış gibi davranılmadı. Bu durum HERMES'in çalıştırılamadığı veya kaynak erişiminin genel olarak olmadığı anlamına gelmez. Kurulum, provider çağrısı ve upstream mutation yapılmadı.

## Yeniden giriş

Her nottaki H-ID → bu tablodaki path/ref/blob → ilgili sembol/bölüm. Kaynak pin değişmeden blob değişirse işlem durdurulup binding açıklanır. Yeni okumalar derinlik ve hangi soruyu değiştirdiğiyle eklenir; mevcut tabloya yalnız dosya sayısını büyütmek için keşif sonucu FULL olarak yazılmaz.
