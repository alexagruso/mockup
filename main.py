from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import random

app = FastAPI()

app.mount("/front", StaticFiles(directory="frontend/public",
          html=True), name="front")


@app.get("/rand")
async def rand():
    return random.randint(0, 100)


@app.get("/")
async def front():
    return RedirectResponse(url="front")
