
from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router

app =FastAPI(title=settings.app_name)

app.include_router(router)
# karsilama ekrani
@app.get("/")
async def root():
    return {
        "message": f"{settings.app_name} is running in {settings.env} environment."
    }
