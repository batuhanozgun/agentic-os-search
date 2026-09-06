# SOUL Context — INDEX

## Rol

Bu dosya `research/soul-context/**` için **retrieval router**'dır. Bir claim'in kanıtı değildir ve kaynak yerine kullanılmaz.

Amaç: her yeni konuşmada tüm context corpus'unu yeniden tam okumadan, soruya göre yalnız gerekli dosyalara inmek.

## Context yüzeyleri

- `evidence/` — source-grounded context syntheses.
- `repos/` — predecessor/current source ledgers.
- `current/` — bounded current operational/cross-project transition context. Development veya Production current-state authority'sinin yerine geçmez.
- `current/briefs/` — kullanıcı tarafından Codex'e iletilecek sürümlü görev tanımları; bulunmaları çalıştırıldıkları veya kabul edildikleri anlamına gelmez.
- `current/reviews/` — kullanıcı tarafından aktarılan Codex yanıtları ve ayrı research-side değerlendirmeler; kaynak metin, inceleme, kabul ve uygulama birbirinin yerine geçmez. Candidate study veya Foundation bulgusu değildir.
- `exploratory/` — erken/provisional research-design/taxonomy/holdout fikirleri; local/provisional only.

## Varsayılan okuma sırası

1. Bu `INDEX.md`.
2. Soru current cross-project transition / Development OS bootstrap ile ilgiliyse önce **`STATE.md`**: güncel research-side bridge checkpoint ve next action burada yaşar.
3. Ardından `current/DEVELOPMENT-OS-BOOTSTRAP.md`: amaç, vizyon, nedenler, tarihsel gözlemler ve aşama koşulları.
4. Güncel görev için STATE'in işaretlediği brief, yanıt/inceleme veya hedef repository'nin canonical state'i.
5. Tarihsel/source-grounded context claim'i için ilgili `evidence/` ve gerektiğinde `repos/` ledger'ı.
6. Exact, tartışmalı, güncellik-kritik veya load-bearing claim için birincil repo kaynağı / current target-repository state.

`exploratory/` yalnız kullanıcı açıkça erken/provisional araştırma fikirlerini istediğinde veya belirli bir frame'i karşılaştırmak gerektiğinde açılır.

## Topic / claim routing

| Konu / soru | Epistemik statü | Önce okunacak | Gerekirse derine in |
|---|---|---|---|
| SOUL Research neden açıldı? | bounded synthesis; direct + inference ayrımı korunur | `evidence/CONTEXT-SYNTHESIS.md` | `evidence/transition-to-soul.md`, `repos/soul/README.md`, `repos/os-architect/README.md` |
| Batu araştırma sonrasında ne tür bir yapı kurmak istiyor? | primary-source supported bounded synthesis + later user direction | `STATE.md` → `current/DEVELOPMENT-OS-BOOTSTRAP.md` | `evidence/CONTEXT-SYNTHESIS.md`, `repos/soul/README.md` |
| SOUL neden first-principles rebuild? | direct predecessor SOUL + historical synthesis | `evidence/transition-to-soul.md` | `repos/soul/README.md`, `repos/os-architect/README.md` |
| SOUL'un ürün yönü nedir? | current user direction; predecessor intent is supporting context | `STATE.md` → `current/DEVELOPMENT-OS-BOOTSTRAP.md` | current target-repository state; `evidence/CONTEXT-SYNTHESIS.md` |
| Development OS neden product architecture'dan önce? | predecessor intent + current bootstrap direction | `current/DEVELOPMENT-OS-BOOTSTRAP.md` | `evidence/CONTEXT-SYNTHESIS.md`, `repos/soul/README.md` / WP-000 source pointer |
| Yeni `soul-development-os` ve `soul-production` neden açıldı; eski `soul` neden active surface değil? | current authorised transition context; not architecture truth | `STATE.md` → `current/DEVELOPMENT-OS-BOOTSTRAP.md` | target repos + old `soul` source when exact state/history matters |
| ChatGPT ↔ Codex geçici bootstrap iş bölümü nedir; ne zaman biter? | current operational bridge | `STATE.md` → `current/DEVELOPMENT-OS-BOOTSTRAP.md` | `soul-development-os` current state once canonical bootstrap exists |
| Research → Development → Production authority sınırı nasıl kuruluyor? | operational boundary + earlier direct governance context | `current/DEVELOPMENT-OS-BOOTSTRAP.md` | `evidence/research-architecture-boundary.md`, target-repository state |
| Codex bootstrap'ta nerede kaldık; clone/binding/preflight tekrar gerekli mi? | current bridge checkpoint; observations qualified by source | **`STATE.md`** | current Codex report / `soul-development-os` actual state; context note for history |
| Codex'e sırada hangi mesaj/görev verilecek? | prepared assignment is not execution or acceptance | **`STATE.md`** | named `current/briefs/` file; review target/authority before relay |
| İlk üç-yüzey Development OS önerisi tam olarak neydi? | user-relayed Codex design candidate; not accepted | `current/reviews/2026-09-06-stage-1/CODEX-RESPONSE.md` | issued S1 brief; `STATE.md` for disposition |
| S1 neden doğrudan kurulmadı; başlangıç düşünme sözleşmesi/B-C/tek yazıcı/test sorunları ne? | bounded review and proposed clarification; not runtime verification | `current/reviews/2026-09-06-stage-1/REVIEW.md` | original response, cited primary sources; current brief via `STATE.md` |
| KEEL → SOUL tarihsel geçişi | direct evidence + bounded inference; source gap açık | `evidence/transition-to-soul.md` | `repos/os-architect/README.md`, `repos/soul/README.md` |
| Eski workspace / KEEL failure dersleri | reconstructed source evidence | `repos/os-architect/README.md` | exact `os-architect` paths/SHAs |
| KEEL'in hangi mekanizmaları gerçekten kod/test karşılığı taşıyor? | selective mechanical counter-read; fresh execution sınırlı | `repos/keel/README.md` | exact `keel` paths/SHAs |
| Predecessor research-house / keel-research ne söyledi? | bounded prior-art; SOUL authority değil | `repos/keel-research/README.md` | exact `keel-research` source pointer |
| Research finding ile architecture decision aynı mı? | direct predecessor governance + bounded context | `evidence/research-architecture-boundary.md` | `repos/soul/README.md`, `repos/keel-research/README.md` |
| Erken D1–D11 / V1–V4 / holdout / stopping fikirleri neydi? | **LOCAL / PROVISIONAL / NOT PROMOTED** | `exploratory/README.md` | ilgili `exploratory/*.md` |

## Kaynak-fidelity kuralları

- Bu indexte `direct` yazması exact wording'in burada kanıtlandığı anlamına gelmez; ilgili evidence/ledger ve gerekirse primary source açılır.
- Current bridge checkpoint'in tek authoritative evi `STATE.md`'dir. Context note'un tarihsel bir blocker'ını daha yeni checkpoint'e üstün tutma.
- `current/` hedef repo'nun current-state authority'sinin yerine geçmez; freshness/load-bearing durumda hedef repository'ye dön.
- Kullanıcının aktardığı Codex/local sonuçları, research assistant'ın doğrudan GitHub gözlemleri ve çıkarımlar ayrı tutulur.
- Bir yanıtın saklanan kopyasının hash eşleşmesi içerik doğruluğunu veya o ajanın bütün okuma/mutation beyanlarını doğrulamaz.
- Retrieval miss, source absence değildir.
- Ledger'daki kısa özet kaynak gövdesinin yerine geçmez.
- `exploratory/` içeriği eski repo bilgisinin bir parçası gibi sunulmaz.
- Bir source branch/ref veya execution environment değişmişse current observation olmadan current truth varsayılmaz.

## Hızlı continuation

- Eski repo / proje bağlamı: ilgili `evidence/` veya `repos/` route'u.
- Yeni Development OS bootstrap: **`STATE.md` → `current/DEVELOPMENT-OS-BOOTSTRAP.md` → STATE'te adlandırılan yanıt/inceleme/brief veya target state**.
- Bootstrap işi tamamlandı sanılmamalı: hazırlanmış brief, gönderilmiş görev, gelen sonuç, kabul ve uygulama farklı durumlardır.

Yeni context research yapılacaksa önce `STATE.md` ve ilgili route açılır; tüm ledger/notes setini topluca okumak default değildir.
