# Hermes Agent — Açık sorular

**2026-09-07 / active, plan v0.3.** Sorular keşif ve continuation kaydıdır; doğrulanmış kusur listesi değildir. Kaynak ID'leri [defterdedir](SOURCE-LEDGER.md).

| ID | Açık ayrım | Sonraki en yüksek değerli kaynak/karşı sınama |
|---|---|---|
| Q01 | Review ne zaman tetiklenir; manual refine, otomatik nudge ve farklı API yolları aynı mı? | `run_agent.py` forwarding → `agent/turn_facade.py`/loop ve ilgili çağıranlar; sadece dokümanın 'after turn' anlatımı yeterli değil. |
| Q02 | Kurulan whitelist bütün ilgili gerçek dispatch yollarında mı uygulanıyor? | `hermes_cli/plugins.py`, actual invoke-tool/worker/context propagation; H09'un mock assertion'ının ötesine geç. |
| Q03 | Okuma/approve/yazma arasında skill değişince hangi içerik esas alınır? | H05/H07/H08 → H22'nin eksik 201–800 aralığı, apply/locking/matching, ledger ve negatif testler. |
| Q04 | Pending record disk hatasında döndürülürse gerçek kullanıcı yüzeyi ne söyler; kayıp işlem yeniden bulunabilir mi? | H07 stage failure → callers, status/commands, hata senaryosu. Arıza koşusu yapılmadı. |
| Q05 | Background origin staging/replay sırasında korunur mu; insan onayı sahiplik kuralını hangi kapsamda değiştirir? | skill/memory mutator, `apply_skill_pending` / `apply_memory_pending`, H06 origin binding ve testler. |
| Q06 | Paylaşılan memory store ve profile context; cancellation deadline sonrası eski worker yazıları nasıl düzenlenir? | H04/H12 → gerçek store kilitleri, caller context-copy, lifecycle/test yolları. |
| Q07 | Sonraki oturum güncellemeyi gerçekten hangi yolla kullanır? | prompt-builder, MemoryStore/session load, skill discovery/view, frozen snapshot ve live/tool görünümü. |
| Q08 | Farklı-model digest önemli tool kanıtını düşürdüğünde dersin doğruluğu nasıl sınanır? | H04 `_digest_history` + varsa eval/trajectory/dataset, farklı görünüm karşılaştırması. Kalite eşdeğerliği varsayılmayacak. |
| Q09 | Curator birleştirme/rollback hangi semantik bilgiyi korur? | [03-SKILL-CURATION](notes/03-SKILL-CURATION.md) §§6–7: isim/beyan sınıflandırması ve best-effort kayıtlar okundu. H18/H19 → ledger/backup/sync ve actual mutator. `absorbed_into` varlığı yeterli semantik oracle değil. |
| Q10 | README session-search özetleme iddiası ile bellek rehberi raw-message anlatımı nasıl uzlaştırılır? | Actual session-search implementation/schema/tests ve gerekirse değişiklik tarihi. |
| Q11 | Terminal sandbox, bütün proses, adapter yetkisi ve session/profile ayrımı hangi kipte geçerli? | H13 → runtime/backend/plugin/gateway/UI kod ve testleri; politika compliance'ı henüz kurulmadı. |
| Q12 | Bilinen büyük kaynak bölgelerinden hangileri yeni birinci-derece mekanizma getirecek? | apps/web/native/cron/provider/compat/eval alt envanteri. İlk F01–F12 planını gerekirse yeniden ayrıştır. |
| Q13 | Boş aday kümesinin curator skip koşulu gerçek çağrı/test yolunda neye yol açıyor? | H18'de dönen ve aranan metinler eşleşmiyor; consolidation-on yoluna özel statik gözlem. Mevcut testin kalan bölümü ve uygun kontrollü karşı örnek; varsayılan-off ile karıştırma. |
| Q14 | Curator prompt'undaki bundled/prune/dry-run talimatı actual guard ve dispatch ile hangi kapsamda uyuşuyor? | H16–H20/H05 → H22 orta bölüm ve batch; otomatik bakım ile LLM mutasyonu ayrı. Bir prompt banner'ını mekanik yazma yasağı diye kapatma. |
| Q15 | Backup veya report/cron-reference yazımı başarısızsa hangi durumlar ayrışıyor? | H18 `_write_run_report`/`_rewrite_cron_refs`, H19 `_relocate` → gerçek backup/ledger/cron/restart ve hata senaryoları. Kaynak dalı canlı olay değildir. |
| Q16 | Batch `operations` biçimi ve kesilmiş tool arguments, curator raporunun sınıflandırmasına ne taşıyor? | H22 schema + H18 `_skill_manage_args`/400-char kesiti → batch/tool-session trace ve ledger; normalizasyonun başka yerde yapılıp yapılmadığını doğrula. |

## Yeniden açma ve kapatma

Bir sorunun cevaplanması, source/symbol/ref ve kanıt statüsüyle ilgili notta gösterilir; tablo yalnız o nota yönlendirir. Kaynak henüz okunmadığı için açık olan soru, gerçek ürün yetersizliği diye etiketlenmez. Deney gerektiren iddia statik kodla kapanmaz. Bu soruların bir kısmı yeterli kaynak incelemesi sonrası çalışma amacı için kapsam dışı bırakılabilir; gerekçesi kaybolmaz.

U01 ve bağlantılı bakım/gelecek-kullanım eksikleri tamamlanmadan genel 'self-improvement verified' veya 'self-improvement absent' sonucu üretilmez. Q13 bir kaynak koşulu uyuşmazlığı; prompt'taki işlem sayısının kaliteye etkisi ise ayrı hipotezdir; aynı kesinlikte sunulmaz.
