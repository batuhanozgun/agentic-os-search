# Hermes Agent — STATE

**Durum:** ACTIVE PARTIAL RESEARCH / U05 SESSION LEASE–HISTORY–RECOVERY SOURCE STUDY  
**Son kayıt:** 2026-09-11; U04 yayını tekrar edilmedi, yeni source-only teknik inceleme yapıldı. Yeni HERMES execution/test koşusu yok.  
**Primary:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release veya kurulu ürün hükmü değil.  
**Plan:** [v0.18](RESEARCH-PLAN.md). **Bütün HERMES araştırması tamamlandı mı? HAYIR.**

## Amaç ve yetki

Önce HERMES-native mekanizma ve sistem açıklaması; daha sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesi. Bu tur kullanıcı güncel main'den cold-start, gerçek continuation lease/history ve ardından rotation/restart araştırmasını açıkça yetkilendirdi. Başlangıç main `ac3cac0139dbfd6bd86773549c93172abcea4484` idi; v0.17 yayın uzlaştırması mevcut teknik hedefle çelişmiyordu. AGENT.md, tetiklenen dokuz protokol ve kayıtlı cold-start yolu repo üzerinden tamamlandı. Bu durum sohbet hafızasından türetilmedi.

Yalnız `research/studies/hermes-agent/**` ve CATALOG'daki HERMES satırı değişebilir. Bütün ürün kurulumu/çalıştırması, gerçek model/provider/credential kullanımı, upstream/diğer repo/control/Foundation/context/Codex/architecture/adoption değişikliği yetkisi yoktur. Codex başka repo kullanır; main hareketleri ona atfedilmez. Otomatik/background devam, izin veya uygulama ayarı değişikliği yoktur. OpenClaw ayrı adaydır.

## Yeni U05 — açıklanan ile doğrulanmayanı ayır

**[20 — Session lease/history/recovery](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md)** → [SOURCES](evidence/2026-09-11-session-lease-recovery/SOURCES.md) → [RESEARCH](evidence/2026-09-11-session-lease-recovery/RESEARCH.md) → [coverage eklemesi](inventory/LEASE-RECOVERY-COVERAGE-2026-09-11.md).

Önceki `turn_facade_lease.py` kaynak engeli açıldı. Admission'ın yeni-session/immediate/waited yolları, actual DB'nin compression-root lease claim/refresh/release'i, quiet caller→prolog history seçimi, transitive tip recovery ve actual transcript child publication okundu. Loop migration helper'ı gerçek set_meta/_execute_write consumer'ına bağlandı; gateway loop scan/in-flight ve heartbeat in-memory watch ayrıldı. **Bu kaynak incelemesidir; actual SessionDB/process/OS/model deneyi veya yeni independent replication değildir.**

Yük taşıyan sonuçlar:

- Lease almak, her girişte history reload yapmak değildir. Admission yalnız bekledikten sonra resume ID/history yükler; rotation recovery ayrıca prolog öncesinde çalışır. Quiet Kanban caller'ın result messages listesini devralmadığı ve prolog'un ayrı liste kurduğu kaynakla görülür. No-wait/no-rotation koşulunda dar history-propagation boşluğu açıklanır; **DB silinmesi, bütün üründe history-loss veya final-provider-wire bug verdict'i verilmez**.
- Compression-root lease session ID değişiminden farklı bir kimlik kullanır. Holder-qualified claim/refresh/release ve liveness/interrupt kaynakları vardır; task-run sahipliği ve bütün dış etkilerin fencing'i buna eşit değildir.
- Transcript parent-close/child/handoff publication tek DB transaction'ındadır; goal/heartbeat/loop taşıma sonradan ayrı çağrılardır. Loop save→clear alt yolu gerçek set_meta'ya ayrı transaction'larla gider, save hatasını gizleyebilir ve durable child receipt doğrulamaz. B:H09'un reduced adapter sonucu artık gerçek-writer source bağlamıyla okunabilir, fakat production/actual-DB fault kanıtına yükseltilmez.
- Gateway loop DB'deki state+route'u tarar; restored awaiting_response=True firing'i engeller, sadece due zamanının geçmesi reset değildir. Heartbeat watch bellek içidir. Actual startup/command/adapter recovery ve heartbeat rotation rebind hâlâ ayrı consumer'lardır.

Son upstream engel: `hermes_state_messages.py` 1–215 okundu; **210–375 continuation 429** aldı. Gerçek resolve_resume_session_id/get_messages_as_conversation gövdeleri, transcript guard'ın kalanı ve append/flush consumer'ı bu tur kapanmadı. Seri retry/kısıt dolaşma yapılmadı. `gateway/run_startup.py` ve test yolları yalnız navigasyonla bulundu; okunmuş/çalıştırılmış sayılmaz. [NOT RUN kontrol tasarımı](evidence/2026-09-11-session-lease-recovery/CHECKS-NOT-RUN.md) tamamlanmış iş değildir.

## Korunan U04-A/B ve yayın kapanışı

**U04-A:** [18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → [kaynaklar](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [araştırma](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md), [raw arşiv](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz). G01–G10/H01–H05, recorded UTC `2026-09-11T06:10:29.139368+00:00`, raw SHA-256 `ae5b94ce2e4c540ef72074e4e37bd3f20fe60615c8e126781615b1e08ce7ebf3`.

**U04-B:** [19](notes/19-U04-DELIVERY-RECONCILIATION.md) → [yayın girişi](evidence/2026-09-11-multiturn/README.md), [özgün araştırma](evidence/2026-09-11-multiturn/delivery/RESEARCH.md), [tam raw RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json). 33 özgün dosya delivery/ altında değişmeden korunur. G01–G12/H01–H09, recorded UTC `2026-09-11T06:11:47.964054+00:00`, raw SHA-256 `42929ea7388c9426bcdd08507ce953f14a5ff887296ac9143bbd7bd672d213a7`; native subtree `d01c92f7414713300934be3bb4e3d40ac57631b3`.

A/B etiketleri iki ayrı kaydı ayırır; ortak G/H numarası aynı vaka değildir. [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) kapsam/ID eşlemesini taşır. A:G06/B:G10 callback timing, A:H05 stale manager, B:H08/H09 reduced migration sınırları korunur. 15+21 veya kontrol toplamı başarı puanı/bağımsız doğrulama değildir. Tam heartbeat byte kimliği Kanban manual full-parent byte/AST sadakatini kapatmaz.

B'nin delivery/repo-updates/ v0.16 dosyaları historical candidate'dır; current dosyaların yerine uygulanmadı. İçlerindeki 'yayımlanmadı' cümleleri ilk teslim anına aittir. **Bilinen A/B yayını tamamlanmış iştir; yeniden ZIP göndermek veya eski probeları sırf sayı artırmak için koşmak sıradaki iş değildir.** U05 hiçbir eski raw/probe'u tekrar çalıştırmadı.

## Sentezler ve daha eski sınırlar

Üç merkezi provisional sentez **değişmeden korunur**: [öğrenme/değişim](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md), [genel tur/bağlam/oturum](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md), [kalıcı iş/devam](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md). **20/U05, 03'teki admission/history olasılığının koşullu source amendment'ıdır.** 03'ü tek başına okuyup alt kaynak hâlâ erişilemiyor sanma; onu U05 ile birlikte oku. Dördüncü completed model veya nihai CORE yaratılmadı.

01–19 notları, bütün eski evidence, önceki U03/K ve A/SA/AP/M4/N/MW/C/V kapsamları korunur. Q07/Q22 final wire/timing/variants; Q26/Q29 full-worker/original; Q38 selection fidelity; actual scanner/quality/artifact/OS/delivery açık. [V0.17 exact STATE](https://github.com/batuhanozgun/agentic-os-search/blob/ac3cac0139dbfd6bd86773549c93172abcea4484/research/studies/hermes-agent/STATE.md) yayın tarihçesini, [v0.16](https://github.com/batuhanozgun/agentic-os-search/blob/a0585203ca0a2bdd1cc8441aa152d7e4a72128cf/research/studies/hermes-agent/STATE.md) önceki ayrıntıları taşır.

## İlk sonraki teknik birim

**Actual DB selector/guard → gerçek quiet next-history consumer → gateway startup/adapter ve saved in-flight recovery.** Önce S10 erişimi yeniden değerlendirilir; resolve_resume_session_id/get_messages_as_conversation ve holder-write guard/flush zinciri okunur. Q40'ın ordinary history sorusu uygun exact-source+actual-DB kontrolüyle ayrılır. Sonra Q42 startup watcher/command/adapter receipt ile awaiting_response ve heartbeat watch reactivation/rotation rebind bağlanır. Gerekli Q41 goal/heartbeat migration ve DB/profile bağları buna eklenir.

Normal continuation ve bir interruption/rotation/restart karşı yolu açıklanırken source-only ile execution ayrı tutulur. B:H09 adapter'ını tekrar koşmak actual SessionDB integration sayılmaz. Erişim engeli sürerse seri retry yerine açık kenar korunur. Bu bounded consumer kesitinden sonra broad F01–F12 haritası yeniden önceliklenir; provider/backend/delegation, cron/scheduler, diğer UI/install/eval ve learning/ledger/sync/quality kaybolmaz. Her güvenlik borcu diğer araştırma ailelerini otomatik durdurmaz.

## Cold start ve yayın

1. Güncel main'den AGENT.md ve tetiklenen protokoller → research root/studies catalog → META/STATE/INDEX → METHOD/plan.
2. **19 + U04-B README/RECONCILIATION/manifest**: iki özgün kaydın yayın/kimlik sınırlarını kazan.
3. **Synthesis/03 + U04-A SOURCES/RESEARCH + CONTINUITY-COVERAGE**, gerekli genel bağlam için merkezi 01/02.
4. **20 + U05 SOURCES/RESEARCH + LEASE-RECOVERY-COVERAGE**: güncel teknik ilerleme ve yeni source-blocked frontier. Eski v0.16/v0.17 first-next cümleleri current yetki değildir.
5. B migration/own-run exact ayrıntısı yük taşıyorsa B SOURCES/SPEC/raw RESULT/probe tam okunur; A exact raw iddiasında summary yerine raw archive gerekir. U05 CHECKS-NOT-RUN sonuç dosyası değildir. Eski sohbet ZIP'i gerekmez.

Bu yayın başlangıçtaki ac3cac main tabanını korur; scoped tree hazırlanır, non-force ref ilerletilir ve main/content/diff geri okunur. HERMES dışı değişiklik, eski evidence/not/synthesis rewrite veya control mutasyonu yoktur. Yayın readback'i behavioral verification değildir.
