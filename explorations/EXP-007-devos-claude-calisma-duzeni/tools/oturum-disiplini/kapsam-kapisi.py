#!/usr/bin/env python3
"""EXP-007 PreToolUse kapısı: KAPSAM kapanmadan yapı kararı / DevOS dokümanı yazılmaz (DERSLER L5, L8).
Kapsanan yollar: Write, Edit, MultiEdit (file_path); Bash (komut metninde korunan yol);
GitHub MCP yazma araçları (girdide korunan yol). Kapsanmayan: başka oturumların yazması (F3 §5.1 uyarısı)."""
import json, sys, re, os
KAPSAM = "/home/user/agentic-os-search/explorations/EXP-007-devos-claude-calisma-duzeni/devos/okuma/KAPSAM.md"
KORUNAN = re.compile(r"devos/(MIMARI-KARARLAR\.md|DEVOS\.md|dokuman/)")
try:
    d = json.load(sys.stdin)
except Exception as e:
    print(f"kapsam-kapisi: girdi okunamadı ({e}); çağrı durduruldu, kapı bozuk olabilir.", file=sys.stderr)
    sys.exit(2)
tool = d.get("tool_name", "")
ti = d.get("tool_input") or {}
if tool in ("Write", "Edit", "MultiEdit"):
    hedef = str(ti.get("file_path", ""))
elif tool == "Bash":
    hedef = str(ti.get("command", ""))
elif tool.startswith("mcp__github__"):
    hedef = json.dumps(ti, ensure_ascii=False)
else:
    sys.exit(0)
if not KORUNAN.search(hedef):
    sys.exit(0)
if not os.path.exists(KAPSAM):
    print(f"DURDURULDU: {KAPSAM} yok; kapsam doğrulanamıyor.", file=sys.stderr)
    sys.exit(2)
acik = [l.strip() for l in open(KAPSAM, encoding="utf-8") if l.startswith("|") and re.search(r"SÜRÜYOR|BOŞLUK VAR|SIRADA", l)]
if acik:
    print(f"DURDURULDU (EXP-007 DERSLER L8, araç={tool}): KAPSAM kapanmadan yapı kararı ya da DevOS dokümanı yazılmaz; korunan yol bu çağrıda geçiyor. Açık satır sayısı: {len(acik)}. İlk üçü:\n" + "\n".join(a[:150] for a in acik[:3]), file=sys.stderr)
    sys.exit(2)
sys.exit(0)
