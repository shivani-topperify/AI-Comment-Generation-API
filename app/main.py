from fastapi import FastAPI

from app import models
from app.database import Base, engine
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Comment Generation API",
    version="1.0.0",
    description="API for generating social media comment drafts"
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "AI Comment Generation API is running"}