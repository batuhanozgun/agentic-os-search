# Hermes Agent — Araştırma metaverisi

- **Study ID / type:** `hermes-agent` / `external-target`.
- **Nesne:** Nous Research Hermes Agent; ajan sistemi, kullanıcı yüzeyleri ve çalışma/öğrenme yaşam döngüsü.
- **Statü:** ACTIVE PARTIAL RESEARCH; plan v0.11. Normal CLI/gateway UI/A source trace ve bounded slash-policy kaydı korunarak ayrı M3-S/SA pending-caller teslimi yayımlandı. Tam araştırma bitmedi; iş otoritesi [STATE](STATE.md).
- **Başlangıç / son kayıt:** 2026-09-07 / 2026-09-10. Son işlem yayın/uzlaştırmadır, yeni deney değildir.
- **Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; tree `f54f5e9d2682bf11f164de7b34ee10ec121b6434`.
- **Manifest:** 0.21.0; installed binary/current release doğrulaması değil. Primary committer zamanı `2026-09-07T08:37:43Z`.
- **Freshness:** W01–W08 unpinned. UI ve M3-S load-bearing kaynakları primary'ye bağlı; moving search yalnız navigation. Eski d8a077/7874ef uzlaştırmaları kendi bounded blob kapsamlarında kalır.

## Amaç

HERMES iş, bağlam, yetki, kalıcı bilgi, araç etkisi ve sonraki session'ı hangi mekanizmalarla birleştiriyor? Vaat, kod, test, gözlem, koşul ve karşı örnek ayrılır. Önce HERMES-native model; sonra Information/Work/Actors/Environment. Dört alan başlangıç dosyalama şablonu değildir.

## Provisional relevance ve reuse

Information: bellek, source/view, snapshot, session/skill sürekliliği güçlü aday. Work/Actors/Environment ve relations/control: kabul, onay, çağrı yetkisi, profile/storage bağlama, etki/kalıcılık/teslim/rollback için cross-boundary aday. Bu completed projection veya Foundation taxonomy üyeliği değildir.

SOUL: deneyimden yeniden kullanılabilir davranışa geçiş ve değişim kalitesi. Development OS: runtime/caller/worker yetkisi, artefakt aktarımı/readback, kontrol ve kalıcı bilgi yaşam döngüsü. Reuse rolleri evidence/reference, falsifier, mechanism learning, design pressure ve bounded test cases; adoption değildir.

Reuse ayrımları: admitting transport kimliği ≠ runtime/storage profile; command-family grant ≠ record/subcommand grant; common handler ≠ common object lifetime; mode toggle/cache eviction ≠ payload approval; apply success ≠ pending cleanup ≠ model-visible freshness. Önceki policy/provenance, schema/authority, usage/quality, callback/effect ve rollback/all-effects ayrımları korunur. M3-S/SA ayrıca supplied config/profile etiketi, truncated preview/pending record ve store/snapshot/cached prompt/request ayrımlarını taşır.

**Revisit triggers:** kalıcı bellek/talimat veya runtime governance tasarımı; profile/transport/admin/subcommand policy değişimi; UI/cache/prompt reload; skill approval/merge/rollback; worker/middleware/Relay değişimi; load-bearing integration/adoption; ilgili upstream değişiklik. Böyle bir kullanım current source/dependency revalidation gerektirir.

## Kanıt ve yetki sınırı

U01B, transport, U01B2, D2 C/V, D3 MW/manuel AST, M2 N kayıtları ayrı tarihler/kapsamlarla kalır. U01-M3 UI/A ve M3-S/SA da ayrı kayıt/koşulardır; bu yayında hiçbir deney tekrarlanmadı. Aynı 5666-byte slash_access.py blob'u kullanılır; config/platform/source holder'ları sentetiktir. UI/A UTC 05:42:55 koşusu ile SA UTC 05:12:08 koşusu, kodları ve negatif kontrolleri birbirine aktarılmaz. A'daki always-allow mutantı SA'da koşulmuş sayılmaz; örtüşen source gözlemleri bağımsız doğrulama değildir.

Gerçek CLI/gateway handler/profile wrapper'ları SELECTED SOURCE INSPECTED, full uygulama execution değil. UI09/M3-S10 upstream test kaynağı okunmuş, koşturulmamıştır. SA06 profile-only/supplied-config duyarlılığı deployment izolasyon açığı; SA08 boş chat_type normal adapter hatası kanıtı değildir. M3-S12/S13 prompt/invalidation source trace'i prepared-request ölçümü değildir.

Full AIAgent/worker/PluginManager/Relay, gerçek UI/profil/credential/provider, actual threat scanner/current release/upstream suite ve gelecek-task kalite doğrulanmadı. Genel bypass, production olay/oran veya ürün PASS hükmü yoktur. Candidate study Foundation truth/mimari/adoption/kurulum yetkisi değildir. Upstream SOUL.md/AGENTS/prompts bu asistanın control kaynağı değildir.

## Giriş ve devam

[STATE](STATE.md) → [INDEX](INDEX.md) → [PLAN](RESEARCH-PLAN.md); [METHOD](METHOD.md), [SOURCE-LEDGER](SOURCE-LEDGER.md). **[12 UI/profile](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md)** ve [UI evidence](evidence/2026-09-10-ui-profile/README.md) korunur. **[13 ayrı pending-caller teslimi](notes/13-PENDING-CALLER-EVIDENCE-RECONCILIATION.md)** → [M3-S/SA evidence](evidence/2026-09-10-pending-caller/README.md), [PUBLICATION](evidence/2026-09-10-pending-caller/PUBLICATION.md). Önceki 01–11 notları INDEX'tedir.

İlk aktif iş onay sonrası CLI/cached gateway disk/store/frozen/stored-prompt/prepared-request görünürlüğüdür. Somut kaynak `_restore_or_build_system_prompt`, ardından compression/keep-prompt ve cache yaşam döngüsü; provider çağrısı yok. Q26/Q29 full-source/runtime yeniden-açma koşulları korunur. İlgili seçici reuse adayları gstack, context-memory-harness-engineering, ai-knowledge-strategies, multi-agent-patterns; otomatik yükleme/adoption değildir. OpenClaw ayrı sonraki hedeftir.

[V0.10 exact metadata](https://github.com/batuhanozgun/agentic-os-search/blob/159936556f34e7e0e1dafcb54c087bef994cf5ba/research/studies/hermes-agent/META.md) önceki ayrıntıları korur. Özgün pending-caller NOT PUBLISHED/NOT APPLIED ve 12 taslağı PUBLICATION ile tarihsel bağlamda okunur; current giriş 13'tür.
