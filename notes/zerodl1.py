# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.19.10",
#     "pyzmq>=27.1.0",
# ]
# ///

# title: ゼロつく1を実装
# date: 2026-01-17
# tags: book, ゼロつく1
# status: public

import marimo

__generated_with = "0.19.11"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # ゼロつく1を実装

    <div style="color:#666; font-size: 0.95em; margin-top: 6px;">
      <span><b>Date:</b> 2026-01-17</span><br/>
      <span><b>Tags:</b> book / ゼロつく1</span>
    </div>

    ---
    """)
    return


@app.cell
def _():
    return


@app.cell
def _():
    print("hello")
    return


@app.cell
def _():
    a = 1
    b = 2
    a + b
    return


@app.cell
def _():
    import math
    math.cos(90)
    return


if __name__ == "__main__":
    app.run()
