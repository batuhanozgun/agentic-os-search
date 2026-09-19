# Context / Memory / Harness — Okuma ve aktarım durumu

2026-09-19. **P1-PILOT-CLOSED / B6-DURABLE-TRANSFER-ACTIVE / CONTEXT-SECTION-RECORDED / PACKAGE-NOT-CLOSED.** Bu dosya concepts içindeki kalıcı aktarımın yetkili yerel durumudur; özgün araştırmanın STATE.md'sinin veya global concepts/STATE.md'nin yerine geçmez.

## Amaç ve iki ayrı tamamlanma

P1 konuşma pilotu sekiz araştırma dosyası üzerinde P1-T1–T3'te tamamlandı. Şimdi yapılan, o sonucu kaynakları ve ek/düzeltmeleriyle kontrol ederek kalıcı kayda almaktır. Pilot araştırması yeniden açılmadı. Kalıcı aktarımın tamamlanması ise ayrı iş: bu tur yalnız context bölümünün kayıtları [TERMS.md](TERMS.md)'ye alındı. D2/D3/D4 ve kalan pilot kayıtları henüz kalıcı aktarılmadı.

İki risk korunur: kullanıcı okuma anındaki yorum seçimlerini denetleyemiyor; önemli anlam/dayanak/belirsizlik/değişiklik görünür olmalı. Ortak sözcükler ortak anlamı garanti etmiyor; kullanıcı onayı, kaynak kullanımı ve çıkarıcının yorumu teknik doğruluk değildir. Genel terim araştırması, yeni ürün deneyi, ortak tanım veya mimari kararı yoktur.

## Kaynak bağlama

- Repository: batuhanozgun/agentic-os-search.
- Kaynak öneki: research/studies/context-memory-harness-engineering/.
- P1 kaynak ref'i: **ac64fb9223cfa797e7eaabcdcbbf8bac3cc3ef0a**.
- S1 kapsam ref'i: **9b46155e904560c90b89e657f3d0d4e00e2e46cf**.
- Paket tree: **e32d7736c4a3b31f123ab84eaafe053b0b2ca08e**.
- [Tam, sekiz yapraklı kaynak manifesti](https://api.github.com/repos/batuhanozgun/agentic-os-search/git/trees/e32d7736c4a3b31f123ab84eaafe053b0b2ca08e).
- [P1 kapanışının değişmez çalışma kaydı](https://github.com/batuhanozgun/agentic-os-search/blob/53c29b54a355742960f466a06a5d9bba0a42f412/concepts/STATE.md).

P1 ref'inden dönen contents listesindeki sekiz path/blob, S1 paket ağacıyla karşılaştırıldı; fark yok. Sekiz dosyanın kip/ad/SHA girdilerinden yerel Git tree yeniden hesaplaması da e32d7736… verdi. Bu, manifest aktarımı ve sürüm eşitliği kontrolüdür; kaynakların bilimsel doğruluğuna veya her kaydın anlamına ilişkin bağımsız doğrulama değildir. Sekiz dosya düz metin Markdown; bu paket ağacında alt dizin veya binary ek bulunmuyor. Bağlantı verilen dış makale/video/repolar bu sekiz dosyanın yeniden okunmuş içerikleri sayılmaz.

## Dosya envanteri ve gerçek okuma

Bütün yollar yukarıdaki kaynak önekine göredir; tüm dosyaların Git kipi 100644'tür. P1 sütunu önceki tamamlanmış pilotun kaydıdır; bu tur yeni okuma olarak sayılmaz. B6-T1 sütunu bu tur gerçekten geri kazanılan içeriktir. EOF kaynak gövdesinin sonunun görüldüğünü belirtir; istek üst sınırı gerçek dosya satır sayısı değildir.

| Dosya | Blob SHA | P1 okuması | B6-T1 kaynak kontrolü | Kalıcı aktarım |
|---|---|---|---|---|
| META.md | 55e8d5abe294e9c9b4ae0cd121c1cea3a74b7007 | tam | tek yanıt, 1–EOF | amaç/sınıf/kaynak rolü geri kazanıldı |
| STATE.md | 298c0b1c6af6523a1da6b9bb0be018c5579573b2 | tam | tek yanıt, 1–EOF | özgün araştırmanın complete / değerlendirme bekliyor durumu ayrıldı |
| INDEX.md | 72c9756038330a499077fe8a6abebda5f280c79e | tam | tek yanıt, 1–EOF | yönlendirme ve tarihsel eski yol ifadeleri not edildi |
| 00-WHY-THIS-RESEARCH.md | be59481ee543f3b1244262664d8e01ac26dec030 | tam | 1–160, 161–340, 341–EOF (istek 600) | amaç/hipotez/atıf sınırları ve context bağlantıları aktarıldı; diğer alan kayıtları sonraki aktarımda |
| 01-CONTEXT-ENGINEERING.md | eed5603460ae9e74d4601b9204bf9502963b9be7 | tam | 1–190, 191–390, 391–620, 621–EOF (istek 900) | K01/K02, C01–C28, E-CTX-01–10 ve context ilişki görünümü kaynakla kontrol edilerek yazıldı |
| 02-AGENT-MEMORY-ENGINEERING.md | 6203b06fe56cad61354e9093d0b404a1ee3592c7 | tam | bu tur yeniden içerik kontrolü yok; yalnız manifest eşitliği | bekliyor |
| 03-HARNESS-ENGINEERING.md | 53f3cbcfbc934155553c9ae6c4ff931126b00876 | tam | bu tur yeniden içerik kontrolü yok; yalnız manifest eşitliği | bekliyor |
| 04-CROSS-LAYER-SYNTHESIS.md | 293ca01ac04952417d9d56b3c79c5f195dd6da35 | tam | bu tur yeniden içerik kontrolü yok; yalnız manifest eşitliği | bekliyor |

Bu tur beş dosyanın tam geri okuması, önceki sekiz dosyalık pilotun yeniden yapılması veya yeni bir tamamlanma yüzdesi değildir. Pilotun bitmiş durumu korunurken kalıcı çıkarım dosyası açık tutulur.

## Context bölümünün kaynak tarafından kontrolü

| Kaynak bölümü | Kayıttaki karşılık |
|---|---|
| D1 §1–4 | araştırma sorusu/kapsam; K01/K02, C01–C03 ve C24/C26; çok token ile yararlı bağlamın ayrımı |
| D1 §5 | C04–C10: talimat, iş durumu, dış kanıt, bellek geri çağırma, araç arayüzü/sonucu ve türetilmiş görünüm |
| D1 §6–10 | C11–C14, C21–C25; RAG/Long Context/CAG/bellek ilişkileri kendi kaynak statüsüyle |
| D1 §11–16 | C10, C15–C20, C27; sıkıştırma, araç çıktısı, alt aktör bağlamı, sıra, kirlenme ve güven sınırı |
| D1 §17 | E-CTX-01–10; ayrı ölçüm/deney üretilmeden kaynak değerlendirme soruları |
| D1 §18–20 | context ilişki görünümü ve C28; SOUL karar çerçevesi ile tarihli Development OS yorumu, mimari değil |
| D1 §21–25 | önceki açıklamaların bulgu tekrarı, güven etiketleri, açık sorular, sınırlar, atıflar ve tarihsel devam; yeni bağımsız kanıt veya yeni araştırma borcu değil |
| D0 §1–4, §7–13 | kapsam, başlangıç hipotezleri, kaynak listesi ve sınırlı araştırma amacı; D1 tanımlarının hangi bağlamdan geldiği |
| D0 §5–6 | SOUL/Development OS kullanım amacı ve tarihli repo yorumu; bugün inşa edilmiş ürün varsayımı değil |
| META/STATE/INDEX | sınıflandırma, araştırma/pilot/seri aktarım durumlarının ayrılığı ve kaynaklara dönüş yolları |

Kontrol, bu context bölümünün kaynakta açıklanmış kullanımlarıyla kalıcı kayıt arasında yapıldı. D0'ın diğer alanlara ilişkin tüm terimleri veya bütün paketin son kapsam hesabı tamamlanmış sayılmıyor. Aynı assistant tarafından yapılan kaynak karşılaştırmasıdır; bağımsız review veya çalıştırılmış test değildir.

## Yorum ve kimlik devri

P1-T1'in K01/K02 ve C01–C20; P1-T3'ün C21–C28 kayıtları özgün kimlikleriyle korundu. Birden çok farklı işlem/nesne içeren bazı gruplar .a/.b alt adresi aldı; üst kimlik eski kaydı bulmaya devam eder. Önceden açıklanmış context değerlendirme başlıkları E-CTX adresleriyle ayrıca erişilebilir yapıldı. Sayısal kimlik artışı yeni kavram keşfi veya ortak tanım kararı değildir.

Önemli eski ayrımlar korunur: atfedilen dar tanım/araştırma genişletmesi; kaynak/türetilmiş görünüm; araç arayüzü/sonucu; doğru erişim/uygun bağlam; kapasite/etkili kullanım; bilgi düzeni/gerçek yükleme. Kalıcı kayıtlar genel tanım gibi okunmasın diye kaynak rolü ve açıklama niteliği her bölümde görünür tutuldu.

## Sıradaki yetkili iş

**B6-T2:** D2'nin aynı kaynak ref'indeki içeriğini ve görünür P1 bellek kayıtlarını kontrol et; K03/K04/K08 ile M01–M28'i uygun kaynak/yorum statüsü ve alt adreslerle TERMS'e ekle. D3 ve D4 ardından gelir. Gerekli source recovery yapılmadan STATE özetinden terim üretme. Kaynak metni gerçekten erişilebilir ve değişmemişse sırf yeni tur olduğu için mekanik tam tekrar yapma; eksik görünüm varsa gerekli derinliği geri kazan.

Sonraki aktarımlarda özellikle korunacak P1 düzeltmeleri: K07 tasarım amacı ile sağlanmış özellik ayrımı; K08 tekil bellek kaydı; H17 bellekten bağlama bilgi/metadata aktarımı; canonical state ile bellek yaşam döngüsünün farklı otorite/kapsam eksenleri; X02'deki tarihli Development OS kullanımı. Bunların varlığını not etmek, ilgili kayıtların burada zaten aktarıldığı anlamına gelmez.

Kalan K/M/H/G/X kayıtları ve paket-geneli ilişkiler tamamlanınca bütün sekiz dosyadan kalıcı döküme son kapsam kontrolü yapılır. Yeni/değişmiş kaynak delta'sı ayrıca kontrol edilir. Ancak ondan sonra bu kalıcı aktarım kapanır ve sıra Superpowers aktarımına geçer. Ortak tanım aşaması hâlâ başlamaz.

## Yayın ve kapsam

Bu turki kalıcı çıktılar TERMS.md ve bu READING.md'dir; global SCOPE/INDEX/PLAN/STATE uygun devam için güncellenebilir. Özgün araştırma dosyaları, kontrol katmanı, Foundation ve diğer oturumların çalışmaları değiştirilmez. Yeni dosyanın varlığı tamamlanma makbuzu değildir. Yayımlanan içerik geri okunur, değişiklik kapsamı ve eşzamanlı kaynak deltaları kontrol edilir; gerçek sonuç global STATE ve görünür yanıtta belirtilir. Kendi henüz bilinmeyen commit'i veya yapılmamış kontrol sonucu burada uydurulmaz.
