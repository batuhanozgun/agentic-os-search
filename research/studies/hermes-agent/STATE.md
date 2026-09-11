# Hermes Agent — STATE

**Durum:** ACTIVE PARTIAL RESEARCH / U03 KANBAN SOURCE RECORD AND RECOVERED DIAGNOSTIC  
**Son kayıt:** 2026-09-11; özgün U03 kanıtı 2026-09-10.  
**Primary:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current-release doğrulaması değil.  
**Plan:** [v0.15](RESEARCH-PLAN.md). **Bütün HERMES araştırması tamamlandı mı? HAYIR.**

## Amaç ve yetki

Önce HERMES-native mekanizma ve sistem açıklaması; daha sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesi. Kullanıcı genel ajan döngüsünü ve ardından kalıcı iş yönetimini araştırmayı yetkilendirdi. Son mesajı yeniden göndermeyi denemektir: **bu kayıt turu mevcut çalışmanın kurtarılması/yayınıdır, yeni araştırma veya yeni deney değildir.**

Yalnız `research/studies/hermes-agent/**` ve CATALOG'daki HERMES satırı değişebilir. Kurulum, bütün ürünü çalıştırma, gerçek model/provider/credential kullanımı, upstream mutation, Codex görevi, Foundation/control/architecture/adoption yetkisi yoktur. Codex başka repo kullanır; main hareketleri ona atfedilmez. Yanıtlar arasında otomatik/background iş veya uygulama/izin değişikliği yapılmaz. OpenClaw ayrı adaydır.

## Şimdi kayda alınan çalışma

[17/U03](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md) → [RESEARCH](evidence/2026-09-10-kanban-task/RESEARCH.md), [SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md), [yayın kurtarması](evidence/2026-09-10-kanban-task/PUBLICATION.md).

Önceki turda getirilen Kanban kaynakları task/create/dependency/claim/run, normal dispatcher kimliği, complete/block/review, başarısızlık/reclaim ve worker context geçişlerini açmıştı. Ayrı iki Git nesnesi bulunup kurtarıldı: draft README `64533b4183596c3beaee798c4a165cc31a9510f4` ve 15 özgün dosya taşıyan kanıt arşivi `5484ca39caf7ae5a8f6a31b68caeec0f9a44363d`. Bir blob'un varlığı önceki main yayını sayılmaz.

K01–K08, kayıtlı zaman `2026-09-10T20:06:13.848575+00:00`: seçili transaction/transition işlevleri ve gerçek geçici SQLite; azaltılmış DDL/açık fixture'lar. [Sonuç özeti](evidence/2026-09-10-kanban-task/RESULT-SUMMARY.json) gezinme içindir; tam ham RESULT.json, iki probe sürümü, seçkiler ve loglar [özgün arşivdedir](evidence/2026-09-10-kanban-task/original-evidence.tar.xz). [Manifest](evidence/2026-09-10-kanban-task/RECOVERY-MANIFEST.json) her dosyanın kimliğini taşır.

Kurtarmada arşivin byte/Git kimliği, 15 member, kayıtlı input/probe hash'leri ve metadata-only script farkı doğrulandı. Kod parse edildi, **çalıştırılmadı**. Yeni RESEARCH/SOURCES companion'ları kurtarma sırasında hazırlandı; arşivde olmayan eski araştırma metni aynen kurtarılmış gibi sunulmaz. Önceki 'hiç ilerleme yoktu' final açıklaması bu somut kayıtla düzeltilmiştir; altyapı kök nedeni ileri sürülmez.

## Açıklanmış sınır ve açık doğrulama borcu

Task kimliği birden fazla run boyunca sürer; geç eski-run completion'ı expected ID ile reddedilebilir. Task/run/completed olayı transaction'ı, sonraki child-promotion/cleanup ve caller success'ten ayrıdır. K05 commit öncesi rollback, K06 commit sonrası exception ayrımını kayıtlar. Low-level expected_run_id=None operator yolu, normal worker'ın run ID aktarımıyla aynı koşul değildir. Bunlar semantik iş kalitesi veya uçtan uca üretim güvenliği kanıtı değildir.

Tam upstream parent byte/AST sadakati, gerçek dispatcher/worker process, init/migration, physical cancellation, artifact copy, goal/review judge ve notification delivery OPEN. K seti gerçek full-module koşusu veya bağımsız replication değildir. Aynı sekiz testi tekrar etmek bu boşlukları kapatmaz.

01–16 notları, syntheses/01–02 ve önceki evidence değişmeden korunur. [V0.14 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/25b06521083e2a4ddf7b0dbeb9454804796963b6/research/studies/hermes-agent/STATE.md) eski ayrıntıyı taşır. Q07/Q22 normal compaction→API-message source bağı geçerlidir; actual approval-to-wire/timing/all variants açık. Q26/Q29 full-original/full-worker verifier NOT RUN olarak kalır. A/SA/AP/M4 ve diğer eski koşular yeniden sayılmaz. U03 üçüncü tamamlanmış synthesis veya bütün HERMES CORE değildir.

## Sonraki çalışma

Bu tur yalnız yayın recovery'sini kapatır. Daha önce yetkilendirilmiş HERMES araştırmasının sıradaki teknik birimi: **Kanban'ın goal-mode worker devamı ve terminal kabulü ile goal/loop/heartbeat'in ayrı süreklilikleri.** `_worker_argv`/quiet CLI kolu, `run_kanban_goal_loop`, `goal_run_status` ve tool'daki `_goal_gate` bağlantıları gerçek primary kaynakta takip edilmeli; yorumlar uygulamanın yerine geçmemeli. Claim-loss/terminal handoff'un devamı durdurma koşulu ile judge'ın anlamsal kalite hükmü ayrılmalı.

K seçkilerini güçlü runtime/security/adoption iddiasında kullanmadan önce full-parent sadakat yeniden açılır; bu doğrulama borcu bütün diğer HERMES ailelerini durduran kapı değildir. Actual SessionDB/lease/restore, skill ledger/sync, provider/backend/delegation, scheduler/diğer UI/install/eval genişliği [v0.14 kapsam haritasında](inventory/CORE-COVERAGE-2026-09-10.md) korunur. Her sohbet Kanban task'ı değildir; goal/loop/heartbeat peşinen tek Work modeli sayılmayacak.

## Cold start ve yayın

Bootstrap → research root/studies catalog → META/STATE/INDEX → METHOD/plan → **17/U03 README/RESEARCH/SOURCES/SPEC/RESULT-SUMMARY/PUBLICATION**. Genel mekanizma için synthesis/02 ve 16/U02; exact K iddiası veya reproduction için committed original archive + manifest. Eski chat ZIP'ine ihtiyaç yoktur.

Yayın tabanı `25b06521083e2a4ddf7b0dbeb9454804796963b6` kullanılır; daha yeni main varsa yeniden uzlaştırılır. Aradaki Foundation/exploration çalışmaları korunur. Ref non-force ilerletilir; yayın başarısı gerçek main ve içerik geri okumasıyla doğrulanır. Geçici inceleme commit'i `6b448f79...` hiçbir branch'e bağlanmadı ve onun placeholder dosya yolları final ağaca dahil değildir. Dosya/test/plan sürümü tamamlanma oranı değildir.
