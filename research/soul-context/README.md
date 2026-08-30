# SOUL Context Research

## Amaç

Bu alanın amacı `os-architect`, `keel`, `soul` ve yalnız gerekli olduğunda sınırlı predecessor kanıtı olarak `keel-research` kaynaklarını okuyarak iki şeyi kalıcı biçimde taşımaktır:

1. SOUL Research projesinin neden açıldığına dair kaynak-temelli bağlam,
2. araştırmanın hangi tür sistemi beslemesinin amaçlandığına dair bounded çalışma anlayışı.

Bu klasör proje-geneli araştırma metodolojisi, agent-control katmanı veya SOUL mimarisi değildir.

## Epistemik ayrım

Bu klasörde üç farklı içerik türü fiziksel olarak ayrılır:

- `repos/` — kaynak okuma defterleri; hangi repo/dosyanın okunduğu, SHA/ref, okuma türü ve maddi bulgu.
- `evidence/` — repo okumalarından türetilen, kaynaklara geri bağlanabilen context sentezi.
- `exploratory/` — bu context çalışması sırasında erken üretilmiş taxonomy, holdout, stopping ve research-design fikirleri. Bunlar bilgi kaynağı veya proje-geneli yöntem değildir.

`exploratory/` içeriği sırf mevcut olduğu için sonraki araştırmaya başlangıç çerçevesi olarak yüklenmez.

## Navigasyon

Önce `INDEX.md` kullanılır. `INDEX.md` hangi konu için hangi dosyanın açılması gerektiğini gösterir; kendisi source-of-truth değildir.

- `INDEX.md` — topic/claim routing index.
- `STATE.md` — bu context hattının güncel statüsü.
- `evidence/CONTEXT-SYNTHESIS.md` — mevcut bounded context sonucu.
- `repos/` — ayrıntılı source ledgers.
- `exploratory/README.md` — erken/ekstra çalışmanın sınırı ve kullanım kuralı.

## Kullanım kuralı

Kullanıcı "eski repo araştırmalarına bak", "önceki repolardan ne biliyoruz?" veya benzeri bir talep verdiğinde varsayılan retrieval alanı:

1. `INDEX.md`,
2. ilgili `evidence/` dosyası,
3. gerekiyorsa ilgili `repos/` ledger bölümü,
4. exact veya tartışmalı claim gerekiyorsa birincil repo kaynağıdır.

`exploratory/` bu varsayılan zincire dahil değildir.

## Kaynak rolleri

- `soul` — current explicit intent, Development OS, foundation/work/verification/review evidence için birincil kaynak.
- `os-architect` — tarihsel failure, yöntem, araştırma, owner-correction ve KEEL geliştirme bağlamı.
- `keel` — somut ürün/mekanizma yüzeyi; tarihsel iddiaların seçici mekanik karşı-okuması.
- `keel-research` — yalnız doğrudan source-chain gerektiğinde bounded predecessor prior-art; SOUL authority değildir.

## Kanıt dili

- **Gözlem:** kaynakta doğrudan görülen olgu.
- **Çıkarım:** bir veya daha fazla gözlemden türetilen yorum.
- **Hipotez:** henüz yeterli karşı-okuma yapılmamış açıklama.

Derived view, summary, ledger veya index birincil kaynağın yerini almaz. Load-bearing exact claim gerekiyorsa kaynak recover edilir.

## Context hattının statüsü

Bu hazırlık/context hattı mevcut amaç için yeterli seviyede tamamlanmış ve durdurulmuştur. Ayrıntı `STATE.md` içindedir.

Proje-geneli "araştırmayı nasıl yapacağız?" kararı bu klasördeki exploratory fikirlerden otomatik türetilmez; ayrıca ve kullanıcı tarafından yetkilendirilmiş ayrı bir çalışma olarak ele alınır.
