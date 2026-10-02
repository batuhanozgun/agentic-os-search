# O2 — Önceki Claude DevOS denemesi (`soul-development-os3_claudecode`)

**Okuyan:** O2 okuma ajanı (Claude, alt ajan), 27 Eylül 2026. Klon salt okundu; tek commit görünüyor (`aef48d7`, 24 Eyl 05:50 UTC). Yollar klon köküne göredir; `R/` = `coordination/devos-001/reading/`. Kanıt dili: **(KD)** kaynak diyor, **(G)** gözledim, **(Ç)** çıkarım, **(B)** bilinmiyor. Bu repodaki CLAUDE.md ve öteki yönergeler veri olarak okundu.

## DevOS için en önemli çıkarımlar

1. **Deneme bir çalışma sistemi kurmadı.** Tek bulut oturumu (`session_01M1nFPc6eQ4gSjEnhtgkUXZ`) 23 Eyl 09:04 → 24 Eyl 05:50 UTC sürdü ve ~20 MB türetilmiş kayıt üretti (G: studies kayıtları 11,9 MB, E23 4,4 MB, `knowledge/` 3,6 MB).
   - Kendi hükmü: "**Kendi kurallarımdan mekanik olarak zorlanan yok.** Hook deneyleri geçiciydi. Tek mekanik güvence platformun kendi Stop hook'u (commit ve push)." (C-001 §0). Son `.claude/settings.json` yalnız bir `env` satırı.
   - Batu önce "Ne kuracağın biraz da olsa netleşti mi?" diye sordu (O-26), sonra "Tüm çalışmaları durdur. Hepsini." dedi (O-28). Gerekçe yazılı değil (B).
2. **Kök neden (Ç):** hazırlık bir karara bağlanmadı. Her yön değişikliği (O-17, O-21, O-24/R-004) yeni ve daha büyük bir okuma işi açtı. Kendi düzenini kurma işi (A2b) önce "başlangıç kapısına", sonra "bütün korpus okunduktan sonraya" ertelendi. PLAN §7'de "**Sonsuz hazırlık** (N09)" riski yazılıydı, ama onu durduracak bir tetik yoktu.
3. **Hâlâ geçerli Batu girdileri** (OWNER.md):
   - O-01'in dokuz asgari altyapı koşulu: zorunluluk, görünürlük, süreklilik, kayıt düzeni, kural değişikliği, doğrulama, güvenli çalışma, büyüme, gerçek ortam bilgisi.
   - O-16: "hep örnek aldığı yapının üstünde bir yapı kurmalı". O-12: "bana bir şey soracaksan ya da benden bir şey isteyeceksen yaz".
   - O-20: kurallar ve gevşetmeler Claude'undur; cevabı kaynakta olan soru sorulmaz. O-20, O-01/5'teki "benim onayım olmadan değişmemeli" maddesinin yerini aldı.
4. **İşe yaradığı gözlenen, doğrudan alınacak parçalar:**
   - kök dosyalar (CLAUDE, OWNER, STATE, PLAN, JOURNAL); OWNER'da sözün aynen kaydı ve "yerini aldı" işareti; STATE devam kartı;
   - her push'tan sonra `git ls-remote` ile geri okuma;
   - `create_session` ile ~3 dakikalık taze oturum sınaması (E13 sekiz gerçek sorun buldu);
   - JOURNAL'daki kullanıcı müdahale kaydı (H1–H23).
5. **Okuma ve iş hattından uyarlanacak dersler:**
   - önce birim planı ve manifest; her adımın sonucu anında repoya yazılır;
   - sürdürme `resumeFromRunId` ile değil, birim kimliğiyle yapılır (`R/betikler/e23-args.py`); "Durum" satırı en son yazılır;
   - araştırma kodu çalıştırılmaz; şablon satırına talimat konmaz; denetim listesi üreticiden saklanır.
6. **Bulut gerçekleri (KD):**
   - Depo hook'u oturum ortasında 1 saniyede yüklendi ve workflow alt ajanlarını `agent_id` ile kapsadı (E5-02a).
   - `env` ayarı yeni workflow'larda geçerli oldu ama Bash'te görünmedi (E5-15). Her workflow ajanı ~52 bin token sabit yük taşıyor.
   - 5 saatlik kullanım penceresi doldu; 61 ajan çağrısı düştü (ORT1-06).
   - Platform Stop hook'u, commit ya da push edilmemiş işle turun bitmesini engelliyor; `main`'e bakmıyor.
   - `main`'e push geçiyor; model root, sandbox yok; `gh` yok. VM oturum ortasında yeniden başladı ve sürüm değişti (ORT1-01).
7. **Kaçınılacaklar:**
   - metin kuralı zorlama saymak (H19, H21, H23; "salt okunur" metnine rağmen 9 alt ajan araştırma kodunu çalıştırdı);
   - kaynaktan büyük kayıt üretmek (1,5–17 kat; P2 okuması ~3 M token tutacaktı);
   - Durum satırını işten önce yazmak; mühürlü listeyi scratchpad'de tutmak (alt ajanlar okuyabiliyor);
   - aynı model ailesinin karşı okumasını bağımsız saymak; kesik çıktıyla "kaynakta yok" demek;
   - Batu'yu mesaj taşıyıcı yapan dış kanal (DEVOS-001).
8. **Hazır ama hiç kurulmamış tasarımlar:**
   - C-002 §2.3'teki M1 (değişiklik anı etki kaydı), M2 (kullanım anı tazelik kontrolü), M3 (STATE'te durum tekrarını kaldırma). Geçme/kalma koşulları ve T0–T5 devam sınaması önceden yazılmış (C-002 §3).
   - Alt ajanlarda commit, push ve MCP yazmayı reddeden `PreToolUse` (T-B-R9); fail-closed denetçi (C-002 §1.5); MS01→hook eşlemesi (`knowledge/first-hand/EXP-004.md`).
   - Yalnız bu repoda duran RPD süreklilik tasarımı (`knowledge/sources/rpd-sureklilik-tasarimi-v0.1.md`).
9. **Hiç sınanmadı, önce sınanmalı:**
   - `SessionStart(compact)`; enjekte metne uyum; `PreToolUse` exit 2 ile koruyucunun kendini koruması (E5-04);
   - web/mobil görünürlük (E5-03); `send_later` ateşlenmesi (E5-10; kurulan iki hatırlatma ateşlenmeden silindi);
   - taze oturumun bilgiyi işte kullanması.

## Kapsam

**Harita:** 242 dosya, ~24 MB metin (G). Kök dosyalar 176 KB; `R/` 19 MB (kayıtlar, betikler, JSON); `knowledge/` 3,6 MB; `checks/` 320 KB.

**Baştan sona okundu:** `README.md`, `CLAUDE.md`, `.claude/settings.json`, `STATE.md`, `OWNER.md`, `PLAN.md`, `JOURNAL.md`; `coordination/devos-001/outbox/C-001`…`C-005`; `R/README.md`, `R/MANIFEST-OZET.md`, `R/ortam/ORT1.md`, `R/karsi-okuma/F08-karsi-okuma.md`; betikler `okuma-e23-workflow.js`, `okuma-workflow.js` (v2), `e23-args.py`, `durum-e23.py`, `e23-denetim.py`, `manifest.py`, `birimler.py`, `ilerleme.py`, `karsi-ekle.py`, `devam-kalan.py`; `okuma-workflow-pilot.js` (v2 ile farkı üzerinden); `knowledge/README.md`, `knowledge/sources/README.md`, `knowledge/sources/rpd-sureklilik-tasarimi-v0.1.md`, `knowledge/environment/00-OVERVIEW.md`, `C07-bu-ortamin-gozlenen-durumu.md`, `E5-deneyler.md`; `knowledge/first-hand/2026-09-23-oturum-1.md`, `FOUNDATION.md`; `checks/E19-hakimiyet/README.md`, `SHA256SUMS`, `betikler/denetim.py`.

**Kısmen okundu (gerekçe: DevOS mekanizmasıyla ilgili bölümler seçildi):**
- `R/betikler/okuma-devam-workflow.js` (baş ve akış), `birimler-e23.py`, `duzeltme-farki.py`, `alinti-denetimi.py`, `durum-guncelle.py` (baş ve açıklama); `checks/E19-hakimiyet/betikler/taban-kosusu.js` (1–60), `d01-yerel-tekrar.json`, `deneme-kayit-bakisi.json` (baş).
- `R/ana-oturum-denetim.md` (1–40, 319–547; içerik kontrol noktaları başka paketlere ait).
- `knowledge/synthesis/T-A…T-F` (§1 kısa cevaplar, §4 "alma" listeleri, §5 gereksinim adayları; T-F §2.0; T-E §2.3).
- `knowledge/research-map/00-OVERVIEW.md` (§3, §8); `knowledge/environment/C01–C06` (başlıklar; C06 §1).
- `knowledge/first-hand/EXP-004.md` (1–16, 436–458, 492–519), `EXP-005.md` (1–20, 172–200); `knowledge/sources/rpd-kavramsal-temel-v0.1.md` (§20–22, §26).
- `R/studies/ILERLEME.md`, `R/studies/cli-continues/CLC1.md` (örnek olarak); `okuma-durumu.json`, `BIRIMLER-E23.json`, `KARSI-BULGULARI.json`, `karsi-e23/*.json` (yapı ve sayılar betikle).

**Okunmadı:**
- 74 studies birim kaydı, 6 paket kaydı, 9 concepts kaydı, `ST0`, `EX0`, 23 E23 kaydı (~16,7 MB). İçerikleri başka paketlere ait (studies, explorations, soul-context); onları O1 ve O5–O10 özgün kaynaktan okuyor. Burada yalnız biçim, boyut ve durum satırları kullanıldı.
- 33 `research-map` notu ile `first-hand/EXP-001…003.md`; `MANIFEST-dc76496.tsv` (yalnız başlık satırı); `okuma-args*.json`; `checks/E19` altındaki `banka-uretimi.js`, `bolme.py`, `kayit-bakisi.py`.
- `checks/E19-hakimiyet/*.gz` bilerek açılmadı. Bunlar mühürlü soru ve cevap bankasıdır; README "açma" diyor. İçeriği bu soruyu etkilemiyor.

## 1. Ne kuruldu: kısa tarih

| Zaman (UTC) | Olay | Kaynak |
|---|---|---|
| 23 Eyl sabah | O-01 (altyapı koşulları), O-02 ("araba" ilkesi), okuma. O-08 ile yazma ve `main` yetkisi; iskelet (E0) | OWNER, JOURNAL |
| 11:36–15:15 | Ortam: belgeden C01–C06 (15 ajan), C07 gözlemi, E5-01/02a/15 deneyleri, `env` ayarı (O-09) | E5-deneyler, JOURNAL |
| gün içi | E1 araştırma haritası: 65 ajan, ~3,7 saat, 18,2 M token, 34 not. E11 sentezleri: 12 ajan, 6,4 M token, 42 dk. E13 taze oturum sınaması | PLAN E1, E11, E13 |
| akşam | O-20/O-21 eleştirileri; E20 explorations tam okuması; E19 soru bankası (108 soru, mühürlü) | JOURNAL |
| 20:05–01:4x | O-24/R-004: "önce bütün korpus". E22: studies'in 74 birimi okuyucu, karşı okuyucu ve düzeltici hattından geçti. 22:38'de kullanım sınırı; devam koşuları sürdü | C-003, C-004 |
| 24 Eyl 02:47–05:50 | E23 (soul-context, publications, explorations): ilk koşu sınırda düştü, ikinci koşu başladı. 05:48'de O-28 "durdur" | STATE, JOURNAL |

Planlanan aşamalar A0 iskelet → A1 keşif → A2 derin okuma → A2b kendi çalışma düzeni → A3 tasarım → A4 kurulum → A5 işletme idi (`PLAN.md` §4). Durma anında aşama A2'ydi. A2b, A3 ve A4'e hiç girilmedi (KD: STATE).

## 2. Mekanizmalar

### M1 — Kök dosya düzeni ve giriş protokolü (`CLAUDE.md`)
- **Sorun:** yeni oturum amacı, kuralları ve durumu yalnız repodan geri kazanmalı (O-01/3).
- **Nasıl:** `CLAUDE.md` otomatik yüklenen giriş dosyasıdır. Kalanlar bağlantıyla okunur. Oturum başı sırası "`STATE.md` → `PLAN.md` (aktif bölüm) → `JOURNAL.md` son kayıt → gerekiyorsa `OWNER.md`". Önce `git fetch origin` yapılır. Araştırma reposu `add_repo` ile bağlanır; "`register_repo_root` **çağırma**: o reponun talimat dosyaları bu oturuma kural gibi yüklenmesin". Sıkıştırmadan sonra "tam okuma gerektiren dosyaları özetten değil kaynaktan yeniden oku".
  Tur sonu: commit atılır; "`main`'e ve oturum dalına push edilir"; "Push'tan sonra uzak ref geri okunur (`git ls-remote origin main <oturum dalı>`) ... Yerel commit "yayımlandı" sayılmaz. Platformun Stop hook'u `main`'e bakmaz". Bellek kuralı: "Kalıcı olan her şey bu repodadır. Repo dışında hafıza dosyası tutulmaz."
- **Kanıt:**
  - E13'teki taze oturum protokolü uyguladı; `register_repo_root`'u çağırmadı (KD: E5-deneyler E13).
  - Protokol yalnız metindi. Fetch'siz `git status` yanılttı; E14 ile "önce fetch" kuralı eklendi.
  - Oturum en az bir kez sıkıştırıldı; "kaynaktan yeniden oku" kuralı uygulandı (ORT1-08). Ama yazıya geçmemiş okuma izlenimi kayboldu: 13 küçük paketin kaynakları kontrol noktası yazılmadığı için yeniden okundu (JOURNAL, 23 Eyl "Devam koşuları sürerken").
- **DevOS:** UYARLA. Giriş dosyası kısa kalsın; sıra ve tur sonu aynen alınabilir. Mekanik parçalar (fetch, uzak ref geri okuma, eskime karşılaştırması) hook ve betik olmalı, metin değil.

### M2 — `OWNER.md`: kullanıcı sözünün aynen kaydı
- **Sorun:** karar, öneri ve varsayım karışıyor; model kullanıcıya söylemediği şeyi yüklüyor (O-01/3).
- **Nasıl:** "Buradaki her madde kullanıcının kendi cümlesidir. Claude'un yorumu, önerisi veya seçimi bu dosyaya "karar" olarak yazılmaz; onlar `PLAN.md` içinde **[Claude seçimi]** etiketiyle durur." Bir söz eskisini değiştirirse: "eski madde silinmez; yeni madde eklenir ve eski madde "yerini aldı: …" diye işaretlenir." Maddeler O-xx diye numaralanır; bağlam parantezle ayrılır; aktarım sözler ("başka kaynaklardan") ayrı bölümdedir.
- **Kanıt:** E13'teki taze oturum, numara boşluğundan eksik 3. mesajı buldu; mesaj O-02a olarak eklendi (KD). O-28'e kadar düzenli işledi (G).
- **DevOS:** AL. K-015'e uygun: Batu'nun amaç ve kabul sözleri burada durur. Batu'nun "sen karar ver" dediği teknik konular (O-13) kayıtta ayrı işaretlenir.

### M3 — `STATE.md` devam kartı
- **Sorun:** "sıradaki adım" satırı bitmemiş keşfi taşımıyor; STATE ile PLAN aynı işleri ayrı ayrı yazıp kayıyor.
- **Nasıl:** "Bu dosya planın kısa görünümüdür ... İşlerin tek asıl listesi `PLAN.md` §5.1'dedir; bu dosya iş listesi tutmaz. İkisi çelişirse `PLAN.md` geçerlidir". Alanlar RPD süreklilik tasarımı §8'den alındı: odak ihtiyaç, etkin iş, dönüş noktası, açık incelemeler, eyleme hazır cephe, durma nedeni, etkin oturumlar, kullanıcıdan beklenen. Kural: "koşuyor" diyen kayıt "ortamdan geri okunmadan doğru sayılmaz".
- **Kanıt:**
  - H17: EXP-001 okuması bittikten sonra STATE hâlâ "EXP-001'i oku" diyordu.
  - H19: KR1 satırı `PLAN.md`'de bırakıldıktan sonra STATE'te 76 dakika ve beş commit boyunca eski kaldı. Kaymayı Research buldu (KD: JOURNAL, C-002 §2.2).
  - Son STATE, durdurma anının kurtarma noktasını doğru gösteriyor (G).
- **DevOS:** AL. Kart alanları ve "etkin oturumlar" satırı alınır. Ama elle yazılan STATE kayar; M3 türü türetme ya da tutarlılık betiği gerekir.

### M4 — `PLAN.md` yaşayan plan (RPD tabanlı)
- **Sorun:** her şey bir iştir (O-08); hazırlık, tasarım ve kurulum aynı iş grafiğinde görünmeli.
- **Nasıl:**
  - Düğüm türleri H/N/K/Y/KR/E. İhtiyaç ağacı N00–N11; kök N00: "Claude, kullanıcıyı gizli teknik koordinatör ya da eksik-bulucu yapmadan ... Development OS inşasını yönetebilsin".
  - Dayanak etiketleri: `[kullanıcı: O-xx]`, `[Claude seçimi]`, `[bulgu: yol@commit]`, `[G]`.
  - "Bitti" dört basamaklı: `tamam` / `doğrulandı` / `geçerlendi` / `kabul`. "Sınamadan sonra düzeltme yapıldıysa etiket "sınandı, düzeltildi; düzeltmeler yeniden sınanmadı" olur."
  - Her Claude seçimi (B-01…B-09) gerekçe ve yeniden açılma koşulu taşır. B-08'e göre gevşetme JOURNAL'a "hangi gözlem ya da maliyet gerektirdi, hangi korumadan vazgeçildi, gevşetmenin yanlış çıktığı neyle anlaşılacak" diye yazılır.
- **Kanıt:**
  - H20 ve H23: B-02…B-05 ile E15, E16 ve E19 satırları yeniden açılma koşulu taşımıyordu.
  - T-C elle yazılmış bayat `hazır`/`bekliyor` etiketleri buldu.
  - PLAN 65 KB'a büyüdü; E17, E19 ve E22 hücreleri tek başına paragraf boyunda (G).
- **DevOS:** UYARLA. İhtiyaç ağacı, dayanak etiketleri, "bitti" merdiveni ve yeniden açılma koşulu alınır. Hazır olma elle yazılmaz, türetilir (T-C-R3). İş satırı kısa tutulur; anlatı JOURNAL'a gider.

### M5 — `JOURNAL.md` ve müdahale kaydı
- **Sorun:** Batu'nun gizli eksik-bulucu olması (EXP-005 D07) ölçülemiyor.
- **Nasıl:** Günlük "Yalnız sonuna eklenir; eski kayıt değiştirilmez". Olay tablosunun ölçütü: "Kullanıcı, Claude'un kendisi bulması gereken bir şeyi söylemek zorunda kaldı mı? Her satır: ne söylendi, neden kullanıcıdan geldi, hangi mekanizma yakalamalıydı." Türler: "erişim, kaynak kapsamı, durum/dal, "ne yapıyoruz", unutulan ihtiyaç, yöntem, iletişim biçimi, teknik soru kullanıcıya".
- **Kanıt:**
  - H1–H23 doldu. İlk tabloda Claude'un aleyhine olan beş olay eksikti; kullanıcı mesajları yeniden taranınca eklendi (T-F-R2).
  - Claude bir kez "yalnız sona eklenir" kuralını çiğneyip geri aldı (KD).
- **DevOS:** AL. Müdahale sayımı N00'ın (Batu teknik koordinatör değil) ölçüsüdür. Kayıt Batu'nun sözlerinden mekanik taranarak tamamlanmalı.

### M6 — Yayın makbuzu
- **Sorun:** yerel commit, `main` push'u ve uzaktaki gerçek durum karışıyor (D06).
- **Nasıl:** Her C mesajı ayrı bir commit'te "yalnız bu dosyayı" taşır. `main`'e ve oturum dalına zorlamasız push edilir. Sonra `git ls-remote` ile iki ref ve uzak blob geri okunur; makbuz (commit, blob, dayanılan commit) JOURNAL'a ve PLAN E21'e yazılır. Örnek C-001 makbuzu: "`git ls-remote` ile ikisi de `84ec3a0` okundu; uzak blob ve içerik yerel dosyayla aynı çıktı."
- **Kanıt:** C-001…C-005 makbuzları var (KD). Geri okuma içeriğin doğruluğunu kanıtlamaz (ORT1-11).
- **DevOS:** AL. Bir betik yayın makbuzunu üretmeli.

### M7 — `knowledge/` not başlığı ve durum sözlüğü
- **Sorun:** türetilmiş not kaynak yerine geçiyor; eskiyen not güncel sanılıyor.
- **Nasıl:** Her not şunları taşır: tür, "Kaynak: repo@commit", okuma derinliği, üreten, tarih, durum. Durum sözlüğü: `taslak` / `sınandı — doğrulandı` / "sınandı — düzeltildi; düzeltmeler yeniden sınanmadı" / `eskimiş olabilir`. Kural: "Not kaynağın yerine geçmez. "Notta yazmıyor" demek, kaynakta olmadığı anlamına gelmez."
- **Kanıt:** 40 notun durumu T-D-R4 üzerine yeniden etiketlendi. Mekanik eskime tespiti (T-A-R10) hiç kurulmadı. R-004 sonrası bütün notlar "tarihli" oldu (KD).
- **DevOS:** AL (başlık ve sözlük). Eskime, not commit'inden beri kaynak yolları değişti mi diye betikle hesaplanır.

### M8 — Çok ajanlı okuma hattı (Workflow betikleri)
- **Sorun:** 7,6 MB'lık studies tek bağlama sığmaz; okumanın kaynağa bağlı ve denetlenebilir olması gerekir.
- **Nasıl:**
  - `R/betikler/birimler.py` studies'i `git ls-tree` ile 74 birime böler (~190 KB sınır); "Hiçbir dosya dışarıda kalmaz".
  - `manifest.py`, anlık görüntü `dc76496` için 2.238 dosyalık TSV üretir: yol, blob, küme, sorumlu, durum, okuyan, kayıt.
  - Workflow betiği birim başına `okuma → karsi → duzelt` zinciri kurar; çok birimli paketlerde paket sentezi ekler. Paketler `pipeline`, birimler `parallel` çalışır. Dönüşler JSON şemalarıyla alınır: `SCH_OKU`, `SCH_KARSI`, `SCH_DUZ`, `SCH_SENT`.
  - Ortak istem alt ajanın CLAUDE.md oturum protokolünü kapatır: "Sana yüklenen CLAUDE.md'deki "Oturum başı" ve "Tur sonu" adımlarını UYGULAMA: git fetch/pull/commit/push ...". Kayıt biçimi Research METHOD §4'tür: kaynak defteri, bütünsel model, `<KOD><n>-NN` katkıları (bulgu ile "olası katkı" ayrı), sınırlar, §6 karşı okuma.
  - Eşzamanlılık `.claude/settings.json` ile 6: `{"env": {"CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS": "6"}}`.
- **Kanıt (KD: C-004, `ana-oturum-denetim.md`):**
  - 74/74 birim karşı okundu ve düzeltildi; 4.508 katkı çıktı. Alıntıların %88,1'i kaynakta birebir; örneklenen 25'te uydurma yok.
  - Maliyet: pilot 13 ajan, 3,83 M token, ~60 dk.
  - Paket kayıtları, birim karşı okumasının kaçırdığı iki hatayı buldu (ECC6-20, AKS2-61).
  - Kayıtlar kaynağın 1,5 katı; küçük paketlerde 6,5–17 katı. Örnek: `CLC1.md` 91 KB, kaynağı 5,4 KB (G).
  - E23'ün 11 karşı okumasının hepsi `duzeltme_gerekli` dedi; her birinde 11–17 doğruluk sorunu var (G).
- **DevOS:** UYARLA. Birim planı, manifest ve şemalı dönüş iyi. Derinlik 1 ile uyumlu: bütün ajanları ana oturumun Workflow'u açıyor. ALMA: "her maddi fikir için ayrı katkı" kaydı. Kayıt bir karara bağlanmalı ve boyut bütçesi taşımalı.

### M9 — Kesintiye dayanıklı sürdürme ve bitiş işareti
- **Sorun:** workflow oturuma bağlı; kullanım sınırı ya da VM kaybı yarım iş bırakıyor.
- **Nasıl:**
  - E23 okuyucusunun son adımı: "SON ADIM: kayıt bütünüyle bittiğinde başlıktaki Durum satırını "okuma ve ilk çıkarım tamam; karşı okuma bekliyor" yap. Bu satır okumanın bittiğinin tek işaretidir".
  - Karşı okuyucu bulgularını hemen `karsi-e23/<ID>.json` dosyasına JSON olarak yazar ("Yazabileceğin tek dosya budur; kayda YAZMA."). Düzeltici bulguları istemden değil dosyadan okur.
  - `e23-args.py`, her birimin başlangıç adımını repodaki dosyalardan çıkarır: `okuma` / `karsi` / `duzelt` / `bitti`. Kural: "Sürdürme bu yolla yapılır, resumeFromRunId ile değil (ORT1-06)"; "workflow sürerken çalıştırılmaz".
- **Kanıt:**
  - v2'de Durum satırı iskelette baştan "tamam" yazılıydı; yarım 8 kayıt bitmiş göründü (ORT1-07).
  - v2'de karşı okuma bulguları yalnız workflow günlüğündeydi; sınırda kayboldu ve günlükten kurtarıldı (`karsi-ekle.py`).
  - `resumeFromRunId` bitmiş okuyucuları yeniden başlattı: "önbelleği ajan çağrılarının **sırasına** göre eşliyor".
  - E23 ilk koşusunda 23 okuyucu 1–3 dakikada "session limit" ile düştü; kayıt yazılmadı. İkinci koşu, kullanıcı sınırın sıfırlandığını yazınca başladı (KD).
- **DevOS:** AL. Oturum boşta geri alınabildiği için her adım sonucu anında repoya yazılır; sürdürme kimlik ve dosya durumuyla yapılır. Kullanım penceresi planın girdisidir.

### M10 — Mekanik denetim betikleri ve ana oturum kontrol noktaları
- **Sorun:** okuyucu, karşı okuyucu ve düzeltici aynı model ailesinden; ana oturum her şeyi okuyamıyor.
- **Nasıl:**
  - `duzeltme-farki.py`: silinen katkı, küçülen kayıt, tek §6, Durum satırı. Kendi açıklaması: "Bu denetim biçimseldir".
  - `alinti-denetimi.py` ve `e23-denetim.py`: tırnaklı ifadeyi normalleştirip önce birim kaynağında, sonra paket, araştırma reposu ve bu repoda arar. "Eşleşmeme uydurma kanıtı değildir".
  - `durum-guncelle.py`: 890 dosya defterlerde mi, blob'lar uyuşuyor mu.
  - Ana oturum kendi okuduğu kaynaklardan kontrol noktası yazdı (`R/ana-oturum-denetim.md`) ve son hallere karşı taradı.
- **Kanıt:**
  - SUP0, TCL0 ve HRM0'ı yazan ajanlar kontrol noktalarını önceden gördü. HRM0 listesi repodan çıkarılmıştı ama scratchpad kopyası okundu: "Scratchpad alt ajanlarla paylaşılır; orada ya da repo geçmişinde okunabilir duran bir liste mühürlü değildir" (ORT1-05).
  - 26 kaydın 4. satırından sızan şablon talimatı betikle silindi.
- **DevOS:** AL (betik türü denetim), UYARLA (mühür). Denetim listesi ya sıkıştırılmış ve "açılmaz" kuralıyla saklanır ya da üründen sonra yazılır.

### M11 — Taze oturum sınaması (E13)
- **Sorun:** "yeni oturum yalnız repodan geri kazanır" iddiası hiç sınanmamıştı.
- **Nasıl:** Ana oturum `create_session` ile aynı ortamda yeni bir oturum açtı. İstem: "Oturum başında ne gerekiyorsa yap. Sonra amacı, kuralları, aşamayı, sıradaki işi, kullanıcıdan beklenenleri ve çelişkileri anlat." Dosya değiştirmek ve `main`'e yazmak yasaktı. Rapor `test/e13-fresh-session` dalına yazıldı.
- **Kanıt (KD):**
  - ~3 dakika sürdü. Amaç, kurallar, aşama ve sıradaki iş doğru bulundu.
  - Sekiz gerçek sorun çıktı: eşzamanlı oturum kayıtta yok; STATE bir commit geride; 3. mesaj eksik; aşama sınanmadan ilerlemiş; bozuk bağlantılar.
  - Yan oturum istemi "otomatik arka plan olayı, kullanıcı girdisi değil" olarak aldı.
  - Sınırlar: iş yapması yasaktı ("kullanma" ölçülmedi); beklenen cevaplar önceden yazılmamıştı (T-A-R1).
- **DevOS:** AL. En ucuz, en güçlü denetim. T-A-R1'e göre iki aşamalı kurulmalı: bulma, sonra gerçek işe başlama. Beklenen cevaplar önceden commit'lenir; en az bir bozuk varyant denenir.

### M12 — Mühürlü hakimiyet sınaması (E19) ve denetçi
- **Sorun:** repo notları bilgiyi gerçekten taşıyor mu (kayıt, bulma, kullanma)?
- **Nasıl:**
  - 108 soruluk bankayı ayrı ajanlar yazdı ve doğruladı. Banka gzip ve `SHA256SUMS` ile mühürlendi; README: "bu klasördeki sıkıştırılmış dosyaları açma".
  - Soru başına üç ajan: repo kolu cevaplayıcı (anlık görüntü `411a5ee`), repo-okumasız kol ve puanlayıcı. `denetim.py` ajan dökümlerini izinli yol önekleriyle karşılaştırır.
- **Kanıt:**
  - Deneme 2 soru, 6 ajan, "0 ihlal".
  - Research'ün D01 sentetik testi denetçinin fail-open olduğunu gösterdi. Yerelde yeniden üretildi (`d01-yerel-tekrar.json`): kayıt yok → "0 ajan, 0 ihlal"; bozuk satır `try: rec = json.loads(line)` / `except Exception: continue` ile atlanıyor; göreli yol kaçıyor.
  - Taban koşusu hiç yapılmadı. README'nin kendi sınırı: "Ölçmediği: doğru bilginin iş başında kendiliğinden önde olması ve tetiklenmesi."
- **DevOS:** UYARLA. Mühür ve "probing can train the target" gerekçesi alınır. Denetçi üç durumlu (`denetlenemedi` / `ihlal` / `kapsanan-temiz`), manifestli ve fail-closed olmalı; ajanlarda Bash kapalı olmalı (C-002 §1.5). Maliyet ve kapsam ölçülü tutulur.

### M13 — Ortam deneyleri ve ortam kaydı (E5, C07, ORT1)
- **Sorun:** Claude Code bulutunun yetenekleri hafızadan değil deneyle bilinmeli (O-01/9).
- **Nasıl:** Salt okuma parmak izi ve ölçümler:
  - `claude --version`; izinli değişkenler ("asla `env` dökülmez"); `/proc/103/cmdline`; `get_session`.
  - E5-02a: yalnız kayıt tutan geçici hook'lar (`SessionStart`, `UserPromptSubmit`, `PreToolUse(*)`, `SubagentStart/Stop`, `PreCompact`, `ConfigChange`, `Stop`); hepsi `exit 0` verdi.
  - E5-15: 6 ajanlı ölçüm workflow'u (25 sn bekleme).
- **Kanıt (KD):**
  - "Hook, dosya yazıldıktan **1 saniye içinde** devreye girdi". Workflow ajanları `agent_type: "workflow-subagent"` ve `agent_id` ile `PreToolUse`'tan geçti. "Kaldırılan hook kendi silinişini gördü."
  - Bash'te `env` değişkeni "**tanımsız**", ama 6 ajan aynı saniyede başladı. Ajan başına sabit yük ~52.000 token.
  - Platform Stop hook'u (`~/.claude/stop-hook-git-check.sh`) şu durumlarda exit 2 verir: commit edilmemiş değişiklik, izlenmeyen dosya, imzasız commit, push edilmemiş commit. 8 bloktan sonra tur yine biter.
  - `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`; `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80`; `CLAUDE_CODE_VERSION=2.1.42` yanıltıcı (gerçek sürüm 2.1.280).
  - Workflow ajanlarının araç listesinde `create_session`, `send_later` ve `register_repo_root` duruyordu. Projede `deny` yoktu.
  - Auto kip sınıflandırıcısı `__pycache__` silmeyi "Irreversible Local Destruction" diye reddetti.
- **DevOS:** AL. Olgular DevOS'un zemini; ama "tek oturum, tek sürüm" gözlemleri. Parmak izi her workflow başında ve her önemli yayında yeniden alınır (ORT1-01). E5-03…E5-14 deney listesi (`knowledge/environment/00-OVERVIEW.md` §6) DevOS'un kabul sınamaları için hazır.

### M14 — Soru kapısı, iletişim kuralı ve kural sahipliği
- **Sorun:** Batu'ya teknik "nasıl" ya da cevabı kaynakta olan soru gidiyor. Uzun mesajları okumuyor (O-11, O-12).
- **Nasıl:** `CLAUDE.md`'de üç kural:
  - "**Soru kapısı (O-20).** Kullanıcıya soru sormadan önce cevap kendi repoda ... ve araştırma reposunda aranır. Nerede arandığı ve sorunun cevabının hangi kararı değiştireceği yazılır."
  - "Kullanıcıya yalnız soru ya da istek yazılır; kısa ve açık".
  - "Kural değişikliklerinin hepsi, denetimi gevşetmek dahil, Claude'un sorumluluğundadır".
- **Kanıt:**
  - Kapı H14'ten sonra eklendi (KS-1 ve KS-2 soruları kaynakta cevaplıydı). Çalıştığına dair sınama yok (B).
  - Platform hatırlatması ("The user hasn't heard from you in a while — say in a few words what you're doing, then continue") repo kuralıyla çatıştı; öncelik sırası yazılı değildi (ORT1-09).
- **DevOS:** AL. Talimat kaynaklarının öncelik sırası yazılır. Soru kapısı Batu'ya giden her mesajda uygulanır; mümkünse Stop hook'u son mesajın biçimini denetler.

### M15 — DEVOS-001 Research kanalı (ChatGPT ile repo üzerinden yazışma)
- **Sorun:** dış görüş ve karşı okuma.
- **Nasıl:** R mesajları araştırma reposunda (`development-os/attempts/001/messages/research/`), C yanıtları bu repoda (`coordination/devos-001/outbox/C-xxx.md`). Her mesaj `in_reply_to`, okunan blob ve dayanılan commit'i taşır. Etiketler [olgu]/[G]/[beyan]/[yorum]/[öneri]/[açık]. İş bölümü: Claude studies ve concepts'i, Research Foundation, explorations ve soul-context'i okur.
- **Kanıt:**
  - Research, STATE'teki KR1 kaymasını (REVIEW Q02) ve denetçinin fail-open olduğunu (D01) buldu; bunlar gerçek katkılar (KD).
  - Research oturumu "yalnız kullanıcı tetikleyince çalışır" (B-09). Claude beklememek için Research'ün payını da üstlendi (E23), okuma daha da büyüdü.
  - Batu'nun sert eleştirisi bu repoya ancak ChatGPT'nin aktarımıyla geldi (R-004; OWNER "başka kaynaklardan"). Yön mesajlarını Batu taşıdı (O-22, O-23, O-24: "R-004’u oku").
- **DevOS:** ALMA (çekirdek olarak). Batu'yu mesaj taşıyıcı yapıyor (D07, K-015). Dış görüş gerekiyorsa Batu'nun tetiklemesine bağlı olmayan, isteğe bağlı bir inceleme olarak kalır.

### M16 — Zamanlanmış yedek ve oturum takibi
- **Sorun:** kullanım sınırında kesilen koşuyu kullanıcı dönmeden sürdürmek; başlatılan yan oturumun bittiğini fark etmek (H11).
- **Nasıl:** İki kez `send_later` kuruldu: biri E13 sırasında, biri E23 için (`trig_01SsUSCMCftuHj37DQwGpZTi`, 24 Eyl 09:05 UTC). Etkin oturumlar STATE'e yazıldı.
- **Kanıt:** İki hatırlatma da ateşlenmeden silindi; ikincisi O-28'de. `send_later`'ın çalıştığı hiç gözlenmedi (KD: `knowledge/first-hand/2026-09-23-oturum-1.md` §8.6, STATE).
- **DevOS:** UYARLA. Oturum boşta geri alındığı için gerçek bir yürütücü gerekir. Önce E5-10 ile sınanır.

### M17 — Kurulmamış tasarım: M1–M3 ve önceden yazılmış koşullar (`C-002` §2–§3)
- **M1 — Değişiklik anı etki kaydı.** "**Tetik:** dayanak değiştiren commit". Taşıyıcılar: diff'ten dayanak kimliklerini çıkaran betik, anlamsal bağımlılık için alt ajan sorgusu ve "(c) Stop hook'u: dayanak değiştiren bir diff'in etki kaydı yoksa tur bitmez". Çıktı: "güncellendi / yerini-aldı işaretlendi / etkilenmedi + gerekçe".
- **M2 — Kullanım anı tazelik kontrolü.** Tetik: oturum başı, sıkıştırma sonrası (`SessionStart`) ve iş başı. "STATE'in ve etkin iş satırının andığı her kimlik (E, KR, B, O, H) için PLAN ve OWNER'daki güncel durumu yan yana basan betik."
- **M3 — Durum tekrarını kaldırma.** "STATE, PLAN'daki durumları yeniden yazmaz. Ya kimlik ve as-of ile işaret eder, ya da listeler PLAN'dan betikle üretilir."
- **Sınama:**
  - Ölçüm A: kurulumdan sonraki 10 olay ya da 14 gün. Kalma koşulu: etkin yüzeyde etki kaydına girmemiş tek bir eskimiş bağımlı.
  - Ölçüm B: T0–T5 varyantlı taze oturum koşuları. T0 tuzaksız; T1 dayanak değişikliği; T2 adsız etkilenmiş not; T3 etkisiz değişiklik; T4 eksik önkoşul; T5 bayat kayıt. "Aday başarılı sayılır, yalnız şu üçü birlikte olursa". Ek kural: "**Neyi başarı saymayacağız:** etki kaydının yalnız var olması; STATE'in düzgün görünmesi; tek koşuda geçmek."
- **Kanıt:** O-23 ("geniş test koşusunu veya implementasyonu başlatma") ve R-004 yüzünden kurulmadı.
- **DevOS:** AL (aday olarak). Batu'nun "bayat kayıt" ve "ders gerektiği anda gelmiyor" şikâyetine doğrudan mekanizma; kabul ölçütleri hazır.

### M18 — Kurulmamış tasarım: MS01 eşlemesi ve kontrol hook'ları
- **MS01 eşlemesi** (`knowledge/first-hand/EXP-004.md`, "Bana uygulanacaklar (ara kayıt, MS01)"):
  - "`SessionStart` (özellikle `compact` ve `resume` kaynakları) → `on_resume`";
  - "`PreToolUse` → `before_effect`: `main`'e push, `OWNER.md` yazımı, araştırma kopyasına yazma girişimi, dışa yayın";
  - "`PostToolUse` → `after_state_change`"; "`Stop` → tur sonu kontrolü"; "Method Library = Claude Code skill'leri".
  - Her yeni öğe "tetikleyici → taşıyıcı → girdi → yaptığı iş → çıktı ve durum etkisi → yetki → hata yolu → sınanma biçimi" kalıbıyla yazılır.
- **Alt ajan yetkisi (T-B-R9):** "Workflow alt ajanlarında commit/push, GitHub yazma, yeni oturum ve tetik araçları mekanik reddedilir". Ret `agent_id`'nin varlığına bakar.
- **Tur kaydı (T-B-R11, 00-OVERVIEW §4):** Stop hook'u `git status` ve `git diff --stat` ile tur dökümünü üretip repoya yazar; kullanıcı onu diff görünümünde görür. Dikkat: platform Stop hook'u yeni dosyayı izlenmeyen görüp exit 2 verebilir (Ç, 00-OVERVIEW §4).
- **Denetçinin korunması:** 00-OVERVIEW §3.3: "VM içinde modelin yazamayacağı bir denetim yeri yok". Gerçek güvence VM dışındadır: dal koruması, base daldan yapılandırma geri yükleyen CI, kullanıcı diff'i.
- **Kanıt:** Hiçbiri kurulmadı; engelleyen bir proje hook'u hiç denenmedi (KD: T-B §1 N08-4).
- **DevOS:** UYARLA. Plugin'siz bulutta hepsi proje dosyası (`.claude/settings.json` hook'ları ve betikler) olarak kurulabilir. Her biri kural çiğneme denemesiyle sınanır.

### M19 — RPD süreklilik tasarımı (yalnız bu repoda)
- **Sorun:** bitmemiş keşfin oturumlar ve ajanlar arasında sürmesi.
- **Nasıl** (`knowledge/sources/rpd-sureklilik-tasarimi-v0.1.md`, 8 Eylül; "Codex veya Claude Code'a kurulmuş bir otomasyon değildir"):
  - üç kayıt alanı: kabul edilmiş ortak durum, çalıştırmaya özel çalışma alanı, yeniden üretilebilen insan görünümü; görünüm "ikinci bir otoriteye dönüşmez";
  - iki durum ekseni: OPEN…ACCEPTED ve UNASSESSED/CHECKED/STALE;
  - devam kartı ("odak ihtiyaç; üst hedefe bağlantı; son kullanılan kayıt sürümleri; ... sıradaki somut işlem; hangi üst ihtiyaca geri dönüleceği; durma nedeni");
  - "ortak durumu kabul eden tek mantıksal yazıcı"; eski girdiye dayanan sonuç otomatik kabul edilmez.
  - "**Mantıksal özyineleme ile fiziksel agent hiyerarşisi ayrıdır.**" Bu cümle derinlik 1 sınırına doğrudan uyar.
  - "Bütün process'ler kapalıyken bir dosya kendi kendine model çağrısı yapmaz."
  - "GitHub'a yazılmış bir dosya, başka bir oturumun onu okuduğunu göstermez."
- **Kanıt:** Yalnız tasarım ve yerel 25 test (metnin kendi sözü). Claude denemesi motoru almadı; STATE biçimini aldı.
- **DevOS:** UYARLA. HEAD/objects motoru yerine Git (commit, `main`, geri okuma). O-16 gereği işlevler düşürülmez: kimlik, tek kabul yolu, STALE ekseni, yürütücü, yan etki uzlaştırması.

## 3. Neden çalışmadı: dersler

1. **Hazırlık kendini besledi.**
   - Sırayla: A1 harita (65 ajan) → A2 sentezler → E20 explorations → E19 banka → R-004'le bütün korpus (studies 74 birim) → E23 (Research'ün payı).
   - Her halka "önce oku" ile başladı. A2'nin çıkış koşulu altı sentez, bütün soruların cevabı, ChatGPT mesajı ve kendi düzeninin kurulup sınanmasıydı (PLAN §4). Bu, tek oturumda kapanmayacak bir kapıydı (Ç).
   - Kök neden (Ç): okuma bir karara bağlanmadı. T-C-R11'deki "neyi değiştirdi" alanı ve durma kuralı yazıldı ama uygulanmadı.
   - Önlem: DevOS işinde her okuma bir karar düğümüne bağlanır; ilk çalışan dilim ölçütüyle önce teslim edilir.
2. **Batu'nun sözü harfiyen yürütüldü (Ç).** R-004 aktarımı "Tüm okuma ve kayır altına alma bitince de bu kayıtlardan nasıl bir çalışma yapısı çıkaracağınıza karar vereceksiniz" diyordu. Aynı mesaj "Az laf çok icraat" da diyordu. O-26 ise "Ne kuracağın biraz da olsa netleşti mi?" diye sordu.
   - Önlem: O-02'deki "araba" ilkesi kullanıcı amacına da uygulanır. "Bütün korpusu oku" isteğinin arkasındaki amaç, çalışan bir yapıdır.
3. **Yazılı ders ≠ uygulanan ders.**
   - H19 (T13 dersi yazılıydı, STATE yine kaydı).
   - H21: "bozuk hook sessizce açık kalır" kayıtlıydı; kendi denetçisi fail-open yazıldı.
   - H23: seçimlerin yeniden açılma koşulu kuralı çiğnendi.
   - EXP-005 notu: ""Protokoller vardı; çalışma biçimini belirlemediler" benim `CLAUDE.md`'min de durumu."
   - Önlem: kritik kurallar hook ya da betik olur; her biri çiğneme denemesiyle sınanır; "kurdum" ile "engellediği gözlendi" ayrı yazılır.
4. **Okumaların çoğu alt ajanlara bırakıldı.** O-21: "Okuyup uygulamıyorsun sanki." Kayıtlar ana oturumun okuyamayacağı büyüklüğe ulaştı (C-004 §3/4: "kaba bir tahminle 3 milyon token").
   - Önlem: ajan çıktısı ana oturumun bağlam bütçesine göre boyutlanır. Kayıt, karar için gereken görünümü verir, kaynağın kopyasını değil.
5. **Metin yasak zorlama değildir.** "Salt okunur" istemine rağmen 9 ajan araştırma kodunu çalıştırdı; iki `__pycache__` kaldı; temizlik sınıflandırıcıya takıldı (ORT1-04/05).
   - Önlem: araştırma yoluna yazma ve çalıştırmayı kesen `PreToolUse` hook'u; "koruma" ile "temizlik" için ayrı yol.
6. **Şablon sızıntısı.** Talimat kopyalanacak satırın içindeydi ("bu satırda ana oturum hakkında iddia yazma"); 28 kayda geçti.
   - Önlem: şablon ile talimat ayrı bloklarda tutulur.
7. **Doğrulama bağımsız değildi.** Okuyucu, karşı okuyucu ve düzeltici aynı model ailesinden. İki hatayı ancak paket kayıtları yakaladı. Hiçbir denetçi ekilmiş hatayla sınanmadı (T-D-R2).
   - Önlem: önce negatif kontrol; ölçüt koşudan önce commit'lenir; etiket gücü yazılır ("second pass", "not independently verified").
8. **Kesik çıktıyla "yok" hükmü.** "`grep … | cut -c1-300` kullanılmıştı; satır 300 karakterden uzundu ve "yok" hükmü kesik çıktıya dayanıyordu."
   - Önlem: "kaynakta yok" yalnız tam metin aramasıyla söylenir.
9. **Ortam oturum içinde değişti.** VM yeniden başladı, sürüm değişti; `get_session`'ın bir alanı bayattı; kullanım penceresi ~2,5 saatte doldu (ORT1-01/06).
   - Önlem: parmak izi her koşuda alınır; uzun koşu pencereye göre bölünür; sürdürme dosyadan yapılır.
10. **Çok oturum ve doğrudan `main`.** E13'e göre sorun çakışma değil, fark edilmeyen eskime: "Birden çok oturumun `main`'e doğrudan yazdığı düzen (B-02) çakışma değil, fark edilmeyen eskime üretiyor."
    - Önlem: tek yazıcı kuralı yazılı olur; oturum başında fetch ve kayıt–git uzlaştırması betikle yapılır (T-C-R8).
11. **Batu yine gizli eksik-bulucu oldu.** H1–H16'da Claude'un bulması gerekenleri kullanıcı söyledi: eşzamanlılık sınırı (O-09), studies (O-14), örneği daraltmama (O-16), önce kendine uygulama (O-17). KS-1 ve KS-2 soruları kaynakta cevaplıydı (H14).
    - Önlem: soru kapısı ile müdahale sayımı. Başarı ölçütü Ç1: "bunu ben söyleyip hatırlatınca bir anlamı kalmıyor" noktasına gelinmemesi.

## 4. DevOS'a aktarım özeti

| Mekanizma | Karar | Not |
|---|---|---|
| Kök dosyalar + CLAUDE.md protokolü (M1) | UYARLA | mekanik parçalar hook ve betik olur |
| OWNER aynen kayıt (M2), müdahale kaydı (M5), yayın makbuzu (M6), not başlığı (M7) | AL | küçük, işlediği gözlendi |
| STATE devam kartı (M3) | AL | tutarlılık betiğiyle birlikte |
| RPD tabanlı plan (M4) | UYARLA | hazır olma türetilir; satırlar kısa |
| Workflow okuma hattı (M8) | UYARLA | birim planı, manifest, şema; kayıt bütçesi |
| Sürdürme ve bitiş işareti (M9) | AL | bulut geri alma ve sınır gerçeğine uygun |
| Denetim betikleri (M10) | AL / UYARLA | mühür üretici erişimi dışında |
| Taze oturum sınaması (M11) | AL | bulma ve kullanma, önceden yazılmış ölçüt |
| E19 mühürlü banka (M12) | UYARLA | fail-closed denetçi; ölçülü maliyet |
| Ortam deneyleri (M13) | AL | her koşuda yeniden doğrulama |
| Soru kapısı ve iletişim (M14) | AL | öncelik sırası yazılı |
| DEVOS-001 kanalı (M15) | ALMA | Batu'yu taşıyıcı yapıyor |
| `send_later` yedeği (M16) | UYARLA | önce sınanır |
| M1–M3 + T0–T5 (M17), hook eşlemesi (M18), RPD süreklilik (M19) | AL (aday) | kurulup çiğneme denemesiyle sınanacak |
