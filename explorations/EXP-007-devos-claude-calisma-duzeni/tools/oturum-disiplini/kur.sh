#!/bin/bash
# EXP-007 ana oturum disiplin hook'larını bu makineye kurar (kullanıcı düzeyi, ~/.claude).
# Makine geri alınınca ~/.claude silinir; yeni oturum bu betiği bir kez çalıştırır.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/exp007
cp "$D"/oturum-hatirlat.sh "$D"/ajan-standart-kapisi.py "$D"/kapsam-kapisi.py ~/.claude/exp007/
chmod +x ~/.claude/exp007/*
if [ -f ~/.claude/settings.json ] && ! cmp -s "$D/settings.json" ~/.claude/settings.json; then
  cp ~/.claude/settings.json ~/.claude/settings.json.yedek.$(date +%s)
fi
cp "$D/settings.json" ~/.claude/settings.json
# Bozma testleri: her kapı bilerek tetiklenir.
echo '{"tool_name":"Agent","tool_input":{"prompt":"x"}}' | ~/.claude/exp007/ajan-standart-kapisi.py 2>/dev/null && { echo "HATA: ajan kapısı durdurmadı"; exit 1; } || true
echo 'bozuk' | ~/.claude/exp007/ajan-standart-kapisi.py 2>/dev/null && { echo "HATA: ajan kapısı bozuk girdide açık kaldı"; exit 1; } || true
echo "kuruldu ve bozma testleri geçti"
