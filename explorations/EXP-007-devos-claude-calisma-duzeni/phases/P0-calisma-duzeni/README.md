# P0 — Çalışma düzenini kurmak (metodoloji)

**Amaç:** Claude'un (ana oturum ve alt ajanlar) EXP-007'yi uzun soluklu, oturumlar arası ve Batu'yu gizli koordinatör yapmadan yürüteceği çalışma düzenini standart seviyede ortaya koymak ve Batu ile anlaşmak.

**Ölçüt:** [DECISIONS](../../DECISIONS.md) K-007. Metodoloji şunları kapsamalı:
- bağlam yönetimi;
- bellek yönetimi;
- alt ajanlar için kalıcı roller;
- en iyi uygulamalara dayalı bir yöntem;
- A003'te söylenen her şeyin "nasıl" yapılacağı.

Hedef standart seviyedir, "yeterli seviye" değil. Alt sistemler arası etkileşim de hesaba katılmalı.

**Kapsam dışı:**
- P1'in kendisi, yani Claude cloud araştırması. Metodolojinin ihtiyaç duyduğu ortam bilgisi R01 ve R07'den alınır.
- DevOS rollerinin tasarımı (P2).
- EXP-006 dosyalarını değiştirmek.
- Kontrol ve yapılandırma değişikliklerini kurmak; bu aşamada yalnız öneri olarak hazırlanır.

## Adımlar

| Adım | İş | Durum | Çıktı |
|---|---|---|---|
| P0.1 | EXP-006'yı anlamak ve ilk öneri (v0) | TAMAM. Anlayış kabul edildi, yapı küçük bulundu (K-006, K-007) | [A003](../../sources/conversation/A003.md); R02–R06 |
| P0.2 | Süreklilik kaydı | TAMAM | README, STATE, DECISIONS, `sources/` |
| P0.3 | Standart seviye araştırması: her alt sistem için dünyada ve repoda "standart" ne? | TAMAM | R07–R11 |
| P0.4 | METHOD v1 taslağı (ayrıntısı aşağıda): önce beş küme taslağı (T1–T5), sonra birleştirme | TAMAM | `drafts/T1–T5` → [METHOD-v1-TASLAK](METHOD-v1-TASLAK.md) (1.514 satır; 157 kart dizini) |
| P0.5 | Eleştiri turu, üç ayrı eleştiri (ayrıntısı aşağıda) | TAMAM: 5 kritik, 26 önemli, 14 küçük bulgu | [reviews/E1](reviews/E1-soz-cikti-ve-standart.md) · [E2](reviews/E2-butunsel-etkilesim.md) · [E3](reviews/E3-batu-ilkeleri-ve-uygulanabilirlik.md) |
| P0.6 | Revizyon ve Batu'ya kısa sunum | SÜRÜYOR: revizyon ajanı çalışıyor | `METHOD-v1.md`, `reviews/DEGISIKLIK-KAYDI.md` |
| P0.7 | Batu'nun düzeltmeleri; A-02'ye göre konuşma içi pilotlar; yeniden revizyon | BEKLİYOR | — |
| P0.8 | Anlaşma ve "başla": onaylanan yapılandırmaların kurulması, yön tabelalarının düzeltilmesi (A-05), P1'e geçiş | BEKLİYOR | — |

**P0.4 taslağının içeriği:**
0. EXP-007'nin baştan sona haritası, P0'dan P6'ya. K-010'a göre EXP-006'nın planı bağlayıcı değildir; yalnız girdi olarak okunur.
1. sistem envanteri;
2. her alt sistem için standart seviye, bizim seçimimiz ve bunun "nasıl" yapılacağı;
3. alt sistemler arası etkileşim matrisi;
4. kalıcı roller;
5. bağlam ve bellek tasarımı;
6. prosedürler;
7. dosya mimarisi;
8. önerilen yapılandırmalar;
9. pilot planı.

Birleştirmenin görev tanımı: [briefs/ENTEGRASYON](briefs/ENTEGRASYON.md).

**P0.5 eleştirileri** (ortak bölüm: [briefs/E-ORTAK](briefs/E-ORTAK.md)):
1. Söz–çıktı izlenebilirliği: A003'te ve U004'te söylenen her şeyin taslakta bir mekanizması var mı? Standart seviyede mi, yoksa yalnız "yeterli" seviyede mi? → [briefs/E1](briefs/E1.md)
2. Bütünsel etkileşim: bir alt sistemde yapılan seçim bir başkasını zayıflatıyor mu? → [briefs/E2](briefs/E2.md)
3. Batu'nun ilkeleri ve ortamda uygulanabilirlik. → [briefs/E3](briefs/E3.md)

**P0.6 revizyonu:** [briefs/REVIZYON](briefs/REVIZYON.md). Her bulgu kabul, kısmen ya da ret kararıyla işlenir; çıktı `METHOD-v1.md` ve `reviews/DEGISIKLIK-KAYDI.md`.

## Araştırma notları (`research/`)

| Not | Soru | Durum | Görev tanımı |
|---|---|---|---|
| R01 | Claude Code cloud, özerkliği ve uzun soluklu çalışmayı taşır mı? | TAMAM (26 ajan) | [A002](../../sources/conversation/A002.md) bağlamında Workflow |
| R02 | EXP-006 nasıl çalıştı, nerede kaydı? | TAMAM | A003 turunda sohbet içi |
| R03 | Batu'nun AI ile çalışma ilkeleri | TAMAM | A003 turunda sohbet içi |
| R04 | Foundation'ın işletime dair çıkarımları | TAMAM | A003 turunda sohbet içi |
| R05 | Studies'teki çalışma mekanizmaları (görev tanımı, plan, doğrulama, devir) | TAMAM | A003 turunda sohbet içi |
| R06 | EXP-004 mekanizmaları | TAMAM | A003 turunda sohbet içi |
| R07 | Anthropic ve Claude Code en iyi uygulamaları | TAMAM | [briefs/R07](briefs/R07.md) |
| R08 | Anthropic dışı metodolojiler | TAMAM | [briefs/R08](briefs/R08.md) |
| R09 | Studies: bağlam, bellek, rol ve yaşam döngüsünde standart seviye | TAMAM | [briefs/R09](briefs/R09.md) |
| R10 | Foundation: bağlam, bellek ve kalıcı rol için gereksinimler | TAMAM | [briefs/R10](briefs/R10.md) |
| R11 | Sistem envanteri ve etkileşim matrisi | TAMAM | [briefs/R11](briefs/R11.md) |

R07–R11 için ortak kurallar: [briefs/ORTAK.md](briefs/ORTAK.md).

Notların hepsi alt ajan çıktısıdır. Kararı taşıyan iddialar kaynağından kontrol edilir. R01–R06'nın başlığında ana oturumun hangi iddiaları kontrol ettiği yazılıdır.

R02–R06'nın görev tanımları sohbet içinde verildi ve repoya yazılmadı. R07'den itibaren görev tanımları `briefs/` altında kayıtlıdır; aynı tanımla yeniden çalıştırılabilir.

## Küme taslakları (`drafts/`)

R11'in 21 alt sistemi beş kümeye bölündü. Her küme kendi alt sistemlerini mekanizma kartlarıyla tasarlar; sonra bir birleştirme ajanı hepsini tek METHOD taslağında birleştirir.

Görev tanımları:
- ortak bölümler: [briefs/ORTAK-SENTEZ](briefs/ORTAK-SENTEZ.md) ve [briefs/T-ORTAK](briefs/T-ORTAK.md);
- her küme için: `briefs/T1.md` … `briefs/T5.md`.

| Küme | Alt sistemler | Çıktı | Durum |
|---|---|---|---|
| T1 | S7 bağlam · S8 bellek · S9 kayıt mimarisi · S10 anlam bütünlüğü | [drafts/T1](drafts/T1-bilgi-tasima.md) | TAMAM (219 KB, 33 kart) |
| T2 | S11 kalıcı roller · S12 orkestrasyon · S13 arayüzler · S16 güvenlik | [drafts/T2](drafts/T2-aktorler-ve-guvenlik.md) | TAMAM (179 KB) |
| T3 | S3 yaşam döngüsü · S4 keşif · S5 plan · S6 araştırma kullanımı · P0–P6 haritası | [drafts/T3](drafts/T3-isin-akisi-ve-harita.md) | TAMAM (170 KB, 33 kart) |
| T4 | S1 yönetişim · S2 Batu ile iş birliği · S14 kalite · S15 muhakeme disiplini · S17 gözlemlenebilirlik | [drafts/T4](drafts/T4-yon-yetki-ve-denetimler.md) | TAMAM (187 KB) |
| T5 | S18 süreklilik · S19 ortam ve yapılandırma · S20 maliyet · S21 öğrenme | [drafts/T5](drafts/T5-dayaniklilik-ve-evrim.md) | TAMAM (192 KB) |
