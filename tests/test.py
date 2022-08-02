import pytest

from main import app
from starlette.testclient import TestClient

client = TestClient(app)

def test_ping():
    # client = TestClient(version_app)
    response = client.get("/")
    # print(response.text)
    assert response.status_code == 200, response.text
    print(type(response))
    print(type(response.text)) #str
    print(type(response.json()["data"]))
    assert response.json() == {'data': {'name': 'Marcus'}}
    assert response.json()["data"]["name"] == "Marcus"