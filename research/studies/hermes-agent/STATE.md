# Hermes Agent — STATE

**Durum:** ACTIVE PARTIAL RESEARCH / GENERAL TURN–CONTEXT–SESSION SOURCE MODEL  
**Son kayıt:** 2026-09-10  
**Primary:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release doğrulaması değil.  
**Plan:** [v0.14](RESEARCH-PLAN.md). **Bütün araştırma tamamlandı mı? HAYIR.**

## Güncel amaç ve yetki

Kullanıcı genel ajan döngüsünü özellikle önemseyip özenli araştırmayı ve operasyonel sınıra kadar devamı yetkilendirdi. Bu dilim normal giriş/oturum → bağlam → model/araç → kayıt → teslim zincirini genişletir. Amaç önce HERMES-native mekanizma/sistem açıklaması, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesidir.

Yalnız HERMES study ve CATALOG'daki HERMES satırı değişebilir. Kurulum, bütün ürünü çalıştırma, model/provider/gerçek credential kullanımı, upstream mutation, Codex görevi, Foundation/control veya adoption yetkisi yoktur. OpenClaw ayrı adaydır. Codex başka repo kullanır; main hareketleri ona atfedilmez. Yanıtlar arasında otomatik/background iş veya uygulama/izin ayarı değişikliği yapılmaz.

## Bu dilimde gerçekten ilerleyen iş

[16/U02](notes/16-GENERAL-TURN-CONTEXT-AND-SESSION.md) → [araştırma](evidence/2026-09-10-turn-lifecycle/RESEARCH.md), [C01–C18 ve reused R01/R02 kaynak defteri](evidence/2026-09-10-turn-lifecycle/SOURCES.md). **Yeni HERMES deneyi çalıştırılmadı.** Yeni değer, actual normal caller/phase ilişkileri ve ikinci provisional üst modeldir; eski dar fixture'lar çoğaltılmadı.

- Normal gateway: resolved session lease → durable active-turn işareti → history read/hygiene → cached/fresh agent → gerçek run_conversation → generation-gated result/persist/delivery kaynakla bağlandı. Unreadable transcript boş history sayılmıyor. Lease/generation'ın varlığı bütün process/harici etki izolasyonu değildir.
- Genel çekirdek: user turn, model–tool iteration ve API attempt ayrı. Clean transcript/api_content/frozen-system/per-turn recall/API-message copy ayrıldı. Request/execution middleware ve transport alt sınırları açık.
- Tool round + gerçek persistence mixin: DB-backed flush False etkiden önce durdurur; isolated/no-DB None ayrı yoldur. Etki sonrası kayıt hatası rollback veya exactly-once garantisi değildir.
- **M4'ü daraltan actual caller kanıtı:** admitted compaction invalidate/reload ardından gerçek build yapar; keep-prompt yalnız yeni/eski metin byte-equal ise korunur. Normal dönüşte yeni active prompt API-message yoluna bağlıdır. M4/V04 artificial invalidate→restore sırası gerçek normal compression sırası değildir.
- Stop/finalizer/delivery: final metin optional gate'lerle yeniden devam edebilir; completed, task acceptance, kalıcılık ve kullanıcıya teslim tek sonuç değildir. Review hesaplama başlangıcı ile bildirim-after-delivery ayrı; on_session_end adı gerçek nesne sonu varsaydırmaz.
- Kanban terminal-tool nudge/task timeout ve goal/loop/heartbeat göçleri tur-üstü iş mekanizmalarını açtı; gerçek task/claim/receipt sistemi henüz incelenmedi.

[İkinci provisional sentez](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md) ve [targeted kapsam haritası](inventory/CORE-COVERAGE-2026-09-10.md) bu ilişkileri birleştirir. **Recursive bütün repository envanteri yapılmış sayılmaz.** Native bütün sistem/CORE/dört-alan veya kalite/adoption sonucu yoktur.

## Korunan önceki kanıt ve açık sınırlar

01–15 notları, synthesis/01, tüm eski evidence ve exact SOURCE-LEDGER-THROUGH-V0.9 değişmeden korunur. [V0.13 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/c163836d959e3ada2f31afd353bb364671b5fb32/research/studies/hermes-agent/STATE.md) önceki AP/M4 detaylarını taşır. A/SA/AP ayrı eski koşular; AP original15 kapanışı a14c815'tedir. M4/V01–V08 selected prompt experiment'in full-parent/fake-DB/reduced-builder sınırları sürer. Hiçbiri bu dilimde yeniden koşulmadı veya bağımsız doğrulamaya yükseltilmedi.

**Q07/Q22:** normal refresh caller ve API-message taşıyıcısı artık source-backed; gerçek approval-to-final-network payload/zaman, bütün compression/engine/provider/CLI varyantları hâlâ OPEN. In-place archive ile prompt update ayrı çağrılardır; actual SQLite crash/atomicity doğrulanmadı.

**Q26/Q29:** full AIAgent/review/executor/PluginManager/Relay ve E01/E02 full-original legacy verifier OPEN/NOT RUN. D3 manuel AST eşleşmesi ikame değildir. Yeni kaynak/bağımlılık, ilgili değişiklik veya load-bearing reuse yeniden açar. Full profile/auth/hook, physical cancellation, real scanner, delivery acknowledgement ve gelecek-task fayda açık.

## İlk sonraki aktif yetkili birim

**Tur-üstü kalıcı iş ve terminal kabulü: önce kanban task/claim/run/receipt.** C17 ve C12'deki çağrı noktalarından task create/claim/dispatch/run → complete/block → terminal kaydı tüketen dispatcher'a in. Araç adının konuşmada görünmesi ile başarılı DB transition/accepted result ayrılmalı. Normal yol ve en az bir interruption/retry/claim-loss karşı yolu source ile açıklanmalı; uygun offline deney gerçek transition consumer'ı sınamalı, salt nudge helper'ı değil.

Bu seçim [kapsam haritası §4](inventory/CORE-COVERAGE-2026-09-10.md) ile gerekçelidir: iç tur modelini kullanıcı işinin kalıcı kabulüne bağlayan açık katman. Her sohbetin kanban task'ı olduğu veya goal/loop/heartbeat'in aynı mekanizma olduğu varsayılmayacak. Ardından bu diğer tur-üstü yollar ve actual SessionDB/lease/restore sınırları bağlanır. Genel F01–F12 ile ledger/sync/skill-cache/curator, provider/backend/delegation, scheduler/diğer UI/install/eval açık tutulur.

## Cold start ve yayın sınırı

Bootstrap → root/studies catalog → META/STATE/INDEX → METHOD/plan v0.14 → **synthesis/02 + 16/U02 SOURCES/RESEARCH + CORE-COVERAGE**. M4'ün anlamı için 15/RESULT ve synthesis/01; eski approval/failure kanıtı için 07/11/M2; Q26 yeniden açılırsa 09/10/E/J.

Yayın tabanı olarak c163836... içindeki güncel ağaç kullanılır; ondan önceki 917d981... üzerine yeni explorations çalışmaları gelmişti ve korunmalıdır. Önceki tool/429 ifadeleri tarihsel; güncel yazma başarısı yalnız gerçek final ref/content readback ile doğrulanır. Mandatory control/authority/state çelişkisinde etkilenen iş durur. Dosya/test/sürüm sayısı tamamlanma oranı değildir.
