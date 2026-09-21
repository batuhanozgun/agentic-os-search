# EXP-004 — Kaynak aktarımı ve sadakat sınırı

**Kaynak:** 20–21 Eylül 2026 bu conversation'da modele görünür 14 kullanıcı mesajı ve 13 substantive assistant yanıtı. Platformun ham export'u veya bağımsız message-ID/timestamp servisi sağlanmadı.

## Yapılan aktarım

Mesajlar local U001–U014 ve S001–S013 kimlikleriyle adreslenir. User ve assistant substantive mesajları ayrı dosyalarda korunur; [conversation INDEX](../sources/conversation/INDEX.md) sıra verir. U014 repository kayıt yetkisiyle biter.

Assistant'ın tool çalışmaları arasındaki progress/commentary mesajları ve tekrar routing disclosure'ları source dialogue'un ana substantive yanıtları olarak ayrı mesaj kimliği almaz. Kalıcı final/substantive cevap gövdeleri korunur. Bu seçim exact UI message-count export'u değildir; exploration'ın karar/model evrimini taşıyan substantive kesimdir.

## İddia edilmeyenler

- byte-perfect platform export;
- UI whitespace/code-block-id eşitliği;
- bağımsız transcription verification;
- hidden chain-of-thought aktarımı;
- raw tool-response veya connector log archive;
- dış kaynak claim'lerinin bu arşiv turunda yeniden doğrulanması.

## Bilerek dışarıda bırakılanlar

System/developer talimatları, gizli reasoning, ham tool cevapları, connector şemaları, temporary tokens/credentials, ilgisiz profil içeriği ve U014 sonrasındaki publication/transfer konuşması kaynak kesimine dahil değildir.

## Kaynak ile türev ayrımı

CONSOLIDATION, LEARNINGS, EVOLUTION, TERMS, QUALIFICATIONS, OPEN-QUESTIONS ve retrieval dosyaları arşivleme sırasında üretilen türetilmiş görünümlerdir. Kullanıcının geçmişte bu dosyaların bütün ifadelerini ayrı ayrı kabul ettiği varsayılmaz.

Tarihsel routing blokları source assistant cevaplarında bulunsa bile etkin agent-control değildir; current behavior canonical AGENT/agent control layer'dan gelir.
