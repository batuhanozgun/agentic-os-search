# SOUL Context — INDEX

## Rol

Bu dosya `research/soul-context/**` için **retrieval router**'dır. Bir claim'in kanıtı değildir ve kaynak yerine kullanılmaz.

Amaç: her yeni konuşmada tüm context corpus'unu yeniden tam okumadan, soruya göre yalnız gerekli dosyalara inmek.

## Context yüzeyleri

- `evidence/` — source-grounded context syntheses.
- `repos/` — predecessor/current source ledgers.
- `current/` — chat/model hafızasında kalmaması gereken bounded **current operational/cross-project transition context**. Development veya Production current-state authority'sinin yerine geçmez.
- `exploratory/` — erken/provisional research-design/taxonomy/holdout fikirleri; local/provisional only.

## Varsayılan okuma sırası

1. Bu `INDEX.md`.
2. Soru current cross-project transition / Development OS bootstrap ile ilgiliyse ilgili `current/` dosyası.
3. Tarihsel/source-grounded context claim'i ise ilgili `evidence/` dosyası.
4. Gerekirse ilgili `repos/` ledger bölümü.
5. Exact, tartışmalı, güncellik-kritik veya load-bearing claim için birincil repo kaynağı / current target-repository state.

`exploratory/` yalnız kullanıcı açıkça erken/provisional araştırma fikirlerini istediğinde veya belirli bir frame'i karşılaştırmak gerektiğinde açılır.

## Topic / claim routing

| Konu / soru | Epistemik statü | Önce okunacak | Gerekirse derine in |
|---|---|---|---|
| SOUL Research neden açıldı? | bounded synthesis; direct + inference ayrımı korunur | `evidence/CONTEXT-SYNTHESIS.md` | `evidence/transition-to-soul.md`, `repos/soul/README.md`, `repos/os-architect/README.md` |
| Batu araştırma sonrasında ne tür bir yapı kurmak istiyor? | primary-source supported bounded synthesis | `evidence/CONTEXT-SYNTHESIS.md` | `repos/soul/README.md` |
| SOUL neden first-principles rebuild? | direct SOUL + historical synthesis | `evidence/transition-to-soul.md` | `repos/soul/README.md`, `repos/os-architect/README.md` |
| SOUL'un current ürün yönü nedir? | direct SOUL | `evidence/CONTEXT-SYNTHESIS.md` | `repos/soul/README.md` ve oradaki exact source pointers |
| Development OS neden product architecture'dan önce? | direct SOUL | `evidence/CONTEXT-SYNTHESIS.md` | `repos/soul/README.md` / WP-000 source pointer |
| Yeni `soul-development-os` ve `soul-production` neden açıldı; eski `soul` neden active surface değil? | current authorised transition context; not architecture truth | `current/DEVELOPMENT-OS-BOOTSTRAP.md` | target repos + old `soul` source when exact state/history matters |
| ChatGPT ↔ Codex geçici bootstrap iş bölümü nedir; ne zaman biter? | current operational/authority bridge | `current/DEVELOPMENT-OS-BOOTSTRAP.md` | `soul-development-os` current state once canonical bootstrap exists |
| Research → Development → Production authority sınırı şu anda nasıl kuruluyor? | current operational boundary + earlier direct governance context | `current/DEVELOPMENT-OS-BOOTSTRAP.md` | `evidence/research-architecture-boundary.md`, current target-repository state |
| Current Codex bootstrap environment / immediate next bootstrap step nedir? | current operational observation; freshness-sensitive | `current/DEVELOPMENT-OS-BOOTSTRAP.md` | current Codex environment / `soul-development-os` actual state |
| KEEL → SOUL tarihsel geçişi | direct evidence + bounded inference; source gap açık | `evidence/transition-to-soul.md` | `repos/os-architect/README.md`, `repos/soul/README.md` |
| Eski workspace / KEEL failure dersleri | reconstructed source evidence | `repos/os-architect/README.md` | exact `os-architect` paths/SHAs |
| KEEL'in hangi mekanizmaları gerçekten kod/test karşılığı taşıyor? | selective mechanical counter-read; fresh execution sınırlı | `repos/keel/README.md` | exact `keel` paths/SHAs |
| Predecessor research-house / keel-research ne söyledi? | bounded prior-art; SOUL authority değil | `repos/keel-research/README.md` | exact `keel-research` source pointer |
| Research finding ile architecture decision aynı mı? | direct SOUL governance + bounded predecessor context | `evidence/research-architecture-boundary.md` | `repos/soul/README.md`, `repos/keel-research/README.md` |
| Erken D1–D11 / V1–V4 / holdout / stopping fikirleri neydi? | **LOCAL / PROVISIONAL / NOT PROMOTED** | `exploratory/README.md` | ilgili `exploratory/*.md` |

## Kaynak-fidelity kuralları

- Bu indexte `direct` yazması exact wording'in burada kanıtlandığı anlamına gelmez; ilgili evidence/ledger ve gerekirse primary source açılır.
- `current/` içeriği current cross-project context'i taşır ama target repo'nun current-state authority'sinin yerine geçmez; freshness/load-bearing durumda target repository'ye dön.
- Retrieval miss, source absence değildir.
- Ledger'daki kısa özet kaynak gövdesinin yerine geçmez.
- `exploratory/` içeriği eski repo bilgisinin bir parçası gibi sunulmaz.
- Bir source branch/ref veya Codex environment değişmişse `last verified`/current observation yoksa current truth varsayılmaz.

## Hızlı continuation

- Eski repo / proje bağlamı için `INDEX.md` → ilgili `evidence/` veya `repos/` route'u yeterli başlangıçtır.
- Yeni Development OS bootstrap / üç-repo çalışma düzeni / ChatGPT↔Codex bridge için doğrudan `current/DEVELOPMENT-OS-BOOTSTRAP.md` oku.
- `STATE.md` context hattının çalışma statüsü/reopen sınırını taşır.

Yeni context research yapılacaksa önce `STATE.md` ve ilgili route açılır; tüm ledger/notes setini topluca okumak default değildir.
