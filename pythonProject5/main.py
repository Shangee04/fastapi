from fastapi import FastAPI
import uvicorn
from scripts.core.services.service_item import app

app_main = FastAPI()
app_main.include_router(app)

if __name__ == "__main__":
    uvicorn.run("main:app_main")

