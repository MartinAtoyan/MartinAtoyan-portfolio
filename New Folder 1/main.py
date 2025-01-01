# Entry point for the FastAPI application
from fastapi import FastAPI
from .database.session import engine
from .models.base import Base
from routers import auth

"""
Initializing the FastAPI app,
initializing the database if needed,
including routers
"""

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
