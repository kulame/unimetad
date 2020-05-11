import sys

import pytest
from fastapi import FastAPI
from app.config import get_settings
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

database_url = "sqlite:///./test.db"
def get_settings_override():
    settings = get_settings()
    settings['DATABASE_URL'] = database_url
    return settings

def db():  
    database = databases.Database(database_url, force_rollback=True) 
    engine = create_engine(
    database_url, connect_args={"check_same_thread": False}
    )
    metadata.create_all(engine)
 
    return database


app.dependency_overrides[get_settings] = get_settings_override
    



@pytest.fixture
def client():
    app.dependency_overrides[get_db] = db
    with TestClient(app) as c:
        yield c
        app.dependency_overrides = {}


