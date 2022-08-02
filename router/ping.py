from fastapi import APIRouter

router = APIRouter()


@router.get("/internal/ping", tags=["health"])
def ping():
    """Simple health check"""
    return "pong"