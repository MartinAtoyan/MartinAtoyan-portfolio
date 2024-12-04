from fastapi import FastAPI, status, HTTPException, EmailStr, Field
from pydantic import BaseModel
from typing import Optional
import random
import json
import aiofiles
import os
from dotenv import load_dotenv
from errors import *

app = FastAPI()

load_dotenv()

HOST = os.environ("HOST")
PORT = int(os.environ("PORT"))

USERS_FILE = os.environ("USERS_FILE")
TASKS_FILE = os.environ("TASKS_FILE")

class User(BaseModel):
    name: str = Field(..., min_length = 1, description = "Name must be at least 2 characters.")
    email: EmailStr
    id:Optional[int] = Field(default_factory = lambda: random.randint(1, 1000))
    password: str = Field(..., min_length = 6, description = "Password must be at least 8 characters.")


class Task(BaseModel):
    title: str = Field(..., min_length = 1, description = "Title must be at least 1 character.")
    description : str 
    user_id : int


async def read_json(file):
    try:
        async with aiofiles.open(file, mode="r") as fl:
            data = await fl.read()
    except json.JSONDecodeError:
        raise FileError("Invalid file.")
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
    

async def write_json(file, data):
    async with aiofiles.open(file, "w") as fl:
        await fl.write(json.dumps(data, indent=2))


async def unpack_json(data):
    try:
        return await data.json()
    except json.JSONDecodeError:
        raise FileError("Invalid file.")
    
@app.post("/users")
async def create_user(data):

    user = await unpack_json(data)
    users = await read_json(USERS_FILE)
    users.append(user)
    await write_json(USERS_FILE, users)



@app.get("/users")
async def users():
    return await read_json(USERS_FILE)


@app.get("/users/{user_id}")
async def get_user_by_id(user_id:int):
    users = await read_json(USERS_FILE)

    flag = False
    for user in users:
        if user["id"] == user_id:
            flag = True
    
    if flag:
        return user
    else:
        raise NotFoundError("User not found by id.")
    


@app.put("/users/{user_id}")
async def update_user(user_id:int, data):
    data_for_update = await unpack_json(data)

    users = await read_json(USERS_FILE)

    flag = False
    for user in users:
        if user["id"] == user_id:
            flag = True
            break
    
    if flag:
        user.update(data_for_update)
        await write_json(USERS_FILE, users)
        return user
    else:
        raise NotFoundError("User not found by id.")
    


@app.delete("/users/{user_id}")
async def delete_user(user_id:int):
    users = await read_json(USERS_FILE)
    
    flag = False
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            flag = True
            break
    
    if flag:
        await write_json(USERS_FILE, user)
    


