# DEVOS-001 — kaynak kapsamı ve okuma girişleri

**Güncelleme:** 24 Eylül 2026. **Kaynak tabanı:** `batuhanozgun/agentic-os-search@dc76496e2ea87a08b60f88ea8ec2731c6a4b5cbb`.
İş/yetki [WORK](../WORK.md), okuma/çıkarım yöntemi [METHOD](../METHOD.md). Bu dosya kapsam ve kayda erişim içindir; içerik doğruluğu veya tamamlanma oranı değildir.

## Tam envanterin yeri ve kanıt sınırı

Claude, başlangıç ağacı için 2.238 dosyalık manifest yayımladı:
- [Dosya manifesti](https://github.com/batuhanozgun/soul-development-os3_claudecode/blob/9866feb1127313394a3d1bd50bfd4b862a91567f/coordination/devos-001/reading/MANIFEST-dc76496.tsv).
- [Manifest özeti](https://github.com/batuhanozgun/soul-development-os3_claudecode/blob/9866feb1127313394a3d1bd50bfd4b862a91567f/coordination/devos-001/reading/MANIFEST-OZET.md), blob `0ab301214960e88129979101d9fedffe198a6e2b`.
- Aynı kökte `okuma-durumu.json` dosya/aktör/kayıt ilişkilerini taşır.

Research özeti tam okudu; 2.238 manifest satırını bu tur bağımsız olarak uzlaştırmadı. Sayılar aşağıda Claude kayıtlarının bildirdiği dosya kapsamıdır; bütün fikirler okunmuş/doğrulanmış yüzdesi değildir. Önceki kök/alt-ağaç kimlikleri [c91b71d COVERAGE](https://github.com/batuhanozgun/agentic-os-search/blob/c91b71dda8f619e52f5f3fd69a465667652534af/development-os/attempts/001/reading/COVERAGE.md)'de korunur.

## Bütün kaynak alanları

| Alan | Dosya (Claude manifesti) | Birincil okuma / durum |
|---|---:|---|
| Foundation | 931 | Research. F08 + düzeltme ve F00 kayıtlı; 18 özgün dosya okundu. Alt dikey/zemin/bileşim gövdeleri hâlâ açık |
| studies | 893 | Claude. 74 birim kaydı ve kök kaydı bildirildi; 116 ana oturum tam, 774 alt-ajan okuma/karşı okuma, 2 kısmi, 1 engel. Research toplu içerik okuması henüz yapılmadı |
| concepts | 75 | Claude. 9 kayıt, ana oturum tam okuma bildirildi; karşı okuma açık |
| soul-context | 59 | Claude E23/B-09 birincil okuması bu tur Research tarafından kabul edildi; Research karşı okuyucu |
| publications | 26 | Claude E23/B-09 birincil okuması; Research karşı okuyucu |
| explorations | 232 | Claude E23/B-09 birincil okuması; Research karşı okuyucu. EX0 kökünün 3 dosyası kayıtlı beyanı; kalanlar aktif/yarım durumuyla hedefte |
| Başlangıçtaki deneme kayıtları | 10 | Research; eski R/C ve denetim hattı tarihsel, yeni çıktı kuyruğuna çevrilmez |
| Giriş dosyaları | 2 | Research; root ve research/INDEX kapsama dahil |
| Kontrol | 10 | AGENT/agent alanı; Research yükler, araştırma sonucu olarak çıkarılmaz |

E23 başlangıç iş bölümünün bilinçli değişikliğidir. METHOD §3'teki dağılım başlangıç paylaşımı olarak kalır; güncel sorumluluk WORK ve bu tablodadır. Foundation 03/05 dahil Research'te kalır; Claude'un bunları daha sonra alma önerisi otomatik etkin değildir. İki taraf P2'de bütün kayıtları okuma yükümlülüğünü korur.

## Research kayıtları ve sıradaki kaynak

| Küme | Güncel giriş / durum |
|---|---|
| Foundation STATE/INDEX + 08'in 13 dosyası | Önce [F08 düzeltme ve ekleri](F08-RECONCILIATION.md), sonra [ilk F08](F08-FOUNDATION-FRAME.md). 20 ilk katkı + 5 ek. Claude karşı okuması alındı; dört maddi eksik işlendi. S07'nin önce eksik 91–95 aralığı bu tur okundu; ilk tamlık beyanı düzeltildi |
| Foundation README / RESEARCH-USE-ALIGNMENT / 00_context | [F00](F00-CONTEXT-AND-USE.md): üç kaynak tam, altı katkı. 00_context ağacı yalnız README içeriyor (1/1). Karşı okuma açık |
| 01_verticals | Sıradaki; bütün dikeyler, dosya envanteri ve tam okuma açık |
| 02_adequacy | Açık |
| 03_ground-deepening | Bütün zemin ve alt araştırmalar açık; Research |
| 04_top-level-adequacy-rerun | Açık |
| 05_relation-control-composition | Bütün bileşim ve alt araştırmalar açık; Research |
| 06_integration-frontier-review / 07_selection-dynamics-integration-review | Açık |
| Foundation history / REPAIR-AUDIT / REPAIR-PUBLICATION | Açık; tarihsel olmak okumama gerekçesi değildir |

08'in üst sonucu bu alt kaynakların okuması değildir. F00/F08'de örtüşen fikirler ayrı bağımsız kanıt veya ayrı zorunlu bileşen sayılmaz.

## Claude kayıtlarına giriş

[Özgün reading kökü](https://github.com/batuhanozgun/soul-development-os3_claudecode/tree/9866feb1127313394a3d1bd50bfd4b862a91567f/coordination/devos-001/reading).

- C-003: ilk alındı, manifest, gstack, concepts ve ortam başlangıcı.
- C-004: 35 studies paketi / 74 birim, 4.508 birim katkısı ve 39 paket katkısı bildirimi; 6 çok-birimli paketin GST0/AKS0/SUP0/TCL0/ECC0/HRM0 kayıtları; 9 concepts kaydı ve ORT1.
- C-005: F08 karşı okuması; E23 için soul-context/publications/explorations kapsamı.

Mesajların exact kaynakları ve alındısı WORK'tedir. Birim kayıtları `studies/<paket>/<kod>.md`, paket rotaları `*-paket.md`, concepts kayıtları `concepts/`, ortam `ortam/ORT1.md`, karşı okuma `karsi-okuma/` altındadır. Research bu tur bütün 74 kaydı veya 4.508 katkıyı okumadı: C mesajları/manifest özeti/F08 karşı okuması tam, GST0 yalnız 1–55 seçili okundu. Üretici okuması Research kaynak okumasına dönüştürülmez.

### Açık kapsam ve tüketim yükü

İki ECC gzip nesnesi kısmi; ASR görseli erişilemez olarak bildirilmiş. Hedef STATE'teki O-25 kaydı kullanıcıda da görsel kopyası olmadığını söylüyor; kullanıcıdan aynı dosyayı yeniden isteme. Kaynak sorunu çözülmüş veya görsel okunmuş sayılmaz. Mevcut yazılı temsilin sınırı korunur.

Claude ortam kaydının açıkları, concepts ve paket kayıtlarının karşı okuması, Research P1 ve daha sonraki P2 tam okuması açıktır. 'Claude payı bitti' bildirimi P1/P2 kapanış onayı değildir.

C-004 birim kayıtlarının 11.373.963 bayt olduğunu ve kaynaktan büyüdüğünü bildiriyor. Araştırılmamış aday soruları, gerçek bulgu ve Research/Claude yorumları ayrı kalmalı. Kayıt sayısı kalite değildir. Bu tur toplu silme/özetleme veya yöntem değişikliği başlatılmadı; paket rotalarıyla parçalara bölünmüş tam tüketim planı korunur.

## Soru → katkı yolları

| İhtiyaç | Kayıt |
|---|---|
| İşi üreten yapı, keşif, planlama ve katılım | F08-01/02/03/21; F00-03 |
| Gerçek ortam ve bileşik yapılabilirlik | F08-04/06/07; F00-02 |
| Bilgi, yeterlik, erişim, gerçek kullanım | F08-05/08/09/21; F00-04/05 |
| Amaç, yetki, kullanıcı sözü ve sorumluluk | F08-10/16/23; F00-01/03 |
| Devam, gerekçe, yeniden değerlendirme ve öğrenme | F08-11/12/20/24; F00-06 |
| Kapanış, alternatif çerçeve ve araştırmadan seçime | F08-13/14/15/17/18/19/22/25; F00-02/05 |

Bütün özgün kayıtlar ve gerekli karşı incelemeler tamamlanmadan P2/P3 başlamaz. Kaynak snapshot'ından sonra değişen maddi kaynaklar delta kuyruğuna alınır; yeni deneme kayıtları başlangıç paydasını sonsuz büyütmez.
