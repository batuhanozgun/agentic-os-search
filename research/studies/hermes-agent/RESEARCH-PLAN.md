# Hermes Agent — Araştırma planı

**v0.15 / 2026-09-11 — U03 publication recovery.** İş otoritesi [STATE](STATE.md), yöntem/kapanış [METHOD](METHOD.md). [V0.14 tam plan](https://github.com/batuhanozgun/agentic-os-search/blob/25b06521083e2a4ddf7b0dbeb9454804796963b6/research/studies/hermes-agent/RESEARCH-PLAN.md) ve [CORE-COVERAGE](inventory/CORE-COVERAGE-2026-09-10.md) korunur.

## 1. Hedef ve mevcut düzey

Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; manifest 0.21.0. Önce native mekanizmalar/sistem ilişkileri; sonra dört-alan ve SOUL/Development OS. İki provisional synthesis vardır: learning/change ve general turn/context/session. Genel kaynak kapsamı hâlâ kısmi; version/test/file sayısından yüzde veya kalite sonucu çıkarılmaz.

## 2. V0.15'in farkı

[17/U03](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md), önceki kalıcı iş kaynak okumalarını ve önceden oluşturulmuş K01–K08 evidence'ını kayda alır. **Bu yayın turunda yeni HERMES deneyi yapılmadı.** Ham 15-file arşiv ve ayrı draft README değişmeden korunur; okunabilir companion'lar ve result summary recovery'de hazırlandı. [PUBLICATION](evidence/2026-09-10-kanban-task/PUBLICATION.md), kaynak/koşu/kurtarma/yayın ayrımını ve önceki final açıklamasının düzeltmesini taşır.

Task → dependency/claim → run → complete/block/review → transaction/post-commit/recovery için source modeli açıldı. K seti gerçek SQLite üzerinde manuel seçilmiş definition'ları ve azaltılmış DDL'yi kullanır. Full parent byte/AST ve actual full-module runtime NOT VERIFIED. Recorded input/probe hash matching, source fidelity veya independent replication değildir.

## 3. Sıradaki yetkili teknik birim

Soru: **Kalıcı bir Kanban görevi birden fazla ajan turunda nasıl sürdürülür; mevcut run'ın terminal handoff veya sahiplik kaybı bu devamı nasıl durdurur? Goal, loop ve heartbeat bununla aynı mı farklı mı sürekliliklerdir?**

Önce primary'de `_worker_argv` ve goal-mode quiet CLI çağrısından actual `run_kanban_goal_loop` tüketicisine, `goal_run_status` ve tool `_goal_gate`/`judge_goal` ilişkisine ilerle. Mevcut run'ın bitişi, task'ın sonraki run'ı, yardımcı judge'ın kararı ve kullanıcının kabulü ayrı tutulmalı. Gerçek callback/DB tüketicisine kadar normal yol ve bir ownership-loss/interrupt/yeniden başlatma karşı yolu açıklanmalı. Ardından goal/loop/heartbeat kalıcı state ve tetikleme farkları karşılaştırılmalı.

Beklenen çıktı test sayısı değil: hangi kimlik ve kayıt birkaç turu aynı işin devamı yapıyor; dur/devam/kabul sınırı nerede; hangi yollar farklı bir native mekanizma gerektiriyor? Yeterli kaynakta sınırlı offline kontrol yapılabilir, fakat kurulum/model/provider/gerçek credential veya bütün ürün çalıştırma yetkisi genişlemez. Bu recovery turu bu yeni teknik çalışmayı başlatmaz.

## 4. Yeniden açma ve kapsam dengesi

K seçkilerinin full-parent sadakati, daha güçlü behavioral/security hükmü için yeniden açılacak borçtur. Exact parent/bağımlılık erişimi sağlanırsa seçkiler otomatik/direct source karşılaştırmasıyla doğrulanır; yerel hash bunu ikame etmez. K01–K08'i aynı taklitlerle çoğaltmak actual dispatcher/goal/artifact/delivery coverage'ı sayılmaz.

Q07/Q22 normal compaction ve API-message bağlantısı source-backed; last-wire/timing/variant açık. Q26/Q29 full-original/full-worker verifier açık/NOT RUN. F01–F12 genişliği, actual SessionDB/lease/crash/search, ledger/sync/skill reuse/curator, provider/backend/delegation ve scheduler/diğer UI/install/eval önceki map'te tutulur. Tüm U01 veya K residual'larını bitirmek diğer ailelerin araştırılmasının ön koşulu değildir.

## 5. Yetki ve teslim ölçütü

Yalnız Hermes study + HERMES catalog row; eski evidence ve syntheses değiştirilmez. Foundation/control/context/Codex/upstream/adoption değişikliği yok. Bir sonraki mantıklı mimari aşama araştırma yetkisi sayılmaz. Sentezlere yükselme METHOD'a göre gerekçeli ve sınırlı olmalı.

Recovery teslimi: iki eski Git nesnesi main'de erişilebilir; archive/member kimlikleri ve result/probe bağı görünür; giriş/state/catalog tutarlı; current parent korunmuş; ref non-force ve içerik geri okuması gerçek. Çalışma tamamı değil yayın kapanır. Yeni kaynak araştırması, doğrulama, kayıt kurtarması ve repository yayını ayrı raporlanır.
