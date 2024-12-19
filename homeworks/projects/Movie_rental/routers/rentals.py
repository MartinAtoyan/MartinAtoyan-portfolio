from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import List, Dict
from ..models.schemas import Rental
from ..utils.auth_utils import decode_token
from .movies import movies_db
from dotenv import load_dotenv
import os
import json
load_dotenv()

RENTAL_FILE = os.environ.get("RENTAL_FILE")

router = APIRouter(prefix="/rentals", tags=["rentals"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_rental():
    try:
        with open(RENTAL_FILE, mode="r") as fl:
            return json.load(fl)
    except FileNotFoundError:
        return {}
    
def write_rental(movies: dict):
  try:
    with open(RENTAL_FILE, 'w') as file:
      json.dump(movies, file, indent=2)
  except json.JSONDecodeError:
    pass


@router.get("/")
async def get_rentals(token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    rental = get_rental()
    return rental    


@router.post("/")
async def rent_movie(rental_data: Rental, token: str = Depends(oauth2_scheme)):
    username = decode_token(token)

    if rental_data.movie not in movies_db:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    rental = get_rental()


    new_rental ={"username" : {
        "user": username,
        "movie_id": rental_data.movie_id,
        "rental_duration": rental_data.rental_duration
    }}

    rental.update[new_rental] 

    write_rental(new_rental)

    return new_rental

