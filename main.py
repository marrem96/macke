import os

from fastapi_versioning import VersionedFastAPI
from fastapi import APIRouter
from fastapi import Security
import main2


from fastapi import FastAPI, APIRouter, Depends, Security
from decouple import config
from starlette.middleware.cors import CORSMiddleware

from core.security import verify_api_key
from router import testRouter, ping

dependencies = [Depends(verify_api_key)]
#dependencies = {}


secure_router = APIRouter(dependencies=dependencies)
secure_router.include_router(testRouter.router)


#app = FastAPI(title="test", description="test", dependencies)

app = FastAPI(title="test", description="test")


app.include_router(secure_router)
app.include_router(ping.router)

from pathlib import Path


def getssh():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"

import requests


def get_json(url):
    """Takes a URL, and returns the JSON."""
    r = requests.get(url)
    return r.json()


def example_2_monkeypatch(str1, str2):
    return main2.addStrings(str1, str2)


def example_1_monkeypatch():
    current_path = os.getcwd()
    return current_path
print("HEEEEEE")
print(example_1_monkeypatch())
#root_path = config("ROOT_PATH", default="")
#version_app = VersionedFastAPI(app, root_path=root_path)

print(example_2_monkeypatch("hej", "pa"))
#@app.get("/test/", dependencies=dependencies)
#@router.get("/test/")
#def index():
#    return {'data': {'name': 'Marcus'}}

#@app.get('/')
#async def index():
#    return {'data': {'name': 'Marcus'}}

"""
@app.get('/blog')
@version(1, 0)
def index(limit, published: bool):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


class Blog(BaseModel):
    title: str
    body: str
    temp: bool


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"Blog is created with title as {request.title}"}


@app.get('/about/')
async def about(id: Union[int, None] = None):
    return {'data': id}



async def common_parameters(q: Union[str, None] = None, skip: int = 0,
                            limit: int = 100
                            ):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/", tags = ["hej"], summary="Test summary",
         description="Test description")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


client = TestClient(app)


async def override_dependency(q: Union[str, None] = None):
    return {"q": q, "skip": 5, "limit": 10}


app.dependency_overrides[common_parameters] = override_dependency


def test_override_in_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Items!",
        "params": {"q": None, "skip": 5, "limit": 10},
    }
"""

"""
from fastapi import Depends, FastAPI, Header, HTTPException


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
"""