# htmx-project

FastAPI + htmx + SQLite による商品一覧表示アプリ。

## 起動手順

### 1. 依存パッケージのインストール

```bash
uv sync
```

### 2. データベースの初期化

```bash
uv run python init_db.py
```

> 既にDBが存在する場合は削除してから再実行する。
> ```bash
> rm data.db && uv run python init_db.py
> ```

### 3. サーバー起動

```bash
uv run uvicorn main:app --reload
```

### 4. ブラウザで確認

`http://localhost:8000` を開く。

## 機能

- カテゴリボタンによる商品フィルタリング（「全て」「食品」「電化製品」「日用品」）
- 商品カード形式表示（画像・商品名・価格・カテゴリ）
- htmx による非同期データ取得（ページリロードなし）

## ファイル構成

```
htmx_project/
├── main.py          # FastAPI アプリ本体
├── init_db.py       # DB初期化スクリプト
├── data.db          # SQLite データベース（init_db.py 実行後に生成）
├── static/
│   └── images/      # 商品画像（SVG）
├── pyproject.toml
└── uv.lock
```
