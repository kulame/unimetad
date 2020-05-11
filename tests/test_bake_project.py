from loguru import logger 
from starlette.testclient import TestClient
from devtools import debug
from starlette.middleware.base import BaseHTTPMiddleware




def test_connection(client):
    # Do fancy stuff with the connection.
    # Note you will not need to close the connection. This is done
    # automatically when the scope (module) of the fixtures ends.
        
    schema = {
        'doc': 'A weather reading.',
        'name': 'Weather',
        'namespace': 'test',
        'type': 'record',
        'fields': [
            {'name': 'station', 'type': 'string'},
            {'name': 'time', 'type': 'long'},
            {'name': 'temp', 'type': 'int'},
        ],
    }

    resp = client.post(
        "api/meta/events",
        json={"name": "test","meta":schema,"producer":"kula"},
    )
    debug(resp.json())