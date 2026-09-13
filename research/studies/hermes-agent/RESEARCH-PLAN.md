# Hermes Agent — Araştırma planı

**v0.26 / 2026-09-13 — U13 yayımlı; Q58 kurulum/güncelleme kaynak araştırması başlangıcı.** [STATE](STATE.md) work/yetki, [METHOD](METHOD.md) yöntem, [MAP](CURRENT-RESEARCH-MAP.md) görünüm. Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a` / manifest0.21.0; current ürün hükmü değil.

## Güncel devir ve başlangıç kapısı

Kullanıcının “anladım. plana göre devam et. operasyonel sınırına kadar çalış.” talebi güncel repository planıyla birlikte yorumlandı. İlk main **93d6b14438802163ed3f542beded218e14cc51cf**, sohbetin son U12 açıklamasından ileriydi: U13/Q57 source ve seçki diagnostic zaten yayımlanmıştı. Q57 tekrarlanmadı. Eksik kalan final publication makbuzu **40a7f952f04b893b2dd0ffdb3df551adfca75c4a** ile uzlaştırıldı; actual main/ref, yalnız PUBLICATION değiştiğini gösteren compare ve yeni makbuz bölümü geri okundu. [U13 makbuzu](evidence/2026-09-13-delegation-reentry/PUBLICATION.md).

AGENT güncel main'den tam okundu; bu conversation'da tam okunmuş R01–R09 değişmeyen canonical sürümleri yeniden uygulandı. U13 STATE/INDEX/META/MAP/PLAN/OPEN-QUESTIONS/SOURCE-LEDGER, note28, A/B araştırması, SOURCES/SPEC/MANIFEST/NOT RUN ve kapsam değerlendirmesi tam geri kazanıldı. Exact eski D/N sonuçları için yeni bağımsız doğrulama iddiası yoktur; raw arşiv yeniden koşulmadı. METHOD ve research root da yeniden tam okundu. U04-A/B, U10–U12 ve dört synthesis değişmeyen aynı-conversation kaynakları/rotalarıyla korunur.

Bu başlangıç kaydı teknik bulgu değildir. Actual main/ref ve plan geri okunduktan sonra Q58-A başlayacak. **A:** pinned dağıtım/manifest/installer → kaynak ve bağımlılık kimliği → home/config/profile → komut/activation. **B:** yalnız A yayımlanıp geri okunduktan sonra gerçek updater/change/refusal/restart yolu; gerekiyorsa doğal küçük sınırda bölünür. Yayınlanmamış bir büyük dilim varken ikinci dilim açılmaz.

## Q58 — yetkili kaynak sorusu

HERMES kaynak/dağıtım paketi ve bağımlılıkları hangi zincirle kurulu komut, home/profile/config ve aktif runtime olur; kurulum/güncelleme bu kimlikleri ve kalıcı kullanıcı durumunu nasıl bağlar?

Başlangıç [STRUCTURE](inventory/STRUCTURE.md)'daki pinned root tree `f54f5e9d2682bf11f164de7b34ee10ec121b6434`. README, manifest/entrypoint ve onların gerçekten referans verdiği installer/updater dosyaları açılır; `scripts/` ve `apps/bootstrap-installer/` alternatifleri gerektiğinde. Mutable arama yalnız navigation; sonuçlar exact pin'e bağlanır. En az normal yol ile materially farklı update/refusal/interruption veya desktop/bootstrap yolu karşılaştırılır. Bütün platformlar için kota esaslı tam okuma yoktur.

Kaynak ref'i, release etiketi, indirilen/kurulan dosya, dependency çözümü, config/profile ve active process eşitlenmez. Yedekleme varlığı tam geri dönüş veya successful activation makbuzu değildir. Bunlar önceden doğru sayılan sonuçlar değil, kaynakla sınanacak ayrımlardır. Çıkış: normal install/activation ve bir değişim yolunda kimlik, etki, korunmuş durum, gerçek consumer ve tamamlanma sınırı kaynakla açıklanabilmeli.

Canlı installer/updater çalıştırma, servis başlatma, gerçek credential/home okuma, ürün/adoption veya upstream patch yoktur. Kaynakları yerelde indirip kimliklerini denetlemek yazılımı kurmak değildir; kaynak okuması davranış deneyi sayılmaz. Gerekirse diagnostic için exact nesne/oracle/çevre ve özgün kanıt ayrı tanımlanır.

## Geniş yön ve sonraki değerlendirme

[U13 kapsam gerekçesi](inventory/SCOPE-REVIEW-2026-09-13-U13.md) yürütme/devam/zaman/runtime/delegation/consumer omurgasının genişlediğini, F12 kurulum/değişim yaşamının ise henüz benzer açıklaması olmadığını kaydeder. F04 learning çekirdeği derindir; skill-ledger/backup/restore/sync/curator/quality eksikleri silinmez. Q58'in anlamlı birimi yayımlanınca F04 library lifecycle ve F12 eval/quality tekrar tartılır; final CORE veya dört-alan/mimari aşamasına otomatik geçilmez.

Q57'nin bütün fault matrisini bitirmek yeni aileye geçmenin ön koşulu değildir. Aynı küçük seam'i tekrar tekrar sınamakla geniş HERMES-native açıklama arasındaki denge korunur.

## Korunan residual'lar ve kapsam

Q57 manual parent fidelity, actual DB ack/claim expiry, CLI volatile queue/crash, TUI late scheduling/release/first request, adapter/API ve task-context fidelity açıktır. Q54 policy/child/context/workspace/summary/cancel; Q55 native binding/history; Q56 terminal/persistence/control; U10 Q49 full run_job/Q51 request-quality/Q52 detection-handling; Q40/Q42 DB/quiet/startup; Q47 timing/store; Q48/Q50 transport/cancel ve eski Q07/Q22/Q26/Q29/Q38 quality/fidelity/whole-worker sınırları korunur. Erteleme kapanış değildir; karşı kanıt veya güçlü reuse ilgili doğrulamayı yeniden açar.

Yalnız `research/studies/hermes-agent/**` ve CATALOG HERMES satırı. METHOD, notes01–28, U04–U13 özgün araştırma/kanıtları ve synthesis01–04 değiştirilmez; U13 publication uzlaştırması ayrı tarihsel kayıt olarak tamamlanmıştır. Foundation, context/Codex, agent-control, diğer studies, upstream, architecture/adoption ve izin/credential ayarları değişmez.

[Exact U13 planı](https://github.com/batuhanozgun/agentic-os-search/blob/93d6b14438802163ed3f542beded218e14cc51cf/research/studies/hermes-agent/RESEARCH-PLAN.md) opening/A/B sırasını ve [U12 planını](https://github.com/batuhanozgun/agentic-os-search/blob/74c5e3d1dcd260a1841c64dda5fb1d182f7bb299/research/studies/hermes-agent/RESEARCH-PLAN.md) korur. Kaynak→mekanizma→alt-sistem→ilişki→CORE→ayrı dört-alan değerlendirmesi; dosya/test sayısı tamamlanma yüzdesi değildir.
