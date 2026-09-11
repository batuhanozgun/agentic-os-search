# Hermes Agent — Araştırma planı

**v0.19 / 2026-09-11 — U06 resume admission/driver source study + bounded local lease execution.** [STATE](STATE.md) work authority, [METHOD](METHOD.md) yöntem. [V0.18 exact plan](https://github.com/batuhanozgun/agentic-os-search/blob/0a475b5d7c50f47689c72cd31f954f5b2303ced6/research/studies/hermes-agent/RESEARCH-PLAN.md) korunur.

## Hedef ve bu revizyonun nedeni

Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest 0.21.0. Önce native mekanizma/sistem modeli, sonra dört-alan ve SOUL/Development OS. Üç merkezi provisional synthesis değişmez; 20/21 bunlarla birlikte okunacak source amendment'lardır. Genel araştırma tamamlanmadı.

V0.18'in actual selector/guard ve startup/adapter consumer soruları kaynak olarak açıldı. U06, DB history projection'ını, holder-write fence'i, startup active-turn promotion/owner check'i, adapter carrier/drain'i ve delivery-redo ayrımını bağladı. Yeni native registry execution **yalnız süreç-içi** kapsamda; actual SessionDB/quiet-next-request/whole-host-restart kontrollerinin yerine geçmedi. Bu yüzden eski messages429 ve 'startup yalnız pointer' durumu current değil, ancak açık validation'ın adı da completed değil.

## U06 gerçek çıktı

[21](notes/21-RESUME-ADMISSION-AND-DRIVER-RECOVERY.md) → [RESEARCH/SOURCES](evidence/2026-09-11-resume-admission/README.md) → [SPEC](evidence/2026-09-11-resume-admission/SPEC.md)/[RESULT](evidence/2026-09-11-resume-admission/RESULT.json). Tam original gateway/turn_lease.py için L01–L07 ve N00–N02. Kimlikler [MANIFEST](evidence/2026-09-11-resume-admission/MANIFEST.json)'te. U04-A/B ve U05 artefaktları yeniden koşulmadı/değiştirilmedi.

Yeni ayrım: gateway process-local lease ≠ durable DB root lease ≠ Kanban run authority. Model-history projection ≠ UI transcript; write-adoption ≠ context reload. Restart computation ≠ hazır yanıtın redelivery'si. Primary heartbeat status ≠ reactivation; set/resume watch kurar. Post-turn complete bir in-flight loop için koşullu telafi, fakat tick-turn/receipt bütünlüğü ayrıca gerekir.

## İlk dar devam: actual admission receipt

**Soru:** startup'ın preclaim ettiği pending slot, adapter'ın hızlı dönüşü/ilk carrier task'ı ve olası drain task'ları arasından gerçek agent admission'a nasıl geçer; startup restore gate neyin bittiğini bekler?

Başlangıç: U06-S03 `_schedule_resume_pending_sessions`/`_run_startup_resume_event` → S06 handle/background/drain → S09 busy/normal dispatch → S07 actual lease/marker/history. Tek normal ve bir deferred/interrupted path için exact event/session/token/history/receipt trace yeterli bounded hedef; bütün platform/crash matrisi hedef değildir. Kaynak full-byte/AST kimliği ve actual consumer yerine test fake'inin kabul üretmemesi gerekir. Sadece yeni bir boolean/test sayısı başarı değildir.

Q40 actual SessionDB + quiet no-wait next-request history trace'i ayrı validation hattıdır. S01/S02 selector/guard okunmuş olmakla bu deney yapılmış sayılmaz. Kaynak materyalizasyonu/dependency sınırı elvermezse explicit NOT RUN korunur; eski küçük adapter'larla kapatılmış gösterilmez. Full ürün kurulumu/provider/model/credential veya environment policy değişimi yoktur.

## Geniş modele dönüş ve erteleme kuralı

[U06 coverage](inventory/RESUME-ADMISSION-COVERAGE-2026-09-11.md), U02 F01–F12 map'ini yeniden değerlendirdi. Dar admission sorusunun ardından **F10 cron/scheduler→run→delivery** ana açıklama boşluğudur: session-bound tekrar ile kalıcı schedule'ın kimlik, admission, persistence, result ve delivery sözleşmeleri karşılaştırılmalı. Araştırma bu tur henüz o yeni birimi başlatmadı.

Bütün Q40–Q46 fault/quality uzayını kapatma ön koşulu konmaz. Dar challenge gerekli kaynak+consumer ile kurulamazsa validation borcu görünür biçimde ertelenebilir; geniş native source araştırması bundan dolayı sonsuza dek durmaz. Aynı L/G/H/K fixture'larını artırmak yerine yeni geçiş okunur. Sonra provider/profile/backend/delegation, diğer UI/install/eval ve learning/ledger/sync/reuse quality tekrar önceliklenir.

## Korunan açık sınırlar

Q07/Q22 final wire/timing/variants, Q26/Q29 full-original/full-worker, Q38 manual K/G parent fidelity, actual migration faults/profile, OS/cancel/external effect, gate/judge quality ve user delivery açık. U06'nın tam küçük modülü bunları otomatik kapatmaz. Daha yeni default-branch restore/acceptance snippet'leri current-version revalidation değildir; primary pin yükseltilmedi.

U04-A/B aynı ID'leri kullanabilen ayrı eski kayıtlardır; 33 B original dosyası ve üç merkezi synthesis korunur. Yeni scope yalnız Hermes package + catalog HERMES row. Güncel main tabanıyla tek scoped content commit, nonforce ref ve exact content/diff readback; sonra yayın receipt'i. Foundation/control/context/diğer studies/Codex/upstream/adoption değişmez.
