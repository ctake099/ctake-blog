# title: はじめてのテスト記事
# date: 2026-02-27
# tags: test, demo
# status: public

import marimo

app = marimo.App()

@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)

@app.cell
def _(mo):
    mo.md(r"""# はじめてのテスト記事

<div style="margin-top: 10px; font-size:13px; color:#4b5563;">2026-02-27</div>
<div style="display:flex; gap:8px; flex-wrap:wrap; margin-top: 8px;">
  <span style="font-size:13px; color:#1f2937; background:#eef2ff; border:1px solid #c7d2fe; border-radius:999px; padding:4px 10px;">#test</span> <span style="font-size:13px; color:#1f2937; background:#eef2ff; border:1px solid #c7d2fe; border-radius:999px; padding:4px 10px;">#demo</span>
</div>
<a href="../index.html" style="
  display:inline-block;
  margin-top:10px;
  padding:8px 14px;
  border-radius:999px;
  border:1px solid #d0d7de;
  background:#f6f8fa;
  color:#111827;
  text-decoration:none;
  font-weight:600;
  font-size:14px;
">← トップページへ</a>

<style>
.hover-actions-parent .cm.opacity-20.h-8.overflow-hidden { display: none !important; }
.hover-actions-parent .absolute.top-0.right-0 { display: none !important; }
.marimo-cell:has(.cm.opacity-20.h-8.overflow-hidden):not(:has(.output-area .output > *)) { display: none !important; }
.marimo-cell:has(.output .markdown) .cm { display: none !important; }
.marimo-cell:has(.output .markdown) .absolute.top-0.right-0 { display: none !important; }
</style>

""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("## 1. 目的")
    return


@app.cell
def _():
    goal = "ビルドと公開の流れを確認する"
    print(goal)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("## 2. サンプル計算")
    return


@app.cell
def _():
    x = [1, 2, 3, 4]
    y = [n * n for n in x]
    y
    return

if __name__ == "__main__":
    app.run()
