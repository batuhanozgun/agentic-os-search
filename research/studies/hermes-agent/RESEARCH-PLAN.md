# Hermes Agent — Araştırma planı

**v0.17 / 2026-09-11 — U04-A/B publication reconciliation.** Work authority [STATE](STATE.md), yöntem/kapanış [METHOD](METHOD.md). [V0.16 exact plan](https://github.com/batuhanozgun/agentic-os-search/blob/a0585203ca0a2bdd1cc8441aa152d7e4a72128cf/research/studies/hermes-agent/RESEARCH-PLAN.md) korunur. Bu revizyon yeni araştırma veya yeni deney değil, ayrı U04 tesliminin kaydıdır.

## 1. Hedef ve düzey

Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release değildir. Önce HERMES-native mekanizmalar/sistem ilişkileri, sonra dört-alan ve SOUL/Development OS. Üç merkezi provisional sentez learning/change, turn/context/session ve persistent work/continuation alanındadır. B'nin paket-local sentezi dördüncü tamamlanmış katman değildir; genel sistem hâlâ kısmi.

## 2. Bu revizyonda değişen

[19](notes/19-U04-DELIVERY-RECONCILIATION.md), 33 özgün dosyalı [U04-B teslimini](evidence/2026-09-11-multiturn/README.md) mevcut [U04-A/18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) ile uzlaştırır. A: 15 grup ve farklı probe/SPEC/raw kimliği. B: 21 durum ve ayrı recorded run. Ortak G/H numaraları yeniden adlandırılmadan package-qualified kullanılır; toplam test/başarı puanı veya bağımsız replication üretilmez.

B:H08/H09 normal/migration-write-fault kaydı Q41'e ek sınırlı girdi, A:S10 facade/history ise Q40'ın korunmuş ilk girişidir. B'nin eski `repo-updates/` dosyaları current authority yerine konmaz; mevcut synthesis/03 ve A evidence değişmez. [Uzlaştırma](evidence/2026-09-11-multiturn/RECONCILIATION.md) eski aday soru numaralarını canonical Q40–Q45'e eşler. Bu yayında hiçbir probe veya model çağrısı çalıştırılmadı.

## 3. İlk sonraki araştırma — v0.16 sırası korunuyor

**Soru:** Devam istemi hangi actual session lease/history ile kabul edilir; rotation/restart sonrası manager durumu ile canlı route/driver/queue nasıl recover edilir?

Başlangıç `agent/turn_facade.py::run_conversation` → `agent/turn_facade_lease.py::admit_durable_turn_lease` → gerçek SessionDB/history tüketicileri. A:S10, caller history'sinin admission tarafından değiştirilebildiğini gösterir; simple same-session veya history-loss hükmü verilmez. Ardından gerekli state_meta get/set/save/child-copy/parent-clear ve watcher/in-flight tick recovery yolları bağlanır. B'nin fixture migration kanıtı bu gerçek consumer'ların yerine geçmez.

Çıktı/durma ölçütü: normal bir continuation'ın history seçimi ve çalışma hakkı; bir interruption/rotation/restart yolunda kalıcı kayıt, live manager, route/driver ve tick'in kabul/red/telafi ilişkileri kaynakla açıklanabilmeli. Sadece saved JSON, helper True, aynı session ID veya test adedi yeterli değildir. Bütün database/OS fault matrisi ön koşul yapılmaz.

Gerekli offline test gerçek consumer+DB sınırına yönelmeli. Ürün kurulumu, model/provider/credential veya başka repository'ye sessiz genişleme yoktur. 429 yeni turda tekrar kontrol edilir; erişim sürmezse kenar source-blocked kalır, seri retry/kısıt dolaşma yerine bağımsız açıklanabilir kenar seçilir. Aynı G/H/K fixture'larını çoğaltmak driver coverage değildir.

## 4. Geniş kapsam ve yeniden açma

[CONTINUITY-COVERAGE](inventory/CONTINUITY-COVERAGE-2026-09-11.md) ile [U02 broad map](inventory/CORE-COVERAGE-2026-09-10.md) korunur. Q40 ilk, gerekli Q41/Q42 bağları ardından; Q43 lower ownership/cancel, Q44 güçlü verification/revision reuse gerektiğinde yeniden açılır. B'den korunan Q45 loop stop/count/condition ayrımı genel source question'dır.

U03/K ve U04 manuel seçkilerin full-parent fidelity borcu ayrı; tam heartbeat hash eşleşmesi onları kapatmaz. Q26/Q29 full-worker/original, Q07/Q22 final wire/timing/variants, actual model quality ve OS/artifact/delivery açık kalır. Provider/backend/delegation, cron/scheduler, diğer UI/install/update/eval, skill-ledger/sync/quality aileleri yeni kanıtla yeniden önceliklenir. Bütün otomasyon Kanban'a veya kalıcı iş yalnız cron'a indirgenmez.

## 5. Yayın ve yetki

Bu tur yalnız HERMES study ve HERMES catalog row. Eski evidence/not/syntheses korunur; Foundation/control/context/Codex/upstream/adoption değişmez. 33 özgün B dosyası native Git tree olarak korunur; yeni wrapper/manifest/uzlaştırma ve current entry'ler onu keşfettirir. Güncel main parent korunur, scoped diff karşılaştırılır, ref non-force ilerler, main/content geri okunur. Yeni araştırma, kayıtlı eski koşu ve yayın doğrulaması ayrı raporlanır.
