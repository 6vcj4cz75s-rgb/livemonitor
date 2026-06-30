from fastapi import FastAPI

app = FastAPI()

CREATORS = [
    {"id": 1, "name": "creator_a", "status": "live"},
    {"id": 2, "name": "creator_b", "status": "offline"},
    {"id": 3, "name": "creator_c", "status": "live"},
]

@app.get("/")
def home():
    return {
        "message": "LiveMonitor running 🚀",
        "status": "ok"
    }

@app.get("/api/creators")
def get_creators():
    return {"data": CREATORS}

@app.get("/api/stats")
def stats():
    live = len([c for c in CREATORS if c["status"] == "live"])
    return {
        "total": len(CREATORS),
        "live": live,
        "offline": len(CREATORS) - live
    }
