from fastapi import APIRouter, Depends
from ..models.schemas import Movie
from ..utils.auth_utils import decode_token
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os
import json
load_dotenv()

MOVIES_FILE = os.environ.get("MOVIES_FILE")

router = APIRouter(prefix="/movies", tags=["movies"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

movie_counter = 1

def get_movies():
    try:
        with open(MOVIES_FILE, mode="r") as fl:
            return json.load(fl)
    except FileNotFoundError:
        return {}
    
def write_movies(movies: dict):
  try:
    with open(MOVIES_FILE, 'w') as file:
      json.dump(movies, file, indent=2)
  except json.JSONDecodeError:
    pass

@router.get("/")
async def list_movies():
    movies = get_movies()
    return movies

@router.post("/")
async def create_movie(movie_data: Movie, token: str = Depends(oauth2_scheme)):
    decode_token(token)
    movies = get_movies()

    new_movie = {"title": movie_data.title, "genre": movie_data.genre, "rating": movie_data.rating}

    movies["title"] = new_movie

    write_movies(movies)

    return new_movie


