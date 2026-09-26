# EXP-006 — history

Bu klasör **current çalışma yüzeyi değildir**.

Buradaki dosyalar, EXP-006 yaşayan çalışma sistemine geçmeden önceki büyük STATE / INDEX / WORK-MAP snapshot'larını tarihsel iz ve migration kanıtı olarak korur.

Kurallar:

- Normal cold-start sırasında okunmaz.
- İçlerindeki "current", "next", "authoritative" veya benzeri ifadeler snapshot'ın üretildiği tarihe aittir.
- Current phase, next responsibility veya rol modeli için bu klasörden karar çıkarılmaz.
- Current authority yolu: `../STATE.md → ../HANDOFF.md → ../WORK.md → ../ACTORS.md`.
- Tarihsel relative link'ler bugünkü dosya yapısında çalışmayabilir; snapshot'lar sırf bugünkü yapıya uysun diye yeniden yazılmaz.

Mevcut snapshot'lar:

- `2026-09-25-pre-work-system-INDEX.md`
- `2026-09-25-pre-work-system-STATE.md`
- `2026-09-25-pre-split-WORK-MAP.md`
