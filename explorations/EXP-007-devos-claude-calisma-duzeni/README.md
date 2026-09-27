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

EXP-007, EXP-006'ya yazmaz. Oradaki "sıradaki" ifadeleri ve durma noktaları da EXP-007'yi yönetmez. EXP-006'dan neyin alınacağı P0'da, METHOD ile birlikte kararlaştırılır.

**EXP-006 ile bağlantı yoktur ([K-010](DECISIONS.md)).**
- ChatGPT, EXP-006'da ayrı ve bağımsız çalışır.
- Claude, konuyu baştan sona devralmış gibi çalışır. EXP-007 ve dalı Claude'un ana çalışma ortamıdır.
- EXP-006 yalnız faydalanmak için, isteğe bağlı okunur. Bu dalda EXP-006'nın eski sürümü durur. Güncel halini okumak için: `git fetch origin main` ve `git show origin/main:<yol>`.

## Dosya görevleri

| Yüzey | Tek işi |
|---|---|
| STATE.md | şu an, sıradaki iş, bekleyen kararlar, oturum ve ortam notları |
| DECISIONS.md | Batu'nun kararları, gereksinimleri ve açık sorular |
| sources/conversation/ | konuşma kaynakları, birebir |
| phases/P0-calisma-duzeni/ | P0 planı, görev tanımları, araştırma notları, taslaklar, eleştiriler |
| tools/ | ölçüm betikleri; şimdilik yalnız gerçek token kullanımı (`token-kullanimi.py`) |

Bu yapı geçicidir. P0'ın çıktısı olan metodoloji kabul edilince paketin yapısı ona göre genişletilir.

## Sınırlar
- Bu pakette şunlar değiştirilmez, yalnız okunur: EXP-006, EXP-001–005, Foundation, studies, concepts, kontrol katmanı (AGENT.md, `agent/`).
- Kontrol ve yapılandırma değişiklikleri (CLAUDE.md, `.claude/agents`, skills, hook'lar) Batu onaylamadan kurulmaz ([A-04](DECISIONS.md)).
- Git: EXP-007 ayrı dalda (`claude/hopeful-pascal-7bekcd`) yaşar ve main'e birleştirilmez (K-009). Dal yalnız bu klasöre dokunur.
