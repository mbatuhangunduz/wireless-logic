from typing import Union
from .router import router
from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "Up and connected"}

@app.get("/env-check")
def env_check():
    return {
        "POSTGRES_USER": os.getenv("POSTGRES_USER"),
        "POSTGRES_DB": os.getenv("POSTGRES_DB"),
        "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("HOST")
    }

app.include_router(router, prefix="/api", tags=["items"])
