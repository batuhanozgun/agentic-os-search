# Hermes Agent — STATE

**2026-09-13 / U12 / plan v0.25 — TOOL ADMISSION AND DELEGATION LIFECYCLE.**
**Statü:** ACTIVE PARTIAL RESEARCH; HERMES bütünü tamamlanmadı. Q54 ordinary tool/child kaynak zinciri ilerledi; detached parent yeniden-kabulü ve gerçek runtime/quality doğrulamaları açık.
**Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest0.21.0; current release/kurulu binary değildir.
**Güncel yayın hükmü:** [U12 PUBLICATION](evidence/2026-09-13-tool-delegation/PUBLICATION.md). STATE başlığı tek başına main/ref/content doğrulaması değildir. [PLAN](RESEARCH-PLAN.md), [METHOD](METHOD.md), [INDEX](INDEX.md), [META](META.md).

## Amaç, yetki ve incremental ilerleme

Kullanıcının “Sıradaki adımına geçebilirsin. Operasyonel sınırına kadar çalış lüten.” talebiyle kayıtlı Q54 sürdürüldü. Amaç önce HERMES-native mekanizmalar/ilişkiler, sonra CORE ve ayrı daha-geç dört-alan/SOUL/Development OS aday değerlendirmesidir. Araştırma benimseme veya implementation yetkisi değildir.

Yalnız `research/studies/hermes-agent/**` ve CATALOG HERMES satırı değişebilir. Foundation, context/Codex, agent-control, diğer studies, upstream, architecture/adoption, izin ve credential ayarları değişmez. Full ürün, gerçek model/provider/NAS/native backend çalıştırması yok; otomatik/background devam yoktur.

Başlangıç main ead0d6775bd49808afbf496292f526cae1fb20df. U11 sonrası Foundation/harness değişiklikleri compare ile ayrıldı; HERMES/control değişmemişti. Q54 başlangıç planı **0fd4b597002eb478cd1ed913a588ba44fe70edb3** main/ref/tam plan/tek-path compare ile doğrulandı; sonra A araştırıldı. Arada gelen **bc99f6e9661bcbbaba9fb2db7332ebad16756775** ayrı harness çalışması/katalog satırını ilerletti; bu çalışma korunur, HERMES'e atfedilmez.

**U12-A ef51c3f4b1d4d94038a428fa9bac1a21dfda778f** main'e yazıldı; actual ref, A araştırmasının/kaynaklarının ve STATE'in tam içerikleri geri okunduktan sonra B başladı. B'nin gerçek içerik/ref/scope sonucu PUBLICATION'dadır. Tarihsel A/B prepared ifadeleri, üst yayın makbuzu tamamlanmışsa yeniden yapılacak iş sayılmaz.

**Kayıt kapısı devam eder:** bir anlamlı kaynak/kanıt/sınır/sonraki soru dilimi main'e bağlanıp doğrulanmadan ikinci büyük dilim biriktirilmez. Yazma kesilirse mevcut dilimin yayını çözülür. Küçük metin yayını gelecekteki her yazmanın veya binary aktarımın garantisi değildir.

## U12'de gerçekten ilerleyen

[Note27](notes/27-TOOL-ADMISSION-AND-DELEGATION.md) → [A: araç kabulü](evidence/2026-09-13-tool-delegation/TOOL-ADMISSION.md) + [B: delegation yaşam döngüsü](evidence/2026-09-13-tool-delegation/DELEGATION-LIFECYCLE.md). [A kaynakları S01–S07](evidence/2026-09-13-tool-delegation/TOOL-SOURCES.md), [B kaynakları S08–S15](evidence/2026-09-13-tool-delegation/DELEGATION-SOURCES.md) gerçek full/selected okuma kapsamlarını taşır.

A: discovery/schema/availability → session-scoped isim/bridge kabulü → pre-effect proposal flush → middleware sonrası son-argüman policy → batch/executor → read_file handler → result/persistence/visibility. Callback once, timeout ve tamamlanma etiketi evrensel exactly-once, rollback veya physical-stop makbuzu değildir. Batch rezervasyonu ile sonraki argüman rewrite kompozisyonu ayrıca açıktır.

B: config/depth-derived rol ve bütçe; yeni child conversation, goal/context/prefill, parent tool restrictions ve role-granted delegation; pinned runtime/capability/pool; task-cwd/container alias ve koşullu worktree; child-owned DB release; sync vs detached group/unit/slot; origin/parent lineage/exact UI control; summary/status/schema/steering; timeout/deferred close; async dispatch/terminal/ledger/recovery/claim/ack. Fresh conversation tam OS izolasyonu değildir; completed yanında budget-truncated bulunabilir; summary budget memory/hook'tan önce uygulanır.

**Yeni behavioral execution: YOK.** HERMES modülleri import edilmedi; gerçek tool/file operation, child, SessionDB/SQLite, model/provider/credential, native süreç veya upstream suite koşulmadı. RESULT veya PASS sayısı yoktur. Tam kaynak okumaları local-byte/dependency/runtime doğrulaması değildir. DB acquire caller'ı fiziksel ayrı connection; schema_valid görev doğruluğu; queue.put parent tüketimi sayılmadı. [NOT RUN](evidence/2026-09-13-tool-delegation/CHECKS-NOT-RUN.md).

## İlk sonraki dar kaynak birimi — Q57

**Async-delegation completion → gerçek host drain → current ownership/claim/ack → parent turn admission/context.** `tools/async_delegation.py::_push_completion_event`, `claim_event_delivery`, `complete_event_delivery`, `restore_undelivered_completions` gerçek tüketicilerinden başlanır. En az bir normal consumer ve materially farklı restored/expired/interim-notice yolu izlenir. CLI/gateway/API yolları aynı sayılmaz; bütün platformlar otomatik kapsam değildir.

Gerekçe: U12 sync parent tool-result dönüşünü ve detached producer/ledger/queue'yu açtı; actual parent kabulü hâlâ arada yük taşıyan boşluk. Q57 bu açık oku bağlar, bütün reliability fault uzayını tüketme kampanyası değildir. İlk anlamlı consumer dilimi yayımlandıktan sonra kapsam haritasına dönülüp learning/skill-ledger/sync/quality ile UI/install/update/eval aileleri yeniden önceliklendirilir. Geniş alanlar kaybolmaz; yakın teknik ayrıntının araştırmayı tek başına yönetmesine izin verilmez.

Q54 source-advanced; policy rewrite/path reservation, actual child authority/context, summary/correction kalite/bütçe, kapasite fallback/cancel ve fiziksel kaynak kapanışı residual'dır. Q55 native model/system/history/restart ve Q56 native terminal/persistence/control ayrıca açık. Güçlü reliability/adoption reuse veya yeni karşı kanıt doğarsa exact ilgili doğrulama yeniden açılır; yalnız sonraya bırakmak kapanış değildir.

## Korunan araştırma ve doğrulama sınırları

U11 [note26](notes/26-RUNTIME-BACKEND-AND-CONTROL-OWNERSHIP.md), [A](evidence/2026-09-12-runtime-backend/RESEARCH.md), [B](evidence/2026-09-12-runtime-backend/BACKEND-OWNERSHIP.md), iki kaynak defteri ve [PUBLICATION](evidence/2026-09-12-runtime-backend/PUBLICATION.md) değişmez. Makbuz6a9a8c48204102d592780971a212b363ec97bc98. U10 [note25](notes/25-CRON-EXECUTION-AND-CONTEXT.md) ve [kanıtları](evidence/2026-09-12-cron-execution-context/README.md) kendi source/selector sınırında korunur. Eski yayınlar bekleyen ZIP veya yeniden deney işi değildir.

U04-A/18 ve U04-B/19 eş numaralarda aynı vakalar değildir. B'nin33 original subtree'si **d01c92f7414713300934be3bb4e3d40ac57631b3**, [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. METHOD, notes01–26, U04–U11 bütün evidence ve synthesis01–04 değişmez; U12-A'nın iki özgün metni de B sırasında değiştirilmez. Dört provisional sentez dört Foundation alanının bittiği anlamına gelmez.

Q40 actual DB/quiet history, Q42 startup admission, Q47 late callback/NAS/clock, Q48/Q50 transport/status/cancel; Q41/Q43/Q44/Q45 ve Q07/Q22/Q26/Q29/Q38 fidelity/quality; U10 Q49 full run_job, Q51 selector→request/quality ve Q52 detection→handling açık. Eski G/H/L/D/B/C vaka sayıları birleştirilmez; yeni source-only çalışma onları yeniden sınamadı.

## Cold-start ve retrieval

1. Current main AGENT/tetiklenen protokoller → research root/studies catalog → META/STATE/INDEX → METHOD/PLAN. U12 PUBLICATION üstü güncel yayın hükmüdür. Başlangıç ve A'nın tamamlanmış kapılarını yeni iş sayma.
2. Note27 + A TOOL-ADMISSION/TOOL-SOURCES + B DELEGATION-LIFECYCLE/DELEGATION-SOURCES + NOT RUN tam okunur. U12'de runtime RESULT veya raw test arşivi yoktur. Source ile uygulama davranışı karıştırılmaz.
3. U11 note26/A/B/kaynaklar/NOT RUN; synthesis02 ordinary-loop ve synthesis04 scheduled-work birlikte okunur. U10 note25/SOURCES/RESEARCH/NOT RUN yolu korunur; exact C hükmü için SPEC+tam RESULT+MANIFEST+raw source/probe/input/output/log gerekir.
4. U04 zorunlu ayrımı note19+B README/RECONCILIATION/manifest; synthesis03+A SOURCES/RESEARCH/CONTINUITY-COVERAGE üzerinden geri kazanılır. Genel memory/turn için synthesis01/02 ve U05/U06/U07 rotaları gerekli derinlikte izlenir. Aynı-conversation full reads değişmeyen source için reuse olabilir, yeni bağımsız kanıt değildir.
5. [Exact U11 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/6a9a8c48204102d592780971a212b363ec97bc98/research/studies/hermes-agent/STATE.md) → eski U10/başlangıç zinciri; [U12-A STATE](https://github.com/batuhanozgun/agentic-os-search/blob/ef51c3f4b1d4d94038a428fa9bac1a21dfda778f/research/studies/hermes-agent/STATE.md) tarihsel yetki/epistemik sınırları korur. MAP/catalog derived yönlendirmedir, raw veya bu STATE'in yerine geçmez.
