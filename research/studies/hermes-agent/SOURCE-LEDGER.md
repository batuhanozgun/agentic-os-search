# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-12 / U09 plan v0.22.** Current authority [STATE](STATE.md). Primary c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a. U08 yayını doğrulandı; U09 yeni SOURCE-ONLY araştırma. Yayın ve source/behavior doğrulaması ayrı.

## U09 yeni kaynak birimi

[24](notes/24-CRON-OCCURRENCE-AND-FIRE-ADMISSION.md) → **[S01–S10](evidence/2026-09-12-cron-occurrence-admission/SOURCES.md)** → [RESEARCH](evidence/2026-09-12-cron-occurrence-admission/RESEARCH.md) / [NOT RUN](evidence/2026-09-12-cron-occurrence-admission/CHECKS-NOT-RUN.md). S01 jobs helpers/claim/finish/due/rearm; S02 provider; S03 Chronos; S04 NAS client; S05 verifier; S06 API adapter; S07 wire contract; S08 dashboard router; S09 profile/forwarder; S10 mocked webhook test sources.

S03/S04/S05/S07 full read; büyük modüller ve testler local SOURCES'da belirtilen seçili kapsam. Full-byte parent, runtime dependency closure veya yeni test koşusu yok. T0–T4 conditional source trace, actual execution değildir. Hedefin wire iddiası ile kod gözlemi ayrı; NAS implementasyonu ve gerçek external duplicate ölçümü yoktur. Current default-branch a84a2223f82c3d9906fd4a9d778a188774e7a08e occurrence pointer'ları navigation only.

## U08 — tamamlanmış kaynak, eski koşu ve bu tur tamamlanan yayın

[23](notes/23-CRON-DRAIN-RECEIPTS-AND-CANCELLATION.md) → [SOURCES](evidence/2026-09-12-cron-drain-receipts/SOURCES.md)/[RESEARCH](evidence/2026-09-12-cron-drain-receipts/RESEARCH.md). Actual gateway drainer/status kaynak zinciri; yalnız full async_utils.py eski koşusu. [SPEC](evidence/2026-09-12-cron-drain-receipts/SPEC.md)/[RESULT](evidence/2026-09-12-cron-drain-receipts/RESULT.json)/[MANIFEST](evidence/2026-09-12-cron-drain-receipts/MANIFEST.json) → raw source/probe/effect/runtime. Source blob 2bc558fad21eeec736c0283cb7df86304349f222; RESULT SHA-256 91833c4ae0b9f229a1c82f6edaa4a25bfc9b39ebc061c9e1811dbe32247dbfa0. B01–B03 actual asyncio/thread/local file, synthetic transport; N01/N02 observation-validator, source mutants değil. Bu tur yeniden çalıştırılmadı.

[U08 PUBLICATION](evidence/2026-09-12-cron-drain-receipts/PUBLICATION.md): content e30f6ee6a027ec247fd3dff6cb28f9a3d7ade1ca, receipt c370cbc88823f7ee4d07aa6c97b75cf509129254. Native ref/diff/content doğrulaması eski deneyin bağımsız tekrarı değildir.

## Önceki source ve raw rotalar

| Birim | Giriş ve exact kanıt |
|---|---|
| U07 /22 | [SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md)/[SPEC](evidence/2026-09-11-cron-scheduling-delivery/SPEC.md)/[RESULT](evidence/2026-09-11-cron-scheduling-delivery/RESULT.json)/[MANIFEST](evidence/2026-09-11-cron-scheduling-delivery/MANIFEST.json); D serisi full queue/real temp SQLite, gerçek network değil |
| U06 /21 | [SOURCES](evidence/2026-09-11-resume-admission/SOURCES.md)/[RESEARCH](evidence/2026-09-11-resume-admission/RESEARCH.md)/[SPEC](evidence/2026-09-11-resume-admission/SPEC.md)/[RESULT](evidence/2026-09-11-resume-admission/RESULT.json)/[MANIFEST](evidence/2026-09-11-resume-admission/MANIFEST.json); L yalnız process-local lease |
| U05 /20 | [SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md)/[NOT RUN](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md); durable lease/quiet history source-only |
| U04-A /18 | [SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md)/[RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md)/[SPEC](evidence/2026-09-11-multi-turn-continuity/SPEC.md) → diagnostic-evidence.tar.xz |
| U04-B /19 | [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md)/[manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json) → [SOURCES](evidence/2026-09-11-multiturn/delivery/SOURCES.md)/[SPEC](evidence/2026-09-11-multiturn/delivery/evidence/SPEC.md)/[RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json)/[probe](evidence/2026-09-11-multiturn/delivery/evidence/probe.py) |
| U03/U02 | [Kanban SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md), [Turn SOURCES](evidence/2026-09-10-turn-lifecycle/SOURCES.md); eski selected-parent/wire sınırları korunur |

Eski tüm raw hash/date ve önceki A/SA/AP/M4/N/MW/C/V zinciri [exact v0.21 ledger](https://github.com/batuhanozgun/agentic-os-search/blob/c370cbc88823f7ee4d07aa6c97b75cf509129254/research/studies/hermes-agent/SOURCE-LEDGER.md) → [through-v0.9](SOURCE-LEDGER-THROUGH-V0.9.md) üzerinden korunur. U04-B 33-original subtree d01c92f7414713300934be3bb4e3d40ac57631b3; A/B aynı G/H ID'leri aynı vaka değildir. Eski kaynaklar taşınmadı/yeniden yazılmadı, deneyler tekrar edilmedi.

Current next source Q49; Q47 gerçek-runtime, Q40/Q42 ve Q48/Q50 ile eski Q07/Q22/Q26/Q29/Q38 açık. U09 kaynak kaydı bunlara substitute değildir. Üç merkezi synthesis ve METHOD korunur; whole CORE/architecture/adoption yoktur.
