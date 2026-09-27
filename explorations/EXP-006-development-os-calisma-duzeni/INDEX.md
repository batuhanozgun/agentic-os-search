# EXP-006 — Development OS çalışma düzeni

**Tür:** Exploration kökenli, yaşayan DevOS tasarım Work'ü.  
**Açılış:** 25 Eylül 2026.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin rol ve çalışma düzenini ortaya koymak.  
**Current:** [WORK](WORK.md) master plan v1.2; P1 kaynak haritası korunuyor, **P2 ilk rol/sözleşme taslağı hazır / CANDIDATE / USER RETURN**. **P3 NEXT / NOT STARTED.** P4–P6 başlamadı; nihai ekip, topoloji veya çalışan sistem kabulü yok.

## Current authority ve tam okuma yolu

AGENT bootstrap ve gerekli kontrollerden sonra:

1. [STATE](STATE.md) — current aşama, sonuç, yetki ve durma noktası.
2. [HANDOFF](HANDOFF.md) — konuşma hafızası olmadan doğru devam.
3. [WORK](WORK.md) — B1–B9/S1 bağı ve P1–P6 master planının tek ana yüzeyi.
4. [DECISIONS](DECISIONS.md) — kullanıcı kısıt/kararları; aday tasarımdan ayrı.
5. [ACTORS](ACTORS.md) — F1–F8 ve P2 DR01–DR16 aday isim/lineage registry'si.
6. [U002](sources/U002-cloud-plan-and-autonomy.md) — cloud, iletişim, özerklik, plan ve kısa cevap kaynak mesajları.
7. [P1-01 Environment haritası](work/P1-01-claude-cloud-environment-map.md) — kaynaklı imkân/sınırlar; actual runtime ve Q açıkları.
8. [P2-01 rol sözleşmeleri](work/P2-01-named-role-contracts.md) — amaç/motivasyon, bilgi, tetik, teslimat/tüketici ve yetki sınırları; P3'e devir.

Tam ve unchanged içerik aynı konuşmada korunabilir. Sonra aktif P aşamasının gerektirdiği Foundation/studies kaynaklarına inilir. P1'in ürün hükümleri yük taşıyan teknik tercihten önce gerektiğinde tazelenir. P2 adları/örnekleri otomatik actor sayısı veya workflow değildir.

S1 gerekçesi için [S1 master](work/S1-role-responsibility-consolidation.md) ve ilgili slice; ayrıntılı geliştirme kapsamı için work/B*.md kullanılır. Tarihsel next/current ifadeleri bu yolu geçersiz kılamaz.

## Dosya sorumlulukları

| Yüzey | Tek işi |
|---|---|
| STATE.md | current/next, yetki, sonuç ve durma sınırı |
| HANDOFF.md | yeni oturumun doğru işi devralması |
| WORK.md | önceki B/S1 bağları ve bütün P1–P6 haritası/teslimatları/geri dönüşleri |
| ACTORS.md | current aday aile, adlandırılmış rol registry'si ve R/M lineage; hazır runtime ekibi değil |
| DECISIONS.md | kullanıcı yönleri ile açık aday tercihleri ayırmak |
| sources/U001.md | başlangıç kaynağı |
| sources/U002-cloud-plan-and-autonomy.md | master plan ve özerklik açıklamalarının kaynak aktarımı |
| EXP-006_Context | tarihsel yön/metodoloji; current sıra değil |
| work/B*.md | korunmuş ayrıştırma; gerçek SOUL backlog'u değil |
| work/S1-role-responsibility-consolidation.md | S1 yöntem/dilim dizini ve sonraki plan bağı |
| work/S1-*.md | korunmuş nitel analizler ve tarihsel dönüşler |
| work/P1-01-claude-cloud-environment-map.md | P1 kaynak sonucu ve runtime açıkları |
| work/P2-01-named-role-contracts.md | P2 aday sözleşmeler, gerekçe, uzmanlık/ayrım ve devir |
| history/ | superseded snapshot'lar; normal cold-start'ta okunmaz |

Aşama ayrıntısı mevcut work/ altında plana bağlanır. Boş aşama dosyaları veya ayrı çalışma paketi açılmaz. Foundation/studies rotaları WORK §5'tedir.

## Güncelleme ve kapsam

Current/next STATE + HANDOFF'a; plan/bağımlılık WORK'e; rol anlamı ACTORS ve ilgili sözleşmeye; gerçek kullanıcı kararı DECISIONS'a gider. Tarihsel analiz yeni görüşe uydurularak yeniden yazılmaz.

EXP-006 DevOS'un kendisi değil, onu ortaya koyma çalışmasının kalıcı sistemidir. Gerçek SOUL işlerini kurulacak ekip keşfeder/yürütür. Claude cloud kullanıcı kısıtıdır; teknik alt ajan/takım ve allocation seçimi P4'te, actual dosyalar P5'tedir. Rutin rol geçişlerinde kullanıcı tetiklemesi gerekmemesi istenir; sınırsız insan-bağımsızlık istenmez.
