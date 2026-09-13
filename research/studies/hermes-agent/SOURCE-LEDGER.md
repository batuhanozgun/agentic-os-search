# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-13 / U14 / plan v0.27.** Work authority [STATE](STATE.md). Primaryc4a5deeffa959f8ebc891e02c5bcf767aff1dd2a / manifest0.21.0. Kaynak, seçki diagnostic, ürün davranışı, sentez ve yayın farklı statülerdir.

## U14 — Install/update/activation, yeni execution yok

[Note29](notes/29-INSTALLATION-UPDATE-AND-ACTIVATION.md)→[A INSTALL-AND-ACTIVATION](evidence/2026-09-13-install-update/INSTALL-AND-ACTIVATION.md)/[A SOURCES S01–S06](evidence/2026-09-13-install-update/INSTALL-SOURCES.md)→[B UPDATE-AND-RECOVERY](evidence/2026-09-13-install-update/UPDATE-AND-RECOVERY.md)/[B SOURCES S07–S14/S05-B](evidence/2026-09-13-install-update/UPDATE-SOURCES.md). [NOT RUN](evidence/2026-09-13-install-update/CHECKS-NOT-RUN.md), [PUBLICATION](evidence/2026-09-13-install-update/PUBLICATION.md).

S01 README, S02 pyproject, S03 install.sh, S05 main, S09 maintenance, S10 fleet, S12 dependencies selected. S04 root launcher, S06 setup.py, S07 update_cmd, S08 update_contract, S11 update_receipt, S13 update_lock, S14 early_recovery full text. Exact blobs/aralıklar source defterlerinde. **Hiçbir modül import edilmedi; installer/updater/solver/service/DB/model/OS/upstream suite çalıştırılmadı.** RESULT/PASS/raw test arşivi yoktur. Tam kaynak metni full local-byte veya dependency closure değildir.

İlk main93d6b144 U13'ü zaten içerdi; stale final PUB40a7f952 ile yalnız yayın kaydı olarak uzlaştırıldı. Q58 opening1d65fd3e actual main/ref/tam plan; A c0d64188 actual main/ref/tam A1–41+42–EOF/SOURCES/STATE; sonra B2ce9310a actual main/ref/tam B1–48+49–EOF/SOURCES/NOTRUN/STATE. Current routes ve next bunlardan sonra. A/B source text'leri sonraki final yönlendirmede değiştirilmez.

Pinned code-control flow observations ve conditional update-lock interleaving/partial-result/receipt-write çıkarımları actual yarış veya failed install değildir. Web search/defaultbranch navigation ve local raw-download başarısızlıkları A source defterinde ayrıdır; primary upgrade/current fix yok. Repository aktarım kontrolleri HERMES davranış testi değildir.

## U13 — Korunan consumer kaynakları ve seçki koşusu

[Note28](notes/28-DELEGATION-COMPLETION-AND-PARENT-REENTRY.md)→[A RESEARCH](evidence/2026-09-13-delegation-reentry/RESEARCH.md)/[SOURCES S01–S08](evidence/2026-09-13-delegation-reentry/SOURCES.md). S01 async ledger U12 reuse; S02 ProcessRegistry/S03 notification/S04 TUI/S05 prompt/S06CLI/S07chat selected; S08 facade full. Kendi B sonrası second-pass/license kayıtları kendi unit'ine aittir; U14'te yeniden doğrulanmadı.

[B DIAGNOSTIC](evidence/2026-09-13-delegation-reentry/DIAGNOSTIC.md)→[SPEC](evidence/2026-09-13-delegation-reentry/SPEC.md)→[MANIFEST](evidence/2026-09-13-delegation-reentry/MANIFEST.json)→[raw](evidence/2026-09-13-delegation-reentry/diagnostic-evidence.tar.xz). Sekiz manuel seçilmiş işlev, D01–D08/N01–N02; bir recorded invocation2026-09-13T04:01:40.644076+00:00–04:01:40.658275+00:00. Modelworker0/SQL0; full-parent fidelity false. Raw RESULT SHA25620e39d3c07c6d61a2e5e3dea7344baf62af52b6ffd6d9f59911ab1cce93e93f1; probe5d61c37dd003a080896ff72f79f7119d7efb05269f92c4392da5ef9a9708ea3c.

Archive9756bytes/11files, SHA2560518ab011705b951db2d5776411be5d2f9080b8d4f09ffa6be9063e45570c7c5, Git798d00149d800ad52fb604a36dca70e1b384e995. D02/03/04/07 I1 ve D05 I2 selection violations; iki sensitivity variant bağımsız ürün testi değil. U14 bu archive'ı tekrar decode/hash/re-run yapmadı; özgün kanıt korunur, kimlikler önceki kayıt üzerinden reusable'dır.

U13 opening899422ceba05f7b6a577b35baf6a985c317b7cf7; A/SPEC2ef205a9bf13d166c15a630e4320dd73eb190fb2; B1372287c9b0806c1d0103cc1c9351bcf4dd69b08; finalroutes93d6b14438802163ed3f542beded218e14cc51cf. [PUBLICATION](evidence/2026-09-13-delegation-reentry/PUBLICATION.md) final readback uzlaştırmasını da taşır. [Coverage](inventory/SCOPE-REVIEW-2026-09-13-U13.md) Q58'in historical yön gerekçesi, current next Q59'dur.

## Önceki doğrudan kanıt yolları

| Birim | Source/ham kanıta giriş |
|---|---|
| U12 tool/delegation | [A](evidence/2026-09-13-tool-delegation/TOOL-ADMISSION.md)/[A SOURCES](evidence/2026-09-13-tool-delegation/TOOL-SOURCES.md), [B](evidence/2026-09-13-tool-delegation/DELEGATION-LIFECYCLE.md)/[B SOURCES](evidence/2026-09-13-tool-delegation/DELEGATION-SOURCES.md), [NOT RUN](evidence/2026-09-13-tool-delegation/CHECKS-NOT-RUN.md)/[PUBLICATION](evidence/2026-09-13-tool-delegation/PUBLICATION.md); source-only |
| U11 runtime/backend | [A SOURCES](evidence/2026-09-12-runtime-backend/SOURCES.md)/[B SOURCES](evidence/2026-09-12-runtime-backend/BACKEND-SOURCES.md)/[PUBLICATION](evidence/2026-09-12-runtime-backend/PUBLICATION.md); source-only |
| U10 execution/context | [SOURCES](evidence/2026-09-12-cron-execution-context/SOURCES.md)/[SPEC](evidence/2026-09-12-cron-execution-context/SPEC.md)/[RESULT](evidence/2026-09-12-cron-execution-context/RESULT.json)/[MANIFEST](evidence/2026-09-12-cron-execution-context/MANIFEST.json); C01–C06 local-file selector, failed first parse korunur |
| U09 occurrence | [SOURCES](evidence/2026-09-12-cron-occurrence-admission/SOURCES.md)/[RESEARCH](evidence/2026-09-12-cron-occurrence-admission/RESEARCH.md); source-only |
| U08 cancellation/drain | [SOURCES](evidence/2026-09-12-cron-drain-receipts/SOURCES.md)/[RESEARCH](evidence/2026-09-12-cron-drain-receipts/RESEARCH.md)→SPEC/RESULT/MANIFEST/raw; native async/synthetic send |
| U07 cron/queue | [SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md)→SPEC/RESULT/MANIFEST/raw; queue/temp SQLite |
| U06 resume | [SOURCES](evidence/2026-09-11-resume-admission/SOURCES.md)/[RESEARCH](evidence/2026-09-11-resume-admission/RESEARCH.md)→SPEC/RESULT/MANIFEST/raw; process-local lease |
| U05 lease/history | [SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md); source-only |
| U04-A/B | [A SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [B RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md)/[33-file manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json); ayrı vaka/raw/probe |
| U03/U02 | [Kanban SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md), [turn SOURCES](evidence/2026-09-10-turn-lifecycle/SOURCES.md) |

[Exact U13 ledger](https://github.com/batuhanozgun/agentic-os-search/blob/93d6b14438802163ed3f542beded218e14cc51cf/research/studies/hermes-agent/SOURCE-LEDGER.md)→U12 bütün eski hash/date/reading/attempt ayrıntıları; [through-v0.9](SOURCE-LEDGER-THROUGH-V0.9.md) erken kayıtlar. Eski original evidence taşınmadı/değiştirilmedi. U04-B33 original subtree d01c92f7414713300934be3bb4e3d40ac57631b3 korunur.

Q59 yalnız next kaynak sorusudur, yapılmış finding değil. Q58 source-advanced; gerçek updater/DB/service/quality ve eski Q40/Q42/Q47–57/fidelity residual'ları kapanmaz. Kaynak okuma sayısı veya yayın commit sayısı ürün güvenilirliği ölçütü değildir.
