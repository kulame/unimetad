import sys

import pytest
from fastapi import FastAPI
from app import config
from app.main import app
from app.routes.api import router
from app.models import get_db, metadata
from fastapi.testclient import TestClient
import databases
from sqlalchemy import create_engine

#TODO implement test database generate



# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL, force_rollback=True)

def db():   
    engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
    )
    metadata.create_all(engine)
 
    return database

@pytest.fixture
def client():
    app.dependency_overrides[get_db] = db
    with TestClient(app) as c:
        yield c
        app.dependency_overrides = {}


