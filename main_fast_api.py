import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    mode = 'DEBUG'
    if ('MODE' in os.environ.keys()):
        mode = os.environ['MODE']
    return {"mode": mode}

