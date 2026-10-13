#!/usr/bin/env python3
"""Собирает index.html: вставляет граф из data/metro.json в src/app.html."""
from pathlib import Path

root = Path(__file__).parent
app = (root / "src" / "app.html").read_text(encoding="utf-8")
data = (root / "data" / "metro.json").read_text(encoding="utf-8").strip().replace("</", "<\\/")
marker = "/*DATA*/null"
assert marker in app, "в src/app.html нет метки /*DATA*/null"
(root / "index.html").write_text(app.replace(marker, data), encoding="utf-8")
print("index.html собран")
