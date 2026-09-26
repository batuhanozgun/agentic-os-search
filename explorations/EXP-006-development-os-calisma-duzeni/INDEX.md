# EXP-006 — Development OS çalışma düzeni

**Tür:** Exploration kökenli, yaşayan DevOS tasarım Work'ü.  
**Açılış:** 25 Eylül 2026.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin rol ve çalışma düzenini ortaya koymak.  
**Current:** Master plan v1.0 mevcut [WORK](WORK.md)'te; **P1 sırada / NOT STARTED**. Claude araştırması ve kurulum henüz başlamadı. S1 aday konsolidasyonu korunuyor; nihai mimari/ekip kabulü yok.

## Current authority ve tam okuma yolu

AGENT bootstrap ve gerekli kontrollerden sonra yeni oturumda:

1. [STATE](STATE.md) — güncel aşama, sonuç, yetki ve durma noktası.
2. [HANDOFF](HANDOFF.md) — son konuşmayı bilmeden doğru devam.
3. [WORK](WORK.md) — B1–B9/S1 bağları ve P1–P6 **master planının tek ana yüzeyi**.
4. [DECISIONS](DECISIONS.md) — kullanıcıyla netleşen kısıt/kararlar; aday tercihlerden ayrı.
5. [ACTORS](ACTORS.md) — aday aile/sorumluluk/uzmanlık ve R/M lineage.
6. [U002](sources/U002-cloud-plan-and-autonomy.md) — cloud, iletişim, özerklik, plan ve kısa cevap hakkındaki üç görünür kullanıcı mesajı.

Bu altı dosya tam okunur. Aynı konuşmada tam ve unchanged içerik varsa tekrar yüklenmez. Sonra yalnız aktif P aşamasının gerektirdiği kaynak derinliğine inilir.

S1 kararının gerekçesi için [S1 master](work/S1-role-responsibility-consolidation.md) ve ilgili slice; sorumluluk ayrıntısı için work/B*.md kullanılır. S1/B dosyalarındaki eski “next/current” ifadeleri yukarıdaki yolu geçersiz kılamaz.

## Dosya sorumlulukları

| Yüzey | Tek işi |
|---|---|
| STATE.md | current/next, yetki, sonuç ve durma sınırı |
| HANDOFF.md | yeni oturumun doğru işi devralması |
| WORK.md | eski B1–B9/S1 bağları + bütün P1–P6 haritası, teslimatlar ve geri dönüşler |
| ACTORS.md | aday aktör/aile/uzmanlık/mekanik sorumluluk registry'si; hazır ajan ekibi değil |
| DECISIONS.md | kabul edilmiş kullanıcı yönleri/kısıtları ile açık tercihleri ayırmak |
| sources/U001.md | başlangıç kullanıcı kaynağı |
| sources/U002-cloud-plan-and-autonomy.md | son master plan ve özerklik açıklamalarının kaynak aktarımı |
| EXP-006_Context | tarihsel yön/metodoloji bağlamı; current sıra değil |
| work/B*.md | korunmuş B alanı ayrıştırmaları; sıralı SOUL backlog'u değil |
| work/S1-role-responsibility-consolidation.md | S1 yöntem/dilim dizini ve sonraki plana bağlantı |
| work/S1-*.md | korunmuş nitel analizler ve eski tur dönüşleri |
| history/ | superseded snapshot'lar; normal cold-start'ta okunmaz |

P aşamaları açıldıkça gereken ayrıntı mevcut work/ altında plana bağlı tutulur; şimdi boş dosya veya yeni çalışma paketi oluşturulmadı. Foundation/studies kaynak rotaları WORK §5'tedir.

## Güncelleme ve kapsam

Current/next değişirse STATE + HANDOFF; plan/bağımlılık değişirse WORK; rol modeli değişirse ACTORS; gerçek kullanıcı kararı değişirse DECISIONS güncellenir. Kaynak aktarımı yorum yerine geçmez; tarihsel analizler yeni görüşe uydurularak yeniden yazılmaz.

Bu paket DevOS'un kendisi değil, DevOS'u ortaya koyma çalışmasının kalıcı sistemidir. Gerçek SOUL işlerini kurulacak DevOS ekibi keşfeder/yürütür. Claude cloud kullanıcı kısıtıdır; alt ajan/takım, iletişim, rol dosyaları ve ajan sayısı henüz seçilmedi. Rutin rol geçişlerinde kullanıcı tetiklemesi gerekmemesi istenir; sınırsız insan-bağımsızlık istenmez.
