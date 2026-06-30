from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os
import psycopg2

app = FastAPI()

DATABASE_URL = os.environ.get("DATABASE_URL")


def db():
    return psycopg2.connect(DATABASE_URL)


# INIT DB
conn = db()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);
""")

conn.commit()
cur.close()
conn.close()


@app.get("/", response_class=HTMLResponse)
def home():
    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT name FROM users")
    users = cur.fetchall()

    cur.close()
    conn.close()

    html = """
    <html>
    <head>
        <title>LIVE DASHBOARD MVP</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

    <body style="font-family:Arial;text-align:center;padding:20px;background:#111;color:white;">

        <h2>🚀 LIVE DASHBOARD MVP</h2>

        <form action="/add" method="post">
            <input name="name" placeholder="username">
            <button>Add</button>
        </form>

        <h3>Users</h3>
        <ul>
    """

    for u in users:
        name = u[0]
        html += f"""
        <li>
            @{name}
            <button onclick="window.open('https://www.tiktok.com/@{name}/live')">
                OPEN LIVE
            </button>
        </li>
        """

    html += """
        </ul>

        <script>
        setInterval(()=>location.reload(), 8000);
        </script>

    </body>
    </html>
    """

    return html


@app.post("/add")
def add(name: str = Form(...)):
    conn = db()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name) VALUES (%s) ON CONFLICT DO NOTHING", (name,))
    conn.commit()

    cur.close()
    conn.close()

    return {"ok": True}
