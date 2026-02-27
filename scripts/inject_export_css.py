from __future__ import annotations

from pathlib import Path

DOCS_DIR = Path("docs")

INJECT = """
<style id="ctake-export-overrides">
/* Hide hide_code code panes immediately to avoid flash on load */
.hover-actions-parent .cm.opacity-20.h-8.overflow-hidden { display: none !important; }
.hover-actions-parent .absolute.top-0.right-0 { display: none !important; }
.marimo-cell:has(.cm.opacity-20.h-8.overflow-hidden):not(:has(.output-area .output > *)) { display: none !important; }
/* Hide code for markdown-rendering cells at all times */
.marimo-cell:has(.output .markdown) .cm { display: none !important; }
.marimo-cell:has(.output .markdown) .absolute.top-0.right-0 { display: none !important; }
</style>
""".strip()


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if 'id="ctake-export-overrides"' in text:
        return False
    idx = text.find("</head>")
    if idx == -1:
        return False
    updated = text[:idx] + INJECT + "\n" + text[idx:]
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    patched = 0
    for html in DOCS_DIR.glob("*/index.html"):
        if patch_file(html):
            patched += 1
    print(f"Injected export CSS into {patched} notebook page(s)")


if __name__ == "__main__":
    main()
