# Hermes Agent — Araştırma planı

**v0.18 / 2026-09-11 — U05 session lease/history/recovery source study.** Work authority [STATE](STATE.md), yöntem/kapanış [METHOD](METHOD.md). [V0.17 exact plan](https://github.com/batuhanozgun/agentic-os-search/blob/ac3cac0139dbfd6bd86773549c93172abcea4484/research/studies/hermes-agent/RESEARCH-PLAN.md) ve onun tarihsel zinciri korunur. Bu revizyon yeni kaynak araştırmasıdır; yeni HERMES deney koşusu değildir.

## 1. Hedef ve düzey

Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release değildir. Önce HERMES-native mekanizmalar/sistem ilişkileri, sonra dört-alan ve SOUL/Development OS. Üç merkezi provisional sentez learning/change, turn/context/session ve persistent work/continuation alanındadır. B'nin paket-local sentezi veya U05 not20 dördüncü tamamlanmış model değildir; genel sistem hâlâ kısmi.

## 2. U05'te yapılan — tekrar iş sayma

[20](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md), [SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md), [RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md). Önceki facade-lease source429 açıldı. Actual admission'ın new/immediate/waited ayrımı; real DB root-key claim/refresh/release; quiet caller/prolog history propagation; transitive tip recovery; atomic transcript publication; afterward loop meta save/clear→real set_meta/_execute_write; gateway loop scan/in-flight ve heartbeat watch source bağı araştırıldı.

Q40, evrensel history reload varsayımından koşullu telafiler ve caller responsibility'ye daraldı. Q41'de actual transcript transaction ile loop-state transfer transaction'ları ayrıldı. Q42'de persisted state ile canlı watcher/route, özellikle awaiting_response gate'i ayrıldı. Bunlar source-inspected sonuçlar; actual source+DB integration veya process-restart reproducer yapılmadı. [NOT RUN kontrol tasarımı](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md) future work'tür.

U04-A/18 ve U04-B/19 zaten yayımlanmış iki ayrı kayıttır. B'nin 33 özgün dosyası, A/B raw/probe/SPEC kimlikleri ve merkezi syntheses/01–03 değişmedi. Aynı G/H numaraları package-qualified kullanılır; test/başarı puanı veya independent replication çıkarılmaz. B delivery/repo-updates current authority değildir.

## 3. İlk sonraki bounded consumer birimi

**Soru:** Actual DB/history/fence tüketicisi ordinary continuation'ın bağlamını nasıl tamamlar veya reddeder; saved in-flight continuation yeni process/driver'da hangi admission/receipt ile yeniden gerçek işe dönüşür?

**A — mevcut source frontier:** primary `hermes_state_messages.py` continuation. 1–215 okundu, 210–375 429 ile durdu. Gerçek resolve_resume_session_id/get_messages_as_conversation ve holder-write guard/append/flush çağrıları okunmalı. S01 artık unreadable diye tekrar baştan bir keşif işi yapılmaz; mekanizma U05'ten geri kazanılır, değişim/yük taşıyan ihtiyaç kadar yeniden okunur.

**B — Q40 ayırıcı trace:** quiet first/next result messages, caller history, admission output, DB rows ve actual next-consumer/request history ayrı gözlenmeli. Immediate/no-rotation, waited reload ve stale-parent recovery karşılaştırılmalı. Bu trace için model taklit edilebilir ama history/admission/DB mekanizmasını taklit edip beklenen sonucu testin üretmesi kabul edilmez. Kaynak/bağımlılıklar yeterli değilse source-only sonuç korunur, fake actual DB diye sunulmaz.

**C — Q42 driver recovery:** actual gateway/run_startup watcher launch; command/adapter/FIFO acceptance ve completion/abandon; restored loop awaiting_response; heartbeat registration ve rotation watch rebind. Sadece LoopManager yeniden oluşturmak actual process restart değildir. Normal adapter return otomatik 'turn işlendi' receipt'i değildir. Bu consumer'larla gerekli goal/heartbeat migration ve DB/profile kimlikleri Q41 altında bağlanır.

**Durma ölçütü:** en az bir normal continuation ve bir interruption/rotation/restart karşı yolunda history, çalışma hakkı, persisted state ve canlı driver'ın kabul/red/telafi ilişkileri açık kaynak/ölçüm kapsamlarıyla açıklanmalı. Sadece saved JSON, helper True, session ID, elapsed time veya test adedi yeterli değildir. Bütün DB/OS fault matrisi ön koşul yapılmaz.

## 4. Sınırlar ve yön değiştirme

Kaynak erişimi yeni oturumda yeniden değerlendirilebilir; yine 429 varsa seri retry veya kısıt dolaşma yerine açıklanamayan kenar kaydedilir. Ürün kurulumu, model/provider/credential, başka repository, ağ/izin ayarı veya mimari değişimine sessiz genişleme yoktur. Eski G/H/K reduced fixture'larını çoğaltmak driver coverage değildir.

[U05 coverage eklemesi](inventory/LEASE-RECOVERY-COVERAGE-2026-09-11.md), [U04 coverage](inventory/CONTINUITY-COVERAGE-2026-09-11.md) ve [U02 broad map](inventory/CORE-COVERAGE-2026-09-10.md) birlikte kullanılır. U05 source consumer birimi yeterince açıklanınca F01–F12 haritası yeniden önceliklendirilir; araştırma süresiz olarak lease/fault köşesine kapanmaz. Q43 gerçek task-run ownership/cancel/fence; Q44 strong verification/revision reuse; Q45 loop stop/count/condition ayrımı kapsamda kalır.

Q38 selected-parent byte/AST fidelity; Q26/Q29 full-worker/original; Q07/Q22 final wire/timing/variants; actual model-quality ve OS/artifact/delivery açık. Provider/backend/delegation, cron/scheduler, diğer UI/install/update/eval, learning/skill-ledger/sync/quality aileleri korunur. Bütün otomasyon Kanban'a veya kalıcı iş yalnız cron'a indirgenmez.

## 5. Yayın ve yetki

Yalnız HERMES study ve HERMES catalog row değişir. Eski evidence/not/syntheses, Foundation/control/context/Codex/upstream/adoption değişmez. Yayın öncesi main tekrar okundu ve ac3cac tabanı değişmemişti. Scoped tree/commit hazırlanır, main ref non-force ilerletilir; actual main, içerik ve diff geri okunarak doğrulanır. Kaynak araştırması, tarihsel kayıtlı koşular ve yayın doğrulaması ayrı raporlanır.
