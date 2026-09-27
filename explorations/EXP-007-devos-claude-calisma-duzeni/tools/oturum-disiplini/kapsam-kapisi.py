#!/usr/bin/env python3
"""EXP-007 PreToolUse(Write|Edit) kapısı: KAPSAM kapanmadan yapı kararı / DevOS dokümanı yazılmaz (DERSLER L5, L8)."""
import json, sys, re, os
KAPSAM = "/home/user/agentic-os-search/explorations/EXP-007-devos-claude-calisma-duzeni/devos/okuma/KAPSAM.md"
KORUNAN = re.compile(r"/devos/(MIMARI-KARARLAR\.md|DEVOS\.md|dokuman/)")
try:
    d = json.load(sys.stdin)
except Exception as e:
    print(f"kapsam-kapisi: girdi okunamadı ({e}); çağrı durduruldu, kapı bozuk olabilir.", file=sys.stderr)
    sys.exit(2)
if d.get("tool_name") not in ("Write", "Edit", "MultiEdit"):
    sys.exit(0)
path = str((d.get("tool_input") or {}).get("file_path", ""))
if not KORUNAN.search(path):
    sys.exit(0)
if not os.path.exists(KAPSAM):
    print(f"DURDURULDU: {KAPSAM} yok; kapsam doğrulanamıyor.", file=sys.stderr)
    sys.exit(2)
acik = [l.strip() for l in open(KAPSAM, encoding="utf-8") if l.startswith("|") and re.search(r"SÜRÜYOR|BOŞLUK VAR|SIRADA", l)]
if acik:
    print("DURDURULDU (EXP-007 DERSLER L8): KAPSAM kapanmadan yapı kararı ya da DevOS dokümanı yazılmaz. Açık satırlar:\n" + "\n".join(a[:160] for a in acik), file=sys.stderr)
    sys.exit(2)
sys.exit(0)
