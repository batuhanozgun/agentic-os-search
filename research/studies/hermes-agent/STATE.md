# Hermes Agent — STATE

**Durum:** ACTIVE PARTIAL RESEARCH / U04-A + U04-B DELIVERY RECONCILIATION  
**Son kayıt:** 2026-09-11; bu checkpoint yayın/uzlaştırmadır, yeni kaynak araştırması veya deney değildir.  
**Primary:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release veya kurulu ürün hükmü değil.  
**Plan:** [v0.17](RESEARCH-PLAN.md). **Bütün HERMES araştırması tamamlandı mı? HAYIR.**

## Amaç ve yetki

Önce HERMES-native mekanizma ve sistem açıklaması; daha sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesi. Kullanıcı çok turlu iş sürekliliği araştırmasını yetkilendirmişti; son isteği sohbetten teslim edilen U04 paketini yeniden GitHub'a göndermeyi denemektir. Bu tur yalnız mevcut teslimi yayımlar ve canonical sürekliliği uzlaştırır; sonraki teknik araştırma başlatılmadı.

Yalnız `research/studies/hermes-agent/**` ve CATALOG'daki HERMES satırı değişebilir. Bütün ürün kurulumu/çalıştırması, gerçek model/provider/credential kullanımı, upstream/diğer repo/control/Foundation/context/Codex/architecture/adoption değişikliği yetkisi yoktur. Codex başka repo kullanır; main hareketleri ona atfedilmez. Otomatik/background devam, izin veya uygulama ayarı değişikliği yoktur. OpenClaw ayrı adaydır.

## İki U04 kaydı ve yayın kapanışı

**U04-A:** [18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md) → [kaynaklar](evidence/2026-09-11-multi-turn-continuity/SOURCES.md), [araştırma](evidence/2026-09-11-multi-turn-continuity/RESEARCH.md), [raw arşiv](evidence/2026-09-11-multi-turn-continuity/diagnostic-evidence.tar.xz). Önceden main'deydi: G01–G10/H01–H05, recorded UTC `2026-09-11T06:10:29.139368+00:00`, raw SHA-256 `ae5b94ce2e4c540ef72074e4e37bd3f20fe60615c8e126781615b1e08ce7ebf3`.

**U04-B:** [19](notes/19-U04-DELIVERY-RECONCILIATION.md) → [yeni yayın girişi](evidence/2026-09-11-multiturn/README.md), [özgün araştırma](evidence/2026-09-11-multiturn/delivery/RESEARCH.md), [tam raw RESULT](evidence/2026-09-11-multiturn/delivery/evidence/RESULT.json). Bekleyen ZIP'in 33 özgün dosyası `delivery/` altında değiştirilmeden korunur. G01–G12/H01–H09, recorded UTC `2026-09-11T06:11:47.964054+00:00`, raw SHA-256 `42929ea7388c9426bcdd08507ce953f14a5ff887296ac9143bbd7bd672d213a7`.

A/B adları bu uzlaştırmanın ayırıcı etiketleridir; orijinal dosya ID'leri yeniden yazılmadı. Aynı G/H numarası aynı vaka değildir. İki çalışma örtüşür; 15+21 veya kontrol toplamı ürün kapsam/başarı puanı ya da bağımsız doğrulama değildir. [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) konu/ID ve eski aday soru eşlemesini taşır.

Transferde ZIP/member hash'leri, recorded probe/SPEC/input bağları, Python/JSON parse ve native Git tree eşleşmesi kontrol edildi. **HERMES probe çalıştırılmadı; upstream yeniden araştırılmadı.** B'nin `repo-updates/` v0.16 dosyaları eski adaydır ve current dosyalara uygulanmadı. İçlerindeki “yayımlanmadı” ifadeleri ilk teslim anına aittir. Mevcut note18, merkezi synthesis/03 ve A kanıtları ezilmedi. Bu bilinen teslim kapatılır; bütün geçmiş sohbet artefaktlarının evrensel envanteri iddia edilmez.

## Mevcut açıklama ve kanıt sınırı

Üç merkezi provisional sentez vardır: [öğrenme/değişim](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md), [genel tur/bağlam/oturum](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md), [kalıcı iş/devam](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md). B'nin paket-local sentezi ayrı tarihsel açıklama girdisidir; dördüncü completed model veya nihai CORE değildir.

U04-A/B, Kanban goal-mode ile session goal/loop/heartbeat'in farklı kimlik/state/wait/gate/budget/driver ilişkilerini açar. Helper outcome, durable receipt, process exit ve semantik kalite eşit değildir. A:G06/B:G10, judge sırasında değişimde callback kontrol zamanını gösterir; actual worker/OS/external-effect kanıtı değildir. A:H05 stale manager sınırını, B:H08/H09 ise normal ve selective child-write fault altında migration yardımcısı sınırını kaydeder. B:H09 actual Hermes SessionDB veya üretim compaction kaybı değildir.

Her iki U04 kaydında tam byte kimliğiyle doğrulanan heartbeat modülüdür; Kanban seçkileri manuel, full-parent byte/AST sadakati açık. Çevre adapter/clock/judge/turn/task-writer fixture'ları ve sınırlı SQLite kullanımı full runtime değildir. A:S10 facade, admission'dan gelen history ile çağıranın girdisini değiştirebilir; B'nin dar CLI görünümü bunu silmez. Lower `turn_facade_lease.py` önceki okumada 429 almıştı: ne kayıpsız history ne de history-loss verdict'i vardır.

01–18 notları, tüm eski evidence ve merkezi syntheses/01–03 korunur. [V0.16 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/a0585203ca0a2bdd1cc8441aa152d7e4a72128cf/research/studies/hermes-agent/STATE.md) A'nın ayrıntılı tarihsel kaydıdır; U03/K ve önceki A/SA/AP/M4/N/MW/C/V çalışmalarının ayrı kapsamları devam eder. Q07/Q22 final wire/timing/variants; Q26/Q29 full-worker/original; Q38 selection fidelity; gerçek scanner/quality/artifact/OS/delivery açıktır. Eski koşular yeniden sayılmadı.

## İlk sonraki teknik birim — değişmedi

**Bir continuation hangi gerçek session lease/history ile kabul edilir; rotation/restart'ta devam kaydı, canlı manager ve route/driver/queue nasıl yeniden birleşir?** İlk giriş primary `agent/turn_facade.py::run_conversation` → `agent/turn_facade_lease.py::admit_durable_turn_lease` ve gerçek SessionDB/history tüketicileridir. Sonra gerekli `goal:/loop:/heartbeat:` save/transfer ve in-flight recovery yollarına inilmelidir.

Normal yeniden giriş ile en az bir interruption/rotation/restart karşı yolunda kaydın hangi bağlam ve yetkiyle gerçek işe dönüştüğü açıklanmalı. B:H09'un azaltılmış adaptörünü tekrar koşmak actual SessionDB entegrasyonu sayılmaz. Kaynak erişimi yeniden kontrol edilir; hâlâ engelliyse seri retry yerine açıklanamayan kenar korunur. Her açık güvenlik borcu diğer araştırma ailelerini durdurmaz; F01–F12, provider/backend/delegation, cron/scheduler, diğer UI/install/eval ve skill-ledger/sync/quality kapsamı korunur.

## Cold start ve yayın

Bootstrap → research root/studies catalog → META/STATE/INDEX → METHOD/plan → **19 + U04-B README/RECONCILIATION/manifest**. Teknik devam için **synthesis/03 + U04-A SOURCES/RESEARCH + CONTINUITY-COVERAGE**; B migration/own-run ayrıntısı yük taşıyorsa B SOURCES/SPEC/raw RESULT/probe tam okunur. A raw archive gerektiren exact iddia için browsing summary yeterli değildir. Eski sohbet ZIP'i gerekmez.

İlk main `a0585203...`, sonraki `bc9f404e...`; aradaki yalnız Foundation değişiklikleri korunur. Yayın tree'si güncel main tabanını taşır, ref non-force veya exact-head anlık PR merge ile ilerletilir; başarı gerçek main ve içerik readback ile doğrulanır. B native original subtree `d01c92f7414713300934be3bb4e3d40ac57631b3`. Kontrol dosyaları, diğer projeler ve önceki kanıtlar değiştirilmez.
