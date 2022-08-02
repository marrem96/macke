import pytest
from starlette.testclient import TestClient
from main import app
import json
from core import security
from typing import List, Tuple

DEFAULT_KEY = "secret_key"
INVALID_KEY = "invalid_key"

API_KEY_TEST: List[Tuple[any, bool]] = [
    ("secret_key", True),
    ("invalid-key", False),
    (None, False),
    ("", False),
]

@pytest.fixture
def test_client():
    client = TestClient(app)
    #app.dependency_overrides = {}
    return client

@pytest.mark.parametrize("api_key,expectation", API_KEY_TEST)
def test_default_security_key(api_key: str, expectation: bool):
    assert security.check_key(api_key) == expectation


def test_verify_missing_api_key(test_client):
    response = test_client.get("/test/")

    json_response = json.loads(response.text)
    assert response.status_code == 403, response.text
    assert json_response["detail"] == "An API key must be passed as query or header"


def test_verify_api_key_with_valid_query_param(test_client):
    response = test_client.get(f"/test/?api-key={DEFAULT_KEY}")

    json_response = json.loads(response.text)
    assert response.status_code == 200, response.text
    assert json_response["data"]["name"] == "Marcus"

def test_verify_api_key_with_invalid_query_param(test_client):
    response = test_client.get(f"/test/?api-key={INVALID_KEY}")

    json_response = json.loads(response.text)
    assert response.status_code == 403, response.text
    assert json_response["detail"] == "Invalid API key."


def test_verify_api_key_with_valid_header_param(test_client):
    response = test_client.get("/test/", headers={"api-key": DEFAULT_KEY})

    json_response = json.loads(response.text)
    assert response.status_code == 200, response.text
    assert json_response["data"]["name"] == "Marcus"


def test_verify_api_key_with_invalid_header_param(test_client):
    response = test_client.get("/test/", headers={"api-key": INVALID_KEY})

    json_response = json.loads(response.text)
    assert response.status_code == 403, response.text
    assert json_response["detail"] == "Invalid API key."
