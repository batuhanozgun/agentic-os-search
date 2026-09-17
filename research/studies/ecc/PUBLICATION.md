# ECC — U00 Publication Receipt

**Date:** 2026-09-17. Bu kayıt yayın/erişim ve bounded self-review kanıtıdır; ECC runtime doğrulaması veya bağımsız yeni-oturum deneyi değildir. Current work authority STATE'tedir.

## Published sequence

| Step | Commit | Scope |
|---|---|---|
| ECC package | `07bdb0cb6f89d2d0c13e806cb5cc190a3c05d1de` | 10 yeni dosya altında `research/studies/ecc/` |
| Catalog discovery | `13444b7ee8612c7055173b077daccc9f257cd975` | CATALOG.md: yalnız 1 ECC satırı eklendi |
| Index discovery | `e328fc9fcd20c8c241b87970a8a272c180faf898` | studies INDEX.md: yalnız 1 route ve 1 package satırı eklendi |

Bu receipt yukarıdaki yayımlanmış checkpoint'i kaydeder. Kendi commit hash'ini kendi içine yazmaya çalışmaz; ardından STATE'in U00 yayın durumunu kapatan küçük güncelleme aynı package içinde yapılır.

## Actual concurrency event — preserved, not a pending merge

İlk input main `e3af9d9fc40391ebb31b2a8972fd5e1b7994d52f` idi. ECC için tree `1b1883f6747af571ea07cc2e2add1e3ac85d1c70` ve commit `057444e4ab72fc688247a8a408371f53498ba915` nesnesi oluşturuldu, fakat main güncellemesi non-fast-forward 422 ile reddedildi. Bu commit main'e yayımlanmadı.

Güncel main `4d40d238935a89f30f172f4c15fcd7c0cd573b12` olarak yeniden okundu. Exact compare yalnız `research/studies/superpowers/STATE.md` değişimini gösterdi. Yeni root tree üzerine yalnız ECC subtree `16002cd488ae2210702c57cc97f482f641aa1af6` bağlandı; commit `07bdb0c...` force olmadan main'e alındı. Ortak dosyalar güncel içerik ve blob SHA ile ayrı güncellendi.

Eski unreferenced commit nesnesi eksik yayın, açılmış branch veya kullanıcıdan beklenen merge işi değildir. Yeni branch yaratılmadı; history force edilmedi; Superpowers'ın eşzamanlı state güncellemesi korunmuştur.

## Checks actually performed

1. GitHub compare `4d40d238935a89f30f172f4c15fcd7c0cd573b12...e328fc9fcd20c8c241b87970a8a272c180faf898`: 3 commit; yalnız 10 ECC dosyası + CATALOG/INDEX değişti. Ortak dosyalarda sırasıyla 1 ve 2 ekleme, 0 silme. Foundation/control/diğer study değişikliği yok.
2. Main üzerinden ECC META, STATE, INDEX, PLAN, METHOD-REVIEW tam geri okundu. METHOD 1–59 ve 60–EOF aralıklarıyla tamamı geri okundu; iki parçada aynı blob `7a6537b4a3d953c05c3671895a718ab41fd973ff`.
3. Main CATALOG satırları 13–22 ve studies INDEX satırları 50–70 geri okundu: ECC→META→STATE/METHOD/PLAN yolu ve 'U01 not started' statüsü mevcut.
4. Bounded self-review: yöntem/plan v0.1; U00 planlama teslimatı; U01 sonraki mantıklı iş; kurulum/adoption/design yetkisi yok; prior screening tam araştırma sayılmıyor. Bu içerik tutarlılığı değerlendirmesi aynı assistant tarafından yapıldı.

Readback snapshot identities:

| File | Blob |
|---|---|
| META.md | `c38e2ee12fef5283e554a1f808e46c846138b17d` |
| INDEX.md | `f8ced6372fd7e1af89daa0b1ef3ea8bb09ebb1a1` |
| METHOD.md | `7a6537b4a3d953c05c3671895a718ab41fd973ff` |
| PLAN.md | `fbd40bcfe581531751e900f725e03eac92b8acbc` |
| METHOD-REVIEW.md | `c6edbf278ffd375d569d97bbdee2635ae78cbde8` |
| STATE.md before closure wording update | `1b91aadad6fb8214d914951c67c7c4bb14508ecc` |
| library CATALOG.md | `3e6ee9da22d2dcdb1aa30ae401fb53ab9a50084f` |
| library INDEX.md | `6a3b0bf65431ac83b51db0cafd2edb8ed2633323` |

## Method execution observation and limits

Non-force yayın kuralı bu olayda stale main'i bastırmayı engelledi; yeniden bağlama ve diff kontrolü eşzamanlı işi korudu. Bu gerçek bir operasyonel örnektir. Bütün concurrency durumlarının güvenli olduğunu veya araştırma yönteminin odağı/kaliteyi uzun vadede koruduğunu kanıtlamaz.

Bütün package dosyaları için otomatik link/semantic test suite çalıştırılmadı; named core entry readbacks ve Git diff kapsamı kontrol edildi. Gerçek cold-start ile başka bir model/oturumun doğru işi devraldığı henüz sınanmadı. ECC kurulmadı, ürün testleri veya live-host/model/effectiveness deneyleri çalıştırılmadı. U00 plan/yöntem kaydı tamamlanır; U01 kaynak haritası sonraki ayrı birimdir.

## U01-A — 2026-09-17 — Published source/local slice

The U00 receipt above is preserved historically. Current work authority remains STATE. U01-A adds real source research and a bounded local probe; broad U01 remains PARTIAL, U01-B is next, METHOD stays 0.1 and PLAN is 0.2.

| Publication | Actual commit | Scope |
|---|---|---|
| U01-A package | `3778884121b2aa48e8e0d6077d50a3c5f65e3761` | 16 ECC paths: 8 new evidence/map/note files, 8 updated entry/plan/log files |
| Catalog status | `6666d58a025cb9d1d5e01501460043886e31ec8c` | ECC row only |
| Library route | `c9c4714154b6d22109e32c955a8aa3d4454b6c5a` | ECC route only |

### Concurrency and exact scope

Initial staging used main `5272ee899d575c1be99c4467295d5cc00f34a2e0`. Before publication main was re-read at `2dc8dc326fb4ba8a2d7ba7cdf5bbae06a7922083`; compare showed new candidate entries and Superpowers state, no ECC mutation. Only the prepared ECC subtree was attached to that current tree. A non-force update of commit `e181e1608857d4437b08861d087f071ba461b3fb` was rejected with 422 because main advanced again.

The new main `b44c03032adb06ead2dee1f075e9016e42ddd72d` added two Superpowers evidence files. Its exact compare was checked; only ECC subtree `7d8f874eb6732febba184e920264a04367cacd37` was attached to current tree `2345f2df3100d75bcf3ba8c92bdddbce6860bec3`, producing the published package commit above. No force or separate branch was used. The rejected/unreferenced commit is not pending user upload or merge work.

Compare `b44c030...3778884` shows one commit and exactly 16 ECC paths; METHOD and WHY were preserved. METHOD-REVIEW, RESEARCH-LOG and SOURCE-LEDGER are additions-only, preserving the U00 records. Compare `b44c030...c9c4714` shows four commits, the 16 ECC paths, one-line replacements in CATALOG and library INDEX, plus a concurrently added Superpowers note. That extra note is not ECC work and was preserved rather than attributed to this study. No Foundation/control changes appear in either comparison.

### Readback and byte identity

Main readbacks performed: complete Note 01, STATE before final publication-wording closure, PLAN v0.2, raw RESULTS.json and PROBE-PLAN.json; current MR01 in METHOD-REVIEW; runner metadata/header; ECC catalog row and library route. The runner was not mechanically reread end-to-end from GitHub, but its returned blob identity matches the exact locally executed file. This is byte identity, not a new execution.

| Artifact | Verified Git blob |
|---|---|
| Note 01 | `972eef37fe698c576ffe9e2b84b49ade10c55f55` |
| PLAN v0.2 | `b5ff2101572bf9c2f3329fe8a473a9b217fa2584` |
| METHOD-REVIEW with MR01 | `ee620791d1981af4eacc9f95aea91918383d1a1d` |
| Probe plan, matches local bytes | `223222466e1d23b2665014b01019a9ae42a9033b` |
| Probe runner, matches executed local bytes | `589c9a31634df43fe96fc9f92c3e105b4ea4b163` |
| Raw results, matches local bytes | `de5989d3c0bcfba1d1614cb2749b961267d26249` |
| Catalog at readback | `0d828da61866bc0c5112d83348917c4eb737508a` |
| Library index at readback | `75b0c350d4f6327dbe27fd0f4e8845029799c758` |

### What these checks do not establish

E01 observed the unchanged checker against three synthetic caches, not a Codex session or real installed cache. The missing-hook challenge was a false-green; it is not three passing product tests. Upstream native-hook tests were read but not run. No full recursive inventory, registry tarball, hook-body/host execution, independent cold-start or method-effectiveness experiment was completed. No full automatic link/semantic suite was run. Source-bound notes, exact raw artifacts and explicit U01-B continuation are durable; future understanding and behavioural benefit remain separate claims.

This receipt records known published commits and completed checks; it does not self-reference its own future commit hash. A following STATE-only update closes the publication wording without advancing the study to U01-B.
