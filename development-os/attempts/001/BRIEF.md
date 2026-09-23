# DEVOS-001 — amaç, kullanıcı yönü ve sınırlar

**Deneme:** 001; 23 Eylül 2026. **Hedef aktör/repo:** Claude Code / `batuhanozgun/soul-development-os3_claudecode`.
**Güncel yön:** bütün korpus okuması ve kayıtlar tamamlandıktan sonra Development OS'u kuracak çalışma yapısına karar.
[Yönetim](WORK.md) · [Yöntem](METHOD.md) · [Kapsam](reading/COVERAGE.md) · [İletişim](EXCHANGE.md).

## İlk amaç

Development OS'u kurabilecek bilgi, iş, aktör ve ortam düzenini hazırlamak; bunu kullanıcıya teknik eksik-bulma, araştırmayı yeniden okuma ve sürekli koordinatörlük yükü bırakmadan yapmak. Mevcut Claude dosyalarının onarımı, E19 veya mesajlaşma bu amaç değildir. Yeni çalışma/test repo veya Deneme-002 seçilmedi.

İlk kullanıcı mesajının amacı: Foundation, gstack, Hermes ve ECC gibi birikimden yararlanarak Claude'un Development OS'u kurabilmesini sağlayacak çalışma düzenini oluşturmasına yardım etmek. İlk mesajdaki tam sözler bu konuşmada görünür; önceki [BRIEF](https://github.com/batuhanozgun/agentic-os-search/blob/dc76496e2ea87a08b60f88ea8ec2731c6a4b5cbb/development-os/attempts/001/BRIEF.md) deneme alanının açılmasına ilişkin özgün kullanıcı mesajını ve ilk kaygıyı korur.

## En son kullanıcı yönü — tam görünür mesaj

Aşağıdaki metin kullanıcının bu konuşmadaki son mesajının aynen aktarımıdır. Claude'a ulaştığı veya uygulandığı anlamına gelmez; alındı WORK'tedir.

> Yumuşatma durumu, bildiğin kaydın gittin konsepten, hiç laf ebeliği yapma. Süslü laflarla avunduğun şeyi yapmak için kendine doğru süzgün bir bağlam yakalayacak çözüm üret.  ilk mesajdan koptun konudan hiç yalan söyleme bana. Claude’a da söyle adam gibi çalışsın. Bokunuzla oynamayın adam gibi yapı kurun. Çocuk oyuncağı mı bu iş. Kendinize gelin tonla araştırma yaptık hala iki tane boktan dosya üstünde konuşuyorsunuz. Şu işi çözecek yapıyı kurmak için adam gibi çalışma yapısı kurun, ufacık konuyu sündürerek oyalanıyorsunuz. Sikicem yapcağınız işi. O da senin reponu okuyor, sen de okuyorsun hala development os’u kurabilecek çalışma düzenini kuramadınız, bu kadar araştırmayı ben kendim okuyayım diye mi yaptırdım ben sana? Bana lafı dolandıra dolandıra cevap veriyorsun. Salak mı sanıyorsun sen beni? Bütün repoyu gözden geçireceksiniz, her turda development os’u kuracak yapıya katkı sağlayacak tüm fikir ve örnek yapıları sonradan onuyabileceğiniz bir şekilde kayıt altına alacaksınız. Tüm okuma ve kayır altına alma bitince de bu kayıtlardan nasıl bir çalışma yapısı çıkaracağınıza karar vereceksiniz. 4 bacak diye konuştuk, iş ne kim yapacak nasıl takip edilecek hangi ortamda yapılacak hepsinin cevabı var, dikkat edlmesi gereken herşey var, okumuyorsunuz, anca laf kalabalığı yapıyorsunuz. Az laf çok icraat, bundan sonra göz açtırmayacağım size. Siktirmeyin yapay zekanızı bana. Adam gibi çalışmanın yöntemini bulmak zorundasın. Sikerim claude’un iki dosyası varmış da yok denetlemiş de ona takılmış da. Takılma kardeşim ben senden ne istedim, sen neyle uğraşıyorsun bu kadar araştırma sonunda sikik bir dosyadan drift edeceksen siktir git çalışma amına koyayım.

## Görev karşılığı

Önce bütün repo incelenecek; her tur gelecekte okunabilecek kaynak-bağlı fikir/örnek kayıtları oluşacak. Bütün okuma/kayıt işi tamamlandıktan sonra kayıtların tamamından nasıl bir çalışma yapısı çıkarılacağına karar verilecek. Dört zemin ve aralarındaki ilişkiler çalışma bakışıdır; zorunlu dört bileşenli mimari değildir.

Bu yön R-003/C-003 dar revizyonu→M1–M3 kurulum sırasını geçersiz kılar. Eski kanıtlar ve mesajlar tarihçe olarak kalır. Kullanıcının sert tepkisi teknik iddianın kanıtı değildir; görev sırası ve hedefe dönüş isteği açıktır. 'Bütün cevaplar zaten var' diye araştırılmamış yetenek veya sonuç icat edilmez.

## Roller ve yetki

Research: kaynak kapsamı, kendi tam okumaları, kalıcı çıkarımlar, bütün işin devamı ve ortak değerlendirme. Claude: kendi atanmış korpus okuması, çıkarımları ve hedefteki gerçek ortam bağlamı. İki tarafın kaynak/okuma statüleri ayrı; anlaşmaları doğruluk kanıtı değil. Batu teknik kaynak seçen veya mesaj içeriği taşıyan ara aktör yapılmaz.

Şimdi yetkili iş: okuma yönteminin kurulması, kaynakların incelenmesi, pasif kalıcı kayıtlar ve bunların tamamından sonraki yapı kararı. Henüz geniş deney, sistem implementasyonu, yeni repo, izin genişletme veya otomasyon başlatılmaz. Agent-control değişmez. Yeni kalıcı kayıtlar Foundation/studies kaynaklarının anlamını geriye dönük değiştirmez.
