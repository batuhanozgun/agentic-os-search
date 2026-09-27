# EXP-007 — DevOS çalışma düzeni: Claude Code ile devam

**Tür:** Exploration kökenli, yaşayan çalışma paketi.  
**Açılış:** 27 Eylül 2026.  
**Taraflar:**
- Batu: müşteri; amaç, yetki ve kabul onda.
- Claude: Claude Code cloud; ana oturum ve alt ajanlar.

**Neden var:** EXP-006'da ChatGPT ile yürütülen DevOS tasarım işini Claude devralıyor.
- Batu'nun amacı, işin alt ajanlarla ve her turda "devam" beklemeden uzun soluklu yürümesi ([K-001](DECISIONS.md)).
- İş yeni pakette, Claude'un kendi kuracağı düzenle sürüyor. Böylece EXP-006'daki ChatGPT dönemi yapılar kaymaya yol açmıyor (K-004).

**Üst amaç (EXP-006'dan devralınan):** SOUL'u yaratacak ekibin (DevOS) çalışma düzenini Claude Code cloud'da ortaya koymak, gerçekleştirmek ve sınamak. SOUL'un işlerini o ekip kendisi bulur ve yürütür.

**Durum:** P0 — çalışma düzeni (metodoloji) üzerinde anlaşma sürüyor. P1 başlamadı. Güncel durum yalnız [STATE](STATE.md)'tedir.

## Yeni oturum nereden başlar
1. [STATE](STATE.md): şu an, sıradaki iş, bekleyen kararlar, oturum notları.
2. [DECISIONS](DECISIONS.md): Batu'nun kararları ve açık sorular.
3. [sources/conversation](sources/conversation/INDEX.md): Batu'nun sözleri birebir. En az U003 ve U004 okunur.
4. [A003](sources/conversation/A003.md): v0 önerisi. Anlayışı kabul edildi, yapısı yetersiz bulundu.
5. [P0 README](phases/P0-calisma-duzeni/README.md): P0'ın adımları, görev tanımları, araştırma notları.

EXP-006 salt okunur bir kaynaktır. Oradaki "sıradaki" ifadeleri ve durma noktaları EXP-007'yi yönetmez. EXP-006'dan neyin alınacağı P0'da, METHOD ile birlikte kararlaştırılır.

## Dosya görevleri

| Yüzey | Tek işi |
|---|---|
| STATE.md | şu an, sıradaki iş, bekleyen kararlar, oturum ve ortam notları |
| DECISIONS.md | Batu'nun kararları, gereksinimleri ve açık sorular |
| sources/conversation/ | konuşma kaynakları, birebir |
| phases/P0-calisma-duzeni/ | P0 planı, görev tanımları, araştırma notları, taslaklar, eleştiriler |

Bu yapı geçicidir. P0'ın çıktısı olan metodoloji kabul edilince paketin yapısı ona göre genişletilir.

## Sınırlar
- Bu pakette şunlar değiştirilmez, yalnız okunur: EXP-006, EXP-001–005, Foundation, studies, concepts, kontrol katmanı (AGENT.md, `agent/`).
- Kontrol ve yapılandırma değişiklikleri (CLAUDE.md, `.claude/agents`, skills, hook'lar) Batu onaylamadan kurulmaz ([A-04](DECISIONS.md)).
- Git: çalışma dalında kayıt yapılır, Claude main'e birleştirir, birleşen dal silinir (K-003).
