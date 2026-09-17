# ECC — Research Round Log

Append-only chronological record of bounded work; current work authority remains STATE. Corrections may be appended with links; historical facts are not silently rewritten. This is a research/work rationale log, not a verbatim conversation or private reasoning transcript.

## U00 — 2026-09-17 — Method and plan establishment

**Authorized request:** kullanıcı önce yöntem ve değişebilir plan istedi; repo'nun araştırmayı beslemesi/yönetmesi, turlar ve oturumlarda güncel tutulması, yöntemin de araştırmayla birlikte değerlendirilen bir örnek olarak korunması istendi.

**Input state:** ECC ön taraması conversation'daydı, `research/studies/ecc/` input main `e3af9d9fc40391ebb31b2a8972fd5e1b7994d52f` üzerinde yoktu (exact-path Contents API 404). Diğer studies katalog/index'e kayıtlıydı; Superpowers'ın yeni kayıtları görüldü ve korunacak.

**Work performed:** gstack, Hermes ve Superpowers METHOD dosyaları tam okundu; güncel Foundation STATE, discussion handoff ve REUSE recover edildi. ECC main direct ref ile sabitlendi; cross-harness dokümanı pinned tam okundu; manifest 1–45 satır seçili okundu. Ön taramanın full/partial/truncated farkları kayda geçirildi. Ayrıntı SOURCE-LEDGER'da.

**Research output:** ECC hakkında yeni runtime/effectiveness sonucu değil; bounded araştırma amacı, sabit kaynak referansı, provisional soru aileleri, iki-döngülü yöntem, esnek faz planı, cold-start/authority, question/source kayıtları ve ilk yöntem değerlendirmesi. Ürün kurulmadı; upstream testleri çalıştırılmadı.

**Method delta:** Ön taramadaki yedi konu nihai subsystem şeması kabul edilmedi. Yalnız portability odağının native discovery'yi daraltmaması, doküman statüsünün current runtime'a yükseltilmemesi, plan/yöntem revizyonlarının sonuçlarıyla kaydedilmesi eklendi. MR00, alternatifleri ve henüz gözlenmemiş etkiyi taşır.

**Project context effect:** Foundation'da genel derinleştirme yerine yeterli-durma/seçici-reuse yönü recover edildi. Bu bilgi geç projeksiyonun çapasını güncelledi; Foundation veya hedef geliştirme işi değiştirilmedi.

**Operational boundary:** Container'dan yardımcı doğrudan GitHub erişimi DNS çözümlemesinde başarısız oldu. Canonical GitHub connector okumaları başarılıydı; onun üzerinden yayın yolu seçildi. Bu olay ECC arızası veya GitHub genel kesintisi olarak yorumlanmadı. Yerel ECC checkout/host capability hazır varsayılmaz.

**Publication:** içerik hazırlığı ve GitHub yayını ayrı eylemlerdir. Gerçek commit/scope/readback receipt PUBLICATION.md oluşturulduğunda orada bulunur. Bu log tamamlanmış runtime testi veya independent cold-start iddiası taşımaz.

**Return:** yöntem/plan kullanıcıya sunulur; bu tur U01 başlatılmaz. Next logical U01 kapsamı PLAN'da, yetkisi STATE'te.

## Later-round record template

`Unit / date / input main / method-plan versions`

- Authorized question, scope and return condition.
- Actual source/dependency coverage; source or local/live execution distinctions.
- Bounded finding and what changed in the system model; strongest rival/counterexample and unresolved limit.
- Impact on QUESTIONS, notes/syntheses and next work.
- Method check: adequate / change needed / insufficient evidence; linked MR entry when material.
- Published artifacts, commit/readback status, interruption or capability boundary.
- Exact next question/first source, authorization/stop boundary and reason for its priority.

Template alanları gereksiz tekrar için değil, yeni oturumun doğru işi devralması içindir. Salt açıklama turu maddi state değiştirmiyorsa yeni log dosyası veya commit kotası yoktur.

## U01-A — 2026-09-17 — Source surfaces and cache-verifier falsifier

**Authorization:** after U00 the user wrote 'harika. devam edebilirsin.' The source study continued; no installation, host/user state change, upstream reporting or architecture work was authorised. Same-conversation canonical STATE and entry identities were recovered; WHY, QUESTIONS, SOURCE-LEDGER and this log were additionally read in full. This is not an independent cold-start experiment.

**Source binding:** ECC remains pinned at `8321021c54d670126ce3b2969d5deb880b4b0c2a`. The project main used for initial publication staging was `5272ee899d575c1be99c4467295d5cc00f34a2e0`; any later rebase and actual publication belong in PUBLICATION. Other sessions' study/catalog changes must be preserved.

**Actual work:** root non-recursive Git tree recovered in full, four selected direct-child lists read, package manifest and selected entry/provider/hook/test files read. Exact S02–S25 scope is in [U01-A sources](evidence/U01-A-SOURCES.md). [STRUCTURE](inventory/STRUCTURE.md) and [TREE-FRONTIER](inventory/TREE-FRONTIER.tsv) preserve the shallow map and 43 root-directory identities. The recursive tree, installer dependency closure and complete README remain open.

**Substantive result:** [Note 01](notes/01-SURFACES-AND-CODEX-CACHE.md) distinguishes npm/Node, Rust and native Workflow pilot surfaces. It corrects the broad Codex instruction-backed screening description using the pinned provider manifest and SessionStart projection, while keeping actual host trust/consumption untested. The shared bootstrap was followed only through the runner; session-start body and other helpers remain outside this slice.

**Actual local execution:** [E01](evidence/u01-a-cache-probe/README.md) used unchanged checker and manifest bytes, verified against Git blob identities, synthetic caches and fake home. A pre-execution source-informed plan defined C0 presence baseline, C1 missing hook, C2 missing MCP. Actual exits were 0, 0, 1. C1 is a missing-reference false-green under the broad checker claim; C2 supplies sensitivity for a field actually checked. Dummy file contents do not represent a working plugin. The upstream native-hook test was inspected, NOT run. No Codex process, installer, network request or model call was part of E01.

**Research/method delta:** U01-A is a bounded result, not completion of all U01. PLAN 0.2 adds U01-B and QUESTIONS splits Q01a/Q01b; METHOD stays 0.1. [MR01](METHOD-REVIEW.md#mr01--2026-09-17--u01-a) records the actual correction, bounded falsifier, acquisition/recording overhead and unproven broader benefits. A potential systemic verifier-maintenance explanation remains a hypothesis; only the local omitted-field mechanism was established.

**Operational boundary:** direct container-side GitHub acquisition failed at DNS; connector reads worked. Offline Python/Node execution succeeded. No full checkout exists. Evidence files contain raw transient paths as historical output, not future locations. Tool-response truncation was not upgraded to full reading.

**Continuation:** U01-B starts with pinned install-modules.json, install-components.json and scripts/install-apply.js, then actual marketplace discovery through the .agents tree. Trace native plugin source/cache versus managed sync and preserve the other runtime/distribution families. U02 is selected only after that evidence. Existing E01 is not a new experiment to count again on re-entry. Actual commit/diff/readback details follow in [PUBLICATION](PUBLICATION.md).
