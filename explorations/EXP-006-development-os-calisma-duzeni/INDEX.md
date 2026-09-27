# EXP-006 — Development OS çalışma düzeni

**Tür:** Exploration kökenli, yaşayan DevOS tasarım Work'ü.  
**Açılış:** 25 Eylül 2026.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin rol ve çalışma düzenini ortaya koymak.  
**Current:** [WORK](WORK.md) master plan v1.3. P1 kaynak haritası/runtime açıkları ve P2 ilk rol tabanı korunuyor. **P3 DESIGN HANDOFF READY v0.5 / CANDIDATE / USER EVALUATION.** D021 sorumluluk sınırı accepted; bütün P3, nihai ekip veya çalışan sistem kabulü değil. **P4–P6 başlamadı.**

## Current authority ve tam okuma yolu

AGENT bootstrap ve gerekli kontrollerden sonra:

1. [STATE](STATE.md) — current aşama, sonuç, yetki ve durma noktası.
2. [HANDOFF](HANDOFF.md) — konuşma hafızası olmadan doğru devam.
3. [WORK](WORK.md) — B1–B9/S1 bağı ve P1–P6 master planının tek ana yüzeyi.
4. [DECISIONS](DECISIONS.md) — kullanıcı kısıt/kararları ve D021; aday tasarımdan ayrı.
5. [ACTORS](ACTORS.md) — F1–F8 ve P2 DR01–DR16 ilk isim/lineage registry'si.
6. [U002](sources/U002-cloud-plan-and-autonomy.md) — cloud, iletişim, özerklik, plan ve kısa cevap kaynak mesajları.
7. [P1-01](work/P1-01-claude-cloud-environment-map.md) — kaynaklı Environment imkân/sınırları; actual runtime ve Q açıkları.
8. [P2-01](work/P2-01-named-role-contracts.md) — ilk rol sözleşmeleri; tek başına güncel bütün tasarım değil.
9. [P3-01](work/P3-01-work-information-discussion.md) — G/Y rol profilleri, içerik–düzen sahipliği, bilgi/çalışma alanı, birleşik senaryo ve H1–H6 teknik devir yükleri.

Tam unchanged içerik aynı konuşmada korunabilir. Sonra aktif P sorusunun gerekli Foundation/studies kaynaklarına inilir. P1 ürün hükümleri yük taşıyan teknik seçimde tazelenir. P2 rol adları otomatik actor sayısı/workflow değildir; P3 kaydı kabul edilmiş mimari değildir.

S1 gerekçesi için [S1 master](work/S1-role-responsibility-consolidation.md) ve ilgili slice; kapsam için work/B*.md kullanılır. Tarihsel next/current ifadeleri bu yolu geçersiz kılamaz. P3'e yeni genel audit açılmaz; kullanıcı düzeltmesi veya somut teknik karşı kanıtta hedefli dönüş mümkündür.

## Dosya sorumlulukları

| Yüzey | Tek işi |
|---|---|
| STATE.md | current/next, yetki, sonuç ve durma sınırı |
| HANDOFF.md | yeni oturumun doğru işi devralması |
| WORK.md | önceki B/S1 bağları ve bütün P1–P6 haritası/teslimatları/geri dönüşleri |
| ACTORS.md | ilk aday aile/rol registry'si ve R/M lineage; P3 farklarıyla birlikte okunur |
| DECISIONS.md | kullanıcı kararları ile aday tercihleri ayırmak |
| sources/U001.md | başlangıç kaynağı |
| sources/U002-cloud-plan-and-autonomy.md | master plan/özerklik kaynak mesajları |
| EXP-006_Context | tarihsel yön/metodoloji; current sıra değil |
| work/B*.md | korunmuş ayrıştırma; gerçek SOUL backlog'u değil |
| work/S1-role-responsibility-consolidation.md | S1 yöntem/dilim dizini ve sonraki plan bağı |
| work/S1-*.md | korunmuş nitel analizler ve tarihsel dönüşler |
| work/P1-01-claude-cloud-environment-map.md | P1 kaynak sonucu ve runtime açıkları |
| work/P2-01-named-role-contracts.md | P2 ilk sözleşme/gerekçe tabanı |
| work/P3-01-work-information-discussion.md | current kavramsal iş/bilgi/düzen sözleşmesi, senaryo, kaynak izi ve P4 gereksinim devri |
| history/ | superseded snapshot'lar; normal cold-start'ta okunmaz |

Aşama ayrıntısı mevcut work/ altında plana bağlanır; boş aşama dosyaları veya ayrı paket açılmaz. Current/next STATE/HANDOFF'a, üst plan WORK'e, kabul edilmiş kullanıcı kararı DECISIONS'a gider. Aday P3 farkı ACTORS/P2'ye nihai kadro gibi geçirilmez; P4 bütününü birlikte kullanmalıdır.

EXP-006 DevOS'un kendisi değil onu ortaya koyma çalışmasıdır. Gerçek SOUL işlerini ekip keşfeder/yürütür. Claude cloud kullanıcı kısıtıdır; teknik alt ajan/takım/actor allocation ve fiziksel alan P4'te, actual dosyalar P5'tedir. Rutin tetikleyici olarak kullanıcı gerekmez; sınırsız insan-bağımsızlık istenmez. P3 devre hazır bulunuşu P4'ün bu tur başladığı anlamına gelmez.
