import sys

import pytest
from fastapi import FastAPI
from app import config
from app.routes.api import router
from app.models import metadata
from fastapi.testclient import TestClient
import databases
from sqlalchemy import create_engine


#TODO implement test database generate

DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)

@pytest.fixture
def app():
    app = FastAPI()
    app.dependency_overrides[config.get_settings] = get_settings_override
    app.include_router(router, prefix="/api", tags=["api"])
    yield app

@pytest.fixture
def client(app):
    with TestClient(app) as c:
        yield c



def get_settings_override():
    return config.Settings(DATABASE_URL="sqlite://")

@pytest.fixture
def db():
    yield db

    # force reloading of module to clear global state

    try:
        del sys.modules["fastapi_sqlalchemy"]
    except KeyError:
        pass

    try:
        del sys.modules["fastapi_sqlalchemy.middleware"]
    except KeyError:
        pass