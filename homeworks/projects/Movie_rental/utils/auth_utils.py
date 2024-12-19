import os
from dotenv import load_dotenv
from fastapi import HTTPException, status
from jose import jwt, JWTError
from datetime import timedelta, datetime

load_dotenv()

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
EXPIRE = 30
ALGORITHM = "HS256"


def create_auth_token(payload_data:dict, secret_key:str = JWT_SECRET_KEY, alg:str = ALGORITHM, expires_in:int = EXPIRE):

    data = payload_data.copy()
    token = jwt.encode(payload_data, secret_key, alg)
    tmp = datetime.now() + timedelta(minutes=expires_in)

    data["exp"] = tmp

    return token


def decode_token(token:str):
    data = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
    
    username = data.get("username")

    try:
        return username
    
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=("Not found user with this token."))
    
    except JWTError:
        raise JWTError("Invalid token.")
    


# token  = create_auth_token({"username":"Bob", "email":"eexample@mail.comn"})
# print(token)
# print(decode_token(token)) 
# TEST IS WORKING


