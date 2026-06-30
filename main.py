from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "LiveMonitor running 🚀"}

@app.get("/api")
def api():
    return {
        "tiktok_lives": [
            {"user": "demo1", "live": False},
            {"user": "demo2", "live": True}
        ]
    }
