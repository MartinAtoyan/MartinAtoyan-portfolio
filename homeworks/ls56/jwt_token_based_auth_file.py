import jwt
from datetime import timezone, timedelta, datetime
import secrets

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"


def create_auth_token(payload_data:dict, secret_key:str, alg:str, expires_in:int = 10):

    data = payload_data.copy()
    token = jwt.encode(payload_data, secret_key, alg)
    tmp = datetime.now() + timedelta(minutes=expires_in)

    data["exp"] = tmp

    return token


def verify_token(token:str):
    username = jwt.decode(token, SECRET_KEY, ALGORITHM)
    return username


data = {
    "username":'Abo',
    "user_id":57,
}


token = create_auth_token(data, SECRET_KEY, ALGORITHM)
print(token)
print(verify_token(token))
