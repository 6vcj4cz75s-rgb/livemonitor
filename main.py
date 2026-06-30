from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Live Tool</title>
    </head>
    <body style="font-family:Arial; text-align:center; padding:40px;">
        <h1>🔥 TikTok Live Tool</h1>

        <input id="u" placeholder="Nhập username TikTok"/>
        <button onclick="openLive()">Mở Live</button>

        <script>
        function openLive(){
            let u = document.getElementById('u').value;
            if(u){
                window.open('https://www.tiktok.com/@' + u + '/live', '_blank');
            }
        }
        </script>
    </body>
    </html>
    """
