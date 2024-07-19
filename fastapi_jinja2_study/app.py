from fastapi import FastAPI
from alembic

app = FastAPI()





@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
