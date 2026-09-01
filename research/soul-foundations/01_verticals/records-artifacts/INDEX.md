# Records / Artifacts — INDEX

## Rol

Bu dosya `records-artifacts/**` araştırması için retrieval router'dır. Bir bulgunun kanıtı veya source-of-truth'u değildir.

## Okuma sırası

1. Güncel araştırma durumu için `STATE.md`.
2. Mevcut bounded sonuç için `synthesis/FOUNDATIONAL-SYNTHESIS.md`.
3. İlgili kavram sınırı için `synthesis/CONCEPT-BOUNDARIES.md`.
4. İlgili iddianın kaynak izi için `sources/` altındaki ledger.
5. Exact veya tartışmalı iddia için ledger'daki birincil kaynağa dön.

## Topic routing

| Konu | Önce oku | Sonra |
|---|---|---|
| Record nedir? | `synthesis/FOUNDATIONAL-SYNTHESIS.md` | `sources/records-archival-science.md` |
| Record ile artifact aynı mı? | `synthesis/CONCEPT-BOUNDARIES.md` | `sources/records-archival-science.md` |
| Bits/content neden tek başına yeterli değil? | `synthesis/FOUNDATIONAL-SYNTHESIS.md` | `sources/digital-preservation.md` |
| Authenticity / reliability / integrity / fixity / usability | `synthesis/CONCEPT-BOUNDARIES.md` | `sources/digital-preservation.md` |
| Provenance / lineage / derivation | `synthesis/CONCEPT-BOUNDARIES.md` | `sources/provenance-identity-time-versioning.md` |
| Identity / version / logical name / content hash | `synthesis/CONCEPT-BOUNDARIES.md` | `sources/provenance-identity-time-versioning.md` |
| Zaman nasıl modellenir? | `synthesis/CONCEPT-BOUNDARIES.md` | `sources/provenance-identity-time-versioning.md` |
| Bilgi nasıl organize edilir / bulunur? | `synthesis/FOUNDATIONAL-SYNTHESIS.md` | `sources/organization-retrieval-lifecycle.md` |
| Retention / deletion / disposition | `synthesis/FOUNDATIONAL-SYNTHESIS.md` | `sources/organization-retrieval-lifecycle.md` |
| Failure modes | `synthesis/FAILURE-MODES.md` | ilgili source ledger |
| Hâlâ çözülmemiş sorular | `synthesis/OPEN-QUESTIONS.md` | ilgili source ledger |
| Work / Actors ile karşılaşılan ilişkiler | `DEFERRED-RELATIONS.md` | diğer vertical'lar tamamlandıktan sonra |

## Epistemik statü

- `sources/` = kaynak okuma defterleri; özetleri kaynak yerine geçmez.
- `synthesis/` = kaynaklardan türetilmiş bounded araştırma sonucu; SOUL architecture kararı değildir.
- `DEFERRED-RELATIONS.md` = bu vertical sırasında görülen fakat burada çözülmeyen cross-vertical sorular.

`records-artifacts` adı ve mevcut kavram şeması provisional'dır. Araştırma yeni ayrımlar gösterirse paket açıkça yeniden çerçevelenebilir.