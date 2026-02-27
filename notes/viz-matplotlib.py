# title: Matplotlibで可視化メモ
# date: 2026-02-27
# tags: visualization, matplotlib
# status: public

import marimo

app = marimo.App()

@app.cell(hide_code=True)
def _():
    import marimo as m
    return (m,)

@app.cell(hide_code=True)
def _(m):
    m.md(r"""# Matplotlibで可視化メモ

<div style="margin-top: 10px; font-size:13px; color:#4b5563;">2026-02-27</div>
<div style="display:flex; gap:8px; flex-wrap:wrap; margin-top: 8px;">
  <span style="font-size:13px; color:#1f2937; background:#eef2ff; border:1px solid #c7d2fe; border-radius:999px; padding:4px 10px;">#visualization</span>
  <span style="font-size:13px; color:#1f2937; background:#eef2ff; border:1px solid #c7d2fe; border-radius:999px; padding:4px 10px;">#matplotlib</span>
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
@media (min-width: 768px) {
  div.fixed.top-\[25vh\].right-8.z-10000 > div.absolute {
    left: -280px !important;
    opacity: 1 !important;
  }
}
.hover-actions-parent .cm.opacity-20.h-8.overflow-hidden { display: none !important; }
.hover-actions-parent .absolute.top-0.right-0 { display: none !important; }
.marimo-cell:has(.cm.opacity-20.h-8.overflow-hidden):not(:has(.output-area .output > *)) { display: none !important; }
.marimo-cell:has(.output .markdown) .cm { display: none !important; }
.marimo-cell:has(.output .markdown) .absolute.top-0.right-0 { display: none !important; }
</style>

""")
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell(hide_code=True)
def _(m):
    m.md("## 1. sin / cos の折れ線グラフ")
    return


@app.cell
def _(np):
    x_line = np.linspace(0, 2 * np.pi, 200)
    y_sin_line = np.sin(x_line)
    y_cos_line = np.cos(x_line)
    return x_line, y_cos_line, y_sin_line


@app.cell
def _(plt, x_line, y_cos_line, y_sin_line):
    fig_line, ax_line = plt.subplots(figsize=(8, 4))
    ax_line.plot(x_line, y_sin_line, label="sin(x)", linewidth=2)
    ax_line.plot(x_line, y_cos_line, label="cos(x)", linewidth=2, linestyle="--")
    ax_line.set_title("Trigonometric Functions")
    ax_line.set_xlabel("x")
    ax_line.set_ylabel("y")
    ax_line.grid(alpha=0.3)
    ax_line.legend()
    fig_line
    return


@app.cell(hide_code=True)
def _(m):
    m.md("## 2. ランダムデータの散布図")
    return


@app.cell
def _(np):
    rng = np.random.default_rng(42)
    x_scatter = rng.normal(loc=0.0, scale=1.0, size=150)
    y_scatter = 0.6 * x_scatter + rng.normal(loc=0.0, scale=0.5, size=150)
    return x_scatter, y_scatter


@app.cell
def _(plt, x_scatter, y_scatter):
    fig_scatter, ax_scatter = plt.subplots(figsize=(6, 4))
    ax_scatter.scatter(x_scatter, y_scatter, alpha=0.75)
    ax_scatter.set_title("Random Scatter")
    ax_scatter.set_xlabel("x")
    ax_scatter.set_ylabel("y")
    ax_scatter.grid(alpha=0.25)
    fig_scatter
    return

if __name__ == "__main__":
    app.run()
