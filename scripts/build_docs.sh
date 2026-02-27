#!/usr/bin/env bash
set -euo pipefail

# ルートで実行される想定（study-notes/）
NOTES_DIR="notes"
DOCS_DIR="docs"

rm -rf "$DOCS_DIR"
mkdir -p "$DOCS_DIR"
touch "$DOCS_DIR/.nojekyll"

# notes/*.py を全部 export（出力先は docs/<filename>/）
shopt -s nullglob
for f in "$NOTES_DIR"/*.py; do
  name="$(basename "$f" .py)"
  rm -rf "$DOCS_DIR/$name"
  uv run marimo export html-wasm "$f" -o "$DOCS_DIR/$name" --mode run --show-code
done

# 不要ファイル削除（表示に不要）
find "$DOCS_DIR" -type f -name "CLAUDE.md" -delete

# ノートHTMLに共通CSSを先に注入して、hidden codeのちらつきを防ぐ
uv run python scripts/inject_export_css.py

# 一覧ページ生成
uv run python scripts/build_index.py

echo "Build done: $DOCS_DIR/"
