from __future__ import annotations

from pathlib import Path

DOCS_DIR = Path("docs")

INJECT_JS = r"""
<script>
(() => {
  const TARGET = "import marimo as mo";
  const CELL_SELECTORS = [
    "marimo-cell",
    "[data-testid='cell']",
    "[data-cell-id]",
    ".cell",
    ".notebook-cell",
  ];

  const hideCellForNode = (node) => {
    for (const selector of CELL_SELECTORS) {
      const cell = node.closest(selector);
      if (cell) {
        cell.style.display = "none";
        return true;
      }
    }
    return false;
  };

  const removeImportCell = () => {
    const nodes = document.querySelectorAll("code, pre, .cm-content, .cm-line");
    for (const node of nodes) {
      const text = (node.textContent || "").trim();
      if (text.includes(TARGET)) {
        if (hideCellForNode(node)) return true;
      }
    }
    return false;
  };

  if (removeImportCell()) return;
  const observer = new MutationObserver(() => {
    if (removeImportCell()) observer.disconnect();
  });
  observer.observe(document.documentElement, { childList: true, subtree: true });
  setTimeout(() => observer.disconnect(), 5000);
})();
</script>
"""


def patch_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "TARGET = \"import marimo as mo\"" in text:
        return False
    idx = text.rfind("</body>")
    if idx == -1:
        return False
    updated = text[:idx] + INJECT_JS + "\n" + text[idx:]
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    count = 0
    for html in DOCS_DIR.glob("*/index.html"):
        if patch_html(html):
            count += 1
    print(f"Postprocessed {count} exported notebook(s)")


if __name__ == "__main__":
    main()
