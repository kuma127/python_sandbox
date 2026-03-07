# main.py
import sqlite3

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_root():
    return HTMLResponse("""
        <html>
          <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
            <script src="https://unpkg.com/htmx.org@1.9.10"></script>
          </head>
          <body>
            <main class="container">
              <h1>商品一覧</h1>
              <div id="categories"
                   hx-get="/api/categories"
                   hx-trigger="load"
                   hx-swap="innerHTML">
              </div>
              <div id="result"></div>
            </main>
          </body>
        </html>
    """)


@app.get("/api/categories")
async def get_categories():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM categories")
    categories = cur.fetchall()
    conn.close()

    buttons = '<button hx-get="/api/data" hx-target="#result" hx-swap="innerHTML">全て</button> '
    for cat in categories:
        buttons += f'<button hx-get="/api/data?category_id={cat[0]}" hx-target="#result" hx-swap="innerHTML">{cat[1]}</button> '
    return HTMLResponse(buttons)


@app.get("/api/data")
async def get_data(category_id: int | None = None):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    if category_id is None:
        cur.execute("""
            SELECT items.id, items.name, items.value, categories.name, items.image_path
            FROM items
            LEFT JOIN categories ON items.category_id = categories.id
        """)
    else:
        cur.execute("""
            SELECT items.id, items.name, items.value, categories.name, items.image_path
            FROM items
            LEFT JOIN categories ON items.category_id = categories.id
            WHERE items.category_id = ?
        """, (category_id,))
    rows = cur.fetchall()
    conn.close()

    def card(r):
        img = f'<img src="/static/{r[4]}" alt="{r[1]}">' if r[4] else ""
        return f"""<article>
          {img}
          <header>{r[1]}</header>
          <p>価格: {r[2]}</p>
          <footer>{r[3] or '未分類'}</footer>
        </article>"""

    def chunk(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    rows_html = "".join(
        f'<div class="grid">{"".join(card(r) for r in group)}</div>'
        for group in chunk(rows, 4)
    )
    return HTMLResponse(rows_html)
