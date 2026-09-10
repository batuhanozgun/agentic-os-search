# EXP-001 — Arşiv kapsamı ve doğrulama

## Hüküm

**Diyalog ve yeniden kullanım katmanı yayımlandı. Özgün eser payload'larının repository yayını eksik olduğu için arşiv bütünü PARTIAL.** Bu hüküm tüm bağımsız doğrulama iddialarından ayrıdır.

## Kaynak kapsamı

| Kaynak kesimi | Korunan şey | Doğrudan yol |
|---|---|---|
| U001–U003 / S001–S003 | Uygulama örneği, LLM girdi-çıktı lensi, bulgu/kural/durum ve başlangıç | [Diyalog INDEX](../sources/conversation/INDEX.md) |
| U004–U006 / S004–S006 | A–B–C, roman/dağıtım, özgün çizimin açıklaması ve C–W düzeltmesi | [Kullanıcı metinleri](../sources/conversation/USER-MESSAGES.md#u004) |
| U007 / S007 | Tam sentetik demo; tablolar, W-01–W-04, C0–C3, D-02 ve koşullu geçerlilik | [S007](../sources/conversation/assistant/S007.md) |
| U008–U009 / S008–S009 | Altı hayali dosya, görünmeyen muhakeme/işletim bilgisi ve aktörler | [S008](../sources/conversation/assistant/S008.md) |
| U010–U011 / S010–S011 | Harness, yanlış maliyet yorumu, kullanıcının mesleki standart düzeltmesi, uzmanlık sürekliliği | [U011](../sources/conversation/USER-MESSAGES.md#u011), [S011](../sources/conversation/assistant/S011.md) |
| U012 / S012 | Kırpmadan konsolidasyon isteği ve özgün teslim iddiası | [S012](../sources/conversation/assistant/S012.md) |
| U013–U015 / S013–S015 | Mekanik modelleme, dosya/işlem ayrımı ve Atlas teslimi | [S013](../sources/conversation/assistant/S013.md), [S015](../sources/conversation/assistant/S015.md) |
| U016–U017 / S016–S017 | Yaşayan katmanlı plan, başka dala not, C/plan/Work ve Foundation dayanağı | [U016](../sources/conversation/USER-MESSAGES.md#u016), [S017](../sources/conversation/assistant/S017.md) |
| U018–U019 / S018 | Ayrı denemeler kütüphanesi, arşiv planı ve açık uygulama yetkisi | [S018](../sources/conversation/assistant/S018.md) |

Toplam: 19 kullanıcı + 18 assistant = 37 görünür mesaj. Döküm model-visible transkripsiyondur; platform export'u, gizli muhakeme veya transport log'u değildir. Eski routing blokları pasif kaynak metindir. Kullanıcı yazımını düzeltmek yerine tespit edilen aktarım hatası kaynak ifadeye geri çevrildi.

## Eserler

| Eser | Yerel doğrulama | Remote durum |
|---|---|---|
| Konsolidasyon MD/PDF | Byte/hash eşit; PDF 35 sayfa | İçerik aktarımı bekliyor |
| Atlas HTML/PDF/ZIP | Byte/hash eşit; PDF 51 sayfa; ZIP 26 üyede CRC sağlam | İçerik aktarımı bekliyor |
| Özgün PNG çizim | Byte/hash eşit; yeniden çizilmedi | İçerik aktarımı bekliyor |
| ZIP'in 26 çıkarılmış kaynağı | Güvenli göreli yol ve üye byte'ı korunuyor | İçerik aktarımı bekliyor |

Atlas modelinden 41 node (22 işlem + 11 bilgi + 8 genel grup), 71 ilişki, 7 görünüm, 10 demo adımı, 12 açık mekanizma ve 21 kayıt tekrar sayıldı. Bu bir payload-kapsam kontrolüdür. Eski DOGRULAMA.json'un 24 UI kontrolü bu tur tekrar koşulmadı; bağımsız SOUL doğrulaması değildir.

## Yapılan remote kontroller

- `main` güncellemeleri `force:false` ile gerçekleştirildi; ayrı helper branch oluşturulmadı.
- `917d981d40ea0d1159543caac6c3fc27308cb36c` ile `55499db9d5dc425cd1a2b505d978e1c719d40c28` GitHub compare sonucu: 7 commit ileride, geride 0; 37 dosya yalnız root README, explorations ve research/INDEX kapsamındadır. Research INDEX değişikliği 4 ek satır, 0 silme.
- Assistant kaynak tree'si `ada897358b70741e31709595a5d9b5a0ef51433b`, S001–S018'in tamamını truncation=false olarak listeledi.
- USER-MESSAGES `baf8f24d784841daf135e148d0a3c9387d528a20` blob'u 1–50, 51–105 ve 106–180 satır aralıklarıyla okundu; U006 aktarım düzeltmesi ve son U019 görüldü. Bir araç çıktısının metadata sonu kısaldı; içerik kesimi görünür kaldı.
- S007'de tekrar gönderim / D-02 / W-03 ve S011'de mesleki standart düzeltmesi remote içerikten seçici geri okundu.
- Kaynak anahtarları, sınıf sınırları ve sonraki sorumluluk için INDEX/STATE/WORK-PLAN yolları açık bırakıldı.

Bu kontroller remote yayının yapısını ve seçili içeriğini doğrular; bütün diyalog için ikinci bir araştırmacı veya ham platform export'una karşı bağımsız sadakat doğrulaması değildir. Bu raporun kendisi daha sonraki checkpoint'te yayımlanır; karşılaştırılan 37 dosyalı snapshot ile raporun yayını aynı olay diye gösterilmez.

## Yerel tamamlama paketi

`EXP001_Artefakt_Tamamlama_Paketi.zip`: **3.416.116 byte**, 37 ZIP girdisi (32 payload + 5 yardımcı dosya), CRC kontrolü sağlam.

SHA-256: `054983b46aaa6ac33b226445ce194c1125ff89e5a7a1e4bdbc11cb579783a5a2`.

Payload manifest SHA-256: `f694d43923ec28e190f985aa30de6b9eefbe739bd00f0c773695785ee1a9e42c`.

Kopyalama helper'ı için 9 yerel kontrol: dry-run, eksik verify, 32 eşit kopya, tam verify, idempotence, farklı hedefte durma, symlink reddi, yanlış repo reddi, bozuk kaynak reddi. Bu helper commit/push veya kimlik doğrulama yapmaz. Güvenlik sertifikasyonu değildir.

## Açık kalan koşullar

1. Altı özgün dosya + 26 çıkarılmış kaynak remote'a henüz ulaşmadı; kalıcı arşivin en dip kaynak erişimi bu bakımdan eksik.
2. Ham platform export'u yok; visible transcription doğruluk sınırı korunuyor.
3. Tarihsel tool citation kimlikleri tek global ID değildir; konu ve S mesajı bazında repository kaynaklarına eşlenir. Bütün eski dış linklerin bugünkü canlılığı doğrulanmadı.
4. Bütün Markdown fragment'leri ayrı bir tarayıcı/crawler ile test edilmedi; bütün linkler geçti iddiası yok.
5. Atlas sonrası yaşayan plan üzerine odaklı araştırma yalnız aday sorudur; bu arşiv işi onu aktive etmedi.

Bir sonraki çalışma [PAYLOAD-TRANSFER](PAYLOAD-TRANSFER.md) ile sınırlandırılmıştır. Başka repository veya agent-control dosyasının değişmesi gerekmez.
