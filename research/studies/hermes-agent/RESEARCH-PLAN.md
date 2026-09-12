# Hermes Agent — Araştırma planı

**v0.24 / 2026-09-13 — U11 yayımlı; Q54 başlangıç checkpoint'i.** [STATE](STATE.md) yetki/current work, [METHOD](METHOD.md) yöntem, [MAP](CURRENT-RESEARCH-MAP.md) büyük resim, [PUBLICATION](evidence/2026-09-12-runtime-backend/PUBLICATION.md) tamamlanmış U11 yayını. Primary c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a / manifest 0.21.0; current ürün hükmü değil.

## Q54 başlangıç — 2026-09-13

Kullanıcı “Sıradaki adımına geçebilirsin. Operasyonel sınırına kadar çalış lüten.” talebiyle kayıtlı Q54'ü sürdürmeyi yetkilendirdi. Başlangıç main ead0d6775bd49808afbf496292f526cae1fb20df. U11 makbuzu 6a9a8c48204102d592780971a212b363ec97bc98 sonrasındaki dört commit yalnız Foundation ve ayrı harness çalışmasını/katalog girişini ilerletmiş; HERMES ve agent-control değişmemiştir. Bunlar korunur. AGENT ve R01–R09 güncel canonical metinleri bu tur tam okundu. U11'in aynı-conversation tam kaynak okumaları, değişmeyen path'ler için yeniden kullanılır; U04-A/B ayrımı ayrıca yeniden geri kazanıldı.

Bu başlangıç kaydı yeni teknik bulgu veya deney değildir. Gerçek main/ref ve bu plan geri okunmadan yeni geniş kaynak dilimi başlatılmaz. İlk dilim Q54-A: tool visibility/registration/policy → ordinary dispatch → effect/result/persistence sınırı. Ardından yalnız A yayımlanıp geri okunduğunda Q54-B: delegation admission → child context/authority → result return/cancel/cleanup. Gerekirse B daha küçük doğal sınırlara bölünür; yayımlanmamış büyük dilim biriktirilmez. Beklenmeyen erişim engeli araştırma bulgusu sayılmaz.

## Yapılan ve revizyon gerekçesi

Kullanıcının onayladığı incremental düzen U11'de uygulandı: başlangıç kaydı d3a4baeeb7afd97d38588c674c4842f01e87c6f0 main'den geri okundu; Q53-A e562de82ab4ea33872e55d501c8b59f26b441fa8 yayımlanıp geri okundu; sonra B araştırıldı. A seçim→runtime→init→gerçek dispatch; B ordinary model transportu ile native whole-turn backend'de history/tools/fallback/cancel/cleanup ve makbuz sahipliğidir. [Note26](notes/26-RUNTIME-BACKEND-AND-CONTROL-OWNERSHIP.md) iki dilimi birleştirir. A/B metinleri ve yayın makbuzu değişmez.

Q53'ün bounded source çıkış ölçütü ilerledi: kimin model isteği, araç, history/compaction, fallback ve kaynak ömrünü yönettiği gerçek caller'larla açıklanabilir. Bütün runtime/config/ilk request veya restart doğrulaması tamamlanmadı. Native factory'de HERMES model/system/history alanlarının açık RPC bağı yokluğu, projection ile authoritative thread farkı ve terminal/persistence etiketleri yeni ayırıcı kontroller doğurdu. U11'de yeni behavioral execution yapılmadı.

Synthesis02 ordinary-loop ve synthesis04 scheduled-work korunur. U11 onlara ek source amendment'ıdır; final CORE veya beşinci completed model değildir. Araştırma yalnız yeni hata aramak değil, alternatif yürütme sahipliğini native açıklamaya katmaktır.

## Aktif geniş kaynak birimi — Q54

**Soru:** HERMES ordinary tool/delegation kabulü, parent/child yetkisini ve bağlamını hangi gerçek mekanizmalarla kuruyor; sonuç, interrupt ve cleanup kime dönüyor?

Başlangıç `run_agent.py::_execute_tool_calls/_dispatch_delegate_task` → `agent/tool_executor.py` ve policy/helper consumer'ları → `tools/delegate_tool.py` gerçek dispatch/child/return yolları. Şema/metadata ile gerçek registration, izin verilen araçlar ile çalıştırma hakkı, parent_agent bağı ile child runtime, background handle ile sonuç kabulü ayrı tutulmalı. Native `hermes_tools_mcp_server.py` stateless yüzeyi karşı sınırdır; bütün Codex plugin/platform katalogları araştırmanın otomatik kapsamı değildir.

Çıkış: en az bir ordinary araç ve bir delegation zincirinde yetki/bağlam/kimlik/return/cleanup sahipleri, source-versus-runtime sınırıyla açıklanabilmeli. Constructor veya fake başarılı sonucu gerçek child kabulü sayma. Full product/model/credential veya upstream değişikliği yoktur.

## Incremental kayıt ve yayın kapısı

Yeni büyük dilimden önce current main/STATE ve kaynak yeterliliği doğrulanır. Her anlamlı dilimde bulgu + kaynak + sınır + sonraki soru birlikte kalıcılaştırılır. Yayımlanmamış bir büyük dilim varken ikincisini biriktirme. Ref/content/scope geri okuması olmadan “kaydedildi” hükmü verme. Yazma kesilirse mevcut dilimin devrini çöz; yeni kapsam açma. Bu çalışma düzeni agent-control mutation değildir.

## Ayrı residual doğrulamalar

Q53 fallback geçiş ortası ve gerçek primary restore; **Q55** native model/system/history binding, fresh/reused/restart ve projection/compaction karşılaştırması; **Q56** terminal event/final text, flush/agent_persisted ve interrupt/process-effect makbuzları. [U11 NOT RUN](evidence/2026-09-12-runtime-backend/CHECKS-NOT-RUN.md). Source branch'i ampirik yanlış-model/data-loss/duplicate kanıtı değildir.

U10 Q49 full accepted→run_job→script/agent/first-request; Q51 selector→request/quality; Q52 detection checkpoint→successful handling. Q47 late-callback/NAS/store/clock, Q48/Q50 transport/status/cancel/seeding, Q40/Q42 actual DB/quiet-history/startup kabulü; Q41/Q43/Q44/Q45/Q07/Q22/Q26/Q29/Q38 önceki sınırları korur. Full source/bağımlılık erişimi, yeni karşı kanıt veya güçlü reliability/adoption reuse gerektirdiğinde ilgili ölçüm açılır. Bütün fault matrisini bitirmek geniş kaynak araştırmasının ön koşulu değildir.

## Geniş yön ve yetki

Native mekanizmalar → alt-sistemler → ilişkiler → çekirdek açıklama → ayrı daha-geç dört-alan/SOUL/Development OS değerlendirmesi. Learning/skill-ledger/sync/quality, alternatif UI/install/update/eval ve diğer backend aileleri kaybolmaz; Q54 sonrası kapsam dengesi yeniden değerlendirilir. Dosya/test sayısı başarı ölçütü değildir.

Yalnız Hermes package + CATALOG Hermes satırı. METHOD, notes01–26, U04–U11 evidence/yayınları ve synthesis01–04 değişmez. Foundation/control/context/Codex/upstream/diğer studies/architecture/adoption ve izin ayarı değişmez. [Exact U11 planı](https://github.com/batuhanozgun/agentic-os-search/blob/6a9a8c48204102d592780971a212b363ec97bc98/research/studies/hermes-agent/RESEARCH-PLAN.md) ve U10 plan zinciri korunur.
