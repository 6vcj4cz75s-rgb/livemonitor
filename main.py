from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

users = ["tiktok1", "tiktok2", "tiktok3"]

@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <html>
    <head>
        <title>TikTok Live Tool</title>
    </head>

    <body style="font-family:Arial; text-align:center; padding:30px;">

        <h1>🔥 TikTok Live Tool</h1>

        <input id="u" placeholder="Nhập username TikTok"/>
        <button onclick="addUser()">Thêm</button>

        <button style="margin-left:10px; background:red; color:white;"
            onclick="openAll()">Open All Live</button>

        <h2>📌 Danh sách</h2>
        <ul>
    """

    for u in users:
        html += f"""
        <li>
            @{u}
            <button onclick="openLive('{u}')">Mở Live</button>
        </li>
        """

    html += """
        </ul>

        <script>
        function openLive(u){
            window.open('https://www.tiktok.com/@' + u + '/live', '_blank');
        }

        function openAll(){
            let users = %s;
            users.forEach(u => {
                window.open('https://www.tiktok.com/@' + u + '/live', '_blank');
            });
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
    """ % users

    return html


@app.get("/add")
def add(user: str):
    if user not in users:
        users.append(user)
    return {"message": "added", "user": user}
