# ECC — Source and Read Ledger

**Observation date:** 2026-09-17. Bu ledger okuma/kimlik kapsamını gösterir; araştırma sonucu veya bütün repo coverage iddiası değildir.

## Primary binding

Repository https://github.com/affaan-m/ECC ; main ref doğrudan GitHub API `git/ref/heads/main` üzerinden `8321021c54d670126ce3b2969d5deb880b4b0c2a` olarak doğrulandı. Bundan sonraki ana corpus bu commit'e bağlıdır. Ön turdaki search-commit sonucu tek başına HEAD kanıtı değildi; U00 direct-ref kontrolü bunu tamamladı.

| ID | Pinned source | Coverage | Identity / observed scope |
|---|---|---|---|
| S01 | git/ref/heads/main | FULL API RESPONSE | 2026-09-17 gözlemi; yukarıdaki commit. Mutable ref gelecekte farklı olabilir. |
| S02 | [docs/architecture/cross-harness.md](https://github.com/affaan-m/ECC/blob/8321021c54d670126ce3b2969d5deb880b4b0c2a/docs/architecture/cross-harness.md) | FULL READ | blob `768414b72432115fe885fecdd9ef72751a6b9742`; ortak layer/adapters/memory/session/Hermes sınırları yazarın belgelenmiş açıklamasıdır; implementation henüz takip edilmedi. |
| S03 | [package.json](https://github.com/affaan-m/ECC/blob/8321021c54d670126ce3b2969d5deb880b4b0c2a/package.json) | SELECTED READ — lines 1–45 | blob `87487a914c0fd739ea62107e7bf9e56b127207a5`; name/version/license alanları görüldü. Önceki tam çağrı truncated olduğundan full-read sayılmaz. Version 2.2.1 distributed package verification değildir. |

## Earlier screening — preserved but not promoted

Aşağıdaki dosyalar aynı conversation'ın ön taramasında main üzerinden okundu. O turda bütün okumalara exact commit bağlanmadı; yük taşıyan araştırma için pinned ref'te yeniden açılacaklar. Blob kimlikleri mevcut olduğunda korunur. Aynı görüşmede okunmuş olmak independent evidence değildir.

| Seed | Source path | Gerçek kapsam ve sınırlama |
|---|---|---|
| D01 | README.md; root directory listing | TRUNCATED / discovery; tam README veya recursive tree okuması değil |
| D02 | docs/architecture/harness-adapter-compliance.md | FULL READ; blob `09061190d5a30d0ea50aa2ae36a6818f26fb2a50`; support etiketleri target claim, actual host parity değil |
| D03 | docs/architecture/platform-value-loop.md | FULL READ; blob `0a61716ea99ba274e0d450cbcd2ec40d3bd949a7`; roadmap/release lane tarihsel olabilir, güncel bütün ürün statüsü değildir |
| D04 | docs/SKILL-PLACEMENT-POLICY.md | FULL READ; blob `7f11f74bc25629d109e3004273ae542dc923e7d3`; policy ile write path enforcement ayrı |
| D05 | docs/continuous-learning-v2-spec.md | FULL READ; blob `a27be00b2351b6e5097dfa8d33b31eb6a89362ee`; kısa yönlendirme, uygulamanın tam incelemesi değil |
| D06 | skills/continuous-learning-v2/SKILL.md | SELECTED/PARTIAL; blob `397b3d334dd1fdf5d7648dd619b6a744cd4734a5`; dosya yapısı başlığında kesilen görünüm, kalan bölüm okunmadı |
| D07 | docs/architecture/session-adapter-contract.md | SELECTED/PARTIAL; blob `49401ff93ea946a7c0f9497442a34cc5166d0580`; claude-history mapping başlığından sonrası önceki görünümde yok |
| D08 | docs/ECC-PRO-SECURITY-ROADMAP.md | TRUNCATED; 2026-06-21 draft tarihi görüldü; belirtilen issue'ların bugün açık olması veya bug'ın devamı doğrulanmadı |

Search snippets (skill tracker, install ownership, architecture/eval paths) yalnız discovery ipucudur; kod/test full-read veya sonuç değildir. Test SOURCE INSPECTED/EXECUTED statüsünde yeni ECC kaydı yok. Gerçek host/model/effectiveness verisi yok.

## Method precedent and project orientation

Aşağıdakiler SOUL Research main üzerinden U00'da FULL READ edildi. Bunlar ECC davranışına kanıt değil, yöntem/current project bağlamıdır.

| Source | Blob / role |
|---|---|
| [gstack METHOD](../gstack/METHOD.md) | `dc003b3f74115667a05787a847eadb10876784c8`; mechanism units, provenance graph, native-before-projection, closure challenge |
| [Hermes METHOD](../hermes-agent/METHOD.md) | `f4b3b25183e7402bf2921f9ca0818e7c5c5aee19`; entrypoint/consumer closure, variation, interruption/publication discipline |
| [Superpowers METHOD](../superpowers/METHOD.md) | `95f684306f92373dbb51f4ceedaff885394e950b`; instruction→implementation→host→effectiveness distinctions |
| [Foundation STATE](../../soul-foundations/STATE.md) | `6d1c3db664bb154546cb6c0bf5edc6da5275dcf8`; 2026-09-17 sufficient-stop/reuse direction, no target design activation |
| [Foundation discussion handoff](../../soul-foundations/08_foundation-sufficiency-reuse-review/DISCUSSION-HANDOFF.md) | `e95cf01635d328ae4d5db414ba5a9c4d70a42fb7`; production-perspective omission and later correction; analytical, not live experiment |
| [Foundation REUSE](../../soul-foundations/08_foundation-sufficiency-reuse-review/REUSE.md) | `b92c29d85055c70536392c0804a7a621efc9caff`; question-first retrieval; historical pending language is superseded by current STATE |

Research root INDEX, studies INDEX/CATALOG/PACKAGE-CONTRACT were recovered in this conversation; current studies INDEX/CATALOG were freshly re-read before publication planning, including Superpowers entries. Agent-control bootstrap/readings are not included as substantive research evidence.

## Ledger growth rule

For each later source: stable ID; exact repo/ref/path/blob when available; date; full/selected/truncated and exact range; related Q/unit/note; target-claim versus implementation versus execution class; dependency/revalidation condition. Directory coverage and reading coverage stay separate. Upstream diff adds a separately labelled revalidation record and affected-claim links.
