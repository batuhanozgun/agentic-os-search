# DevOS okuma turu — kapsam listesi

Ana oturum bu listeyi tutar. Bir notun kapsamında boşluk kalırsa kapatma ajanı gönderilir. Bütün satırlar kapanmadan yapı kararına geçilmez. Durum işaretleri: TAMAM / BOŞLUK VAR → kapatıcı / SÜRÜYOR.

| Kaynak kümesi | Not | Durum | Boşluk ve kapatıcı |
|---|---|---|---|
| Ana oturumun kendi okumaları | O0 | TAMAM | — |
| development-os, soul-context | O1 | SÜRÜYOR | — |
| Önceki Claude DevOS reposu | O2 | BOŞLUK VAR | PLAN ve JOURNAL'ın tamamı, knowledge sentezleri, RPD, C-002 → G6 |
| keel, oyun2 | O3 | BOŞLUK VAR | file-guard.sh, sevk.sh, yardımcı dosyalar, ROL.md'ler, testler → G1 |
| loopinance-claude-code | O4 | BOŞLUK VAR | 11 workflow betiği, bekci.sh testleri, 73 setup handoff'u, Audit raporları, tutanaklar; ürün kanonunun yapısı ve harness'in onu nasıl yönettiği → G7 |
| ECC (ilk, sığ okuma) | O5 | YERİNE GEÇİYOR | Yerine O5a–O5d geçer |
| ECC study, birinci yarı | O5a | TAMAM | Notlar 29–56 O5b'de. E08'in ham prompt gövdeleri tek tek okunmadı: gövdeler probe girdileri; mekanizma ve sonuçları notta. |
| ECC study, ikinci yarı | O5b | SÜRÜYOR | — |
| ECC repo: ajanlar, komutlar, kurulum | O5c | SÜRÜYOR | — |
| ECC repo: skill'ler, hook'lar, öğrenme | O5d | BOŞLUK VAR | 25 orkestrasyon ve bellek skill'i, memory-vault, oturum kütüphaneleri ve testler okunmadı → O5e |
| ECC orkestrasyon ve bellek katmanı, testler | O5e | SÜRÜYOR | — |
| Hermes, superpowers, gstack, mattpocock | O6 | BOŞLUK VAR | okunmayan notlar ve upstream'ler → G2 |
| Bellek ve bağlam studies | O7 | BOŞLUK VAR | 6 paketin upstream'i, R09, EXP-003 → G3 |
| Harness ve döngü studies | O8 | BOŞLUK VAR | 3 upstream → G4 |
| Orkestrasyon ve iş grafı studies | O9 | BOŞLUK VAR | beads upstream, ERPNext, public-apis → G4 |
| Foundation ve explorations | O10 | BOŞLUK VAR | Foundation → F1–F4; explorations → G5 |
| Foundation 03: bilgi ve iş | F1 | SÜRÜYOR | — |
| Foundation 03: aktörler ve ortam | F2 | TAMAM | 224 dosyanın hepsi okundu |
| Foundation 05, 08, 04, 06, 07 | F3 | SÜRÜYOR | — |
| Foundation 01, 02, history | F4 | SÜRÜYOR | Yer açılınca başlatıldı (O13 bitti). |
| Kapatıcılar G1–G7 | G1–G7 | SÜRÜYOR | — |
| Claude Code platformu | O11 | BOŞLUK VAR | Ajan "KAPSAM BÖLÜNMELİ" dedi: env-vars, settings, tools, commands, cli, remote-control ve başka sayfalar tam okunmadı → O11b, O11c |
| Platform: zorlama katmanı belgeleri | O11b | SÜRÜYOR | — |
| Platform: taşıyıcı katman belgeleri | O11c | SÜRÜYOR | — |
| os-architect | O12 | BOŞLUK VAR | 131 dosyanın hepsi okundu; git geçmişi (eski KARARLAR, 1,2 MB'lık silinmiş Araştırmalar/) okunmadı → O12b |
| os-architect git geçmişi | O12b | SÜRÜYOR | — |
| GitHub çerçeveleri | O13 | BOŞLUK VAR | Ajan "KAPSAM BÖLÜNMELİ" dedi: depoların yalnız mekanizmayı taşıyan dosyaları okundu. arxiv, letta.com, docs.langchain.com ve roocode belgeleri ağ politikası yüzünden kapalı. Kapatıcılar: O13a, O13b, O13c. |
| Codex ve Letta belleği (kod ve belge) | O13a | SÜRÜYOR | — |
| Backlog.md ve Task Master (kod) | O13b | SÜRÜYOR | — |
| OpenHands, Goose, Magentic-One | O13c | SÜRÜYOR | — |
| Akademik kaynaklar | O14 | ORTAM ENGELİ | Ajan "KAPSAM BÖLÜNMELİ" dedi. Ağ politikası arxiv.org, openreview.net, aclanthology.org, proceedings.*, huggingface.co, semanticscholar.org ve metr.org'u kapatıyor. Tam metin yalnız Who&When ve LoCoMo'da okundu. Öbürlerinde resmi repo kodu okundu; sayılar arama özetinden geliyor ve notta [AÖ] diye işaretli. **Tetik:** Batu ağ iznini açarsa O14b, notun §0.4 listesini okur. Batu'ya bilgi verildi; yapı kararında [AÖ] sayılar yük taşımaz. |
| Anthropic ve Claude Code çerçeveleri | O15 | BOŞLUK VAR | Ajan "KAPSAM BÖLÜNMELİ" dedi: claude-flow, claude-code-templates, BMAD ve SuperClaude'un çoğu; awesome-claude-code'da bağlanan çerçeveler okunmadı; claude.dev ağ politikası yüzünden kapalı → O15b, O15c |
| BMAD ve SuperClaude | O15b | **SIRADA** | 20 ajan sınırı |
| claude-flow, templates, awesome-claude-code | O15c | **SIRADA** | 20 ajan sınırı |
| Architect-3'ün os-architect deneyimi (Batu'nun yapıştırması, U022) | O16 | TAMAM | Ana oturum okudu; O12 ile karşılaştırılacak |

**Kabul kuralı:** Her notun kapsam bölümü ana oturumca okunur. "Okunmadı" diye kalan her kalemin ya bir kapatıcısı ya da "içerik konu dışı" gerekçesi olur; ikinci durumda gerekçe dosya açıldıktan sonra yazılmış olmalıdır. Bitmeyen kalem, yapı kararını bekletir.

**Ağ sınırı (27 Eylül, gözlem):** Bu ortamın ağ politikası şu adreslere izin vermiyor (kabukta `curl` 000; ajanlar da aynısını bildirdi): arxiv.org, export.arxiv.org, ar5iv.labs.arxiv.org, huggingface.co, api.semanticscholar.org, openreview.net, paperswithcode.com, letta.com, docs.langchain.com. Açık olanlar: github.com (git), raw.githubusercontent.com, anthropic.com, code.claude.com. Akademik kaynaklar GitHub üzerinden okunuyor; okunamayanlar notlarda "erişilemedi" diye yazılıyor. Batu'ya bilgi verildi: ortam ayarlarında bu adresler izin listesine eklenebilir.
