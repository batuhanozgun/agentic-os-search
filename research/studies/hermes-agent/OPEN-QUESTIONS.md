# Hermes Agent — Açık sorular

**2026-09-07 / active.** Sorular keşif ve continuation kaydıdır; doğrulanmış kusur listesi değildir. Kaynak ID'leri [defterdedir](SOURCE-LEDGER.md).

| ID | Açık ayrım | Sonraki en yüksek değerli kaynak/karşı sınama |
|---|---|---|
| Q01 | Review ne zaman tetiklenir; manual refine, otomatik nudge ve farklı API yolları aynı mı? | `run_agent.py` forwarding → `agent/turn_facade.py`/loop ve ilgili çağıranlar; sadece dokümanın 'after turn' anlatımı yeterli değil. |
| Q02 | Kurulan whitelist bütün ilgili gerçek dispatch yollarında mı uygulanıyor? | `hermes_cli/plugins.py`, actual invoke-tool/worker/context propagation; H09'un mock assertion'ının ötesine geç. |
| Q03 | Okuma/approve/yazma arasında skill değişince hangi içerik esas alınır? | H05/H07/H08 → `tools/skill_manager_tool.py`, apply/locking/matching, ledger ve negatif testler. |
| Q04 | Pending record disk hatasında döndürülürse gerçek kullanıcı yüzeyi ne söyler; kayıp işlem yeniden bulunabilir mi? | H07 stage failure → callers, status/commands, hata senaryosu. Bu tur arıza koşusu yapılmadı. |
| Q05 | Background origin staging/replay sırasında korunur mu; insan onayı sahiplik kuralını hangi kapsamda değiştirir? | skill/memory mutator, `apply_skill_pending` / `apply_memory_pending`, H06 origin binding ve testler. |
| Q06 | Paylaşılan memory store ve profile context; cancellation deadline sonrası eski worker yazıları nasıl düzenlenir? | H04/H12 → gerçek store kilitleri, caller context-copy, lifecycle/test yolları. |
| Q07 | Sonraki oturum güncellemeyi gerçekten hangi yolla kullanır? | prompt-builder, MemoryStore/session load, skill discovery/view, frozen snapshot ve live/tool görünümü. |
| Q08 | Farklı-model digest önemli tool kanıtını düşürdüğünde dersin doğruluğu nasıl sınanır? | H04 `_digest_history` + varsa eval/trajectory/dataset, farklı görünüm karşılaştırması. Kalite eşdeğerliği varsayılmayacak. |
| Q09 | Curator birleştirme/silme/rollback hangi semantik bilgiyi korur? | skill_usage/ledger, curator ve skills_sync ailesi; `absorbed_into` tek başına yeterli oracle değil. |
| Q10 | README session-search özetleme iddiası ile bellek rehberi raw-message anlatımı nasıl uzlaştırılır? | Actual session-search implementation/schema/tests ve gerekirse değişiklik tarihi. |
| Q11 | Terminal sandbox, bütün proses, adapter yetkisi ve session/profile ayrımı hangi kipte geçerli? | H13 → runtime/backend/plugin/gateway/UI kod ve testleri; politika compliance'ı henüz kurulmadı. |
| Q12 | Bilinen büyük kaynak bölgelerinden hangileri yeni birinci-derece mekanizma getirecek? | apps/web/native/cron/provider/compat/eval alt envanteri. İlk F01–F12 planını gerekirse yeniden ayrıştır. |

## Yeniden açma ve kapatma

Bir sorunun cevaplanması, source/symbol/ref ve kanıt statüsüyle ilgili notta gösterilir; tablo yalnız o nota yönlendirir. Kaynak henüz okunmadığı için açık olan soru, gerçek ürün yetersizliği diye etiketlenmez. Deney gerektiren iddia statik kodla kapanmaz. Bu soruların bir kısmı yeterli kaynak incelemesi sonrası çalışma amacı için kapsam dışı bırakılabilir; gerekçesi kaybolmaz.

U01'in eksikleri tamamlanmadan genel 'self-improvement verified' veya 'self-improvement absent' sonucu üretilmez.
