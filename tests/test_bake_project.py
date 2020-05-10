from loguru import logger 
from starlette.testclient import TestClient
from devtools import debug
from starlette.middleware.base import BaseHTTPMiddleware
db_url = "sqlite://"


def test_init(app):
    logger.success("hello")


def test_connection(app,client):
    # Do fancy stuff with the connection.
    # Note you will not need to close the connection. This is done
    # automatically when the scope (module) of the fixtures ends.
    resp = client.post(
        "api/meta/events",
        json={"name": "test","meta":{},"producer":"kula"},
    )
    debug(resp.json())