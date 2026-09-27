#!/bin/bash
# EXP-007 süreklilik hook'u (SessionStart: compact|resume). Çıktı bağlama eklenir.
R=/home/user/agentic-os-search/explorations/EXP-007-devos-claude-calisma-duzeni
echo "=== EXP-007 SÜREKLİLİK (hook) ==="
echo "Bağlam sıkıştırıldı ya da oturum sürdürüldü. Özet yetmez; şu dosyaları ŞİMDİ baştan sona oku: $R/STATE.md · $R/DERSLER.md · $R/devos/okuma/KAPSAM.md · $R/devos/okuma/STANDART.md"
echo "Kurallar: Batu'ya soru yok (K-014..K-017). KAPSAM kapanmadan yapı kararı yok. Her alt ajan görev metni STANDART.md'yi ilk okuma olarak taşır. SIRADA olan kalemleri başlat."
echo "--- STATE şu anki adım ---"
grep -m1 '^\*\*Şu anki adım:\*\*' "$R/STATE.md" 2>/dev/null
echo "--- KAPSAM: kapanmamış satırlar ---"
grep -E '^\|' "$R/devos/okuma/KAPSAM.md" 2>/dev/null | grep -E 'SÜRÜYOR|BOŞLUK VAR|SIRADA' | cut -c1-200
echo "=== son ==="
exit 0
