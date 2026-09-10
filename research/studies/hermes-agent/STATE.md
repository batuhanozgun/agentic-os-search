# Hermes Agent — STATE

**Durum:** ACTIVE RESEARCH / UI-PROFILE CALLER EVIDENCE + RECOVERED PENDING-CALLER DELIVERY  
**Son kayıt:** 2026-09-10  
**Kaynak pin:** `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`  
**Mevcut plan:** [RESEARCH-PLAN](RESEARCH-PLAN.md), v0.11.  
**Araştırma tamamlandı mı?** HAYIR. Normal CLI/gateway kaynak zinciri ve ayrı bounded policy kayıtları ilerledi; gerçek prompt/request, bütün UI/profile/worker entegrasyonu ve genel sentez açık.

## Yetkilendirilmiş amaç ve son yayın

Amaç önce HERMES-native mekanizma modeli, sonra Information/Work/Actors/Environment ve SOUL/Development OS değerlendirmesidir. Kullanıcının araştırmaya devam yetkisi sürer; son talebi gönderilememiş paketin yeniden yayımlanmasıdır. Bu tur yalnız o teslimi kalıcılaştırıp devam kayıtlarını uzlaştırdı. Yeni araştırma veya HERMES deneyi başlatılmadı.

OpenClaw ayrı adaydır. Kurulum, bütün ürünü başlatma, provider/model çağrısı, gerçek credential kullanımı, upstream değişikliği, Codex görevi, Foundation aktivasyonu veya adoption kapsamda değildir. Yanıtlar arasında otomatik/background iş yapılmaz. Codex başka repository kullanır; research main hareketleri ona atfedilmez. Ayar/izin değiştirilmedi; geçmiş araç hatasına doğrulanmamış kök neden atanmadı. Kapsam yalnız HERMES paketi ve katalogdaki HERMES satırıdır.

## Birikimli durum ve korunmuş kanıt

| Dilim | Kalıcı giriş ve statü |
|---|---|
| İlk keşif / U01 review | [01](notes/01-ORIENTATION.md), [02](notes/02-BACKGROUND-LEARNING.md); pin, snapshot/fork/köken/guard kaynakları |
| U01-C curator | [03](notes/03-SKILL-CURATION.md); bakım/report/cron/rollback, kendi kimliği korunur |
| U01B / U01B2 | [04](notes/04-SKILL-WRITE-TRANSACTION-AND-APPROVAL.md), [08](notes/08-APPROVAL-ROUNDTRIP-AND-ROLLBACK-BOUNDARIES.md); ayrı bounded skill/onay deneyleri |
| U01-DOC | [05](notes/05-DISPATCH-CONTEXT-AND-REPLAY-CONTRACTS.md); sekiz unpinned belge/K01–K09 tarihsel tasarım |
| U01-D / U01-M | [06](notes/06-CALLER-DISPATCH-AND-CONTEXT-TRANSFER.md), [07](notes/07-MEMORY-STORE-AND-PENDING-REPLAY.md); caller/store kaynakları ve eski transport kanıtı |
| U01-D2 / D3 | [09](notes/09-WORKER-POLICY-EXECUTION-BOUNDARY.md), [10](notes/10-REVIEW-ADMISSION-AND-MIDDLEWARE-FAILURES.md); selected worker/C/V, 22 manuel-range AST ve exact middleware MW |
| U01-M2 | [11](notes/11-MEMORY-STATE-AND-PENDING-LIFECYCLE.md); beş tam modül/N01–N12, 91af441 v0.9 yayını |
| U01-M3 UI/A | [12](notes/12-UI-PROFILE-AND-APPROVAL-CALLERS.md) → [UI araştırma](evidence/2026-09-10-ui-profile/RESEARCH.md), [UI SOURCES](evidence/2026-09-10-ui-profile/SOURCES.md), [A01–A08](evidence/2026-09-10-ui-profile/RESULT.json). 1599365 v0.10 kaydı değişmeden korunur. |
| U01-M3 M3-S/SA teslimi | **[13](notes/13-PENDING-CALLER-EVIDENCE-RECONCILIATION.md)** → [ayrı araştırma](evidence/2026-09-10-pending-caller/RESEARCH.md), [M3-S SOURCES](evidence/2026-09-10-pending-caller/SOURCES.md), [SA01–SA08](evidence/2026-09-10-pending-caller/POLICY-RESULT.json). Önceden koşulmuş ZIP teslimi bu tur yayımlandı. |

Önceki 01–12 notları, bütün eski evidence ve exact [SOURCE-LEDGER-THROUGH-V0.9](SOURCE-LEDGER-THROUGH-V0.9.md) korunur. [V0.10 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/159936556f34e7e0e1dafcb54c087bef994cf5ba/research/studies/hermes-agent/STATE.md) önceki tam ayrıntıları taşır. Donmuş defter ve eski notların next-work ifadeleri current authority değildir.

## İki M3 kaydının epistemik ayrımı

UI/A ve M3-S/SA aynı U01-M3 adını kullanmış ayrı kayıtlardır; biri diğerinin yerine geçmez. Ortak slash_access.py blob'u `07204201e411f29f912bb9bba6beec0566acab9d`, 5666 byte. İki koşu da Python 3.13.5/Linux ve sentetik config/source holder'larıyla sınırlıdır.

- **UI/A koşusu:** UTC `2026-09-10T05:42:55.258536+00:00`; A01–A08, bozuk-source pre-import reddi ve ayrı always-allow mutant kontrolü. Gerçek UI/profile/store/provider koşusu yok.
- **M3-S/SA koşusu:** UTC `2026-09-10T05:12:08.954654+00:00`; SA01–SA08 ve bozuk-source pre-import reddi. SA06 profile-only/supplied-config duyarlılığı deployment izolasyon açığı değildir; SA08 boş chat_type davranışı normal adapter hatası değildir. Always-allow mutantı bu koşuya mal edilmez.

Örtüşen source trace bağımsız doğrulama olarak sayılmaz. Kod, senaryo, sonuç, negatif kontrol ve koşu zamanları kendi defterlerine bağlı kalır; sayılar ürün PASS toplamı veya tamamlanma oranı değildir. Hiçbir eski koşu bu yayında tekrar edilmedi.

**SOURCE OBSERVATION:** CLI live/fresh ve gateway fresh-store; normal ingress auth/canonical slash gate/busy-idle/shared apply; profile wrappers/context-local home/transport damgası; record alanları; mode setter/eviction ve payload apply ayrımı; diff truncation. M3-S12/S13 ayrıca memory_parts/build/invalidate/cached-turn kaynak bağını taşır. Büyük caller kaynakları yürütülmüş değildir; UI09 ve M3-S10 upstream test kaynağı NOT RUN.

**BOUNDED INFERENCE:** Command-name yetkisi subcommand/kayıt sahipliğine eşit değildir; aynı active home'a giden session'lar bu storage katmanını paylaşır; M2 disk/live ayrışmasının etkisi live/fresh store ömrüne bağlıdır. Transport home, routed runtime home, pairing-store ve supplied slash config tek profile kavramına indirgenmez.

**OPEN:** Tam route/transport auth ve hook yolları; gerçek config ownership/multi-session cache; actual UI hata enjeksiyonu; apply/cleanup/reload/request bütünlüğü. Üretimde yetkisiz erişim, olay oranı veya öğrenme kalitesi hükmü verilmez.

## İlk sonraki aktif yetkili iş — onaydan prepared request'e

Q07/Q22: CLI mevcut ajanında ve gateway cached-agent reuse yolunda yeni dosya içeriği ne zaman store/frozen snapshot/stored-cached prompt/prepared request'e taşınır?

12'nin yönü korunur; 13/M3-S12/S13'ün somut rotasıyla `agent/conversation_loop.py::_restore_or_build_system_prompt` açılır. Yeni store'un eski DB system prompt'unu yeniden kullanması, compression/keep-prompt, invalidation/rebuild ve cache reuse/eviction alternatifleri kaynakla ayrılır. Ne apply success'in hemen modele görünürlüğü ne de cache'in kesin eski kaldığı baştan varsayılır. `/memory approval on` ile `/memory approve <id>` aynı etki değildir.

Önce pinned kaynak bağı; sonra güvenli offline prepared-request readback mümkünse gerçek/sentetik sınırlar ve karşı senaryolarla çalışılır. Provider/credential veya bütün ürün kurulumuna geçilmez. Normal yazım, silme, hata ve restore/reload ayrımları korunur. Bounded durma noktası hangi çağrının hangi görünümü yenilediği ve hangi dalın açık kaldığıdır.

Ardından ledger/backup/restore/sync → skill/cache → U01-C nested batch/report/cron ve trigger/cancel/shared-store; U02–U04+ ve F01–F12 genişliği sürer. Actual normal UI caller'larını ilk kez bulunacak iş gibi başa alma; aynı A/SA/N/C/V fixture tekrarı full-path kanıtı değildir.

## Ertelenmiş ileri doğrulama

Q26/Q29 full review/AIAgent/executor/PluginManager/Relay ve tam E01/E02 local originals ile legacy verify_excerpts.py OPEN/NOT RUN. E01 `799199c10f9930da77c01da2324373614b27cb78`; E02 `da8d7e2c68b2346e6ecc15567d755d96085ef767`. D3'ün iki manuel transkripsiyonla 22 AST eşleşmesi full-original doğrulama değildir. Yeni tam materyalizasyon/bağımlılık erişimi, source değişimi veya load-bearing tasarım/adoption/güvenlik hükmü yeniden açma tetikleyicisidir.

Native alt-sistem sentezi, genel ilişkiler, dört-alan projeksiyonu ve CORE tamamlanmadı. Bir scope/security adayı HERMES'in geri kalanını yutmaz. Mandatory control/authorization/state çelişkisinde etkilenen iş durur; bitiş ölçütü METHOD'dur.

## Yayın ve yeni oturum

Hazırlıkta main 91af441 idi; son kontrolde 1599365'e ilerlediği görüldü. Eski detached aday e91745f main'e zorla bağlanmadı; teslim güncel ağaca eklenip 12 korunarak 13 açıldı. [PUBLICATION](evidence/2026-09-10-pending-caller/PUBLICATION.md), [TRANSFER-CHECK](evidence/2026-09-10-pending-caller/TRANSFER-CHECK.json). 18 özgün dosyanın yeniden konumlandırılmış tree kimliği `246a833b3a13414be817a02fa58f4b5259126fb0`, yerel hesap ile uzak geri okumada eşleşti. Aktarım davranış doğrulaması değildir.

Cold start: canonical bootstrap → root/studies catalog → META/STATE/INDEX → METHOD/plan v0.11 → **12/UI ve 13/M3-S-SA'nın ayrı sınırları + 13 PUBLICATION**. Görünürlükte 07/11/M2 ve M3-S12/S13'e; Q26 yeniden açılırsa 09/10/E/J'ye dön. Delivery içindeki eski 12 taslağı, NOT PUBLISHED/NOT APPLIED ve eski planlar tarihsel teslimdir. Yeni oturum sohbet ZIP'ine ihtiyaç duymadan iki kaydı da bulabilir; kullanıcı elle dosya taşımaz.
