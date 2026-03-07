import sqlite3


def init_db():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    # 1. categories テーブル
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    # 2. items テーブル（category_id, image_path を追加）
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            value       TEXT NOT NULL,
            category_id INTEGER REFERENCES categories(id),
            image_path  TEXT
        )
    """)

    # 3. サンプルデータ
    cur.executemany(
        "INSERT INTO categories (name) VALUES (?)",
        [
            ("食品",),
            ("電化製品",),
            ("日用品",),
        ],
    )

    cur.executemany(
        "INSERT INTO items (name, value, category_id, image_path) VALUES (?, ?, ?, ?)",
        [
            ("りんご",         "200円",   1, "images/food_apple.svg"),
            ("バナナ",         "150円",   1, "images/food_banana.svg"),
            ("チョコレート",   "300円",   1, "images/food_choco.svg"),
            ("ポテトチップス", "180円",   1, "images/food_chips.svg"),
            ("スマートフォン", "80000円", 2, "images/elec_phone.svg"),
            ("イヤホン",       "5000円",  2, "images/elec_earphone.svg"),
            ("充電器",         "2000円",  2, "images/elec_charger.svg"),
            ("シャンプー",     "600円",   3, "images/daily_shampoo.svg"),
            ("歯ブラシ",       "300円",   3, "images/daily_toothbrush.svg"),
            ("タオル",         "800円",   3, "images/daily_towel.svg"),
        ],
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("DB初期化完了: data.db")
