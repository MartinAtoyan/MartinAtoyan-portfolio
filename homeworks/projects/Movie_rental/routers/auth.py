from dotenv import load_dotenv
import os
from fastapi import APIRouter
from passlib.context import CryptContext
from ..models.schemas import User
import json
from ..utils.auth_utils import create_auth_token, decode_token
from fastapi import HTTPException, status

load_dotenv()
pwd_context = CryptContext(schemes='sha256_crypt')

router = APIRouter(prefix="/auth", tags=['auth'])

USERS_FILE = os.environ.get("USERS_FILE")

def get_users():
    try:
        with open(USERS_FILE, mode="r") as fl:
            return json.load(fl)
    except FileNotFoundError:
        return {}
    
def write_users(users: dict):
  try:
    with open(USERS_FILE, 'w') as file:
      json.dump(users, file, indent=2)
  except json.JSONDecodeError:
    pass

def hashed_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(password:str, hash_password:str) -> bool:
    return pwd_context.verify(password, hash_password)


@router.post("/register")
async def register_user(user: User):
    users = get_users()

    if user.username in users:
        raise "User already exists."
    
    hash_new_pws = hashed_password(user.password)
    new_user = {"username": user.username, "password": hash_new_pws, "email": user.email}
    users[user.username] = new_user
    write_users(users)

    return new_user


@router.post("/login")
async def login_user(user: User):
    users = get_users()
    user_from_db = users.get("username")
    
    if not user or not verify_password(user_from_db['password'], user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    
    token = create_auth_token(user)
    return user


