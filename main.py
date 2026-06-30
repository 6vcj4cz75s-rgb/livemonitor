from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import sqlite3

app = FastAPI()

# tạo database
conn = sqlite3.connect("data.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")
conn.commit()


@app.get("/", response_class=HTMLResponse)
def home():
    cur.execute("SELECT name FROM users")
    users = cur.fetchall()

    html = """
    <html>
    <head>
        <title>Live Tool DB</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

    <body style="font-family:Arial; text-align:center; padding:20px;">

        <h2>🔥 TikTok Live Tool + DATABASE</h2>

        <input id="u" placeholder="username">
        <button onclick="addUser()">Add</button>

        <h3>Danh sách</h3>
        <ul>
    """

    for u in users:
        name = u[0]
        html += f"""
        <li>
            @{name}
            <button onclick="openLive('{name}')">Open</button>
        </li>
        """

    html += """
        </ul>

        <script>
        function openLive(u){
            window.open('https://www.tiktok.com/@' + u + '/live', '_blank');
        }

        function addUser(){
            let u = document.getElementById('u').value;
            if(u){
                window.location.href = '/add?user=' + u;
            }
        }
        </script>

    </body>
    </html>
    """

    return html


@app.get("/add")
def add(user: str):
    cur.execute("INSERT INTO users (name) VALUES (?)", (user,))
    conn.commit()
    return {"ok": True, "user": user}
