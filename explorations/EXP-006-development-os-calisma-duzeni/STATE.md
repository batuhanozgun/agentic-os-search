# EXP-006 — STATE

**Durum:** AÇIK / uzun soluklu DevOS tasarım çalışması.  
**Güncelleme:** 27 Eylül 2026, P4 ilk teknik tercih ve fiziksel çalışma alanı taslağı.  
**Üst amaç:** Claude Code cloud ortamında SOUL'u geliştirecek ekibin çalışma düzenini ortaya koymak.  
**Current:** **P4 INITIAL TECHNICAL BASELINE / CONDITIONAL DESIGN / NOT DEPLOYED.** Kullanıcının P3 devir sonucundan sonraki “devam et” yönü P4'ü açtı. Teknik başlangıç tercihi yapıldı; hedef Claude'da doğrulanmış veya kullanıcıca benimsenmiş nihai mimari değildir. **P4 AÇIK; P5/P6 BAŞLAMADI.**  
**Üst harita:** [WORK — master plan v1.4](WORK.md). P1→P2↔P3→P4→P5→P6 sırası korunur.

## Sabit sınırlar

- Gerçek SOUL işlerini kurulacak ekip keşfeder, planlar ve yürütür. Assistant ekibin düzenini tasarlar; hazır SOUL backlog'u seçmez.
- Claude Code cloud hedef Environment'dır. Birincil belgeler P4'te hedefli tazelendi; hedef hesap/VM'nin araç, izin, erişim ve devam davranışı henüz görülmedi.
- K1 talep→çalışma→yanıt→kullanım; K2 rutin rol geçişinde Batu'nun tetikleyici olmamasıdır. Başlatma/yeniden başlatma, gerçek müdahale, yetki ve kabul mümkündür; sınırsız gözetimsizlik hedef değildir.
- D021: İçerik sahibi anlamı ve gerekçeyi; çalışma alanı tarafı yer, statü, kaynak/sürüm bağı, bulunabilirlik, bakım, devir ve yeniden kullanımı taşır. Düzen görevlisi ürün kararının yerine geçmez.
- Kanon/v2/ECC/Hermes/Gas Town/Beads bütün olarak alınmaz. Research agent-control dosyaları DevOS'a otomatik talimat olarak aktarılmaz.

## Devralınan zemin

SOUL hedefi→B1–B9→R1–R25/M1–M9→S1-01–17→F1–F8→P1–P6 bağı korunur. B haritası gerçek SOUL iş sırası değildir. S1-17 CLOSURE-READY / CANDIDATE; kullanıcı kapanışı veya çalışan sistem kabulü değildir. S1-16 kaynak-tamlığı sınırı S1-17 §7'dedir.

[ACTORS](ACTORS.md) ve [P2-01](work/P2-01-named-role-contracts.md) ilk rol/sözleşme tabanı; [P3-01 v0.5](work/P3-01-work-information-discussion.md) G/Y koordinasyonu/güvencesi, D021 bakım karşılığı ve H1–H6 gereksinim devridir. P3 kavramsal tasarım devrine hazır olarak kullanılır; devam izni bütün ayrıntılara kullanıcı kabulü değildir. P2'yi tek başına son runtime kadrosu sayma.

[P1-01](work/P1-01-claude-cloud-environment-map.md) tarihsel kaynak haritasını ve Q01–Q06'yı korur. P4'ün yük taşıyan güncel kaynak tazelemesi P4-01 §8'dedir; eski P1 cümlesi actual kurulum kanıtı değildir.

## P4 ilk teknik tasarım

**Tek ayrıntı yüzeyi:** [P4-01 — cloud çalışma biçimi ve fiziksel alan](work/P4-01-cloud-runtime-and-workspace-design.md).

**Başlangıç tercihi:** Bir ana Y/DevOS İşletim Koordinatörü oturumu + adlandırılmış ve mesajlaşabilen özel alt ajanlar. G/SOUL Geliştirme Koordinatörü ayrı görevlendirme; G/Y incelemeleri ayrı bağlamlar. Takımlar başlangıçta zorunlu değil, ihtiyaç/gerçek davranış gerekçelendirirse yeniden karşılaştırılacak alternatif.

- Rol amacı/araç sınırı `.claude/agents/` tanımlarında; ortak kısa giriş `CLAUDE.md`; yürürlüğe alınmış yöntemler skill olarak. Aynı rol metninin iki authoritative kopyası kurulmaz.
- Bir operasyon deposunda ayrı `soul/` ve `devos/` alanları tercih edildi. İş/karar/dayanak/deneme/kütüphane kayıtları ürünle ilişkilidir; Research ayrı salt-okur kaynak olarak bağlanacaktır. Operasyon reposu henüz seçilmedi veya açılmadı.
- Üreticiler özel çalışma kopyalarında aday değişiklik üretir; aynı current branch'e yayın tek kontrollü yoldan sıralı yürür. Ana Y bu yolu işletir, içerik hükmünü üstlenmez. Bu tercih bütün yazarları DR07'ye toplamaz.
- Native mesajlar iletişim taşıyıcısı; kalıcı Work/request/consumer bağı Git kayıtlarında. Var olan rol doğrudan mesaj alabilir; eksik rol Y tarafından etkinleştirilir. Her mesaj iki koordinatörden onay istemez.
- Dayanıklı devam noktası izinli cloud çalışma branch'ine doğrulanmış checkpoint'tir; yalnız yerel worktree veya auto-memory değildir. Her ara rol geçişinde main merge'i/kullanıcı komutu gerekmez.

**Yük taşıyan açık:** Worktree ve Git beklenen-temel kontrolü tek başına yetki duvarı değildir. Shell, paylaşılan Git alanı, API/MCP veya kontrol dosyası yoluyla koruma aşılabilir. Hedefte yazma/yayın sınırı ve eski görevliden gelen çıktı fiilen korunmadan güvenli paralel mutasyon iddiası kurulmaz. Gerekiyorsa salt-okur uzmanlar + daha dar mutasyon kanalı tercih edilir; H3/H5 düşürülmez.

## Kanıt ve yapılmayanlar

Resmî Claude/Git kaynaklarının ilgili bölümleri yeniden okundu. Dar yerel Git probe'unda beklenen eski SHA ile ikinci stale güncelleme reddedildi; eski SHA koşulu olmadan aynı ref değiştirilebildi. Bu, korunmuş yayın yolunun gereğini gösterir; hedef Claude veya güvenlik sınırının çalıştığını göstermez. Gözlem kapsamı P4-01 §8'de.

Canlı Claude oturumu, ajan iletişim denemesi, hedef izin/sandbox testi, VM restore veya yayın timeout'u yapılmadı. P4'ün koşullu tercihi P4'ün tamamlandığı değildir. P5 rol/skill/hook dosyaları üretilmedi; başka repo değiştirilmedi.

## Current next responsibility

**Bu tur sonuç:** H1–H6'ya bağlı çalışma topolojisi, rol allocation yaklaşımı, fiziksel dosya/klasör yerleşimi, çağrı/devir ve kontrollü yayın için bütünlüklü ilk teknik tasarım. Kullanıcıya kısa sonuç ve gerçek açıkları ver; P3 örneklerini yeniden anlatma.

**Sıradaki bütünlüklü P4 işi:** Bu seçime göre rol→araç→okuma/yazma/yayın yetki matrisini ve hedef cloud kabul denemesi paketini tamamlamak. Tek paket tanım yükleme, A→B→A iletişim/tüketim, checkpoint/yeniden giriş ve doğrudan/dolaylı eski-yazıcı karşı vakalarını kapsar. Gerçek hedef erişimi/çalıştırma kanıtı gereken yerde açıkça ayrılır; olmayan kabiliyeti varsayarak P5'e geçilmez.

P4 devamı, teknik başlangıç tercihini kullanıcıca kabul edilmiş yapmaz. Kaynak veya hedef gözlemi tercihi değiştirirse gerekçeli alternatif/ilgili P2/P3 dönüşü açılır; yeni genel audit veya tüm rol taxonomy'sini tekrar kurma yoktur.

## Fresh-session yolu

AGENT ve gerekli kontroller→[INDEX](INDEX.md)→STATE→[HANDOFF](HANDOFF.md)→[WORK](WORK.md)→[DECISIONS](DECISIONS.md)→[ACTORS](ACTORS.md)→[U002](sources/U002-cloud-plan-and-autonomy.md)→[P1-01](work/P1-01-claude-cloud-environment-map.md)→[P2-01](work/P2-01-named-role-contracts.md)→[P3-01](work/P3-01-work-information-discussion.md)→[P4-01](work/P4-01-cloud-runtime-and-workspace-design.md) tam okunur. Aynı konuşmadaki tam unchanged içerik korunabilir; sonra yalnız aktif sorunun kaynağına inilir.

Eski P dosyalarının geçmiş next/not-started ifadeleri bu current sırayı yönetmez. P2 tabanı, P3 kavramsal devir, D021 kabulü ve P4 koşullu teknik tercihi ayrı tutulur. Kısa sunum küçük çalışma birimi değildir.
