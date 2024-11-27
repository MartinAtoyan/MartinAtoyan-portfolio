from fastapi import FastAPI, HTTPException, status, Request
import json
from errors import *
import aiofiles


app = FastAPI()

USERS_FILE = "homeworks/ls53/users.json"
TASKS_FILE = "homeworks/ls53/tasks.json"

async def read_json(file):
    try: 
        async with aiofiles.open(file, mode="r") as fl:
            data = await fl.read()
            return json.loads(data)
    except json.JSONDecodeError:
        raise FileError("Invalid file.")
    except FileNotFoundError:
        raise FileError("File not found.")
    

    
async def write_json(file, data):
    async with aiofiles.open(file, mode="w") as fl:
        await fl.write(json.dumps(data, indent=2))

        

async def get_next_id(data):
    if data:
        return max(item["id"] for item in data) + 1
    return 1



def validator_for_user(user: dict):
    
    if not isinstance(user, dict):
        raise ValidationError("User's type must be dict.")

    if not isinstance(user["name"], str):
        raise ValidationError("User's name must be string.")
    
    if "@" not in user["email"]:
        raise ValidationError("User's email must contain '@'.")
    
    if len(user["password"]) < 6:
        raise ValidationError("User's password must be at least than 6 characters.")



def validator_for_tasks(task:dict, users):
    if not isinstance(task, dict):
        raise ValidationError("User's task's type must be dict.") 
    
    if not isinstance(task["title"], str) and len(task["title"]) < 1:
        raise ValidationError("Task must be at least 1 character text.")
    
    if not any(user["id"] == task["user_id"] for user in users):
        raise ValidationError(f"Invalid 'user_id': There isn't user with {task["user_id"]} ID")



async def unpack_json(data: Request):
    try:
        # content = await data.body()
        # return json.loads(content)
        return await data.json()
    except json.JSONDecodeError:
        raise ValidationError("Invalid file.")
    
@app.post("/users")
async def create_user(data: Request):
    
    user = await unpack_json(data)
    validator_for_user(user)

    users = await read_json(USERS_FILE)
    user["id"] = await get_next_id(users)
    
    users.append(user)
    await write_json(USERS_FILE, users)
    
    return user

@app.get("/users")
async def users():
    return await read_json(USERS_FILE)

@app.get("/users/{user_id}")
async def get_user_by_id(user_id:int):
    users = await read_json(USERS_FILE)

    flag = None
    for user in users:
        if user["id"] == user_id:
            flag = True
    
    if flag:
        return user
    else:
        raise NotFoundError(f"Not found user by id ({user_id}).")


@app.put("/users/{user_id}")
async def update_user(user_id:int, data:Request):
    update_data = await unpack_json(data)

    validator_for_user(update_data)

    users = await read_json(USERS_FILE)

    for user in users:
        if user["id"] == user_id:
            user.update(update_data)
            await write_json(USERS_FILE, users)
            return user
    
    raise NotFoundError(f"Not found user by ID{user_id}.")


@app.delete("users/{user_id}")
async def delete_user(user_id:int):
    
    users = await read_json(USERS_FILE)

    flag = None

    for user in users:
        if user["id"] == user_id:
            flag = True

    if flag:
        users.remove(user)
        await write_json(USERS_FILE, users)
        return f"User with {user_id} ID removed from user's list."    
    else:
        raise NotFoundError(f"Not found user with {user_id} ID.")



@app.post("/tasks")
async def create_task(data: Request):

    task = await unpack_json(data)
    users = await read_json(USERS_FILE)

    validator_for_tasks(task, users)

    tasks = await read_json(TASKS_FILE)
    task["id"] = await get_next_id(tasks)

    tasks.append(task)

    await write_json(TASKS_FILE, tasks)
    return task



@app.get("/tasks")
def get_task_by_id(task_id:int):

    tasks = unpack_json(TASKS_FILE)
    flag = False

    for task in tasks:
        if task["id"] == task_id:
            flag = True
    
    if flag:
        return task
    else:
        return NotFoundError(f"Task with ID {task_id} not found.")
    


@app.put("/tasks/{task_id}")
async def update_task(task_id:int, data:Request):
    update_data = await unpack_json(data)

    tasks = await read_json(TASKS_FILE)
    users  = await read_json(USERS_FILE)

    validator_for_tasks(update_data, users)

    for task in tasks:
        if task["id"] == task_id:
            task.update(update_data)
            await write_json(TASKS_FILE, task)
            return task
        
    raise NotFoundError(f"Task with ID {task_id} not found.")



@app.delete("/tasks/{user_id}")
async def delete_task(task_id:int):
    tasks = await read_json(TASKS_FILE)

    flag = False

    for task in tasks:
        if task["id"] == task_id:
            flag = True

    if flag:
        tasks.remove(tasks)
        return "task removed successfuly."
    else:
        raise NotFoundError(f"Task with ID {task_id} not found.")



@app.post("/register")
async def register_user(data:Request):
    return await create_user(data)



@app.post("/login")
async def login(data:Request):
    
    data = await unpack_json(data)
    email = data["email"]
    password = data["password"]

    users = await read_json(USERS_FILE)

    flag = False

    for user in users:
        if user["email"] == email and user["password"] == password:
            flag = True

    if flag:
        return "You login in your account."
    else:
        raise "Please check your email or password correction."
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)