# Concepts — Hazırlık incelemesi

Tarih: 2026-09-19. Statü: hazırlık yayını ve son kontroller sürüyor. Bu dosya kurulum incelemesidir; pilot, terim çıkarımı veya yeni-oturum davranış deneyinin sonucu değildir. Güncel iş STATE.md'dedir.

## Başlangıç ve devralınan bağlam

Repository: batuhanozgun/agentic-os-search. Başlangıç main: c7e5d02a5be15b4b938c2796e3c274b04aa4bca4; tree 3d5007cd9bc3260065555f8e0ceecbe6af8adfac. Kök liste concepts dizininin bulunmadığını doğruladı. README eski altı dosyanın kaldırıldığını, diğer yönlendirmelerin henüz bırakıldığını belirtiyordu.

Bu konuşmanın görünür kullanıcı mesajları ve assistant yanıtları baştan sona yeniden değerlendirildi. Kalıcı ORIGIN kaydı beş kullanıcı mesajını ve açıkça alıntı olmayan kısa kronolojiyi taşır; bütün konuşma/araç arşivi değildir. Önceki konuşmaların project summary'leri yeni amaç yerine kullanılmadı.

AGENT güncel main'den yeniden getirildi. Aynı konuşmada tam okunmuş R01–R09 sürümleri başlangıç ağacındaki blob kimlikleriyle eşleşiyordu; R09 ayrıca tam içerikle yeniden okundu. Aynı konuşmada tam okunmuş README, research/INDEX, studies INDEX/CATALOG/PACKAGE-CONTRACT içerikleri aynı başlangıç sürümüne aitti. Kaynak araştırmaların tam okuması bu hazırlıkta yapılmadı.

## Eski izlerin ayrımı

Repository genelindeki concepts ve concepts/ aramaları, exact concepts/INDEX.md araması ve concept-use/programme anlatımı aramasıyla etkin yönlendirmeler belirlendi. Dönen arama parçaları tam dosya okuması veya evrensel yokluk kanıtı sayılmadı. Etkilenen giriş dosyaları tam içerikle değerlendirildi. Büyük recursive tree çıktısı araç görünümünde kesildi; bu tek çıktıdan bütün dosyaların okunduğu sonucu çıkarılmadı.

| Yüzey | Tespit / hedef işlem |
|---|---|
| README.md | Eski sıfırlama ve eksik hedef açıklaması; yeni programa ve doğru cold-start'a yönlendirilecek. |
| research/INDEX.md | Eski program tanıtımı, erişim tablosu ve yerleştirme istisnası; yeni iki aşamalı kapsamla değiştirilecek. |
| research/studies/INDEX.md | Tüm envanter bitmeden yerel referansa izin veren eski yöntem; kaldırılacak. |
| research/studies/CATALOG.md | Eski program açıklaması; araştırma satırları değişmeden yenilenecek. |
| research/studies/PACKAGE-CONTRACT.md | Eski yerleştirme/yöntem atıfları; yeni programa uygun dar istisnayla değiştirilecek. |
| agent/protocols/candidate-research-library.md | Eski concepts bölümü; yeni kullanıcı talebiyle sınırlı okuma/görünürlük/aşama disipliniyle değiştirilecek. |
| AGENT.md | R09 tetikleyicisinde concepts'in açık görünmesi sağlanacak; diğer routing soruları değişmeyecek. |

EXP-003 içindeki sources/conversation/assistant/S001.md tam okundu: başında bunun tarihsel yanıt aktarımı ve routing bloklarının tarihsel metin olduğu zaten açık. İçindeki eski concepts atfı yeni current route değildir; özgün alıntı değiştirilmez. ECC tur/yayın kayıtlarındaki eşzamanlı çalışma veya korunmuş kapsam notları da geçmiş işlem kanıtıdır, concepts yöntem otoritesi değildir. Gstack içindeki concepts klasörü ve dış standart/kaynakların concepts adları bu programın artığı diye silinmez.

Temizlik hedefi eski etkin karar/yöntem/yönlendirmelerdir. Başka araştırmaların tarihini veya bilimsel içeriğini yeniden yazmak değildir. Bu tarama repo genelinde bütün baytların anlamsal incelemesi ya da bütün tarihsel izlerin silindiği iddiası değildir.

## Yayın sınırı

Yeni dosyalar: concepts/ORIGIN.md, CHARTER.md, METHOD.md, PLAN.md, STATE.md, INDEX.md ve bu SETUP-REVIEW.md. Henüz research-bazlı TERMS veya READING dosyası, terim listesi, ortak tanım ya da önceden belirlenmiş kavram hiyerarşisi yoktur.

Mevcut main üzerinde bağlı GitHub create/update işlemleri kullanılacak. Yeni branch, force push, geçmiş yeniden yazımı ve araştırma paketi mutation'ı yoktur. Giriş dosyalarına yönlendirmeler çalışma dosyaları oluşturulduktan sonra güncellenir. Kontrol değişikliği yalnız AGENT/R09 concepts kapsamındadır; değişen iki canonical kontrol dosyası yeniden okunur.

## Son kontrol listesi — henüz tamamlanmış sayma

- İzin verilen 14 dosyanın dışına taşılmadığını başlangıç–son commit karşılaştırmasıyla kontrol et.
- Mevcut dosyaların diff'lerini incele; CATALOG araştırma satırları ve concepts dışı genel metin korunmuş olmalı.
- Yeni concepts dosyalarını main'den geri oku; statüler, yetki değişimi, iki risk ve sıradaki iş birbirleriyle tutarlı olmalı.
- AGENT ve R09'u değişiklik sonrasında tam oku; diğer protokol blob'ları değişmemiş olmalı.
- Yeni local markdown bağlantıları ve cold-start dosyaları mevcut olmalı.
- Eski etkin erken-referans yöntemi current router metinlerinde kalmamalı; korunmuş tarihsel kayıtlar yeni talimat olarak sunulmamalı.
- STATE hazırlık sürüyor durumundan ancak gerçek yayın kontrolü tamamlanınca hazırlanmış/pilot-bekliyor durumuna taşınmalı.

## Doğrulamanın sınırı

Bu kontrol aynı assistant'ın kaynak/diff/bağlantı incelemesidir. Başka aktörle bağımsız review, gerçek yeni konuşma koşusu, okuma-çıkarım pilotu veya davranışsal drift'in ortadan kalktığına dair deney yapılmadı. Dosyaların doğru yerleştirilmesi gerekli bir süreklilik desteğidir; modelin ileride kuralları eksiksiz uygulayacağını kanıtlamaz.
