# Hermes Agent — STATE

**Durum:** ACTIVE PARTIAL RESEARCH / SELECTED PROMPT-RESTORE EVIDENCE + FIRST PROVISIONAL SUBSYSTEM SYNTHESIS  
**Son kayıt:** 2026-09-10  
**Primary:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release doğrulaması değil.  
**Plan:** [v0.13](RESEARCH-PLAN.md). **Bütün araştırma tamamlandı mı? HAYIR.**

## Yetki ve bu turun kapanan işleri

Kullanıcı derin durum değerlendirmesini kabul edip devamı yetkilendirdi. Aynı turda iki ayrı ilerleme oldu:

1. `a14c8152a918a3379b4a0d6d67af9f7aece2f70e` ile AP'nin 15 özgün dosyası ve [kapsam değerlendirmesi](inventory/SCOPE-REVIEW-2026-09-10.md) yayımlandı, main geri okundu. Bu eski teslimin recovery'sidir; eski deney tekrarı değildir.
2. Yeni [15/M4](notes/15-MEMORY-PROMPT-RESTORE-BOUNDARIES.md) araştırması ve V01–V08 koşusu, ardından [ilk geçici alt-sistem sentezi](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md) üretildi. Tam model isteği/gerçek UI/compression entegrasyonu kapanmadı.

Amaç önce HERMES-native mekanizma/sistem açıklaması, sonra dört alan ve SOUL/Development OS değerlendirmesidir. Yalnız HERMES paketi ve CATALOG HERMES satırı değişebilir. Kurulum, bütün ürünü çalıştırma, provider/model çağrısı, gerçek credential, upstream mutation, Codex görevi, Foundation/control değişimi ve adoption yetkisi yoktur. OpenClaw ayrı aday. Codex başka repo kullanır; main hareketleri ona atfedilmez. Yanıtlar arasında otomatik/background iş ve izin/uygulama ayarı değişikliği yoktur.

## Kalıcı kanıt ve güven sınırı

01–14 notları, eski evidence paketleri ve exact SOURCE-LEDGER-THROUGH-V0.9 korunur. [Önceki v0.12 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/a14c8152a918a3379b4a0d6d67af9f7aece2f70e/research/studies/hermes-agent/STATE.md), INDEX ve SOURCE-LEDGER geçmişe döndürür.

A/SA/AP üç ayrı eski kayıttır; aynı slash-policy modülünü ve örtüşen soruları kullanır. Test/negatif kontrol/zamanlar birleşmez; independent corroboration veya ürün PASS toplamı değildir. AP'nin original 12 taslağı/NOT PUBLISHED metinleri tarihsel, current giriş 14'tür. AP bilinen kayıt eksikliği kapandı; daha güçlü bütün geçmişe dair güvence yalnız gerçekten envanteri yapılmış kapsam için kullanılır.

**M4 yürütmesi:** UTC `2026-09-10T16:11:51.320434+00:00`. Beş exact archived M2 modülü + altı manually selected prompt definition. Sentetik DB/agent/reduced builder/callback/capability çevresi; actual temporary-file memory/pending etkileri. V01–V08 beklentileri eşleşti; full-source/local-selection identity reddi ve iki comparator mutantı ayrı. Eski N/A/SA/AP suite'leri tekrarlanmadı. Ortak M2 fixture'ı bağımsızlık sağlamaz. Seçki hash'i full-parent byte fidelity değildir.

**Bulgu:** Fresh memory snapshot'a rağmen compatible DB stored prompt seçilebildi; unusable stored prompt/no-history/runtime mismatch gibi yollar fresh build'e gitti. Reload/invalidation/DB persist ayrı; delete de aynı görünürlük sınırını taşıdı. V04'ün invalidate→restore sırası harness kontrollüdür, actual compression kusuru değildir. V07 fake DB arızası SQLite sonucu değildir.

**Açık:** Gerçek CLI/gateway'de stale süre, tam prompt builder, cached-agent reuse/eviction, actual compression/keep-prompt, turn_context/request assembly ve son provider içeriği. Source 429 erişim sınırı bu halkaları kapatmadı; kaynakta mekanizma yokluğu değildir. Yeni döngü source trace'i seçicinin turn_context'e verildiğini ve ayrı request fazlarını gösterir; bunlar yürütülmedi. Q07/Q22 end-to-end OPEN, bounded selector geçişi artık yeni kanıtla açıklanır.

## İlk sonraki aktif yetkili iş

**Genel turn/context/session çekirdeği ve geniş kaynak-topoloji karşı okuması.** Amaç U01'i daha fazla küçük teste bölmek değil, ilk geçici modelin hangi geniş mekanizmaları dışarıda bıraktığını bulmaktır. Başlangıç: M4-S03 gerçek `run_conversation` → turn_context/request/preflight/compression/session persistence; ilişkili gateway cache yaşam döngüsü. Pinned alt ağaçlar/kritik entrypoints çıkarılır, listelenmiş/read/source-backed/executed/synthesised ayrı tutulur. Birkaç bilinmeyen dosyaya dayanarak bütün aile kapanışı verilmez.

Q07/Q22'nin kalan prepared-request bağlantısı bu genel çekirdeğin önemli köprüsüdür; terk edilmez veya kapalı ilan edilmez. Erişim izin verdiğinde actual caller order ve request assembly doğrulanır; aynı V/A/N fixture'larını çoğaltmak yeterli değildir. Geçmiş 429 kalıcı erişim yokluğu olarak kullanılmaz, fakat seri tekrar veya kısıt etrafından dolaşma yapılmaz.

Ardından ledger/backup/restore/sync, skill-cache ve curator nested batch/report/cron; tool/provider/backend/delegation, gateway/scheduler, diğer UI ve install/eval ailelerinin önceliği kapsam haritasıyla belirlenir. Bütün U01 residual'ları kapanana kadar genel kapsam ertelenmez. İlk sentez mevcut üst katmandır; nihai native sistem/CORE/dört-alan veya learning-quality sonucu değildir.

## İleri doğrulama ve cold start

Q26/Q29 full AIAgent/review/worker/executor/PluginManager/Relay ve E01/E02 full-original legacy verifier OPEN/NOT RUN. D3'ün 22 manuel-range AST eşleşmesi full-original fidelity değildir. Yeni tam-source/bağımlılık, ilgili değişiklik veya load-bearing güvenlik/adoption/tasarım hükmü yeniden açar. Full profile/auth/hook/platform, scanner, actual UI fault injection ve gelecek-task fayda da açık.

Bootstrap → research/studies routers → META/STATE/INDEX → METHOD/plan v0.13 → kapsam değerlendirmesi → **synthesis/01 ve 15/M4 SOURCES/RESEARCH/SPEC/RESULT sınırları**. Eski 12/13/14 source ve koşu kimlikleri ayrı; görünürlükte 07/11/M2'ye dön. Yeni dosyaların core local/remote tree'si `8dd2cfd73516926b5bc7d1adf0737556c2d6bf61` eşleşti; bu yalnız transferdir. Final commit/ref readback ayrıca yapılır. Mandatory authority/control/state çelişkisinde etkilenen iş durur.
