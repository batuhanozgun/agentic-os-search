# Records / Artifacts — INDEX

## Rol

Bu dosya `records-artifacts/**` araştırması için retrieval router'dır. Bir bulgunun kanıtı veya source-of-truth'u değildir.

## Varsayılan okuma sırası

1. Güncel durum ve yetki sınırı için `STATE.md`.
2. Güncel object-boundaries sonucu için `synthesis/OBJECT-BOUNDARIES.md` ve artifact hükmünün adversarial düzeltmesi için `synthesis/ARTIFACT-COUNTERCHECK.md`.
3. Önceki foundational zemini gerekiyorsa `FOUNDATIONAL-SYNTHESIS.md`.
4. İlgili iddianın konsolide kaynak izi için `SOURCES.md` ve pass-specific source ledger'lar.
5. Exact veya tartışmalı claim için ledger içindeki birincil kaynağa dön.

## Topic routing

| Konu | Önce oku | Gerekirse derine in |
|---|---|---|
| Güncel Records araştırma durumu / yetkili iş | `STATE.md` | `OPEN-QUESTIONS.md` |
| Object-boundaries pass'in amacı ve dönüş koşulu | `OBJECT-BOUNDARIES-PLAN.md` | `STATE.md` |
| Recordhood: bir şey ne zaman record olur? | `synthesis/OBJECT-BOUNDARIES.md` | `sources/object-boundaries-recordhood.md`, `FOUNDATIONAL-SYNTHESIS.md` |
| Resource / record / representation / copy / version / derivation / aggregation sınırları | `synthesis/OBJECT-BOUNDARIES.md` | `sources/object-boundaries-recordhood.md` |
| `Artifact` için güncel hüküm | `synthesis/ARTIFACT-COUNTERCHECK.md` | `synthesis/OBJECT-BOUNDARIES.md`, `sources/artifact-counterframe.md`, `sources/object-boundaries-recordhood.md` |
| Record nedir? — foundational zemin | `FOUNDATIONAL-SYNTHESIS.md` | `SOURCES.md`, `sources/records-archival-science.md`, `sources/term-boundaries.md` |
| Bilgi / data / record / state / event / claim / evidence ayrımları | `synthesis/CONCEPT-BOUNDARIES.md` | `FOUNDATIONAL-SYNTHESIS.md`, `SOURCES.md` |
| Bits/content neden tek başına yeterli değil? | `FOUNDATIONAL-SYNTHESIS.md` | `sources/digital-preservation.md` |
| Authenticity / reliability / integrity / fixity / usability | `synthesis/CONCEPT-BOUNDARIES.md` | `SOURCES.md`, `sources/digital-preservation.md` |
| Provenance / lineage / derivation | `FOUNDATIONAL-SYNTHESIS.md` | `sources/provenance-identity-time-versioning.md`, `sources/object-boundaries-recordhood.md` |
| Identity / version / representation / copy | `synthesis/OBJECT-BOUNDARIES.md` | `sources/object-boundaries-recordhood.md`, `sources/provenance-identity-time-versioning.md` |
| Temporal semantics | `FOUNDATIONAL-SYNTHESIS.md` | `sources/provenance-identity-time-versioning.md` |
| Bilgi nasıl organize edilir / bulunur? | `FOUNDATIONAL-SYNTHESIS.md` | `sources/organization-retrieval-lifecycle.md` |
| Retention / deletion / disposition | `FOUNDATIONAL-SYNTHESIS.md` | `sources/organization-retrieval-lifecycle.md` |
| Failure modes | `synthesis/FAILURE-MODES.md` | ilgili source ledger |
| Hâlâ çözülmemiş / sonraki yüksek-bilgi soruları | `OPEN-QUESTIONS.md` | ilgili synthesis/source ledger |
| Foundational pass neden durdu? | `synthesis/RETURN-CONDITION-REVIEW.md` | `RESEARCH-PLAN.md` |
| Object-boundaries pass neden durdu? | `synthesis/OBJECT-BOUNDARIES.md` section 10 | `OBJECT-BOUNDARIES-PLAN.md` |
| Work / Actors ile karşılaşılan ilişkiler | `DEFERRED-RELATIONS.md` | diğer vertical'lar tamamlandıktan sonra |

## Epistemik statü

- `SOURCES.md` = foundational pass'in konsolide source ledger'ı; birincil kaynak yerine geçmez.
- `sources/` = konu/pass-bazlı source ledger'lar; exact claim'de primary source'a geri dönülür.
- `FOUNDATIONAL-SYNTHESIS.md` = foundational pass'in bounded sentezi.
- `synthesis/OBJECT-BOUNDARIES.md` = object-boundaries pass'in ana bounded sentezi; SOUL architecture kararı değildir.
- `synthesis/ARTIFACT-COUNTERCHECK.md` = artifact hükmüne son adverse-evidence düzeltmesi; artifact ile ilgili okumada ana sentezle birlikte kullanılmalıdır.
- `OPEN-QUESTIONS.md` = current internal Records research queue; execution yetkisi değildir.
- `DEFERRED-RELATIONS.md` = bu vertical sırasında görülen fakat burada çözülmeyen cross-vertical sorular.

`records-artifacts` adı provisional'dır. Object-boundaries pass, niteliksiz `artifact`ı foundational Records super-category olarak desteklememiştir; fakat doğru broader persistent-information kategorisi henüz çözülmediği için package adı otomatik değiştirilmez.