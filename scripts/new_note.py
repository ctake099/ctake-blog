from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

TEMPLATE = """# title: {title}
# date: {today}
# tags: {tags}
# status: draft

import marimo

app = marimo.App()

@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)

@app.cell
def _(mo):
    mo.md(r\"\"\"# {title}

<div style=\"margin-top: 10px; font-size:13px; color:#4b5563;\">{today}</div>
<div style=\"display:flex; gap:8px; flex-wrap:wrap; margin-top: 8px;\">
  {tags_chips_html}
</div>

<style>
.hover-actions-parent .cm.opacity-20.h-8.overflow-hidden {{ display: none !important; }}
.hover-actions-parent .absolute.top-0.right-0 {{ display: none !important; }}
.marimo-cell:has(.cm.opacity-20.h-8.overflow-hidden):not(:has(.output-area .output > *)) {{ display: none !important; }}
.marimo-cell:has(.output .markdown) .cm {{ display: none !important; }}
.marimo-cell:has(.output .markdown) .absolute.top-0.right-0 {{ display: none !important; }}
</style>

\"\"\")
    return

if __name__ == \"__main__\":
    app.run()
"""

def clean_slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9._-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "note"

def find_available_path(out_dir: Path, base: str) -> Path:
    p = out_dir / f"{base}.py"
    if not p.exists():
        return p
    i = 2
    while True:
        p2 = out_dir / f"{base}-{i}.py"
        if not p2.exists():
            return p2
        i += 1

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="new_note.py",
        description='Usage: new_note.py <slug> "<title>" -t tag1,tag2',
    )
    parser.add_argument("slug", help="file slug, e.g. zerotsuku1, mnist-min")
    parser.add_argument("title", help='note title (required). Use quotes if needed.')
    parser.add_argument("-t", "--tags", default="", help="comma-separated tags, e.g. book,math")
    parser.add_argument("--dir", default="notes", help="directory to create note in (default: notes)")
    args = parser.parse_args()

    slug = clean_slug(args.slug)
    title = args.title.strip()
    if not title:
        raise SystemExit("Error: title is required and must be non-empty.")

    tags_list = [t.strip() for t in args.tags.split(",") if t.strip()]
    tags = ", ".join(tags_list)
    tags_chips_html = " ".join(
        [
            f'<span style="font-size:13px; color:#1f2937; background:#eef2ff; border:1px solid #c7d2fe; border-radius:999px; padding:4px 10px;">#{t}</span>'
            for t in tags_list
        ]
    )
    today = date.today().isoformat()

    out_dir = Path(args.dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    path = find_available_path(out_dir, slug)

    path.write_text(
        TEMPLATE.format(
            title=title,
            today=today,
            tags=tags,
            tags_chips_html=tags_chips_html,
        ),
        encoding="utf-8",
    )
    print(path)

if __name__ == "__main__":
    main()
