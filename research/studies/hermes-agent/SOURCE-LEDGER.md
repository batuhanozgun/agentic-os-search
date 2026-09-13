# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-13 / U13 / plan v0.26.** Work authority [STATE](STATE.md). Primary c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a / manifest0.21.0. Kaynak okuma, seçki diagnostic, ürün davranışı, sentez ve publication farklı statülerdir.

## U13 — Consumer kaynakları ve seçki koşusu

[Note28](notes/28-DELEGATION-COMPLETION-AND-PARENT-REENTRY.md)→[A RESEARCH](evidence/2026-09-13-delegation-reentry/RESEARCH.md)/[SOURCES S01–S08](evidence/2026-09-13-delegation-reentry/SOURCES.md). S01 async ledger önceki U12 full read reuse; S02 ProcessRegistry, S03 notification format, S04 TUI notifications, S05 prompt-turn, S06 CLI ve S07 chat selected; S08 facade full yeniden okundu. B sonrası S04/S05 branch'leri second-pass karşı okundu, license full+exact blob eşleşti. Primary yükseltilmedi; current docs ve default-branch sonuçları ayrı navigation'dır.

[B DIAGNOSTIC](evidence/2026-09-13-delegation-reentry/DIAGNOSTIC.md)→[SPEC](evidence/2026-09-13-delegation-reentry/SPEC.md)→[MANIFEST](evidence/2026-09-13-delegation-reentry/MANIFEST.json)→[raw](evidence/2026-09-13-delegation-reentry/diagnostic-evidence.tar.xz). Sekiz manuel seçilmiş işlev, D01–D08/N01–N02; **bir** recorded invocation 2026-09-13T04:01:40.644076+00:00–04:01:40.658275+00:00. Model worker execution0, SQL0; full-parent byte/AST fidelity false. Raw RESULT SHA25620e39d3c07c6d61a2e5e3dea7344baf62af52b6ffd6d9f59911ab1cce93e93f1, probe5d61c37dd003a080896ff72f79f7119d7efb05269f92c4392da5ef9a9708ea3c.

Archive9756bytes/11files, SHA2560518ab011705b951db2d5776411be5d2f9080b8d4f09ffa6be9063e45570c7c5, Git798d00149d800ad52fb604a36dca70e1b384e995. B source identities actual selected text'e aittir, parent modules'a değil. D02/03/04/07 I1 ve D05 I2 violation-in-selection; iki mutant observation sensitivity. Derived RESULT-SUMMARY raw yerine kullanılmaz.

Opening899422ceba05f7b6a577b35baf6a985c317b7cf7; A/SPEC2ef205a9bf13d166c15a630e4320dd73eb190fb2 main readback önce, B execution sonra; B1372287c9b0806c1d0103cc1c9351bcf4dd69b08 main readback önce, [coverage review](inventory/SCOPE-REVIEW-2026-09-13-U13.md) sonra. [PUBLICATION](evidence/2026-09-13-delegation-reentry/PUBLICATION.md) gerçek scope/ref/readback sınırını taşır; yeni bağımsız behavioral verification değildir.

## Korunan önceki doğrudan kanıt yolları

| Birim | Source/ham kanıta giriş |
|---|---|
| U12 tool/delegation | [A](evidence/2026-09-13-tool-delegation/TOOL-ADMISSION.md)/[A SOURCES](evidence/2026-09-13-tool-delegation/TOOL-SOURCES.md), [B](evidence/2026-09-13-tool-delegation/DELEGATION-LIFECYCLE.md)/[B SOURCES](evidence/2026-09-13-tool-delegation/DELEGATION-SOURCES.md), [NOT RUN](evidence/2026-09-13-tool-delegation/CHECKS-NOT-RUN.md)/[PUBLICATION](evidence/2026-09-13-tool-delegation/PUBLICATION.md); yeni koşu yoktu |
| U11 runtime/backend | [A SOURCES](evidence/2026-09-12-runtime-backend/SOURCES.md)/[B SOURCES](evidence/2026-09-12-runtime-backend/BACKEND-SOURCES.md)/[PUBLICATION](evidence/2026-09-12-runtime-backend/PUBLICATION.md); source-only |
| U10 execution/context | [SOURCES](evidence/2026-09-12-cron-execution-context/SOURCES.md)/[SPEC](evidence/2026-09-12-cron-execution-context/SPEC.md)/[RESULT](evidence/2026-09-12-cron-execution-context/RESULT.json)/[MANIFEST](evidence/2026-09-12-cron-execution-context/MANIFEST.json); C01–C06 yalnız local-file selector, first parse failure korunur |
| U09 occurrence | [SOURCES](evidence/2026-09-12-cron-occurrence-admission/SOURCES.md)/[RESEARCH](evidence/2026-09-12-cron-occurrence-admission/RESEARCH.md); source-only |
| U08 cancellation/drain | [SOURCES](evidence/2026-09-12-cron-drain-receipts/SOURCES.md)/[RESEARCH](evidence/2026-09-12-cron-drain-receipts/RESEARCH.md)→SPEC/RESULT/MANIFEST/raw; native async bridge/synthetic send |
| U07 cron/queue | [SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md)→SPEC/RESULT/MANIFEST/raw; queue/temp SQLite |
| U06 resume | [SOURCES](evidence/2026-09-11-resume-admission/SOURCES.md)/[RESEARCH](evidence/2026-09-11-resume-admission/RESEARCH.md)→SPEC/RESULT/MANIFEST/raw; process-local lease |
| U05 lease/history | [SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md); source-only |
| U04-A/B | [A SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [B RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md)/[33-file manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json); separate raw/probe IDs |
| U03/U02 | [Kanban SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md), [turn SOURCES](evidence/2026-09-10-turn-lifecycle/SOURCES.md) |

[Exact U12 ledger](https://github.com/batuhanozgun/agentic-os-search/blob/74c5e3d1dcd260a1841c64dda5fb1d182f7bb299/research/studies/hermes-agent/SOURCE-LEDGER.md) bütün önceki source/hash/date/reading/failed-attempt ayrıntısını; [through-v0.9](SOURCE-LEDGER-THROUGH-V0.9.md) erken kayıtları korur. Önceki raw/evidence taşınmadı, tekrar koşulmadı. U04-B33 original subtree d01c92f7414713300934be3bb4e3d40ac57631b3 değişmez.

Q58 henüz kaynak araştırması değildir; yalnız coverage kararı/next route. U13 mevcut source+diagnostic+publication'ın sınırları eski Q40/Q42/Q47–56 ve quality/fidelity borçlarını kapatmaz. License identity dışındaki seçim hash'leri full-parent fidelity anlamına gelmez.
