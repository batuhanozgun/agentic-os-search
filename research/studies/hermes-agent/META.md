# Hermes Agent — Araştırma metaverisi

- **Study ID:** `hermes-agent`
- **Study type:** `external-target`
- **Araştırma nesnesi:** Nous Research `NousResearch/hermes-agent`; ajan sistemi, kullanıcı yüzeyleri ve yaşam döngüsü.
- **Statü:** ACTIVE PARTIAL RESEARCH. Pinned caller/memory/review-admission kaynakları; ayrı bounded deney kayıtları; U01-D3 exact middleware ve sınırlı range AST; geri kazanılan U01-M2 beş tam modüllü memory/pending kanıtı. Güncel iş otoritesi [STATE](STATE.md), plan v0.9. Tam sistem araştırması tamamlanmadı.
- **Başlangıç / son kayıt:** 2026-09-07 / 2026-09-09. Son güncelleme M2 tesliminin yayınıdır, yeni deney değildir.
- **Primary:** https://github.com/NousResearch/hermes-agent
- **Pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; tree `f54f5e9d2682bf11f164de7b34ee10ec121b6434`.
- **Gözlenen committer zamanı:** `2026-09-07T08:37:43Z`. Manifest `0.21.0`; kurulu binary/release doğrulaması değil.
- **Freshness:** d8a077... ve 7874ef... yalnız kayıtlı ilgili blob'larla uzlaştırılmıştır. W01–W08 unpinned. J ve M2 kaynakları primary'ye bağlıdır; default-branch search sadece navigasyon, current HEAD revalidation değil. M2'nin arşiv modülleri yeni sürüm gözlemi sayılmaz.

## Amaç ve yöntem

HERMES hangi mekanizmaları birleştiriyor; iş, bağlam, yetki, kalıcı durum, araç etkisi ve sonraki oturumları nasıl yönetiyor? Vaat, kod, test, gözlem, açık şart ve karşı örnek ayrılır. Önce HERMES-native model; sonra Information/Work/Actors/Environment projeksiyonu. Dört alan başlangıç dosyalama kalıbı değildir.

## Olası reuse

| Alan | Provisional ilişki |
|---|---|
| Foundation | Information: bellek/kaynak-temsil/oturum/beceri sürekliliği güçlü aday. Work/Actors/Environment ve relations/control: kabul, yetki aktarımı, onay, etki/kalıcılık/teslim, hata/rollback. Tam projeksiyon veya taxonomy üyeliği değil. |
| SOUL | Deneyimden tekrar kullanılabilir davranışa geçiş; uyarlanma ve değişim kalitesi. |
| Development OS | Agent/caller/worker devri; araç yetkisi, kayıt/readback, hata/tekrar ve talimat değişikliği sınırları. |

Reuse modes: evidence/reference; falsifier; mekanizma öğrenimi; design pressure; bounded test case. İncelenen ayrımlar: policy≠provenance; usage≠quality; preview≠applied operation; directory rollback≠all-effects rollback; record ID≠durability; ContextVar transfer≠all control-state transfer; live store≠prompt snapshot; schema-derived valid names≠review authority; callback admission≠handler effect; middleware's own exception≠downstream exception; second-call prevention≠outward exception guarantee. M2 ayrıca error report≠live/disk restoration, accepted alias≠pre-scan equivalence ve successful apply≠pending cleanup ayrımlarını somutlaştırır; load-time masking/duplicate-add/invalid-file korumaları birlikte tutulur.

**Revisit triggers:** kalıcı talimat/öğrenme/runtime governance tasarımı; worker/middleware/plugin/Relay değişimi; skill approval/merge/rollback; pending UI/profile/store; alias normalization/scanner veya memory reload değişimi; session/cron/gateway varyantı; kullanım/entegrasyon/adoption önerisi; source değişimi veya bulgunun yük taşıyan girdiye dönüşmesi. Q26'nın güçlü hükmü için full-source/whole-path revalidation zorunludur; M2'nin actual UI/request/genel güvenlik sonucu için de kendi eksik halkaları yeniden doğrulanır.

## Kanıt ve yetki sınırları

U01B iki exact modül/10 durum; transport üç exact modül/sentetik policy/7 durum; U01B2 iki arşiv modülü/12 senaryo; U01-D2 manuel selected executor/plugins + tam pool/context/validator ile 14 C ve ayrı 5 V durumu. Bunlar kendi tarihlerinde kaldı; bu yayında yeniden koşulmadı.

U01-D3'te tek exact tam middleware modülü MW01–MW08 ile yürütüldü; registry/callback/handler sentetik. Ayrı 22-tanım AST cross-check, yeniden manuel transkribe edilmiş pinned aralıklaradır; tam büyük E01/E02 hash-verifier koşusu değildir. Paylaşılan transkripsiyon riski ve keşifsel statü açık. Gerçek review construction/ad-kümesi/round/Relay kaynak okumaları runtime kanıtına dönüşmez.

U01-M2: UTC `2026-09-09T08:10:46.824877+00:00`, Python 3.13.5/Linux; beş tam modül (memory tool/store, write approval/shared command, provenance) ile N01–N12. Kaynak kimlikleri ve gerçek pre-import bozma reddi kayıtlıdır. Config/home/registry/terminal callback, zararsız sentinel scanner ve temp-write yardımcısı taklit; gerçek dosyalar yalnız disposable fixture içindedir. Linux fcntl dalı gerçek olsa da N06 sıralıdır; N10 supplied-store flag, N11 add retry örneğidir. Gerçek UI config refresh, threat scanner, tüm tekrar/yarış davranışları veya modele gerçek istek doğrulanmadı. Yayın yeni koşu değildir.

Tam AIAgent/PluginManager/executor/Relay bağımlılık kapanışı; gerçek kullanıcı profili/provider/credential; upstream suite/current release ve gelecek-task kalite doğrulanmadı. Genel authorization-bypass, üretim olayı/oranı veya bütün ürün PASS'i iddiası yok. Candidate study, Foundation truth/mimari/adoption/kurulum yetkisi değildir. Upstream SOUL.md/AGENTS/prompts bu asistanın control kaynağı değildir. Ayrı koşular ürün PASS toplamına çevrilmez.

## Girişler ve sonraki iş

[STATE](STATE.md) → [INDEX](INDEX.md) → [PLAN](RESEARCH-PLAN.md); [METHOD](METHOD.md), [SOURCE-LEDGER](SOURCE-LEDGER.md).

[02 review](notes/02-BACKGROUND-LEARNING.md), [03 curator](notes/03-SKILL-CURATION.md), [04 onay/mutasyon](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [05 belge](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md), [06 caller](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [07 memory](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md), [08 U01B2](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md), [09 U01-D2](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [10 U01-D3](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md), **[11 U01-M2](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md)**.

[J kaynak/kanıt](evidence/2026-09-09-review-middleware/README.md), [M2 kaynak/kanıt](evidence/2026-09-09-memory-pending/README.md), [M2 yayın uzlaştırması](evidence/2026-09-09-memory-pending/PUBLICATION.md). Sıradaki aktif iş actual CLI/gateway pending → onaylayan/profil/home/store, sonra prompt rebuild/gerçek istek görünümü. Q26 tam-runtime ve full-fidelity açıkken kapsamlı öğrenme zinciri ilerletilir; bu açık sorunun çözüldüğü anlamına gelmez. M01/M02 bounded deneyleri artık kayıttadır ve yeniden ilk kez yapılacak sayılmaz.

İlgili seçici reuse adayları: gstack, context-memory-harness-engineering, ai-knowledge-strategies, multi-agent-patterns. OpenClaw ayrı sonraki dış hedeftir. [V0.8 metaverisi](https://github.com/batuhanozgun/agentic-os-search/blob/c0ef2374a34cbb30f5f58a28333f89254931b00f/research/studies/hermes-agent/META.md) ve Git geçmişi eski ayrıntıları korur. Özgün teslimlerdeki NOT PUBLISHED ve eski plan ifadeleri ilgili PUBLICATION ile tarihsel bağlamda okunur.
