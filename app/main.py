from typing import Union
from .router import router
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "Up and connected"}

app.include_router(router, prefix="/api", tags=["items"])
