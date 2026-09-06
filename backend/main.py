from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "backend is alive"}

@app.get("/api/message")
def get_message():
    return {"message": "fastapi is alive"}

@app.get("/api/incidents")
def get_incidents():
    incidents = [
        {
            "id": 1,
            "title": "Communications system offline",
            "priority": "High",
            "status": "Open"
        },
        {
            "id": 2,
            "title": "Database connection failure",
            "priority": "Critical",
            "status": "In Progress"
        },
        {
            "id": 3,
            "title": "User unable to access dashboard",
            "priority": "Low",
            "status": "Assigned"
        }
    ]

    return incidents