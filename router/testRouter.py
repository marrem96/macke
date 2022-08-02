from fastapi import APIRouter
from fastapi import Security

router = APIRouter()

from fastapi_versioning import VersionedFastAPI

from fastapi import FastAPI, APIRouter, Depends
from decouple import config
from starlette.middleware.cors import CORSMiddleware

from core.security import verify_api_key


#@router.get("/test/", dependencies=[Security(verify_api_key)])
#@router.get("/test/", dependencies=[Depends(verify_api_key)])
@router.get("/test/")
def index():
    return {'data': {'name': 'Marcus'}}
