import json 
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from errors import *

pwd_context = CryptContext(schemes='sha256_crypt')

load_dotenv()
USERS_FILE = os.environ.get("USERS_FILE")
LOGS_FILE = os.environ.get("LOGS_FILE")

def get_users():
    try:
        with open(USERS_FILE, mode="r") as fl:
            return json.load(fl)
    except FileNotFoundError:
        return {}
    

def save_users(users):
    try:
        with open(USERS_FILE, mode="w") as fl:
            json.dump(users, fl, indent=2)
    except json.JSONDecodeError:
        raise "Invalid file."
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
    

def hashed_password(password):
    return pwd_context.hash(password)


def register_user(username, password):
    users = get_users()
    if username in users:
        return False
    
    hashed_pw = hashed_password(password)
    users[username] = {"username": username, "password": hashed_pw}

    save_users(users)
    log_event('registration', username, 'successfully')
    return True



def log_event(event, username, status=None):
    try:
        with open(LOGS_FILE, 'r') as fl:
            logs = json.load(fl)
    except FileNotFoundError:
        logs = []

    log_entry = {
        "event": event,
        "username": username,
    }

    if status is not None:
        log_entry["status"] = status

    logs.append(log_entry)

    with open(LOGS_FILE, 'w') as fl:
        json.dump(logs, fl, indent=2)

    
def verify_user(username, password):
    users = get_users()
    if username in users and pwd_context.verify(password, users[username]["password"]):
        log_event("login", username, "successfully")
        return True
    else:
        log_event("login", username, "fail")
        return False
    
