# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-11 / plan v0.20; U07 yayın checkpoint'i.** [STATE](STATE.md) work authority. Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; current installed ürün değildir. Yeni U07 source study ve bounded real-SQLite queue execution önceki U06'dan ayrıdır; bu aktarım yeni araştırma/deney değildir. Eski koşular tekrar edilmedi.

## U07 — özgün araştırma ve yayın

[22](notes/22-CRON-SCHEDULING-EXECUTION-AND-DELIVERY.md) → [U07 S01–S08](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md)/[SOURCES.json](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.json) → [RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md). S01 startup selected; S02 scheduler selected; S03 executions full read NOT RUN; S04 provider/S05 jobs/S07 delivery selected; **S06 queue full byte + bounded execution**; S08 MIT reuse.

S06 blob `689fd620d6193003bbd168a0e62770a0d0306ac6`, SHA-256 `62529e31774f414f9cda886505f0db7f291d13f566cc06982c11cba1da005c4b`, 13.837 byte. D01–D06 ve N00–N02; recorded UTC `2026-09-11T14:22:57.364884+00:00`–`2026-09-11T14:22:57.404381+00:00`. Raw RESULT SHA-256 `c53f850cceaad5e84eb800ce88b02c9a4eb227a00d82ee1714aecaefe7b51719`. [SPEC](evidence/2026-09-11-cron-scheduling-delivery/SPEC.md)/[RESULT](evidence/2026-09-11-cron-scheduling-delivery/RESULT.json)/[MANIFEST](evidence/2026-09-11-cron-scheduling-delivery/MANIFEST.json), source/probe/input/log/DB/raw archive. İlk attempt-00 pre-case metadata hatası; yalnız metadata expression düzeltmesi, oracles/SPEC/source sabit. Yeni behavioral run ile artifact kontrolleri ayrı.

Queue None/pending çalıştırıldı; üst delivered classifier bağlantısı source inference. Actual gateway drainer/status consumer, foreign-owner process, SessionDB/history, full host/OS/network/model açık. gateway/run.py 3150–3325 429, seri retry yok. Yeni default-branch `04dd80a...` queued alanları ve drainer yalnız navigation, current revalidation değil. İlk write-action yokluğu tarihsel kayıttır; güncel U07 yayın makbuzu: [PUBLICATION](evidence/2026-09-11-cron-scheduling-delivery/PUBLICATION.md).

## U06 — yayımlanmış tarihsel kaynak ve koşu

[21](notes/21-RESUME-ADMISSION-AND-DRIVER-RECOVERY.md) → **[S01–S12](evidence/2026-09-11-resume-admission/SOURCES.md)** → [RESEARCH](evidence/2026-09-11-resume-admission/RESEARCH.md). S01 actual messages selector/projection/guard, S02 flush/holder/adoption, S03 startup/recovery/redelivery, S04 lifecycle marker, S05 commands, S06 adapter/task, S07 gateway turn, S08 turn runner, S09 inbound, S10 yardımcı navigation, S11 native registry, S12 MIT license. Her ID'nin tam/range/incidental kapsamı local SOURCES'tadır; listed olmak full-read/run değildir.

**Yeni yürütme yalnız S11:** tam `gateway/turn_lease.py` blob `1f65614e66e748ec61573aced3fa48b57ee20281`, 9,190 byte. [SPEC](evidence/2026-09-11-resume-admission/SPEC.md), [tam RESULT](evidence/2026-09-11-resume-admission/RESULT.json), [arşiv/manifest](evidence/2026-09-11-resume-admission/MANIFEST.json). UTC `2026-09-11T11:06:33.167739+00:00`; L01–L07 expectation_met. N00 identity, N01 timeout ve N02 rebind bozma kontrolleri ilgili yanlışı ayırdı. Raw RESULT SHA-256 `04663c7528a379c27450ddc2c0d91dd2f5182a751984062aa1af5f1a58e696a0`; archive SHA-256 `2b62b7b919e5cf710601bffff88bf50a058112add94b8b85bfc038c69779f7db`, Git blob `3cbd1a1d3b452af456af9ec51d32c79a79e043e2`.

Bu gerçek asyncio tek process/modül diagnostic'idir; SessionDB, GatewayRunner/adapter/OS restart, provider/model, semantic acceptance veya upstream suite değildir. Aynı araştırmacı oracle'ı independent replication sayılmaz. Exact probe/source/inputs archive'de; native SPEC/RESULT byte-equal kopyalardır. [README](evidence/2026-09-11-resume-admission/README.md) reproduction'ı verir.

Messages429 source engeli U06'da açıldı. Raw download DNS hatası nedeniyle büyük runtime tam materyalize edilmedi; S11 connector metni+Git hash ile kuruldu. Default-branch daha yeni restore/acceptance snippet'leri ve official web docs yalnız navigation/freshness uyarısı; primary pin yükseltilmedi. Keşfedilen upstream test dosyaları bu tur source-inspected/run değil.

## Korunan U05 ve daha eski rotalar

[20/U05](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md) → [U05 SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md)/[CHECKS-NOT-RUN](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md). Durable root lease, waited-only history reload, quiet caller/prolog gap, rotation/publication, manager/driver kaynakları; source-only historical çalışma. U06 yeni küçük registry testi U05 actual-DB/whole-host kontrollerini kapatmaz.

[V0.18 exact ledger](https://github.com/batuhanozgun/agentic-os-search/blob/0a475b5d7c50f47689c72cd31f954f5b2303ced6/research/studies/hermes-agent/SOURCE-LEDGER.md) → v0.17/v0.16/v0.15 bağlantıları → [through-v0.9](SOURCE-LEDGER-THROUGH-V0.9.md). Bütün önceki evidence dosyaları yerinde/değişmeden. [U02 source map](evidence/2026-09-10-turn-lifecycle/SOURCES.md) genel turn; [U03](evidence/2026-09-10-kanban-task/SOURCES.md) task/run/terminal ve original K archive. M4 artificial V04 normal compaction caller değildir; A/SA/AP ortak kaynakları bağımsız test sayılmaz.

## U04-A/B kimliği ve yayını tamamlanmış işler

[A/18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → [A SOURCES](evidence/2026-09-11-multi-turn-continuity/SOURCES.md)/[RESEARCH](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md)/[archive](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz). G01–G10/H01–H05, raw SHA-256 `ae5b94ce2e4c540ef72074e4e37bd3f20fe60615c8e126781615b1e08ce7ebf3`.

[B/19](notes/19-U04-DELIVERY-RECONCILIATION.md) → [B SOURCES](evidence/2026-09-11-multiturn/delivery/SOURCES.md)/[RESEARCH](evidence/2026-09-11-multiturn/delivery/RESEARCH.md)/[raw RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json)/[probe](evidence/2026-09-11-multiturn/delivery/evidence/probe.py). G01–G12/H01–H09, raw SHA-256 `42929ea7388c9426bcdd08507ce953f14a5ff887296ac9143bbd7bd672d213a7`. 33 original dosya subtree `d01c92f7414713300934be3bb4e3d40ac57631b3`; [manifest](evidence/2026-09-11-multiturn/DELIVERY-MANIFEST.json) ve [reconciliation](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. B repo-updates historical candidate'dır. B:H09 reduced adapter, actual DB/compaction fault değil.

A/B'nin aynı G/H ID'leri eş vaka değildir; L ile birleştirilmiş başarı skoru yok. Tam heartbeat kimliği eski Kanban selected-parent fidelity'yi kapatmaz. Merkezi üç synthesis ve notes/01–20 değişmez; 21 ek kaynak açıklamasıdır, yeni completed CORE değildir.

## Açık consumer / next

U07 ilk yeni consumer: actual cron gateway delivery drainer/profile/transport ve queued/delivered/finished receipt; sonra occurrence/late callback/rearm ve run_job script/agent/context. Q40 actual DB/quiet history, Q42 startup preclaim/carrier/drain/actual admission explicit deferred. Q41 migration, Q43 worker/effect, Q07/Q22 wire, Q26/Q29 full worker, Q38 manual fidelity korunur. U07 queue full byte kimliği onları kapatmaz.

[U06 PUBLICATION](evidence/2026-09-11-resume-admission/PUBLICATION.md) tamamlanmış yayındır; yeni [U07 PUBLICATION](evidence/2026-09-11-cron-scheduling-delivery/PUBLICATION.md) güncel yayın ile ilk yerel teslim sınırını ayrı taşır. HERMES dışında mutation yoktur.
