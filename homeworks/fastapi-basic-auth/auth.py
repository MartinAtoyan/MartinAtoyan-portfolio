from fastapi import Request, Form, status
from fastapi.responses import RedirectResponse
from users_db import verify_user, register_user
from fastapi.templating import Jinja2Templates
# from starlette.status import HTTP_302_FOUND

templates = Jinja2Templates(directory="templates")

async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

async def login_post(request: Request):
    form = await request.form()
    username = form.get("username")
    password = form.get("password")

    if verify_user(username, password):
        response = RedirectResponse(url="/secure", status_code=status.HTTP_302_FOUND)
        response.set_cookie(key="username", value=username)
        return response
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

async def register_get(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

async def register_post(request: Request):
    form = await request.form()
    username = form.get("username")
    password = form.get("password")

    if register_user(username, password):
        return templates.TemplateResponse("login.html", {"request": request})
    else:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Username already exists"})

async def logout(request: Request):
    response = RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    response.delete_cookie(key="username")
    return response
