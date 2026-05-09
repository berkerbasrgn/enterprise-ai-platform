from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
async def root():
    return {
        "Message": f"{settings.app_name} is up and running in {settings.env}!"
    }