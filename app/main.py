from fastapi import FastAPI

app = FastAPI(title = "Enterprise AI Platform")

@app.get("/")
async def root():
    return {"Message": "API is up and running!"}