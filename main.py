from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

users = []

@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <html>
    <head>
        <title>TikTok Live Tool</title>
    </head>
    <body style="font-family: Arial; text-align:center; padding:20px;">
        <h1>🎯 TikTok Live Tool</h1>

        <form action="/add" method="get">
            <input name="user" placeholder="Nhập username TikTok" />
            <button type="submit">Thêm</button>
        </form>

        <h2>Danh sách:</h2>
        <ul>
    """

    for u in users:
        html += f'<li>@{u} - <a href="https://www.tiktok.com/@{u}/live" target="_blank">Mở Live</a></li>'

    html += """
        </ul>
    </body>
    </html>
    """
    return html

@app.get("/add")
def add(user: str):
    if user not in users:
        users.append(user)
    return {"message": "added", "user": user}
