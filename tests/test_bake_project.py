from loguru import logger 
from starlette.testclient import TestClient
from devtools import debug
from starlette.middleware.base import BaseHTTPMiddleware




def test_connection(client):
    # Do fancy stuff with the connection.
    # Note you will not need to close the connection. This is done
    # automatically when the scope (module) of the fixtures ends.
    resp = client.post(
        "api/meta/events",
        json={"name": "test","meta":{},"producer":"kula"},
    )
    debug(resp.json())