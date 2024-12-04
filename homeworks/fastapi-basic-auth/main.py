from fastapi import FastAPI, Request, Depends,status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from users_db import log_event
from auth import *
from users_db import log_event
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def get_username(request: Request):
    return request.cookies.get("username")


@app.get("/login")
async def login_get_route(request: Request):
    return await login_get(request)

@app.post("/login")
async def login_post_route(request: Request):
    return await login_post(request)

@app.get("/register")
async def register_get_route(request: Request):
    return await register_get(request)

@app.post("/register")
async def register_post_route(request: Request):
    return await register_post(request)

@app.get("/logout")
async def logout_route(request: Request):
    return await logout(request)

@app.get("/")
def index():
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)

@app.get("/secure")
def secure_page(request: Request, username: str = Depends(get_username)):
    if username:
        log_event("secure_page_access", username, "logged out")
        return templates.TemplateResponse("secure.html", {"request": request, "username": username})
    else:
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)



if __name__ == "__main__":
    PORT = int(os.environ.get("PORT"))
    uvicorn.run("main:app", host="127.0.0.1", port=PORT, reload=True)

