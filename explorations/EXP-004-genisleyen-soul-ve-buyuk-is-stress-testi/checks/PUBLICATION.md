# EXP-004 — Güncel yayın ve kontrol kaydı

**Durum:** SOURCE-FIDELITY-REPAIR-STAGED / MAIN-PUBLICATION-PENDING.

Önceki PR #29 ve #30 gerçekten yayımlandı; ancak kaynak tamlığı iddiaları fazla güçlüydü. Eski metin değişmeden [HISTORICAL-PUBLICATION-PR29-30](HISTORICAL-PUBLICATION-PR29-30.md) içinde korunur. Güncel kaynak kapsamı [manifest](../SOURCE-MANIFEST.json) ve [onarım kaydındadır](REPAIR-20260921.md).

## Bu onarımın bağlı kimlikleri

Başlangıç main `fb488942ddbd951f3ce5887c1acdab2c3aac8bc6`; dal `repair/exp-004-source-fidelity-20260921`.
Kaynak payload `f1e93a9f052fb98b3f2e28e987233f3b51193534`; assistant tree `ba3111b97927ebb231947b2a500eee1d534a5a16`; kullanıcı blob `1866f243b3771a2d0152bc6b20f67c1a7f3f80c3`.

31 kaynak mesajı/16 dosya/182.486 byte; rakamlar Git ağaç/contents metadata'sı ve byte-toplam hesabına dayanır. USER-MESSAGES, S001, S013 ve S015 uzaktan tam geri okundu. Bütün kaynak gövdelerinin ikinci kez tam okunması, bağımsız transcription veya platform export eşitliği iddia edilmez.

## Yayında kontrol edilecek sınır

Exact PR head, gerçekleşen merge, gerçek main parent ve değişen yollar; kaynak ağaç ve kullanıcı blob eşitliği; eski yoğunlaştırılmış ağaç ve tarihsel eserlerin korunması; güncel STATE/INDEX/manifest/router'ların main'den erişimi. Eşzamanlı başka işlerin farkları korunur; force push yoktur.

Bu dosya henüz gelecekteki merge SHA'sını uydurmaz. Gerçekleşen yayın ve readback sonucu gözlendikten sonra kapanış kaydı eklenir. Bu onarım hiçbir SOUL runtime, öğrenme performansı veya bütün repository kusursuzluğu iddiası taşımaz.
