from fastapi import FastAPI

from app.routes.roadmap import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {"status": "running"}