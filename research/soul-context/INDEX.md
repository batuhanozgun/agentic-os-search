# SOUL Context — INDEX

Bu dosya retrieval router'dır; agent-control, araştırma sonucu veya hedef repository'nin canlı durum otoritesi değildir. Güncel cross-project yön [STATE](STATE.md)'ten alınır.

## Güncel Claude Code hazırlığı

`STATE.md` → [CC-DEVOS-PREP / WORK](current/claude-code-devos-preparation/WORK.md) → [OWNER-CONTEXT](current/claude-code-devos-preparation/OWNER-CONTEXT.md) → [SOURCE-REGISTER](current/claude-code-devos-preparation/SOURCE-REGISTER.md) → [CLAUDE-TASK-01](current/claude-code-devos-preparation/CLAUDE-TASK-01.md).

WORK ayrıntılı hazırlık ve gönderim durumunu taşır. Yeni görevin hazırlanması, iletilmesi, Claude'un devralması, runtime koşuları ve Development OS inşasına hazır olması farklı olaylardır. `_02` yetkisi/mimarisi/kanıtı bu hedefe miras değildir. Source-REGISTER'daki okuma derinliği korunur; özet veya dosya adı tam kaynak sayılmaz.

## Konuya göre geri çağırma

| Soru | İlk yol | Derinlik ve sınır |
|---|---|---|
| Claude'a şimdi ne gönderilecek; ne gerçekleşti? | Güncel STATE → WORK | Exact görev ve varsa gerçek target response/ref; otomatik gönderim varsayılmaz |
| Kullanıcının hazırlık ve kapsam beklentisi | OWNER-CONTEXT | Özgün kullanıcı ifadeleri; Research yorumu ayrı |
| RPD'nin tamamı ve kaynaklarına erişim | SOURCE-REGISTER → `../studies/recursive-prerequisite-discovery/` | Özgün iki kaynak ve araştırma kaydı ayrı; eksik byte özetle tamamlanmaz |
| Mesleki standart, entelektüel taban ve süreç dersleri | `../../explorations/CATALOG.md` | Seçilen EXP'nin STATE/INDEX → özgün diyalog/eser; birikim mimari kabulü değil |
| Araştırmadan ne yararlanılacak? | `../soul-foundations/STATE.md` ve current reuse yolu; `../studies/CATALOG.md` | İhtiyaç → ilgili kaynak → seçenek/karar/kanıta katkı; corpus hazır reçete değil |
| SOUL Research neden var; ürün ve geliştirme ayrımı | `evidence/CONTEXT-SYNTHESIS.md` | `evidence/transition-to-soul.md`, `repos/soul/README.md`; güncel niyet yeni kullanıcı yönüyle birlikte |
| Research / Development / Production sınırı | STATE → `evidence/research-architecture-boundary.md` | İlgili hedefin kendi gerçek durumu ayrıca okunur |
| 8 Eylül `_02` görev/devir ayrıntısı | STATE'in tarihsel exact sürüm bağlantısı | O görevde gönderilmiş exact REVIEW ve ek kimlikleri; yeni Claude grant'ı değil |
| 22 Eylül iptal edilen girişim | EXP-005 STATE → lessons → source conversation | Eski görev belgesi tarihsel eser; tekrar yürütülmez |
| Eski bootstrap / coordinator / S1–G1 tarihi | Aşağıdaki korunmuş index ve Git STATE tarihçesi | `current/briefs/`, `current/reviews/`, `current/DEVELOPMENT-OS-BOOTSTRAP.md`; current yetki yerine geçmez |
| KEEL / OS Architect / predecessor kanıtı | `repos/os-architect/README.md`, `repos/keel/README.md`, `repos/keel-research/README.md` | Claim için exact kaynak; tarihsel test gerçek yeniden koşu değildir |
| Erken yerel model fikirleri | `exploratory/README.md` | LOCAL / PROVISIONAL, varsayılan çalışma metodu değil |

## Tarihsel navigasyonun korunması

Önceki ayrıntılı Codex rota tablosu [cee38caa exact INDEX](https://github.com/batuhanozgun/agentic-os-search/blob/cee38caa970399fa4bf267cb484331e0c50164c9/research/soul-context/INDEX.md)'te korunur; blob `4568f0a28dfd3e80c5f69e82d5f15f89a2864f92`. Eski brief/review/evidence dosyaları değiştirilmedi. Tarihsel "güncel" sözcüğü ve hazırlanmış görev, yeni hedefe yetki aktarmaz.

## Yüzeylerin rolleri

`repos/` source ledgers; `evidence/` kaynak-bağlı context sentezleri; `current/` sınırlı cross-project hazırlık/devir ve tarihli görevler; `exploratory/` yerel geçici fikirlerdir. Hangi görev gerçekten current, hangisi yalnız hazırlanmış veya tarihsel, STATE ve onun yönlendirdiği iş kaydından belirlenir. Belge varlığı, hash eşleşmesi, aktarım ve davranış yeterliği tek hükme birleştirilmez.
