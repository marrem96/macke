"""System module."""
from fastapi import Security
from fastapi.security import APIKeyHeader, APIKeyQuery
from starlette.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from decouple import config

API_KEY_NAME = "api-key"
api_key_query = APIKeyQuery(
    name=API_KEY_NAME, scheme_name="API key query", auto_error=False
)
api_key_header = APIKeyHeader(
    name=API_KEY_NAME, scheme_name="API key header", auto_error=False
)


def check_key(key: str):
    """
    Check key
    """
    return key == config("API_KEY_SECRET", default="secret_key", cast=str)


def verify_api_key(
        query_param: str = Security(api_key_query),
        header_param: str = Security(api_key_header),
):
    """
    Verify
    """
    if config("USE_API_KEY", default=True, cast=bool):
        if not query_param and not header_param:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail="An API key must be passed as query or header",
            )

        if query_param and check_key(query_param):
            return query_param

        if header_param and check_key(header_param):
            return header_param

        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid API key.")
    # API key verification disabled
    return None
