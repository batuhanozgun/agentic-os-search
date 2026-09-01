# Records / Artifacts — INDEX

## Rol

Bu dosya `records-artifacts/**` araştırması için retrieval router'dır. Bir bulgunun kanıtı veya source-of-truth'u değildir.

## Varsayılan okuma sırası

1. Güncel durum ve yetki sınırı için `STATE.md`.
2. Mevcut bounded sonuç için `FOUNDATIONAL-SYNTHESIS.md`.
3. İlgili iddianın konsolide kaynak izi için `SOURCES.md`.
4. Daha ayrıntılı lens/source okuması gerekiyorsa `sources/` altındaki ledger.
5. Exact veya tartışmalı claim için ledger/SOURCES içindeki birincil kaynağa dön.

## Topic routing

| Konu | Önce oku | Gerekirse derine in |
|---|---|---|
| Record nedir? | `FOUNDATIONAL-SYNTHESIS.md` | `SOURCES.md`, `sources/records-archival-science.md`, `sources/term-boundaries.md` |
| Record ile artifact aynı mı? | `FOUNDATIONAL-SYNTHESIS.md` | `synthesis/CONCEPT-BOUNDARIES.md`, `sources/term-boundaries.md` |
| Bilgi / data / record / state / event / claim / evidence ayrımları | `synthesis/CONCEPT-BOUNDARIES.md` | `FOUNDATIONAL-SYNTHESIS.md`, `SOURCES.md` |
| Bits/content neden tek başına yeterli değil? | `FOUNDATIONAL-SYNTHESIS.md` | `sources/digital-preservation.md` |
| Authenticity / reliability / integrity / fixity / usability | `synthesis/CONCEPT-BOUNDARIES.md` | `SOURCES.md`, `sources/digital-preservation.md` |
| Provenance / lineage / derivation | `FOUNDATIONAL-SYNTHESIS.md` | `sources/provenance-identity-time-versioning.md` |
| Identity / version / logical name / content hash | `FOUNDATIONAL-SYNTHESIS.md` | `sources/provenance-identity-time-versioning.md` |
| Temporal semantics | `FOUNDATIONAL-SYNTHESIS.md` | `sources/provenance-identity-time-versioning.md` |
| Bilgi nasıl organize edilir / bulunur? | `FOUNDATIONAL-SYNTHESIS.md` | `sources/organization-retrieval-lifecycle.md` |
| Retention / deletion / disposition | `FOUNDATIONAL-SYNTHESIS.md` | `sources/organization-retrieval-lifecycle.md` |
| Failure modes | `synthesis/FAILURE-MODES.md` | ilgili source ledger |
| Hâlâ çözülmemiş sorular | `OPEN-QUESTIONS.md` | ilgili synthesis/source ledger |
| Pass neden burada durdu? | `synthesis/RETURN-CONDITION-REVIEW.md` | `RESEARCH-PLAN.md` |
| Work / Actors ile karşılaşılan ilişkiler | `DEFERRED-RELATIONS.md` | diğer vertical'lar tamamlandıktan sonra |

## Epistemik statü

- `SOURCES.md` = bu pass'in konsolide source ledger'ı; birincil kaynak yerine geçmez.
- `sources/` = daha ayrıntılı ve konu-bazlı source ledger'lar; `SOURCES.md`'ye tabidir.
- `FOUNDATIONAL-SYNTHESIS.md` = completed foundational pass'in ana bounded sentezi; SOUL architecture kararı değildir.
- `synthesis/` = ana sentezi açıklayan destekleyici kavram/failure/review modülleri; ikinci bir foundational synthesis içermez.
- `OPEN-QUESTIONS.md` = bir sonraki internal Records araştırmasının aday soru kuyruğu; execution yetkisi değildir.
- `DEFERRED-RELATIONS.md` = bu vertical sırasında görülen fakat burada çözülmeyen cross-vertical sorular.

`records-artifacts` adı ve mevcut kavram şeması provisional'dır. Araştırma yeni ayrımlar gösterirse paket açıkça yeniden çerçevelenebilir.