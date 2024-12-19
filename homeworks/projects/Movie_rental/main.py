import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
import os
load_dotenv()

from .routers.auth import router as auth_router
from .routers.movies import router as movies_router
from .routers.rentals import router as rentals_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(movies_router)
app.include_router(rentals_router)

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT"))
    HOST = os.environ.get("HOST")
    uvicorn.run("main:app", host=HOST, port=PORT)
