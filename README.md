# Study Notes（marimo + GitHub Pages）

このリポジトリは、学習メモを **marimo ノート（.py）** として管理し、`docs/` に **html-wasm** で書き出してブラウザで閲覧できるようにします。  
一覧ページ（検索・タグ・カード表示）は `scripts/build_index.py` が自動生成します。

---

## セットアップ（初回だけ）

uv を使って仮想環境を作り、必要なパッケージを入れます。

```bash
uv venv
uv pip install -U marimo
```
source .venv/bin/activate は不要です。以降は uv run ... で実行します。

⸻

いつもの流れ（上からこの順で）
	1.	新規ノート作成 → 2) 編集 → 3) public にする → 4) ビルド → 5) ローカル確認

1. 新しいノートを作る（テンプレ生成）

notes/ 配下にノートを作成します。ファイル名は slug（英数字など） になります。
```
uv run python scripts/new_note.py <slug> "<title>" -t tag1,tag2
```
例：
```
uv run python scripts/new_note.py zerodl1 "ゼロつく1を実装" -t book,ゼロつく1
```
生成例：
	•	notes/zerodl1.py
（同名があれば zerodl1-2.py のように枝番が付きます）

2. ノートを編集する（marimo UI）
```
uv run marimo edit notes/<slug>.py
```
例：
```
uv run marimo edit notes/zerodl1.py
```
ブラウザで開いたら、セルを追加して Markdown / コードを書きます。保存すると .py に反映されます。


⸻

公開/非公開の切り替え（status）

ノートファイル先頭のメタ情報で公開状態を管理します。
```
# status: draft
```

•	draft：一覧に出さない

•	public：一覧に出す

公開する場合は draft を public に変更します（marimo UIで開いたまま編集してOK）。

⸻

docs を生成する（ビルド）

docs/ を作り直し、各ノートを html-wasm に export して、一覧ページ docs/index.html を生成します。
```
./scripts/build_docs.sh
```

⸻

ローカルで確認する
```
uv run python -m http.server 8000 --directory docs
```

ブラウザで以下にアクセスします。
	•	一覧：http://localhost:8000/
	•	個別ノート：一覧のカードをクリック

