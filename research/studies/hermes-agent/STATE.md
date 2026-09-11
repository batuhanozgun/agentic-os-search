# Hermes Agent — STATE

**Durum: U07 / plan v0.20 — CRON SCHEDULING, EXECUTION AND DELIVERY.**
**Yayın başlangıç main:** `d928ee14b16a277c010a966816fc2c4097944aab`; önceki U06/v0.19 yayını korunur.
**Research:** ACTIVE PARTIAL RESEARCH. **Bütün HERMES tamamlandı mı? HAYIR.**
**Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0; current release/kurulu ürün değildir.
**Tarih:** 2026-09-11. Bu checkpoint önceki U07 tesliminin yayın devridir; yeni teknik araştırma veya deney koşusu değildir. [U07 yayın durumu](evidence/2026-09-11-cron-scheduling-delivery/PUBLICATION.md).

## Güncel amaç, yetki ve kapsam

Önce HERMES-native mekanizma ve sistem açıklaması; sonra dört-alan/SOUL/Development OS değerlendirmesi. Kullanıcı U06'nın başarılı yayınından sonra araştırmaya devam edilmesini açıkça istedi; U07 teknik çalışması o yetkiyle yapıldı. Sonraki “yine gönderememe sorunu ile karşılaştın, tekrar dene” isteği yalnız hazırlanmış U07 tesliminin yayınını yetkilendirir. Güncel AGENT ve main/STATE yeniden okundu; aynı konuşmanın zorunlu protokolleri geçerlidir. Başlangıç main paket tabanıyla aynıdır. Eski yayınlar veya deneyler yeniden yapılmaz.

Yalnız `research/studies/hermes-agent/**` ve CATALOG'daki HERMES satırı değişebilir. Full product install/run, gerçek model/provider/credential, upstream/diğer repo/Foundation/context/Codex/control/architecture/adoption değişikliği yoktur. Otomatik/background çalışma veya izin/ayar değişikliği yok. OpenClaw ayrı adaydır; main hareketleri Codex'e atfedilmez.

**İlk U07 teknik turunda yayın yapılamadı:** o tur write/commit/ref eylemleri sunulmadı. Kullanıcının bu yeniden gönderme isteğinde bu eylemler sunuluyor. Neden değiştiklerine veya repository izinlerine ilişkin teşhis yapılmıyor. Özgün başarısız yayın kaydı PUBLICATION içinde tarihsel olarak korunur; güncel ref/content doğrulaması aynı dosyanın üst bölümünden okunur.

## Devralınan dar hedef ve erteleme

Q42 startup preclaim→adapter carrier/drain→actual agent admission ilk hedefti. Pinned startup wrapper 30–190 yeniden okundu: adapter dönüşünden sonra tek görülen task shield edilir. `gateway/run.py` 3150–3325 isteği 429 aldı; o aralık okunmuş sayılmadı, retry/dolaşma yapılmadı. Actual full-host/DB challenge kurulmadı. **Q42 ve actual SessionDB quiet next-request Q40 açık/ertelenmiştir.**

V0.19 planının açık erteleme kuralıyla F10 cron/scheduler→run→delivery ailesine geçildi. Bu geçiş dar borcu kapatmaz; bütün fault matrisi bitmeden broad native araştırmayı sonsuza dek bekletmez. Sırf yeni test sayısı için U06 registry veya U04 fixture'ları yeniden koşulmadı.

## Yeni U07 — gerçek ilerleme

[22 — Cron: scheduling/execution/delivery](notes/22-CRON-SCHEDULING-EXECUTION-AND-DELIVERY.md) → [RESEARCH](evidence/2026-09-11-cron-scheduling-delivery/RESEARCH.md) → [SOURCES](evidence/2026-09-11-cron-scheduling-delivery/SOURCES.md) → [coverage](inventory/CRON-COVERAGE-2026-09-11.md).

Kaynakla açılan: job save vs scheduler registration; recurring preadvance vs finite one-shot dispatch hakkı; profile-local jobs lock vs fail-closed per-job fence; execution audit/ownership/adoption/terminal/unknown; external worker acknowledgement ve belirsiz handoff; computation/delivery status ayrımı; exact-ID queue/tombstone; conditional no-error→delivered classification. Bunlar bütün cron ailesinin kapanışı değildir.

**Yeni yürütme yalnız tam orijinal `cron/delivery_queue.py`:** Git blob `689fd620d6193003bbd168a0e62770a0d0306ac6`, 13.837 byte; gerçek geçici SQLite/WAL, açık dependency seams ve synthetic transport. [SPEC](evidence/2026-09-11-cron-scheduling-delivery/SPEC.md), [RESULT](evidence/2026-09-11-cron-scheduling-delivery/RESULT.json), [MANIFEST/raw](evidence/2026-09-11-cron-scheduling-delivery/MANIFEST.json). UTC `2026-09-11T14:22:57.364884+00:00`–`2026-09-11T14:22:57.404381+00:00`; D01–D06 expectation_met; N00 source identity, N01/N02 mutant oracles ilgili davranış farklarını ayırdı. Raw RESULT SHA-256 `c53f850cceaad5e84eb800ce88b02c9a4eb227a00d82ee1714aecaefe7b51719`.

D01 None/hata-yok dönüşüyle birlikte DB pending kaldı; D03 delivering timeout unknown ve late finish reddi; D06 gerçek SQLite-trigger terminal-write fault sonrası bir callback, delivering→unknown ve ikinci callback yok. Diğerleri exact-ID tekrar/tombstone ve processed-count/failed ayrımıdır. D01 sıfır callback alanı tüketicisiz setup açıklaması; D02/D05/D06 gerçek recording callback sayılarıdır. Source-bound outer classifier bağlantısı **çalıştırılmamış koşullu çıkarım** olarak ayrı tutulur. No-error queue deferral, uygun üst koşullarda delivered sınıfına girebilir; bütün UI/current-version davranışı kanıtlanmadı.

İlk harness girişimi metadata toplamada kendi subprocess yasağına takıldı, case/DB başlamadı. Yalnız platform metadata ifadesi değişti; SPEC/source/oracles aynı kaldı; attempt-00 probe/log/hash saklandı. Bir başarılı behavioral run vardır, başarısız bootstrap yeşile çevrilmedi. Bu actual SessionDB, network, GatewayRunner, foreign owner/process restart, model kalitesi, bütün cron veya bağımsız replication değildir.

## Korunan yayın ve kanıtlar

U04-A [18](notes/18-MULTI-TURN-GOAL-LOOP-AND-HEARTBEAT.md), ayrı U04-B [19](notes/19-U04-DELIVERY-RECONCILIATION.md), U05 [20](notes/20-SESSION-LEASE-HISTORY-AND-RECOVERY.md), U06 [21](notes/21-RESUME-ADMISSION-AND-DRIVER-RECOVERY.md) zaten canonical yayınlardır. U06 içerik `8779ce350b32d5a1ccee6fa48c31604dd93616cc`, yayın makbuzu `d928ee14b16a277c010a966816fc2c4097944aab`. **U06 eski ZIP'ini tekrar gönderme işi yoktur.** Bu yayın checkpoint'inin konusu U07'dir; eski U06 paketi değildir.

U04-B'nin 33 original dosyalı subtree'si `d01c92f7414713300934be3bb4e3d40ac57631b3`; [A/B reconciliation](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. Aynı G/H numarası aynı vaka değildir; A 15/B 21, U06 L ve U07 D sayıları independent replication veya ürün skoru oluşturmaz. B:H09 reduced adapter actual SessionDB fault değildir; U07 D06 ise başka bir queue modülünün gerçek SQLite trigger fault'udur, eski B sonucunun genişletilmesi değildir.

Bütün notes01–21, eski evidence, METHOD ve merkezi [01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md)/[02](synthesis/02-TURN-CONTEXT-AND-SESSION-PROVISIONAL.md)/[03](synthesis/03-PERSISTENT-WORK-AND-CONTINUATION-PROVISIONAL.md) değişmeden bırakıldı. 20/21/22 source amendments birlikte okunur; dördüncü completed model/final CORE yoktur. [V0.19 exact STATE](https://github.com/batuhanozgun/agentic-os-search/blob/d928ee14b16a277c010a966816fc2c4097944aab/research/studies/hermes-agent/STATE.md) eski raw/source kimlik zincirini taşır.

## İlk sonraki teknik iş

**Cron delivery'nin gerçek gateway drainer/profile/transport caller'ı ve queued/delivered/finished status tüketicileri.** Exact execution kimliği, callback sonucu, durable queue durumu, job/execution outcome ve dış makbuz normal + deferred/uncertain yolda bağlanmalı. Default-branch navigation pinned/current implementation yerine geçmez. Aynı D/L fixture'larını artırmak bu consumer açığını kapatmaz.

Ardından scheduled occurrence/late external callback/due/claim/rearm ve shared `run_job` içindeki script/agent/preflight/history yolu. Q47–Q49 bunları izler; Q46 compute-vs-delivery yeni queue kesitiyle genişler. Q40/Q42 explicit deferred, Q41 migration/profile, Q43 full worker/effect, Q44/Q45 kalite/stop semantics açık kalır. Q07/Q22 wire/variants, Q26/Q29 full worker, Q38 manual K/G parent fidelity korunur. Provider/backend/delegation, diğer UI/install/eval ve skill-ledger/sync/quality geniş haritada kaybolmaz. Foundation veya mimari/adoption'a geçilmez.

## Cold-start / yetki yolu

1. Güncel main AGENT ve tetiklenen protokoller → research root/studies catalog → current META/STATE/INDEX → METHOD/plan.
2. U07 için canonical INDEX → note22 → U07 PUBLICATION/README/MANIFEST yolu izlenir. Note22, RESEARCH, SOURCES ve coverage içindeki unpublished ifadeler açıkça ilk teslim anını kaydeder; güncel yayın hükmü PUBLICATION üst bölümündedir. Doğrulanmış yayın sonrasında eski sohbet ZIP'i gerekli değildir.
3. U04 ayrımı için 19 + B README/RECONCILIATION/manifest; üst açıklama için synthesis/03 + A SOURCES/RESEARCH/CONTINUITY-COVERAGE. Bunlar aynı konuşmadan sonraki gerçek cold-start'ta STATE'in eski mandatory yolunu korur.
4. U05/20 ve U06/21 SOURCES/RESEARCH/coverage; ardından U07/22 SOURCES/RESEARCH/CRON-COVERAGE. Eski 'first next' veya source429 kayıtları tarihsel kapsamlarıyla okunur.
5. Exact U07 execution için SPEC + tam RESULT + MANIFEST + arşivdeki source/probe/inputs/log/DB/attempt-00. Exact eski A/B/L iddiaları için kendi raw/probe'u; summary yeterli değildir.

## Yayın ve sonraki yetki

Bu checkpoint yeni araştırma değil, mevcut U07 dosyalarının scoped yayın ve geri okuma işidir. Tam 19 aday yol yalnız Hermes study + CATALOG HERMES satırıdır. Ham source/SPEC/probe/RESULT/log/DB/arşiv kimlikleri değiştirilmez; current entry dosyalarındaki yayın durumu uzlaştırılır. Araştırma/not/coverage içindeki ilk teslim açıklamaları tarihsel olarak korunur. Content commit/ref/diff ve içerik kimlikleri doğrulanmadan yayın başarılı sayılmaz; güncel sonuç [PUBLICATION](evidence/2026-09-11-cron-scheduling-delivery/PUBLICATION.md) üst bölümündedir.

**Next logical technical work:** Q48/Q46 actual cron gateway drainer/status receipt; ardından Q47 occurrence/rearm ve Q49 run_job/context. **Bu tur yetkilendirilen iş:** U07 yayını ve doğrulaması. Yayın isteği yeni teknik birimi otomatik başlatmaz. Q40/Q42 ve bütün diğer açık doğrulamalar açık kalır; yayın/hash kontrolü yeni davranış deneyi veya bağımsız replication değildir.
