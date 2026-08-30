# SOUL Context — INDEX

## Rol

Bu dosya `research/soul-context/**` için **retrieval router**'dır. Bir claim'in kanıtı değildir ve kaynak yerine kullanılmaz.

Amaç: her yeni konuşmada tüm context corpus'unu yeniden tam okumadan, soruya göre yalnız gerekli dosyalara inmek.

## Varsayılan okuma sırası

1. Bu `INDEX.md`.
2. İlgili konu için işaretlenen `evidence/` dosyası.
3. Gerekirse ilgili `repos/` ledger bölümü.
4. Exact, tartışmalı, güncellik-kritik veya load-bearing claim için birincil repo kaynağı.

`exploratory/` yalnız kullanıcı açıkça erken/provisional araştırma fikirlerini istediğinde veya belirli bir frame'i karşılaştırmak gerektiğinde açılır.

## Topic / claim routing

| Konu / soru | Epistemik statü | Önce okunacak | Gerekirse derine in |
|---|---|---|---|
| SOUL Research neden açıldı? | bounded synthesis; direct + inference ayrımı korunur | `evidence/CONTEXT-SYNTHESIS.md` | `evidence/transition-to-soul.md`, `repos/soul/README.md`, `repos/os-architect/README.md` |
| Batu araştırma sonrasında ne tür bir yapı kurmak istiyor? | primary-source supported bounded synthesis | `evidence/CONTEXT-SYNTHESIS.md` | `repos/soul/README.md` |
| SOUL neden first-principles rebuild? | direct SOUL + historical synthesis | `evidence/transition-to-soul.md` | `repos/soul/README.md`, `repos/os-architect/README.md` |
| SOUL'un current ürün yönü nedir? | direct SOUL | `evidence/CONTEXT-SYNTHESIS.md` | `repos/soul/README.md` ve oradaki exact source pointers |
| Development OS neden product architecture'dan önce? | direct SOUL | `evidence/CONTEXT-SYNTHESIS.md` | `repos/soul/README.md` / WP-000 source pointer |
| KEEL → SOUL tarihsel geçişi | direct evidence + bounded inference; source gap açık | `evidence/transition-to-soul.md` | `repos/os-architect/README.md`, `repos/soul/README.md` |
| Eski workspace / KEEL failure dersleri | reconstructed source evidence | `repos/os-architect/README.md` | exact `os-architect` paths/SHAs |
| KEEL'in hangi mekanizmaları gerçekten kod/test karşılığı taşıyor? | selective mechanical counter-read; fresh execution sınırlı | `repos/keel/README.md` | exact `keel` paths/SHAs |
| Predecessor research-house / keel-research ne söyledi? | bounded prior-art; SOUL authority değil | `repos/keel-research/README.md` | exact `keel-research` source pointer |
| Research finding ile architecture decision aynı mı? | direct SOUL governance + bounded predecessor context | `evidence/research-architecture-boundary.md` | `repos/soul/README.md`, `repos/keel-research/README.md` |
| Erken D1–D11 / V1–V4 / holdout / stopping fikirleri neydi? | **LOCAL / PROVISIONAL / NOT PROMOTED** | `exploratory/README.md` | ilgili `exploratory/*.md` |

## Kaynak-fidelity kuralları

- Bu indexte `direct` yazması exact wording'in burada kanıtlandığı anlamına gelmez; ilgili evidence/ledger ve gerekirse primary source açılır.
- Retrieval miss, source absence değildir.
- Ledger'daki kısa özet kaynak gövdesinin yerine geçmez.
- `exploratory/` içeriği eski repo bilgisinin bir parçası gibi sunulmaz.
- Bir source branch/ref değişmişse `last verified` bilgisi yoksa current truth varsayılmaz.

## Hızlı continuation

Bu context hattı yalnız eski repo bilgisini geri çağırmak için açılıyorsa `README.md + INDEX.md` çoğu durumda yeterli başlangıçtır. `STATE.md` yalnız hattın çalışma statüsü veya yeniden açılma sınırı gerektiğinde okunur.

Yeni context araştırması yapılacaksa önce `STATE.md` ve ilgili ledger açılır; tüm ledger/notes setini topluca okumak default değildir.
