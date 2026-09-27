# EXP-006 — Development OS çalışma düzeni

**Tür:** Exploration kökenli, yaşayan DevOS tasarım Work'ü.  
**Açılış:** 25 Eylül 2026.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin rol ve çalışma düzenini ortaya koymak.  
**Current:** [WORK](WORK.md) master plan v1.4. P1 kaynak/runtime sınırları, P2 rol tabanı ve P3 v0.5 kavramsal devir korunur. **P4 INITIAL TECHNICAL BASELINE / CONDITIONAL DESIGN / NOT DEPLOYED.** Ana Y oturumu + özel alt ajanlar, fiziksel alan ve kontrollü yayın başlangıç tercihidir; hedefte yeterlik veya kullanıcı mimari kabulü değildir. **P4 açık; P5/P6 başlamadı.**

## Current authority ve tam okuma yolu

AGENT bootstrap ve gereken kontrollerden sonra:

1. [STATE](STATE.md) — current aşama, yetki, sonuç ve gerçek açıklar.
2. [HANDOFF](HANDOFF.md) — konuşma hafızası olmadan doğru devam.
3. [WORK](WORK.md) — B1–B9/S1 bağı ve P1–P6 master planının tek ana yüzeyi.
4. [DECISIONS](DECISIONS.md) — kullanıcı kısıt/kararları; D021 sınırı ve D022 P4 devam yetkisi.
5. [ACTORS](ACTORS.md) — F1–F8 ve P2 DR01–DR16 ilk registry.
6. [U002](sources/U002-cloud-plan-and-autonomy.md) — cloud, iletişim, özerklik, plan ve kısa cevap kaynak mesajları.
7. [P1-01](work/P1-01-claude-cloud-environment-map.md) — ilk Environment haritası ve Q açıkları; güncel seçim tazelemesi P4'tedir.
8. [P2-01](work/P2-01-named-role-contracts.md) — ilk rol sözleşmeleri; tek başına son runtime kadrosu değil.
9. [P3-01](work/P3-01-work-information-discussion.md) — G/Y, içerik–düzen, çalışma/devir kuralları ve H1–H6.
10. [P4-01](work/P4-01-cloud-runtime-and-workspace-design.md) — güncel koşullu teknik tercih, rol allocation, fiziksel yerleşim, çağrı/yayın ve kapanmamış hedef kanıtı.

Tam unchanged içerik aynı konuşmada korunabilir. Sonra aktif P sorusunun gerekli Foundation/studies veya birincil teknik kaynağına inilir. P1'in kaynak bilgisi actual hedef yeterliği sayılmaz. P3 kavramsal devre hazırdır, tüm ayrıntıları kullanıcıca kabul edilmiş değildir. P4 tercihi koşullarıyla okunur; P5 kurulumu gibi devralınmaz.

S1 gerekçesi için [S1 master](work/S1-role-responsibility-consolidation.md) ve ilgili slice; iş kapsamı için work/B*.md kullanılır. Tarihsel next/current/not-started checkpoint'leri bu yolu geçersiz kılamaz. Hedefli somut sorun yoksa yeni genel P3 audit'i açılmaz.

## Dosya sorumlulukları

| Yüzey | Tek işi |
|---|---|
| STATE.md | current/next, yetki, sonuç ve durma sınırı |
| HANDOFF.md | yeni oturumun doğru işi devralması |
| WORK.md | önceki B/S1 bağları ve bütün P1–P6 haritası/teslimatları/geri dönüşleri |
| ACTORS.md | ilk aile/rol registry ve R/M lineage; P3/P4 farklarıyla birlikte okunur |
| DECISIONS.md | kullanıcı kararları ile assistant'ın teknik tercihlerini ayırmak |
| sources/U001.md | başlangıç kaynağı |
| sources/U002-cloud-plan-and-autonomy.md | master plan/özerklik kaynak mesajları |
| EXP-006_Context | tarihsel yön/metodoloji; current sıra değil |
| work/B*.md | korunmuş ayrıştırma; gerçek SOUL backlog'u değil |
| work/S1-role-responsibility-consolidation.md | S1 yöntem/dilim dizini |
| work/S1-*.md | nitel analizler ve tarihsel dönüşler |
| work/P1-01-claude-cloud-environment-map.md | ilk kaynak haritası ve runtime açıkları |
| work/P2-01-named-role-contracts.md | ilk rol/sözleşme tabanı |
| work/P3-01-work-information-discussion.md | kavramsal iş/bilgi/düzen sözleşmesi, senaryo ve H1–H6 |
| work/P4-01-cloud-runtime-and-workspace-design.md | güncel koşullu teknik tasarımın tek ayrıntı evi; hedefte kurulmuş dosyalar değil |
| history/ | superseded snapshot'lar; normal cold-start'ta okunmaz |

Aşama ayrıntısı mevcut work/ altında ana plana bağlanır; boş dosya veya bağımsız paralel paket açılmaz. Current/next STATE/HANDOFF'a, üst harita WORK'e, gerçek kullanıcı kararı DECISIONS'a gider. P4 teknik tercihleri kabul edilmiş kadro diye ACTORS/P2'ye sessizce geçirilmez.

EXP-006, DevOS'un kendisi değil onu ortaya koyma çalışmasıdır. Gerçek SOUL işlerini ekip keşfeder/yürütür. Claude cloud kullanıcı kısıtıdır; P4 teknik seçim ve fiziksel alanı tasarlar, P5 gerçekleştirir, P6 davranışı sınar. Rutin tetikleyici olarak kullanıcı gerekmez; sınırsız insan-bağımsızlık istenmez.
