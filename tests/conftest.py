import sys

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient
from app import config
from app.models import metadata
from app.routes.api import router

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


@pytest.fixture
def DBSessionMiddleware():
    from fastapi_sqlalchemy import DBSessionMiddleware

    yield DBSessionMiddleware


def get_settings_override():
    return config.Settings(DATABASE_URL="sqlite://")

@pytest.fixture
def db():
    from fastapi_sqlalchemy import db
    metadata.create_all(db)
    
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