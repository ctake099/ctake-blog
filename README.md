# ctake099 Blog (marimo + GitHub Pages)

このリポジトリは、`notes/*.py` の marimo ノートを `docs/` にエクスポートして GitHub Pages で公開します。


## 1. 新規ブログ記事を作る

```bash
python3 scripts/new_note.py <slug> "<title>" -t tag1,tag2
```

例:

```bash
python3 scripts/new_note.py cnn-note "CNNメモ" -t ml,vision,python
```

生成先:

- `notes/<slug>.py`

## 2. 記事を編集する

```bash
uv run marimo edit notes/<slug>.py
```

## 3. 公開設定にする

`notes/<slug>.py` の先頭メタを以下に変更:

```python
# status: public
```

- `draft` は一覧に出ません
- `public` は一覧に出ます

## 4. サイトをビルドする

```bash
bash scripts/build_docs.sh
```

これで以下が更新されます:

- `docs/<slug>/index.html`（記事ページ）
- `docs/index.html`（トップ一覧）

## 5. ローカルで確認する

```bash
python3 -m http.server 8765 --directory docs
```

ブラウザ:

- トップ: `http://127.0.0.1:8765/index.html`
- 記事: トップからクリック

## 6. GitHubへ反映（公開更新）

```bash
git add .
git commit -m "Add note: <slug>"
git push
```

GitHub Pages (設定済み前提):

- Branch: `main`
- Folder: `/docs`

公開URL:

- `https://ctake099.github.io/ctake-blog/`

## よく使うワンセット

```bash
python3 scripts/new_note.py <slug> "<title>" -t tag1,tag2
uv run marimo edit notes/<slug>.py
bash scripts/build_docs.sh
git add . && git commit -m "Update <slug>" && git push
```

## 補足: `notes/zerodl1.py` について

このファイルはサンプル記事として使っているため、以下のUI調整が入っています。

- ヘッダー（タイトル下の日時・タグ表示）
- `← トップページへ` ボタン
- marimoの `hide_code` セルを見せないためのCSS

同じ見た目を新規記事でも使いたい場合は、`scripts/new_note.py` のテンプレートを基準にしてください。
