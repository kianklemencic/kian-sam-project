from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "backend is alive"}

@app.get("/api/message")
def get_message():
    return {"message": "fastapi is alive"}