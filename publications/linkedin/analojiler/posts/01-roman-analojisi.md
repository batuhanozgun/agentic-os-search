# Taslak 01 — Roman analojisi

- Durum: LinkedIn post taslağı; yayımlanmış içerik değildir.
- Kaynak: [01-roman-analojisi-kullanici-talebinden-yasayan-is-tanimina.md](../01-roman-analojisi-kullanici-talebinden-yasayan-is-tanimina.md)
- Genel üslup rehberi: [BATU-YAZIM-REHBERI.md](../../../BATU-YAZIM-REHBERI.md)
- LinkedIn yayın rehberi: [LINKEDIN-YAYIN-REHBERI.md](../../LINKEDIN-YAYIN-REHBERI.md)
- Post gövdesi karakter sayısı: 2133
- Üst sınır: 2800

---

Agentic sistemler üzerine çalışırken şuna takıldım: Kullanıcının yazdığı prompt ile sistemin yapması gereken iş aynı şey mi?

Mesela kullanıcı “bir roman yazmak istiyorum” dedi.

Tek bir chat'te ilk refleks konu, karakterler, bölümler deyip romana girişmek olabilir. Çok-rollü bir agentic sistemde ise bu daha tehlikeli. Planner bunu task'lara böler, Researcher araştırır, Writer yazar, Verifier da verilen kriterlere göre kontrol eder.

Herkes görevini gayet düzgün yapar.

Ama başta yanlış işi tanımladıysak sistem yanlış şeyi çok iyi yapmış olur.

Çünkü “roman yaz” gerçekten ne demek?

Roman Word dosyası olarak masaüstünde mi kalacak? Basılacak mı? Yayıncı mı bulunacak? Dağıtım, fiyatlama, reklam işin parçası mı? Belki hiçbirisi değil; kullanıcı gerçekten yalnızca kendisi için yazıyordur.

Buradaki mesele AI'ın kullanıcıdan daha akıllı olup gizli niyet okuması değil. Tam tersine, prompt'u doğrudan executable work kabul etmemesi.

Agentic bir yapıda bir yerde “hangi iş gerçekten yapılmalı?” sorusunu taşıyan bir mekanizma lazım. Adına work discovery, planning, mission qualification ne derseniz deyin. Bu illa ayrı bir agent olmak zorunda da değil.

Ama bunun tersi de problem: Her şeyi tamamen anlamadan hiçbir şeye başlamamak.

Romanın ilk bölümünü yazmak için dağıtım şirketinin kim olduğunu bilmeye gerek yok. İlk bölümü değiştirecek kritik belirsizlikler yeterince kapandıysa Writer başlayabilir.

Sonra execution'ın kendisi yeni bilgi üretir.

Başta “dağıtımcı bul” diye task açmışızdır. Yayıncı bulunur, yayıncının dağıtımı da yaptığı ortaya çıkar. Task kaybolur. Başka bir bulgu hedef kitleyi değiştirir, editoryal plan değişir. Yeni bir uzman role ihtiyaç doğabilir.

Yani agentic sistemde plan sadece başlangıçta çizilen task graph değil. Çalışırken yaşayan bir state.

Bu yüzden raw user request ile current work definition'ın da aynı şey olmaması gerektiğini düşünüyorum. İlki kaynaktır, ikincisi çalıştıkça değişen mevcut anlayış.

Bence agentic yapılardaki asıl risklerden biri yanlış cevap almak değil.

Yanlış işin kusursuz şekilde orkestre edilmesi.

Prompt başlangıç noktasıdır; task specification değil.
